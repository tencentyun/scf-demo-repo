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


class Block(AbstractModel):
    """區塊對象

    """

    def __init__(self):
        """
        :param BlockNum: 區塊編号
        :type BlockNum: int
        :param DataHash: 區塊Hash數值
        :type DataHash: str
        :param BlockId: 區塊ID，與區塊編号一直
        :type BlockId: int
        :param PreHash: 前一個區塊Hash（未使用）,與區塊Hash數值一直
        :type PreHash: str
        :param TxCount: 區塊内的交易數量
        :type TxCount: int
        """
        self.BlockNum = None
        self.DataHash = None
        self.BlockId = None
        self.PreHash = None
        self.TxCount = None


    def _deserialize(self, params):
        self.BlockNum = params.get("BlockNum")
        self.DataHash = params.get("DataHash")
        self.BlockId = params.get("BlockId")
        self.PreHash = params.get("PreHash")
        self.TxCount = params.get("TxCount")


class GetBlockListRequest(AbstractModel):
    """GetBlockList請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名稱，固定欄位：block
        :type Module: str
        :param Operation: 操作名稱，固定欄位：block_list
        :type Operation: str
        :param ChannelId: 通道ID，固定欄位：0
        :type ChannelId: int
        :param GroupId: 組織ID，固定欄位：0
        :type GroupId: int
        :param ChannelName: 需要查詢的通道名稱，可在通道詳情或清單中獲取
        :type ChannelName: str
        :param GroupName: 調用介面的組織名稱，可以在組織管理清單中獲取當前組織的名稱
        :type GroupName: str
        :param ClusterId: 區塊鏈網絡ID，可在區塊鏈網絡詳情或清單中獲取
        :type ClusterId: str
        :param Offset: 需要獲取的起始交易偏移
        :type Offset: int
        :param Limit: 需要獲取的交易數量
        :type Limit: int
        """
        self.Module = None
        self.Operation = None
        self.ChannelId = None
        self.GroupId = None
        self.ChannelName = None
        self.GroupName = None
        self.ClusterId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ChannelId = params.get("ChannelId")
        self.GroupId = params.get("GroupId")
        self.ChannelName = params.get("ChannelName")
        self.GroupName = params.get("GroupName")
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetBlockListResponse(AbstractModel):
    """GetBlockList返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 區塊數量
        :type TotalCount: int
        :param BlockList: 區塊清單
        :type BlockList: list of Block
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BlockList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BlockList") is not None:
            self.BlockList = []
            for item in params.get("BlockList"):
                obj = Block()
                obj._deserialize(item)
                self.BlockList.append(obj)
        self.RequestId = params.get("RequestId")


class GetClusterSummaryRequest(AbstractModel):
    """GetClusterSummary請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名稱，固定欄位：cluster_mng
        :type Module: str
        :param Operation: 操作名稱，固定欄位：cluster_summary
        :type Operation: str
        :param ClusterId: 區塊鏈網絡ID，可在區塊鏈網絡詳情或清單中獲取
        :type ClusterId: str
        :param GroupId: 組織ID，固定欄位：0
        :type GroupId: int
        :param GroupName: 調用介面的組織名稱，可以在組織管理清單中獲取當前組織的名稱
        :type GroupName: str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.GroupId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")


class GetClusterSummaryResponse(AbstractModel):
    """GetClusterSummary返回參數結構體

    """

    def __init__(self):
        """
        :param TotalChannelCount: 網絡通道總數量
        :type TotalChannelCount: int
        :param MyChannelCount: 當前組織創建的通道數量
        :type MyChannelCount: int
        :param OtherChannelCount: 其組織創建的通道數量
        :type OtherChannelCount: int
        :param JoinChannelCount: 當前組織加入的通道數量
        :type JoinChannelCount: int
        :param NoneChannelCount: 與當前組織無關的通道數量
        :type NoneChannelCount: int
        :param TotalPeerCount: 網絡節點總數量
        :type TotalPeerCount: int
        :param MyPeerCount: 當前組織創建的節點數量
        :type MyPeerCount: int
        :param OtherPeerCount: 其他組織創建的節點數量
        :type OtherPeerCount: int
        :param TotalGroupCount: 網絡組織總數量
        :type TotalGroupCount: int
        :param MyGroupCount: 當前組織創建的組織數量
        :type MyGroupCount: int
        :param OtherGroupCount: 其他組織創建的組織數量
        :type OtherGroupCount: int
        :param TotalChaincodeCount: 網絡智慧合約總數量
        :type TotalChaincodeCount: int
        :param RecentChaincodeCount: 最近7天發起的智慧合約數量
        :type RecentChaincodeCount: int
        :param MyChaincodeCount: 當前組織發起的智慧合約數量
        :type MyChaincodeCount: int
        :param OtherChaincodeCount: 其組織發起的智慧合約數量
        :type OtherChaincodeCount: int
        :param TotalCertCount: 當前組織的證書總數量
        :type TotalCertCount: int
        :param TlsCertCount: 頒發給當前組織的證書數量
        :type TlsCertCount: int
        :param PeerCertCount: 網絡背書節點證書數量
        :type PeerCertCount: int
        :param OrderCertCount: 網絡排序節點證書數量
        :type OrderCertCount: int
        :param ClientCertCount: 當前組織業務證書數量
        :type ClientCertCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalChannelCount = None
        self.MyChannelCount = None
        self.OtherChannelCount = None
        self.JoinChannelCount = None
        self.NoneChannelCount = None
        self.TotalPeerCount = None
        self.MyPeerCount = None
        self.OtherPeerCount = None
        self.TotalGroupCount = None
        self.MyGroupCount = None
        self.OtherGroupCount = None
        self.TotalChaincodeCount = None
        self.RecentChaincodeCount = None
        self.MyChaincodeCount = None
        self.OtherChaincodeCount = None
        self.TotalCertCount = None
        self.TlsCertCount = None
        self.PeerCertCount = None
        self.OrderCertCount = None
        self.ClientCertCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalChannelCount = params.get("TotalChannelCount")
        self.MyChannelCount = params.get("MyChannelCount")
        self.OtherChannelCount = params.get("OtherChannelCount")
        self.JoinChannelCount = params.get("JoinChannelCount")
        self.NoneChannelCount = params.get("NoneChannelCount")
        self.TotalPeerCount = params.get("TotalPeerCount")
        self.MyPeerCount = params.get("MyPeerCount")
        self.OtherPeerCount = params.get("OtherPeerCount")
        self.TotalGroupCount = params.get("TotalGroupCount")
        self.MyGroupCount = params.get("MyGroupCount")
        self.OtherGroupCount = params.get("OtherGroupCount")
        self.TotalChaincodeCount = params.get("TotalChaincodeCount")
        self.RecentChaincodeCount = params.get("RecentChaincodeCount")
        self.MyChaincodeCount = params.get("MyChaincodeCount")
        self.OtherChaincodeCount = params.get("OtherChaincodeCount")
        self.TotalCertCount = params.get("TotalCertCount")
        self.TlsCertCount = params.get("TlsCertCount")
        self.PeerCertCount = params.get("PeerCertCount")
        self.OrderCertCount = params.get("OrderCertCount")
        self.ClientCertCount = params.get("ClientCertCount")
        self.RequestId = params.get("RequestId")


class GetInvokeTxRequest(AbstractModel):
    """GetInvokeTx請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：transaction
        :type Module: str
        :param Operation: 操作名，固定欄位：query_txid
        :type Operation: str
        :param ClusterId: 區塊鏈網絡ID，可在區塊鏈網絡詳情或清單中獲取
        :type ClusterId: str
        :param ChannelName: 業務所屬通道名稱，可在通道詳情或清單中獲取
        :type ChannelName: str
        :param PeerName: 執行該查詢交易的節點名稱，可以在通道詳情中獲取該通道上的節點名稱極其所屬組織名稱
        :type PeerName: str
        :param PeerGroup: 執行該查詢交易的節點所屬組織名稱，可以在通道詳情中獲取該通道上的節點名稱極其所屬組織名稱
        :type PeerGroup: str
        :param TxId: 交易ID
        :type TxId: str
        :param GroupName: 調用合約的組織名稱，可以在組織管理清單中獲取當前組織的名稱
        :type GroupName: str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.ChannelName = None
        self.PeerName = None
        self.PeerGroup = None
        self.TxId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.ChannelName = params.get("ChannelName")
        self.PeerName = params.get("PeerName")
        self.PeerGroup = params.get("PeerGroup")
        self.TxId = params.get("TxId")
        self.GroupName = params.get("GroupName")


class GetInvokeTxResponse(AbstractModel):
    """GetInvokeTx返回參數結構體

    """

    def __init__(self):
        """
        :param TxValidationCode: 交易執行狀态碼
        :type TxValidationCode: int
        :param TxValidationMsg: 交易執行訊息
        :type TxValidationMsg: str
        :param BlockId: 交易所在區塊ID
        :type BlockId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TxValidationCode = None
        self.TxValidationMsg = None
        self.BlockId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TxValidationCode = params.get("TxValidationCode")
        self.TxValidationMsg = params.get("TxValidationMsg")
        self.BlockId = params.get("BlockId")
        self.RequestId = params.get("RequestId")


class GetLatesdTransactionListRequest(AbstractModel):
    """GetLatesdTransactionList請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名稱，固定欄位：transaction
        :type Module: str
        :param Operation: 操作名稱，固定欄位：latest_transaction_list
        :type Operation: str
        :param GroupId: 組織ID，固定欄位：0
        :type GroupId: int
        :param ChannelId: 通道ID，固定欄位：0
        :type ChannelId: int
        :param LatestBlockNumber: 獲取的最新交易的區塊數量，取值範圍1~5
        :type LatestBlockNumber: int
        :param GroupName: 調用介面的組織名稱，可以在組織管理清單中獲取當前組織的名稱
        :type GroupName: str
        :param ChannelName: 需要查詢的通道名稱，可在通道詳情或清單中獲取
        :type ChannelName: str
        :param ClusterId: 區塊鏈網絡ID，可在區塊鏈網絡詳情或清單中獲取
        :type ClusterId: str
        :param Offset: 需要獲取的起始交易偏移
        :type Offset: int
        :param Limit: 需要獲取的交易數量
        :type Limit: int
        """
        self.Module = None
        self.Operation = None
        self.GroupId = None
        self.ChannelId = None
        self.LatestBlockNumber = None
        self.GroupName = None
        self.ChannelName = None
        self.ClusterId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupId = params.get("GroupId")
        self.ChannelId = params.get("ChannelId")
        self.LatestBlockNumber = params.get("LatestBlockNumber")
        self.GroupName = params.get("GroupName")
        self.ChannelName = params.get("ChannelName")
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetLatesdTransactionListResponse(AbstractModel):
    """GetLatesdTransactionList返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 交易總數量
        :type TotalCount: int
        :param TransactionList: 交易清單
        :type TransactionList: list of TransactionItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TransactionList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TransactionList") is not None:
            self.TransactionList = []
            for item in params.get("TransactionList"):
                obj = TransactionItem()
                obj._deserialize(item)
                self.TransactionList.append(obj)
        self.RequestId = params.get("RequestId")


class InvokeRequest(AbstractModel):
    """Invoke請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：transaction
        :type Module: str
        :param Operation: 操作名，固定欄位：invoke
        :type Operation: str
        :param ClusterId: 區塊鏈網絡ID，可在區塊鏈網絡詳情或清單中獲取
        :type ClusterId: str
        :param ChaincodeName: 業務所屬智慧合約名稱，可在智慧合約詳情或清單中獲取
        :type ChaincodeName: str
        :param ChannelName: 業務所屬通道名稱，可在通道詳情或清單中獲取
        :type ChannelName: str
        :param Peers: 對該筆交易進行背書的節點清單（包括節點名稱和節點所屬組織名稱，詳見數據結構一節），可以在通道詳情中獲取該通道上的節點名稱極其所屬組織名稱
        :type Peers: list of PeerSet
        :param FuncName: 該筆交易需要調用的智慧合約中的函數名稱
        :type FuncName: str
        :param GroupName: 調用合約的組織名稱，可以在組織管理清單中獲取當前組織的名稱
        :type GroupName: str
        :param Args: 被調用的函數參數清單
        :type Args: list of str
        :param AsyncFlag: 同步調用标識，可選參數，值爲0或者不傳表示使用同步方法調用，調用後會等待交易執行後再返回執行結果；值爲1時表示使用異步方式調用Invoke，執行後會立即返回交易對應的Txid，後續需要通過GetInvokeTx這個API查詢該交易的執行結果。（對于邏輯較爲簡單的交易，可以使用同步模式；對于邏輯較爲複雜的交易，建議使用異步模式，否則容易導緻API因等待時間過長，返回等待超時）
        :type AsyncFlag: int
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.ChaincodeName = None
        self.ChannelName = None
        self.Peers = None
        self.FuncName = None
        self.GroupName = None
        self.Args = None
        self.AsyncFlag = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.ChaincodeName = params.get("ChaincodeName")
        self.ChannelName = params.get("ChannelName")
        if params.get("Peers") is not None:
            self.Peers = []
            for item in params.get("Peers"):
                obj = PeerSet()
                obj._deserialize(item)
                self.Peers.append(obj)
        self.FuncName = params.get("FuncName")
        self.GroupName = params.get("GroupName")
        self.Args = params.get("Args")
        self.AsyncFlag = params.get("AsyncFlag")


class InvokeResponse(AbstractModel):
    """Invoke返回參數結構體

    """

    def __init__(self):
        """
        :param Txid: 交易ID
        :type Txid: str
        :param Events: 交易執行結果
        :type Events: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Txid = None
        self.Events = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Txid = params.get("Txid")
        self.Events = params.get("Events")
        self.RequestId = params.get("RequestId")


class PeerSet(AbstractModel):
    """PeerSet

    """

    def __init__(self):
        """
        :param PeerName: 節點名稱
        :type PeerName: str
        :param OrgName: 組織名稱
        :type OrgName: str
        """
        self.PeerName = None
        self.OrgName = None


    def _deserialize(self, params):
        self.PeerName = params.get("PeerName")
        self.OrgName = params.get("OrgName")


class QueryRequest(AbstractModel):
    """Query請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：transaction
        :type Module: str
        :param Operation: 操作名，固定欄位：query
        :type Operation: str
        :param ClusterId: 區塊鏈網絡ID，可在區塊鏈網絡詳情或清單中獲取
        :type ClusterId: str
        :param ChaincodeName: 業務所屬智慧合約名稱，可在智慧合約詳情或清單中獲取
        :type ChaincodeName: str
        :param ChannelName: 業務所屬通道名稱，可在通道詳情或清單中獲取
        :type ChannelName: str
        :param Peers: 執行該查詢交易的節點清單（包括節點名稱和節點所屬組織名稱，詳見數據結構一節），可以在通道詳情中獲取該通道上的節點名稱極其所屬組織名稱
        :type Peers: list of PeerSet
        :param FuncName: 該筆交易查詢需要調用的智慧合約中的函數名稱
        :type FuncName: str
        :param GroupName: 調用合約的組織名稱，可以在組織管理清單中獲取當前組織的名稱
        :type GroupName: str
        :param Args: 被調用的函數參數清單
        :type Args: list of str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.ChaincodeName = None
        self.ChannelName = None
        self.Peers = None
        self.FuncName = None
        self.GroupName = None
        self.Args = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.ChaincodeName = params.get("ChaincodeName")
        self.ChannelName = params.get("ChannelName")
        if params.get("Peers") is not None:
            self.Peers = []
            for item in params.get("Peers"):
                obj = PeerSet()
                obj._deserialize(item)
                self.Peers.append(obj)
        self.FuncName = params.get("FuncName")
        self.GroupName = params.get("GroupName")
        self.Args = params.get("Args")


class QueryResponse(AbstractModel):
    """Query返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 查詢結果數據
        :type Data: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class TransactionItem(AbstractModel):
    """交易清單項訊息

    """

    def __init__(self):
        """
        :param TransactionId: 交易ID
        :type TransactionId: str
        :param TransactionHash: 交易hash
        :type TransactionHash: str
        :param CreateOrgName: 創建交易的組織名
        :type CreateOrgName: str
        :param BlockId: 交易所在區塊号
        :type BlockId: int
        :param TransactionType: 交易類型（普通交易和配置交易）
        :type TransactionType: str
        :param CreateTime: 交易創建時間
        :type CreateTime: str
        :param BlockHeight: 交易所在區塊高度
        :type BlockHeight: int
        :param TransactionStatus: 交易狀态
        :type TransactionStatus: str
        """
        self.TransactionId = None
        self.TransactionHash = None
        self.CreateOrgName = None
        self.BlockId = None
        self.TransactionType = None
        self.CreateTime = None
        self.BlockHeight = None
        self.TransactionStatus = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.TransactionHash = params.get("TransactionHash")
        self.CreateOrgName = params.get("CreateOrgName")
        self.BlockId = params.get("BlockId")
        self.TransactionType = params.get("TransactionType")
        self.CreateTime = params.get("CreateTime")
        self.BlockHeight = params.get("BlockHeight")
        self.TransactionStatus = params.get("TransactionStatus")