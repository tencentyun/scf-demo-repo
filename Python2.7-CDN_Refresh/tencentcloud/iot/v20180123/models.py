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


class Action(AbstractModel):
    """規則引擎轉發動作

    """

    def __init__(self):
        """
        :param Topic: 轉發至topic
注意：此欄位可能返回 null，表示取不到有效值。
        :type Topic: :class:`tencentcloud.iot.v20180123.models.TopicAction`
        :param Service: 轉發至第三發
注意：此欄位可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.iot.v20180123.models.ServiceAction`
        :param Ckafka: 轉發至第三發Ckafka
注意：此欄位可能返回 null，表示取不到有效值。
        :type Ckafka: :class:`tencentcloud.iot.v20180123.models.CkafkaAction`
        """
        self.Topic = None
        self.Service = None
        self.Ckafka = None


    def _deserialize(self, params):
        if params.get("Topic") is not None:
            self.Topic = TopicAction()
            self.Topic._deserialize(params.get("Topic"))
        if params.get("Service") is not None:
            self.Service = ServiceAction()
            self.Service._deserialize(params.get("Service"))
        if params.get("Ckafka") is not None:
            self.Ckafka = CkafkaAction()
            self.Ckafka._deserialize(params.get("Ckafka"))


class ActivateRuleRequest(AbstractModel):
    """ActivateRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 規則Id
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")


class ActivateRuleResponse(AbstractModel):
    """ActivateRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddDeviceRequest(AbstractModel):
    """AddDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱，唯一标識某産品下的一個設備
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class AddDeviceResponse(AbstractModel):
    """AddDevice返回參數結構體

    """

    def __init__(self):
        """
        :param Device: 設備訊息
        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        self.RequestId = params.get("RequestId")


class AddProductRequest(AbstractModel):
    """AddProduct請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 産品名稱，同一區域産品名稱需唯一，支援中文、英文字母、中劃線和下劃線，長度不超過31個字元，中文占兩個字元
        :type Name: str
        :param Description: 産品描述
        :type Description: str
        :param DataTemplate: 數據模版
        :type DataTemplate: list of DataTemplate
        :param DataProtocol: 産品版本（native表示基礎版，template表示高級版，預設值爲template）
        :type DataProtocol: str
        :param AuthType: 設備認證方式（1：動态令牌，2：簽名直連鑒權）
        :type AuthType: int
        :param CommProtocol: 通信方式（other/wifi/cellular/nb-iot）
        :type CommProtocol: str
        :param DeviceType: 産品的設備類型（device: 直連設備；sub_device：子設備；gateway：閘道設備）
        :type DeviceType: str
        """
        self.Name = None
        self.Description = None
        self.DataTemplate = None
        self.DataProtocol = None
        self.AuthType = None
        self.CommProtocol = None
        self.DeviceType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("DataTemplate") is not None:
            self.DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self.DataTemplate.append(obj)
        self.DataProtocol = params.get("DataProtocol")
        self.AuthType = params.get("AuthType")
        self.CommProtocol = params.get("CommProtocol")
        self.DeviceType = params.get("DeviceType")


class AddProductResponse(AbstractModel):
    """AddProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Product: 産品訊息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = Product()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class AddRuleRequest(AbstractModel):
    """AddRule請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 名稱
        :type Name: str
        :param Description: 描述
        :type Description: str
        :param Query: 查詢
        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        :param Actions: 轉發動作清單
        :type Actions: list of Action
        :param DataType: 數據類型（0：文本，1：二進制）
        :type DataType: int
        """
        self.Name = None
        self.Description = None
        self.Query = None
        self.Actions = None
        self.DataType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Query") is not None:
            self.Query = RuleQuery()
            self.Query._deserialize(params.get("Query"))
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        self.DataType = params.get("DataType")


class AddRuleResponse(AbstractModel):
    """AddRule返回參數結構體

    """

    def __init__(self):
        """
        :param Rule: 規則
        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self.Rule = Rule()
            self.Rule._deserialize(params.get("Rule"))
        self.RequestId = params.get("RequestId")


class AddTopicRequest(AbstractModel):
    """AddTopic請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param TopicName: Topic名稱
        :type TopicName: str
        """
        self.ProductId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TopicName = params.get("TopicName")


class AddTopicResponse(AbstractModel):
    """AddTopic返回參數結構體

    """

    def __init__(self):
        """
        :param Topic: Topic訊息
        :type Topic: :class:`tencentcloud.iot.v20180123.models.Topic`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Topic = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Topic") is not None:
            self.Topic = Topic()
            self.Topic._deserialize(params.get("Topic"))
        self.RequestId = params.get("RequestId")


class AppAddUserRequest(AbstractModel):
    """AppAddUser請求參數結構體

    """

    def __init__(self):
        """
        :param UserName: 用戶名
        :type UserName: str
        :param Password: 密碼
        :type Password: str
        """
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")


class AppAddUserResponse(AbstractModel):
    """AppAddUser返回參數結構體

    """

    def __init__(self):
        """
        :param AppUser: 應用用戶
        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AppUser = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppUser") is not None:
            self.AppUser = AppUser()
            self.AppUser._deserialize(params.get("AppUser"))
        self.RequestId = params.get("RequestId")


class AppDeleteDeviceRequest(AbstractModel):
    """AppDeleteDevice請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class AppDeleteDeviceResponse(AbstractModel):
    """AppDeleteDevice返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AppDevice(AbstractModel):
    """綁定設備

    """

    def __init__(self):
        """
        :param DeviceId: 設備Id
        :type DeviceId: str
        :param ProductId: 所屬産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param AliasName: 别名
        :type AliasName: str
        :param Region: 地區
        :type Region: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        """
        self.DeviceId = None
        self.ProductId = None
        self.DeviceName = None
        self.AliasName = None
        self.Region = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.AliasName = params.get("AliasName")
        self.Region = params.get("Region")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AppDeviceDetail(AbstractModel):
    """綁定設備詳情

    """

    def __init__(self):
        """
        :param DeviceId: 設備Id
        :type DeviceId: str
        :param ProductId: 所屬産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param AliasName: 别名
        :type AliasName: str
        :param Region: 地區
        :type Region: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        :param DeviceInfo: 設備訊息（json）
        :type DeviceInfo: str
        :param DataTemplate: 數據範本
        :type DataTemplate: list of DataTemplate
        """
        self.DeviceId = None
        self.ProductId = None
        self.DeviceName = None
        self.AliasName = None
        self.Region = None
        self.CreateTime = None
        self.UpdateTime = None
        self.DeviceInfo = None
        self.DataTemplate = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.AliasName = params.get("AliasName")
        self.Region = params.get("Region")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.DeviceInfo = params.get("DeviceInfo")
        if params.get("DataTemplate") is not None:
            self.DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self.DataTemplate.append(obj)


class AppGetDeviceDataRequest(AbstractModel):
    """AppGetDeviceData請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class AppGetDeviceDataResponse(AbstractModel):
    """AppGetDeviceData返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceData: 設備數據。
        :type DeviceData: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceData = params.get("DeviceData")
        self.RequestId = params.get("RequestId")


class AppGetDeviceRequest(AbstractModel):
    """AppGetDevice請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class AppGetDeviceResponse(AbstractModel):
    """AppGetDevice返回參數結構體

    """

    def __init__(self):
        """
        :param AppDevice: 綁定設備詳情
        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDeviceDetail`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AppDevice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppDevice") is not None:
            self.AppDevice = AppDeviceDetail()
            self.AppDevice._deserialize(params.get("AppDevice"))
        self.RequestId = params.get("RequestId")


class AppGetDeviceStatusesRequest(AbstractModel):
    """AppGetDeviceStatuses請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        :param DeviceIds: 設備Id清單（單次限制1000個設備）
        :type DeviceIds: list of str
        """
        self.AccessToken = None
        self.DeviceIds = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.DeviceIds = params.get("DeviceIds")


class AppGetDeviceStatusesResponse(AbstractModel):
    """AppGetDeviceStatuses返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceStatuses: 設備狀态
        :type DeviceStatuses: list of DeviceStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceStatuses = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceStatuses") is not None:
            self.DeviceStatuses = []
            for item in params.get("DeviceStatuses"):
                obj = DeviceStatus()
                obj._deserialize(item)
                self.DeviceStatuses.append(obj)
        self.RequestId = params.get("RequestId")


class AppGetDevicesRequest(AbstractModel):
    """AppGetDevices請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        """
        self.AccessToken = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")


class AppGetDevicesResponse(AbstractModel):
    """AppGetDevices返回參數結構體

    """

    def __init__(self):
        """
        :param Devices: 綁定設備清單
        :type Devices: list of AppDevice
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = AppDevice()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class AppGetTokenRequest(AbstractModel):
    """AppGetToken請求參數結構體

    """

    def __init__(self):
        """
        :param UserName: 用戶名
        :type UserName: str
        :param Password: 密碼
        :type Password: str
        :param Expire: TTL
        :type Expire: int
        """
        self.UserName = None
        self.Password = None
        self.Expire = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.Expire = params.get("Expire")


class AppGetTokenResponse(AbstractModel):
    """AppGetToken返回參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AccessToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.RequestId = params.get("RequestId")


class AppGetUserRequest(AbstractModel):
    """AppGetUser請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        """
        self.AccessToken = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")


class AppGetUserResponse(AbstractModel):
    """AppGetUser返回參數結構體

    """

    def __init__(self):
        """
        :param AppUser: 用戶訊息
        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AppUser = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppUser") is not None:
            self.AppUser = AppUser()
            self.AppUser._deserialize(params.get("AppUser"))
        self.RequestId = params.get("RequestId")


class AppIssueDeviceControlRequest(AbstractModel):
    """AppIssueDeviceControl請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param ControlData: 控制數據（json）
        :type ControlData: str
        :param Metadata: 是否發送metadata欄位
        :type Metadata: bool
        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None
        self.ControlData = None
        self.Metadata = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ControlData = params.get("ControlData")
        self.Metadata = params.get("Metadata")


class AppIssueDeviceControlResponse(AbstractModel):
    """AppIssueDeviceControl返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AppResetPasswordRequest(AbstractModel):
    """AppResetPassword請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        :param OldPassword: 舊密碼
        :type OldPassword: str
        :param NewPassword: 新密碼
        :type NewPassword: str
        """
        self.AccessToken = None
        self.OldPassword = None
        self.NewPassword = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.OldPassword = params.get("OldPassword")
        self.NewPassword = params.get("NewPassword")


class AppResetPasswordResponse(AbstractModel):
    """AppResetPassword返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AppSecureAddDeviceRequest(AbstractModel):
    """AppSecureAddDevice請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        :param DeviceSignature: 設備簽名
        :type DeviceSignature: str
        """
        self.AccessToken = None
        self.DeviceSignature = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.DeviceSignature = params.get("DeviceSignature")


class AppSecureAddDeviceResponse(AbstractModel):
    """AppSecureAddDevice返回參數結構體

    """

    def __init__(self):
        """
        :param AppDevice: 綁定設備訊息
        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDevice`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AppDevice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppDevice") is not None:
            self.AppDevice = AppDevice()
            self.AppDevice._deserialize(params.get("AppDevice"))
        self.RequestId = params.get("RequestId")


class AppUpdateDeviceRequest(AbstractModel):
    """AppUpdateDevice請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param AliasName: 設備别名
        :type AliasName: str
        """
        self.AccessToken = None
        self.ProductId = None
        self.DeviceName = None
        self.AliasName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.AliasName = params.get("AliasName")


class AppUpdateDeviceResponse(AbstractModel):
    """AppUpdateDevice返回參數結構體

    """

    def __init__(self):
        """
        :param AppDevice: 設備訊息
        :type AppDevice: :class:`tencentcloud.iot.v20180123.models.AppDevice`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AppDevice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppDevice") is not None:
            self.AppDevice = AppDevice()
            self.AppDevice._deserialize(params.get("AppDevice"))
        self.RequestId = params.get("RequestId")


class AppUpdateUserRequest(AbstractModel):
    """AppUpdateUser請求參數結構體

    """

    def __init__(self):
        """
        :param AccessToken: 訪問Token
        :type AccessToken: str
        :param NickName: 昵稱
        :type NickName: str
        """
        self.AccessToken = None
        self.NickName = None


    def _deserialize(self, params):
        self.AccessToken = params.get("AccessToken")
        self.NickName = params.get("NickName")


class AppUpdateUserResponse(AbstractModel):
    """AppUpdateUser返回參數結構體

    """

    def __init__(self):
        """
        :param AppUser: 應用用戶
        :type AppUser: :class:`tencentcloud.iot.v20180123.models.AppUser`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AppUser = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppUser") is not None:
            self.AppUser = AppUser()
            self.AppUser._deserialize(params.get("AppUser"))
        self.RequestId = params.get("RequestId")


class AppUser(AbstractModel):
    """應用用戶

    """

    def __init__(self):
        """
        :param ApplicationId: 應用Id
        :type ApplicationId: str
        :param UserName: 用戶名
        :type UserName: str
        :param NickName: 昵稱
        :type NickName: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 修改時間
        :type UpdateTime: str
        """
        self.ApplicationId = None
        self.UserName = None
        self.NickName = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.UserName = params.get("UserName")
        self.NickName = params.get("NickName")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class AssociateSubDeviceToGatewayProductRequest(AbstractModel):
    """AssociateSubDeviceToGatewayProduct請求參數結構體

    """

    def __init__(self):
        """
        :param SubDeviceProductId: 子設備産品Id
        :type SubDeviceProductId: str
        :param GatewayProductId: 閘道産品Id
        :type GatewayProductId: str
        """
        self.SubDeviceProductId = None
        self.GatewayProductId = None


    def _deserialize(self, params):
        self.SubDeviceProductId = params.get("SubDeviceProductId")
        self.GatewayProductId = params.get("GatewayProductId")


class AssociateSubDeviceToGatewayProductResponse(AbstractModel):
    """AssociateSubDeviceToGatewayProduct返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BoolData(AbstractModel):
    """布爾類型數據

    """

    def __init__(self):
        """
        :param Name: 名稱
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Mode: 讀寫模式
        :type Mode: str
        :param Range: 取值清單
        :type Range: list of bool
        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")


class CkafkaAction(AbstractModel):
    """轉發至Ckafka

    """

    def __init__(self):
        """
        :param InstanceId: 實例Id
        :type InstanceId: str
        :param TopicName: topic名稱
        :type TopicName: str
        :param Region: 地域
        :type Region: str
        """
        self.InstanceId = None
        self.TopicName = None
        self.Region = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.Region = params.get("Region")


class DataHistoryEntry(AbstractModel):
    """數據曆史條目

    """

    def __init__(self):
        """
        :param Id: 日志id
        :type Id: str
        :param Timestamp: 時間戳
        :type Timestamp: int
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param Data: 數據
        :type Data: str
        """
        self.Id = None
        self.Timestamp = None
        self.DeviceName = None
        self.Data = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Timestamp = params.get("Timestamp")
        self.DeviceName = params.get("DeviceName")
        self.Data = params.get("Data")


class DataTemplate(AbstractModel):
    """數據模版

    """

    def __init__(self):
        """
        :param Number: 數字類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Number: :class:`tencentcloud.iot.v20180123.models.NumberData`
        :param String: 字串類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type String: :class:`tencentcloud.iot.v20180123.models.StringData`
        :param Enum: 列舉類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Enum: :class:`tencentcloud.iot.v20180123.models.EnumData`
        :param Bool: 布爾類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Bool: :class:`tencentcloud.iot.v20180123.models.BoolData`
        """
        self.Number = None
        self.String = None
        self.Enum = None
        self.Bool = None


    def _deserialize(self, params):
        if params.get("Number") is not None:
            self.Number = NumberData()
            self.Number._deserialize(params.get("Number"))
        if params.get("String") is not None:
            self.String = StringData()
            self.String._deserialize(params.get("String"))
        if params.get("Enum") is not None:
            self.Enum = EnumData()
            self.Enum._deserialize(params.get("Enum"))
        if params.get("Bool") is not None:
            self.Bool = BoolData()
            self.Bool._deserialize(params.get("Bool"))


class DeactivateRuleRequest(AbstractModel):
    """DeactivateRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 規則Id
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")


class DeactivateRuleResponse(AbstractModel):
    """DeactivateRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DebugLogEntry(AbstractModel):
    """設備日志條目

    """

    def __init__(self):
        """
        :param Id: 日志id
        :type Id: str
        :param Event: 行爲（事件）
        :type Event: str
        :param LogType: shadow/action/mqtt, 分别表示：影子/規則引擎/上下線日志
        :type LogType: str
        :param Timestamp: 時間戳
        :type Timestamp: int
        :param Result: success/fail
        :type Result: str
        :param Data: 日志詳細内容
        :type Data: str
        :param Topic: 數據來源topic
        :type Topic: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.Id = None
        self.Event = None
        self.LogType = None
        self.Timestamp = None
        self.Result = None
        self.Data = None
        self.Topic = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Event = params.get("Event")
        self.LogType = params.get("LogType")
        self.Timestamp = params.get("Timestamp")
        self.Result = params.get("Result")
        self.Data = params.get("Data")
        self.Topic = params.get("Topic")
        self.DeviceName = params.get("DeviceName")


class DeleteDeviceRequest(AbstractModel):
    """DeleteDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
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


class DeleteProductRequest(AbstractModel):
    """DeleteProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
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


class DeleteRuleRequest(AbstractModel):
    """DeleteRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 規則Id
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic請求參數結構體

    """

    def __init__(self):
        """
        :param TopicId: TopicId
        :type TopicId: str
        :param ProductId: 産品Id
        :type ProductId: str
        """
        self.TopicId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.ProductId = params.get("ProductId")


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Device(AbstractModel):
    """設備

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param DeviceSecret: 設備金鑰
        :type DeviceSecret: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param DeviceInfo: 設備訊息（json）
        :type DeviceInfo: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceSecret = None
        self.UpdateTime = None
        self.CreateTime = None
        self.DeviceInfo = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceSecret = params.get("DeviceSecret")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.DeviceInfo = params.get("DeviceInfo")


class DeviceEntry(AbstractModel):
    """設備條目

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param DeviceSecret: 設備金鑰
        :type DeviceSecret: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceSecret = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceSecret = params.get("DeviceSecret")
        self.CreateTime = params.get("CreateTime")


class DeviceLogEntry(AbstractModel):
    """設備日志條目

    """

    def __init__(self):
        """
        :param Id: 日志id
        :type Id: str
        :param Msg: 日志内容
        :type Msg: str
        :param Code: 狀态碼
        :type Code: str
        :param Timestamp: 時間戳
        :type Timestamp: int
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param Method: 設備動作
        :type Method: str
        """
        self.Id = None
        self.Msg = None
        self.Code = None
        self.Timestamp = None
        self.DeviceName = None
        self.Method = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Msg = params.get("Msg")
        self.Code = params.get("Code")
        self.Timestamp = params.get("Timestamp")
        self.DeviceName = params.get("DeviceName")
        self.Method = params.get("Method")


class DeviceSignature(AbstractModel):
    """設備簽名

    """

    def __init__(self):
        """
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param DeviceSignature: 設備簽名
        :type DeviceSignature: str
        """
        self.DeviceName = None
        self.DeviceSignature = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DeviceSignature = params.get("DeviceSignature")


class DeviceStatData(AbstractModel):
    """設備統計數據

    """

    def __init__(self):
        """
        :param Datetime: 時間點
        :type Datetime: str
        :param DeviceOnline: 在線設備數
        :type DeviceOnline: int
        :param DeviceActive: 啟動設備數
        :type DeviceActive: int
        :param DeviceTotal: 設備總數
        :type DeviceTotal: int
        """
        self.Datetime = None
        self.DeviceOnline = None
        self.DeviceActive = None
        self.DeviceTotal = None


    def _deserialize(self, params):
        self.Datetime = params.get("Datetime")
        self.DeviceOnline = params.get("DeviceOnline")
        self.DeviceActive = params.get("DeviceActive")
        self.DeviceTotal = params.get("DeviceTotal")


class DeviceStatus(AbstractModel):
    """設備狀态

    """

    def __init__(self):
        """
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param Status: 設備狀态（inactive, online, offline）
        :type Status: str
        :param FirstOnline: 首次上線時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type FirstOnline: str
        :param LastOnline: 最後上線時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastOnline: str
        :param OnlineTimes: 上線次數
        :type OnlineTimes: int
        """
        self.DeviceName = None
        self.Status = None
        self.FirstOnline = None
        self.LastOnline = None
        self.OnlineTimes = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Status = params.get("Status")
        self.FirstOnline = params.get("FirstOnline")
        self.LastOnline = params.get("LastOnline")
        self.OnlineTimes = params.get("OnlineTimes")


class EnumData(AbstractModel):
    """列舉類型數據

    """

    def __init__(self):
        """
        :param Name: 名稱
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Mode: 讀寫模式
        :type Mode: str
        :param Range: 取值清單
        :type Range: list of str
        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")


class GetDataHistoryRequest(AbstractModel):
    """GetDataHistory請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceNames: 設備名稱清單，允許最多一次100台
        :type DeviceNames: list of str
        :param StartTime: 查詢開始時間
        :type StartTime: str
        :param EndTime: 查詢結束時間
        :type EndTime: str
        :param Size: 查詢數據量
        :type Size: int
        :param Order: 時間排序（desc/asc）
        :type Order: str
        :param ScrollId: 查詢遊标
        :type ScrollId: str
        """
        self.ProductId = None
        self.DeviceNames = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Order = None
        self.ScrollId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Order = params.get("Order")
        self.ScrollId = params.get("ScrollId")


class GetDataHistoryResponse(AbstractModel):
    """GetDataHistory返回參數結構體

    """

    def __init__(self):
        """
        :param DataHistory: 數據曆史
        :type DataHistory: list of DataHistoryEntry
        :param ScrollId: 查詢遊标
        :type ScrollId: str
        :param ScrollTimeout: 查詢遊标超時
        :type ScrollTimeout: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataHistory = None
        self.ScrollId = None
        self.ScrollTimeout = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataHistory") is not None:
            self.DataHistory = []
            for item in params.get("DataHistory"):
                obj = DataHistoryEntry()
                obj._deserialize(item)
                self.DataHistory.append(obj)
        self.ScrollId = params.get("ScrollId")
        self.ScrollTimeout = params.get("ScrollTimeout")
        self.RequestId = params.get("RequestId")


class GetDebugLogRequest(AbstractModel):
    """GetDebugLog請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceNames: 設備名稱清單，最大支援100台
        :type DeviceNames: list of str
        :param StartTime: 查詢開始時間
        :type StartTime: str
        :param EndTime: 查詢結束時間
        :type EndTime: str
        :param Size: 查詢數據量
        :type Size: int
        :param Order: 時間排序（desc/asc）
        :type Order: str
        :param ScrollId: 查詢遊标
        :type ScrollId: str
        :param Type: 日志類型（shadow/action/mqtt）
        :type Type: str
        """
        self.ProductId = None
        self.DeviceNames = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Order = None
        self.ScrollId = None
        self.Type = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Order = params.get("Order")
        self.ScrollId = params.get("ScrollId")
        self.Type = params.get("Type")


class GetDebugLogResponse(AbstractModel):
    """GetDebugLog返回參數結構體

    """

    def __init__(self):
        """
        :param DebugLog: 調試日志
        :type DebugLog: list of DebugLogEntry
        :param ScrollId: 查詢遊标
        :type ScrollId: str
        :param ScrollTimeout: 遊标超時
        :type ScrollTimeout: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DebugLog = None
        self.ScrollId = None
        self.ScrollTimeout = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DebugLog") is not None:
            self.DebugLog = []
            for item in params.get("DebugLog"):
                obj = DebugLogEntry()
                obj._deserialize(item)
                self.DebugLog.append(obj)
        self.ScrollId = params.get("ScrollId")
        self.ScrollTimeout = params.get("ScrollTimeout")
        self.RequestId = params.get("RequestId")


class GetDeviceDataRequest(AbstractModel):
    """GetDeviceData請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class GetDeviceDataResponse(AbstractModel):
    """GetDeviceData返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceData: 設備數據
        :type DeviceData: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceData = params.get("DeviceData")
        self.RequestId = params.get("RequestId")


class GetDeviceLogRequest(AbstractModel):
    """GetDeviceLog請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceNames: 設備名稱清單，最大支援100台
        :type DeviceNames: list of str
        :param StartTime: 查詢開始時間
        :type StartTime: str
        :param EndTime: 查詢結束時間
        :type EndTime: str
        :param Size: 查詢數據量
        :type Size: int
        :param Order: 時間排序（desc/asc）
        :type Order: str
        :param ScrollId: 查詢遊标
        :type ScrollId: str
        :param Type: 日志類型（comm/status）
        :type Type: str
        """
        self.ProductId = None
        self.DeviceNames = None
        self.StartTime = None
        self.EndTime = None
        self.Size = None
        self.Order = None
        self.ScrollId = None
        self.Type = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Size = params.get("Size")
        self.Order = params.get("Order")
        self.ScrollId = params.get("ScrollId")
        self.Type = params.get("Type")


class GetDeviceLogResponse(AbstractModel):
    """GetDeviceLog返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceLog: 設備日志
        :type DeviceLog: list of DeviceLogEntry
        :param ScrollId: 查詢遊标
        :type ScrollId: str
        :param ScrollTimeout: 遊标超時
        :type ScrollTimeout: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceLog = None
        self.ScrollId = None
        self.ScrollTimeout = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceLog") is not None:
            self.DeviceLog = []
            for item in params.get("DeviceLog"):
                obj = DeviceLogEntry()
                obj._deserialize(item)
                self.DeviceLog.append(obj)
        self.ScrollId = params.get("ScrollId")
        self.ScrollTimeout = params.get("ScrollTimeout")
        self.RequestId = params.get("RequestId")


class GetDeviceRequest(AbstractModel):
    """GetDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class GetDeviceResponse(AbstractModel):
    """GetDevice返回參數結構體

    """

    def __init__(self):
        """
        :param Device: 設備訊息
        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        self.RequestId = params.get("RequestId")


class GetDeviceSignaturesRequest(AbstractModel):
    """GetDeviceSignatures請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceNames: 設備名稱清單（單次限制1000個設備）
        :type DeviceNames: list of str
        :param Expire: 過期時間
        :type Expire: int
        """
        self.ProductId = None
        self.DeviceNames = None
        self.Expire = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.Expire = params.get("Expire")


class GetDeviceSignaturesResponse(AbstractModel):
    """GetDeviceSignatures返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceSignatures: 設備綁定簽名清單
        :type DeviceSignatures: list of DeviceSignature
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceSignatures = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceSignatures") is not None:
            self.DeviceSignatures = []
            for item in params.get("DeviceSignatures"):
                obj = DeviceSignature()
                obj._deserialize(item)
                self.DeviceSignatures.append(obj)
        self.RequestId = params.get("RequestId")


class GetDeviceStatisticsRequest(AbstractModel):
    """GetDeviceStatistics請求參數結構體

    """

    def __init__(self):
        """
        :param Products: 産品Id清單
        :type Products: list of str
        :param StartDate: 開始日期
        :type StartDate: str
        :param EndDate: 結束日期
        :type EndDate: str
        """
        self.Products = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.Products = params.get("Products")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class GetDeviceStatisticsResponse(AbstractModel):
    """GetDeviceStatistics返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceStatistics: 統計數據
        :type DeviceStatistics: list of DeviceStatData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceStatistics") is not None:
            self.DeviceStatistics = []
            for item in params.get("DeviceStatistics"):
                obj = DeviceStatData()
                obj._deserialize(item)
                self.DeviceStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class GetDeviceStatusesRequest(AbstractModel):
    """GetDeviceStatuses請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceNames: 設備名稱清單（單次限制1000個設備）
        :type DeviceNames: list of str
        """
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")


class GetDeviceStatusesResponse(AbstractModel):
    """GetDeviceStatuses返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceStatuses: 設備狀态清單
        :type DeviceStatuses: list of DeviceStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceStatuses = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceStatuses") is not None:
            self.DeviceStatuses = []
            for item in params.get("DeviceStatuses"):
                obj = DeviceStatus()
                obj._deserialize(item)
                self.DeviceStatuses.append(obj)
        self.RequestId = params.get("RequestId")


class GetDevicesRequest(AbstractModel):
    """GetDevices請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param Offset: 偏移
        :type Offset: int
        :param Length: 長度
        :type Length: int
        :param Keyword: 關鍵字查詢
        :type Keyword: str
        """
        self.ProductId = None
        self.Offset = None
        self.Length = None
        self.Keyword = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")
        self.Keyword = params.get("Keyword")


class GetDevicesResponse(AbstractModel):
    """GetDevices返回參數結構體

    """

    def __init__(self):
        """
        :param Devices: 設備清單
        :type Devices: list of DeviceEntry
        :param Total: 設備總數
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
                obj = DeviceEntry()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetProductRequest(AbstractModel):
    """GetProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        """
        self.ProductId = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")


class GetProductResponse(AbstractModel):
    """GetProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Product: 産品訊息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = Product()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class GetProductsRequest(AbstractModel):
    """GetProducts請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移
        :type Offset: int
        :param Length: 長度
        :type Length: int
        """
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")


class GetProductsResponse(AbstractModel):
    """GetProducts返回參數結構體

    """

    def __init__(self):
        """
        :param Products: Product清單
        :type Products: list of ProductEntry
        :param Total: Product總數
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


class GetRuleRequest(AbstractModel):
    """GetRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 規則Id
        :type RuleId: str
        """
        self.RuleId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")


class GetRuleResponse(AbstractModel):
    """GetRule返回參數結構體

    """

    def __init__(self):
        """
        :param Rule: 規則
        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self.Rule = Rule()
            self.Rule._deserialize(params.get("Rule"))
        self.RequestId = params.get("RequestId")


class GetRulesRequest(AbstractModel):
    """GetRules請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移
        :type Offset: int
        :param Length: 長度
        :type Length: int
        """
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")


class GetRulesResponse(AbstractModel):
    """GetRules返回參數結構體

    """

    def __init__(self):
        """
        :param Rules: 規則清單
        :type Rules: list of Rule
        :param Total: 規則總數
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = Rule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class GetTopicRequest(AbstractModel):
    """GetTopic請求參數結構體

    """

    def __init__(self):
        """
        :param TopicId: TopicId
        :type TopicId: str
        :param ProductId: 産品Id
        :type ProductId: str
        """
        self.TopicId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.ProductId = params.get("ProductId")


class GetTopicResponse(AbstractModel):
    """GetTopic返回參數結構體

    """

    def __init__(self):
        """
        :param Topic: Topic訊息
        :type Topic: :class:`tencentcloud.iot.v20180123.models.Topic`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Topic = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Topic") is not None:
            self.Topic = Topic()
            self.Topic._deserialize(params.get("Topic"))
        self.RequestId = params.get("RequestId")


class GetTopicsRequest(AbstractModel):
    """GetTopics請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param Offset: 偏移
        :type Offset: int
        :param Length: 長度
        :type Length: int
        """
        self.ProductId = None
        self.Offset = None
        self.Length = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Length = params.get("Length")


class GetTopicsResponse(AbstractModel):
    """GetTopics返回參數結構體

    """

    def __init__(self):
        """
        :param Topics: Topic清單
        :type Topics: list of Topic
        :param Total: Topic總數
        :type Total: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Topics = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = Topic()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class IssueDeviceControlRequest(AbstractModel):
    """IssueDeviceControl請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param ControlData: 控制數據（json）
        :type ControlData: str
        :param Metadata: 是否發送metadata欄位
        :type Metadata: bool
        """
        self.ProductId = None
        self.DeviceName = None
        self.ControlData = None
        self.Metadata = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.ControlData = params.get("ControlData")
        self.Metadata = params.get("Metadata")


class IssueDeviceControlResponse(AbstractModel):
    """IssueDeviceControl返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NumberData(AbstractModel):
    """數字類型數據

    """

    def __init__(self):
        """
        :param Name: 名稱
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Mode: 讀寫模式
        :type Mode: str
        :param Range: 取值範圍
        :type Range: list of float
        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")


class Product(AbstractModel):
    """産品

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param ProductKey: 産品Key
        :type ProductKey: str
        :param AppId: AppId
        :type AppId: int
        :param Name: 産品名稱
        :type Name: str
        :param Description: 産品描述
        :type Description: str
        :param Domain: 連接域名
        :type Domain: str
        :param Standard: 産品規格
        :type Standard: int
        :param AuthType: 鑒權類型（0：直連，1：Token）
        :type AuthType: int
        :param Deleted: 删除（0未删除）
        :type Deleted: int
        :param Message: 備注
        :type Message: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        :param DataTemplate: 數據模版
        :type DataTemplate: list of DataTemplate
        :param DataProtocol: 數據協議（native/template）
        :type DataProtocol: str
        :param Username: 直連用戶名
        :type Username: str
        :param Password: 直連密碼
        :type Password: str
        :param CommProtocol: 通信方式
        :type CommProtocol: str
        :param Qps: qps
        :type Qps: int
        :param Region: 地域
        :type Region: str
        :param DeviceType: 産品的設備類型
        :type DeviceType: str
        :param AssociatedProducts: 關聯的産品清單
        :type AssociatedProducts: list of str
        """
        self.ProductId = None
        self.ProductKey = None
        self.AppId = None
        self.Name = None
        self.Description = None
        self.Domain = None
        self.Standard = None
        self.AuthType = None
        self.Deleted = None
        self.Message = None
        self.CreateTime = None
        self.UpdateTime = None
        self.DataTemplate = None
        self.DataProtocol = None
        self.Username = None
        self.Password = None
        self.CommProtocol = None
        self.Qps = None
        self.Region = None
        self.DeviceType = None
        self.AssociatedProducts = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductKey = params.get("ProductKey")
        self.AppId = params.get("AppId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Domain = params.get("Domain")
        self.Standard = params.get("Standard")
        self.AuthType = params.get("AuthType")
        self.Deleted = params.get("Deleted")
        self.Message = params.get("Message")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("DataTemplate") is not None:
            self.DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self.DataTemplate.append(obj)
        self.DataProtocol = params.get("DataProtocol")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.CommProtocol = params.get("CommProtocol")
        self.Qps = params.get("Qps")
        self.Region = params.get("Region")
        self.DeviceType = params.get("DeviceType")
        self.AssociatedProducts = params.get("AssociatedProducts")


class ProductEntry(AbstractModel):
    """産品條目

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param ProductKey: 産品Key
        :type ProductKey: str
        :param AppId: AppId
        :type AppId: int
        :param Name: 産品名稱
        :type Name: str
        :param Description: 産品描述
        :type Description: str
        :param Domain: 連接域名
        :type Domain: str
        :param AuthType: 鑒權類型（0：直連，1：Token）
        :type AuthType: int
        :param DataProtocol: 數據協議（native/template）
        :type DataProtocol: str
        :param Deleted: 删除（0未删除）
        :type Deleted: int
        :param Message: 備注
        :type Message: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param CommProtocol: 通信方式
        :type CommProtocol: str
        :param Region: 地域
        :type Region: str
        :param DeviceType: 設備類型
        :type DeviceType: str
        """
        self.ProductId = None
        self.ProductKey = None
        self.AppId = None
        self.Name = None
        self.Description = None
        self.Domain = None
        self.AuthType = None
        self.DataProtocol = None
        self.Deleted = None
        self.Message = None
        self.CreateTime = None
        self.CommProtocol = None
        self.Region = None
        self.DeviceType = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductKey = params.get("ProductKey")
        self.AppId = params.get("AppId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.Domain = params.get("Domain")
        self.AuthType = params.get("AuthType")
        self.DataProtocol = params.get("DataProtocol")
        self.Deleted = params.get("Deleted")
        self.Message = params.get("Message")
        self.CreateTime = params.get("CreateTime")
        self.CommProtocol = params.get("CommProtocol")
        self.Region = params.get("Region")
        self.DeviceType = params.get("DeviceType")


class PublishMsgRequest(AbstractModel):
    """PublishMsg請求參數結構體

    """

    def __init__(self):
        """
        :param Topic: Topic
        :type Topic: str
        :param Message: 訊息内容
        :type Message: str
        :param Qos: Qos(目前QoS支援0與1)
        :type Qos: int
        """
        self.Topic = None
        self.Message = None
        self.Qos = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Message = params.get("Message")
        self.Qos = params.get("Qos")


class PublishMsgResponse(AbstractModel):
    """PublishMsg返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetDeviceRequest(AbstractModel):
    """ResetDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class ResetDeviceResponse(AbstractModel):
    """ResetDevice返回參數結構體

    """

    def __init__(self):
        """
        :param Device: 設備訊息
        :type Device: :class:`tencentcloud.iot.v20180123.models.Device`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Device = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Device") is not None:
            self.Device = Device()
            self.Device._deserialize(params.get("Device"))
        self.RequestId = params.get("RequestId")


class Rule(AbstractModel):
    """規則

    """

    def __init__(self):
        """
        :param RuleId: 規則Id
        :type RuleId: str
        :param AppId: AppId
        :type AppId: int
        :param Name: 名稱
        :type Name: str
        :param Description: 描述
        :type Description: str
        :param Query: 查詢
        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        :param Actions: 轉發
        :type Actions: list of Action
        :param Active: 已啓動
        :type Active: int
        :param Deleted: 已删除
        :type Deleted: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        :param MsgOrder: 訊息順序
        :type MsgOrder: int
        :param DataType: 數據類型（0：文本，1：二進制）
        :type DataType: int
        """
        self.RuleId = None
        self.AppId = None
        self.Name = None
        self.Description = None
        self.Query = None
        self.Actions = None
        self.Active = None
        self.Deleted = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MsgOrder = None
        self.DataType = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.AppId = params.get("AppId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Query") is not None:
            self.Query = RuleQuery()
            self.Query._deserialize(params.get("Query"))
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        self.Active = params.get("Active")
        self.Deleted = params.get("Deleted")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.MsgOrder = params.get("MsgOrder")
        self.DataType = params.get("DataType")


class RuleQuery(AbstractModel):
    """查詢

    """

    def __init__(self):
        """
        :param Field: 欄位
        :type Field: str
        :param Condition: 過濾規則
        :type Condition: str
        :param Topic: Topic
注意：此欄位可能返回 null，表示取不到有效值。
        :type Topic: str
        :param ProductId: 産品Id
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductId: str
        """
        self.Field = None
        self.Condition = None
        self.Topic = None
        self.ProductId = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Condition = params.get("Condition")
        self.Topic = params.get("Topic")
        self.ProductId = params.get("ProductId")


class ServiceAction(AbstractModel):
    """轉發到第三方http(s)服務

    """

    def __init__(self):
        """
        :param Url: 服務url網址
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")


class StringData(AbstractModel):
    """數字類型數據

    """

    def __init__(self):
        """
        :param Name: 名稱
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Mode: 讀寫模式
        :type Mode: str
        :param Range: 長度範圍
        :type Range: list of int non-negative
        """
        self.Name = None
        self.Desc = None
        self.Mode = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Mode = params.get("Mode")
        self.Range = params.get("Range")


class Topic(AbstractModel):
    """Topic

    """

    def __init__(self):
        """
        :param TopicId: TopicId
        :type TopicId: str
        :param TopicName: Topic名稱
        :type TopicName: str
        :param ProductId: 産品Id
        :type ProductId: str
        :param MsgLife: 訊息最大生命周期
        :type MsgLife: int
        :param MsgSize: 訊息最大大小
        :type MsgSize: int
        :param MsgCount: 訊息最大數量
        :type MsgCount: int
        :param Deleted: 已删除
        :type Deleted: int
        :param Path: Topic完整路徑
        :type Path: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param UpdateTime: 更新時間
        :type UpdateTime: str
        """
        self.TopicId = None
        self.TopicName = None
        self.ProductId = None
        self.MsgLife = None
        self.MsgSize = None
        self.MsgCount = None
        self.Deleted = None
        self.Path = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.ProductId = params.get("ProductId")
        self.MsgLife = params.get("MsgLife")
        self.MsgSize = params.get("MsgSize")
        self.MsgCount = params.get("MsgCount")
        self.Deleted = params.get("Deleted")
        self.Path = params.get("Path")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class TopicAction(AbstractModel):
    """轉發到topic動作

    """

    def __init__(self):
        """
        :param Topic: 目标topic
        :type Topic: str
        """
        self.Topic = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")


class UnassociateSubDeviceFromGatewayProductRequest(AbstractModel):
    """UnassociateSubDeviceFromGatewayProduct請求參數結構體

    """

    def __init__(self):
        """
        :param SubDeviceProductId: 子設備産品Id
        :type SubDeviceProductId: str
        :param GatewayProductId: 閘道設備産品Id
        :type GatewayProductId: str
        """
        self.SubDeviceProductId = None
        self.GatewayProductId = None


    def _deserialize(self, params):
        self.SubDeviceProductId = params.get("SubDeviceProductId")
        self.GatewayProductId = params.get("GatewayProductId")


class UnassociateSubDeviceFromGatewayProductResponse(AbstractModel):
    """UnassociateSubDeviceFromGatewayProduct返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateProductRequest(AbstractModel):
    """UpdateProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品Id
        :type ProductId: str
        :param Name: 産品名稱
        :type Name: str
        :param Description: 産品描述
        :type Description: str
        :param DataTemplate: 數據模版
        :type DataTemplate: list of DataTemplate
        """
        self.ProductId = None
        self.Name = None
        self.Description = None
        self.DataTemplate = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("DataTemplate") is not None:
            self.DataTemplate = []
            for item in params.get("DataTemplate"):
                obj = DataTemplate()
                obj._deserialize(item)
                self.DataTemplate.append(obj)


class UpdateProductResponse(AbstractModel):
    """UpdateProduct返回參數結構體

    """

    def __init__(self):
        """
        :param Product: 更新後的産品訊息
        :type Product: :class:`tencentcloud.iot.v20180123.models.Product`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Product = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Product") is not None:
            self.Product = Product()
            self.Product._deserialize(params.get("Product"))
        self.RequestId = params.get("RequestId")


class UpdateRuleRequest(AbstractModel):
    """UpdateRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleId: 規則Id
        :type RuleId: str
        :param Name: 名稱
        :type Name: str
        :param Description: 描述
        :type Description: str
        :param Query: 查詢
        :type Query: :class:`tencentcloud.iot.v20180123.models.RuleQuery`
        :param Actions: 轉發動作清單
        :type Actions: list of Action
        :param DataType: 數據類型（0：文本，1：二進制）
        :type DataType: int
        """
        self.RuleId = None
        self.Name = None
        self.Description = None
        self.Query = None
        self.Actions = None
        self.DataType = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        if params.get("Query") is not None:
            self.Query = RuleQuery()
            self.Query._deserialize(params.get("Query"))
        if params.get("Actions") is not None:
            self.Actions = []
            for item in params.get("Actions"):
                obj = Action()
                obj._deserialize(item)
                self.Actions.append(obj)
        self.DataType = params.get("DataType")


class UpdateRuleResponse(AbstractModel):
    """UpdateRule返回參數結構體

    """

    def __init__(self):
        """
        :param Rule: 規則
        :type Rule: :class:`tencentcloud.iot.v20180123.models.Rule`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Rule = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self.Rule = Rule()
            self.Rule._deserialize(params.get("Rule"))
        self.RequestId = params.get("RequestId")