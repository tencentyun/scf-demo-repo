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


class AuthTestTidRequest(AbstractModel):
    """AuthTestTid請求參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備端SDK填入測試TID參數後生成的加密數據串
        :type Data: str
        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")


class AuthTestTidResponse(AbstractModel):
    """AuthTestTid返回參數結構體

    """

    def __init__(self):
        """
        :param Pass: 認證結果
        :type Pass: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Pass = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Pass = params.get("Pass")
        self.RequestId = params.get("RequestId")


class BurnTidNotifyRequest(AbstractModel):
    """BurnTidNotify請求參數結構體

    """

    def __init__(self):
        """
        :param OrderId: 訂單編號
        :type OrderId: str
        :param Tid: TID編號
        :type Tid: str
        """
        self.OrderId = None
        self.Tid = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Tid = params.get("Tid")


class BurnTidNotifyResponse(AbstractModel):
    """BurnTidNotify返回參數結構體

    """

    def __init__(self):
        """
        :param Tid: 接收回執成功的TID
        :type Tid: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Tid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.RequestId = params.get("RequestId")


class DeliverTidNotifyRequest(AbstractModel):
    """DeliverTidNotify請求參數結構體

    """

    def __init__(self):
        """
        :param OrderId: 訂單編號
        :type OrderId: str
        :param Tid: TID編號
        :type Tid: str
        """
        self.OrderId = None
        self.Tid = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Tid = params.get("Tid")


class DeliverTidNotifyResponse(AbstractModel):
    """DeliverTidNotify返回參數結構體

    """

    def __init__(self):
        """
        :param RemaindCount: 剩餘空發數量
        :type RemaindCount: int
        :param Tid: 已回執的TID編碼
        :type Tid: str
        :param ProductKey: 産品公鑰
        :type ProductKey: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RemaindCount = None
        self.Tid = None
        self.ProductKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RemaindCount = params.get("RemaindCount")
        self.Tid = params.get("Tid")
        self.ProductKey = params.get("ProductKey")
        self.RequestId = params.get("RequestId")


class DeliverTidsRequest(AbstractModel):
    """DeliverTids請求參數結構體

    """

    def __init__(self):
        """
        :param OrderId: 訂單ID
        :type OrderId: str
        :param Quantity: 數量，1~100
        :type Quantity: int
        """
        self.OrderId = None
        self.Quantity = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Quantity = params.get("Quantity")


class DeliverTidsResponse(AbstractModel):
    """DeliverTids返回參數結構體

    """

    def __init__(self):
        """
        :param TidSet: 空發的TID訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type TidSet: list of TidKeysInfo
        :param ProductKey: 産品公鑰
        :type ProductKey: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TidSet = None
        self.ProductKey = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TidSet") is not None:
            self.TidSet = []
            for item in params.get("TidSet"):
                obj = TidKeysInfo()
                obj._deserialize(item)
                self.TidSet.append(obj)
        self.ProductKey = params.get("ProductKey")
        self.RequestId = params.get("RequestId")


class DescribeAvailableLibCountRequest(AbstractModel):
    """DescribeAvailableLibCount請求參數結構體

    """

    def __init__(self):
        """
        :param OrderId: 訂單編號
        :type OrderId: str
        """
        self.OrderId = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")


class DescribeAvailableLibCountResponse(AbstractModel):
    """DescribeAvailableLibCount返回參數結構體

    """

    def __init__(self):
        """
        :param Quantity: 可空發的白盒金鑰數量
        :type Quantity: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Quantity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Quantity = params.get("Quantity")
        self.RequestId = params.get("RequestId")


class DescribePermissionRequest(AbstractModel):
    """DescribePermission請求參數結構體

    """


class DescribePermissionResponse(AbstractModel):
    """DescribePermission返回參數結構體

    """

    def __init__(self):
        """
        :param EnterpriseUser: 企業用戶
        :type EnterpriseUser: bool
        :param DownloadPermission: 下載控制台權限
        :type DownloadPermission: str
        :param UsePermission: 使用控制台權限
        :type UsePermission: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EnterpriseUser = None
        self.DownloadPermission = None
        self.UsePermission = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnterpriseUser = params.get("EnterpriseUser")
        self.DownloadPermission = params.get("DownloadPermission")
        self.UsePermission = params.get("UsePermission")
        self.RequestId = params.get("RequestId")


class DownloadTidsRequest(AbstractModel):
    """DownloadTids請求參數結構體

    """

    def __init__(self):
        """
        :param OrderId: 訂單編號
        :type OrderId: str
        :param Quantity: 下載數量：1~10
        :type Quantity: int
        """
        self.OrderId = None
        self.Quantity = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Quantity = params.get("Quantity")


class DownloadTidsResponse(AbstractModel):
    """DownloadTids返回參數結構體

    """

    def __init__(self):
        """
        :param TidSet: 下載的TID訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type TidSet: list of TidKeysInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TidSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TidSet") is not None:
            self.TidSet = []
            for item in params.get("TidSet"):
                obj = TidKeysInfo()
                obj._deserialize(item)
                self.TidSet.append(obj)
        self.RequestId = params.get("RequestId")


class TidKeysInfo(AbstractModel):
    """系統生成的TID和金鑰訊息

    """

    def __init__(self):
        """
        :param Tid: TID號碼
        :type Tid: str
        :param PublicKey: 公鑰
        :type PublicKey: str
        :param PrivateKey: 私鑰
        :type PrivateKey: str
        :param Psk: 共享金鑰
        :type Psk: str
        :param DownloadUrl: 軟加固白盒金鑰下載網址
        :type DownloadUrl: str
        :param DeviceCode: 軟加固設備標識碼
        :type DeviceCode: str
        """
        self.Tid = None
        self.PublicKey = None
        self.PrivateKey = None
        self.Psk = None
        self.DownloadUrl = None
        self.DeviceCode = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.PublicKey = params.get("PublicKey")
        self.PrivateKey = params.get("PrivateKey")
        self.Psk = params.get("Psk")
        self.DownloadUrl = params.get("DownloadUrl")
        self.DeviceCode = params.get("DeviceCode")


class UploadDeviceUniqueCodeRequest(AbstractModel):
    """UploadDeviceUniqueCode請求參數結構體

    """

    def __init__(self):
        """
        :param CodeSet: 硬體唯一標識碼
        :type CodeSet: list of str
        :param OrderId: 硬體標識碼綁定的申請編號
        :type OrderId: str
        """
        self.CodeSet = None
        self.OrderId = None


    def _deserialize(self, params):
        self.CodeSet = params.get("CodeSet")
        self.OrderId = params.get("OrderId")


class UploadDeviceUniqueCodeResponse(AbstractModel):
    """UploadDeviceUniqueCode返回參數結構體

    """

    def __init__(self):
        """
        :param Count: 本次已上傳數量
        :type Count: int
        :param ExistedCodeSet: 重複的硬體唯一標識碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExistedCodeSet: list of str
        :param LeftQuantity: 剩餘可上傳數量
        :type LeftQuantity: int
        :param IllegalCodeSet: 錯誤的硬體唯一標識碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type IllegalCodeSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.ExistedCodeSet = None
        self.LeftQuantity = None
        self.IllegalCodeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.ExistedCodeSet = params.get("ExistedCodeSet")
        self.LeftQuantity = params.get("LeftQuantity")
        self.IllegalCodeSet = params.get("IllegalCodeSet")
        self.RequestId = params.get("RequestId")


class VerifyChipBurnInfoRequest(AbstractModel):
    """VerifyChipBurnInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Data: 驗證數據
        :type Data: str
        """
        self.Data = None


    def _deserialize(self, params):
        self.Data = params.get("Data")


class VerifyChipBurnInfoResponse(AbstractModel):
    """VerifyChipBurnInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Pass: 驗證結果
        :type Pass: bool
        :param VerifiedTimes: 已驗證次數
        :type VerifiedTimes: int
        :param LeftTimes: 剩餘驗證次數
        :type LeftTimes: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Pass = None
        self.VerifiedTimes = None
        self.LeftTimes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Pass = params.get("Pass")
        self.VerifiedTimes = params.get("VerifiedTimes")
        self.LeftTimes = params.get("LeftTimes")
        self.RequestId = params.get("RequestId")