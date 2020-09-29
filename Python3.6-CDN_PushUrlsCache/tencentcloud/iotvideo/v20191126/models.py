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


class BindDevInfo(AbstractModel):
    """終端用戶綁定的設備

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param DeviceModel: 設備型號
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeviceModel: str
        :param Role: 用戶角色，owner：主人，guest：訪客
        :type Role: str
        """
        self.Tid = None
        self.DeviceName = None
        self.DeviceModel = None
        self.Role = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.DeviceName = params.get("DeviceName")
        self.DeviceModel = params.get("DeviceModel")
        self.Role = params.get("Role")


class BindUsrInfo(AbstractModel):
    """設備綁定的終端用戶

    """

    def __init__(self):
        """
        :param AccessId: IotVideo平台分配給終端用戶的用戶id
        :type AccessId: str
        :param Role: 用戶角色，owner：主人，guest：訪客
        :type Role: str
        """
        self.AccessId = None
        self.Role = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.Role = params.get("Role")


class CreateAppUsrRequest(AbstractModel):
    """CreateAppUsr請求參數結構體

    """

    def __init__(self):
        """
        :param CunionId: 標識用戶的唯一ID，防止同一個用戶多次注冊
        :type CunionId: str
        """
        self.CunionId = None


    def _deserialize(self, params):
        self.CunionId = params.get("CunionId")


class CreateAppUsrResponse(AbstractModel):
    """CreateAppUsr返回參數結構體

    """

    def __init__(self):
        """
        :param CunionId: 廠商雲標識用戶的唯一ID
        :type CunionId: str
        :param AccessId: 客戶的終端用戶在IoT Video上的唯一標識ID
        :type AccessId: str
        :param NewRegist: 用戶是否爲新創建
        :type NewRegist: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CunionId = None
        self.AccessId = None
        self.NewRegist = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CunionId = params.get("CunionId")
        self.AccessId = params.get("AccessId")
        self.NewRegist = params.get("NewRegist")
        self.RequestId = params.get("RequestId")


class CreateBindingRequest(AbstractModel):
    """CreateBinding請求參數結構體

    """

    def __init__(self):
        """
        :param AccessId: 終端用戶在IoT Video上的唯一標識ID
        :type AccessId: str
        :param Tid: 設備TID
        :type Tid: str
        :param Role: 用戶角色，owner：主人，guest：訪客
        :type Role: str
        :param ForceBind: 是否踢掉之前的主人，true：踢掉；false：不踢掉。當role爲owner時，可以不填
        :type ForceBind: bool
        """
        self.AccessId = None
        self.Tid = None
        self.Role = None
        self.ForceBind = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.Tid = params.get("Tid")
        self.Role = params.get("Role")
        self.ForceBind = params.get("ForceBind")


class CreateBindingResponse(AbstractModel):
    """CreateBinding返回參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問設備的AccessToken
        :type AccessToken: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccessToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.RequestId = params.get("RequestId")


class CreateDevTokenRequest(AbstractModel):
    """CreateDevToken請求參數結構體

    """

    def __init__(self):
        """
        :param AccessId: 客戶的終端用戶在IoT Video上的唯一標識ID
        :type AccessId: str
        :param Tids: 設備TID清單,0<元素數量<=100
        :type Tids: list of str
        :param TtlMinutes: Token的TTL(time to alive)分鍾數
        :type TtlMinutes: int
        """
        self.AccessId = None
        self.Tids = None
        self.TtlMinutes = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.Tids = params.get("Tids")
        self.TtlMinutes = params.get("TtlMinutes")


class CreateDevTokenResponse(AbstractModel):
    """CreateDevToken返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 返回的用戶token清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of DevTokenInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DevTokenInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class CreateDevicesRequest(AbstractModel):
    """CreateDevices請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param Number: 創建設備的數量，數量範圍1-100
        :type Number: int
        :param NamePrefix: 設備名稱前綴，支援英文、數字，不超過10字元
        :type NamePrefix: str
        :param Operator: 操作人
        :type Operator: str
        """
        self.ProductId = None
        self.Number = None
        self.NamePrefix = None
        self.Operator = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Number = params.get("Number")
        self.NamePrefix = params.get("NamePrefix")
        self.Operator = params.get("Operator")


class CreateDevicesResponse(AbstractModel):
    """CreateDevices返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 新創建設備的認證訊息
        :type Data: list of DeviceCertificate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DeviceCertificate()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class CreateGencodeRequest(AbstractModel):
    """CreateGencode請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param Revision: 物模型發布版本號，-1代表最新編輯（未發布）的版本
        :type Revision: int
        """
        self.ProductId = None
        self.Revision = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Revision = params.get("Revision")


class CreateGencodeResponse(AbstractModel):
    """CreateGencode返回參數結構體

    """

    def __init__(self):
        """
        :param ZipCode: 生成的原始碼(zip壓縮後的base64編碼)
注意：此欄位可能返回 null，表示取不到有效值。
        :type ZipCode: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ZipCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ZipCode = params.get("ZipCode")
        self.RequestId = params.get("RequestId")


class CreateIotDataTypeRequest(AbstractModel):
    """CreateIotDataType請求參數結構體

    """

    def __init__(self):
        """
        :param IotDataType: 用戶自定義數據類型，json格式的字串
        :type IotDataType: str
        """
        self.IotDataType = None


    def _deserialize(self, params):
        self.IotDataType = params.get("IotDataType")


class CreateIotDataTypeResponse(AbstractModel):
    """CreateIotDataType返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateIotModelRequest(AbstractModel):
    """CreateIotModel請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param IotModel: 物模型json串
        :type IotModel: str
        """
        self.ProductId = None
        self.IotModel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.IotModel = params.get("IotModel")


class CreateIotModelResponse(AbstractModel):
    """CreateIotModel返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductModel: 産器型號(APP産品,爲APP包名)
        :type ProductModel: str
        :param Features: 設備功能碼（ypsxth:音訊雙向通話 ，spdxth:視訊單向通話）
        :type Features: list of str
        :param ProductName: 産品名稱
僅支援中文、英文、數字、下劃線，不超過32個字元
        :type ProductName: str
        :param ProductDescription: 産品描述訊息
不支援單引號、雙引號、退格符、回車符、換行符、制表符、反斜杠、下劃線、“%”、“#”、“$”，不超過128字元
        :type ProductDescription: str
        :param ChipManufactureId: 主晶片産商ID
        :type ChipManufactureId: str
        :param ChipId: 主晶片ID
        :type ChipId: str
        """
        self.ProductModel = None
        self.Features = None
        self.ProductName = None
        self.ProductDescription = None
        self.ChipManufactureId = None
        self.ChipId = None


    def _deserialize(self, params):
        self.ProductModel = params.get("ProductModel")
        self.Features = params.get("Features")
        self.ProductName = params.get("ProductName")
        self.ProductDescription = params.get("ProductDescription")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")


class CreateProductResponse(AbstractModel):
    """CreateProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 産品詳細訊息
        :type Data: :class:`taifucloudcloud.iotvideo.v20191126.models.ProductBase`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ProductBase()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateStorageRequest(AbstractModel):
    """CreateStorage請求參數結構體

    """

    def __init__(self):
        """
        :param PkgId: 雲存套餐ID
        :type PkgId: str
        :param Tid: 設備TID
        :type Tid: str
        :param UserTag: 用戶唯一標識，由廠商保證内部唯一性
        :type UserTag: str
        """
        self.PkgId = None
        self.Tid = None
        self.UserTag = None


    def _deserialize(self, params):
        self.PkgId = params.get("PkgId")
        self.Tid = params.get("Tid")
        self.UserTag = params.get("UserTag")


class CreateStorageResponse(AbstractModel):
    """CreateStorage返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTraceIdsRequest(AbstractModel):
    """CreateTraceIds請求參數結構體

    """

    def __init__(self):
        """
        :param Tids: 設備TID清單
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class CreateTraceIdsResponse(AbstractModel):
    """CreateTraceIds返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUploadPathRequest(AbstractModel):
    """CreateUploadPath請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param FileName: 固件文件名
        :type FileName: str
        """
        self.ProductId = None
        self.FileName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.FileName = params.get("FileName")


class CreateUploadPathResponse(AbstractModel):
    """CreateUploadPath返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 固件上傳網址URL，用戶可将本地的固件文件通過該URL以PUT的請求方式上傳。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class CreateUsrTokenRequest(AbstractModel):
    """CreateUsrToken請求參數結構體

    """

    def __init__(self):
        """
        :param AccessId: 終端用戶在IoT Video上的唯一標識ID
        :type AccessId: str
        :param UniqueId: 終端唯一ID，用於區分同一個用戶的多個終端
        :type UniqueId: str
        :param TtlMinutes: Token的TTL(time to alive)分鍾數
        :type TtlMinutes: int
        """
        self.AccessId = None
        self.UniqueId = None
        self.TtlMinutes = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.UniqueId = params.get("UniqueId")
        self.TtlMinutes = params.get("TtlMinutes")


class CreateUsrTokenResponse(AbstractModel):
    """CreateUsrToken返回參數結構體

    """

    def __init__(self):
        """
        :param AccessId: 終端用戶在IoT Video上的唯一標識ID
        :type AccessId: str
        :param AccessToken: IoT Video平台的AccessToken
        :type AccessToken: str
        :param ExpireTime: Token的過期時間，單位秒(UTC時間)
        :type ExpireTime: int
        :param TerminalId: 終端ID
        :type TerminalId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccessId = None
        self.AccessToken = None
        self.ExpireTime = None
        self.TerminalId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.AccessToken = params.get("AccessToken")
        self.ExpireTime = params.get("ExpireTime")
        self.TerminalId = params.get("TerminalId")
        self.RequestId = params.get("RequestId")


class DeleteAppUsrRequest(AbstractModel):
    """DeleteAppUsr請求參數結構體

    """

    def __init__(self):
        """
        :param AccessId: 客戶的終端用戶在IoT Video上的唯一標識ID
        :type AccessId: str
        """
        self.AccessId = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")


class DeleteAppUsrResponse(AbstractModel):
    """DeleteAppUsr返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBindingRequest(AbstractModel):
    """DeleteBinding請求參數結構體

    """

    def __init__(self):
        """
        :param AccessId: 終端用戶在IoT Video上的唯一標識ID
        :type AccessId: str
        :param Tid: 設備TID
        :type Tid: str
        :param Role: 用戶角色，owner：主人，guest：訪客
        :type Role: str
        """
        self.AccessId = None
        self.Tid = None
        self.Role = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.Tid = params.get("Tid")
        self.Role = params.get("Role")


class DeleteBindingResponse(AbstractModel):
    """DeleteBinding返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice請求參數結構體

    """

    def __init__(self):
        """
        :param Tids: 設備TID清單
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class DeleteDeviceResponse(AbstractModel):
    """DeleteDevice返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteIotDataTypeRequest(AbstractModel):
    """DeleteIotDataType請求參數結構體

    """

    def __init__(self):
        """
        :param TypeId: 自定義數據類型的標識符
        :type TypeId: str
        """
        self.TypeId = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")


class DeleteIotDataTypeResponse(AbstractModel):
    """DeleteIotDataType返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMessageQueueRequest(AbstractModel):
    """DeleteMessageQueue請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DeleteMessageQueueResponse(AbstractModel):
    """DeleteMessageQueue返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOtaVersionRequest(AbstractModel):
    """DeleteOtaVersion請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param OtaVersion: 固件版本號，格式爲x.y.z， x，y 範圍0-63，z範圍1~524288
        :type OtaVersion: str
        :param Operator: 操作人
        :type Operator: str
        """
        self.ProductId = None
        self.OtaVersion = None
        self.Operator = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.Operator = params.get("Operator")


class DeleteOtaVersionResponse(AbstractModel):
    """DeleteOtaVersion返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProductRequest(AbstractModel):
    """DeleteProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DeleteProductResponse(AbstractModel):
    """DeleteProduct返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTraceIdsRequest(AbstractModel):
    """DeleteTraceIds請求參數結構體

    """

    def __init__(self):
        """
        :param Tids: 設備TID清單
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class DeleteTraceIdsResponse(AbstractModel):
    """DeleteTraceIds返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBindDevRequest(AbstractModel):
    """DescribeBindDev請求參數結構體

    """

    def __init__(self):
        """
        :param AccessId: 終端用戶在IoT Video上的唯一標識ID
        :type AccessId: str
        """
        self.AccessId = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")


class DescribeBindDevResponse(AbstractModel):
    """DescribeBindDev返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 綁定的設備清單訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of BindDevInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BindDevInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBindUsrRequest(AbstractModel):
    """DescribeBindUsr請求參數結構體

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param AccessId: 設備主人的AccessId
        :type AccessId: str
        """
        self.Tid = None
        self.AccessId = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.AccessId = params.get("AccessId")


class DescribeBindUsrResponse(AbstractModel):
    """DescribeBindUsr返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 具有綁定關系的終端用戶訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of BindUsrInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = BindUsrInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceModelRequest(AbstractModel):
    """DescribeDeviceModel請求參數結構體

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param Branch: 物模型的分支路徑
        :type Branch: str
        """
        self.Tid = None
        self.Branch = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Branch = params.get("Branch")


class DescribeDeviceModelResponse(AbstractModel):
    """DescribeDeviceModel返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備物模型訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`taifucloudcloud.iotvideo.v20191126.models.DeviceModelData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DeviceModelData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice請求參數結構體

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        """
        self.Tid = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`taifucloudcloud.iotvideo.v20191126.models.DeviceData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DeviceData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ReturnModel: 是否返回全量數據
當該值爲false時，返回值中的設備物模型、固件版本、在線狀态、最後在線時間欄位等欄位，都将返回數據類型的零值。
        :type ReturnModel: bool
        :param Limit: 分頁數量,0<取值範圍<=100
        :type Limit: int
        :param Offset: 分頁偏移，取值＞0
        :type Offset: int
        :param OtaVersion: 指定固件版本號，爲空查詢此産品下所有設備
        :type OtaVersion: str
        :param DeviceName: 設備名稱，支援左前綴模糊比對
        :type DeviceName: str
        """
        self.ProductId = None
        self.ReturnModel = None
        self.Limit = None
        self.Offset = None
        self.OtaVersion = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ReturnModel = params.get("ReturnModel")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OtaVersion = params.get("OtaVersion")
        self.DeviceName = params.get("DeviceName")


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備訊息 清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of DevicesData
        :param TotalCount: 設備總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DevicesData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIotDataTypeRequest(AbstractModel):
    """DescribeIotDataType請求參數結構體

    """

    def __init__(self):
        """
        :param TypeId: 自定義數據類型的標識符，爲空則返回全量自定義類型的清單
        :type TypeId: str
        """
        self.TypeId = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")


class DescribeIotDataTypeResponse(AbstractModel):
    """DescribeIotDataType返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 自定義數據類型，json格式的字串
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeIotModelRequest(AbstractModel):
    """DescribeIotModel請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param Revision: 物模型版本號， -1表示最新編輯的（未發布）
        :type Revision: int
        """
        self.ProductId = None
        self.Revision = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Revision = params.get("Revision")


class DescribeIotModelResponse(AbstractModel):
    """DescribeIotModel返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 物模型定義，json格式的字串
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeIotModelsRequest(AbstractModel):
    """DescribeIotModels請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeIotModelsResponse(AbstractModel):
    """DescribeIotModels返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 曆史版本清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of IotModelData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = IotModelData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLogsRequest(AbstractModel):
    """DescribeLogs請求參數結構體

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param Limit: 當前分頁的最大條數,0<取值範圍<=100
        :type Limit: int
        :param Offset: 分頁偏移量,取值範圍>0
        :type Offset: int
        :param LogType: 日志類型 1.在線狀态變更 2.ProConst變更 3.ProWritable變更 4.Action控制 5.ProReadonly變更 6.Event事件
        :type LogType: int
        :param StartTime: 查詢的起始時間 UNIX時間戳，單位秒
        :type StartTime: int
        :param DataObject: 物模型對象索引，用於模糊查詢，字元長度<=255，每層節點的字元長度<=16
        :type DataObject: str
        :param EndTime: 查詢的結束時間 UNIX時間戳，單位秒
        :type EndTime: int
        """
        self.Tid = None
        self.Limit = None
        self.Offset = None
        self.LogType = None
        self.StartTime = None
        self.DataObject = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.LogType = params.get("LogType")
        self.StartTime = params.get("StartTime")
        self.DataObject = params.get("DataObject")
        self.EndTime = params.get("EndTime")


class DescribeLogsResponse(AbstractModel):
    """DescribeLogs返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備日志訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of LogData
        :param TotalCount: Data數組所包含的訊息條數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = LogData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMessageQueueRequest(AbstractModel):
    """DescribeMessageQueue請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeMessageQueueResponse(AbstractModel):
    """DescribeMessageQueue返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 訊息隊列配置
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`taifucloudcloud.iotvideo.v20191126.models.MsgQueueData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = MsgQueueData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeModelDataRetRequest(AbstractModel):
    """DescribeModelDataRet請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeModelDataRetResponse(AbstractModel):
    """DescribeModelDataRet返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備響應結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeOtaVersionsRequest(AbstractModel):
    """DescribeOtaVersions請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁偏移量
        :type Offset: int
        :param Limit: 每頁數量，0<取值範圍<=100
        :type Limit: int
        :param ProductId: 産品ID，爲空時查詢客戶所有産品的版本訊息
        :type ProductId: str
        :param OtaVersion: 版本號，支援模糊比對
        :type OtaVersion: str
        :param PubStatus: 版本類型 1未發布 2測試發布 3正式發布 4禁用
        :type PubStatus: int
        """
        self.Offset = None
        self.Limit = None
        self.ProductId = None
        self.OtaVersion = None
        self.PubStatus = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.PubStatus = params.get("PubStatus")


class DescribeOtaVersionsResponse(AbstractModel):
    """DescribeOtaVersions返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 版本數量
        :type TotalCount: int
        :param Data: 版本詳細訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of VersionData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VersionData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProductRequest(AbstractModel):
    """DescribeProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeProductResponse(AbstractModel):
    """DescribeProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 産品詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: :class:`taifucloudcloud.iotvideo.v20191126.models.ProductData`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ProductData()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 分頁大小，當前頁面中顯示的最大數量，值範圍 1-100
        :type Limit: int
        :param Offset: 分頁偏移，Offset從0開始
        :type Offset: int
        :param ProductModel: 産器型號(APP産品,爲APP包名)
        :type ProductModel: str
        :param StartTime: 開始時間 ，UNIX 時間戳，單位秒
        :type StartTime: int
        :param EndTime: 結束時間 ，UNIX 時間戳，單位秒
        :type EndTime: int
        """
        self.Limit = None
        self.Offset = None
        self.ProductModel = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ProductModel = params.get("ProductModel")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 産品詳細訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of ProductData
        :param TotalCount: 産品總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ProductData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePubVersionsRequest(AbstractModel):
    """DescribePubVersions請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribePubVersionsResponse(AbstractModel):
    """DescribePubVersions返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 曆史發布的版本清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of OtaPubHistory
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = OtaPubHistory()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegistrationStatusRequest(AbstractModel):
    """DescribeRegistrationStatus請求參數結構體

    """

    def __init__(self):
        """
        :param CunionIds: 終端用戶的唯一ID清單，0<元素數量<=100
        :type CunionIds: list of str
        """
        self.CunionIds = None


    def _deserialize(self, params):
        self.CunionIds = params.get("CunionIds")


class DescribeRegistrationStatusResponse(AbstractModel):
    """DescribeRegistrationStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 終端用戶注冊狀态清單
        :type Data: list of RegisteredStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = RegisteredStatus()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRunLogRequest(AbstractModel):
    """DescribeRunLog請求參數結構體

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        """
        self.Tid = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")


class DescribeRunLogResponse(AbstractModel):
    """DescribeRunLog返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備運作日志文本訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeTraceIdsRequest(AbstractModel):
    """DescribeTraceIds請求參數結構體

    """


class DescribeTraceIdsResponse(AbstractModel):
    """DescribeTraceIds返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備TID清單，清單元素之間以“,”分隔
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeTraceStatusRequest(AbstractModel):
    """DescribeTraceStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Tids: 設備TID清單
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class DescribeTraceStatusResponse(AbstractModel):
    """DescribeTraceStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備追蹤狀态清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: list of TraceStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TraceStatus()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DevTokenInfo(AbstractModel):
    """用於終端用戶臨時訪問設備的token授權訊息

    """

    def __init__(self):
        """
        :param AccessId: 客戶的終端用戶在IotVideo上的唯一標識id
        :type AccessId: str
        :param Tid: 設備TID
        :type Tid: str
        :param AccessToken: IotVideo平台的accessToken
        :type AccessToken: str
        :param ExpireTime: Token的過期時間，單位秒(UTC時間)
        :type ExpireTime: int
        """
        self.AccessId = None
        self.Tid = None
        self.AccessToken = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.AccessId = params.get("AccessId")
        self.Tid = params.get("Tid")
        self.AccessToken = params.get("AccessToken")
        self.ExpireTime = params.get("ExpireTime")


class DeviceCertificate(AbstractModel):
    """設備證書及金鑰

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param Certificate: 設備初始證書訊息，base64編碼
        :type Certificate: str
        :param WhiteBoxSoUrl: 設備私鑰下載網址
        :type WhiteBoxSoUrl: str
        """
        self.Tid = None
        self.Certificate = None
        self.WhiteBoxSoUrl = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Certificate = params.get("Certificate")
        self.WhiteBoxSoUrl = params.get("WhiteBoxSoUrl")


class DeviceData(AbstractModel):
    """設備訊息

    """

    def __init__(self):
        """
        :param Tid: 設備TID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tid: str
        :param ActiveTime: 啟動時間 0代表未啟動
注意：此欄位可能返回 null，表示取不到有效值。
        :type ActiveTime: int
        :param Disabled: 設備是否被禁用
注意：此欄位可能返回 null，表示取不到有效值。
        :type Disabled: bool
        :param OtaVersion: 固件版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type OtaVersion: str
        :param Online: 設備在線狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type Online: int
        :param LastOnlineTime: 設備最後上線時間（mqtt連接成功時間），UNIX時間戳，單位秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastOnlineTime: int
        :param IotModel: 物模型json數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type IotModel: str
        :param DeviceName: 設備名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param ProductId: 産品ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param Certificate: 設備初始證書訊息，base64編碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param WhiteBoxSoUrl: 設備私鑰下載網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type WhiteBoxSoUrl: str
        :param StreamStatus: 設備推流狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type StreamStatus: bool
        """
        self.Tid = None
        self.ActiveTime = None
        self.Disabled = None
        self.OtaVersion = None
        self.Online = None
        self.LastOnlineTime = None
        self.IotModel = None
        self.DeviceName = None
        self.ProductId = None
        self.Certificate = None
        self.WhiteBoxSoUrl = None
        self.StreamStatus = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.ActiveTime = params.get("ActiveTime")
        self.Disabled = params.get("Disabled")
        self.OtaVersion = params.get("OtaVersion")
        self.Online = params.get("Online")
        self.LastOnlineTime = params.get("LastOnlineTime")
        self.IotModel = params.get("IotModel")
        self.DeviceName = params.get("DeviceName")
        self.ProductId = params.get("ProductId")
        self.Certificate = params.get("Certificate")
        self.WhiteBoxSoUrl = params.get("WhiteBoxSoUrl")
        self.StreamStatus = params.get("StreamStatus")


class DeviceModelData(AbstractModel):
    """設備物模型數據

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param Branch: 物模型分支路徑
注意：此欄位可能返回 null，表示取不到有效值。
        :type Branch: str
        :param IotModel: 物模型數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type IotModel: str
        """
        self.Tid = None
        self.Branch = None
        self.IotModel = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Branch = params.get("Branch")
        self.IotModel = params.get("IotModel")


class DevicesData(AbstractModel):
    """設備清單元素所包含的設備基本訊息

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param ActiveTime: 啟動時間 0代表未啟動
        :type ActiveTime: int
        :param Disabled: 設備是否被禁用
        :type Disabled: bool
        :param StreamStatus: 設備推流狀态
        :type StreamStatus: bool
        :param OtaVersion: 固件版本
        :type OtaVersion: str
        :param Online: 設備在線狀态
        :type Online: int
        :param LastOnlineTime: 設備最後上線時間（mqtt連接成功時間），UNIX時間戳，單位秒
        :type LastOnlineTime: int
        :param IotModel: 物模型json數據
        :type IotModel: str
        :param LastUpdateTime: 設備固件最新更新時間，UNIX時間戳，單位秒
        :type LastUpdateTime: int
        """
        self.Tid = None
        self.DeviceName = None
        self.ActiveTime = None
        self.Disabled = None
        self.StreamStatus = None
        self.OtaVersion = None
        self.Online = None
        self.LastOnlineTime = None
        self.IotModel = None
        self.LastUpdateTime = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.DeviceName = params.get("DeviceName")
        self.ActiveTime = params.get("ActiveTime")
        self.Disabled = params.get("Disabled")
        self.StreamStatus = params.get("StreamStatus")
        self.OtaVersion = params.get("OtaVersion")
        self.Online = params.get("Online")
        self.LastOnlineTime = params.get("LastOnlineTime")
        self.IotModel = params.get("IotModel")
        self.LastUpdateTime = params.get("LastUpdateTime")


class DisableDeviceRequest(AbstractModel):
    """DisableDevice請求參數結構體

    """

    def __init__(self):
        """
        :param Tids: 設備TID ≤100
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class DisableDeviceResponse(AbstractModel):
    """DisableDevice返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableDeviceStreamRequest(AbstractModel):
    """DisableDeviceStream請求參數結構體

    """

    def __init__(self):
        """
        :param Tids: 設備TID清單
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class DisableDeviceStreamResponse(AbstractModel):
    """DisableDeviceStream返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableOtaVersionRequest(AbstractModel):
    """DisableOtaVersion請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param OtaVersion: 固件版本號，格式爲x.y.z， x，y 範圍0-63，z範圍1~524288
        :type OtaVersion: str
        :param Operator: 操作人
        :type Operator: str
        """
        self.ProductId = None
        self.OtaVersion = None
        self.Operator = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.Operator = params.get("Operator")


class DisableOtaVersionResponse(AbstractModel):
    """DisableOtaVersion返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IotModelData(AbstractModel):
    """物模型曆史版本

    """

    def __init__(self):
        """
        :param Revision: 版本號
        :type Revision: int
        :param ReleaseTime: 發布時間
        :type ReleaseTime: int
        """
        self.Revision = None
        self.ReleaseTime = None


    def _deserialize(self, params):
        self.Revision = params.get("Revision")
        self.ReleaseTime = params.get("ReleaseTime")


class LogData(AbstractModel):
    """設備日志訊息

    """

    def __init__(self):
        """
        :param Occurtime: 發生時間 UNIX時間戳，單位秒
        :type Occurtime: int
        :param LogType: 日志類型 1在線狀态變更 2FP變更 3SP變更 4CO控制 5ST變更 6EV事件
        :type LogType: int
        :param DataObject: 物模型對象索引
注意：此欄位可能返回 null，表示取不到有效值。
        :type DataObject: str
        :param OldValue: 物模型舊值  json串
注意：此欄位可能返回 null，表示取不到有效值。
        :type OldValue: str
        :param NewValue: 物模型新值  json串
注意：此欄位可能返回 null，表示取不到有效值。
        :type NewValue: str
        """
        self.Occurtime = None
        self.LogType = None
        self.DataObject = None
        self.OldValue = None
        self.NewValue = None


    def _deserialize(self, params):
        self.Occurtime = params.get("Occurtime")
        self.LogType = params.get("LogType")
        self.DataObject = params.get("DataObject")
        self.OldValue = params.get("OldValue")
        self.NewValue = params.get("NewValue")


class ModifyDeviceActionRequest(AbstractModel):
    """ModifyDeviceAction請求參數結構體

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param Wakeup: 如果設備處於休眠狀态，是否喚醒設備
        :type Wakeup: bool
        :param Branch: 物模型的分支路徑
        :type Branch: str
        :param Value: 寫入的物模型數據，如果是json需要轉義成字串
        :type Value: str
        :param IsNum: Value欄位的類型是否爲數值（float、int）
        :type IsNum: bool
        """
        self.Tid = None
        self.Wakeup = None
        self.Branch = None
        self.Value = None
        self.IsNum = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Wakeup = params.get("Wakeup")
        self.Branch = params.get("Branch")
        self.Value = params.get("Value")
        self.IsNum = params.get("IsNum")


class ModifyDeviceActionResponse(AbstractModel):
    """ModifyDeviceAction返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備端的響應結果
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: str
        :param TaskId: 任務ID
若設備端未能及時響應時，會返回此欄位，用戶可以通過DescribeModelDataRet獲取設備的最終響應結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyDevicePropertyRequest(AbstractModel):
    """ModifyDeviceProperty請求參數結構體

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param Wakeup: 如果設備處於休眠狀态，是否喚醒設備
        :type Wakeup: bool
        :param Branch: 物模型的分支路徑
        :type Branch: str
        :param Value: 寫入的物模型數據，如果是json需要轉義成字串
        :type Value: str
        :param IsNum: Value欄位是否爲數值（float、int）
        :type IsNum: bool
        """
        self.Tid = None
        self.Wakeup = None
        self.Branch = None
        self.Value = None
        self.IsNum = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Wakeup = params.get("Wakeup")
        self.Branch = params.get("Branch")
        self.Value = params.get("Value")
        self.IsNum = params.get("IsNum")


class ModifyDevicePropertyResponse(AbstractModel):
    """ModifyDeviceProperty返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProductRequest(AbstractModel):
    """ModifyProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ProductName: 産品名稱
        :type ProductName: str
        :param ProductDescription: 産品描述
        :type ProductDescription: str
        :param ChipManufactureId: 主晶片産商ID
        :type ChipManufactureId: str
        :param ChipId: 主晶片ID
        :type ChipId: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductDescription = None
        self.ChipManufactureId = None
        self.ChipId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDescription = params.get("ProductDescription")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")


class ModifyProductResponse(AbstractModel):
    """ModifyProduct返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MsgQueueData(AbstractModel):
    """産品轉發訊息隊列配置

    """

    def __init__(self):
        """
        :param MsgQueueType: 訊息隊列類型 1：CMQ 2：kafka
        :type MsgQueueType: int
        :param MsgType: 訊息類型清單，整型值（0-31）之間以“,”分隔
        :type MsgType: str
        :param Topic: 主題名稱
        :type Topic: str
        :param Instance: 實例名稱
        :type Instance: str
        :param MsgRegion: 訊息地域
        :type MsgRegion: str
        """
        self.MsgQueueType = None
        self.MsgType = None
        self.Topic = None
        self.Instance = None
        self.MsgRegion = None


    def _deserialize(self, params):
        self.MsgQueueType = params.get("MsgQueueType")
        self.MsgType = params.get("MsgType")
        self.Topic = params.get("Topic")
        self.Instance = params.get("Instance")
        self.MsgRegion = params.get("MsgRegion")


class OtaPubHistory(AbstractModel):
    """産品發布過的全部版本

    """

    def __init__(self):
        """
        :param OtaVersion: 版本名稱
        :type OtaVersion: str
        :param PublishTime: 發布時間，unix時間戳，單位：秒
        :type PublishTime: int
        """
        self.OtaVersion = None
        self.PublishTime = None


    def _deserialize(self, params):
        self.OtaVersion = params.get("OtaVersion")
        self.PublishTime = params.get("PublishTime")


class ProductBase(AbstractModel):
    """産品訊息摘要

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ProductModel: 産器型號(APP産品,爲APP包名)
        :type ProductModel: str
        :param ProductName: 産品名稱
        :type ProductName: str
        :param ProductDescription: 産品描述訊息
        :type ProductDescription: str
        :param CreateTime: 創建時間，UNIX 時間戳，單位秒
        :type CreateTime: int
        :param IotModelRevision: 物模型發布版本號,0代表物模型尚未發布
        :type IotModelRevision: int
        :param SecretKey: 産品金鑰
        :type SecretKey: str
        """
        self.ProductId = None
        self.ProductModel = None
        self.ProductName = None
        self.ProductDescription = None
        self.CreateTime = None
        self.IotModelRevision = None
        self.SecretKey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductModel = params.get("ProductModel")
        self.ProductName = params.get("ProductName")
        self.ProductDescription = params.get("ProductDescription")
        self.CreateTime = params.get("CreateTime")
        self.IotModelRevision = params.get("IotModelRevision")
        self.SecretKey = params.get("SecretKey")


class ProductData(AbstractModel):
    """産品訊息

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param ProductName: 産品名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param ProductDescription: 産品描述訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductDescription: str
        :param CreateTime: 創建時間，UNIX 時間戳，單位秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param IotModelRevision: 物模型發布版本號,0代表物模型尚未發布
注意：此欄位可能返回 null，表示取不到有效值。
        :type IotModelRevision: int
        :param SecretKey: 産品金鑰
注意：此欄位可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param Features: 設備功能碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type Features: list of str
        :param ProductModel: 産器型號(APP産品,爲APP包名)
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductModel: str
        :param ChipManufactureId: 主晶片廠商id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChipManufactureId: str
        :param ChipId: 主晶片型號
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChipId: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductDescription = None
        self.CreateTime = None
        self.IotModelRevision = None
        self.SecretKey = None
        self.Features = None
        self.ProductModel = None
        self.ChipManufactureId = None
        self.ChipId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDescription = params.get("ProductDescription")
        self.CreateTime = params.get("CreateTime")
        self.IotModelRevision = params.get("IotModelRevision")
        self.SecretKey = params.get("SecretKey")
        self.Features = params.get("Features")
        self.ProductModel = params.get("ProductModel")
        self.ChipManufactureId = params.get("ChipManufactureId")
        self.ChipId = params.get("ChipId")


class RegisteredStatus(AbstractModel):
    """終端用戶注冊狀态

    """

    def __init__(self):
        """
        :param CunionId: 終端用戶的唯一ID
        :type CunionId: str
        :param IsRegisted: 注冊狀态
        :type IsRegisted: bool
        """
        self.CunionId = None
        self.IsRegisted = None


    def _deserialize(self, params):
        self.CunionId = params.get("CunionId")
        self.IsRegisted = params.get("IsRegisted")


class RunDeviceRequest(AbstractModel):
    """RunDevice請求參數結構體

    """

    def __init__(self):
        """
        :param Tids: TID清單 ≤100
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class RunDeviceResponse(AbstractModel):
    """RunDevice返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunDeviceStreamRequest(AbstractModel):
    """RunDeviceStream請求參數結構體

    """

    def __init__(self):
        """
        :param Tids: 設備TID 清單
        :type Tids: list of str
        """
        self.Tids = None


    def _deserialize(self, params):
        self.Tids = params.get("Tids")


class RunDeviceStreamResponse(AbstractModel):
    """RunDeviceStream返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunIotModelRequest(AbstractModel):
    """RunIotModel請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param IotModel: 物模型定義，json格式的字串
        :type IotModel: str
        """
        self.ProductId = None
        self.IotModel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.IotModel = params.get("IotModel")


class RunIotModelResponse(AbstractModel):
    """RunIotModel返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunOtaVersionRequest(AbstractModel):
    """RunOtaVersion請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param OtaVersion: 固件版本號，格式爲x.y.z， x，y 範圍0-63，z範圍1~524288
        :type OtaVersion: str
        :param GrayValue: 灰度值,取值範圍0-100，爲0時相當於暫停發布
        :type GrayValue: int
        :param OldVersions: 指定的舊版本
        :type OldVersions: list of str
        :param Operator: 操作人
        :type Operator: str
        """
        self.ProductId = None
        self.OtaVersion = None
        self.GrayValue = None
        self.OldVersions = None
        self.Operator = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.GrayValue = params.get("GrayValue")
        self.OldVersions = params.get("OldVersions")
        self.Operator = params.get("Operator")


class RunOtaVersionResponse(AbstractModel):
    """RunOtaVersion返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunTestOtaVersionRequest(AbstractModel):
    """RunTestOtaVersion請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param OtaVersion: 固件版本號，格式爲x.y.z， x，y 範圍0-63，z範圍1~524288
        :type OtaVersion: str
        :param Tids: 指定可升級的設備TID
        :type Tids: list of str
        :param Operator: 操作人
        :type Operator: str
        """
        self.ProductId = None
        self.OtaVersion = None
        self.Tids = None
        self.Operator = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.Tids = params.get("Tids")
        self.Operator = params.get("Operator")


class RunTestOtaVersionResponse(AbstractModel):
    """RunTestOtaVersion返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SendOnlineMsgRequest(AbstractModel):
    """SendOnlineMsg請求參數結構體

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param Wakeup: 如果設備處於休眠狀态，是否喚醒設備
        :type Wakeup: bool
        :param WaitResp: 等待回應類型
0：不等待設備回應直接響應請求;
1：要求設備确認訊息已接收,或等待超時後返回;
2：要求設備進行響應處理,收到設備的響應數據後,将設備響應數據回應給請求方;
        :type WaitResp: int
        :param MsgTopic: 訊息主題
        :type MsgTopic: str
        :param MsgContent: 訊息内容，最大長度不超過8k位元
        :type MsgContent: str
        """
        self.Tid = None
        self.Wakeup = None
        self.WaitResp = None
        self.MsgTopic = None
        self.MsgContent = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.Wakeup = params.get("Wakeup")
        self.WaitResp = params.get("WaitResp")
        self.MsgTopic = params.get("MsgTopic")
        self.MsgContent = params.get("MsgContent")


class SendOnlineMsgResponse(AbstractModel):
    """SendOnlineMsg返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 若返回此項則表明需要用戶用此taskID進行查詢請求是否成功(只有waitresp不等於0的情況下才可能會返回該taskID項)
        :type TaskId: str
        :param Data: 設備響應訊息
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class SetMessageQueueRequest(AbstractModel):
    """SetMessageQueue請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param MsgQueueType: 訊息隊列類型 1-CMQ; 2-Ckafka
        :type MsgQueueType: int
        :param MsgType: 訊息類型,整型值（0-31）之間以“,”分隔
0：在線狀态變更
1.固件版本變更
2.設置參數變更
3.控制狀态變更
4.狀态訊息變更
5.事件發布
        :type MsgType: str
        :param Topic: 訊息隊列主題，不超過32字元
        :type Topic: str
        :param Instance: kafka訊息隊列的實例名，不超過64字元
        :type Instance: str
        :param MsgRegion: 訊息地域，不超過32字元
        :type MsgRegion: str
        """
        self.ProductId = None
        self.MsgQueueType = None
        self.MsgType = None
        self.Topic = None
        self.Instance = None
        self.MsgRegion = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.MsgQueueType = params.get("MsgQueueType")
        self.MsgType = params.get("MsgType")
        self.Topic = params.get("Topic")
        self.Instance = params.get("Instance")
        self.MsgRegion = params.get("MsgRegion")


class SetMessageQueueResponse(AbstractModel):
    """SetMessageQueue返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TraceStatus(AbstractModel):
    """布爾值，標識指定設備是否在白名單中

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param IsExist: 設備追蹤狀态
        :type IsExist: bool
        """
        self.Tid = None
        self.IsExist = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.IsExist = params.get("IsExist")


class UpgradeDeviceRequest(AbstractModel):
    """UpgradeDevice請求參數結構體

    """

    def __init__(self):
        """
        :param Tid: 設備TID
        :type Tid: str
        :param OtaVersion: 固件版本號
        :type OtaVersion: str
        :param UpgradeNow: 是否立即升級
        :type UpgradeNow: bool
        """
        self.Tid = None
        self.OtaVersion = None
        self.UpgradeNow = None


    def _deserialize(self, params):
        self.Tid = params.get("Tid")
        self.OtaVersion = params.get("OtaVersion")
        self.UpgradeNow = params.get("UpgradeNow")


class UpgradeDeviceResponse(AbstractModel):
    """UpgradeDevice返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備端返回的數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class UploadOtaVersionRequest(AbstractModel):
    """UploadOtaVersion請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param OtaVersion: 固件版本號，格式爲x.y.z， x，y 範圍0-63，z範圍1~524288
        :type OtaVersion: str
        :param VersionUrl: 固件版本URL
        :type VersionUrl: str
        :param FileSize: 文件大小，單位：byte
        :type FileSize: int
        :param Md5: 文件md5校驗碼（32字元）
        :type Md5: str
        :param Operator: 操作人
        :type Operator: str
        """
        self.ProductId = None
        self.OtaVersion = None
        self.VersionUrl = None
        self.FileSize = None
        self.Md5 = None
        self.Operator = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.VersionUrl = params.get("VersionUrl")
        self.FileSize = params.get("FileSize")
        self.Md5 = params.get("Md5")
        self.Operator = params.get("Operator")


class UploadOtaVersionResponse(AbstractModel):
    """UploadOtaVersion返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VersionData(AbstractModel):
    """固件版本詳細訊息

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param OtaVersion: 固件版本號
注意：此欄位可能返回 null，表示取不到有效值。
        :type OtaVersion: str
        :param PubStatus: 版本類型 1未發布 2測試發布 3正式發布 4禁用
注意：此欄位可能返回 null，表示取不到有效值。
        :type PubStatus: int
        :param VersionUrl: 固件版本儲存路徑URL
注意：此欄位可能返回 null，表示取不到有效值。
        :type VersionUrl: str
        :param FileSize: 文件大小，byte
注意：此欄位可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param Md5: 文件校驗碼
注意：此欄位可能返回 null，表示取不到有效值。
        :type Md5: str
        :param OldVersions: 指定的允許升級的舊版本，PubStatus=3時有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type OldVersions: str
        :param Tids: 指定的允許升級的舊設備id，PubStatus=2時有效
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tids: str
        :param GrayValue: 灰度值（0-100）,PubStatus=3時有效，表示n%的升級總量
注意：此欄位可能返回 null，表示取不到有效值。
        :type GrayValue: int
        :param PublishTime: 最近一次發布時間，UNIX時間戳，單位秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type PublishTime: int
        :param ActiveCount: 此版本啟動的設備總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ActiveCount: int
        :param OnlineCount: 此版本在線的設備總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type OnlineCount: int
        :param UpdateTime: 上傳固件文件的時間，UNIX時間戳，單位秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param UploadTime: 發布記錄的最後變更時間，UNIX時間戳，單位秒
注意：此欄位可能返回 null，表示取不到有效值。
        :type UploadTime: int
        :param ModifyTimes: 該固件版本發布的變更次數
注意：此欄位可能返回 null，表示取不到有效值。
        :type ModifyTimes: int
        """
        self.ProductId = None
        self.OtaVersion = None
        self.PubStatus = None
        self.VersionUrl = None
        self.FileSize = None
        self.Md5 = None
        self.OldVersions = None
        self.Tids = None
        self.GrayValue = None
        self.PublishTime = None
        self.ActiveCount = None
        self.OnlineCount = None
        self.UpdateTime = None
        self.UploadTime = None
        self.ModifyTimes = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.OtaVersion = params.get("OtaVersion")
        self.PubStatus = params.get("PubStatus")
        self.VersionUrl = params.get("VersionUrl")
        self.FileSize = params.get("FileSize")
        self.Md5 = params.get("Md5")
        self.OldVersions = params.get("OldVersions")
        self.Tids = params.get("Tids")
        self.GrayValue = params.get("GrayValue")
        self.PublishTime = params.get("PublishTime")
        self.ActiveCount = params.get("ActiveCount")
        self.OnlineCount = params.get("OnlineCount")
        self.UpdateTime = params.get("UpdateTime")
        self.UploadTime = params.get("UploadTime")
        self.ModifyTimes = params.get("ModifyTimes")