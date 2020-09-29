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


class ActionTimer(AbstractModel):
    """定時任務

    """

    def __init__(self):
        """
        :param Externals: 擴展數據
        :type Externals: :class:`taifucloudcloud.cvm.v20170312.models.Externals`
        :param TimerAction: 定時器名稱，目前僅支援銷毀一個值：TerminateInstances。
        :type TimerAction: str
        :param ActionTime: 執行時間，格式形如：2018-5-29 11:26:40,執行時間必須大於當前時間5分鍾。
        :type ActionTime: str
        """
        self.Externals = None
        self.TimerAction = None
        self.ActionTime = None


    def _deserialize(self, params):
        if params.get("Externals") is not None:
            self.Externals = Externals()
            self.Externals._deserialize(params.get("Externals"))
        self.TimerAction = params.get("TimerAction")
        self.ActionTime = params.get("ActionTime")


class AllocateHostsRequest(AbstractModel):
    """AllocateHosts請求參數結構體

    """

    def __init__(self):
        """
        :param Placement: 實例所在的位置。通過該參數可以指定實例所屬可用區，所屬項目等屬性。
        :type Placement: :class:`taifucloudcloud.cvm.v20170312.models.Placement`
        :param ClientToken: 用於保證請求幂等性的字串。
        :type ClientToken: str
        :param HostChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type HostChargePrepaid: :class:`taifucloudcloud.cvm.v20170312.models.ChargePrepaid`
        :param HostChargeType: 實例計費類型。目前僅支援：PREPAID（預付費，即包年包月模式）。
        :type HostChargeType: str
        :param HostType: CDH實例機型，預設爲：'HS1'。
        :type HostType: str
        :param HostCount: 購買CDH實例數量。
        :type HostCount: int
        :param TagSpecification: 標簽描述清單。通過指定該參數可以同時綁定標簽到相應的資源實例。
        :type TagSpecification: list of TagSpecification
        """
        self.Placement = None
        self.ClientToken = None
        self.HostChargePrepaid = None
        self.HostChargeType = None
        self.HostType = None
        self.HostCount = None
        self.TagSpecification = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ClientToken = params.get("ClientToken")
        if params.get("HostChargePrepaid") is not None:
            self.HostChargePrepaid = ChargePrepaid()
            self.HostChargePrepaid._deserialize(params.get("HostChargePrepaid"))
        self.HostChargeType = params.get("HostChargeType")
        self.HostType = params.get("HostType")
        self.HostCount = params.get("HostCount")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)


class AllocateHostsResponse(AbstractModel):
    """AllocateHosts返回參數結構體

    """

    def __init__(self):
        """
        :param HostIdSet: 新創建雲子機的實例id清單。
        :type HostIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HostIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HostIdSet = params.get("HostIdSet")
        self.RequestId = params.get("RequestId")


class AssociateInstancesKeyPairsRequest(AbstractModel):
    """AssociateInstancesKeyPairs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID，每次請求批次實例的上限爲100。<br>可以通過以下方式獲取可用的實例ID：<br><li>通過登入[控制台](https://console.cloud.taifucloud.com/cvm/index)查詢實例ID。<br><li>通過調用介面 [DescribeInstances](https://cloud.taifucloud.com/document/api/213/15728) ，取返回訊息中的`InstanceId`獲取實例ID。
        :type InstanceIds: list of str
        :param KeyIds: 一個或多個待操作的金鑰對ID，每次請求批次金鑰對的上限爲100。金鑰對ID形如：`skey-3glfot13`。<br>可以通過以下方式獲取可用的金鑰ID：<br><li>通過登入[控制台](https://console.cloud.taifucloud.com/cvm/sshkey)查詢金鑰ID。<br><li>通過調用介面 [DescribeKeyPairs](https://cloud.taifucloud.com/document/api/213/15699) ，取返回訊息中的`KeyId`獲取金鑰對ID。
        :type KeyIds: list of str
        :param ForceStop: 是否對運作中的實例選擇強制關機。建議對運作中的實例先手動關機，然後再綁定金鑰。取值範圍：<br><li>TRUE：表示在正常關機失敗後進行強制關機。<br><li>FALSE：表示在正常關機失敗後不進行強制關機。<br>預設取值：FALSE。
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.KeyIds = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.KeyIds = params.get("KeyIds")
        self.ForceStop = params.get("ForceStop")


class AssociateInstancesKeyPairsResponse(AbstractModel):
    """AssociateInstancesKeyPairs返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 要綁定的`安全組ID`，類似sg-efil73jd，只支援綁定單個安全組。
        :type SecurityGroupIds: list of str
        :param InstanceIds: 被綁定的`實例ID`，類似ins-lesecurk，支援指定多個實例。
        :type InstanceIds: list of str
        """
        self.SecurityGroupIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceIds = params.get("InstanceIds")


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ChargePrepaid(AbstractModel):
    """描述預付費模式，即包年包月相關參數。包括購買時長和自動續約邏輯等。

    """

    def __init__(self):
        """
        :param Period: 購買實例的時長，單位：月。取值範圍：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自動續約標識。取值範圍：<br><li>NOTIFY_AND_AUTO_RENEW：通知過期且自動續約<br><li>NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約<br><br>預設取值：NOTIFY_AND_AUTO_RENEW。若該參數指定爲NOTIFY_AND_AUTO_RENEW，在帳戶餘額充足的情況下，實例到期後将按月自動續約。
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class CreateDisasterRecoverGroupRequest(AbstractModel):
    """CreateDisasterRecoverGroup請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 分散置放群組名稱，長度1-60個字元，支援中、英文。
        :type Name: str
        :param Type: 分散置放群組類型，取值範圍：<br><li>HOST：物理機<br><li>SW：交換機<br><li>RACK：機架
        :type Type: str
        :param ClientToken: 用於保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。<br>更多詳細訊息請參閱：如何保證幂等性。
        :type ClientToken: str
        """
        self.Name = None
        self.Type = None
        self.ClientToken = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.ClientToken = params.get("ClientToken")


class CreateDisasterRecoverGroupResponse(AbstractModel):
    """CreateDisasterRecoverGroup返回參數結構體

    """

    def __init__(self):
        """
        :param DisasterRecoverGroupId: 分散置放群組ID清單。
        :type DisasterRecoverGroupId: str
        :param Type: 分散置放群組類型，取值範圍：<br><li>HOST：物理機<br><li>SW：交換機<br><li>RACK：機架
        :type Type: str
        :param Name: 分散置放群組名稱，長度1-60個字元，支援中、英文。
        :type Name: str
        :param CvmQuotaTotal: 置放群組内可容納的雲主機數量。
        :type CvmQuotaTotal: int
        :param CurrentNum: 置放群組内已有的雲主機數量。
        :type CurrentNum: int
        :param CreateTime: 置放群組創建時間。
        :type CreateTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DisasterRecoverGroupId = None
        self.Type = None
        self.Name = None
        self.CvmQuotaTotal = None
        self.CurrentNum = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        self.CvmQuotaTotal = params.get("CvmQuotaTotal")
        self.CurrentNum = params.get("CurrentNum")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    """CreateImage請求參數結構體

    """

    def __init__(self):
        """
        :param ImageName: 映像名稱
        :type ImageName: str
        :param InstanceId: 需要制作映像的實例ID
        :type InstanceId: str
        :param ImageDescription: 映像描述
        :type ImageDescription: str
        :param ForcePoweroff: 軟關機失敗時是否執行強制關機以制作映像
        :type ForcePoweroff: str
        :param Sysprep: 創建Windows映像時是否啓用Sysprep
        :type Sysprep: str
        :param Reboot: 實例處於運作中時，是否允許關機執行制作映像任務。
        :type Reboot: str
        :param DataDiskIds: 實例需要制作映像的數據盤Id
        :type DataDiskIds: list of str
        :param SnapshotIds: 需要制作映像的快照Id,必須包含一個系統盤快照
        :type SnapshotIds: list of str
        :param DryRun: 檢測請求的合法性，但不會對操作的資源産生任何影響
        :type DryRun: bool
        """
        self.ImageName = None
        self.InstanceId = None
        self.ImageDescription = None
        self.ForcePoweroff = None
        self.Sysprep = None
        self.Reboot = None
        self.DataDiskIds = None
        self.SnapshotIds = None
        self.DryRun = None


    def _deserialize(self, params):
        self.ImageName = params.get("ImageName")
        self.InstanceId = params.get("InstanceId")
        self.ImageDescription = params.get("ImageDescription")
        self.ForcePoweroff = params.get("ForcePoweroff")
        self.Sysprep = params.get("Sysprep")
        self.Reboot = params.get("Reboot")
        self.DataDiskIds = params.get("DataDiskIds")
        self.SnapshotIds = params.get("SnapshotIds")
        self.DryRun = params.get("DryRun")


class CreateImageResponse(AbstractModel):
    """CreateImage返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair請求參數結構體

    """

    def __init__(self):
        """
        :param KeyName: 金鑰對名稱，可由數字，字母和下劃線組成，長度不超過25個字元。
        :type KeyName: str
        :param ProjectId: 金鑰對創建後所屬的項目ID。
可以通過以下方式獲取項目ID：
<li>通過項目清單查詢項目ID。
<li>通過調用介面DescribeProject，取返回訊息中的`projectId `獲取項目ID。
        :type ProjectId: int
        """
        self.KeyName = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")


class CreateKeyPairResponse(AbstractModel):
    """CreateKeyPair返回參數結構體

    """

    def __init__(self):
        """
        :param KeyPair: 金鑰對訊息。
        :type KeyPair: :class:`taifucloudcloud.cvm.v20170312.models.KeyPair`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyPair = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyPair") is not None:
            self.KeyPair = KeyPair()
            self.KeyPair._deserialize(params.get("KeyPair"))
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了數據盤的訊息

    """

    def __init__(self):
        """
        :param DiskSize: 數據盤大小，單位：GB。最小調整步長爲10G，不同數據盤類型取值範圍不同，具體限制詳見：[CVM實例配置](/document/product/213/2177)。預設值爲0，表示不購買數據盤。更多限制詳見産品文件。
        :type DiskSize: int
        :param DiskType: 數據盤類型。數據盤類型限制詳見[CVM實例配置](/document/product/213/2177)。取值範圍：<br><li>LOCAL_BASIC：本地硬碟<br><li>LOCAL_SSD：本地SSD硬碟<br><li>CLOUD_BASIC：普通雲硬碟<br><li>CLOUD_PREMIUM：高效能雲硬碟<br><li>CLOUD_SSD：SSD雲硬碟<br><br>預設取值：LOCAL_BASIC。<br><br>該參數對`ResizeInstanceDisk`介面無效。
        :type DiskType: str
        :param DiskId: 數據盤ID。LOCAL_BASIC 和 LOCAL_SSD 類型沒有ID。暫時不支援該參數。
        :type DiskId: str
        :param DeleteWithInstance: 數據盤是否随子機銷毀。取值範圍：
<li>TRUE：子機銷毀時，銷毀數據盤，只支援按小時後付費雲盤
<li>FALSE：子機銷毀時，保留數據盤<br>
預設取值：TRUE<br>
該參數目前僅用於 `RunInstances` 介面。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param SnapshotId: 數據盤快照ID。選擇的數據盤快照大小需小於數據盤大小。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        """
        self.DiskSize = None
        self.DiskType = None
        self.DiskId = None
        self.DeleteWithInstance = None
        self.SnapshotId = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.SnapshotId = params.get("SnapshotId")


class DeleteDisasterRecoverGroupsRequest(AbstractModel):
    """DeleteDisasterRecoverGroups請求參數結構體

    """

    def __init__(self):
        """
        :param DisasterRecoverGroupIds: 分散置放群組ID清單，可通過[DescribeDisasterRecoverGroups](https://cloud.taifucloud.com/document/api/213/17810)介面獲取。
        :type DisasterRecoverGroupIds: list of str
        """
        self.DisasterRecoverGroupIds = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")


class DeleteDisasterRecoverGroupsResponse(AbstractModel):
    """DeleteDisasterRecoverGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImagesRequest(AbstractModel):
    """DeleteImages請求參數結構體

    """

    def __init__(self):
        """
        :param ImageIds: 準備删除的映像Id清單
        :type ImageIds: list of str
        """
        self.ImageIds = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")


class DeleteImagesResponse(AbstractModel):
    """DeleteImages返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteKeyPairsRequest(AbstractModel):
    """DeleteKeyPairs請求參數結構體

    """

    def __init__(self):
        """
        :param KeyIds: 一個或多個待操作的金鑰對ID。每次請求批次金鑰對的上限爲100。<br>可以通過以下方式獲取可用的金鑰ID：<br><li>通過登入[控制台](https://console.cloud.taifucloud.com/cvm/sshkey)查詢金鑰ID。<br><li>通過調用介面 [DescribeKeyPairs](https://cloud.taifucloud.com/document/api/213/15699) ，取返回訊息中的 `KeyId` 獲取金鑰對ID。
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class DeleteKeyPairsResponse(AbstractModel):
    """DeleteKeyPairs返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDisasterRecoverGroupQuotaRequest(AbstractModel):
    """DescribeDisasterRecoverGroupQuota請求參數結構體

    """


class DescribeDisasterRecoverGroupQuotaResponse(AbstractModel):
    """DescribeDisasterRecoverGroupQuota返回參數結構體

    """

    def __init__(self):
        """
        :param GroupQuota: 可創建置放群組數量的上限。
        :type GroupQuota: int
        :param CurrentNum: 當前用戶已經創建的置放群組數量。
        :type CurrentNum: int
        :param CvmInHostGroupQuota: 物理機類型容災組内實例的配額數。
        :type CvmInHostGroupQuota: int
        :param CvmInSwGroupQuota: 交換機類型容災組内實例的配額數。
        :type CvmInSwGroupQuota: int
        :param CvmInRackGroupQuota: 機架類型容災組内實例的配額數。
        :type CvmInRackGroupQuota: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupQuota = None
        self.CurrentNum = None
        self.CvmInHostGroupQuota = None
        self.CvmInSwGroupQuota = None
        self.CvmInRackGroupQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupQuota = params.get("GroupQuota")
        self.CurrentNum = params.get("CurrentNum")
        self.CvmInHostGroupQuota = params.get("CvmInHostGroupQuota")
        self.CvmInSwGroupQuota = params.get("CvmInSwGroupQuota")
        self.CvmInRackGroupQuota = params.get("CvmInRackGroupQuota")
        self.RequestId = params.get("RequestId")


class DescribeDisasterRecoverGroupsRequest(AbstractModel):
    """DescribeDisasterRecoverGroups請求參數結構體

    """

    def __init__(self):
        """
        :param DisasterRecoverGroupIds: 分散置放群組ID清單。
        :type DisasterRecoverGroupIds: list of str
        :param Name: 分散置放群組名稱，支援模糊比對。
        :type Name: str
        :param Offset: 偏移量，預設爲0。關於`Offset`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關於`Limit`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        """
        self.DisasterRecoverGroupIds = None
        self.Name = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        self.Name = params.get("Name")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDisasterRecoverGroupsResponse(AbstractModel):
    """DescribeDisasterRecoverGroups返回參數結構體

    """

    def __init__(self):
        """
        :param DisasterRecoverGroupSet: 分散置放群組訊息清單。
        :type DisasterRecoverGroupSet: list of DisasterRecoverGroup
        :param TotalCount: 用戶置放群組總量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DisasterRecoverGroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DisasterRecoverGroupSet") is not None:
            self.DisasterRecoverGroupSet = []
            for item in params.get("DisasterRecoverGroupSet"):
                obj = DisasterRecoverGroup()
                obj._deserialize(item)
                self.DisasterRecoverGroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHostsRequest(AbstractModel):
    """DescribeHosts請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
<li> zone - String - 是否必填：否 - （過濾條件）按照可用區過濾。</li>
<li> project-id - Integer - 是否必填：否 - （過濾條件）按照項目ID過濾。可通過調用 DescribeProject 查詢已創建的項目清單或登入控制台進行檢視；也可以調用 AddProject 創建新的項目。</li>
<li> host-id - String - 是否必填：否 - （過濾條件）按照CDH ID過濾。CDH ID形如：host-11112222。</li>
<li> host-name - String - 是否必填：否 - （過濾條件）按照CDH實例名稱過濾。</li>
<li> host-state - String - 是否必填：否 - （過濾條件）按照CDH實例狀态進行過濾。（PENDING：創建中|LAUNCH_FAILURE：創建失敗|RUNNING：運作中|EXPIRED：已過期）</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeHostsResponse(AbstractModel):
    """DescribeHosts返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合查詢條件的cdh實例總數
        :type TotalCount: int
        :param HostSet: cdh實例詳細訊息清單
        :type HostSet: list of HostItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.HostSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HostSet") is not None:
            self.HostSet = []
            for item in params.get("HostSet"):
                obj = HostItem()
                obj._deserialize(item)
                self.HostSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageQuotaRequest(AbstractModel):
    """DescribeImageQuota請求參數結構體

    """


class DescribeImageQuotaResponse(AbstractModel):
    """DescribeImageQuota返回參數結構體

    """

    def __init__(self):
        """
        :param ImageNumQuota: 帳戶的映像配額
        :type ImageNumQuota: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageNumQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageNumQuota = params.get("ImageNumQuota")
        self.RequestId = params.get("RequestId")


class DescribeImageSharePermissionRequest(AbstractModel):
    """DescribeImageSharePermission請求參數結構體

    """

    def __init__(self):
        """
        :param ImageId: 需要共享的映像Id
        :type ImageId: str
        """
        self.ImageId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")


class DescribeImageSharePermissionResponse(AbstractModel):
    """DescribeImageSharePermission返回參數結構體

    """

    def __init__(self):
        """
        :param SharePermissionSet: 映像共享訊息
        :type SharePermissionSet: list of SharePermission
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SharePermissionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SharePermissionSet") is not None:
            self.SharePermissionSet = []
            for item in params.get("SharePermissionSet"):
                obj = SharePermission()
                obj._deserialize(item)
                self.SharePermissionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages請求參數結構體

    """

    def __init__(self):
        """
        :param ImageIds: 映像ID清單 。映像ID如：`img-gvbnzy6f`。array型參數的格式可以參考[API簡介](https://cloud.taifucloud.com/document/api/213/15688)。映像ID可以通過如下方式獲取：<br><li>通過[DescribeImages](https://cloud.taifucloud.com/document/api/213/15715)介面返回的`ImageId`獲取。<br><li>通過[映像控制台](https://console.cloud.taifucloud.com/cvm/image)獲取。
        :type ImageIds: list of str
        :param Filters: 過濾條件，每次請求的`Filters`的上限爲0，`Filters.Values`的上限爲5。參數不可以同時指定`ImageIds`和`Filters`。詳細的過濾條件如下：
<li> image-id - String - 是否必填： 否 - （過濾條件）按照映像ID進行過濾</li>
<li> image-type - String - 是否必填： 否 - （過濾條件）按照映像類型進行過濾。取值範圍：詳見[映像類型](https://cloud.taifucloud.com/document/product/213/9452#image_type)。</li>
<li> image-state - String - 是否必填： 否 - （過濾條件）按照映像狀态進行過濾。取值範圍：詳見[映像狀态](https://cloud.taifucloud.com/document/product/213/9452#image_state)。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關於Offset詳見[API簡介](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)。
        :type Offset: int
        :param Limit: 數量限制，預設爲20，最大值爲100。關於Limit詳見[API簡介](/document/api/213/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89)。
        :type Limit: int
        :param InstanceType: 實例類型，如 `S1.SMALL1`
        :type InstanceType: str
        """
        self.ImageIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceType = params.get("InstanceType")


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回參數結構體

    """

    def __init__(self):
        """
        :param ImageSet: 一個關於映像詳細訊息的結構體，主要包括映像的主要狀态與屬性。
        :type ImageSet: list of Image
        :param TotalCount: 符合要求的映像數量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImageSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageSet") is not None:
            self.ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self.ImageSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImportImageOsRequest(AbstractModel):
    """DescribeImportImageOs請求參數結構體

    """


class DescribeImportImageOsResponse(AbstractModel):
    """DescribeImportImageOs返回參數結構體

    """

    def __init__(self):
        """
        :param ImportImageOsListSupported: 支援的導入映像的作業系統類型。
        :type ImportImageOsListSupported: :class:`taifucloudcloud.cvm.v20170312.models.ImageOsList`
        :param ImportImageOsVersionSet: 支援的導入映像的作業系統版本。
        :type ImportImageOsVersionSet: list of OsVersion
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ImportImageOsListSupported = None
        self.ImportImageOsVersionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImportImageOsListSupported") is not None:
            self.ImportImageOsListSupported = ImageOsList()
            self.ImportImageOsListSupported._deserialize(params.get("ImportImageOsListSupported"))
        if params.get("ImportImageOsVersionSet") is not None:
            self.ImportImageOsVersionSet = []
            for item in params.get("ImportImageOsVersionSet"):
                obj = OsVersion()
                obj._deserialize(item)
                self.ImportImageOsVersionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceFamilyConfigsRequest(AbstractModel):
    """DescribeInstanceFamilyConfigs請求參數結構體

    """


class DescribeInstanceFamilyConfigsResponse(AbstractModel):
    """DescribeInstanceFamilyConfigs返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceFamilyConfigSet: 實例機型組配置的清單訊息
        :type InstanceFamilyConfigSet: list of InstanceFamilyConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceFamilyConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfigSet") is not None:
            self.InstanceFamilyConfigSet = []
            for item in params.get("InstanceFamilyConfigSet"):
                obj = InstanceFamilyConfig()
                obj._deserialize(item)
                self.InstanceFamilyConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceInternetBandwidthConfigsRequest(AbstractModel):
    """DescribeInstanceInternetBandwidthConfigs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeInstanceInternetBandwidthConfigsResponse(AbstractModel):
    """DescribeInstanceInternetBandwidthConfigs返回參數結構體

    """

    def __init__(self):
        """
        :param InternetBandwidthConfigSet: 頻寬配置訊息清單。
        :type InternetBandwidthConfigSet: list of InternetBandwidthConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InternetBandwidthConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InternetBandwidthConfigSet") is not None:
            self.InternetBandwidthConfigSet = []
            for item in params.get("InternetBandwidthConfigSet"):
                obj = InternetBandwidthConfig()
                obj._deserialize(item)
                self.InternetBandwidthConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTypeConfigsRequest(AbstractModel):
    """DescribeInstanceTypeConfigs請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。
<li> zone - String - 是否必填：否 -（過濾條件）按照[可用區](https://cloud.taifucloud.com/document/api/213/9452#zone)過濾。</li>
<li> instance-family - String - 是否必填：否 -（過濾條件）按照實例機型系列過濾。實例機型系列形如：S1、I1、M1等。</li>
每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲1。
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeInstanceTypeConfigsResponse(AbstractModel):
    """DescribeInstanceTypeConfigs返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceTypeConfigSet: 實例機型配置清單。
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeConfigSet") is not None:
            self.InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self.InstanceTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceVncUrlRequest(AbstractModel):
    """DescribeInstanceVncUrl請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 一個操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728) API返回值中的`InstanceId`獲取。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeInstanceVncUrlResponse(AbstractModel):
    """DescribeInstanceVncUrl返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceVncUrl: 實例的管理終端網址。
        :type InstanceVncUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceVncUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceVncUrl = params.get("InstanceVncUrl")
        self.RequestId = params.get("RequestId")


class DescribeInstancesOperationLimitRequest(AbstractModel):
    """DescribeInstancesOperationLimit請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 按照一個或者多個實例ID查詢，可通過[DescribeInstances](https://cloud.taifucloud.com/document/api/213/9388)API返回值中的InstanceId獲取。實例ID形如：ins-xxxxxxxx。（此參數的具體格式可參考API[簡介](https://cloud.taifucloud.com/document/api/213/15688)的id.N一節）。每次請求的實例的上限爲100。
        :type InstanceIds: list of str
        :param Operation: 實例操作。
<li> INSTANCE_DEGRADE：實例降配操作</li>
        :type Operation: str
        """
        self.InstanceIds = None
        self.Operation = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Operation = params.get("Operation")


class DescribeInstancesOperationLimitResponse(AbstractModel):
    """DescribeInstancesOperationLimit返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceOperationLimitSet: 該參數表示調整配置操作（降配）限制次數查詢。
        :type InstanceOperationLimitSet: list of OperationCountLimit
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceOperationLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceOperationLimitSet") is not None:
            self.InstanceOperationLimitSet = []
            for item in params.get("InstanceOperationLimitSet"):
                obj = OperationCountLimit()
                obj._deserialize(item)
                self.InstanceOperationLimitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 按照一個或者多個實例ID查詢。實例ID形如：`ins-xxxxxxxx`。（此參數的具體格式可參考API[簡介](https://cloud.taifucloud.com/document/api/213/15688)的`id.N`一節）。每次請求的實例的上限爲100。參數不支援同時指定`InstanceIds`和`Filters`。
        :type InstanceIds: list of str
        :param Filters: 過濾條件。
<li> zone - String - 是否必填：否 -（過濾條件）按照可用區過濾。</li>
<li> project-id - Integer - 是否必填：否 -（過濾條件）按照項目ID過濾。可通過調用[DescribeProject](https://cloud.taifucloud.com/document/api/378/4400)查詢已創建的項目清單或登入[控制台](https://console.cloud.taifucloud.com/cvm/index)進行檢視；也可以調用[AddProject](https://cloud.taifucloud.com/document/api/378/4398)創建新的項目。</li>
<li> host-id - String - 是否必填：否 - （過濾條件）按照[CDH](https://cloud.taifucloud.com/document/product/416) ID過濾。[CDH](https://cloud.taifucloud.com/document/product/416) ID形如：host-xxxxxxxx。</li>
<li> vpc-id - String - 是否必填：否 - （過濾條件）按照VPC ID進行過濾。VPC ID形如：vpc-xxxxxxxx。</li>
<li> subnet-id - String - 是否必填：否 - （過濾條件）按照子網ID進行過濾。子網ID形如：subnet-xxxxxxxx。</li>
<li> instance-id - String - 是否必填：否 - （過濾條件）按照實例ID過濾。實例ID形如：ins-xxxxxxxx。</li>
<li> security-group-id - String - 是否必填：否 - （過濾條件）按照安全組ID過濾，安全組ID形如: sg-8jlk3f3r。</li>
<li> instance-name - String - 是否必填：否 - （過濾條件）按照實例名稱過濾。</li>
<li> instance-charge-type - String - 是否必填：否 -（過濾條件）按照實例計費模式過濾。 (PREPAID：表示預付費，即包年包月 | POSTPAID_BY_HOUR：表示後付費，即按量計費 | CDHPAID：表示[CDH](https://cloud.taifucloud.com/document/product/416)付費，即只對[CDH](https://cloud.taifucloud.com/document/product/416)計費，不對[CDH](https://cloud.taifucloud.com/document/product/416)上的實例計費。 )  </li>
<li> private-ip-address - String - 是否必填：否 - （過濾條件）按照實例主網卡的内網IP過濾。</li>
<li> public-ip-address - String - 是否必填：否 - （過濾條件）按照實例主網卡的公網IP過濾，包含實例創建時自動分配的IP和實例創建後手動綁定的彈性IP。</li>
<li> tag-key - String - 是否必填：否 - （過濾條件）按照標簽鍵進行過濾。</li>
<li> tag-value - String - 是否必填：否 - （過濾條件）按照標簽值進行過濾。</li>
<li> tag:tag-key - String - 是否必填：否 - （過濾條件）按照標簽鍵值對進行過濾。 tag-key使用具體的標簽鍵進行替換。使用請參考範例2。</li>
每次請求的`Filters`的上限爲10，`Filter.Values`的上限爲5。參數不支援同時指定`InstanceIds`和`Filters`。
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關於`Offset`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關於`Limit`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        """
        self.InstanceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例數量。
        :type TotalCount: int
        :param InstanceSet: 實例詳細訊息清單。
        :type InstanceSet: list of Instance
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesStatusRequest(AbstractModel):
    """DescribeInstancesStatus請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 按照一個或者多個實例ID查詢。實例ID形如：`ins-11112222`。此參數的具體格式可參考API[簡介](https://cloud.taifucloud.com/document/api/213/15688)的`id.N`一節）。每次請求的實例的上限爲100。
        :type InstanceIds: list of str
        :param Offset: 偏移量，預設爲0。關於`Offset`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關於`Limit`的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        """
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeInstancesStatusResponse(AbstractModel):
    """DescribeInstancesStatus返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的實例狀态數量。
        :type TotalCount: int
        :param InstanceStatusSet: [實例狀态](https://cloud.taifucloud.com/document/api/213/15738) 清單。
        :type InstanceStatusSet: list of InstanceStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceStatusSet") is not None:
            self.InstanceStatusSet = []
            for item in params.get("InstanceStatusSet"):
                obj = InstanceStatus()
                obj._deserialize(item)
                self.InstanceStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInternetChargeTypeConfigsRequest(AbstractModel):
    """DescribeInternetChargeTypeConfigs請求參數結構體

    """


class DescribeInternetChargeTypeConfigsResponse(AbstractModel):
    """DescribeInternetChargeTypeConfigs返回參數結構體

    """

    def __init__(self):
        """
        :param InternetChargeTypeConfigSet: 網絡計費類型配置。
        :type InternetChargeTypeConfigSet: list of InternetChargeTypeConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InternetChargeTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InternetChargeTypeConfigSet") is not None:
            self.InternetChargeTypeConfigSet = []
            for item in params.get("InternetChargeTypeConfigSet"):
                obj = InternetChargeTypeConfig()
                obj._deserialize(item)
                self.InternetChargeTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKeyPairsRequest(AbstractModel):
    """DescribeKeyPairs請求參數結構體

    """

    def __init__(self):
        """
        :param KeyIds: 金鑰對ID，金鑰對ID形如：`skey-11112222`（此介面支援同時傳入多個ID進行過濾。此參數的具體格式可參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)的 `id.N` 一節）。參數不支援同時指定 `KeyIds` 和 `Filters`。金鑰對ID可以通過登入[控制台](https://console.cloud.taifucloud.com/cvm/index)查詢。
        :type KeyIds: list of str
        :param Filters: 過濾條件。
<li> project-id - Integer - 是否必填：否 -（過濾條件）按照項目ID過濾。可以通過[項目清單](https://console.cloud.taifucloud.com/project)查詢項目ID，或者調用介面 [DescribeProject](https://cloud.taifucloud.com/document/api/378/4400)，取返回訊息中的projectId獲取項目ID。</li>
<li> key-name - String - 是否必填：否 -（過濾條件）按照金鑰對名稱過濾。</li>參數不支援同時指定 `KeyIds` 和 `Filters`。
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關於 `Offset` 的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。返回數量，預設爲20，最大值爲100。關於 `Limit` 的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關於 `Limit` 的更進一步介紹請參考 API [簡介](https://cloud.taifucloud.com/document/api/213/15688)中的相關小節。
        :type Limit: int
        """
        self.KeyIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeKeyPairsResponse(AbstractModel):
    """DescribeKeyPairs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的金鑰對數量。
        :type TotalCount: int
        :param KeyPairSet: 金鑰對詳細訊息清單。
        :type KeyPairSet: list of KeyPair
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.KeyPairSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KeyPairSet") is not None:
            self.KeyPairSet = []
            for item in params.get("KeyPairSet"):
                obj = KeyPair()
                obj._deserialize(item)
                self.KeyPairSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions請求參數結構體

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 地域數量
        :type TotalCount: int
        :param RegionSet: 地域清單訊息
        :type RegionSet: list of RegionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeZoneInstanceConfigInfos請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。

<li> zone - String - 是否必填：否 -（過濾條件）按照可用區過濾。</li>

<li> instance-family String - 是否必填：否 -（過濾條件）按照機型系列過濾。按照實例機型系列過濾。實例機型系列形如：S1、I1、M1等。</li>

<li> instance-type - String - 是否必填：否 - （過濾條件）按照機型過濾。按照實例機型過濾。不同實例機型指定了不同的資源規格，具體取值可通過調用介面 DescribeInstanceTypeConfigs 來獲得最新的規格表或參見實例類型描述。若不指定該參數，則預設機型爲S1.SMALL1。</li>

<li> instance-charge-type - String - 是否必填：否 -（過濾條件）按照實例計費模式過濾。 (PREPAID：表示預付費，即包年包月 | POSTPAID_BY_HOUR：表示後付費，即按量計費 | CDHPAID：表示CDH付費，即只對CDH計費，不對CDH上的實例計費。 )  </li>
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeZoneInstanceConfigInfos返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceTypeQuotaSet: 可用區機型配置清單。
        :type InstanceTypeQuotaSet: list of InstanceTypeQuotaItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceTypeQuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeQuotaSet") is not None:
            self.InstanceTypeQuotaSet = []
            for item in params.get("InstanceTypeQuotaSet"):
                obj = InstanceTypeQuotaItem()
                obj._deserialize(item)
                self.InstanceTypeQuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones請求參數結構體

    """


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 可用區數量。
        :type TotalCount: int
        :param ZoneSet: 可用區清單訊息。
        :type ZoneSet: list of ZoneInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ZoneSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID，每次請求批次實例的上限爲100。<br><br>可以通過以下方式獲取可用的實例ID：<br><li>通過登入[控制台](https://console.cloud.taifucloud.com/cvm/index)查詢實例ID。<br><li>通過調用介面 [DescribeInstances](https://cloud.taifucloud.com/document/api/213/15728) ，取返回訊息中的 `InstanceId` 獲取實例ID。
        :type InstanceIds: list of str
        :param KeyIds: 金鑰對ID清單，每次請求批次金鑰對的上限爲100。金鑰對ID形如：`skey-11112222`。<br><br>可以通過以下方式獲取可用的金鑰ID：<br><li>通過登入[控制台](https://console.cloud.taifucloud.com/cvm/sshkey)查詢金鑰ID。<br><li>通過調用介面 [DescribeKeyPairs](https://cloud.taifucloud.com/document/api/213/15699) ，取返回訊息中的 `KeyId` 獲取金鑰對ID。
        :type KeyIds: list of str
        :param ForceStop: 是否對運作中的實例選擇強制關機。建議對運作中的實例先手動關機，然後再解綁金鑰。取值範圍：<br><li>TRUE：表示在正常關機失敗後進行強制關機。<br><li>FALSE：表示在正常關機失敗後不進行強制關機。<br><br>預設取值：FALSE。
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.KeyIds = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.KeyIds = params.get("KeyIds")
        self.ForceStop = params.get("ForceStop")


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    """DisassociateInstancesKeyPairs返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups請求參數結構體

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 要解綁的`安全組ID`，類似sg-efil73jd，只支援解綁單個安全組。
        :type SecurityGroupIds: list of str
        :param InstanceIds: 被解綁的`實例ID`，類似ins-lesecurk，支援指定多個實例 。
        :type InstanceIds: list of str
        """
        self.SecurityGroupIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceIds = params.get("InstanceIds")


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisasterRecoverGroup(AbstractModel):
    """容災組訊息

    """

    def __init__(self):
        """
        :param DisasterRecoverGroupId: 分散置放群組id。
        :type DisasterRecoverGroupId: str
        :param Name: 分散置放群組名稱，長度1-60個字元。
        :type Name: str
        :param Type: 分散置放群組類型，取值範圍：<br><li>HOST：物理機<br><li>SW：交換機<br><li>RACK：機架
        :type Type: str
        :param CvmQuotaTotal: 分散置放群組内最大容納雲主機數量。
        :type CvmQuotaTotal: int
        :param CurrentNum: 分散置放群組内雲主機當前數量。
        :type CurrentNum: int
        :param InstanceIds: 分散置放群組内，雲主機id清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceIds: list of str
        :param CreateTime: 分散置放群組創建時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.DisasterRecoverGroupId = None
        self.Name = None
        self.Type = None
        self.CvmQuotaTotal = None
        self.CurrentNum = None
        self.InstanceIds = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.CvmQuotaTotal = params.get("CvmQuotaTotal")
        self.CurrentNum = params.get("CurrentNum")
        self.InstanceIds = params.get("InstanceIds")
        self.CreateTime = params.get("CreateTime")


class EnhancedService(AbstractModel):
    """描述了實例的增強服務啓用情況與其設置，如雲安全，雲監控等實例 Agent

    """

    def __init__(self):
        """
        :param SecurityService: 開啓雲安全服務。若不指定該參數，則預設開啓雲安全服務。
        :type SecurityService: :class:`taifucloudcloud.cvm.v20170312.models.RunSecurityServiceEnabled`
        :param MonitorService: 開啓雲監控服務。若不指定該參數，則預設開啓雲監控服務。
        :type MonitorService: :class:`taifucloudcloud.cvm.v20170312.models.RunMonitorServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))


class Externals(AbstractModel):
    """擴展數據

    """

    def __init__(self):
        """
        :param ReleaseAddress: 釋放網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReleaseAddress: bool
        :param UnsupportNetworks: 不支援的網絡類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnsupportNetworks: list of str
        :param StorageBlockAttr: HDD本地儲存屬性
注意：此欄位可能返回 null，表示取不到有效值。
        :type StorageBlockAttr: :class:`taifucloudcloud.cvm.v20170312.models.StorageBlock`
        """
        self.ReleaseAddress = None
        self.UnsupportNetworks = None
        self.StorageBlockAttr = None


    def _deserialize(self, params):
        self.ReleaseAddress = params.get("ReleaseAddress")
        self.UnsupportNetworks = params.get("UnsupportNetworks")
        if params.get("StorageBlockAttr") is not None:
            self.StorageBlockAttr = StorageBlock()
            self.StorageBlockAttr._deserialize(params.get("StorageBlockAttr"))


class Filter(AbstractModel):
    """>描述鍵值對過濾器，用於條件過濾查詢。例如過濾ID、名稱、狀态等
    > * 若存在多個`Filter`時，`Filter`間的關系爲邏輯與（`AND`）關系。
    > * 若同一個`Filter`存在多個`Values`，同一`Filter`下`Values`間的關系爲邏輯或（`OR`）關系。
    >
    > 以[DescribeInstances](https://cloud.taifucloud.com/document/api/213/15728)介面的`Filter`爲例。若我們需要查詢可用區（`zone`）爲 一區 ***並且*** 實例計費模式（`instance-charge-type`）爲包年包月 ***或者*** 按量計費的實例時，可如下實現：
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=PREPAID
    &Filters.1.Values.1=POSTPAID_BY_HOUR
    ```

    """

    def __init__(self):
        """
        :param Name: 需要過濾的欄位。
        :type Name: str
        :param Values: 欄位的過濾值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class HostItem(AbstractModel):
    """cdh實例詳細訊息

    """

    def __init__(self):
        """
        :param Placement: cdh實例所在的位置。通過該參數可以指定實例所屬可用區，所屬項目等屬性。
        :type Placement: :class:`taifucloudcloud.cvm.v20170312.models.Placement`
        :param HostId: cdh實例id
        :type HostId: str
        :param HostType: cdh實例類型
        :type HostType: str
        :param HostName: cdh實例名稱
        :type HostName: str
        :param HostChargeType: cdh實例付費模式
        :type HostChargeType: str
        :param RenewFlag: cdh實例自動續約標記
        :type RenewFlag: str
        :param CreatedTime: cdh實例創建時間
        :type CreatedTime: str
        :param ExpiredTime: cdh實例過期時間
        :type ExpiredTime: str
        :param InstanceIds: cdh實例上已創建雲子機的實例id清單
        :type InstanceIds: list of str
        :param HostState: cdh實例狀态
        :type HostState: str
        :param HostIp: cdh實例ip
        :type HostIp: str
        :param HostResource: cdh實例資源訊息
        :type HostResource: :class:`taifucloudcloud.cvm.v20170312.models.HostResource`
        :param CageId: 專用宿主機所屬的圍籠ID。該欄位僅對金融專區圍籠内的專用宿主機有效。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CageId: str
        """
        self.Placement = None
        self.HostId = None
        self.HostType = None
        self.HostName = None
        self.HostChargeType = None
        self.RenewFlag = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.InstanceIds = None
        self.HostState = None
        self.HostIp = None
        self.HostResource = None
        self.CageId = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.HostId = params.get("HostId")
        self.HostType = params.get("HostType")
        self.HostName = params.get("HostName")
        self.HostChargeType = params.get("HostChargeType")
        self.RenewFlag = params.get("RenewFlag")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.InstanceIds = params.get("InstanceIds")
        self.HostState = params.get("HostState")
        self.HostIp = params.get("HostIp")
        if params.get("HostResource") is not None:
            self.HostResource = HostResource()
            self.HostResource._deserialize(params.get("HostResource"))
        self.CageId = params.get("CageId")


class HostResource(AbstractModel):
    """cdh實例的資源訊息

    """

    def __init__(self):
        """
        :param CpuTotal: cdh實例總cpu核數
        :type CpuTotal: int
        :param CpuAvailable: cdh實例可用cpu核數
        :type CpuAvailable: int
        :param MemTotal: cdh實例總内存大小（單位爲:GiB）
        :type MemTotal: float
        :param MemAvailable: cdh實例可用内存大小（單位爲:GiB）
        :type MemAvailable: float
        :param DiskTotal: cdh實例總磁盤大小（單位爲:GiB）
        :type DiskTotal: int
        :param DiskAvailable: cdh實例可用磁盤大小（單位爲:GiB）
        :type DiskAvailable: int
        """
        self.CpuTotal = None
        self.CpuAvailable = None
        self.MemTotal = None
        self.MemAvailable = None
        self.DiskTotal = None
        self.DiskAvailable = None


    def _deserialize(self, params):
        self.CpuTotal = params.get("CpuTotal")
        self.CpuAvailable = params.get("CpuAvailable")
        self.MemTotal = params.get("MemTotal")
        self.MemAvailable = params.get("MemAvailable")
        self.DiskTotal = params.get("DiskTotal")
        self.DiskAvailable = params.get("DiskAvailable")


class Image(AbstractModel):
    """一個關於映像詳細訊息的結構體，主要包括映像的主要狀态與屬性。

    """

    def __init__(self):
        """
        :param ImageId: 映像ID
        :type ImageId: str
        :param OsName: 映像作業系統
        :type OsName: str
        :param ImageType: 映像類型
        :type ImageType: str
        :param CreatedTime: 映像創建時間
        :type CreatedTime: str
        :param ImageName: 映像名稱
        :type ImageName: str
        :param ImageDescription: 映像描述
        :type ImageDescription: str
        :param ImageSize: 映像大小
        :type ImageSize: int
        :param Architecture: 映像架構
        :type Architecture: str
        :param ImageState: 映像狀态
        :type ImageState: str
        :param Platform: 映像來源平台
        :type Platform: str
        :param ImageCreator: 映像創建者
        :type ImageCreator: str
        :param ImageSource: 映像來源
        :type ImageSource: str
        :param SyncPercent: 同步百分比
注意：此欄位可能返回 null，表示取不到有效值。
        :type SyncPercent: int
        :param IsSupportCloudinit: 映像是否支援cloud-init
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsSupportCloudinit: bool
        :param SnapshotSet: 映像關聯的快照訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type SnapshotSet: list of Snapshot
        """
        self.ImageId = None
        self.OsName = None
        self.ImageType = None
        self.CreatedTime = None
        self.ImageName = None
        self.ImageDescription = None
        self.ImageSize = None
        self.Architecture = None
        self.ImageState = None
        self.Platform = None
        self.ImageCreator = None
        self.ImageSource = None
        self.SyncPercent = None
        self.IsSupportCloudinit = None
        self.SnapshotSet = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.OsName = params.get("OsName")
        self.ImageType = params.get("ImageType")
        self.CreatedTime = params.get("CreatedTime")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        self.ImageSize = params.get("ImageSize")
        self.Architecture = params.get("Architecture")
        self.ImageState = params.get("ImageState")
        self.Platform = params.get("Platform")
        self.ImageCreator = params.get("ImageCreator")
        self.ImageSource = params.get("ImageSource")
        self.SyncPercent = params.get("SyncPercent")
        self.IsSupportCloudinit = params.get("IsSupportCloudinit")
        if params.get("SnapshotSet") is not None:
            self.SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self.SnapshotSet.append(obj)


class ImageOsList(AbstractModel):
    """支援的作業系統類型，根據windows和linux分類。

    """

    def __init__(self):
        """
        :param Windows: 支援的windows作業系統。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Windows: list of str
        :param Linux: 支援的linux作業系統
注意：此欄位可能返回 null，表示取不到有效值。
        :type Linux: list of str
        """
        self.Windows = None
        self.Linux = None


    def _deserialize(self, params):
        self.Windows = params.get("Windows")
        self.Linux = params.get("Linux")


class ImportImageRequest(AbstractModel):
    """ImportImage請求參數結構體

    """

    def __init__(self):
        """
        :param Architecture: 導入映像的作業系統架構，`x86_64` 或 `i386`
        :type Architecture: str
        :param OsType: 導入映像的作業系統類型，通過`DescribeImportImageOs`獲取
        :type OsType: str
        :param OsVersion: 導入映像的作業系統版本，通過`DescribeImportImageOs`獲取
        :type OsVersion: str
        :param ImageUrl: 導入映像存放的cos網址
        :type ImageUrl: str
        :param ImageName: 映像名稱
        :type ImageName: str
        :param ImageDescription: 映像描述
        :type ImageDescription: str
        :param DryRun: 只檢查參數，不執行任務
        :type DryRun: bool
        :param Force: 是否強制導入，參考[強制導入映像](https://cloud.taifucloud.com/document/product/213/12849)
        :type Force: bool
        """
        self.Architecture = None
        self.OsType = None
        self.OsVersion = None
        self.ImageUrl = None
        self.ImageName = None
        self.ImageDescription = None
        self.DryRun = None
        self.Force = None


    def _deserialize(self, params):
        self.Architecture = params.get("Architecture")
        self.OsType = params.get("OsType")
        self.OsVersion = params.get("OsVersion")
        self.ImageUrl = params.get("ImageUrl")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        self.DryRun = params.get("DryRun")
        self.Force = params.get("Force")


class ImportImageResponse(AbstractModel):
    """ImportImage返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImportKeyPairRequest(AbstractModel):
    """ImportKeyPair請求參數結構體

    """

    def __init__(self):
        """
        :param KeyName: 金鑰對名稱，可由數字，字母和下劃線組成，長度不超過25個字元。
        :type KeyName: str
        :param ProjectId: 金鑰對創建後所屬的[項目](/document/product/378/10863)ID。<br><br>可以通過以下方式獲取項目ID：<br><li>通過[項目清單](https://console.cloud.taifucloud.com/project)查詢項目ID。<br><li>通過調用介面 [DescribeProject](https://cloud.taifucloud.com/document/api/378/4400)，取返回訊息中的 `projectId ` 獲取項目ID。

如果是預設項目，直接填0就可以。
        :type ProjectId: int
        :param PublicKey: 金鑰對的公鑰内容，`OpenSSH RSA` 格式。
        :type PublicKey: str
        """
        self.KeyName = None
        self.ProjectId = None
        self.PublicKey = None


    def _deserialize(self, params):
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        self.PublicKey = params.get("PublicKey")


class ImportKeyPairResponse(AbstractModel):
    """ImportKeyPair返回參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 金鑰對ID。
        :type KeyId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class InquiryPriceModifyInstancesChargeTypeRequest(AbstractModel):
    """InquiryPriceModifyInstancesChargeType請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲100。
        :type InstanceIds: list of str
        :param InstanceChargeType: 實例[計費類型](https://cloud.taifucloud.com/document/product/213/2180)。<br><li>PREPAID：預付費，即包年包月。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的續約時長、是否設置自動續約等屬性。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.cvm.v20170312.models.InstanceChargePrepaid`
        """
        self.InstanceIds = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class InquiryPriceModifyInstancesChargeTypeResponse(AbstractModel):
    """InquiryPriceModifyInstancesChargeType返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 該參數表示對應配置實例轉換計費模式的價格。
        :type Price: :class:`taifucloudcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewInstancesRequest(AbstractModel):
    """InquiryPriceRenewInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲100。
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的續約時長、是否設置自動續約等屬性。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param DryRun: 試運作。
        :type DryRun: bool
        :param RenewPortableDataDisk: 是否續約彈性數據盤。取值範圍：<br><li>TRUE：表示續約包年包月實例同時續約其掛載的彈性數據盤<br><li>FALSE：表示續約包年包月實例同時不再續約其掛載的彈性數據盤<br><br>預設取值：TRUE。
        :type RenewPortableDataDisk: bool
        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None
        self.DryRun = None
        self.RenewPortableDataDisk = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.DryRun = params.get("DryRun")
        self.RenewPortableDataDisk = params.get("RenewPortableDataDisk")


class InquiryPriceRenewInstancesResponse(AbstractModel):
    """InquiryPriceRenewInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 該參數表示對應配置實例的價格。
        :type Price: :class:`taifucloudcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetInstanceRequest(AbstractModel):
    """InquiryPriceResetInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID。可通過 [DescribeInstances](https://cloud.taifucloud.com/document/api/213/15728) API返回值中的`InstanceId`獲取。
        :type InstanceId: str
        :param ImageId: 指定有效的[映像](/document/product/213/4940)ID，格式形如`img-xxx`。映像類型分爲四種：<br/><li>公共映像</li><li>自定義映像</li><li>共享映像</li><li>服務市場映像</li><br/>可通過以下方式獲取可用的映像ID：<br/><li>`公共映像`、`自定義映像`、`共享映像`的映像ID可通過登入[控制台](https://console.cloud.taifucloud.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查詢；`服務映像市場`的映像ID可通過[雲市場](https://market.cloud.taifucloud.com/list)查詢。</li><li>通過調用介面 [DescribeImages](https://cloud.taifucloud.com/document/api/213/15715) ，取返回訊息中的`ImageId`欄位。</li>
        :type ImageId: str
        :param SystemDisk: 實例系統盤配置訊息。系統盤爲雲盤的實例可以通過該參數指定重裝後的系統盤大小來實現對系統盤的擴容操作，若不指定則預設系統盤大小保持不變。系統盤大小只支援擴容不支援縮容；重裝只支援修改系統盤的大小，不能修改系統盤的類型。
        :type SystemDisk: :class:`taifucloudcloud.cvm.v20170312.models.SystemDisk`
        :param LoginSettings: 實例登入設置。通過該參數可以設置實例的登入方式密碼、金鑰或保持映像的原始登入設置。預設情況下會随機生成密碼，並以站内信方式知會到用戶。
        :type LoginSettings: :class:`taifucloudcloud.cvm.v20170312.models.LoginSettings`
        :param EnhancedService: 增強服務。通過該參數可以指定是否開啓雲安全、雲監控等服務。若不指定該參數，則預設開啓雲監控、雲安全服務。
        :type EnhancedService: :class:`taifucloudcloud.cvm.v20170312.models.EnhancedService`
        """
        self.InstanceId = None
        self.ImageId = None
        self.SystemDisk = None
        self.LoginSettings = None
        self.EnhancedService = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))


class InquiryPriceResetInstanceResponse(AbstractModel):
    """InquiryPriceResetInstance返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 該參數表示重裝成對應配置實例的價格。
        :type Price: :class:`taifucloudcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲100。當調整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 計費方式的頻寬時，只支援一個實例。
        :type InstanceIds: list of str
        :param InternetAccessible: 公網出頻寬配置。不同機型頻寬上限範圍不一緻，具體限制詳見頻寬限制對賬表。暫時只支援`InternetMaxBandwidthOut`參數。
        :type InternetAccessible: :class:`taifucloudcloud.cvm.v20170312.models.InternetAccessible`
        :param StartTime: 頻寬生效的起始時間。格式：`YYYY-MM-DD`，例如：`2016-10-30`。起始時間不能早於當前時間。如果起始時間是今天則新設置的頻寬立即生效。該參數只對包年包月頻寬有效，其他模式頻寬不支援該參數，否則介面會以相應錯誤碼返回。
        :type StartTime: str
        :param EndTime: 頻寬生效的終止時間。格式：`YYYY-MM-DD`，例如：`2016-10-30`。新設置的頻寬的有效期包含終止時間此日期。終止時間不能晚於包年包月實例的到期時間。實例的到期時間可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`ExpiredTime`獲取。該參數只對包年包月頻寬有效，其他模式頻寬不支援該參數，否則介面會以相應錯誤碼返回。
        :type EndTime: str
        """
        self.InstanceIds = None
        self.InternetAccessible = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class InquiryPriceResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetInstancesInternetMaxBandwidth返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 該參數表示頻寬調整爲對應大小之後的價格。
        :type Price: :class:`taifucloudcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetInstancesTypeRequest(AbstractModel):
    """InquiryPriceResetInstancesType請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲1。
        :type InstanceIds: list of str
        :param InstanceType: 實例機型。不同實例機型指定了不同的資源規格，具體取值可參見附表實例資源規格對照表，也可以調用查詢實例資源規格清單介面獲得最新的規格表。
        :type InstanceType: str
        """
        self.InstanceIds = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")


class InquiryPriceResetInstancesTypeResponse(AbstractModel):
    """InquiryPriceResetInstancesType返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 該參數表示調整成對應機型實例的價格。
        :type Price: :class:`taifucloudcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResizeInstanceDisksRequest(AbstractModel):
    """InquiryPriceResizeInstanceDisks請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。
        :type InstanceId: str
        :param DataDisks: 待擴容的數據盤配置訊息。只支援擴容非彈性數據盤（[`DescribeDisks`](https://cloud.taifucloud.com/document/api/362/16315)介面返回值中的`Portable`爲`false`表示非彈性），且[數據盤類型](/document/api/213/9452#block_device)爲：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。數據盤容量單位：GB。最小擴容步長：10G。關於數據盤類型的選擇請參考硬碟産品簡介。可選數據盤類型受到實例類型`InstanceType`限制。另外允許擴容的最大容量也因數據盤類型的不同而有所差異。
        :type DataDisks: list of DataDisk
        :param ForceStop: 是否對運作中的實例選擇強制關機。建議對運作中的實例先手動關機，然後再重置用戶密碼。取值範圍：<br><li>TRUE：表示在正常關機失敗後進行強制關機<br><li>FALSE：表示在正常關機失敗後不進行強制關機<br><br>預設取值：FALSE。<br><br>強制關機的效果等同於關閉物理電腦的電源開關。強制關機可能會導緻數據丢失或文件系統損壞，請僅在服務器不能正常關機時使用。
        :type ForceStop: bool
        """
        self.InstanceId = None
        self.DataDisks = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.ForceStop = params.get("ForceStop")


class InquiryPriceResizeInstanceDisksResponse(AbstractModel):
    """InquiryPriceResizeInstanceDisks返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 該參數表示磁盤擴容成對應配置的價格。
        :type Price: :class:`taifucloudcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRunInstancesRequest(AbstractModel):
    """InquiryPriceRunInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Placement: 實例所在的位置。通過該參數可以指定實例所屬可用區，所屬項目等屬性。
        :type Placement: :class:`taifucloudcloud.cvm.v20170312.models.Placement`
        :param ImageId: 指定有效的[映像](https://cloud.taifucloud.com/document/product/213/4940)ID，格式形如`img-xxx`。映像類型分爲四種：<br/><li>公共映像</li><li>自定義映像</li><li>共享映像</li><li>服務市場映像</li><br/>可通過以下方式獲取可用的映像ID：<br/><li>`公共映像`、`自定義映像`、`共享映像`的映像ID可通過登入[控制台](https://console.cloud.taifucloud.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查詢；`服務映像市場`的映像ID可通過[雲市場](https://market.cloud.taifucloud.com/list)查詢。</li><li>通過調用介面 [DescribeImages](https://cloud.taifucloud.com/document/api/213/15715) ，取返回訊息中的`ImageId`欄位。</li>
        :type ImageId: str
        :param InstanceChargeType: 實例[計費類型](https://cloud.taifucloud.com/document/product/213/2180)。<br><li>PREPAID：預付費，即包年包月<br><li>POSTPAID_BY_HOUR：按小時後付費<br>預設值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param InstanceType: 實例機型。不同實例機型指定了不同的資源規格，具體取值可通過調用介面[DescribeInstanceTypeConfigs](https://cloud.taifucloud.com/document/api/213/15749)來獲得最新的規格表或參見[CVM實例配置](https://cloud.taifucloud.com/document/product/213/2177)描述。若不指定該參數，則預設機型爲S1.SMALL1。
        :type InstanceType: str
        :param SystemDisk: 實例系統盤配置訊息。若不指定該參數，則按照系統預設值進行分配。
        :type SystemDisk: :class:`taifucloudcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: 實例數據盤配置訊息。若不指定該參數，則預設不購買數據盤。支援購買的時候指定11塊數據盤，其中最多包含1塊LOCAL_BASIC數據盤或者LOCAL_SSD數據盤，最多包含10塊CLOUD_BASIC數據盤、CLOUD_PREMIUM數據盤或者CLOUD_SSD數據盤。
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: 私有網絡相關訊息配置。通過該參數可以指定私有網絡的ID，子網ID等訊息。若不指定該參數，則預設使用基礎網絡。若在此參數中指定了私有網絡ip，那麽InstanceCount參數只能爲1。
        :type VirtualPrivateCloud: :class:`taifucloudcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: 公網頻寬相關訊息設置。若不指定該參數，則預設公網頻寬爲0Mbps。
        :type InternetAccessible: :class:`taifucloudcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: 購買實例數量。取值範圍：[1，100]。預設取值：1。指定購買實例的數量不能超過用戶所能購買的剩餘配額數量，具體配額相關限制詳見[CVM實例購買限制](https://cloud.taifucloud.com/document/product/213/2664)。
        :type InstanceCount: int
        :param InstanceName: 實例顯示名稱。<br><li>不指定實例顯示名稱則預設顯示‘未命名’。</li><li>購買多台實例，如果指定模式串`{R:x}`，表示生成數字`[x, x+n-1]`，其中`n`表示購買實例的數量，例如`server_{R:3}`，購買1台時，實例顯示名稱爲`server_3`；購買2台時，實例顯示名稱分别爲`server_3`，`server_4`。支援指定多個模式串`{R:x}`。</li><li>購買多台實例，如果不指定模式串，則在實例顯示名稱添加後綴`1、2...n`，其中`n`表示購買實例的數量，例如`server_`，購買2台時，實例顯示名稱分别爲`server_1`，`server_2`。
        :type InstanceName: str
        :param LoginSettings: 實例登入設置。通過該參數可以設置實例的登入方式密碼、金鑰或保持映像的原始登入設置。預設情況下會随機生成密碼，並以站内信方式知會到用戶。
        :type LoginSettings: :class:`taifucloudcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: 實例所屬安全組。該參數可以通過調用 [DescribeSecurityGroups](https://cloud.taifucloud.com/document/api/215/15808) 的返回值中的sgId欄位來獲取。若不指定該參數，則預設不綁定安全組。
        :type SecurityGroupIds: list of str
        :param EnhancedService: 增強服務。通過該參數可以指定是否開啓雲安全、雲監控等服務。若不指定該參數，則預設開啓雲監控、雲安全服務。
        :type EnhancedService: :class:`taifucloudcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: 用於保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。<br>更多詳細訊息請參閱：如何保證幂等性。
        :type ClientToken: str
        :param HostName: 雲伺服器的主機名。<br><li>點號（.）和短橫線（-）不能作爲 HostName 的首尾字元，不能連續使用。<br><li>Windows 實例：名字元長度爲[2, 15]，允許字母（不限制大小寫）、數字和短橫線（-）組成，不支援點號（.），不能全是數字。<br><li>其他類型（Linux 等）實例：字元長度爲[2, 30]，允許支援多個點號，點之間爲一段，每段允許字母（不限制大小寫）、數字和短橫線（-）組成。
        :type HostName: str
        :param TagSpecification: 標簽描述清單。通過指定該參數可以同時綁定標簽到相應的資源實例，當前僅支援綁定標簽到雲主機實例。
        :type TagSpecification: list of TagSpecification
        :param InstanceMarketOptions: 實例的市場相關選項，如競價實例相關參數
        :type InstanceMarketOptions: :class:`taifucloudcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        """
        self.Placement = None
        self.ImageId = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceCount = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.ClientToken = None
        self.HostName = None
        self.TagSpecification = None
        self.InstanceMarketOptions = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ImageId = params.get("ImageId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ClientToken = params.get("ClientToken")
        self.HostName = params.get("HostName")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))


class InquiryPriceRunInstancesResponse(AbstractModel):
    """InquiryPriceRunInstances返回參數結構體

    """

    def __init__(self):
        """
        :param Price: 該參數表示對應配置實例的價格。
        :type Price: :class:`taifucloudcloud.cvm.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """描述實例的訊息

    """

    def __init__(self):
        """
        :param Placement: 實例所在的位置。
        :type Placement: :class:`taifucloudcloud.cvm.v20170312.models.Placement`
        :param InstanceId: 實例`ID`。
        :type InstanceId: str
        :param InstanceType: 實例機型。
        :type InstanceType: str
        :param CPU: 實例的CPU核數，單位：核。
        :type CPU: int
        :param Memory: 實例内存容量，單位：`GB`。
        :type Memory: int
        :param RestrictState: 實例業務狀态。取值範圍：<br><li>NORMAL：表示正常狀态的實例<br><li>EXPIRED：表示過期的實例<br><li>PROTECTIVELY_ISOLATED：表示被安全隔離的實例。
        :type RestrictState: str
        :param InstanceName: 實例名稱。
        :type InstanceName: str
        :param InstanceChargeType: 實例計費模式。取值範圍：<br><li>`PREPAID`：表示預付費，即包年包月<br><li>`POSTPAID_BY_HOUR`：表示後付費，即按量計費<br><li>`CDHPAID`：`CDH`付費，即只對`CDH`計費，不對`CDH`上的實例計費。
        :type InstanceChargeType: str
        :param SystemDisk: 實例系統盤訊息。
        :type SystemDisk: :class:`taifucloudcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: 實例數據盤訊息。只包含随實例購買的數據盤。
        :type DataDisks: list of DataDisk
        :param PrivateIpAddresses: 實例主網卡的内網`IP`清單。
        :type PrivateIpAddresses: list of str
        :param PublicIpAddresses: 實例主網卡的公網`IP`清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param InternetAccessible: 實例頻寬訊息。
        :type InternetAccessible: :class:`taifucloudcloud.cvm.v20170312.models.InternetAccessible`
        :param VirtualPrivateCloud: 實例所屬虛拟私有網絡訊息。
        :type VirtualPrivateCloud: :class:`taifucloudcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param ImageId: 生産實例所使用的映像`ID`。
        :type ImageId: str
        :param RenewFlag: 自動續約標識。取值範圍：<br><li>`NOTIFY_AND_MANUAL_RENEW`：表示通知即将過期，但不自動續約<br><li>`NOTIFY_AND_AUTO_RENEW`：表示通知即将過期，而且自動續約<br><li>`DISABLE_NOTIFY_AND_MANUAL_RENEW`：表示不通知即将過期，也不自動續約。
        :type RenewFlag: str
        :param CreatedTime: 創建時間。按照`ISO8601`標準表示，並且使用`UTC`時間。格式爲：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        :param ExpiredTime: 到期時間。按照`ISO8601`標準表示，並且使用`UTC`時間。格式爲：`YYYY-MM-DDThh:mm:ssZ`。
        :type ExpiredTime: str
        :param OsName: 作業系統名稱。
        :type OsName: str
        :param SecurityGroupIds: 實例所屬安全組。該參數可以通過調用 [DescribeSecurityGroups](https://cloud.taifucloud.com/document/api/215/15808) 的返回值中的sgId欄位來獲取。
        :type SecurityGroupIds: list of str
        :param LoginSettings: 實例登入設置。目前只返回實例所關聯的金鑰。
        :type LoginSettings: :class:`taifucloudcloud.cvm.v20170312.models.LoginSettings`
        :param InstanceState: 實例狀态。取值範圍：<br><li>PENDING：表示創建中<br></li><li>LAUNCH_FAILED：表示創建失敗<br></li><li>RUNNING：表示運作中<br></li><li>STOPPED：表示關機<br></li><li>STARTING：表示開機中<br></li><li>STOPPING：表示關機中<br></li><li>REBOOTING：表示重啓中<br></li><li>SHUTDOWN：表示停止待銷毀<br></li><li>TERMINATING：表示銷毀中。<br></li>
        :type InstanceState: str
        :param Tags: 實例關聯的標簽清單。
        :type Tags: list of Tag
        :param StopChargingMode: 實例的關機計費模式。
取值範圍：<br><li>KEEP_CHARGING：關機繼續收費<br><li>STOP_CHARGING：關機停止收費<li>NOT_APPLICABLE：實例處於非關機狀态或者不适用關機停止計費的條件<br>
        :type StopChargingMode: str
        """
        self.Placement = None
        self.InstanceId = None
        self.InstanceType = None
        self.CPU = None
        self.Memory = None
        self.RestrictState = None
        self.InstanceName = None
        self.InstanceChargeType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None
        self.InternetAccessible = None
        self.VirtualPrivateCloud = None
        self.ImageId = None
        self.RenewFlag = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.OsName = None
        self.SecurityGroupIds = None
        self.LoginSettings = None
        self.InstanceState = None
        self.Tags = None
        self.StopChargingMode = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.InstanceId = params.get("InstanceId")
        self.InstanceType = params.get("InstanceType")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.RestrictState = params.get("RestrictState")
        self.InstanceName = params.get("InstanceName")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ImageId = params.get("ImageId")
        self.RenewFlag = params.get("RenewFlag")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.OsName = params.get("OsName")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.InstanceState = params.get("InstanceState")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.StopChargingMode = params.get("StopChargingMode")


class InstanceChargePrepaid(AbstractModel):
    """描述了實例的計費模式

    """

    def __init__(self):
        """
        :param Period: 購買實例的時長，單位：月。取值範圍：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自動續約標識。取值範圍：<br><li>NOTIFY_AND_AUTO_RENEW：通知過期且自動續約<br><li>NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約<br><br>預設取值：NOTIFY_AND_MANUAL_RENEW。若該參數指定爲NOTIFY_AND_AUTO_RENEW，在帳戶餘額充足的情況下，實例到期後将按月自動續約。
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class InstanceFamilyConfig(AbstractModel):
    """描述實例的機型族配置訊息
    形如：{'InstanceFamilyName': '標準型S1', 'InstanceFamily': 'S1'}、{'InstanceFamilyName': '網絡優化型N1', 'InstanceFamily': 'N1'}、{'InstanceFamilyName': '高IO型I1', 'InstanceFamily': 'I1'}等。

    """

    def __init__(self):
        """
        :param InstanceFamilyName: 機型族名稱的中文全稱。
        :type InstanceFamilyName: str
        :param InstanceFamily: 機型族名稱的英文簡稱。
        :type InstanceFamily: str
        """
        self.InstanceFamilyName = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.InstanceFamilyName = params.get("InstanceFamilyName")
        self.InstanceFamily = params.get("InstanceFamily")


class InstanceMarketOptionsRequest(AbstractModel):
    """競價請求相關選項

    """

    def __init__(self):
        """
        :param SpotOptions: 競價相關選項
        :type SpotOptions: :class:`taifucloudcloud.cvm.v20170312.models.SpotMarketOptions`
        :param MarketType: 市場選項類型，當前只支援取值：spot
        :type MarketType: str
        """
        self.SpotOptions = None
        self.MarketType = None


    def _deserialize(self, params):
        if params.get("SpotOptions") is not None:
            self.SpotOptions = SpotMarketOptions()
            self.SpotOptions._deserialize(params.get("SpotOptions"))
        self.MarketType = params.get("MarketType")


class InstanceStatus(AbstractModel):
    """描述實例的狀态。狀态類型詳見[實例狀态表](/document/api/213/9452#INSTANCE_STATE)

    """

    def __init__(self):
        """
        :param InstanceId: 實例`ID`。
        :type InstanceId: str
        :param InstanceState: [實例狀态](/document/api/213/9452#INSTANCE_STATE)。
        :type InstanceState: str
        """
        self.InstanceId = None
        self.InstanceState = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceState = params.get("InstanceState")


class InstanceTypeConfig(AbstractModel):
    """描述實例機型配置訊息

    """

    def __init__(self):
        """
        :param Zone: 可用區。
        :type Zone: str
        :param InstanceType: 實例機型。
        :type InstanceType: str
        :param InstanceFamily: 實例機型系列。
        :type InstanceFamily: str
        :param GPU: GPU核數，單位：核。
        :type GPU: int
        :param CPU: CPU核數，單位：核。
        :type CPU: int
        :param Memory: 内存容量，單位：`GB`。
        :type Memory: int
        """
        self.Zone = None
        self.InstanceType = None
        self.InstanceFamily = None
        self.GPU = None
        self.CPU = None
        self.Memory = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceFamily = params.get("InstanceFamily")
        self.GPU = params.get("GPU")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")


class InstanceTypeQuotaItem(AbstractModel):
    """描述實例機型配額訊息。

    """

    def __init__(self):
        """
        :param Zone: 可用區。
        :type Zone: str
        :param InstanceType: 實例機型。
        :type InstanceType: str
        :param InstanceChargeType: 實例計費模式。取值範圍： <br><li>PREPAID：表示預付費，即包年包月<br><li>POSTPAID_BY_HOUR：表示後付費，即按量計費<br><li>CDHPAID：表示[CDH](https://cloud.taifucloud.com/document/product/416)付費，即只對CDH計費，不對CDH上的實例計費。
        :type InstanceChargeType: str
        :param NetworkCard: 網卡類型，例如：25代表25G網卡
        :type NetworkCard: int
        :param Externals: 擴展屬性。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Externals: :class:`taifucloudcloud.cvm.v20170312.models.Externals`
        :param Cpu: 實例的CPU核數，單位：核。
        :type Cpu: int
        :param Memory: 實例内存容量，單位：`GB`。
        :type Memory: int
        :param InstanceFamily: 實例機型系列。
        :type InstanceFamily: str
        :param TypeName: 機型名稱。
        :type TypeName: str
        :param LocalDiskTypeList: 本地磁盤規格清單。當該參數返回爲空值時，表示當前情況下無法創建本地盤。
        :type LocalDiskTypeList: list of LocalDiskType
        :param Status: 實例是否售賣。取值範圍： <br><li>SELL：表示實例可購買<br><li>SOLD_OUT：表示實例已售罄。
        :type Status: str
        :param Price: 實例的售賣價格。
        :type Price: :class:`taifucloudcloud.cvm.v20170312.models.ItemPrice`
        """
        self.Zone = None
        self.InstanceType = None
        self.InstanceChargeType = None
        self.NetworkCard = None
        self.Externals = None
        self.Cpu = None
        self.Memory = None
        self.InstanceFamily = None
        self.TypeName = None
        self.LocalDiskTypeList = None
        self.Status = None
        self.Price = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.NetworkCard = params.get("NetworkCard")
        if params.get("Externals") is not None:
            self.Externals = Externals()
            self.Externals._deserialize(params.get("Externals"))
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.InstanceFamily = params.get("InstanceFamily")
        self.TypeName = params.get("TypeName")
        if params.get("LocalDiskTypeList") is not None:
            self.LocalDiskTypeList = []
            for item in params.get("LocalDiskTypeList"):
                obj = LocalDiskType()
                obj._deserialize(item)
                self.LocalDiskTypeList.append(obj)
        self.Status = params.get("Status")
        if params.get("Price") is not None:
            self.Price = ItemPrice()
            self.Price._deserialize(params.get("Price"))


class InternetAccessible(AbstractModel):
    """描述了實例的公網可訪問性，聲明了實例的公網使用計費模式，最大頻寬等

    """

    def __init__(self):
        """
        :param InternetChargeType: 網絡計費類型。取值範圍：<br><li>BANDWIDTH_PREPAID：預付費按頻寬結算<br><li>TRAFFIC_POSTPAID_BY_HOUR：流量按小時後付費<br><li>BANDWIDTH_POSTPAID_BY_HOUR：頻寬按小時後付費<br><li>BANDWIDTH_PACKAGE：頻寬包用戶<br>預設取值：非頻寬包用戶預設與子機付費類型保持一緻。
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 公網出頻寬上限，單位：Mbps。預設值：0Mbps。不同機型頻寬上限範圍不一緻，具體限制詳見[購買網絡頻寬](/document/product/213/509)。
        :type InternetMaxBandwidthOut: int
        :param PublicIpAssigned: 是否分配公網IP。取值範圍：<br><li>TRUE：表示分配公網IP<br><li>FALSE：表示不分配公網IP<br><br>當公網頻寬大於0Mbps時，可自由選擇開通與否，預設開通公網IP；當公網頻寬爲0，則不允許分配公網IP。
        :type PublicIpAssigned: bool
        :param BandwidthPackageId: 頻寬包ID。可通過[`DescribeBandwidthPackages`](https://cloud.taifucloud.com/document/api/215/19209)介面返回值中的`BandwidthPackageId`獲取。
        :type BandwidthPackageId: str
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.PublicIpAssigned = None
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.PublicIpAssigned = params.get("PublicIpAssigned")
        self.BandwidthPackageId = params.get("BandwidthPackageId")


class InternetBandwidthConfig(AbstractModel):
    """描述了按頻寬計費的相關訊息

    """

    def __init__(self):
        """
        :param StartTime: 開始時間。按照`ISO8601`標準表示，並且使用`UTC`時間。格式爲：`YYYY-MM-DDThh:mm:ssZ`。
        :type StartTime: str
        :param EndTime: 結束時間。按照`ISO8601`標準表示，並且使用`UTC`時間。格式爲：`YYYY-MM-DDThh:mm:ssZ`。
        :type EndTime: str
        :param InternetAccessible: 實例頻寬訊息。
        :type InternetAccessible: :class:`taifucloudcloud.cvm.v20170312.models.InternetAccessible`
        """
        self.StartTime = None
        self.EndTime = None
        self.InternetAccessible = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))


class InternetChargeTypeConfig(AbstractModel):
    """描述了網絡計費

    """

    def __init__(self):
        """
        :param InternetChargeType: 網絡計費模式。
        :type InternetChargeType: str
        :param Description: 網絡計費模式描述訊息。
        :type Description: str
        """
        self.InternetChargeType = None
        self.Description = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.Description = params.get("Description")


class ItemPrice(AbstractModel):
    """描述了單項的價格訊息

    """

    def __init__(self):
        """
        :param UnitPrice: 後續單價，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param ChargeUnit: 後續計價單元，可取值範圍： <br><li>HOUR：表示計價單元是按每小時來計算。當前涉及該計價單元的場景有：實例按小時後付費（POSTPAID_BY_HOUR）、頻寬按小時後付費（BANDWIDTH_POSTPAID_BY_HOUR）：<br><li>GB：表示計價單元是按每GB來計算。當前涉及該計價單元的場景有：流量按小時後付費（TRAFFIC_POSTPAID_BY_HOUR）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param OriginalPrice: 預支費用的原價，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param DiscountPrice: 預支費用的折扣價，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")


class KeyPair(AbstractModel):
    """描述金鑰對訊息

    """

    def __init__(self):
        """
        :param KeyId: 金鑰對的`ID`，是金鑰對的唯一標識。
        :type KeyId: str
        :param KeyName: 金鑰對名稱。
        :type KeyName: str
        :param ProjectId: 金鑰對所屬的項目`ID`。
        :type ProjectId: int
        :param Description: 金鑰對描述訊息。
        :type Description: str
        :param PublicKey: 金鑰對的純文本公鑰。
        :type PublicKey: str
        :param PrivateKey: 金鑰對的純文本私鑰。Top Cloud 不會保管私鑰，請用戶自行妥善保存。
        :type PrivateKey: str
        :param AssociatedInstanceIds: 金鑰關聯的實例`ID`清單。
        :type AssociatedInstanceIds: list of str
        :param CreatedTime: 創建時間。按照`ISO8601`標準表示，並且使用`UTC`時間。格式爲：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        """
        self.KeyId = None
        self.KeyName = None
        self.ProjectId = None
        self.Description = None
        self.PublicKey = None
        self.PrivateKey = None
        self.AssociatedInstanceIds = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyName = params.get("KeyName")
        self.ProjectId = params.get("ProjectId")
        self.Description = params.get("Description")
        self.PublicKey = params.get("PublicKey")
        self.PrivateKey = params.get("PrivateKey")
        self.AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self.CreatedTime = params.get("CreatedTime")


class LocalDiskType(AbstractModel):
    """本地磁盤規格

    """

    def __init__(self):
        """
        :param Type: 本地磁盤類型。
        :type Type: str
        :param PartitionType: 本地磁盤屬性。
        :type PartitionType: str
        :param MinSize: 本地磁盤最小值。
        :type MinSize: int
        :param MaxSize: 本地磁盤最大值。
        :type MaxSize: int
        """
        self.Type = None
        self.PartitionType = None
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PartitionType = params.get("PartitionType")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")


class LoginSettings(AbstractModel):
    """描述了實例登入相關配置與訊息。

    """

    def __init__(self):
        """
        :param Password: 實例登入密碼。不同作業系統類型密碼複雜度限制不一樣，具體如下：<br><li>Linux實例密碼必須8到16位，至少包括兩項[a-z，A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]中的特殊符號。<br><li>Windows實例密碼必須12到16位，至少包括三項[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]中的特殊符號。<br><br>若不指定該參數，則由系統随機生成密碼，並通過站内信方式通知到用戶。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Password: str
        :param KeyIds: 金鑰ID清單。關聯金鑰後，就可以通過對應的私鑰來訪問實例；KeyId可通過介面DescribeKeyPairs獲取，金鑰與密碼不能同時指定，同時Windows作業系統不支援指定金鑰。當前僅支援購買的時候指定一個金鑰。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyIds: list of str
        :param KeepImageLogin: 保持映像的原始設置。該參數與Password或KeyIds.N不能同時指定。只有使用自定義映像、共享映像或外部導入映像創建實例時才能指定該參數爲TRUE。取值範圍：<br><li>TRUE：表示保持映像的登入設置<br><li>FALSE：表示不保持映像的登入設置<br><br>預設取值：FALSE。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeepImageLogin: str
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")


class ModifyDisasterRecoverGroupAttributeRequest(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param DisasterRecoverGroupId: 分散置放群組ID，可使用[DescribeDisasterRecoverGroups](https://cloud.taifucloud.com/document/api/213/17810)介面獲取。
        :type DisasterRecoverGroupId: str
        :param Name: 分散置放群組名稱，長度1-60個字元，支援中、英文。
        :type Name: str
        """
        self.DisasterRecoverGroupId = None
        self.Name = None


    def _deserialize(self, params):
        self.DisasterRecoverGroupId = params.get("DisasterRecoverGroupId")
        self.Name = params.get("Name")


class ModifyDisasterRecoverGroupAttributeResponse(AbstractModel):
    """ModifyDisasterRecoverGroupAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHostsAttributeRequest(AbstractModel):
    """ModifyHostsAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param HostIds: 一個或多個待操作的CDH實例ID。
        :type HostIds: list of str
        :param HostName: CDH實例顯示名稱。可任意命名，但不得超過60個字元。
        :type HostName: str
        :param RenewFlag: 自動續約標識。取值範圍：<br><li>NOTIFY_AND_AUTO_RENEW：通知過期且自動續約<br><li>NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約<br><br>若該參數指定爲NOTIFY_AND_AUTO_RENEW，在帳戶餘額充足的情況下，實例到期後将按月自動續約。
        :type RenewFlag: str
        """
        self.HostIds = None
        self.HostName = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.HostIds = params.get("HostIds")
        self.HostName = params.get("HostName")
        self.RenewFlag = params.get("RenewFlag")


class ModifyHostsAttributeResponse(AbstractModel):
    """ModifyHostsAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ImageId: 映像ID，形如`img-gvbnzy6f`。映像ID可以通過如下方式獲取：<br><li>通過[DescribeImages](https://cloud.taifucloud.com/document/api/213/15715)介面返回的`ImageId`獲取。<br><li>通過[映像控制台](https://console.cloud.taifucloud.com/cvm/image)獲取。
        :type ImageId: str
        :param ImageName: 設置新的映像名稱；必須滿足下列限制：<br> <li> 不得超過20個字元。<br> <li> 映像名稱不能與已有映像重複。
        :type ImageName: str
        :param ImageDescription: 設置新的映像描述；必須滿足下列限制：<br> <li> 不得超過60個字元。
        :type ImageDescription: str
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageDescription = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")


class ModifyImageAttributeResponse(AbstractModel):
    """ModifyImageAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageSharePermissionRequest(AbstractModel):
    """ModifyImageSharePermission請求參數結構體

    """

    def __init__(self):
        """
        :param ImageId: 映像ID，形如`img-gvbnzy6f`。映像Id可以通過如下方式獲取：<br><li>通過[DescribeImages](https://cloud.taifucloud.com/document/api/213/15715)介面返回的`ImageId`獲取。<br><li>通過[映像控制台](https://console.cloud.taifucloud.com/cvm/image)獲取。 <br>映像ID必須指定爲狀态爲`NORMAL`的映像。映像狀态請參考[映像數據表](/document/api/213/9452#image_state)。
        :type ImageId: str
        :param AccountIds: 接收分享映像的賬號Id清單，array型參數的格式可以參考[API簡介](/document/api/213/568)。帳號ID不同於 號，查詢用戶帳號ID請檢視[帳號訊息](https://console.cloud.taifucloud.com/developer)中的帳號ID欄。
        :type AccountIds: list of str
        :param Permission: 操作，包括 `SHARE`，`CANCEL`。其中`SHARE`代表分享操作，`CANCEL`代表取消分享操作。
        :type Permission: str
        """
        self.ImageId = None
        self.AccountIds = None
        self.Permission = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.AccountIds = params.get("AccountIds")
        self.Permission = params.get("Permission")


class ModifyImageSharePermissionResponse(AbstractModel):
    """ModifyImageSharePermission返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/9388) API返回值中的`InstanceId`獲取。每次請求允許操作的實例數量上限是100。
        :type InstanceIds: list of str
        :param InstanceName: 實例名稱。可任意命名，但不得超過60個字元。
        :type InstanceName: str
        :param SecurityGroups: 指定實例的安全組Id清單，子機将重新關聯指定清單的安全組，原本關聯的安全組會被解綁。
        :type SecurityGroups: list of str
        """
        self.InstanceIds = None
        self.InstanceName = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceName = params.get("InstanceName")
        self.SecurityGroups = params.get("SecurityGroups")


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesChargeTypeRequest(AbstractModel):
    """ModifyInstancesChargeType請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/9388)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲100。
        :type InstanceIds: list of str
        :param InstanceChargeType: 實例[計費類型](https://cloud.taifucloud.com/document/product/213/2180)。<br><li>PREPAID：預付費，即包年包月。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.cvm.v20170312.models.InstanceChargePrepaid`
        """
        self.InstanceIds = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class ModifyInstancesChargeTypeResponse(AbstractModel):
    """ModifyInstancesChargeType返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesProjectRequest(AbstractModel):
    """ModifyInstancesProject請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/9388) API返回值中的`InstanceId`獲取。每次請求允許操作的實例數量上限是100。
        :type InstanceIds: list of str
        :param ProjectId: 項目ID。項目可以使用[AddProject](https://cloud.taifucloud.com/doc/api/403/4398)介面創建。後續使用[DescribeInstances](https://cloud.taifucloud.com/document/api/213/9388)介面查詢實例時，項目ID可用於過濾結果。
        :type ProjectId: int
        """
        self.InstanceIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProjectId = params.get("ProjectId")


class ModifyInstancesProjectResponse(AbstractModel):
    """ModifyInstancesProject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesRenewFlagRequest(AbstractModel):
    """ModifyInstancesRenewFlag請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/9388) API返回值中的`InstanceId`獲取。每次請求允許操作的實例數量上限是100。
        :type InstanceIds: list of str
        :param RenewFlag: 自動續約標識。取值範圍：<br><li>NOTIFY_AND_AUTO_RENEW：通知過期且自動續約<br><li>NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約<br><br>若該參數指定爲NOTIFY_AND_AUTO_RENEW，在帳戶餘額充足的情況下，實例到期後将按月自動續約。
        :type RenewFlag: str
        """
        self.InstanceIds = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.RenewFlag = params.get("RenewFlag")


class ModifyInstancesRenewFlagResponse(AbstractModel):
    """ModifyInstancesRenewFlag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesVpcAttributeRequest(AbstractModel):
    """ModifyInstancesVpcAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 待操作的實例ID數組。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。
        :type InstanceIds: list of str
        :param VirtualPrivateCloud: 私有網絡相關訊息配置。通過該參數指定私有網絡的ID，子網ID，私有網絡ip等訊息。當指定私有網絡ID和子網ID（子網必須在實例所在的可用區）與指定實例所在私有網絡不一緻時，會将實例遷移至指定的私有網絡的子網下。可通過`PrivateIpAddresses`指定私有網絡子網IP，若需指定則所有已指定的實例均需要指定子網IP，此時`InstanceIds`與`PrivateIpAddresses`一一對應。不指定`PrivateIpAddresses`時随機分配私有網絡子網IP。
        :type VirtualPrivateCloud: :class:`taifucloudcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param ForceStop: 是否對運作中的實例選擇強制關機。預設爲TRUE。
        :type ForceStop: bool
        :param ReserveHostName: 是否保留主機名。預設爲FALSE。
        :type ReserveHostName: bool
        """
        self.InstanceIds = None
        self.VirtualPrivateCloud = None
        self.ForceStop = None
        self.ReserveHostName = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ForceStop = params.get("ForceStop")
        self.ReserveHostName = params.get("ReserveHostName")


class ModifyInstancesVpcAttributeResponse(AbstractModel):
    """ModifyInstancesVpcAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyKeyPairAttributeRequest(AbstractModel):
    """ModifyKeyPairAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 金鑰對ID，金鑰對ID形如：`skey-xxxxxxxx`。<br><br>可以通過以下方式獲取可用的金鑰 ID：<br><li>通過登入[控制台](https://console.cloud.taifucloud.com/cvm/sshkey)查詢金鑰 ID。<br><li>通過調用介面 [DescribeKeyPairs](https://cloud.taifucloud.com/document/api/213/9403) ，取返回訊息中的 `KeyId` 獲取金鑰對 ID。
        :type KeyId: str
        :param KeyName: 修改後的金鑰對名稱，可由數字，字母和下劃線組成，長度不超過25個字元。
        :type KeyName: str
        :param Description: 修改後的金鑰對描述訊息。可任意命名，但不得超過60個字元。
        :type Description: str
        """
        self.KeyId = None
        self.KeyName = None
        self.Description = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeyName = params.get("KeyName")
        self.Description = params.get("Description")


class ModifyKeyPairAttributeResponse(AbstractModel):
    """ModifyKeyPairAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OperationCountLimit(AbstractModel):
    """描述了單台實例操作次數限制

    """

    def __init__(self):
        """
        :param Operation: 實例操作。
        :type Operation: str
        :param InstanceId: 實例ID。
        :type InstanceId: str
        :param CurrentCount: 當前已使用次數，如果返回值爲-1表示該操作無次數限制。
        :type CurrentCount: int
        :param LimitCount: 操作次數最高額度，如果返回值爲-1表示該操作無次數限制，如果返回值爲0表示不支援調整配置。
        :type LimitCount: int
        """
        self.Operation = None
        self.InstanceId = None
        self.CurrentCount = None
        self.LimitCount = None


    def _deserialize(self, params):
        self.Operation = params.get("Operation")
        self.InstanceId = params.get("InstanceId")
        self.CurrentCount = params.get("CurrentCount")
        self.LimitCount = params.get("LimitCount")


class OsVersion(AbstractModel):
    """作業系統支援的類型。

    """

    def __init__(self):
        """
        :param OsName: 作業系統類型
        :type OsName: str
        :param OsVersions: 支援的作業系統版本
        :type OsVersions: list of str
        :param Architecture: 支援的作業系統架構
        :type Architecture: list of str
        """
        self.OsName = None
        self.OsVersions = None
        self.Architecture = None


    def _deserialize(self, params):
        self.OsName = params.get("OsName")
        self.OsVersions = params.get("OsVersions")
        self.Architecture = params.get("Architecture")


class Placement(AbstractModel):
    """描述了實例的抽象位置，包括其所在的可用區，所屬的項目，宿主機等（僅CDH産品可用）

    """

    def __init__(self):
        """
        :param Zone: 實例所屬的[可用區](/document/product/213/9452#zone)ID。該參數也可以通過調用  [DescribeZones](/document/api/213/9455) 的返回值中的Zone欄位來獲取。
        :type Zone: str
        :param ProjectId: 實例所屬項目ID。該參數可以通過調用 [DescribeProject](/document/api/378/4400) 的返回值中的 projectId 欄位來獲取。不填爲預設項目。
        :type ProjectId: int
        :param HostIds: 實例所屬的專用宿主機ID清單。如果您有購買專用宿主機並且指定了該參數，則您購買的實例就會随機的佈署在這些專用宿主機上。
        :type HostIds: list of str
        """
        self.Zone = None
        self.ProjectId = None
        self.HostIds = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.HostIds = params.get("HostIds")


class Price(AbstractModel):
    """價格

    """

    def __init__(self):
        """
        :param InstancePrice: 描述了實例價格。
        :type InstancePrice: :class:`taifucloudcloud.cvm.v20170312.models.ItemPrice`
        :param BandwidthPrice: 描述了網絡價格。
        :type BandwidthPrice: :class:`taifucloudcloud.cvm.v20170312.models.ItemPrice`
        """
        self.InstancePrice = None
        self.BandwidthPrice = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = ItemPrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self.BandwidthPrice = ItemPrice()
            self.BandwidthPrice._deserialize(params.get("BandwidthPrice"))


class RebootInstancesRequest(AbstractModel):
    """RebootInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/9388)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲100。
        :type InstanceIds: list of str
        :param ForceReboot: 是否在正常重啓失敗後選擇強制重啓實例。取值範圍：<br><li>TRUE：表示在正常重啓失敗後進行強制重啓<br><li>FALSE：表示在正常重啓失敗後不進行強制重啓<br><br>預設取值：FALSE。
        :type ForceReboot: bool
        """
        self.InstanceIds = None
        self.ForceReboot = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ForceReboot = params.get("ForceReboot")


class RebootInstancesResponse(AbstractModel):
    """RebootInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域訊息

    """

    def __init__(self):
        """
        :param Region: 地域名稱，例如，ap-guangzhou
        :type Region: str
        :param RegionName: 地域描述，例如，華南地區( )
        :type RegionName: str
        :param RegionState: 地域是否可用狀态
        :type RegionState: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionState = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionState = params.get("RegionState")


class RenewHostsRequest(AbstractModel):
    """RenewHosts請求參數結構體

    """

    def __init__(self):
        """
        :param HostIds: 一個或多個待操作的CDH實例ID。
        :type HostIds: list of str
        :param HostChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type HostChargePrepaid: :class:`taifucloudcloud.cvm.v20170312.models.ChargePrepaid`
        """
        self.HostIds = None
        self.HostChargePrepaid = None


    def _deserialize(self, params):
        self.HostIds = params.get("HostIds")
        if params.get("HostChargePrepaid") is not None:
            self.HostChargePrepaid = ChargePrepaid()
            self.HostChargePrepaid._deserialize(params.get("HostChargePrepaid"))


class RenewHostsResponse(AbstractModel):
    """RenewHosts返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewInstancesRequest(AbstractModel):
    """RenewInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/9388)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲100。
        :type InstanceIds: list of str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的續約時長、是否設置自動續約等屬性。包年包月實例該參數爲必傳參數。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param RenewPortableDataDisk: 是否續約彈性數據盤。取值範圍：<br><li>TRUE：表示續約包年包月實例同時續約其掛載的彈性數據盤<br><li>FALSE：表示續約包年包月實例同時不再續約其掛載的彈性數據盤<br><br>預設取值：TRUE。
        :type RenewPortableDataDisk: bool
        """
        self.InstanceIds = None
        self.InstanceChargePrepaid = None
        self.RenewPortableDataDisk = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.RenewPortableDataDisk = params.get("RenewPortableDataDisk")


class RenewInstancesResponse(AbstractModel):
    """RenewInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstanceRequest(AbstractModel):
    """ResetInstance請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID。可通過 [DescribeInstances](https://cloud.taifucloud.com/document/api/213/9388) API返回值中的`InstanceId`獲取。
        :type InstanceId: str
        :param ImageId: 指定有效的[映像](https://cloud.taifucloud.com/document/product/213/4940)ID，格式形如`img-xxx`。映像類型分爲四種：<br/><li>公共映像</li><li>自定義映像</li><li>共享映像</li><li>服務市場映像</li><br/>可通過以下方式獲取可用的映像ID：<br/><li>`公共映像`、`自定義映像`、`共享映像`的映像ID可通過登入[控制台](https://console.cloud.taifucloud.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查詢；`服務映像市場`的映像ID可通過[雲市場](https://market.cloud.taifucloud.com/list)查詢。</li><li>通過調用介面 [DescribeImages](https://cloud.taifucloud.com/document/api/213/9418) ，取返回訊息中的`ImageId`欄位。</li>
<br>預設取值：預設使用當前映像。
        :type ImageId: str
        :param SystemDisk: 實例系統盤配置訊息。系統盤爲雲盤的實例可以通過該參數指定重裝後的系統盤大小來實現對系統盤的擴容操作，若不指定則預設系統盤大小保持不變。系統盤大小只支援擴容不支援縮容；重裝只支援修改系統盤的大小，不能修改系統盤的類型。
        :type SystemDisk: :class:`taifucloudcloud.cvm.v20170312.models.SystemDisk`
        :param LoginSettings: 實例登入設置。通過該參數可以設置實例的登入方式密碼、金鑰或保持映像的原始登入設置。預設情況下會随機生成密碼，並以站内信方式知會到用戶。
        :type LoginSettings: :class:`taifucloudcloud.cvm.v20170312.models.LoginSettings`
        :param EnhancedService: 增強服務。通過該參數可以指定是否開啓雲安全、雲監控等服務。若不指定該參數，則預設開啓雲監控、雲安全服務。
        :type EnhancedService: :class:`taifucloudcloud.cvm.v20170312.models.EnhancedService`
        :param HostName: 重灌系統時，可以指定修改實例的HostName。
        :type HostName: str
        """
        self.InstanceId = None
        self.ImageId = None
        self.SystemDisk = None
        self.LoginSettings = None
        self.EnhancedService = None
        self.HostName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.HostName = params.get("HostName")


class ResetInstanceResponse(AbstractModel):
    """ResetInstance返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesInternetMaxBandwidthRequest(AbstractModel):
    """ResetInstancesInternetMaxBandwidth請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/9388)介面返回值中的 `InstanceId` 獲取。 每次請求批次實例的上限爲100。當調整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 計費方式的頻寬時，只支援一個實例。
        :type InstanceIds: list of str
        :param InternetAccessible: 公網出頻寬配置。不同機型頻寬上限範圍不一緻，具體限制詳見頻寬限制對賬表。暫時只支援 `InternetMaxBandwidthOut` 參數。
        :type InternetAccessible: :class:`taifucloudcloud.cvm.v20170312.models.InternetAccessible`
        :param StartTime: 頻寬生效的起始時間。格式：`YYYY-MM-DD`，例如：`2016-10-30`。起始時間不能早於當前時間。如果起始時間是今天則新設置的頻寬立即生效。該參數只對包年包月頻寬有效，其他模式頻寬不支援該參數，否則介面會以相應錯誤碼返回。
        :type StartTime: str
        :param EndTime: 頻寬生效的終止時間。格式： `YYYY-MM-DD` ，例如：`2016-10-30` 。新設置的頻寬的有效期包含終止時間此日期。終止時間不能晚於包年包月實例的到期時間。實例的到期時間可通過 [`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/9388)介面返回值中的`ExpiredTime`獲取。該參數只對包年包月頻寬有效，其他模式頻寬不支援該參數，否則介面會以相應錯誤碼返回。
        :type EndTime: str
        """
        self.InstanceIds = None
        self.InternetAccessible = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ResetInstancesInternetMaxBandwidthResponse(AbstractModel):
    """ResetInstancesInternetMaxBandwidth返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728) API返回值中的`InstanceId`獲取。每次請求允許操作的實例數量上限是100。
        :type InstanceIds: list of str
        :param Password: 實例登入密碼。不同作業系統類型密碼複雜度限制不一樣，具體如下：<br><li>`Linux`實例密碼必須8到16位，至少包括兩項`[a-z，A-Z]、[0-9]`和`[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]`中的符號。密碼不允許以`/`符號開頭。<br><li>`Windows`實例密碼必須12到16位，至少包括三項`[a-z]，[A-Z]，[0-9]`和`[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]`中的符號。密碼不允許以`/`符號開頭。<br><li>如果實例即包含`Linux`實例又包含`Windows`實例，則密碼複雜度限制按照`Windows`實例的限制。
        :type Password: str
        :param UserName: 待重置密碼的實例作業系統用戶名。不得超過64個字元。
        :type UserName: str
        :param ForceStop: 是否對運作中的實例選擇強制關機。建議對運作中的實例先手動關機，然後再重置用戶密碼。取值範圍：<br><li>TRUE：表示在正常關機失敗後進行強制關機<br><li>FALSE：表示在正常關機失敗後不進行強制關機<br><br>預設取值：FALSE。<br><br>強制關機的效果等同於關閉物理電腦的電源開關。強制關機可能會導緻數據丢失或文件系統損壞，請僅在服務器不能正常關機時使用。
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.Password = None
        self.UserName = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Password = params.get("Password")
        self.UserName = params.get("UserName")
        self.ForceStop = params.get("ForceStop")


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesTypeRequest(AbstractModel):
    """ResetInstancesType請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲1。
        :type InstanceIds: list of str
        :param InstanceType: 實例機型。不同實例機型指定了不同的資源規格，具體取值可通過調用介面[`DescribeInstanceTypeConfigs`](https://cloud.taifucloud.com/document/api/213/15749)來獲得最新的規格表或參見[實例類型](https://cloud.taifucloud.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param ForceStop: 是否對運作中的實例選擇強制關機。建議對運作中的實例先手動關機，然後再重置用戶密碼。取值範圍：<br><li>TRUE：表示在正常關機失敗後進行強制關機<br><li>FALSE：表示在正常關機失敗後不進行強制關機<br><br>預設取值：FALSE。<br><br>強制關機的效果等同於關閉物理電腦的電源開關。強制關機可能會導緻數據丢失或文件系統損壞，請僅在服務器不能正常關機時使用。
        :type ForceStop: bool
        """
        self.InstanceIds = None
        self.InstanceType = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceType = params.get("InstanceType")
        self.ForceStop = params.get("ForceStop")


class ResetInstancesTypeResponse(AbstractModel):
    """ResetInstancesType返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResizeInstanceDisksRequest(AbstractModel):
    """ResizeInstanceDisks請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。
        :type InstanceId: str
        :param DataDisks: 待擴容的數據盤配置訊息。只支援擴容非彈性數據盤（[`DescribeDisks`](https://cloud.taifucloud.com/document/api/362/16315)介面返回值中的`Portable`爲`false`表示非彈性），且[數據盤類型](/document/api/213/9452#block_device)爲：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。數據盤容量單位：GB。最小擴容步長：10G。關於數據盤類型的選擇請參考硬碟産品簡介。可選數據盤類型受到實例類型`InstanceType`限制。另外允許擴容的最大容量也因數據盤類型的不同而有所差異。
        :type DataDisks: list of DataDisk
        :param ForceStop: 是否對運作中的實例選擇強制關機。建議對運作中的實例先手動關機，然後再重置用戶密碼。取值範圍：<br><li>TRUE：表示在正常關機失敗後進行強制關機<br><li>FALSE：表示在正常關機失敗後不進行強制關機<br><br>預設取值：FALSE。<br><br>強制關機的效果等同於關閉物理電腦的電源開關。強制關機可能會導緻數據丢失或文件系統損壞，請僅在服務器不能正常關機時使用。
        :type ForceStop: bool
        """
        self.InstanceId = None
        self.DataDisks = None
        self.ForceStop = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.ForceStop = params.get("ForceStop")


class ResizeInstanceDisksResponse(AbstractModel):
    """ResizeInstanceDisks返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunInstancesRequest(AbstractModel):
    """RunInstances請求參數結構體

    """

    def __init__(self):
        """
        :param Placement: 實例所在的位置。通過該參數可以指定實例所屬可用區，所屬項目，所屬宿主機（在專用宿主機上創建子機時指定）等屬性。
        :type Placement: :class:`taifucloudcloud.cvm.v20170312.models.Placement`
        :param ImageId: 指定有效的[映像](https://cloud.taifucloud.com/document/product/213/4940)ID，格式形如`img-xxx`。映像類型分爲四種：<br/><li>公共映像</li><li>自定義映像</li><li>共享映像</li><li>服務市場映像</li><br/>可通過以下方式獲取可用的映像ID：<br/><li>`公共映像`、`自定義映像`、`共享映像`的映像ID可通過登入[控制台](https://console.cloud.taifucloud.com/cvm/image?rid=1&imageType=PUBLIC_IMAGE)查詢；`服務映像市場`的映像ID可通過[雲市場](https://market.cloud.taifucloud.com/list)查詢。</li><li>通過調用介面 [DescribeImages](https://cloud.taifucloud.com/document/api/213/15715) ，取返回訊息中的`ImageId`欄位。</li>
        :type ImageId: str
        :param InstanceChargeType: 實例[計費類型](https://cloud.taifucloud.com/document/product/213/2180)。<br><li>PREPAID：預付費，即包年包月<br><li>POSTPAID_BY_HOUR：按小時後付費<br><li>CDHPAID：獨享子機（基於專用宿主機創建，宿主機部分的資源不收費）<br><li>SPOTPAID：競價付費<br>預設值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月實例的購買時長、是否設置自動續約等屬性。若指定實例的付費模式爲預付費則該參數必傳。
        :type InstanceChargePrepaid: :class:`taifucloudcloud.cvm.v20170312.models.InstanceChargePrepaid`
        :param InstanceType: 實例機型。不同實例機型指定了不同的資源規格。
<br><li>對於付費模式爲PREPAID或POSTPAID\_BY\_HOUR的實例創建，具體取值可通過調用介面[DescribeInstanceTypeConfigs](https://cloud.taifucloud.com/document/api/213/15749)來獲得最新的規格表或參見[實例類型](https://cloud.taifucloud.com/document/product/213/11518)描述。若不指定該參數，則預設機型爲S1.SMALL1。<br><li>對於付費模式爲CDHPAID的實例創建，該參數以"CDH_"爲前綴，根據cpu和内存配置生成，具體形式爲：CDH_XCXG，例如對於創建cpu爲1核，内存爲1G大小的專用宿主機的實例，該參數應該爲CDH_1C1G。
        :type InstanceType: str
        :param SystemDisk: 實例系統盤配置訊息。若不指定該參數，則按照系統預設值進行分配。
        :type SystemDisk: :class:`taifucloudcloud.cvm.v20170312.models.SystemDisk`
        :param DataDisks: 實例數據盤配置訊息。若不指定該參數，則預設不購買數據盤。支援購買的時候指定11塊數據盤，其中最多包含1塊LOCAL_BASIC數據盤或者LOCAL_SSD數據盤，最多包含10塊CLOUD_BASIC數據盤、CLOUD_PREMIUM數據盤或者CLOUD_SSD數據盤。
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: 私有網絡相關訊息配置。通過該參數可以指定私有網絡的ID，子網ID等訊息。若不指定該參數，則預設使用基礎網絡。若在此參數中指定了私有網絡ip，表示每個實例的主網卡ip，而且InstanceCount參數必須與私有網絡ip的個數一緻。
        :type VirtualPrivateCloud: :class:`taifucloudcloud.cvm.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: 公網頻寬相關訊息設置。若不指定該參數，則預設公網頻寬爲0Mbps。
        :type InternetAccessible: :class:`taifucloudcloud.cvm.v20170312.models.InternetAccessible`
        :param InstanceCount: 購買實例數量。包年包月實例取值範圍：[1，300]，按量計費實例取值範圍：[1，100]。預設取值：1。指定購買實例的數量不能超過用戶所能購買的剩餘配額數量，具體配額相關限制詳見[CVM實例購買限制](https://cloud.taifucloud.com/document/product/213/2664)。
        :type InstanceCount: int
        :param InstanceName: 實例顯示名稱。<br><li>不指定實例顯示名稱則預設顯示‘未命名’。</li><li>購買多台實例，如果指定模式串`{R:x}`，表示生成數字`[x, x+n-1]`，其中`n`表示購買實例的數量，例如`server_{R:3}`，購買1台時，實例顯示名稱爲`server_3`；購買2台時，實例顯示名稱分别爲`server_3`，`server_4`。支援指定多個模式串`{R:x}`。</li><li>購買多台實例，如果不指定模式串，則在實例顯示名稱添加後綴`1、2...n`，其中`n`表示購買實例的數量，例如`server_`，購買2台時，實例顯示名稱分别爲`server_1`，`server_2`。
        :type InstanceName: str
        :param LoginSettings: 實例登入設置。通過該參數可以設置實例的登入方式密碼、金鑰或保持映像的原始登入設置。預設情況下會随機生成密碼，並以站内信方式知會到用戶。
        :type LoginSettings: :class:`taifucloudcloud.cvm.v20170312.models.LoginSettings`
        :param SecurityGroupIds: 實例所屬安全組。該參數可以通過調用 [DescribeSecurityGroups](https://cloud.taifucloud.com/document/api/215/15808) 的返回值中的sgId欄位來獲取。若不指定該參數，則綁定預設安全組。
        :type SecurityGroupIds: list of str
        :param EnhancedService: 增強服務。通過該參數可以指定是否開啓雲安全、雲監控等服務。若不指定該參數，則預設開啓雲監控、雲安全服務。
        :type EnhancedService: :class:`taifucloudcloud.cvm.v20170312.models.EnhancedService`
        :param ClientToken: 用於保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。<br>更多詳細訊息請參閱：如何保證幂等性。
        :type ClientToken: str
        :param HostName: 雲伺服器的主機名。<br><li>點號（.）和短橫線（-）不能作爲 HostName 的首尾字元，不能連續使用。<br><li>Windows 實例：名字元長度爲[2, 15]，允許字母（不限制大小寫）、數字和短橫線（-）組成，不支援點號（.），不能全是數字。<br><li>其他類型（Linux 等）實例：字元長度爲[2, 60]，允許支援多個點號，點之間爲一段，每段允許字母（不限制大小寫）、數字和短橫線（-）組成。
        :type HostName: str
        :param ActionTimer: 定時任務。通過該參數可以爲實例指定定時任務，目前僅支援定時銷毀。
        :type ActionTimer: :class:`taifucloudcloud.cvm.v20170312.models.ActionTimer`
        :param DisasterRecoverGroupIds: 置放群組id，僅支援指定一個。
        :type DisasterRecoverGroupIds: list of str
        :param TagSpecification: 標簽描述清單。通過指定該參數可以同時綁定標簽到相應的資源實例，當前僅支援綁定標簽到雲主機實例。
        :type TagSpecification: list of TagSpecification
        :param InstanceMarketOptions: 實例的市場相關選項，如競價實例相關參數，若指定實例的付費模式爲競價付費則該參數必傳。
        :type InstanceMarketOptions: :class:`taifucloudcloud.cvm.v20170312.models.InstanceMarketOptionsRequest`
        :param UserData: 提供給實例使用的用戶數據，需要以 base64 方式編碼，支援的最大數據大小爲 16KB。關於獲取此參數的詳細介紹，請參閱[Windows](https://cloud.taifucloud.com/document/product/213/17526)和[Linux](https://cloud.taifucloud.com/document/product/213/17525)啓動時運作命令。
        :type UserData: str
        """
        self.Placement = None
        self.ImageId = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceCount = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.ClientToken = None
        self.HostName = None
        self.ActionTimer = None
        self.DisasterRecoverGroupIds = None
        self.TagSpecification = None
        self.InstanceMarketOptions = None
        self.UserData = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ImageId = params.get("ImageId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceCount = params.get("InstanceCount")
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.ClientToken = params.get("ClientToken")
        self.HostName = params.get("HostName")
        if params.get("ActionTimer") is not None:
            self.ActionTimer = ActionTimer()
            self.ActionTimer._deserialize(params.get("ActionTimer"))
        self.DisasterRecoverGroupIds = params.get("DisasterRecoverGroupIds")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))
        self.UserData = params.get("UserData")


class RunInstancesResponse(AbstractModel):
    """RunInstances返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceIdSet: 當通過本介面來創建實例時會返回該參數，表示一個或多個實例`ID`。返回實例`ID`清單並不代表實例創建成功，可根據 [DescribeInstances](https://cloud.taifucloud.com/document/api/213/15728) 介面查詢返回的InstancesSet中對應實例的`ID`的狀态來判斷創建是否完成；如果實例狀态由“準備中”變爲“正在運作”，則爲創建成功。
        :type InstanceIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “雲監控” 服務相關的訊息

    """

    def __init__(self):
        """
        :param Enabled: 是否開啓[雲監控](/document/product/248)服務。取值範圍：<br><li>TRUE：表示開啓雲監控服務<br><li>FALSE：表示不開啓雲監控服務<br><br>預設取值：TRUE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “雲安全” 服務相關的訊息

    """

    def __init__(self):
        """
        :param Enabled: 是否開啓[雲安全](/document/product/296)服務。取值範圍：<br><li>TRUE：表示開啓雲安全服務<br><li>FALSE：表示不開啓雲安全服務<br><br>預設取值：TRUE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class SharePermission(AbstractModel):
    """映像分享訊息結構

    """

    def __init__(self):
        """
        :param CreatedTime: 映像分享時間
        :type CreatedTime: str
        :param AccountId: 映像分享的帳戶ID
        :type AccountId: str
        """
        self.CreatedTime = None
        self.AccountId = None


    def _deserialize(self, params):
        self.CreatedTime = params.get("CreatedTime")
        self.AccountId = params.get("AccountId")


class Snapshot(AbstractModel):
    """描述映像關聯的快照訊息

    """

    def __init__(self):
        """
        :param SnapshotId: 快照Id。
        :type SnapshotId: str
        :param DiskUsage: 創建此快照的雲硬碟類型。取值範圍：
SYSTEM_DISK：系統盤
DATA_DISK：數據盤。
        :type DiskUsage: str
        :param DiskSize: 創建此快照的雲硬碟大小，單位GB。
        :type DiskSize: int
        """
        self.SnapshotId = None
        self.DiskUsage = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskSize = params.get("DiskSize")


class SpotMarketOptions(AbstractModel):
    """競價相關選項

    """

    def __init__(self):
        """
        :param MaxPrice: 競價出價
        :type MaxPrice: str
        :param SpotInstanceType: 競價請求類型，當前僅支援類型：one-time
        :type SpotInstanceType: str
        """
        self.MaxPrice = None
        self.SpotInstanceType = None


    def _deserialize(self, params):
        self.MaxPrice = params.get("MaxPrice")
        self.SpotInstanceType = params.get("SpotInstanceType")


class StartInstancesRequest(AbstractModel):
    """StartInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲100。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class StartInstancesResponse(AbstractModel):
    """StartInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopInstancesRequest(AbstractModel):
    """StopInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲100。
        :type InstanceIds: list of str
        :param ForceStop: 是否在正常關閉失敗後選擇強制關閉實例。取值範圍：<br><li>TRUE：表示在正常關閉失敗後進行強制關閉<br><li>FALSE：表示在正常關閉失敗後不進行強制關閉<br><br>預設取值：FALSE。
        :type ForceStop: bool
        :param StopType: 實例的關閉模式。取值範圍：<br><li>SOFT_FIRST：表示在正常關閉失敗後進行強制關閉<br><li>HARD：直接強制關閉<br><li>SOFT：僅軟關機<br>預設取值：SOFT。
        :type StopType: str
        :param StoppedMode: 按量計費實例關機收費模式。
取值範圍：<br><li>KEEP_CHARGING：關機繼續收費<br><li>STOP_CHARGING：關機停止收費<br>預設取值：KEEP_CHARGING。
該參數只針對部分按量計費雲硬碟實例生效，詳情參考[按量計費實例關機不收費說明](https://cloud.taifucloud.com/document/product/213/19918)
        :type StoppedMode: str
        """
        self.InstanceIds = None
        self.ForceStop = None
        self.StopType = None
        self.StoppedMode = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ForceStop = params.get("ForceStop")
        self.StopType = params.get("StopType")
        self.StoppedMode = params.get("StoppedMode")


class StopInstancesResponse(AbstractModel):
    """StopInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StorageBlock(AbstractModel):
    """HDD的本地儲存訊息

    """

    def __init__(self):
        """
        :param Type: HDD本地儲存類型，值爲：LOCAL_PRO.
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: str
        :param MinSize: HDD本地儲存的最小容量
注意：此欄位可能返回 null，表示取不到有效值。
        :type MinSize: int
        :param MaxSize: HDD本地儲存的最大容量
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaxSize: int
        """
        self.Type = None
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")


class SyncImagesRequest(AbstractModel):
    """SyncImages請求參數結構體

    """

    def __init__(self):
        """
        :param ImageIds: 映像ID清單 ，映像ID可以通過如下方式獲取：<br><li>通過[DescribeImages](https://cloud.taifucloud.com/document/api/213/15715)介面返回的`ImageId`獲取。<br><li>通過[映像控制台](https://console.cloud.taifucloud.com/cvm/image)獲取。<br>映像ID必須滿足限制：<br><li>映像ID對應的映像狀态必須爲`NORMAL`。<br><li>映像大小小於50GB。<br>映像狀态請參考[映像數據表](/document/api/213/9452#image_state)。
        :type ImageIds: list of str
        :param DestinationRegions: 目的同步地域清單；必須滿足限制：<br><li>不能爲源地域，<br><li>必須是一個合法的Region。<br><li>暫不支援部分地域同步。<br>具體地域參數請參考[Region](https://cloud.taifucloud.com/document/product/213/6091)。
        :type DestinationRegions: list of str
        """
        self.ImageIds = None
        self.DestinationRegions = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")
        self.DestinationRegions = params.get("DestinationRegions")


class SyncImagesResponse(AbstractModel):
    """SyncImages返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """描述了作業系統所在塊設備即系統盤的訊息

    """

    def __init__(self):
        """
        :param DiskType: 系統盤類型。系統盤類型限制詳見[CVM實例配置](/document/product/213/2177)。取值範圍：<br><li>LOCAL_BASIC：本地硬碟<br><li>LOCAL_SSD：本地SSD硬碟<br><li>CLOUD_BASIC：普通雲硬碟<br><li>CLOUD_SSD：SSD雲硬碟<br><li>CLOUD_PREMIUM：高效能雲硬碟<br><br>預設取值：CLOUD_BASIC。
        :type DiskType: str
        :param DiskId: 系統盤ID。LOCAL_BASIC 和 LOCAL_SSD 類型沒有ID。暫時不支援該參數。
        :type DiskId: str
        :param DiskSize: 系統盤大小，單位：GB。預設值爲 50
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")


class Tag(AbstractModel):
    """標簽鍵值對

    """

    def __init__(self):
        """
        :param Key: 標簽鍵
        :type Key: str
        :param Value: 標簽值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class TagSpecification(AbstractModel):
    """創建資源實例時同時綁定的標簽對說明

    """

    def __init__(self):
        """
        :param ResourceType: 標簽綁定的資源類型，當前支援類型："instance"和"host"
        :type ResourceType: str
        :param Tags: 標簽對清單
        :type Tags: list of Tag
        """
        self.ResourceType = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 一個或多個待操作的實例ID。可通過[`DescribeInstances`](https://cloud.taifucloud.com/document/api/213/15728)介面返回值中的`InstanceId`獲取。每次請求批次實例的上限爲100。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VirtualPrivateCloud(AbstractModel):
    """描述了VPC相關訊息，包括子網，IP訊息等

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡ID，形如`vpc-xxx`。有效的VpcId可通過登入[控制台](https://console.cloud.taifucloud.com/vpc/vpc?rid=1)查詢；也可以調用介面 [DescribeVpcEx](/document/api/215/1372) ，從介面返回中的`unVpcId`欄位獲取。若在創建子機時VpcId與SubnetId同時傳入`DEFAULT`，則強制使用預設vpc網絡。
        :type VpcId: str
        :param SubnetId: 私有網絡子網ID，形如`subnet-xxx`。有效的私有網絡子網ID可通過登入[控制台](https://console.cloud.taifucloud.com/vpc/subnet?rid=1)查詢；也可以調用介面  [DescribeSubnets](/document/api/215/15784) ，從介面返回中的`unSubnetId`欄位獲取。若在創建子機時SubnetId與VpcId同時傳入`DEFAULT`，則強制使用預設vpc網絡。
        :type SubnetId: str
        :param AsVpcGateway: 是否用作公網閘道。公網閘道只有在實例擁有公網IP以及處於私有網絡下時才能正常使用。取值範圍：<br><li>TRUE：表示用作公網閘道<br><li>FALSE：表示不用作公網閘道<br><br>預設取值：FALSE。
        :type AsVpcGateway: bool
        :param PrivateIpAddresses: 私有網絡子網 IP 數組，在創建實例、修改實例vpc屬性操作中可使用此參數。當前僅批次創建多台實例時支援傳入相同子網的多個 IP。
        :type PrivateIpAddresses: list of str
        """
        self.VpcId = None
        self.SubnetId = None
        self.AsVpcGateway = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AsVpcGateway = params.get("AsVpcGateway")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")


class ZoneInfo(AbstractModel):
    """可用區訊息

    """

    def __init__(self):
        """
        :param Zone: 可用區名稱，例如，ap-guangzhou-3
        :type Zone: str
        :param ZoneName: 可用區描述，例如， 三區
        :type ZoneName: str
        :param ZoneId: 可用區ID
        :type ZoneId: str
        :param ZoneState: 可用區狀态，包含AVAILABLE和UNAVAILABLE。AVAILABLE代表可用，UNAVAILABLE代表不可用。
        :type ZoneState: str
        """
        self.Zone = None
        self.ZoneName = None
        self.ZoneId = None
        self.ZoneState = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.ZoneId = params.get("ZoneId")
        self.ZoneState = params.get("ZoneState")