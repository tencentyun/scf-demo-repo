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


class ApplyUserCertRequest(AbstractModel):
    """ApplyUserCert請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：cert_mng
        :type Module: str
        :param Operation: 操作名，固定欄位：cert_apply_for_user
        :type Operation: str
        :param ClusterId: 區塊鏈網絡ID，可在區塊鏈網絡詳情或清單中獲取
        :type ClusterId: str
        :param GroupName: 申請證書的組織名稱，可以在組織管理清單中獲取當前組織的名稱
        :type GroupName: str
        :param UserIdentity: 用戶證書標識，用於標識用戶證書，要求由純小寫字母組成，長度小於10
        :type UserIdentity: str
        :param Applicant: 證書申請實體，使用Top Cloud 賬號實名認證的名稱
        :type Applicant: str
        :param IdentityNum: 證件號碼。如果Top Cloud 賬號對應的實名認證類型爲企業認證，填入“0”；如果Top Cloud 賬號對應的實名認證類型爲個人認證，填入個人身份證號碼
        :type IdentityNum: str
        :param CsrData: csr p10證書文件。需要用戶根據文件生成證書的CSR文件
        :type CsrData: str
        :param Notes: 證書備注訊息
        :type Notes: str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.GroupName = None
        self.UserIdentity = None
        self.Applicant = None
        self.IdentityNum = None
        self.CsrData = None
        self.Notes = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.GroupName = params.get("GroupName")
        self.UserIdentity = params.get("UserIdentity")
        self.Applicant = params.get("Applicant")
        self.IdentityNum = params.get("IdentityNum")
        self.CsrData = params.get("CsrData")
        self.Notes = params.get("Notes")


class ApplyUserCertResponse(AbstractModel):
    """ApplyUserCert返回參數結構體

    """

    def __init__(self):
        """
        :param CertId: 證書ID
        :type CertId: int
        :param CertDn: 證書DN
        :type CertDn: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertId = None
        self.CertDn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertDn = params.get("CertDn")
        self.RequestId = params.get("RequestId")


class BcosBlockObj(AbstractModel):
    """Bcos區塊對象

    """

    def __init__(self):
        """
        :param BlockHash: 區塊哈希
        :type BlockHash: str
        :param BlockNumber: 區塊高度
        :type BlockNumber: int
        :param BlockTimestamp: 區塊時間戳
        :type BlockTimestamp: str
        :param Sealer: 打包節點ID
        :type Sealer: str
        :param SealerIndex: 打包節點索引
        :type SealerIndex: int
        :param CreateTime: 記錄保存時間
        :type CreateTime: str
        :param TransCount: 交易數量
        :type TransCount: int
        :param ModifyTime: 記錄修改時間
        :type ModifyTime: str
        """
        self.BlockHash = None
        self.BlockNumber = None
        self.BlockTimestamp = None
        self.Sealer = None
        self.SealerIndex = None
        self.CreateTime = None
        self.TransCount = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.BlockHash = params.get("BlockHash")
        self.BlockNumber = params.get("BlockNumber")
        self.BlockTimestamp = params.get("BlockTimestamp")
        self.Sealer = params.get("Sealer")
        self.SealerIndex = params.get("SealerIndex")
        self.CreateTime = params.get("CreateTime")
        self.TransCount = params.get("TransCount")
        self.ModifyTime = params.get("ModifyTime")


class BcosTransInfo(AbstractModel):
    """Bcos交易訊息對象

    """

    def __init__(self):
        """
        :param BlockNumber: 所屬區塊高度
        :type BlockNumber: int
        :param BlockTimestamp: 區塊時間戳
        :type BlockTimestamp: str
        :param TransHash: 交易哈希
        :type TransHash: str
        :param TransFrom: 交易發起者
        :type TransFrom: str
        :param TransTo: 交易接收者
        :type TransTo: str
        :param CreateTime: 落庫時間
        :type CreateTime: str
        :param ModifyTime: 修改時間
        :type ModifyTime: str
        """
        self.BlockNumber = None
        self.BlockTimestamp = None
        self.TransHash = None
        self.TransFrom = None
        self.TransTo = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.BlockNumber = params.get("BlockNumber")
        self.BlockTimestamp = params.get("BlockTimestamp")
        self.TransHash = params.get("TransHash")
        self.TransFrom = params.get("TransFrom")
        self.TransTo = params.get("TransTo")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")


class Block(AbstractModel):
    """區塊對象

    """

    def __init__(self):
        """
        :param BlockNum: 區塊編號
        :type BlockNum: int
        :param DataHash: 區塊Hash數值
        :type DataHash: str
        :param BlockId: 區塊ID，與區塊編號一緻
        :type BlockId: int
        :param PreHash: 前一個區塊Hash（未使用）,與區塊Hash數值一緻
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


class BlockByNumberHandlerRequest(AbstractModel):
    """BlockByNumberHandler請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：block
        :type Module: str
        :param Operation: 操作名，固定欄位：block_by_number
        :type Operation: str
        :param GroupPk: 當前群組編號
        :type GroupPk: str
        :param BlockNumber: 區塊高度
        :type BlockNumber: int
        """
        self.Module = None
        self.Operation = None
        self.GroupPk = None
        self.BlockNumber = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupPk = params.get("GroupPk")
        self.BlockNumber = params.get("BlockNumber")


class BlockByNumberHandlerResponse(AbstractModel):
    """BlockByNumberHandler返回參數結構體

    """

    def __init__(self):
        """
        :param BlockJson: 返回區塊json字串
        :type BlockJson: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BlockJson = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BlockJson = params.get("BlockJson")
        self.RequestId = params.get("RequestId")


class DeployDynamicContractHandlerRequest(AbstractModel):
    """DeployDynamicContractHandler請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：contract
        :type Module: str
        :param Operation: 操作名，固定欄位：deploy_by_dynamic_contract
        :type Operation: str
        :param GroupPk: 群組編號
        :type GroupPk: str
        :param ContractName: 合約名稱
        :type ContractName: str
        :param AbiInfo: 合約編譯後的abi
        :type AbiInfo: str
        :param ByteCodeBin: 合約編譯後的binary
        :type ByteCodeBin: str
        :param ConstructorParams: 構造函數入參
        :type ConstructorParams: list of str
        """
        self.Module = None
        self.Operation = None
        self.GroupPk = None
        self.ContractName = None
        self.AbiInfo = None
        self.ByteCodeBin = None
        self.ConstructorParams = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupPk = params.get("GroupPk")
        self.ContractName = params.get("ContractName")
        self.AbiInfo = params.get("AbiInfo")
        self.ByteCodeBin = params.get("ByteCodeBin")
        self.ConstructorParams = params.get("ConstructorParams")


class DeployDynamicContractHandlerResponse(AbstractModel):
    """DeployDynamicContractHandler返回參數結構體

    """

    def __init__(self):
        """
        :param ContractAddress: 佈署成功返回的合約網址
        :type ContractAddress: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ContractAddress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ContractAddress = params.get("ContractAddress")
        self.RequestId = params.get("RequestId")


class DownloadUserCertRequest(AbstractModel):
    """DownloadUserCert請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：cert_mng
        :type Module: str
        :param Operation: 操作名，固定欄位：cert_download_for_user
        :type Operation: str
        :param CertId: 證書ID，可以在證書詳情頁面獲取
        :type CertId: int
        :param CertDn: 證書DN，可以在證書詳情頁面獲取
        :type CertDn: str
        :param ClusterId: 區塊鏈網絡ID，可在區塊鏈網絡詳情或清單中獲取
        :type ClusterId: str
        :param GroupName: 下載證書的組織名稱，可以在組織管理清單中獲取當前組織的名稱
        :type GroupName: str
        """
        self.Module = None
        self.Operation = None
        self.CertId = None
        self.CertDn = None
        self.ClusterId = None
        self.GroupName = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.CertId = params.get("CertId")
        self.CertDn = params.get("CertDn")
        self.ClusterId = params.get("ClusterId")
        self.GroupName = params.get("GroupName")


class DownloadUserCertResponse(AbstractModel):
    """DownloadUserCert返回參數結構體

    """

    def __init__(self):
        """
        :param CertName: 證書名稱
        :type CertName: str
        :param CertCtx: 證書内容
        :type CertCtx: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertName = None
        self.CertCtx = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertName = params.get("CertName")
        self.CertCtx = params.get("CertCtx")
        self.RequestId = params.get("RequestId")


class EndorserGroup(AbstractModel):
    """背書組織及其節點清單

    """

    def __init__(self):
        """
        :param EndorserGroupName: 背書組織名稱
        :type EndorserGroupName: str
        :param EndorserPeerList: 背書節點清單
        :type EndorserPeerList: list of str
        """
        self.EndorserGroupName = None
        self.EndorserPeerList = None


    def _deserialize(self, params):
        self.EndorserGroupName = params.get("EndorserGroupName")
        self.EndorserPeerList = params.get("EndorserPeerList")


class GetBlockListHandlerRequest(AbstractModel):
    """GetBlockListHandler請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：block
        :type Module: str
        :param Operation: 操作名，固定欄位：get_block_list
        :type Operation: str
        :param Offset: 記錄偏移數
        :type Offset: int
        :param Limit: 每頁記錄數
        :type Limit: int
        :param GroupPk: 當前群組編號
        :type GroupPk: str
        :param BlockHash: 區塊哈希
        :type BlockHash: str
        """
        self.Module = None
        self.Operation = None
        self.Offset = None
        self.Limit = None
        self.GroupPk = None
        self.BlockHash = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupPk = params.get("GroupPk")
        self.BlockHash = params.get("BlockHash")


class GetBlockListHandlerResponse(AbstractModel):
    """GetBlockListHandler返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總記錄數
        :type TotalCount: int
        :param GroupPk: 當前群組編號
        :type GroupPk: str
        :param List: 返回數據清單
        :type List: list of BcosBlockObj
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.GroupPk = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.GroupPk = params.get("GroupPk")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BcosBlockObj()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


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


class GetBlockTransactionListForUserRequest(AbstractModel):
    """GetBlockTransactionListForUser請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：transaction
        :type Module: str
        :param Operation: 操作名，固定欄位：block_transaction_list_for_user
        :type Operation: str
        :param ClusterId: 區塊鏈網絡ID，可在區塊鏈網絡詳情或清單中獲取
        :type ClusterId: str
        :param GroupName: 參與交易的組織名稱，可以在組織管理清單中獲取當前組織的名稱
        :type GroupName: str
        :param ChannelName: 業務所屬通道名稱，可在通道詳情或清單中獲取
        :type ChannelName: str
        :param BlockId: 區塊ID，通過GetInvokeTx介面可以獲取交易所在的區塊ID
        :type BlockId: int
        :param Offset: 查詢的交易清單起始偏移網址
        :type Offset: int
        :param Limit: 查詢的交易清單數量
        :type Limit: int
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.GroupName = None
        self.ChannelName = None
        self.BlockId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.GroupName = params.get("GroupName")
        self.ChannelName = params.get("ChannelName")
        self.BlockId = params.get("BlockId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetBlockTransactionListForUserResponse(AbstractModel):
    """GetBlockTransactionListForUser返回參數結構體

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
        :param JoinChannelCount: 當前組織加入的通道數量
        :type JoinChannelCount: int
        :param TotalPeerCount: 網絡節點總數量
        :type TotalPeerCount: int
        :param MyPeerCount: 當前組織創建的節點數量
        :type MyPeerCount: int
        :param OrderCount: 其他組織創建的節點數量
        :type OrderCount: int
        :param TotalGroupCount: 網絡組織總數量
        :type TotalGroupCount: int
        :param MyGroupCount: 當前組織創建的組織數量
        :type MyGroupCount: int
        :param TotalChaincodeCount: 網絡智慧合約總數量
        :type TotalChaincodeCount: int
        :param RecentChaincodeCount: 最近7天發起的智慧合約數量
        :type RecentChaincodeCount: int
        :param MyChaincodeCount: 當前組織發起的智慧合約數量
        :type MyChaincodeCount: int
        :param TotalCertCount: 當前組織的證書總數量
        :type TotalCertCount: int
        :param TlsCertCount: 頒發給當前組織的證書數量
        :type TlsCertCount: int
        :param PeerCertCount: 網絡背書節點證書數量
        :type PeerCertCount: int
        :param ClientCertCount: 當前組織業務證書數量
        :type ClientCertCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalChannelCount = None
        self.MyChannelCount = None
        self.JoinChannelCount = None
        self.TotalPeerCount = None
        self.MyPeerCount = None
        self.OrderCount = None
        self.TotalGroupCount = None
        self.MyGroupCount = None
        self.TotalChaincodeCount = None
        self.RecentChaincodeCount = None
        self.MyChaincodeCount = None
        self.TotalCertCount = None
        self.TlsCertCount = None
        self.PeerCertCount = None
        self.ClientCertCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalChannelCount = params.get("TotalChannelCount")
        self.MyChannelCount = params.get("MyChannelCount")
        self.JoinChannelCount = params.get("JoinChannelCount")
        self.TotalPeerCount = params.get("TotalPeerCount")
        self.MyPeerCount = params.get("MyPeerCount")
        self.OrderCount = params.get("OrderCount")
        self.TotalGroupCount = params.get("TotalGroupCount")
        self.MyGroupCount = params.get("MyGroupCount")
        self.TotalChaincodeCount = params.get("TotalChaincodeCount")
        self.RecentChaincodeCount = params.get("RecentChaincodeCount")
        self.MyChaincodeCount = params.get("MyChaincodeCount")
        self.TotalCertCount = params.get("TotalCertCount")
        self.TlsCertCount = params.get("TlsCertCount")
        self.PeerCertCount = params.get("PeerCertCount")
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


class GetTransByHashHandlerRequest(AbstractModel):
    """GetTransByHashHandler請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：transaction
        :type Module: str
        :param Operation: 操作名，固定欄位：get_trans_by_hash
        :type Operation: str
        :param GroupPk: 群組編號
        :type GroupPk: str
        :param TransHash: 交易哈希
        :type TransHash: str
        """
        self.Module = None
        self.Operation = None
        self.GroupPk = None
        self.TransHash = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupPk = params.get("GroupPk")
        self.TransHash = params.get("TransHash")


class GetTransByHashHandlerResponse(AbstractModel):
    """GetTransByHashHandler返回參數結構體

    """

    def __init__(self):
        """
        :param TransactionJson: 交易訊息json字串
        :type TransactionJson: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TransactionJson = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransactionJson = params.get("TransactionJson")
        self.RequestId = params.get("RequestId")


class GetTransListHandlerRequest(AbstractModel):
    """GetTransListHandler請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：transaction
        :type Module: str
        :param Operation: 操作名，固定欄位：get_trans_list
        :type Operation: str
        :param Offset: 記錄偏移量
        :type Offset: int
        :param Limit: 每頁記錄數
        :type Limit: int
        :param GroupPk: 群組編號
        :type GroupPk: str
        :param TransHash: 交易哈希
        :type TransHash: str
        """
        self.Module = None
        self.Operation = None
        self.Offset = None
        self.Limit = None
        self.GroupPk = None
        self.TransHash = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupPk = params.get("GroupPk")
        self.TransHash = params.get("TransHash")


class GetTransListHandlerResponse(AbstractModel):
    """GetTransListHandler返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總記錄數
        :type TotalCount: int
        :param GroupPk: 當前群組編號
        :type GroupPk: str
        :param List: 返回數據清單
        :type List: list of BcosTransInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.GroupPk = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.GroupPk = params.get("GroupPk")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BcosTransInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class GetTransactionDetailForUserRequest(AbstractModel):
    """GetTransactionDetailForUser請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：transaction
        :type Module: str
        :param Operation: 操作名，固定欄位：transaction_detail_for_user
        :type Operation: str
        :param ClusterId: 區塊鏈網絡ID，可在區塊鏈網絡詳情或清單中獲取
        :type ClusterId: str
        :param GroupName: 參與交易的組織名稱，可以在組織管理清單中獲取當前組織的名稱
        :type GroupName: str
        :param ChannelName: 業務所屬通道名稱，可在通道詳情或清單中獲取
        :type ChannelName: str
        :param BlockId: 區塊ID，通過GetInvokeTx介面可以獲取交易所在的區塊ID
        :type BlockId: int
        :param TransactionId: 交易ID，需要查詢的詳情的交易ID
        :type TransactionId: str
        """
        self.Module = None
        self.Operation = None
        self.ClusterId = None
        self.GroupName = None
        self.ChannelName = None
        self.BlockId = None
        self.TransactionId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ClusterId = params.get("ClusterId")
        self.GroupName = params.get("GroupName")
        self.ChannelName = params.get("ChannelName")
        self.BlockId = params.get("BlockId")
        self.TransactionId = params.get("TransactionId")


class GetTransactionDetailForUserResponse(AbstractModel):
    """GetTransactionDetailForUser返回參數結構體

    """

    def __init__(self):
        """
        :param TransactionId: 交易ID
        :type TransactionId: str
        :param TransactionHash: 交易hash
        :type TransactionHash: str
        :param CreateOrgName: 創建交易的組織名
        :type CreateOrgName: str
        :param TransactionType: 交易類型（普通交易和配置交易）
        :type TransactionType: str
        :param TransactionStatus: 交易狀态
        :type TransactionStatus: str
        :param CreateTime: 交易創建時間
        :type CreateTime: str
        :param TransactionData: 交易數據
        :type TransactionData: str
        :param BlockId: 交易所在區塊號
        :type BlockId: int
        :param BlockHash: 交易所在區塊哈希
        :type BlockHash: str
        :param BlockHeight: 交易所在區塊高度
        :type BlockHeight: int
        :param ChannelName: 通道名稱
        :type ChannelName: str
        :param ContractName: 交易所在合約名稱
        :type ContractName: str
        :param EndorserOrgList: 背書組織清單
        :type EndorserOrgList: list of EndorserGroup
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TransactionId = None
        self.TransactionHash = None
        self.CreateOrgName = None
        self.TransactionType = None
        self.TransactionStatus = None
        self.CreateTime = None
        self.TransactionData = None
        self.BlockId = None
        self.BlockHash = None
        self.BlockHeight = None
        self.ChannelName = None
        self.ContractName = None
        self.EndorserOrgList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransactionId = params.get("TransactionId")
        self.TransactionHash = params.get("TransactionHash")
        self.CreateOrgName = params.get("CreateOrgName")
        self.TransactionType = params.get("TransactionType")
        self.TransactionStatus = params.get("TransactionStatus")
        self.CreateTime = params.get("CreateTime")
        self.TransactionData = params.get("TransactionData")
        self.BlockId = params.get("BlockId")
        self.BlockHash = params.get("BlockHash")
        self.BlockHeight = params.get("BlockHeight")
        self.ChannelName = params.get("ChannelName")
        self.ContractName = params.get("ContractName")
        if params.get("EndorserOrgList") is not None:
            self.EndorserOrgList = []
            for item in params.get("EndorserOrgList"):
                obj = EndorserGroup()
                obj._deserialize(item)
                self.EndorserOrgList.append(obj)
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
        :param AsyncFlag: 同步調用標識，可選參數，值爲0或者不傳表示使用同步方法調用，調用後會等待交易執行後再返回執行結果；值爲1時表示使用異步方式調用Invoke，執行後會立即返回交易對應的Txid，後續需要通過GetInvokeTx這個API查詢該交易的執行結果。（對於邏輯較爲簡單的交易，可以使用同步模式；對於邏輯較爲複雜的交易，建議使用異步模式，否則容易導緻API因等待時間過長，返回等待超時）
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


class SendTransactionHandlerRequest(AbstractModel):
    """SendTransactionHandler請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：transaction
        :type Module: str
        :param Operation: 操作名，固定欄位：send_transaction
        :type Operation: str
        :param GroupPk: 群組編號
        :type GroupPk: str
        :param ContractId: 合約編號
        :type ContractId: int
        :param FuncName: 合約方法名
        :type FuncName: str
        :param FuncParam: 合約方法入參
        :type FuncParam: list of str
        """
        self.Module = None
        self.Operation = None
        self.GroupPk = None
        self.ContractId = None
        self.FuncName = None
        self.FuncParam = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupPk = params.get("GroupPk")
        self.ContractId = params.get("ContractId")
        self.FuncName = params.get("FuncName")
        self.FuncParam = params.get("FuncParam")


class SendTransactionHandlerResponse(AbstractModel):
    """SendTransactionHandler返回參數結構體

    """

    def __init__(self):
        """
        :param TransactionRsp: 交易結果json字串
        :type TransactionRsp: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TransactionRsp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransactionRsp = params.get("TransactionRsp")
        self.RequestId = params.get("RequestId")


class SrvInvokeRequest(AbstractModel):
    """SrvInvoke請求參數結構體

    """

    def __init__(self):
        """
        :param Service: 服務類型，iss或者dam
        :type Service: str
        :param Method: 服務介面，要調用的方法函數名
        :type Method: str
        :param Param: 用戶自定義json字串
        :type Param: str
        """
        self.Service = None
        self.Method = None
        self.Param = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.Method = params.get("Method")
        self.Param = params.get("Param")


class SrvInvokeResponse(AbstractModel):
    """SrvInvoke返回參數結構體

    """

    def __init__(self):
        """
        :param RetCode: 返回碼
        :type RetCode: int
        :param RetMsg: 返回訊息
        :type RetMsg: str
        :param Data: 返回數據
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RetCode = None
        self.RetMsg = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RetCode = params.get("RetCode")
        self.RetMsg = params.get("RetMsg")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class TransByDynamicContractHandlerRequest(AbstractModel):
    """TransByDynamicContractHandler請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名，固定欄位：transaction
        :type Module: str
        :param Operation: 操作名，固定欄位：trans_by_dynamic_contract
        :type Operation: str
        :param GroupPk: 群組編號
        :type GroupPk: str
        :param ContractAddress: 合約網址（合約佈署成功，可得到合約網址）
        :type ContractAddress: str
        :param ContractName: 合約名
        :type ContractName: str
        :param AbiInfo: 合約編譯後的abi
        :type AbiInfo: str
        :param FuncName: 合約被調用方法名
        :type FuncName: str
        :param FuncParam: 合約被調用方法的入參
        :type FuncParam: list of str
        """
        self.Module = None
        self.Operation = None
        self.GroupPk = None
        self.ContractAddress = None
        self.ContractName = None
        self.AbiInfo = None
        self.FuncName = None
        self.FuncParam = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.GroupPk = params.get("GroupPk")
        self.ContractAddress = params.get("ContractAddress")
        self.ContractName = params.get("ContractName")
        self.AbiInfo = params.get("AbiInfo")
        self.FuncName = params.get("FuncName")
        self.FuncParam = params.get("FuncParam")


class TransByDynamicContractHandlerResponse(AbstractModel):
    """TransByDynamicContractHandler返回參數結構體

    """

    def __init__(self):
        """
        :param TransactionRsp: 交易結果json字串
        :type TransactionRsp: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TransactionRsp = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TransactionRsp = params.get("TransactionRsp")
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
        :param BlockId: 交易所在區塊號
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