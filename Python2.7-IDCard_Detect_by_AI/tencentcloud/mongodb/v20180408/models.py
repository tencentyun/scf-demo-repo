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


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour請求參數結構體

    """

    def __init__(self):
        """
        :param Memory: 實例内存大小，單位：GB
        :type Memory: int
        :param Volume: 實例硬碟大小，單位：GB
        :type Volume: int
        :param ReplicateSetNum: 副本集個數，1爲單副本集實例，大于1爲分片集群實例，最大不超過10
        :type ReplicateSetNum: int
        :param SecondaryNum: 每個副本集内從節點個數，目前只支援從節點數爲2
        :type SecondaryNum: int
        :param EngineVersion: MongoDB引擎版本，值包括：MONGO_2、MONGO_3_MMAP、MONGO_3_WT 、MONGO_3_ROCKS和MONGO_36_WT
        :type EngineVersion: str
        :param Machine: 實例類型，GIO：高IO版；TGIO：高IO萬兆
        :type Machine: str
        :param GoodsNum: 實例數量，預設值爲1, 最小值1，最大值爲10
        :type GoodsNum: int
        :param Zone: 可用區訊息，格式如：ap-guangzhou-2
        :type Zone: str
        :param InstanceRole: 實例角色，支援值包括：MASTER-表示主實例，DR-表示災備實例，RO-表示只讀實例
        :type InstanceRole: str
        :param InstanceType: 實例類型，REPLSET-副本集，SHARD-分片集群
        :type InstanceType: str
        :param Encrypt: 數據是否加密，當且僅當引擎版本爲MONGO_3_ROCKS，可以選擇加密
        :type Encrypt: int
        :param VpcId: 私有網絡ID，如果不傳則預設選擇基礎網絡
        :type VpcId: str
        :param SubnetId: 私有網絡下的子網ID，如果設置了 VpcId，則 SubnetId必填
        :type SubnetId: str
        :param ProjectId: 項目ID，不填爲預設項目
        :type ProjectId: int
        :param SecurityGroup: 安全組參數
        :type SecurityGroup: list of str
        """
        self.Memory = None
        self.Volume = None
        self.ReplicateSetNum = None
        self.SecondaryNum = None
        self.EngineVersion = None
        self.Machine = None
        self.GoodsNum = None
        self.Zone = None
        self.InstanceRole = None
        self.InstanceType = None
        self.Encrypt = None
        self.VpcId = None
        self.SubnetId = None
        self.ProjectId = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.SecondaryNum = params.get("SecondaryNum")
        self.EngineVersion = params.get("EngineVersion")
        self.Machine = params.get("Machine")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.InstanceRole = params.get("InstanceRole")
        self.InstanceType = params.get("InstanceType")
        self.Encrypt = params.get("Encrypt")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroup = params.get("SecurityGroup")


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceRequest(AbstractModel):
    """CreateDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param SecondaryNum: 每個副本集内從節點個數
        :type SecondaryNum: int
        :param Memory: 實例内存大小，單位：GB
        :type Memory: int
        :param Volume: 實例硬碟大小，單位：GB
        :type Volume: int
        :param MongoVersion: 版本号，當前僅支援 MONGO_3_WT
        :type MongoVersion: str
        :param MachineCode: 機器類型，GIO：高IO版；TGIO：高IO萬兆
        :type MachineCode: str
        :param GoodsNum: 實例數量，預設值爲1, 最小值1，最大值爲10
        :type GoodsNum: int
        :param Zone: 實例所屬區域名稱，格式如：ap-guangzhou-2
        :type Zone: str
        :param TimeSpan: 時長，購買月數
        :type TimeSpan: int
        :param Password: 實例密碼
        :type Password: str
        :param ProjectId: 項目ID，不填爲預設項目
        :type ProjectId: int
        :param SecurityGroup: 安全組參數
        :type SecurityGroup: list of str
        :param UniqVpcId: 私有網絡ID，如果不傳則預設選擇基礎網絡
        :type UniqVpcId: str
        :param UniqSubnetId: 私有網絡下的子網ID，如果設置了 VpcId，則 SubnetId必填
        :type UniqSubnetId: str
        """
        self.SecondaryNum = None
        self.Memory = None
        self.Volume = None
        self.MongoVersion = None
        self.MachineCode = None
        self.GoodsNum = None
        self.Zone = None
        self.TimeSpan = None
        self.Password = None
        self.ProjectId = None
        self.SecurityGroup = None
        self.UniqVpcId = None
        self.UniqSubnetId = None


    def _deserialize(self, params):
        self.SecondaryNum = params.get("SecondaryNum")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.MongoVersion = params.get("MongoVersion")
        self.MachineCode = params.get("MachineCode")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.TimeSpan = params.get("TimeSpan")
        self.Password = params.get("Password")
        self.ProjectId = params.get("ProjectId")
        self.SecurityGroup = params.get("SecurityGroup")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")


class CreateDBInstanceResponse(AbstractModel):
    """CreateDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class TerminateDBInstanceRequest(AbstractModel):
    """TerminateDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class TerminateDBInstanceResponse(AbstractModel):
    """TerminateDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param AsyncRequestId: 訂單ID，表示注銷實例成功
        :type AsyncRequestId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceHourRequest(AbstractModel):
    """UpgradeDBInstanceHour請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5
        :type InstanceId: str
        :param Memory: 升級後的内存大小，單位：GB
        :type Memory: int
        :param Volume: 升級後的硬碟大小，單位：GB
        :type Volume: int
        :param OplogSize: 升級後oplog的大小，單位：GB，預設爲磁盤空間的10%，允許設置的最小值爲磁盤的10%，最大值爲磁盤的90%
        :type OplogSize: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")


class UpgradeDBInstanceHourResponse(AbstractModel):
    """UpgradeDBInstanceHour返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID，格式如：cmgo-p8vnipr5。與雲資料庫控制台頁面中顯示的實例ID相同
        :type InstanceId: str
        :param Memory: 升級後的内存大小，單位：GB
        :type Memory: int
        :param Volume: 升級後的硬碟大小，單位：GB
        :type Volume: int
        :param OplogSize: 升級後oplog的大小，單位：GB，預設爲磁盤空間的10%，允許設置的最小值爲磁盤的10%，最大值爲磁盤的90%
        :type OplogSize: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回參數結構體

    """

    def __init__(self):
        """
        :param DealId: 訂單ID
        :type DealId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")