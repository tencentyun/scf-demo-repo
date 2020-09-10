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


class CheckVcodeRequest(AbstractModel):
    """CheckVcode請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名VerifyCode
        :type Module: str
        :param Operation: 操作名CheckVcode
        :type Operation: str
        :param AccountResId: 帳号ID
        :type AccountResId: str
        :param ContractResId: 合同ID
        :type ContractResId: str
        :param VerifyCode: 驗證碼
        :type VerifyCode: str
        """
        self.Module = None
        self.Operation = None
        self.AccountResId = None
        self.ContractResId = None
        self.VerifyCode = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.AccountResId = params.get("AccountResId")
        self.ContractResId = params.get("ContractResId")
        self.VerifyCode = params.get("VerifyCode")


class CheckVcodeResponse(AbstractModel):
    """CheckVcode返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateContractByUploadRequest(AbstractModel):
    """CreateContractByUpload請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名ContractMng
        :type Module: str
        :param Operation: 操作名CreateContractByUpload
        :type Operation: str
        :param SignInfos: 簽署人訊息
        :type SignInfos: list of SignInfo
        :param ContractFile: 合同上傳連結網址
        :type ContractFile: str
        :param ContractName: 合同名稱
        :type ContractName: str
        :param Remarks: 備注
        :type Remarks: str
        :param Initiator: 合同發起方Top Cloud 帳号ID（由平台自動填寫）
        :type Initiator: str
        :param ExpireTime: 合同長時間未簽署的過期時間
        :type ExpireTime: str
        """
        self.Module = None
        self.Operation = None
        self.SignInfos = None
        self.ContractFile = None
        self.ContractName = None
        self.Remarks = None
        self.Initiator = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        if params.get("SignInfos") is not None:
            self.SignInfos = []
            for item in params.get("SignInfos"):
                obj = SignInfo()
                obj._deserialize(item)
                self.SignInfos.append(obj)
        self.ContractFile = params.get("ContractFile")
        self.ContractName = params.get("ContractName")
        self.Remarks = params.get("Remarks")
        self.Initiator = params.get("Initiator")
        self.ExpireTime = params.get("ExpireTime")


class CreateContractByUploadResponse(AbstractModel):
    """CreateContractByUpload返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateEnterpriseAccountRequest(AbstractModel):
    """CreateEnterpriseAccount請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名AccountMng
        :type Module: str
        :param Operation: 操作名CreateEnterpriseAccount
        :type Operation: str
        :param Name: 企業用戶名稱
        :type Name: str
        :param IdentType: 企業用戶證件類型，8代表營業執照，詳情請見常見問題
        :type IdentType: int
        :param IdentNo: 企業用戶營業執照号碼
        :type IdentNo: str
        :param MobilePhone: 企業聯系人手機号
        :type MobilePhone: str
        :param TransactorName: 經辦人姓名
        :type TransactorName: str
        :param TransactorIdentType: 經辦人證件類型，0代表身份證
        :type TransactorIdentType: int
        :param TransactorIdentNo: 經辦人證件号碼
        :type TransactorIdentNo: str
        :param TransactorPhone: 經辦人手機号
        :type TransactorPhone: str
        :param Email: 企業聯系人電子信箱
        :type Email: str
        """
        self.Module = None
        self.Operation = None
        self.Name = None
        self.IdentType = None
        self.IdentNo = None
        self.MobilePhone = None
        self.TransactorName = None
        self.TransactorIdentType = None
        self.TransactorIdentNo = None
        self.TransactorPhone = None
        self.Email = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Name = params.get("Name")
        self.IdentType = params.get("IdentType")
        self.IdentNo = params.get("IdentNo")
        self.MobilePhone = params.get("MobilePhone")
        self.TransactorName = params.get("TransactorName")
        self.TransactorIdentType = params.get("TransactorIdentType")
        self.TransactorIdentNo = params.get("TransactorIdentNo")
        self.TransactorPhone = params.get("TransactorPhone")
        self.Email = params.get("Email")


class CreateEnterpriseAccountResponse(AbstractModel):
    """CreateEnterpriseAccount返回參數結構體

    """

    def __init__(self):
        """
        :param AccountResId: 帳号ID
        :type AccountResId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccountResId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccountResId = params.get("AccountResId")
        self.RequestId = params.get("RequestId")


class CreatePersonalAccountRequest(AbstractModel):
    """CreatePersonalAccount請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名AccountMng
        :type Module: str
        :param Operation: 操作名CreatePersonalAccount
        :type Operation: str
        :param Name: 個人用戶姓名
        :type Name: str
        :param IdentType: 個人用戶證件類型，0代表身份證，詳情請見常見問題
        :type IdentType: int
        :param IdentNo: 個人用戶證件号碼
        :type IdentNo: str
        :param MobilePhone: 個人用戶手機号
        :type MobilePhone: str
        """
        self.Module = None
        self.Operation = None
        self.Name = None
        self.IdentType = None
        self.IdentNo = None
        self.MobilePhone = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.Name = params.get("Name")
        self.IdentType = params.get("IdentType")
        self.IdentNo = params.get("IdentNo")
        self.MobilePhone = params.get("MobilePhone")


class CreatePersonalAccountResponse(AbstractModel):
    """CreatePersonalAccount返回參數結構體

    """

    def __init__(self):
        """
        :param AccountResId: 賬号ID
        :type AccountResId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccountResId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccountResId = params.get("AccountResId")
        self.RequestId = params.get("RequestId")


class CreateSealRequest(AbstractModel):
    """CreateSeal請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名SealMng
        :type Module: str
        :param Operation: 操作名CreateSeal
        :type Operation: str
        :param AccountResId: 帳号ID
        :type AccountResId: str
        :param ImgUrl: 簽章連結，圖片必須爲png格式
        :type ImgUrl: str
        :param ImgData: 圖片數據，base64編碼
        :type ImgData: str
        """
        self.Module = None
        self.Operation = None
        self.AccountResId = None
        self.ImgUrl = None
        self.ImgData = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.AccountResId = params.get("AccountResId")
        self.ImgUrl = params.get("ImgUrl")
        self.ImgData = params.get("ImgData")


class CreateSealResponse(AbstractModel):
    """CreateSeal返回參數結構體

    """

    def __init__(self):
        """
        :param SealResId: 簽章ID
        :type SealResId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SealResId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealResId = params.get("SealResId")
        self.RequestId = params.get("RequestId")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名AccountMng
        :type Module: str
        :param Operation: 操作名DeleteAccount
        :type Operation: str
        :param AccountList: 帳号ID清單
        :type AccountList: list of str
        """
        self.Module = None
        self.Operation = None
        self.AccountList = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.AccountList = params.get("AccountList")


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回參數結構體

    """

    def __init__(self):
        """
        :param DelSuccessList: 删除成功帳号ID清單
        :type DelSuccessList: list of str
        :param DelFailedList: 删除失敗帳号ID清單
        :type DelFailedList: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DelSuccessList = None
        self.DelFailedList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DelSuccessList = params.get("DelSuccessList")
        self.DelFailedList = params.get("DelFailedList")
        self.RequestId = params.get("RequestId")


class DeleteSealRequest(AbstractModel):
    """DeleteSeal請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名SealMng
        :type Module: str
        :param Operation: 操作名DeleteSeal
        :type Operation: str
        :param AccountResId: 帳号ID
        :type AccountResId: str
        :param SealResId: 簽章ID
        :type SealResId: str
        """
        self.Module = None
        self.Operation = None
        self.AccountResId = None
        self.SealResId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.AccountResId = params.get("AccountResId")
        self.SealResId = params.get("SealResId")


class DeleteSealResponse(AbstractModel):
    """DeleteSeal返回參數結構體

    """

    def __init__(self):
        """
        :param SealResId: 簽章ID
        :type SealResId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SealResId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SealResId = params.get("SealResId")
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名CommonMng
        :type Module: str
        :param Operation: 操作名DescribeTaskStatus
        :type Operation: str
        :param TaskId: 任務ID
        :type TaskId: int
        """
        self.Module = None
        self.Operation = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.TaskId = params.get("TaskId")


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回參數結構體

    """

    def __init__(self):
        """
        :param TaskResult: 任務結果
        :type TaskResult: str
        :param TaskType: 任務類型，010代表合同上傳結果，020代表合同下載結果
        :type TaskType: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.TaskType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskResult = params.get("TaskResult")
        self.TaskType = params.get("TaskType")
        self.RequestId = params.get("RequestId")


class DownloadContractRequest(AbstractModel):
    """DownloadContract請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名ContractMng
        :type Module: str
        :param Operation: 操作名DownloadContract
        :type Operation: str
        :param ContractResId: 合同ID
        :type ContractResId: str
        """
        self.Module = None
        self.Operation = None
        self.ContractResId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ContractResId = params.get("ContractResId")


class DownloadContractResponse(AbstractModel):
    """DownloadContract返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SendVcodeRequest(AbstractModel):
    """SendVcode請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名VerifyCode
        :type Module: str
        :param Operation: 操作名SendVcode
        :type Operation: str
        :param ContractResId: 合同ID
        :type ContractResId: str
        :param AccountResId: 帳号ID
        :type AccountResId: str
        """
        self.Module = None
        self.Operation = None
        self.ContractResId = None
        self.AccountResId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ContractResId = params.get("ContractResId")
        self.AccountResId = params.get("AccountResId")


class SendVcodeResponse(AbstractModel):
    """SendVcode返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SignContractByCoordinateRequest(AbstractModel):
    """SignContractByCoordinate請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名ContractMng
        :type Module: str
        :param Operation: 操作名SignContractByCoordinate
        :type Operation: str
        :param ContractResId: 合同ID
        :type ContractResId: str
        :param AccountResId: 帳戶ID
        :type AccountResId: str
        :param SignLocations: 簽署坐标，坐标原點在文件左下角，坐标單位爲磅，坐标不得超過合同文件邊界
        :type SignLocations: list of SignLocation
        :param AuthorizationTime: 授權時間（由平台自動填充）
        :type AuthorizationTime: str
        :param Position: 授權IP網址（由平台自動填充）
        :type Position: str
        :param SealResId: 簽章ID
        :type SealResId: str
        :param CertType: 選用證書類型：1  表示RSA證書， 2 表示國密證書， 參數不傳時預設爲1
        :type CertType: int
        :param ImageData: 簽名圖片，base64編碼
        :type ImageData: str
        """
        self.Module = None
        self.Operation = None
        self.ContractResId = None
        self.AccountResId = None
        self.SignLocations = None
        self.AuthorizationTime = None
        self.Position = None
        self.SealResId = None
        self.CertType = None
        self.ImageData = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ContractResId = params.get("ContractResId")
        self.AccountResId = params.get("AccountResId")
        if params.get("SignLocations") is not None:
            self.SignLocations = []
            for item in params.get("SignLocations"):
                obj = SignLocation()
                obj._deserialize(item)
                self.SignLocations.append(obj)
        self.AuthorizationTime = params.get("AuthorizationTime")
        self.Position = params.get("Position")
        self.SealResId = params.get("SealResId")
        self.CertType = params.get("CertType")
        self.ImageData = params.get("ImageData")


class SignContractByCoordinateResponse(AbstractModel):
    """SignContractByCoordinate返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SignContractByKeywordRequest(AbstractModel):
    """SignContractByKeyword請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名ContractMng
        :type Module: str
        :param Operation: 操作名SignContractByKeyword
        :type Operation: str
        :param ContractResId: 合同ID
        :type ContractResId: str
        :param AccountResId: 帳戶ID
        :type AccountResId: str
        :param SignKeyword: 簽署關鍵字，偏移坐标原點爲關鍵字中心
        :type SignKeyword: :class:`tencentcloud.ds.v20180523.models.SignKeyword`
        :param AuthorizationTime: 授權時間（由平台自動填充）
        :type AuthorizationTime: str
        :param Position: 授權IP網址（由平台自動填充）
        :type Position: str
        :param SealResId: 簽章ID
        :type SealResId: str
        :param CertType: 選用證書類型：1  表示RSA證書， 2 表示國密證書， 參數不傳時預設爲1
        :type CertType: int
        :param ImageData: 簽名圖片，base64編碼
        :type ImageData: str
        """
        self.Module = None
        self.Operation = None
        self.ContractResId = None
        self.AccountResId = None
        self.SignKeyword = None
        self.AuthorizationTime = None
        self.Position = None
        self.SealResId = None
        self.CertType = None
        self.ImageData = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ContractResId = params.get("ContractResId")
        self.AccountResId = params.get("AccountResId")
        if params.get("SignKeyword") is not None:
            self.SignKeyword = SignKeyword()
            self.SignKeyword._deserialize(params.get("SignKeyword"))
        self.AuthorizationTime = params.get("AuthorizationTime")
        self.Position = params.get("Position")
        self.SealResId = params.get("SealResId")
        self.CertType = params.get("CertType")
        self.ImageData = params.get("ImageData")


class SignContractByKeywordResponse(AbstractModel):
    """SignContractByKeyword返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SignInfo(AbstractModel):
    """簽署人訊息

    """

    def __init__(self):
        """
        :param AccountResId: 帳戶ID
        :type AccountResId: str
        :param AuthorizationTime: 授權時間（上傳合同可不傳該參數）
        :type AuthorizationTime: str
        :param Location: 授權IP網址（上傳合同可不傳該參數）
        :type Location: str
        :param SealId: 簽章ID
        :type SealId: str
        :param ImageData: 簽名圖片，優先級比SealId高
        :type ImageData: str
        :param CertType: 預設值：1  表示RSA證書， 2 表示國密證書， 參數不傳時預設爲1
        :type CertType: int
        :param SignLocation: 簽名域的标簽值
        :type SignLocation: str
        """
        self.AccountResId = None
        self.AuthorizationTime = None
        self.Location = None
        self.SealId = None
        self.ImageData = None
        self.CertType = None
        self.SignLocation = None


    def _deserialize(self, params):
        self.AccountResId = params.get("AccountResId")
        self.AuthorizationTime = params.get("AuthorizationTime")
        self.Location = params.get("Location")
        self.SealId = params.get("SealId")
        self.ImageData = params.get("ImageData")
        self.CertType = params.get("CertType")
        self.SignLocation = params.get("SignLocation")


class SignKeyword(AbstractModel):
    """簽署關鍵字訊息

    """

    def __init__(self):
        """
        :param Keyword: 關鍵字
        :type Keyword: str
        :param OffsetCoordX: X軸偏移坐标
        :type OffsetCoordX: str
        :param OffsetCoordY: Y軸偏移坐标
        :type OffsetCoordY: str
        :param ImageWidth: 簽章圖片寬度
        :type ImageWidth: str
        :param ImageHeight: 簽章圖片高度
        :type ImageHeight: str
        """
        self.Keyword = None
        self.OffsetCoordX = None
        self.OffsetCoordY = None
        self.ImageWidth = None
        self.ImageHeight = None


    def _deserialize(self, params):
        self.Keyword = params.get("Keyword")
        self.OffsetCoordX = params.get("OffsetCoordX")
        self.OffsetCoordY = params.get("OffsetCoordY")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")


class SignLocation(AbstractModel):
    """簽署坐标對象

    """

    def __init__(self):
        """
        :param SignOnPage: 簽名域頁數
        :type SignOnPage: str
        :param SignLocationLBX: 簽名域左下角X軸坐标軸
        :type SignLocationLBX: str
        :param SignLocationLBY: 簽名域左下角Y軸坐标軸
        :type SignLocationLBY: str
        :param SignLocationRUX: 簽名域右上角X軸坐标軸
        :type SignLocationRUX: str
        :param SignLocationRUY: 簽名域右上角Y軸坐标軸
        :type SignLocationRUY: str
        """
        self.SignOnPage = None
        self.SignLocationLBX = None
        self.SignLocationLBY = None
        self.SignLocationRUX = None
        self.SignLocationRUY = None


    def _deserialize(self, params):
        self.SignOnPage = params.get("SignOnPage")
        self.SignLocationLBX = params.get("SignLocationLBX")
        self.SignLocationLBY = params.get("SignLocationLBY")
        self.SignLocationRUX = params.get("SignLocationRUX")
        self.SignLocationRUY = params.get("SignLocationRUY")