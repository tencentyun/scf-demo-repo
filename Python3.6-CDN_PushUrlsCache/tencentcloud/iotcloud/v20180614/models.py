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


class Attribute(AbstractModel):
    """設備屬性

    """

    def __init__(self):
        """
        :param Tags: 屬性清單
        :type Tags: list of DeviceTag
        """
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)


class BatchPublishMessage(AbstractModel):
    """批次發訊息請求

    """

    def __init__(self):
        """
        :param Topic: 訊息發往的主題。爲 Topic 權限中去除 ProductID 和 DeviceName 的部分，如 “event”
        :type Topic: str
        :param Payload: 訊息内容
        :type Payload: str
        """
        self.Topic = None
        self.Payload = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")


class BatchUpdateShadow(AbstractModel):
    """批次更新設備影子任務

    """

    def __init__(self):
        """
        :param Desired: 設備影子的期望狀态，格式爲 Json 對象序列化之後的字串
        :type Desired: str
        """
        self.Desired = None


    def _deserialize(self, params):
        self.Desired = params.get("Desired")


class BindDevicesRequest(AbstractModel):
    """BindDevices請求參數結構體

    """

    def __init__(self):
        """
        :param GatewayProductId: 閘道設備的産品ID
        :type GatewayProductId: str
        :param GatewayDeviceName: 閘道設備的設備名
        :type GatewayDeviceName: str
        :param ProductId: 被綁定設備的産品ID
        :type ProductId: str
        :param DeviceNames: 被綁定的多個設備名
        :type DeviceNames: list of str
        :param Skey: 中興CLAA設備的綁定需要skey，普通的設備不需要
        :type Skey: str
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.ProductId = None
        self.DeviceNames = None
        self.Skey = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.Skey = params.get("Skey")


class BindDevicesResponse(AbstractModel):
    """BindDevices返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BrokerSubscribe(AbstractModel):
    """代理訂閱訊息

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class CancelTaskRequest(AbstractModel):
    """CancelTask請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 任務 ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class CancelTaskResponse(AbstractModel):
    """CancelTask返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDeviceRequest(AbstractModel):
    """CreateDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品 ID 。創建産品時Top Cloud 爲用戶分配全局唯一的 ID
        :type ProductId: str
        :param DeviceName: 設備名稱。命名規則：[a-zA-Z0-9:_-]{1,48}。
        :type DeviceName: str
        :param Attribute: 設備屬性
        :type Attribute: :class:`taifucloudcloud.iotcloud.v20180614.models.Attribute`
        :param DefinedPsk: 是否使用自定義PSK，預設不使用
        :type DefinedPsk: str
        :param Isp: 運營商類型，當産品是NB-IoT産品時，此欄位必填。1表示 電信，2表示  ，3表示  
        :type Isp: int
        :param Imei: IMEI，當産品是NB-IoT産品時，此欄位必填
        :type Imei: str
        :param LoraDevEui: LoRa設備的DevEui，當創建LoRa時，此欄位必填
        :type LoraDevEui: str
        :param LoraMoteType: LoRa設備的MoteType
        :type LoraMoteType: int
        :param Skey: 創建LoRa設備需要skey
        :type Skey: str
        :param LoraAppKey: LoRa設備的AppKey
        :type LoraAppKey: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Attribute = None
        self.DefinedPsk = None
        self.Isp = None
        self.Imei = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.Skey = None
        self.LoraAppKey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        if params.get("Attribute") is not None:
            self.Attribute = Attribute()
            self.Attribute._deserialize(params.get("Attribute"))
        self.DefinedPsk = params.get("DefinedPsk")
        self.Isp = params.get("Isp")
        self.Imei = params.get("Imei")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.Skey = params.get("Skey")
        self.LoraAppKey = params.get("LoraAppKey")


class CreateDeviceResponse(AbstractModel):
    """CreateDevice返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param DevicePsk: 對稱加密金鑰，base64編碼。采用對稱加密時返回該參數
        :type DevicePsk: str
        :param DeviceCert: 設備證書，用於 TLS 建立連結時校驗用戶端身份。采用非對稱加密時返回該參數
        :type DeviceCert: str
        :param DevicePrivateKey: 設備私鑰，用於 TLS 建立連結時校驗用戶端身份，Top Cloud 後台不保存，請妥善保管。采用非對稱加密時返回該參數
        :type DevicePrivateKey: str
        :param LoraDevEui: LoRa設備的DevEui，當設備是LoRa設備時，會返回該欄位
        :type LoraDevEui: str
        :param LoraMoteType: LoRa設備的MoteType，當設備是LoRa設備時，會返回該欄位
        :type LoraMoteType: int
        :param LoraAppKey: LoRa設備的AppKey，當設備是LoRa設備時，會返回該欄位
        :type LoraAppKey: str
        :param LoraNwkKey: LoRa設備的NwkKey，當設備是LoRa設備時，會返回該欄位
        :type LoraNwkKey: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceName = None
        self.DevicePsk = None
        self.DeviceCert = None
        self.DevicePrivateKey = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.LoraAppKey = None
        self.LoraNwkKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DevicePsk = params.get("DevicePsk")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.LoraAppKey = params.get("LoraAppKey")
        self.LoraNwkKey = params.get("LoraNwkKey")
        self.RequestId = params.get("RequestId")


class CreateLoraDeviceRequest(AbstractModel):
    """CreateLoraDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品 ID ，創建産品時Top Cloud 爲用戶分配全局唯一的 ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param DeviceType: 設備類型 ，目前支援A、B、C三種
        :type DeviceType: str
        :param AppEui: LoRa應用UUID
        :type AppEui: str
        :param DeviceEui: LoRa設備UUID
        :type DeviceEui: str
        :param AppKey: LoRa應用金鑰
        :type AppKey: str
        :param AuthKey: LoRa設備驗證金鑰
        :type AuthKey: str
        :param Memo: 設備備注
        :type Memo: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.DeviceType = None
        self.AppEui = None
        self.DeviceEui = None
        self.AppKey = None
        self.AuthKey = None
        self.Memo = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.DeviceType = params.get("DeviceType")
        self.AppEui = params.get("AppEui")
        self.DeviceEui = params.get("DeviceEui")
        self.AppKey = params.get("AppKey")
        self.AuthKey = params.get("AuthKey")
        self.Memo = params.get("Memo")


class CreateLoraDeviceResponse(AbstractModel):
    """CreateLoraDevice返回參數結構體

    """

    def __init__(self):
        """
        :param AppEui: LoRa應用UUID
        :type AppEui: str
        :param DeviceEui: LoRa設備UUID
        :type DeviceEui: str
        :param ClassType: 設備類型,目前支援A、B、C三種
        :type ClassType: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AppEui = None
        self.DeviceEui = None
        self.ClassType = None
        self.DeviceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppEui = params.get("AppEui")
        self.DeviceEui = params.get("DeviceEui")
        self.ClassType = params.get("ClassType")
        self.DeviceName = params.get("DeviceName")
        self.RequestId = params.get("RequestId")


class CreateMultiDeviceRequest(AbstractModel):
    """CreateMultiDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品 ID。創建産品時Top Cloud 爲用戶分配全局唯一的 ID
        :type ProductId: str
        :param DeviceNames: 批次創建的設備名數組，單次最多創建 100 個設備。命名規則：[a-zA-Z0-9:_-]{1,48}
        :type DeviceNames: list of str
        """
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")


class CreateMultiDeviceResponse(AbstractModel):
    """CreateMultiDevice返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID，Top Cloud 生成全局唯一的任務 ID，有效期一個月，一個月之後任務失效。可以調用獲取創建多設備任務狀态介面獲取該任務的執行狀态，當狀态爲成功時，可以調用獲取創建多設備任務結果介面獲取該任務的結果
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateProductRequest(AbstractModel):
    """CreateProduct請求參數結構體

    """

    def __init__(self):
        """
        :param ProductName: 産品名稱，名稱不能和已經存在的産品名稱重複。命名規則：[a-zA-Z0-9:_-]{1,32}
        :type ProductName: str
        :param ProductProperties: 産品屬性
        :type ProductProperties: :class:`taifucloudcloud.iotcloud.v20180614.models.ProductProperties`
        :param Skey: 創建CLAA産品時，需要Skey
        :type Skey: str
        """
        self.ProductName = None
        self.ProductProperties = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))
        self.Skey = params.get("Skey")


class CreateProductResponse(AbstractModel):
    """CreateProduct返回參數結構體

    """

    def __init__(self):
        """
        :param ProductName: 産品名稱
        :type ProductName: str
        :param ProductId: 産品 ID，Top Cloud 生成全局唯一 ID
        :type ProductId: str
        :param ProductProperties: 産品屬性
        :type ProductProperties: :class:`taifucloudcloud.iotcloud.v20180614.models.ProductProperties`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProductName = None
        self.ProductId = None
        self.ProductProperties = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProductName = params.get("ProductName")
        self.ProductId = params.get("ProductId")
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))
        self.RequestId = params.get("RequestId")


class CreateTaskRequest(AbstractModel):
    """CreateTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskType: 任務類型，取值爲 “UpdateShadow” 或者 “PublishMessage”
        :type TaskType: str
        :param ProductId: 執行任務的産品ID
        :type ProductId: str
        :param DeviceNameFilter: 執行任務的設備名的正規表示式
        :type DeviceNameFilter: str
        :param ScheduleTimeInSeconds: 任務開始執行的時間。 取值爲 Unix 時間戳，單位秒，且需大於等於當前時間時間戳，0爲系統當前時間時間戳，即立即執行，最大爲當前時間86400秒後，超過則取值爲當前時間86400秒後
        :type ScheduleTimeInSeconds: int
        :param Tasks: 任務描述細節，描述見下 Task
        :type Tasks: :class:`taifucloudcloud.iotcloud.v20180614.models.Task`
        :param MaxExecutionTimeInSeconds: 最長執行時間，單位秒，被調度後超過此時間仍未有結果則視爲任務失敗。取值爲0-86400，預設爲86400
        :type MaxExecutionTimeInSeconds: int
        """
        self.TaskType = None
        self.ProductId = None
        self.DeviceNameFilter = None
        self.ScheduleTimeInSeconds = None
        self.Tasks = None
        self.MaxExecutionTimeInSeconds = None


    def _deserialize(self, params):
        self.TaskType = params.get("TaskType")
        self.ProductId = params.get("ProductId")
        self.DeviceNameFilter = params.get("DeviceNameFilter")
        self.ScheduleTimeInSeconds = params.get("ScheduleTimeInSeconds")
        if params.get("Tasks") is not None:
            self.Tasks = Task()
            self.Tasks._deserialize(params.get("Tasks"))
        self.MaxExecutionTimeInSeconds = params.get("MaxExecutionTimeInSeconds")


class CreateTaskResponse(AbstractModel):
    """CreateTask返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 創建的任務ID
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateTopicPolicyRequest(AbstractModel):
    """CreateTopicPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param ProductID: 産品自身ID
        :type ProductID: str
        :param TopicName: Topic名稱
        :type TopicName: str
        :param Privilege: Topic權限，1發布，2訂閱，3訂閱和發布
        :type Privilege: int
        :param BrokerSubscribe: 代理訂閱訊息，閘道産品爲綁定的子産品創建topic時需要填寫，内容爲子産品的ID和設備訊息。
        :type BrokerSubscribe: :class:`taifucloudcloud.iotcloud.v20180614.models.BrokerSubscribe`
        """
        self.ProductID = None
        self.TopicName = None
        self.Privilege = None
        self.BrokerSubscribe = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.TopicName = params.get("TopicName")
        self.Privilege = params.get("Privilege")
        if params.get("BrokerSubscribe") is not None:
            self.BrokerSubscribe = BrokerSubscribe()
            self.BrokerSubscribe._deserialize(params.get("BrokerSubscribe"))


class CreateTopicPolicyResponse(AbstractModel):
    """CreateTopicPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTopicRuleRequest(AbstractModel):
    """CreateTopicRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleName: 規則名稱
        :type RuleName: str
        :param TopicRulePayload: 規則内容
        :type TopicRulePayload: :class:`taifucloudcloud.iotcloud.v20180614.models.TopicRulePayload`
        """
        self.RuleName = None
        self.TopicRulePayload = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("TopicRulePayload") is not None:
            self.TopicRulePayload = TopicRulePayload()
            self.TopicRulePayload._deserialize(params.get("TopicRulePayload"))


class CreateTopicRuleResponse(AbstractModel):
    """CreateTopicRule返回參數結構體

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
        :param ProductId: 設備所屬的産品 ID
        :type ProductId: str
        :param DeviceName: 需要删除的設備名稱
        :type DeviceName: str
        :param Skey: 删除LoRa設備以及LoRa閘道設備需要skey
        :type Skey: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Skey = params.get("Skey")


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


class DeleteLoraDeviceRequest(AbstractModel):
    """DeleteLoraDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 設備所屬産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DeleteLoraDeviceResponse(AbstractModel):
    """DeleteLoraDevice返回參數結構體

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
        :param ProductId: 需要删除的産品 ID
        :type ProductId: str
        :param Skey: 删除LoRa産品需要skey
        :type Skey: str
        """
        self.ProductId = None
        self.Skey = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Skey = params.get("Skey")


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


class DeleteTopicRuleRequest(AbstractModel):
    """DeleteTopicRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleName: 規則名
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class DeleteTopicRuleResponse(AbstractModel):
    """DeleteTopicRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeviceClientKeyRequest(AbstractModel):
    """DescribeDeviceClientKey請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 所屬産品的Id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceClientKeyResponse(AbstractModel):
    """DescribeDeviceClientKey返回參數結構體

    """

    def __init__(self):
        """
        :param ClientKey: 設備的私鑰
        :type ClientKey: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ClientKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClientKey = params.get("ClientKey")
        self.RequestId = params.get("RequestId")


class DescribeDeviceRequest(AbstractModel):
    """DescribeDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductID: 産品ID
        :type ProductID: str
        :param DeviceName: 設備名
        :type DeviceName: str
        """
        self.ProductID = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceResponse(AbstractModel):
    """DescribeDevice返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceName: 設備名
        :type DeviceName: str
        :param Online: 設備是否在線，0不在線，1在線
        :type Online: int
        :param LoginTime: 設備登入時間
        :type LoginTime: int
        :param Version: 設備固件版本
        :type Version: str
        :param LastUpdateTime: 設備最後更新時間
        :type LastUpdateTime: int
        :param DeviceCert: 設備證書
        :type DeviceCert: str
        :param DevicePsk: 設備金鑰
        :type DevicePsk: str
        :param Tags: 設備屬性
        :type Tags: list of DeviceTag
        :param DeviceType: 設備類型
        :type DeviceType: int
        :param Imei: IMEI
        :type Imei: str
        :param Isp: 運營商類型
        :type Isp: int
        :param ConnIP: IP網址
        :type ConnIP: int
        :param NbiotDeviceID: NB IoT運營商處的DeviceID
        :type NbiotDeviceID: str
        :param LoraDevEui: Lora設備的dev eui
        :type LoraDevEui: str
        :param LoraMoteType: Lora設備的mote type
        :type LoraMoteType: int
        :param LogLevel: 設備的sdk日志等級
注意：此欄位可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param FirstOnlineTime: 首次上線時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param LastOfflineTime: 最近下線時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastOfflineTime: int
        :param CreateTime: 設備創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param CertState: 設備證書獲取狀态，0 未獲取過設備金鑰, 1 已獲取過設備金鑰
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertState: int
        :param EnableState: 設備啓用狀态
注意：此欄位可能返回 null，表示取不到有效值。
        :type EnableState: int
        :param Labels: 設備標簽
注意：此欄位可能返回 null，表示取不到有效值。
        :type Labels: list of DeviceLabel
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.Version = None
        self.LastUpdateTime = None
        self.DeviceCert = None
        self.DevicePsk = None
        self.Tags = None
        self.DeviceType = None
        self.Imei = None
        self.Isp = None
        self.ConnIP = None
        self.NbiotDeviceID = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.LogLevel = None
        self.FirstOnlineTime = None
        self.LastOfflineTime = None
        self.CreateTime = None
        self.CertState = None
        self.EnableState = None
        self.Labels = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.Version = params.get("Version")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeviceType = params.get("DeviceType")
        self.Imei = params.get("Imei")
        self.Isp = params.get("Isp")
        self.ConnIP = params.get("ConnIP")
        self.NbiotDeviceID = params.get("NbiotDeviceID")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.LogLevel = params.get("LogLevel")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LastOfflineTime = params.get("LastOfflineTime")
        self.CreateTime = params.get("CreateTime")
        self.CertState = params.get("CertState")
        self.EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceShadowRequest(AbstractModel):
    """DescribeDeviceShadow請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品 ID
        :type ProductId: str
        :param DeviceName: 設備名稱。命名規則：[a-zA-Z0-9:_-]{1,48}
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeDeviceShadowResponse(AbstractModel):
    """DescribeDeviceShadow返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備影子數據
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 需要檢視設備清單的産品 ID
        :type ProductId: str
        :param Offset: 偏移量，Offset從0開始
        :type Offset: int
        :param Limit: 分頁的大小，數值範圍 10-250
        :type Limit: int
        :param FirmwareVersion: 設備固件版本號，若不帶此參數會返回所有固件版本的設備
        :type FirmwareVersion: str
        """
        self.ProductId = None
        self.Offset = None
        self.Limit = None
        self.FirmwareVersion = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FirmwareVersion = params.get("FirmwareVersion")


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 設備總數
        :type TotalCount: int
        :param Devices: 設備詳細訊息清單
        :type Devices: list of DeviceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Devices = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Devices") is not None:
            self.Devices = []
            for item in params.get("Devices"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.Devices.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoraDeviceRequest(AbstractModel):
    """DescribeLoraDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        """
        self.ProductId = None
        self.DeviceName = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")


class DescribeLoraDeviceResponse(AbstractModel):
    """DescribeLoraDevice返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param AppEui: LoRa應用UUID
        :type AppEui: str
        :param DeviceEui: LoRa設備UUID
        :type DeviceEui: str
        :param AppKey: LoRa應用金鑰
        :type AppKey: str
        :param ClassType: 設備類型,目前支援A、B、C三種
        :type ClassType: str
        :param ProductId: 設備所屬産品id
        :type ProductId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceName = None
        self.AppEui = None
        self.DeviceEui = None
        self.AppKey = None
        self.ClassType = None
        self.ProductId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.AppEui = params.get("AppEui")
        self.DeviceEui = params.get("DeviceEui")
        self.AppKey = params.get("AppKey")
        self.ClassType = params.get("ClassType")
        self.ProductId = params.get("ProductId")
        self.RequestId = params.get("RequestId")


class DescribeMultiDevTaskRequest(AbstractModel):
    """DescribeMultiDevTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID，由批次創建設備介面返回
        :type TaskId: str
        :param ProductId: 産品 ID，創建産品時Top Cloud 爲用戶分配全局唯一的 ID
        :type ProductId: str
        """
        self.TaskId = None
        self.ProductId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ProductId = params.get("ProductId")


class DescribeMultiDevTaskResponse(AbstractModel):
    """DescribeMultiDevTask返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID
        :type TaskId: str
        :param TaskStatus: 任務是否完成。0 代表任務未開始，1 代表任務正在執行，2 代表任務已完成
        :type TaskStatus: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.TaskStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskStatus = params.get("TaskStatus")
        self.RequestId = params.get("RequestId")


class DescribeMultiDevicesRequest(AbstractModel):
    """DescribeMultiDevices請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品 ID，創建産品時Top Cloud 爲用戶分配全局唯一的 ID
        :type ProductId: str
        :param TaskId: 任務 ID，由批次創建設備介面返回
        :type TaskId: str
        :param Offset: 分頁偏移
        :type Offset: int
        :param Limit: 分頁大小，每頁返回的設備個數
        :type Limit: int
        """
        self.ProductId = None
        self.TaskId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMultiDevicesResponse(AbstractModel):
    """DescribeMultiDevices返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務 ID，由批次創建設備介面返回
        :type TaskId: str
        :param DevicesInfo: 設備詳細訊息清單
        :type DevicesInfo: list of MultiDevicesInfo
        :param TotalDevNum: 該任務創建設備的總數
        :type TotalDevNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.DevicesInfo = None
        self.TotalDevNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("DevicesInfo") is not None:
            self.DevicesInfo = []
            for item in params.get("DevicesInfo"):
                obj = MultiDevicesInfo()
                obj._deserialize(item)
                self.DevicesInfo.append(obj)
        self.TotalDevNum = params.get("TotalDevNum")
        self.RequestId = params.get("RequestId")


class DescribeProductsRequest(AbstractModel):
    """DescribeProducts請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量，Offset從0開始
        :type Offset: int
        :param Limit: 分頁大小，當前頁面中顯示的最大數量，值範圍 10-250。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeProductsResponse(AbstractModel):
    """DescribeProducts返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 産品總數
        :type TotalCount: int
        :param Products: 産品詳細訊息清單
        :type Products: list of ProductInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Products = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Products") is not None:
            self.Products = []
            for item in params.get("Products"):
                obj = ProductInfo()
                obj._deserialize(item)
                self.Products.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 任務ID
        :type Id: str
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回參數結構體

    """

    def __init__(self):
        """
        :param Type: 任務類型，目前取值爲 “UpdateShadow” 或者 “PublishMessage”
        :type Type: str
        :param Id: 任務 ID
        :type Id: str
        :param ProductId: 産品 ID
        :type ProductId: str
        :param Status: 狀态。1表示等待處理，2表示調度處理中，3表示已完成，4表示失敗，5表示已取消
        :type Status: int
        :param CreateTime: 任務創建時間，Unix 時間戳
        :type CreateTime: int
        :param UpdateTime: 最後任務更新時間，Unix 時間戳
        :type UpdateTime: int
        :param DoneTime: 任務完成時間，Unix 時間戳
        :type DoneTime: int
        :param ScheduleTime: 被調度時間，Unix 時間戳
        :type ScheduleTime: int
        :param RetCode: 返回的錯誤碼
        :type RetCode: int
        :param ErrMsg: 返回的錯誤訊息
        :type ErrMsg: str
        :param Percent: 完成任務的設備比例
        :type Percent: int
        :param AllDeviceCnt: 比對到的需執行任務的設備數目
        :type AllDeviceCnt: int
        :param DoneDeviceCnt: 已完成任務的設備數目
        :type DoneDeviceCnt: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Type = None
        self.Id = None
        self.ProductId = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.DoneTime = None
        self.ScheduleTime = None
        self.RetCode = None
        self.ErrMsg = None
        self.Percent = None
        self.AllDeviceCnt = None
        self.DoneDeviceCnt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.DoneTime = params.get("DoneTime")
        self.ScheduleTime = params.get("ScheduleTime")
        self.RetCode = params.get("RetCode")
        self.ErrMsg = params.get("ErrMsg")
        self.Percent = params.get("Percent")
        self.AllDeviceCnt = params.get("AllDeviceCnt")
        self.DoneDeviceCnt = params.get("DoneDeviceCnt")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量，從0開始
        :type Offset: int
        :param Limit: 分頁的大小，數值範圍 1-250
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 用戶一個月内創建的任務總數
        :type TotalCount: int
        :param Tasks: 此頁任務對象的數組，按創建時間排序
        :type Tasks: list of TaskInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """設備詳細訊息

    """

    def __init__(self):
        """
        :param DeviceName: 設備名
        :type DeviceName: str
        :param Online: 設備是否在線，0不在線，1在線
        :type Online: int
        :param LoginTime: 設備登入時間
        :type LoginTime: int
        :param Version: 設備版本
        :type Version: str
        :param DeviceCert: 設備證書，證書加密的設備返回
        :type DeviceCert: str
        :param DevicePsk: 設備金鑰，金鑰加密的設備返回
        :type DevicePsk: str
        :param Tags: 設備屬性
        :type Tags: list of DeviceTag
        :param DeviceType: 設備類型
        :type DeviceType: int
        :param Imei: IMEI
        :type Imei: str
        :param Isp: 運營商類型
        :type Isp: int
        :param NbiotDeviceID: NB IOT運營商處的DeviceID
        :type NbiotDeviceID: str
        :param ConnIP: IP網址
        :type ConnIP: int
        :param LastUpdateTime: 設備最後更新時間
        :type LastUpdateTime: int
        :param LoraDevEui: LoRa設備的dev eui
        :type LoraDevEui: str
        :param LoraMoteType: LoRa設備的Mote type
        :type LoraMoteType: int
        :param FirstOnlineTime: 首次上線時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type FirstOnlineTime: int
        :param LastOfflineTime: 最近下線時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type LastOfflineTime: int
        :param CreateTime: 設備創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param LogLevel: 設備日志級别
注意：此欄位可能返回 null，表示取不到有效值。
        :type LogLevel: int
        :param CertState: 設備證書獲取狀态, 1 已獲取過設備金鑰，0 未獲取過設備金鑰
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertState: int
        :param EnableState: 設備可用狀态，0禁用，1啓用
注意：此欄位可能返回 null，表示取不到有效值。
        :type EnableState: int
        :param Labels: 設備標簽
注意：此欄位可能返回 null，表示取不到有效值。
        :type Labels: list of DeviceLabel
        """
        self.DeviceName = None
        self.Online = None
        self.LoginTime = None
        self.Version = None
        self.DeviceCert = None
        self.DevicePsk = None
        self.Tags = None
        self.DeviceType = None
        self.Imei = None
        self.Isp = None
        self.NbiotDeviceID = None
        self.ConnIP = None
        self.LastUpdateTime = None
        self.LoraDevEui = None
        self.LoraMoteType = None
        self.FirstOnlineTime = None
        self.LastOfflineTime = None
        self.CreateTime = None
        self.LogLevel = None
        self.CertState = None
        self.EnableState = None
        self.Labels = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.Online = params.get("Online")
        self.LoginTime = params.get("LoginTime")
        self.Version = params.get("Version")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePsk = params.get("DevicePsk")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = DeviceTag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeviceType = params.get("DeviceType")
        self.Imei = params.get("Imei")
        self.Isp = params.get("Isp")
        self.NbiotDeviceID = params.get("NbiotDeviceID")
        self.ConnIP = params.get("ConnIP")
        self.LastUpdateTime = params.get("LastUpdateTime")
        self.LoraDevEui = params.get("LoraDevEui")
        self.LoraMoteType = params.get("LoraMoteType")
        self.FirstOnlineTime = params.get("FirstOnlineTime")
        self.LastOfflineTime = params.get("LastOfflineTime")
        self.CreateTime = params.get("CreateTime")
        self.LogLevel = params.get("LogLevel")
        self.CertState = params.get("CertState")
        self.EnableState = params.get("EnableState")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = DeviceLabel()
                obj._deserialize(item)
                self.Labels.append(obj)


class DeviceLabel(AbstractModel):
    """設備標簽

    """

    def __init__(self):
        """
        :param Key: 標簽標識
        :type Key: str
        :param Value: 標簽值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class DeviceTag(AbstractModel):
    """設備屬性

    """

    def __init__(self):
        """
        :param Tag: 屬性名稱
        :type Tag: str
        :param Type: 屬性值的類型，1 int，2 string
        :type Type: int
        :param Value: 屬性的值
        :type Value: str
        """
        self.Tag = None
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Type = params.get("Type")
        self.Value = params.get("Value")


class DisableTopicRuleRequest(AbstractModel):
    """DisableTopicRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleName: 規則名稱
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class DisableTopicRuleResponse(AbstractModel):
    """DisableTopicRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableTopicRuleRequest(AbstractModel):
    """EnableTopicRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleName: 規則名稱
        :type RuleName: str
        """
        self.RuleName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")


class EnableTopicRuleResponse(AbstractModel):
    """EnableTopicRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MultiDevicesInfo(AbstractModel):
    """創建設備時返回的設備訊息

    """

    def __init__(self):
        """
        :param DeviceName: 設備名
        :type DeviceName: str
        :param DevicePsk: 對稱加密金鑰，base64 編碼，采用對稱加密時返回該參數
        :type DevicePsk: str
        :param DeviceCert: 設備證書，采用非對稱加密時返回該參數
        :type DeviceCert: str
        :param DevicePrivateKey: 設備私鑰，采用非對稱加密時返回該參數，Top Cloud 爲用戶快取起來，其生命週期與任務生命週期一緻
        :type DevicePrivateKey: str
        :param Result: 錯誤碼
        :type Result: int
        :param ErrMsg: 錯誤訊息
        :type ErrMsg: str
        """
        self.DeviceName = None
        self.DevicePsk = None
        self.DeviceCert = None
        self.DevicePrivateKey = None
        self.Result = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.DeviceName = params.get("DeviceName")
        self.DevicePsk = params.get("DevicePsk")
        self.DeviceCert = params.get("DeviceCert")
        self.DevicePrivateKey = params.get("DevicePrivateKey")
        self.Result = params.get("Result")
        self.ErrMsg = params.get("ErrMsg")


class ProductInfo(AbstractModel):
    """産品詳細訊息

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param ProductName: 産品名
        :type ProductName: str
        :param ProductMetadata: 産品中繼資料
        :type ProductMetadata: :class:`taifucloudcloud.iotcloud.v20180614.models.ProductMetadata`
        :param ProductProperties: 産品屬性
        :type ProductProperties: :class:`taifucloudcloud.iotcloud.v20180614.models.ProductProperties`
        """
        self.ProductId = None
        self.ProductName = None
        self.ProductMetadata = None
        self.ProductProperties = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.ProductName = params.get("ProductName")
        if params.get("ProductMetadata") is not None:
            self.ProductMetadata = ProductMetadata()
            self.ProductMetadata._deserialize(params.get("ProductMetadata"))
        if params.get("ProductProperties") is not None:
            self.ProductProperties = ProductProperties()
            self.ProductProperties._deserialize(params.get("ProductProperties"))


class ProductMetadata(AbstractModel):
    """産品中繼資料

    """

    def __init__(self):
        """
        :param CreationDate: 産品創建時間
        :type CreationDate: int
        """
        self.CreationDate = None


    def _deserialize(self, params):
        self.CreationDate = params.get("CreationDate")


class ProductProperties(AbstractModel):
    """産品屬性

    """

    def __init__(self):
        """
        :param ProductDescription: 産品描述
        :type ProductDescription: str
        :param EncryptionType: 加密類型，1表示證書認證，2表示簽名認證。如不填寫，預設值是1
        :type EncryptionType: str
        :param Region: 産品所屬區域，目前只支援 （gz）
        :type Region: str
        :param ProductType: 産品類型，各個類型值代表的節點-類型如下：
0 普通産品，2 NB-IoT産品，4 LoRa産品，3 LoRa閘道産品，5 普通閘道産品   預設值是0
        :type ProductType: int
        :param Format: 數據格式，取值爲json或者custom，預設值是json
        :type Format: str
        :param Platform: 産品所屬平台，預設值是0
        :type Platform: str
        :param Appeui: LoRa産品運營側APPEUI，只有LoRa産品需要填寫
        :type Appeui: str
        :param ModelId: 産品綁定的物模型ID，-1表示不綁定
        :type ModelId: str
        :param ModelName: 産品綁定的物模型名稱
        :type ModelName: str
        :param ProductKey: 産品金鑰，suite産品才會有
        :type ProductKey: str
        :param RegisterType: 動态注冊類型 0-關閉, 1-預定義設備名 2-動态定義設備名
        :type RegisterType: int
        :param ProductSecret: 動态注冊産品秘鑰
        :type ProductSecret: str
        :param RegisterLimit: RegisterType爲2時，設備動态創建的限制數量
        :type RegisterLimit: int
        """
        self.ProductDescription = None
        self.EncryptionType = None
        self.Region = None
        self.ProductType = None
        self.Format = None
        self.Platform = None
        self.Appeui = None
        self.ModelId = None
        self.ModelName = None
        self.ProductKey = None
        self.RegisterType = None
        self.ProductSecret = None
        self.RegisterLimit = None


    def _deserialize(self, params):
        self.ProductDescription = params.get("ProductDescription")
        self.EncryptionType = params.get("EncryptionType")
        self.Region = params.get("Region")
        self.ProductType = params.get("ProductType")
        self.Format = params.get("Format")
        self.Platform = params.get("Platform")
        self.Appeui = params.get("Appeui")
        self.ModelId = params.get("ModelId")
        self.ModelName = params.get("ModelName")
        self.ProductKey = params.get("ProductKey")
        self.RegisterType = params.get("RegisterType")
        self.ProductSecret = params.get("ProductSecret")
        self.RegisterLimit = params.get("RegisterLimit")


class PublishAsDeviceRequest(AbstractModel):
    """PublishAsDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param Port: LoRa 設備端口
        :type Port: int
        :param Payload: 訊息内容
        :type Payload: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Port = None
        self.Payload = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Port = params.get("Port")
        self.Payload = params.get("Payload")


class PublishAsDeviceResponse(AbstractModel):
    """PublishAsDevice返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PublishMessageRequest(AbstractModel):
    """PublishMessage請求參數結構體

    """

    def __init__(self):
        """
        :param Topic: 訊息發往的主題。命名規則：${ProductId}/${DeviceName}/[a-zA-Z0-9:_-]{1,128}
        :type Topic: str
        :param Payload: 訊息内容
        :type Payload: str
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param Qos: 服務質量等級，取值爲0或1
        :type Qos: int
        """
        self.Topic = None
        self.Payload = None
        self.ProductId = None
        self.DeviceName = None
        self.Qos = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Qos = params.get("Qos")


class PublishMessageResponse(AbstractModel):
    """PublishMessage返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PublishToDeviceRequest(AbstractModel):
    """PublishToDevice請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param Port: LoRa 端口
        :type Port: int
        :param Payload: 訊息内容
        :type Payload: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.Port = None
        self.Payload = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.Port = params.get("Port")
        self.Payload = params.get("Payload")


class PublishToDeviceResponse(AbstractModel):
    """PublishToDevice返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceTopicRuleRequest(AbstractModel):
    """ReplaceTopicRule請求參數結構體

    """

    def __init__(self):
        """
        :param RuleName: 規則名稱
        :type RuleName: str
        :param TopicRulePayload: 替換的規則包體
        :type TopicRulePayload: :class:`taifucloudcloud.iotcloud.v20180614.models.TopicRulePayload`
        :param ModifyType: 修改類型，0：其他，1：創建行爲，2：更新行爲，3：删除行爲
        :type ModifyType: int
        :param ActionIndex: action增删改變更填對應topicRulePayload裏面第幾個action
        :type ActionIndex: int
        """
        self.RuleName = None
        self.TopicRulePayload = None
        self.ModifyType = None
        self.ActionIndex = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("TopicRulePayload") is not None:
            self.TopicRulePayload = TopicRulePayload()
            self.TopicRulePayload._deserialize(params.get("TopicRulePayload"))
        self.ModifyType = params.get("ModifyType")
        self.ActionIndex = params.get("ActionIndex")


class ReplaceTopicRuleResponse(AbstractModel):
    """ReplaceTopicRule返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetDeviceStateRequest(AbstractModel):
    """ResetDeviceState請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceNames: 設備名稱
        :type DeviceNames: list of str
        """
        self.ProductId = None
        self.DeviceNames = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")


class ResetDeviceStateResponse(AbstractModel):
    """ResetDeviceState返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Task(AbstractModel):
    """任務描述細節

    """

    def __init__(self):
        """
        :param UpdateShadowTask: 批次更新影子任務的描述細節，當 taskType 取值爲 “UpdateShadow” 時，此欄位必填。描述見下 BatchUpdateShadow
        :type UpdateShadowTask: :class:`taifucloudcloud.iotcloud.v20180614.models.BatchUpdateShadow`
        :param PublishMessageTask: 批次下發訊息任務的描述細節，當 taskType 取值爲 “PublishMessage” 時，此欄位必填。描述見下 BatchPublishMessage
        :type PublishMessageTask: :class:`taifucloudcloud.iotcloud.v20180614.models.BatchPublishMessage`
        """
        self.UpdateShadowTask = None
        self.PublishMessageTask = None


    def _deserialize(self, params):
        if params.get("UpdateShadowTask") is not None:
            self.UpdateShadowTask = BatchUpdateShadow()
            self.UpdateShadowTask._deserialize(params.get("UpdateShadowTask"))
        if params.get("PublishMessageTask") is not None:
            self.PublishMessageTask = BatchPublishMessage()
            self.PublishMessageTask._deserialize(params.get("PublishMessageTask"))


class TaskInfo(AbstractModel):
    """任務清單詳細訊息

    """

    def __init__(self):
        """
        :param Type: 任務類型，目前取值爲 “UpdateShadow” 或者 “PublishMessage”
        :type Type: str
        :param Id: 任務 ID
        :type Id: str
        :param ProductId: 産品 ID
        :type ProductId: str
        :param Status: 狀态。1表示等待處理，2表示調度處理中，3表示已完成，4表示失敗，5表示已取消
        :type Status: int
        :param CreateTime: 任務創建時間，Unix 時間戳
        :type CreateTime: int
        :param UpdateTime: 最後任務更新時間，Unix 時間戳
        :type UpdateTime: int
        :param RetCode: 返回的錯誤碼
        :type RetCode: int
        :param ErrMsg: 返回的錯誤訊息
        :type ErrMsg: str
        """
        self.Type = None
        self.Id = None
        self.ProductId = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.RetCode = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")
        self.ProductId = params.get("ProductId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.RetCode = params.get("RetCode")
        self.ErrMsg = params.get("ErrMsg")


class TopicRulePayload(AbstractModel):
    """創建規則請求包體

    """

    def __init__(self):
        """
        :param Sql: 規則的SQL語句，如： SELECT * FROM 'pid/dname/event'，然後對其進行base64編碼，得：U0VMRUNUICogRlJPTSAncGlkL2RuYW1lL2V2ZW50Jw==
        :type Sql: str
        :param Actions: 行爲的JSON字串，大部分種類舉例如下：
[
    {
        "republish": {
            "topic": "TEST/test"
        }
    },
    {
        "forward": {
            "api": "http://127.0.0.1:8080"
        }
    },
    {
        "ckafka": {
            "instance": {
                "id": "ckafka-test",
                "name": ""
            },
            "topic": {
                "id": "topic-test",
                "name": "test"
            },
            "region": "gz"
        }
    },
    {
        "cmqqueue": {
            "queuename": "queue-test-TEST",
            "region": "gz"
        }
    },
    {
        "mysql": {
            "instanceid": "cdb-test",
            "region": "gz",
            "username": "test",
            "userpwd": "*****",
            "dbname": "d_mqtt",
            "tablename": "t_test",
            "fieldpairs": [
                {
                    "field": "test",
                    "value": "test"
                }
            ],
            "devicetype": "CUSTOM"
        }
    }
]
        :type Actions: str
        :param Description: 規則描述
        :type Description: str
        :param RuleDisabled: 是否禁用規則
        :type RuleDisabled: bool
        """
        self.Sql = None
        self.Actions = None
        self.Description = None
        self.RuleDisabled = None


    def _deserialize(self, params):
        self.Sql = params.get("Sql")
        self.Actions = params.get("Actions")
        self.Description = params.get("Description")
        self.RuleDisabled = params.get("RuleDisabled")


class UnbindDevicesRequest(AbstractModel):
    """UnbindDevices請求參數結構體

    """

    def __init__(self):
        """
        :param GatewayProductId: 閘道設備的産品ID
        :type GatewayProductId: str
        :param GatewayDeviceName: 閘道設備的設備名
        :type GatewayDeviceName: str
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceNames: 多個設備名
        :type DeviceNames: list of str
        :param Skey: 中興CLAA設備的解綁需要Skey，普通設備不需要
        :type Skey: str
        """
        self.GatewayProductId = None
        self.GatewayDeviceName = None
        self.ProductId = None
        self.DeviceNames = None
        self.Skey = None


    def _deserialize(self, params):
        self.GatewayProductId = params.get("GatewayProductId")
        self.GatewayDeviceName = params.get("GatewayDeviceName")
        self.ProductId = params.get("ProductId")
        self.DeviceNames = params.get("DeviceNames")
        self.Skey = params.get("Skey")


class UnbindDevicesResponse(AbstractModel):
    """UnbindDevices返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDeviceAvailableStateRequest(AbstractModel):
    """UpdateDeviceAvailableState請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 設備所屬産品id
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param EnableState: 要設置的設備狀态，1爲啓用，0爲禁用
        :type EnableState: int
        """
        self.ProductId = None
        self.DeviceName = None
        self.EnableState = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.EnableState = params.get("EnableState")


class UpdateDeviceAvailableStateResponse(AbstractModel):
    """UpdateDeviceAvailableState返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateDeviceShadowRequest(AbstractModel):
    """UpdateDeviceShadow請求參數結構體

    """

    def __init__(self):
        """
        :param ProductId: 産品ID
        :type ProductId: str
        :param DeviceName: 設備名稱
        :type DeviceName: str
        :param State: 虛拟設備的狀态，JSON字串格式，由desired結構組成
        :type State: str
        :param ShadowVersion: 當前版本號，需要和後台的version保持一緻，才能更新成功
        :type ShadowVersion: int
        :param Prefix: 下發delta訊息的topic前綴，可選類型: "$shadow","$template"。不填寫預設"$shadow"。
        :type Prefix: str
        """
        self.ProductId = None
        self.DeviceName = None
        self.State = None
        self.ShadowVersion = None
        self.Prefix = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DeviceName = params.get("DeviceName")
        self.State = params.get("State")
        self.ShadowVersion = params.get("ShadowVersion")
        self.Prefix = params.get("Prefix")


class UpdateDeviceShadowResponse(AbstractModel):
    """UpdateDeviceShadow返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 設備影子數據，JSON字串格式
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class UpdateTopicPolicyRequest(AbstractModel):
    """UpdateTopicPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param ProductID: 産品ID
        :type ProductID: str
        :param TopicName: 更新前Topic名
        :type TopicName: str
        :param NewTopicName: 更新後Topic名
        :type NewTopicName: str
        :param Privilege: Topic權限
        :type Privilege: int
        :param BrokerSubscribe: 代理訂閱訊息
        :type BrokerSubscribe: :class:`taifucloudcloud.iotcloud.v20180614.models.BrokerSubscribe`
        """
        self.ProductID = None
        self.TopicName = None
        self.NewTopicName = None
        self.Privilege = None
        self.BrokerSubscribe = None


    def _deserialize(self, params):
        self.ProductID = params.get("ProductID")
        self.TopicName = params.get("TopicName")
        self.NewTopicName = params.get("NewTopicName")
        self.Privilege = params.get("Privilege")
        if params.get("BrokerSubscribe") is not None:
            self.BrokerSubscribe = BrokerSubscribe()
            self.BrokerSubscribe._deserialize(params.get("BrokerSubscribe"))


class UpdateTopicPolicyResponse(AbstractModel):
    """UpdateTopicPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")