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


class CallDeviceActionAsyncRequest(AbstractModel):
    """CallDeviceActionAsync請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param ActionId: 動作Id
        :type ActionId: str
        :param InputParams: 輸入參數
        :type InputParams: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.ActionId = None
        self.InputParams = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ActionId = params.get("ActionId")
        self.InputParams = params.get("InputParams")


class CallDeviceActionAsyncResponse(AbstractModel):
    """CallDeviceActionAsync返回參數結構體

    """

    def __init__(self):
        """
        :param ClientToken: 調用Id
        :type ClientToken: str
        :param Status: 異步調用狀态
        :type Status: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ClientToken = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class CallDeviceActionSyncRequest(AbstractModel):
    """CallDeviceActionSync請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param ActionId: 動作Id
        :type ActionId: str
        :param InputParams: 輸入參數
        :type InputParams: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.ActionId = None
        self.InputParams = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ActionId = params.get("ActionId")
        self.InputParams = params.get("InputParams")


class CallDeviceActionSyncResponse(AbstractModel):
    """CallDeviceActionSync返回參數結構體

    """

    def __init__(self):
        """
        :param ClientToken: 調用Id
        :type ClientToken: str
        :param OutputParams: 輸出參數
注意：此欄位可能返回 null，表示取不到有效值。
        :type OutputParams: str
        :param Status: 返回狀态
        :type Status: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ClientToken = None
        self.OutputParams = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClientToken = params.get("ClientToken")
        self.OutputParams = params.get("OutputParams")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ControlDeviceDataRequest(AbstractModel):
    """ControlDeviceData請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param Data: 屬性數據, JSON格式字串, 注意欄位需要在物模型屬性裏定義
        :type Data: str
        :param Method: 請求類型 , 不填該參數或者 desired 表示下發屬性給設備,  reported 表示模拟設備上報屬性
        :type Method: str
        :param DeviceId: 設備ID，該欄位有值将代替 ProductId/DeviceName , 通常情況不需要填寫
        :type DeviceId: str
        :param DataTimestamp: 上報數據UNIX時間戳(毫秒), 僅對Method:reported有效
        :type DataTimestamp: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.Data = None
        self.Method = None
        self.DeviceId = None
        self.DataTimestamp = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Data = params.get("Data")
        self.Method = params.get("Method")
        self.DeviceId = params.get("DeviceId")
        self.DataTimestamp = params.get("DataTimestamp")


class ControlDeviceDataResponse(AbstractModel):
    """ControlDeviceData返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 返回訊息
        :type Data: str
        :param Result: JSON字串， 返回下發控制的結果訊息, 
Sent = 1 表示設備已經在線并且訂閱了控制下發的mqtt topic
注意：此欄位可能返回 null，表示取不到有效值。
        :type Result: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID。
        :type ProductId: str
        :param DeviceName: 設備名稱。命名規則：[a-zA-Z0-9:_-]{1,48}。
        :type DeviceName: str
        :param DevAddr: LoRaWAN 設備網址
        :type DevAddr: str
        :param AppKey: LoRaWAN 應用金鑰
        :type AppKey: str
        :param DevEUI: LoRaWAN 設備唯一标識
        :type DevEUI: str
        :param AppSKey: LoRaWAN 應用會話金鑰
        :type AppSKey: str
        :param NwkSKey: LoRaWAN 網絡會話金鑰
        :type NwkSKey: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DevAddr = None
        self.AppKey = None
        self.DevEUI = None
        self.AppSKey = None
        self.NwkSKey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DevAddr = params.get("DevAddr")
        self.AppKey = params.get("AppKey")
        self.DevEUI = params.get("DevEUI")
        self.AppSKey = params.get("AppSKey")
        self.NwkSKey = params.get("NwkSKey")


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備參數描述。
        :type Data: :class:`taifucloudcloud.iotexplorer.v20190423.models.DeviceData`
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


class CreateProjectRequest(AbstractModel):
    """CreateProject請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param ProjectDesc: 項目描述
        :type ProjectDesc: str
        """
        self.ProjectName = None
        self.ProjectDesc = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")


class CreateProjectResponse(AbstractModel):
    """CreateProject返回參數結構體

    """

    def __init__(self):
        """
        :param Project: 返回訊息
        :type Project: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProjectEntry`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntry()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class CreateStudioProductRequest(AbstractModel):
    """CreateStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductName: 産品名稱，名稱不能和已經存在的産品名稱重複。命名規則：[a-zA-Z0-9:_-]{1,32}
        :type ProductName: str
        :param CategoryId: 産品分組範本ID , ( 自定義範本填寫1 , 控制台調用會使用預置的其他ID)
        :type CategoryId: int
        :param ProductType: 産品類型 填寫 ( 0 普通産品 )
        :type ProductType: int
        :param EncryptionType: 加密類型 加密類型，1表示證書認證，2表示簽名認證。
        :type EncryptionType: str
        :param NetType: 連接類型 可以填寫 wifi cellular else
        :type NetType: str
        :param DataProtocol: 數據協議 (1 使用物模型 2 爲自定義)
        :type DataProtocol: int
        :param ProductDesc: 産品描述
        :type ProductDesc: str
        :param ProjectId: 産品的項目ID
        :type ProjectId: str
        """
        self.ProductName = None
        self.CategoryId = None
        self.ProductType = None
        self.EncryptionType = None
        self.NetType = None
        self.DataProtocol = None
        self.ProductDesc = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.CategoryId = params.get("CategoryId")
        self.ProductType = params.get("ProductType")
        self.EncryptionType = params.get("EncryptionType")
        self.NetType = params.get("NetType")
        self.DataProtocol = params.get("DataProtocol")
        self.ProductDesc = params.get("ProductDesc")
        self.ProjectId = params.get("ProjectId")


class CreateStudioProductResponse(AbstractModel):
    """CreateStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Product: 産品描述
        :type Product: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID。
        :type ProductId: str
        :param DeviceName: 設備名稱。
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


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


class DeleteProjectRequest(AbstractModel):
    """DeleteProject請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStudioProductRequest(AbstractModel):
    """DeleteStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DeleteStudioProductResponse(AbstractModel):
    """DeleteStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataHistoryRequest(AbstractModel):
    """DescribeDeviceDataHistory請求參數結構體

    """

    def __init__(self):
        """
        :param MinTime: 區間開始時間（Unix 時間戳，毫秒級）
        :type MinTime: int
        :param MaxTime: 區間結束時間（Unix 時間戳，毫秒級）
        :type MaxTime: int
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param FieldName: 屬性欄位名稱，對應數據範本中功能屬性的标識符
        :type FieldName: str
        :param Limit: 返回條數
        :type Limit: int
        :param Context: 檢索上下文
        :type Context: str
        """
        self.MinTime = None
        self.MaxTime = None
        self.ProductId = None
        self.DeviceName = None
        self.FieldName = None
        self.Limit = None
        self.Context = None


    def _deserialize(self, params):
        self.MinTime = params.get("MinTime")
        self.MaxTime = params.get("MaxTime")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.FieldName = params.get("FieldName")
        self.Limit = params.get("Limit")
        self.Context = params.get("Context")


class DescribeDeviceDataHistoryResponse(AbstractModel):
    """DescribeDeviceDataHistory返回參數結構體

    """

    def __init__(self):
        """
        :param FieldName: 屬性欄位名稱，對應數據範本中功能屬性的标識符
注意：此欄位可能返回 null，表示取不到有效值。
        :type FieldName: str
        :param Listover: 數據是否已全部返回，true 表示數據全部返回，false 表示還有數據待返回，可将 Context 作爲入參，繼續查詢返回結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param Context: 檢索上下文，當 ListOver 爲false時，可以用此上下文，繼續讀取後續數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Context: str
        :param Results: 曆史數據結果數組，返回對應時間點及取值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Results: list of DeviceDataHistoryItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FieldName = None
        self.Listover = None
        self.Context = None
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FieldName = params.get("FieldName")
        self.Listover = params.get("Listover")
        self.Context = params.get("Context")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = DeviceDataHistoryItem()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceDataRequest(AbstractModel):
    """DescribeDeviceData請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param DeviceId: 設備ID，該欄位有值将代替 ProductId/DeviceName
        :type DeviceId: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceId = params.get("DeviceId")


class DescribeDeviceDataResponse(AbstractModel):
    """DescribeDeviceData返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備數據
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名
        :type DeviceName: str
        :param DeviceId: 設備ID，該欄位有值将代替 ProductId/DeviceName
        :type DeviceId: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceId = params.get("DeviceId")


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回參數結構體

    """

    def __init__(self):
        """
        :param Device: 設備訊息
        :type Device: :class:`taifucloudcloud.iotexplorer.v20190423.models.DeviceInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = DeviceInfo()
            self.Device._deserialize(params.get("Device"))
        self.RequestId = params.get("RequestId")


class DescribeModelDefinitionRequest(AbstractModel):
    """DescribeModelDefinition請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeModelDefinitionResponse(AbstractModel):
    """DescribeModelDefinition返回參數結構體

    """

    def __init__(self):
        """
        :param Model: 産品數據範本
        :type Model: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProductModelDefinition`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Model = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self.Model = ProductModelDefinition()
            self.Model._deserialize(params.get("Model"))
        self.RequestId = params.get("RequestId")


class DescribeProjectRequest(AbstractModel):
    """DescribeProject請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")


class DescribeProjectResponse(AbstractModel):
    """DescribeProject返回參數結構體

    """

    def __init__(self):
        """
        :param Project: 返回訊息
        :type Project: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProjectEntryEx`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntryEx()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class DescribeStudioProductRequest(AbstractModel):
    """DescribeStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class DescribeStudioProductResponse(AbstractModel):
    """DescribeStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Product: 産品詳情
        :type Product: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class DeviceData(AbstractModel):
    """DeviceData

    """

    def __init__(self):
        """
        :param DeviceCert: 設備證書，用于 TLS 建立連結時校驗用戶端身份。采用非對稱加密時返回該參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeviceCert: str
        :param DeviceName: 設備名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param DevicePrivateKey: 設備私鑰，用于 TLS 建立連結時校驗用戶端身份，Top Cloud 後台不保存，請妥善保管。采用非對稱加密時返回該參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DevicePrivateKey: str
        :param DevicePsk: 對稱加密金鑰，base64編碼。采用對稱加密時返回該參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DevicePsk: str
        """
        self.DeviceCert = None
        self.DeviceName = None
        self.DevicePrivateKey = None
        self.DevicePsk = None


    def _deserialize(self, params):
        self.DeviceCert = params.get("DeviceCert")
        self.DeviceName = params.get("DeviceName")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.DevicePsk = params.get("DevicePsk")


class DeviceDataHistoryItem(AbstractModel):
    """設備曆史數據結構

    """

    def __init__(self):
        """
        :param Time: 時間點，毫秒時間戳
        :type Time: str
        :param Value: 欄位取值
        :type Value: str
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class DeviceInfo(AbstractModel):
    """設備詳細訊息

    """

    def __init__(self):
        """
        :param DeviceName: 設備名
        :type DeviceName: str
        :param Status: 0: 離線, 1: 在線, 2: 獲取失敗, 3 未啟動
        :type Status: int
        :param DevicePsk: 設備金鑰，金鑰加密的設備返回
        :type DevicePsk: str
        :param FirstOnlineTime: 首次上線時間
注意：此欄位可能返回 null，表示取不到有效值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param LoginTime: 最後一次上線時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type LoginTime: int
        :param CreateTime: 設備創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param Version: 設備固件版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type Version: str
        :param DeviceCert: 設備證書
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeviceCert: str
        :param LogLevel: 日志級别
注意：此欄位可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param DevAddr: LoRaWAN 設備網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type DevAddr: str
        :param AppKey: LoRaWAN 應用金鑰
注意：此欄位可能返回 null，表示取不到有效值。
        :type AppKey: str
        :param DevEUI: LoRaWAN 設備唯一标識
注意：此欄位可能返回 null，表示取不到有效值。
        :type DevEUI: str
        :param AppSKey: LoRaWAN 應用會話金鑰
注意：此欄位可能返回 null，表示取不到有效值。
        :type AppSKey: str
        :param NwkSKey: LoRaWAN 網絡會話金鑰
注意：此欄位可能返回 null，表示取不到有效值。
        :type NwkSKey: str
        """
        self.DeviceName = None
        self.Status = None
        self.DevicePsk = None
        self.FirstOnlineTime = None
        self.LoginTime = None
        self.CreateTime = None
        self.Version = None
        self.DeviceCert = None
        self.LogLevel = None
        self.DevAddr = None
        self.AppKey = None
        self.DevEUI = None
        self.AppSKey = None
        self.NwkSKey = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Status = params.get("Status")
        self.DevicePsk = params.get("DevicePsk")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LoginTime = params.get("LoginTime")
        self.CreateTime = params.get("CreateTime")
        self.Version = params.get("Version")
        self.DeviceCert = params.get("DeviceCert")
        self.LogLevel = params.get("LogLevel")
        self.DevAddr = params.get("DevAddr")
        self.AppKey = params.get("AppKey")
        self.DevEUI = params.get("DevEUI")
        self.AppSKey = params.get("AppSKey")
        self.NwkSKey = params.get("NwkSKey")


class EventHistoryItem(AbstractModel):
    """設備事件的搜索結果項

    """

    def __init__(self):
        """
        :param TimeStamp: 事件的時間戳
注意：此欄位可能返回 null，表示取不到有效值。
        :type TimeStamp: int
        :param ProductId: 事件的産品ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param DeviceName: 事件的設備名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeviceName: str
        :param EventId: 事件的标識符ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventId: str
        :param Type: 事件的類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: str
        :param Data: 事件的數據
注意：此欄位可能返回 null，表示取不到有效值。
        :type Data: str
        """
        self.TimeStamp = None
        self.ProductId = None
        self.DeviceName = None
        self.EventId = None
        self.Type = None
        self.Data = None


    def _deserialize(self, params):
        self.TimeStamp = params.get("TimeStamp")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.EventId = params.get("EventId")
        self.Type = params.get("Type")
        self.Data = params.get("Data")


class GetDeviceListRequest(AbstractModel):
    """GetDeviceList請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 需要檢視設備清單的産品 ID
        :type ProductId: str
        :param Offset: 分頁偏移
        :type Offset: int
        :param Limit: 分頁的大小，數值範圍 10-100
        :type Limit: int
        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetDeviceListResponse(AbstractModel):
    """GetDeviceList返回參數結構體

    """

    def __init__(self):
        """
        :param Devices: 返回的設備清單, 注意清單設備的 DevicePsk 爲空, 要獲取設備的 DevicePsk 請使用 DescribeDevice
注意：此欄位可能返回 null，表示取不到有效值。
        :type Devices: list of DeviceInfo
        :param Total: 産品下的設備總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Devices = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetProjectListRequest(AbstractModel):
    """GetProjectList請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 個數限制
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetProjectListResponse(AbstractModel):
    """GetProjectList返回參數結構體

    """

    def __init__(self):
        """
        :param Projects: 項目清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Projects: list of ProjectEntryEx
        :param Total: 清單項個數
注意：此欄位可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Projects = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = ProjectEntryEx()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetStudioProductListRequest(AbstractModel):
    """GetStudioProductList請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param DevStatus: 産品DevStatus
        :type DevStatus: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Limit
        :type Limit: int
        """
        self.ProjectId = None
        self.DevStatus = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.DevStatus = params.get("DevStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class GetStudioProductListResponse(AbstractModel):
    """GetStudioProductList返回參數結構體

    """

    def __init__(self):
        """
        :param Products: 産品清單
        :type Products: list of ProductEntry
        :param Total: 産品數量
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class ListEventHistoryRequest(AbstractModel):
    """ListEventHistory請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param Type: 搜索的事件類型：alert 表示告警，fault 表示故障，info 表示訊息，爲空則表示查詢上述所有類型事件
        :type Type: str
        :param StartTime: 起始時間（Unix 時間戳，秒級）, 爲0 表示 當前時間 - 24h
        :type StartTime: int
        :param EndTime: 結束時間（Unix 時間戳，秒級）, 爲0 表示當前時間
        :type EndTime: int
        :param Context: 搜索上下文, 用作查詢遊标
        :type Context: str
        :param Size: 單次獲取的曆史數據項目的最大數量
        :type Size: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Context = None
        self.Size = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Context = params.get("Context")
        self.Size = params.get("Size")


class ListEventHistoryResponse(AbstractModel):
    """ListEventHistory返回參數結構體

    """

    def __init__(self):
        """
        :param Context: 搜索上下文, 用作查詢遊标
注意：此欄位可能返回 null，表示取不到有效值。
        :type Context: str
        :param Total: 搜索結果數量
注意：此欄位可能返回 null，表示取不到有效值。
        :type Total: int
        :param Listover: 搜索結果是否已經結束
注意：此欄位可能返回 null，表示取不到有效值。
        :type Listover: bool
        :param EventHistory: 搜集結果集
注意：此欄位可能返回 null，表示取不到有效值。
        :type EventHistory: list of EventHistoryItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Context = None
        self.Total = None
        self.Listover = None
        self.EventHistory = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Total = params.get("Total")
        self.Listover = params.get("Listover")
        if params.get("EventHistory") is not None:
            self.EventHistory = []
            for item in params.get("EventHistory"):
                obj = EventHistoryItem()
                obj._deserialize(item)
                self.EventHistory.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyModelDefinitionRequest(AbstractModel):
    """ModifyModelDefinition請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ModelSchema: 數據範本定義
        :type ModelSchema: str
        """
        self.ProductId = None
        self.ModelSchema = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelSchema = params.get("ModelSchema")


class ModifyModelDefinitionResponse(AbstractModel):
    """ModifyModelDefinition返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param ProjectDesc: 項目描述
        :type ProjectDesc: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回參數結構體

    """

    def __init__(self):
        """
        :param Project: 項目詳情
        :type Project: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProjectEntry`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Project = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Project") is not None:
            self.Project = ProjectEntry()
            self.Project._deserialize(params.get("Project"))
        self.RequestId = params.get("RequestId")


class ModifyStudioProductRequest(AbstractModel):
    """ModifyStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ProductName: 産品名稱
        :type ProductName: str
        :param ProductDesc: 産品描述
        :type ProductDesc: str
        :param ModuleId: 模型ID
        :type ModuleId: int
        :param EnableProductScript: 是否打開二進制轉Json功能, 取值爲字串 true/false
        :type EnableProductScript: str
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductDesc = None
        self.ModuleId = None
        self.EnableProductScript = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.ProductDesc = params.get("ProductDesc")
        self.ModuleId = params.get("ModuleId")
        self.EnableProductScript = params.get("EnableProductScript")


class ModifyStudioProductResponse(AbstractModel):
    """ModifyStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Product: 産品描述
        :type Product: :class:`taifucloudcloud.iotexplorer.v20190423.models.ProductEntry`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = ProductEntry()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class ProductEntry(AbstractModel):
    """産品詳情

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ProductName: 産品名稱
        :type ProductName: str
        :param CategoryId: 産品分組範本ID
        :type CategoryId: int
        :param EncryptionType: 加密類型
        :type EncryptionType: str
        :param NetType: 連接類型
        :type NetType: str
        :param DataProtocol: 數據協議
        :type DataProtocol: int
        :param ProductDesc: 産品描述
        :type ProductDesc: str
        :param DevStatus: 狀态
        :type DevStatus: str
        :param CreateTime: 創建時間
        :type CreateTime: int
        :param UpdateTime: 更新時間
        :type UpdateTime: int
        :param Region: 區域
        :type Region: str
        :param ProductType: 産品類型
        :type ProductType: int
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ModuleId: 産品ModuleId
        :type ModuleId: int
        :param EnableProductScript: 是否使用腳本進行二進制轉json功能 可以取值 true / false
注意：此欄位可能返回 null，表示取不到有效值。
        :type EnableProductScript: str
        """
        self.ProductId = None
        self.ProductName = None
        self.CategoryId = None
        self.EncryptionType = None
        self.NetType = None
        self.DataProtocol = None
        self.ProductDesc = None
        self.DevStatus = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Region = None
        self.ProductType = None
        self.ProjectId = None
        self.ModuleId = None
        self.EnableProductScript = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        self.CategoryId = params.get("CategoryId")
        self.EncryptionType = params.get("EncryptionType")
        self.NetType = params.get("NetType")
        self.DataProtocol = params.get("DataProtocol")
        self.ProductDesc = params.get("ProductDesc")
        self.DevStatus = params.get("DevStatus")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Region = params.get("Region")
        self.ProductType = params.get("ProductType")
        self.ProjectId = params.get("ProjectId")
        self.ModuleId = params.get("ModuleId")
        self.EnableProductScript = params.get("EnableProductScript")


class ProductModelDefinition(AbstractModel):
    """産品模型定義

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ModelDefine: 模型定義
        :type ModelDefine: str
        :param UpdateTime: 更新時間，秒級時間戳
        :type UpdateTime: int
        :param CreateTime: 創建時間，秒級時間戳
        :type CreateTime: int
        :param CategoryModel: 産品所屬分類的模型快照（産品創建時刻的）
注意：此欄位可能返回 null，表示取不到有效值。
        :type CategoryModel: str
        """
        self.ProductId = None
        self.ModelDefine = None
        self.UpdateTime = None
        self.CreateTime = None
        self.CategoryModel = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ModelDefine = params.get("ModelDefine")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.CategoryModel = params.get("CategoryModel")


class ProjectEntry(AbstractModel):
    """項目詳情

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param ProjectDesc: 項目描述
        :type ProjectDesc: str
        :param CreateTime: 創建時間，unix時間戳
        :type CreateTime: int
        :param UpdateTime: 更新時間，unix時間戳
        :type UpdateTime: int
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class ProjectEntryEx(AbstractModel):
    """項目詳情

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ProjectName: 項目名稱
        :type ProjectName: str
        :param ProjectDesc: 項目描述
        :type ProjectDesc: str
        :param CreateTime: 項目創建時間，unix時間戳
        :type CreateTime: int
        :param UpdateTime: 項目更新時間，unix時間戳
        :type UpdateTime: int
        :param ProductCount: 産品數量
        :type ProductCount: int
        :param NativeAppCount: NativeApp數量
        :type NativeAppCount: int
        :param WebAppCount: WebApp數量
        :type WebAppCount: int
        """
        self.ProjectId = None
        self.ProjectName = None
        self.ProjectDesc = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ProductCount = None
        self.NativeAppCount = None
        self.WebAppCount = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.ProjectDesc = params.get("ProjectDesc")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ProductCount = params.get("ProductCount")
        self.NativeAppCount = params.get("NativeAppCount")
        self.WebAppCount = params.get("WebAppCount")


class ReleaseStudioProductRequest(AbstractModel):
    """ReleaseStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DevStatus: 産品DevStatus
        :type DevStatus: str
        """
        self.ProductId = None
        self.DevStatus = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DevStatus = params.get("DevStatus")


class ReleaseStudioProductResponse(AbstractModel):
    """ReleaseStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchStudioProductRequest(AbstractModel):
    """SearchStudioProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
        :type ProjectId: str
        :param ProductName: 産品名稱
        :type ProductName: str
        :param Limit: 清單Limit
        :type Limit: int
        :param Offset: 清單Offset
        :type Offset: int
        :param DevStatus: 産品Status
        :type DevStatus: str
        """
        self.ProjectId = None
        self.ProductName = None
        self.Limit = None
        self.Offset = None
        self.DevStatus = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProductName = params.get("ProductName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.DevStatus = params.get("DevStatus")


class SearchStudioProductResponse(AbstractModel):
    """SearchStudioProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Products: 産品清單
        :type Products: list of ProductEntry
        :param Total: 産品數量
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Products = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductEntry()
                obj._deserialize(item)
                self.Products.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")