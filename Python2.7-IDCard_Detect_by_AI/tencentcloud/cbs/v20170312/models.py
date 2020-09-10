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


class ApplySnapshotRequest(AbstractModel):
    """ApplySnapshot請求參數結構體

    """

    def __init__(self):
        """
        :param SnapshotId: 快照ID, 可通過[DescribeSnapshots](/document/product/362/15647)查詢。
        :type SnapshotId: str
        :param DiskId: 快照原雲硬碟ID，可通過[DescribeDisks](/document/product/362/16315)介面查詢。
        :type DiskId: str
        """
        self.SnapshotId = None
        self.DiskId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.DiskId = params.get("DiskId")


class ApplySnapshotResponse(AbstractModel):
    """ApplySnapshot返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachDetail(AbstractModel):
    """描述一個實例已掛載和可掛載數據盤的數量。

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID。
        :type InstanceId: str
        :param AttachedDiskCount: 實例已掛載數據盤的數量。
        :type AttachedDiskCount: int
        :param MaxAttachCount: 實例最大可掛載數據盤的數量。
        :type MaxAttachCount: int
        """
        self.InstanceId = None
        self.AttachedDiskCount = None
        self.MaxAttachCount = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AttachedDiskCount = params.get("AttachedDiskCount")
        self.MaxAttachCount = params.get("MaxAttachCount")


class AttachDisksRequest(AbstractModel):
    """AttachDisks請求參數結構體

    """

    def __init__(self):
        """
        :param DiskIds: 将要被掛載的彈性雲盤ID。通過[DescribeDisks](/document/product/362/16315)介面查詢。單次最多可掛載10塊彈性雲盤。
        :type DiskIds: list of str
        :param InstanceId: 雲伺服器實例ID。雲盤将被掛載到此雲伺服器上，通過[DescribeInstances](/document/product/213/15728)介面查詢。
        :type InstanceId: str
        :param DeleteWithInstance: 可選參數，不傳該參數則僅執行掛載操作。傳入`True`時，會在掛載成功後将雲硬碟設置爲随雲主機銷毀模式，僅對按量計費雲硬碟有效。
        :type DeleteWithInstance: bool
        """
        self.DiskIds = None
        self.InstanceId = None
        self.DeleteWithInstance = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.InstanceId = params.get("InstanceId")
        self.DeleteWithInstance = params.get("DeleteWithInstance")


class AttachDisksResponse(AbstractModel):
    """AttachDisks返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AutoSnapshotPolicy(AbstractModel):
    """描述了定期快照策略的詳細訊息

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyId: 定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param AutoSnapshotPolicyName: 定期快照策略名稱。
        :type AutoSnapshotPolicyName: str
        :param AutoSnapshotPolicyState: 定期快照策略的狀态。取值範圍：<br><li>NORMAL：正常<br><li>ISOLATED：已隔離。
        :type AutoSnapshotPolicyState: str
        :param IsActivated: 定期快照策略是否啟動。
        :type IsActivated: bool
        :param IsPermanent: 使用該定期快照策略創建出來的快照是否永久保留。
        :type IsPermanent: bool
        :param RetentionDays: 使用該定期快照策略創建出來的快照保留天數。
        :type RetentionDays: int
        :param CreateTime: 定期快照策略的創建時間。
        :type CreateTime: str
        :param NextTriggerTime: 定期快照下次觸發的時間。
        :type NextTriggerTime: str
        :param Policy: 定期快照的執行策略。
        :type Policy: list of Policy
        :param DiskIdSet: 已綁定當前定期快照策略的雲盤ID清單。
        :type DiskIdSet: list of str
        """
        self.AutoSnapshotPolicyId = None
        self.AutoSnapshotPolicyName = None
        self.AutoSnapshotPolicyState = None
        self.IsActivated = None
        self.IsPermanent = None
        self.RetentionDays = None
        self.CreateTime = None
        self.NextTriggerTime = None
        self.Policy = None
        self.DiskIdSet = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self.AutoSnapshotPolicyState = params.get("AutoSnapshotPolicyState")
        self.IsActivated = params.get("IsActivated")
        self.IsPermanent = params.get("IsPermanent")
        self.RetentionDays = params.get("RetentionDays")
        self.CreateTime = params.get("CreateTime")
        self.NextTriggerTime = params.get("NextTriggerTime")
        if params.get("Policy") is not None:
            self.Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self.Policy.append(obj)
        self.DiskIdSet = params.get("DiskIdSet")


class BindAutoSnapshotPolicyRequest(AbstractModel):
    """BindAutoSnapshotPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyId: 要綁定的定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param DiskIds: 要綁定的雲硬碟ID清單，一次請求最多綁定80塊雲盤。
        :type DiskIds: list of str
        """
        self.AutoSnapshotPolicyId = None
        self.DiskIds = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.DiskIds = params.get("DiskIds")


class BindAutoSnapshotPolicyResponse(AbstractModel):
    """BindAutoSnapshotPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAutoSnapshotPolicyRequest(AbstractModel):
    """CreateAutoSnapshotPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param Policy: 定期快照的執行策略。
        :type Policy: list of Policy
        :param AutoSnapshotPolicyName: 要創建的定期快照策略名。不傳則預設爲“未命名”。最大長度不能超60個位元。
        :type AutoSnapshotPolicyName: str
        :param IsActivated: 是否啟動定期快照策略，FALSE表示未啟動，TRUE表示啟動，預設爲TRUE。
        :type IsActivated: bool
        :param IsPermanent: 通過該定期快照策略創建的快照是否永久保留。FALSE表示非永久保留，TRUE表示永久保留，預設爲FALSE。
        :type IsPermanent: bool
        :param RetentionDays: 通過該定期快照策略創建的快照保留天數，預設保留7天。如果指定本參數，則IsPermanent入參不可指定爲TRUE，否則會産生沖突。
        :type RetentionDays: int
        :param DryRun: 是否創建定期快照的執行策略。TRUE表示只需獲取首次開始備份的時間，不實際創建定期快照策略，FALSE表示創建，預設爲FALSE。
        :type DryRun: bool
        """
        self.Policy = None
        self.AutoSnapshotPolicyName = None
        self.IsActivated = None
        self.IsPermanent = None
        self.RetentionDays = None
        self.DryRun = None


    def _deserialize(self, params):
        if params.get("Policy") is not None:
            self.Policy = []
            for item in params.get("Policy"):
                obj = Policy()
                obj._deserialize(item)
                self.Policy.append(obj)
        self.AutoSnapshotPolicyName = params.get("AutoSnapshotPolicyName")
        self.IsActivated = params.get("IsActivated")
        self.IsPermanent = params.get("IsPermanent")
        self.RetentionDays = params.get("RetentionDays")
        self.DryRun = params.get("DryRun")


class CreateAutoSnapshotPolicyResponse(AbstractModel):
    """CreateAutoSnapshotPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyId: 新創建的定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        :param NextTriggerTime: 首次開始備份的時間。
        :type NextTriggerTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AutoSnapshotPolicyId = None
        self.NextTriggerTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")
        self.NextTriggerTime = params.get("NextTriggerTime")
        self.RequestId = params.get("RequestId")


class CreateDisksRequest(AbstractModel):
    """CreateDisks請求參數結構體

    """

    def __init__(self):
        """
        :param DiskType: 硬碟媒體類型。取值範圍：<br><li>CLOUD_BASIC：表示普通雲硬碟<br><li>CLOUD_PREMIUM：表示高效能雲硬碟<br><li>CLOUD_SSD：表示SSD雲硬碟。
        :type DiskType: str
        :param DiskChargeType: 雲硬碟計費類型。<br><li>PREPAID：預付費，即包年包月<br><li>POSTPAID_BY_HOUR：按小時後付費<br><li>CDCPAID：獨享集群付費<br>各類型價格請參考雲硬碟[價格總覽](/document/product/362/2413)。
        :type DiskChargeType: str
        :param Placement: 實例所在的位置。通過該參數可以指定實例所屬可用區，所屬項目。若不指定項目，将在預設項目下進行創建。
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param DiskName: 雲盤顯示名稱。不傳則預設爲“未命名”。最大長度不能超60個位元。
        :type DiskName: str
        :param DiskCount: 創建雲硬碟數量，不傳則預設爲1。單次請求最多可創建的雲盤數有限制，具體參見[雲硬碟使用限制](https://cloud.tencent.com/doc/product/362/5145)。
        :type DiskCount: int
        :param DiskChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數指定包年包月雲盤的購買時長、是否設置自動續約等屬性。<br>創建預付費雲盤該參數必傳，創建按小時後付費雲盤無需傳該參數。
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param DiskSize: 雲硬碟大小，單位爲GB。<br><li>如果傳入`SnapshotId`則可不傳`DiskSize`，此時新建雲盤的大小爲快照大小<br><li>如果傳入`SnapshotId`同時傳入`DiskSize`，則雲盤大小必須大于或等于快照大小<br><li>雲盤大小取值範圍參見雲硬碟[産品分類](/document/product/362/2353)的說明。
        :type DiskSize: int
        :param SnapshotId: 快照ID，如果傳入則根據此快照創建雲硬碟，快照類型必須爲數據盤快照，可通過[DescribeSnapshots](/document/product/362/15647)介面查詢快照，見輸出參數DiskUsage解釋。
        :type SnapshotId: str
        :param ClientToken: 用于保證請求幂等性的字串。該字串由客戶生成，需保證不同請求之間唯一，最大值不超過64個ASCII字元。若不指定該參數，則無法保證請求的幂等性。
        :type ClientToken: str
        :param Encrypt: 傳入該參數用于創建加密雲盤，取值固定爲ENCRYPT。
        :type Encrypt: str
        :param Tags: 雲盤綁定的标簽。
        :type Tags: list of Tag
        :param Shareable: 可選參數，預設爲False。傳入True時，雲盤将創建爲共享型雲盤。
        :type Shareable: bool
        """
        self.DiskType = None
        self.DiskChargeType = None
        self.Placement = None
        self.DiskName = None
        self.DiskCount = None
        self.DiskChargePrepaid = None
        self.DiskSize = None
        self.SnapshotId = None
        self.ClientToken = None
        self.Encrypt = None
        self.Tags = None
        self.Shareable = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskChargeType = params.get("DiskChargeType")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.DiskName = params.get("DiskName")
        self.DiskCount = params.get("DiskCount")
        if params.get("DiskChargePrepaid") is not None:
            self.DiskChargePrepaid = DiskChargePrepaid()
            self.DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self.DiskSize = params.get("DiskSize")
        self.SnapshotId = params.get("SnapshotId")
        self.ClientToken = params.get("ClientToken")
        self.Encrypt = params.get("Encrypt")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Shareable = params.get("Shareable")


class CreateDisksResponse(AbstractModel):
    """CreateDisks返回參數結構體

    """

    def __init__(self):
        """
        :param DiskIdSet: 創建的雲硬碟ID清單。
        :type DiskIdSet: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DiskIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DiskIdSet = params.get("DiskIdSet")
        self.RequestId = params.get("RequestId")


class CreateSnapshotRequest(AbstractModel):
    """CreateSnapshot請求參數結構體

    """

    def __init__(self):
        """
        :param DiskId: 需要創建快照的雲硬碟ID，可通過[DescribeDisks](/document/product/362/16315)介面查詢。
        :type DiskId: str
        :param SnapshotName: 快照名稱，不傳則新快照名稱預設爲“未命名”。
        :type SnapshotName: str
        """
        self.DiskId = None
        self.SnapshotName = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.SnapshotName = params.get("SnapshotName")


class CreateSnapshotResponse(AbstractModel):
    """CreateSnapshot返回參數結構體

    """

    def __init__(self):
        """
        :param SnapshotId: 新創建的快照ID。
        :type SnapshotId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.RequestId = params.get("RequestId")


class DeleteAutoSnapshotPoliciesRequest(AbstractModel):
    """DeleteAutoSnapshotPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyIds: 要删除的定期快照策略ID清單。
        :type AutoSnapshotPolicyIds: list of str
        """
        self.AutoSnapshotPolicyIds = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")


class DeleteAutoSnapshotPoliciesResponse(AbstractModel):
    """DeleteAutoSnapshotPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots請求參數結構體

    """

    def __init__(self):
        """
        :param SnapshotIds: 要删除的快照ID清單，可通過[DescribeSnapshots](/document/product/362/15647)查詢。
        :type SnapshotIds: list of str
        """
        self.SnapshotIds = None


    def _deserialize(self, params):
        self.SnapshotIds = params.get("SnapshotIds")


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAutoSnapshotPoliciesRequest(AbstractModel):
    """DescribeAutoSnapshotPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param AutoSnapshotPolicyIds: 要查詢的定期快照策略ID清單。參數不支援同時指定`AutoSnapshotPolicyIds`和`Filters`。
        :type AutoSnapshotPolicyIds: list of str
        :param Filters: 過濾條件。參數不支援同時指定`AutoSnapshotPolicyIds`和`Filters`。<br><li>auto-snapshot-policy-id - Array of String - 是否必填：否 -（過濾條件）按定期快照策略ID進行過濾。定期快照策略ID形如：`asp-11112222`。<br><li>auto-snapshot-policy-state - Array of String - 是否必填：否 -（過濾條件）按定期快照策略的狀态進行過濾。定期快照策略ID形如：`asp-11112222`。(NORMAL：正常 | ISOLATED：已隔離。)<br><li>auto-snapshot-policy-name - Array of String - 是否必填：否 -（過濾條件）按定期快照策略名稱進行過濾。
        :type Filters: list of Filter
        :param Limit: 返回數量，預設爲20，最大值爲100。關于`Limit`的更進一步介紹請參考 API [簡介](/document/362/13158)中的相關小節。
        :type Limit: int
        :param Offset: 偏移量，預設爲0。關于`Offset`的更進一步介紹請參考API[簡介](/document/362/13158)中的相關小節。
        :type Offset: int
        :param Order: 輸出定期快照清單的排列順序。取值範圍：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        :param OrderField: 定期快照清單排序的依據欄位。取值範圍：<br><li>CREATETIME：依據定期快照的創建時間排序<br>預設按創建時間排序。
        :type OrderField: str
        """
        self.AutoSnapshotPolicyIds = None
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        self.AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeAutoSnapshotPoliciesResponse(AbstractModel):
    """DescribeAutoSnapshotPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 有效的定期快照策略數量。
        :type TotalCount: int
        :param AutoSnapshotPolicySet: 定期快照策略清單。
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AutoSnapshotPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicySet") is not None:
            self.AutoSnapshotPolicySet = []
            for item in params.get("AutoSnapshotPolicySet"):
                obj = AutoSnapshotPolicy()
                obj._deserialize(item)
                self.AutoSnapshotPolicySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskAssociatedAutoSnapshotPolicyRequest(AbstractModel):
    """DescribeDiskAssociatedAutoSnapshotPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param DiskId: 要查詢的雲硬碟ID。
        :type DiskId: str
        """
        self.DiskId = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")


class DescribeDiskAssociatedAutoSnapshotPolicyResponse(AbstractModel):
    """DescribeDiskAssociatedAutoSnapshotPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 雲盤綁定的定期快照數量。
        :type TotalCount: int
        :param AutoSnapshotPolicySet: 雲盤綁定的定期快照清單。
        :type AutoSnapshotPolicySet: list of AutoSnapshotPolicy
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AutoSnapshotPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AutoSnapshotPolicySet") is not None:
            self.AutoSnapshotPolicySet = []
            for item in params.get("AutoSnapshotPolicySet"):
                obj = AutoSnapshotPolicy()
                obj._deserialize(item)
                self.AutoSnapshotPolicySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskConfigQuotaRequest(AbstractModel):
    """DescribeDiskConfigQuota請求參數結構體

    """

    def __init__(self):
        """
        :param InquiryType: 查詢類别，取值範圍。<br><li>INQUIRY_CBS_CONFIG：查詢雲盤配置清單<br><li>INQUIRY_CVM_CONFIG：查詢雲盤與實例搭配的配置清單。
        :type InquiryType: str
        :param Zones: 查詢一個或多個[可用區](/document/product/213/15753#ZoneInfo)下的配置。
        :type Zones: list of str
        :param DiskChargeType: 付費模式。取值範圍：<br><li>PREPAID：預付費<br><li>POSTPAID_BY_HOUR：後付費。
        :type DiskChargeType: str
        :param DiskTypes: 硬碟媒體類型。取值範圍：<br><li>CLOUD_BASIC：表示普通雲硬碟<br><li>CLOUD_PREMIUM：表示高效能雲硬碟<br><li>CLOUD_SSD：表示SSD雲硬碟。
        :type DiskTypes: list of str
        :param DiskUsage: 系統盤或數據盤。取值範圍：<br><li>SYSTEM_DISK：表示系統盤<br><li>DATA_DISK：表示數據盤。
        :type DiskUsage: str
        :param InstanceFamilies: 按照實例機型系列過濾。實例機型系列形如：S1、I1、M1等。詳見[實例類型](https://cloud.tencent.com/document/product/213/11518)
        :type InstanceFamilies: list of str
        :param CPU: 實例CPU核數。
        :type CPU: int
        :param Memory: 實例内存大小。
        :type Memory: int
        """
        self.InquiryType = None
        self.Zones = None
        self.DiskChargeType = None
        self.DiskTypes = None
        self.DiskUsage = None
        self.InstanceFamilies = None
        self.CPU = None
        self.Memory = None


    def _deserialize(self, params):
        self.InquiryType = params.get("InquiryType")
        self.Zones = params.get("Zones")
        self.DiskChargeType = params.get("DiskChargeType")
        self.DiskTypes = params.get("DiskTypes")
        self.DiskUsage = params.get("DiskUsage")
        self.InstanceFamilies = params.get("InstanceFamilies")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")


class DescribeDiskConfigQuotaResponse(AbstractModel):
    """DescribeDiskConfigQuota返回參數結構體

    """

    def __init__(self):
        """
        :param DiskConfigSet: 雲盤配置清單。
        :type DiskConfigSet: list of DiskConfig
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DiskConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskConfigSet") is not None:
            self.DiskConfigSet = []
            for item in params.get("DiskConfigSet"):
                obj = DiskConfig()
                obj._deserialize(item)
                self.DiskConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDiskOperationLogsRequest(AbstractModel):
    """DescribeDiskOperationLogs請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。支援以下條件：
<li>disk-id - Array of String - 是否必填：是 - 按雲盤ID過濾，每個請求最多可指定10個雲盤ID。
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


class DescribeDiskOperationLogsResponse(AbstractModel):
    """DescribeDiskOperationLogs返回參數結構體

    """

    def __init__(self):
        """
        :param DiskOperationLogSet: 雲盤的操作日志清單。
        :type DiskOperationLogSet: list of DiskOperationLog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DiskOperationLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskOperationLogSet") is not None:
            self.DiskOperationLogSet = []
            for item in params.get("DiskOperationLogSet"):
                obj = DiskOperationLog()
                obj._deserialize(item)
                self.DiskOperationLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    """DescribeDisks請求參數結構體

    """

    def __init__(self):
        """
        :param DiskIds: 按照一個或者多個雲硬碟ID查詢。雲硬碟ID形如：`disk-11112222`，此參數的具體格式可參考API[簡介](/document/product/362/15633)的ids.N一節）。參數不支援同時指定`DiskIds`和`Filters`。
        :type DiskIds: list of str
        :param Filters: 過濾條件。參數不支援同時指定`DiskIds`和`Filters`。<br><li>disk-usage - Array of String - 是否必填：否 -（過濾條件）按雲盤類型過濾。 (SYSTEM_DISK：表示系統盤 | DATA_DISK：表示數據盤)<br><li>disk-charge-type - Array of String - 是否必填：否 -（過濾條件）按照雲硬碟計費模式過濾。 (PREPAID：表示預付費，即包年包月 | POSTPAID_BY_HOUR：表示後付費，即按量計費。)<br><li>portable - Array of String - 是否必填：否 -（過濾條件）按是否爲彈性雲盤過濾。 (TRUE：表示彈性雲盤 | FALSE：表示非彈性雲盤。)<br><li>project-id - Array of Integer - 是否必填：否 -（過濾條件）按雲硬碟所屬項目ID過濾。<br><li>disk-id - Array of String - 是否必填：否 -（過濾條件）按照雲硬碟ID過濾。雲盤ID形如：`disk-11112222`。<br><li>disk-name - Array of String - 是否必填：否 -（過濾條件）按照雲盤名稱過濾。<br><li>disk-type - Array of String - 是否必填：否 -（過濾條件）按照雲盤媒體類型過濾。(CLOUD_BASIC：表示普通雲硬碟 | CLOUD_PREMIUM：表示高效能雲硬碟。| CLOUD_SSD：SSD表示SSD雲硬碟。)<br><li>disk-state - Array of String - 是否必填：否 -（過濾條件）按照雲盤狀态過濾。(UNATTACHED：未掛載 | ATTACHING：掛載中 | ATTACHED：已掛載 | DETACHING：解挂中 | EXPANDING：擴容中 | ROLLBACKING：回滾中 | TORECYCLE：待回收。)<br><li>instance-id - Array of String - 是否必填：否 -（過濾條件）按照雲盤掛載的雲主機實例ID過濾。可根據此參數查詢掛載在指定雲主機下的雲硬碟。<br><li>zone - Array of String - 是否必填：否 -（過濾條件）按照[可用區](/document/product/213/15753#ZoneInfo)過濾。<br><li>instance-ip-address - Array of String - 是否必填：否 -（過濾條件）按雲盤所掛載雲主機的内網或外網IP過濾。<br><li>instance-name - Array of String - 是否必填：否 -（過濾條件）按雲盤所掛載的實例名稱過濾。<br><li>tag-key - Array of String - 是否必填：否 -（過濾條件）按照标簽鍵進行過濾。<br><li>tag-value - Array of String - 是否必填：否 -（過濾條件）照标簽值進行過濾。<br><li>tag:tag-key - Array of String - 是否必填：否 -（過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于`Offset`的更進一步介紹請參考API[簡介](/document/product/362/15633)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關于`Limit`的更進一步介紹請參考 API [簡介](/document/product/362/15633)中的相關小節。
        :type Limit: int
        :param Order: 輸出雲盤清單的排列順序。取值範圍：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        :param OrderField: 雲盤清單排序的依據欄位。取值範圍：<br><li>CREATE_TIME：依據雲盤的創建時間排序<br><li>DEADLINE：依據雲盤的到期時間排序<br>預設按雲盤創建時間排序。
        :type OrderField: str
        :param ReturnBindAutoSnapshotPolicy: 雲盤詳情中是否需要返回雲盤綁定的定期快照策略ID，TRUE表示需要返回，FALSE表示不返回。
        :type ReturnBindAutoSnapshotPolicy: bool
        """
        self.DiskIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None
        self.ReturnBindAutoSnapshotPolicy = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        self.ReturnBindAutoSnapshotPolicy = params.get("ReturnBindAutoSnapshotPolicy")


class DescribeDisksResponse(AbstractModel):
    """DescribeDisks返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的雲硬碟數量。
        :type TotalCount: int
        :param DiskSet: 雲硬碟的詳細訊息清單。
        :type DiskSet: list of Disk
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DiskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DiskSet") is not None:
            self.DiskSet = []
            for item in params.get("DiskSet"):
                obj = Disk()
                obj._deserialize(item)
                self.DiskSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesDiskNumRequest(AbstractModel):
    """DescribeInstancesDiskNum請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 雲伺服器實例ID，通過[DescribeInstances](/document/product/213/15728)介面查詢。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeInstancesDiskNumResponse(AbstractModel):
    """DescribeInstancesDiskNum返回參數結構體

    """

    def __init__(self):
        """
        :param AttachDetail: 各個雲伺服器已掛載和可掛載彈性雲盤的數量。
        :type AttachDetail: list of AttachDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AttachDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AttachDetail") is not None:
            self.AttachDetail = []
            for item in params.get("AttachDetail"):
                obj = AttachDetail()
                obj._deserialize(item)
                self.AttachDetail.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotOperationLogsRequest(AbstractModel):
    """DescribeSnapshotOperationLogs請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 過濾條件。支援以下條件：
<li>snapshot-id - Array of String - 是否必填：是 - 按快照ID過濾，每個請求最多可指定10個快照ID。
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


class DescribeSnapshotOperationLogsResponse(AbstractModel):
    """DescribeSnapshotOperationLogs返回參數結構體

    """

    def __init__(self):
        """
        :param SnapshotOperationLogSet: 快照操作日志清單。
        :type SnapshotOperationLogSet: list of SnapshotOperationLog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SnapshotOperationLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SnapshotOperationLogSet") is not None:
            self.SnapshotOperationLogSet = []
            for item in params.get("SnapshotOperationLogSet"):
                obj = SnapshotOperationLog()
                obj._deserialize(item)
                self.SnapshotOperationLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots請求參數結構體

    """

    def __init__(self):
        """
        :param SnapshotIds: 要查詢快照的ID清單。參數不支援同時指定`SnapshotIds`和`Filters`。
        :type SnapshotIds: list of str
        :param Filters: 過濾條件。參數不支援同時指定`SnapshotIds`和`Filters`。<br><li>snapshot-id - Array of String - 是否必填：否 -（過濾條件）按照快照的ID過濾。快照ID形如：`snap-11112222`。<br><li>snapshot-name - Array of String - 是否必填：否 -（過濾條件）按照快照名稱過濾。<br><li>snapshot-state - Array of String - 是否必填：否 -（過濾條件）按照快照狀态過濾。 (NORMAL：正常 | CREATING：創建中 | ROLLBACKING：回滾中。)<br><li>disk-usage - Array of String - 是否必填：否 -（過濾條件）按創建快照的雲盤類型過濾。 (SYSTEM_DISK：代表系統盤 | DATA_DISK：代表數據盤。)<br><li>project-id  - Array of String - 是否必填：否 -（過濾條件）按雲硬碟所屬項目ID過濾。<br><li>disk-id  - Array of String - 是否必填：否 -（過濾條件）按照創建快照的雲硬碟ID過濾。<br><li>zone - Array of String - 是否必填：否 -（過濾條件）按照[可用區](/document/product/213/15753#ZoneInfo)過濾。<br><li>encrypt - Array of String - 是否必填：否 -（過濾條件）按是否加密盤快照過濾。 (TRUE：表示加密盤快照 | FALSE：表示非加密盤快照。)
        :type Filters: list of Filter
        :param Offset: 偏移量，預設爲0。關于`Offset`的更進一步介紹請參考API[簡介](/document/product/362/15633)中的相關小節。
        :type Offset: int
        :param Limit: 返回數量，預設爲20，最大值爲100。關于`Limit`的更進一步介紹請參考 API [簡介](/document/product/362/15633)中的相關小節。
        :type Limit: int
        :param Order: 輸出雲盤清單的排列順序。取值範圍：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        :param OrderField: 快照清單排序的依據欄位。取值範圍：<br><li>CREATE_TIME：依據快照的創建時間排序<br>預設按創建時間排序。
        :type OrderField: str
        """
        self.SnapshotIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        self.SnapshotIds = params.get("SnapshotIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 快照的數量。
        :type TotalCount: int
        :param SnapshotSet: 快照的詳情清單。
        :type SnapshotSet: list of Snapshot
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SnapshotSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SnapshotSet") is not None:
            self.SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self.SnapshotSet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachDisksRequest(AbstractModel):
    """DetachDisks請求參數結構體

    """

    def __init__(self):
        """
        :param DiskIds: 将要解挂的雲硬碟ID， 通過[DescribeDisks](/document/product/362/16315)介面查詢，單次請求最多可解挂10塊彈性雲盤。
        :type DiskIds: list of str
        :param InstanceId: 對于非共享型雲盤，會忽略該參數；對于共享型雲盤，該參數表示要從哪個CVM實例上解挂雲盤。
        :type InstanceId: str
        """
        self.DiskIds = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.InstanceId = params.get("InstanceId")


class DetachDisksResponse(AbstractModel):
    """DetachDisks返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Disk(AbstractModel):
    """描述了雲硬碟的詳細訊息

    """

    def __init__(self):
        """
        :param DiskId: 雲硬碟ID。
        :type DiskId: str
        :param DiskUsage: 雲硬碟類型。取值範圍：<br><li>SYSTEM_DISK：系統盤<br><li>DATA_DISK：數據盤。
        :type DiskUsage: str
        :param DiskChargeType: 付費模式。取值範圍：<br><li>PREPAID：預付費，即包年包月<br><li>POSTPAID_BY_HOUR：後付費，即按量計費。
        :type DiskChargeType: str
        :param Portable: 是否爲彈性雲盤，false表示非彈性雲盤，true表示彈性雲盤。
        :type Portable: bool
        :param Placement: 雲硬碟所在的位置。
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param SnapshotAbility: 雲盤是否具備創建快照的能力。取值範圍：<br><li>false表示不具備<br><li>true表示具備。
        :type SnapshotAbility: bool
        :param DiskName: 雲硬碟名稱。
        :type DiskName: str
        :param DiskSize: 雲硬碟大小，單位GB。
        :type DiskSize: int
        :param DiskState: 雲盤狀态。取值範圍：<br><li>UNATTACHED：未掛載<br><li>ATTACHING：掛載中<br><li>ATTACHED：已掛載<br><li>DETACHING：解挂中<br><li>EXPANDING：擴容中<br><li>ROLLBACKING：回滾中<br><li>TORECYCLE：待回收<br><li>DUMPING：拷貝硬碟中。
        :type DiskState: str
        :param DiskType: 雲盤媒體類型。取值範圍：<br><li>CLOUD_BASIC：表示普通雲硬碟<br><li>CLOUD_PREMIUM：表示高效能雲硬碟<br><li>CLOUD_SSD：SSD表示SSD雲硬碟。
        :type DiskType: str
        :param Attached: 雲盤是否掛載到雲主機上。取值範圍：<br><li>false:表示未掛載<br><li>true:表示已掛載。
        :type Attached: bool
        :param InstanceId: 雲硬碟掛載的雲主機ID。
        :type InstanceId: str
        :param CreateTime: 雲硬碟的創建時間。
        :type CreateTime: str
        :param DeadlineTime: 雲硬碟的到期時間。
        :type DeadlineTime: str
        :param Rollbacking: 雲盤是否處于快照回滾狀态。取值範圍：<br><li>false:表示不處于快照回滾狀态<br><li>true:表示處于快照回滾狀态。
        :type Rollbacking: bool
        :param RollbackPercent: 雲盤快照回滾的進度。
        :type RollbackPercent: int
        :param Encrypt: 雲盤是否爲加密盤。取值範圍：<br><li>false:表示非加密盤<br><li>true:表示加密盤。
        :type Encrypt: bool
        :param AutoRenewFlagError: 雲盤已掛載到子機，且子機與雲盤都是包年包月。<br><li>true：子機設置了自動續約标識，但雲盤未設置<br><li>false：雲盤自動續約标識正常。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AutoRenewFlagError: bool
        :param RenewFlag: 自動續約标識。取值範圍：<br><li>NOTIFY_AND_AUTO_RENEW：通知過期且自動續約<br><li>NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        :param DeadlineError: 在雲盤已掛載到實例，且實例與雲盤都是包年包月的條件下，此欄位才有意義。<br><li>true:雲盤到期時間早于實例。<br><li>false：雲盤到期時間晚于實例。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeadlineError: bool
        :param IsReturnable: 判斷預付費的雲盤是否支援主動退還。<br><li>true:支援主動退還<br><li>false:不支援主動退還。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsReturnable: bool
        :param ReturnFailCode: 預付費雲盤在不支援主動退還的情況下，該參數表明不支援主動退還的具體原因。取值範圍：<br><li>1：雲硬碟已經退還<br><li>2：雲硬碟已過期<br><li>3：雲盤不支援退還<br><li>8：超過可退還數量的限制。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReturnFailCode: int
        :param AutoSnapshotPolicyIds: 雲盤關聯的定期快照ID。只有在調用DescribeDisks介面時，入參ReturnBindAutoSnapshotPolicy取值爲TRUE才會返回該參數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AutoSnapshotPolicyIds: list of str
        :param Tags: 與雲盤綁定的标簽，雲盤未綁定标簽則取值爲空。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param DeleteWithInstance: 雲盤是否與掛載的實例一起銷毀。<br><li>true:銷毀實例時會同時銷毀雲盤，只支援按小時後付費雲盤。<br><li>false：銷毀實例時不銷毀雲盤。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param DifferDaysOfDeadline: 當前時間距離盤到期的天數（僅對預付費盤有意義）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DifferDaysOfDeadline: int
        :param Migrating: 雲盤是否處于類型變更中。取值範圍：<br><li>false:表示雲盤不處于類型變更中<br><li>true:表示雲盤已發起類型變更，正處于遷移中。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Migrating: bool
        :param MigratePercent: 雲盤類型變更的遷移進度，取值0到100。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MigratePercent: int
        :param Shareable: 雲盤是否爲共享型雲盤。
        :type Shareable: bool
        :param InstanceIdList: 對于非共享型雲盤，該參數爲空數組。對于共享型雲盤，則表示該雲盤當前被掛載到的CVM實例InstanceId
        :type InstanceIdList: list of str
        """
        self.DiskId = None
        self.DiskUsage = None
        self.DiskChargeType = None
        self.Portable = None
        self.Placement = None
        self.SnapshotAbility = None
        self.DiskName = None
        self.DiskSize = None
        self.DiskState = None
        self.DiskType = None
        self.Attached = None
        self.InstanceId = None
        self.CreateTime = None
        self.DeadlineTime = None
        self.Rollbacking = None
        self.RollbackPercent = None
        self.Encrypt = None
        self.AutoRenewFlagError = None
        self.RenewFlag = None
        self.DeadlineError = None
        self.IsReturnable = None
        self.ReturnFailCode = None
        self.AutoSnapshotPolicyIds = None
        self.Tags = None
        self.DeleteWithInstance = None
        self.DifferDaysOfDeadline = None
        self.Migrating = None
        self.MigratePercent = None
        self.Shareable = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskChargeType = params.get("DiskChargeType")
        self.Portable = params.get("Portable")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.SnapshotAbility = params.get("SnapshotAbility")
        self.DiskName = params.get("DiskName")
        self.DiskSize = params.get("DiskSize")
        self.DiskState = params.get("DiskState")
        self.DiskType = params.get("DiskType")
        self.Attached = params.get("Attached")
        self.InstanceId = params.get("InstanceId")
        self.CreateTime = params.get("CreateTime")
        self.DeadlineTime = params.get("DeadlineTime")
        self.Rollbacking = params.get("Rollbacking")
        self.RollbackPercent = params.get("RollbackPercent")
        self.Encrypt = params.get("Encrypt")
        self.AutoRenewFlagError = params.get("AutoRenewFlagError")
        self.RenewFlag = params.get("RenewFlag")
        self.DeadlineError = params.get("DeadlineError")
        self.IsReturnable = params.get("IsReturnable")
        self.ReturnFailCode = params.get("ReturnFailCode")
        self.AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.DifferDaysOfDeadline = params.get("DifferDaysOfDeadline")
        self.Migrating = params.get("Migrating")
        self.MigratePercent = params.get("MigratePercent")
        self.Shareable = params.get("Shareable")
        self.InstanceIdList = params.get("InstanceIdList")


class DiskChargePrepaid(AbstractModel):
    """描述了實例的計費模式

    """

    def __init__(self):
        """
        :param Period: 購買雲盤的時長，預設單位爲月，取值範圍：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自動續約标識。取值範圍：<br><li>NOTIFY_AND_AUTO_RENEW：通知過期且自動續約<br><li>NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約<br><br>預設取值：NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約。
        :type RenewFlag: str
        :param CurInstanceDeadline: 需要将雲盤的到期時間與掛載的子機對齊時，可傳入該參數。該參數表示子機當前的到期時間，此時Period如果傳入，則表示子機需要續約的時長，雲盤會自動按對齊到子機續約後的到期時間續約，範例取值：2018-03-30 20:15:03。
        :type CurInstanceDeadline: str
        """
        self.Period = None
        self.RenewFlag = None
        self.CurInstanceDeadline = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        self.CurInstanceDeadline = params.get("CurInstanceDeadline")


class DiskConfig(AbstractModel):
    """雲盤配置。

    """

    def __init__(self):
        """
        :param Available: 配置是否可用。
        :type Available: bool
        :param DiskType: 雲盤媒體類型。取值範圍：<br><li>CLOUD_BASIC：表示普通雲硬碟<br><li>CLOUD_PREMIUM：表示高效能雲硬碟<br><li>CLOUD_SSD：SSD表示SSD雲硬碟。
        :type DiskType: str
        :param DiskUsage: 雲盤類型。取值範圍：<br><li>SYSTEM_DISK：表示系統盤<br><li>DATA_DISK：表示數據盤。
        :type DiskUsage: str
        :param DiskChargeType: 付費模式。取值範圍：<br><li>PREPAID：表示預付費，即包年包月<br><li>POSTPAID_BY_HOUR：表示後付費，即按量計費。
        :type DiskChargeType: str
        :param MaxDiskSize: 最大可配置雲盤大小，單位GB。
        :type MaxDiskSize: int
        :param MinDiskSize: 最小可配置雲盤大小，單位GB。
        :type MinDiskSize: int
        :param Zone: 所在[可用區](/document/api/213/9452#zone)。
        :type Zone: str
        :param DeviceClass: 實例機型。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeviceClass: str
        :param InstanceFamily: 實例機型系列。詳見[實例類型](https://cloud.tencent.com/document/product/213/11518)
注意：此欄位可能返回 null，表示取不到有效值。
        :type InstanceFamily: str
        """
        self.Available = None
        self.DiskType = None
        self.DiskUsage = None
        self.DiskChargeType = None
        self.MaxDiskSize = None
        self.MinDiskSize = None
        self.Zone = None
        self.DeviceClass = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.Available = params.get("Available")
        self.DiskType = params.get("DiskType")
        self.DiskUsage = params.get("DiskUsage")
        self.DiskChargeType = params.get("DiskChargeType")
        self.MaxDiskSize = params.get("MaxDiskSize")
        self.MinDiskSize = params.get("MinDiskSize")
        self.Zone = params.get("Zone")
        self.DeviceClass = params.get("DeviceClass")
        self.InstanceFamily = params.get("InstanceFamily")


class DiskOperationLog(AbstractModel):
    """雲盤操作日志。

    """

    def __init__(self):
        """
        :param Operator: 操作者的UIN。
        :type Operator: str
        :param Operation: 操作類型。取值範圍：
CBS_OPERATION_ATTACH：掛載雲硬碟
CBS_OPERATION_DETACH：解挂雲硬碟
CBS_OPERATION_RENEW：續約
CBS_OPERATION_EXPAND：擴容
CBS_OPERATION_CREATE：創建
CBS_OPERATION_ISOLATE：隔離
CBS_OPERATION_MODIFY：修改雲硬碟屬性
ASP_OPERATION_BIND：關聯定期快照策略
ASP_OPERATION_UNBIND：取消關聯定期快照策略
        :type Operation: str
        :param DiskId: 操作的雲盤ID。
        :type DiskId: str
        :param OperationState: 操作的狀态。取值範圍：
SUCCESS :表示操作成功 
FAILED :表示操作失敗 
PROCESSING :表示操作中。
        :type OperationState: str
        :param StartTime: 開始時間。
        :type StartTime: str
        :param EndTime: 結束時間。
        :type EndTime: str
        """
        self.Operator = None
        self.Operation = None
        self.DiskId = None
        self.OperationState = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Operation = params.get("Operation")
        self.DiskId = params.get("DiskId")
        self.OperationState = params.get("OperationState")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class Filter(AbstractModel):
    """描述鍵值對過濾器，用于條件過濾查詢。

    """

    def __init__(self):
        """
        :param Name: 過濾鍵的名稱。
        :type Name: str
        :param Values: 一個或者多個過濾值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Image(AbstractModel):
    """映像。

    """

    def __init__(self):
        """
        :param ImageId: 映像實例ID。
        :type ImageId: str
        :param ImageName: 映像名稱。
        :type ImageName: str
        """
        self.ImageId = None
        self.ImageName = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")


class InquiryPriceCreateDisksRequest(AbstractModel):
    """InquiryPriceCreateDisks請求參數結構體

    """

    def __init__(self):
        """
        :param DiskType: 雲硬碟類型。取值範圍：<br><li>普通雲硬碟：CLOUD_BASIC<br><li>高效能雲硬碟：CLOUD_PREMIUM<br><li>SSD雲硬碟：CLOUD_SSD。
        :type DiskType: str
        :param DiskSize: 雲硬碟大小，單位爲GB。雲盤大小取值範圍參見雲硬碟[産品分類](/document/product/362/2353)的說明。
        :type DiskSize: int
        :param DiskChargeType: 雲硬碟計費類型。<br><li>PREPAID：預付費，即包年包月<br><li>POSTPAID_BY_HOUR：按小時後付費
        :type DiskChargeType: str
        :param DiskChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數指定包年包月雲盤的購買時長、是否設置自動續約等屬性。<br>創建預付費雲盤該參數必傳，創建按小時後付費雲盤無需傳該參數。
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param DiskCount: 購買雲盤的數量。不填則預設爲1。
        :type DiskCount: int
        :param ProjectId: 雲盤所屬項目ID。
        :type ProjectId: int
        """
        self.DiskType = None
        self.DiskSize = None
        self.DiskChargeType = None
        self.DiskChargePrepaid = None
        self.DiskCount = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        self.DiskChargeType = params.get("DiskChargeType")
        if params.get("DiskChargePrepaid") is not None:
            self.DiskChargePrepaid = DiskChargePrepaid()
            self.DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self.DiskCount = params.get("DiskCount")
        self.ProjectId = params.get("ProjectId")


class InquiryPriceCreateDisksResponse(AbstractModel):
    """InquiryPriceCreateDisks返回參數結構體

    """

    def __init__(self):
        """
        :param DiskPrice: 描述了新購雲盤的價格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.Price`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = Price()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewDisksRequest(AbstractModel):
    """InquiryPriceRenewDisks請求參數結構體

    """

    def __init__(self):
        """
        :param DiskIds: 雲硬碟ID， 通過[DescribeDisks](/document/product/362/16315)介面查詢。
        :type DiskIds: list of str
        :param DiskChargePrepaids: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月雲盤的購買時長。如果在該參數中指定CurInstanceDeadline，則會按對齊到子機到期時間來續約。如果是批次續約詢價，該參數與Disks參數一一對應，元素數量需保持一緻。
        :type DiskChargePrepaids: list of DiskChargePrepaid
        :param NewDeadline: 指定雲盤新的到期時間，形式如：2017-12-17 00:00:00。參數`NewDeadline`和`DiskChargePrepaids`是兩種指定詢價時長的方式，兩者必傳一個。
        :type NewDeadline: str
        :param ProjectId: 雲盤所屬項目ID。 如傳入則僅用于鑒權。
        :type ProjectId: int
        """
        self.DiskIds = None
        self.DiskChargePrepaids = None
        self.NewDeadline = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        if params.get("DiskChargePrepaids") is not None:
            self.DiskChargePrepaids = []
            for item in params.get("DiskChargePrepaids"):
                obj = DiskChargePrepaid()
                obj._deserialize(item)
                self.DiskChargePrepaids.append(obj)
        self.NewDeadline = params.get("NewDeadline")
        self.ProjectId = params.get("ProjectId")


class InquiryPriceRenewDisksResponse(AbstractModel):
    """InquiryPriceRenewDisks返回參數結構體

    """

    def __init__(self):
        """
        :param DiskPrice: 描述了續約雲盤的價格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = PrepayPrice()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResizeDiskRequest(AbstractModel):
    """InquiryPriceResizeDisk請求參數結構體

    """

    def __init__(self):
        """
        :param DiskId: 雲硬碟ID， 通過[DescribeDisks](/document/product/362/16315)介面查詢。
        :type DiskId: str
        :param DiskSize: 雲硬碟擴容後的大小，單位爲GB，不得小於當前雲硬碟大小。雲盤大小取值範圍參見雲硬碟[産品分類](/document/product/362/2353)的說明。
        :type DiskSize: int
        :param ProjectId: 雲盤所屬項目ID。 如傳入則僅用于鑒權。
        :type ProjectId: int
        """
        self.DiskId = None
        self.DiskSize = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        self.ProjectId = params.get("ProjectId")


class InquiryPriceResizeDiskResponse(AbstractModel):
    """InquiryPriceResizeDisk返回參數結構體

    """

    def __init__(self):
        """
        :param DiskPrice: 描述了擴容雲盤的價格。
        :type DiskPrice: :class:`tencentcloud.cbs.v20170312.models.PrepayPrice`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DiskPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DiskPrice") is not None:
            self.DiskPrice = PrepayPrice()
            self.DiskPrice._deserialize(params.get("DiskPrice"))
        self.RequestId = params.get("RequestId")


class ModifyDiskAttributesRequest(AbstractModel):
    """ModifyDiskAttributes請求參數結構體

    """

    def __init__(self):
        """
        :param DiskIds: 一個或多個待操作的雲硬碟ID。如果傳入多個雲盤ID，僅支援所有雲盤修改爲同一屬性。
        :type DiskIds: list of str
        :param ProjectId: 新的雲硬碟項目ID，只支援修改彈性雲盤的項目ID。通過[DescribeProject](/document/api/378/4400)介面查詢可用項目及其ID。
        :type ProjectId: int
        :param DiskName: 新的雲硬碟名稱。
        :type DiskName: str
        :param Portable: 是否爲彈性雲盤，FALSE表示非彈性雲盤，TRUE表示彈性雲盤。僅支援非彈性雲盤修改爲彈性雲盤。
        :type Portable: bool
        :param DeleteWithInstance: 成功掛載到雲主機後該雲硬碟是否随雲主機銷毀，TRUE表示随雲主機銷毀，FALSE表示不随雲主機銷毀。僅支援按量計費雲硬碟數據盤。
        :type DeleteWithInstance: bool
        :param DiskType: 變更雲盤類型時，可傳入該參數，表示變更的目标類型，取值範圍：<br><li>CLOUD_PREMIUM：表示高效能雲硬碟<br><li>CLOUD_SSD：表示SSD雲硬碟。<br>當前不支援批次變更類型，即傳入DiskType時，DiskIds僅支援傳入一塊雲盤；<br>變更雲盤類型時不支援同時變更其他屬性。
        :type DiskType: str
        """
        self.DiskIds = None
        self.ProjectId = None
        self.DiskName = None
        self.Portable = None
        self.DeleteWithInstance = None
        self.DiskType = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.ProjectId = params.get("ProjectId")
        self.DiskName = params.get("DiskName")
        self.Portable = params.get("Portable")
        self.DeleteWithInstance = params.get("DeleteWithInstance")
        self.DiskType = params.get("DiskType")


class ModifyDiskAttributesResponse(AbstractModel):
    """ModifyDiskAttributes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDisksRenewFlagRequest(AbstractModel):
    """ModifyDisksRenewFlag請求參數結構體

    """

    def __init__(self):
        """
        :param DiskIds: 一個或多個待操作的雲硬碟ID。
        :type DiskIds: list of str
        :param RenewFlag: 雲盤的續約标識。取值範圍：<br><li>NOTIFY_AND_AUTO_RENEW：通知過期且自動續約<br><li>NOTIFY_AND_MANUAL_RENEW：通知過期不自動續約<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知過期不自動續約。
        :type RenewFlag: str
        """
        self.DiskIds = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.RenewFlag = params.get("RenewFlag")


class ModifyDisksRenewFlagResponse(AbstractModel):
    """ModifyDisksRenewFlag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySnapshotAttributeRequest(AbstractModel):
    """ModifySnapshotAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param SnapshotId: 快照ID, 可通過[DescribeSnapshots](/document/product/362/15647)查詢。
        :type SnapshotId: str
        :param SnapshotName: 新的快照名稱。最長爲60個字元。
        :type SnapshotName: str
        :param IsPermanent: 快照的保留時間，FALSE表示非永久保留，TRUE表示永久保留。僅支援将非永久快照修改爲永久快照。
        :type IsPermanent: bool
        """
        self.SnapshotId = None
        self.SnapshotName = None
        self.IsPermanent = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.SnapshotName = params.get("SnapshotName")
        self.IsPermanent = params.get("IsPermanent")


class ModifySnapshotAttributeResponse(AbstractModel):
    """ModifySnapshotAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Placement(AbstractModel):
    """描述了實例的抽象位置，包括其所在的可用區，所屬的項目，以及所屬的獨享集群的ID和名字。

    """

    def __init__(self):
        """
        :param Zone: 雲硬碟所屬的[可用區](/document/product/213/15753#ZoneInfo)ID。該參數也可以通過調用  [DescribeZones](/document/product/213/15707) 的返回值中的Zone欄位來獲取。
        :type Zone: str
        :param ProjectId: 實例所屬項目ID。該參數可以通過調用 [DescribeProject](/document/api/378/4400) 的返回值中的 projectId 欄位來獲取。不填爲預設項目。
        :type ProjectId: int
        :param CdcId: 實例所屬的獨享集群ID。作爲入參時，表示對指定的CdcId獨享集群的資源進行操作，可爲空。 作爲出參時，表示資源所屬的獨享集群的ID，可爲空。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CdcId: str
        :param CageId: 圍籠Id。作爲入參時，表示對指定的CageId的資源進行操作，可爲空。 作爲出參時，表示資源所屬圍籠ID，可爲空。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CageId: str
        :param CdcName: 獨享集群名字。作爲入參時，忽略。作爲出參時，表示雲硬碟所屬的獨享集群名，可爲空。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CdcName: str
        """
        self.Zone = None
        self.ProjectId = None
        self.CdcId = None
        self.CageId = None
        self.CdcName = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.CdcId = params.get("CdcId")
        self.CageId = params.get("CageId")
        self.CdcName = params.get("CdcName")


class Policy(AbstractModel):
    """描述了定期快照的執行策略。可理解爲在DayOfWeek指定的那幾天中，在Hour指定的小時執行該條定期快照策略。

    """

    def __init__(self):
        """
        :param DayOfWeek: 指定每周從周一到周日需要觸發定期快照的日期，取值範圍：[0, 6]。0表示周日觸發，1-6分别表示周一至周六。
        :type DayOfWeek: list of int non-negative
        :param Hour: 指定定期快照策略的觸發時間。單位爲小時，取值範圍：[0, 23]。00:00 ~ 23:00 共 24 個時間點可選，1表示 01:00，依此類推。
        :type Hour: list of int non-negative
        """
        self.DayOfWeek = None
        self.Hour = None


    def _deserialize(self, params):
        self.DayOfWeek = params.get("DayOfWeek")
        self.Hour = params.get("Hour")


class PrepayPrice(AbstractModel):
    """預付費訂單的費用。

    """

    def __init__(self):
        """
        :param OriginalPrice: 預付費雲盤或快照預支費用的原價，單位：元。
        :type OriginalPrice: float
        :param DiscountPrice: 預付費雲盤或快照預支費用的折扣價，單位：元。
        :type DiscountPrice: float
        """
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")


class Price(AbstractModel):
    """描述預付費或後付費雲盤的價格。

    """

    def __init__(self):
        """
        :param OriginalPrice: 預付費雲盤預支費用的原價，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginalPrice: float
        :param DiscountPrice: 預付費雲盤預支費用的折扣價，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DiscountPrice: float
        :param UnitPrice: 後付費雲盤原單價，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param ChargeUnit: 後付費雲盤的計價單元，取值範圍：<br><li>HOUR：表示後付費雲盤的計價單元是按小時計算。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ChargeUnit: str
        :param UnitPriceDiscount: 後付費雲盤折扣單價，單位：元。
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        """
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.UnitPrice = None
        self.ChargeUnit = None
        self.UnitPriceDiscount = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.UnitPriceDiscount = params.get("UnitPriceDiscount")


class RenewDiskRequest(AbstractModel):
    """RenewDisk請求參數結構體

    """

    def __init__(self):
        """
        :param DiskChargePrepaid: 預付費模式，即包年包月相關參數設置。通過該參數可以指定包年包月雲盤的續約時長。<br>在雲盤與掛載的實例一起續約的場景下，可以指定參數CurInstanceDeadline，此時雲盤會按對齊到實例續約後的到期時間來續約。
        :type DiskChargePrepaid: :class:`tencentcloud.cbs.v20170312.models.DiskChargePrepaid`
        :param DiskId: 雲硬碟ID， 通過[DescribeDisks](/document/product/362/16315)介面查詢。
        :type DiskId: str
        """
        self.DiskChargePrepaid = None
        self.DiskId = None


    def _deserialize(self, params):
        if params.get("DiskChargePrepaid") is not None:
            self.DiskChargePrepaid = DiskChargePrepaid()
            self.DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self.DiskId = params.get("DiskId")


class RenewDiskResponse(AbstractModel):
    """RenewDisk返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResizeDiskRequest(AbstractModel):
    """ResizeDisk請求參數結構體

    """

    def __init__(self):
        """
        :param DiskId: 雲硬碟ID， 通過[DescribeDisks](/document/product/362/16315)介面查詢。
        :type DiskId: str
        :param DiskSize: 雲硬碟擴容後的大小，單位爲GB，必須大于當前雲硬碟大小。雲盤大小取值範圍參見雲硬碟[産品分類](/document/product/362/2353)的說明。
        :type DiskSize: int
        """
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")


class ResizeDiskResponse(AbstractModel):
    """ResizeDisk返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Snapshot(AbstractModel):
    """描述了快照的詳細訊息

    """

    def __init__(self):
        """
        :param SnapshotId: 快照ID。
        :type SnapshotId: str
        :param Placement: 快照所在的位置。
        :type Placement: :class:`tencentcloud.cbs.v20170312.models.Placement`
        :param DiskUsage: 創建此快照的雲硬碟類型。取值範圍：<br><li>SYSTEM_DISK：系統盤<br><li>DATA_DISK：數據盤。
        :type DiskUsage: str
        :param DiskId: 創建此快照的雲硬碟ID。
        :type DiskId: str
        :param DiskSize: 創建此快照的雲硬碟大小，單位GB。
        :type DiskSize: int
        :param SnapshotState: 快照的狀态。取值範圍：<br><li>NORMAL：正常<br><li>CREATING：創建中<br><li>ROLLBACKING：回滾中<br><li>COPYING_FROM_REMOTE：跨地域複制快照拷貝中。
        :type SnapshotState: str
        :param SnapshotName: 快照名稱，用戶自定義的快照别名。調用[ModifySnapshotAttribute](/document/product/362/15650)可修改此欄位。
        :type SnapshotName: str
        :param Percent: 快照創建進度百分比，快照創建成功後此欄位恒爲100。
        :type Percent: int
        :param CreateTime: 快照的創建時間。
        :type CreateTime: str
        :param DeadlineTime: 快照到期時間。如果快照爲永久保留，此欄位爲空。
        :type DeadlineTime: str
        :param Encrypt: 是否爲加密盤創建的快照。取值範圍：<br><li>true：該快照爲加密盤創建的<br><li>false:非加密盤創建的快照。
        :type Encrypt: bool
        :param IsPermanent: 是否爲永久快照。取值範圍：<br><li>true：永久快照<br><li>false：非永久快照。
        :type IsPermanent: bool
        :param CopyingToRegions: 快照正在跨地域複制的目的地域，預設取值爲[]。
        :type CopyingToRegions: list of str
        :param CopyFromRemote: 是否爲跨地域複制的快照。取值範圍：<br><li>true：表示爲跨地域複制的快照。<br><li>false:本地域的快照。
        :type CopyFromRemote: bool
        :param Images: 快照關聯的映像清單。
        :type Images: list of Image
        :param ImageCount: 快照關聯的映像個數。
        :type ImageCount: int
        """
        self.SnapshotId = None
        self.Placement = None
        self.DiskUsage = None
        self.DiskId = None
        self.DiskSize = None
        self.SnapshotState = None
        self.SnapshotName = None
        self.Percent = None
        self.CreateTime = None
        self.DeadlineTime = None
        self.Encrypt = None
        self.IsPermanent = None
        self.CopyingToRegions = None
        self.CopyFromRemote = None
        self.Images = None
        self.ImageCount = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.DiskUsage = params.get("DiskUsage")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        self.SnapshotState = params.get("SnapshotState")
        self.SnapshotName = params.get("SnapshotName")
        self.Percent = params.get("Percent")
        self.CreateTime = params.get("CreateTime")
        self.DeadlineTime = params.get("DeadlineTime")
        self.Encrypt = params.get("Encrypt")
        self.IsPermanent = params.get("IsPermanent")
        self.CopyingToRegions = params.get("CopyingToRegions")
        self.CopyFromRemote = params.get("CopyFromRemote")
        if params.get("Images") is not None:
            self.Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self.Images.append(obj)
        self.ImageCount = params.get("ImageCount")


class SnapshotOperationLog(AbstractModel):
    """快照操作日志。

    """

    def __init__(self):
        """
        :param Operator: 操作者的UIN。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Operator: str
        :param Operation: 操作類型。取值範圍：
SNAP_OPERATION_DELETE：删除快照
SNAP_OPERATION_ROLLBACK：回滾快照
SNAP_OPERATION_MODIFY：修改快照屬性
SNAP_OPERATION_CREATE：創建快照
SNAP_OPERATION_COPY：跨地域複制快照
ASP_OPERATION_CREATE_SNAP：由定期快照策略創建快照
ASP_OPERATION_DELETE_SNAP：由定期快照策略删除快照
        :type Operation: str
        :param SnapshotId: 操作的快照ID。
        :type SnapshotId: str
        :param OperationState: 操作的狀态。取值範圍：
SUCCESS :表示操作成功 
FAILED :表示操作失敗 
PROCESSING :表示操作中。
        :type OperationState: str
        :param StartTime: 開始時間。
        :type StartTime: str
        :param EndTime: 結束時間。
        :type EndTime: str
        """
        self.Operator = None
        self.Operation = None
        self.SnapshotId = None
        self.OperationState = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.Operation = params.get("Operation")
        self.SnapshotId = params.get("SnapshotId")
        self.OperationState = params.get("OperationState")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class Tag(AbstractModel):
    """标簽。

    """

    def __init__(self):
        """
        :param Key: 标簽健。
        :type Key: str
        :param Value: 标簽值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class TerminateDisksRequest(AbstractModel):
    """TerminateDisks請求參數結構體

    """

    def __init__(self):
        """
        :param DiskIds: 需退還的雲盤ID清單。
        :type DiskIds: list of str
        """
        self.DiskIds = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")


class TerminateDisksResponse(AbstractModel):
    """TerminateDisks返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnbindAutoSnapshotPolicyRequest(AbstractModel):
    """UnbindAutoSnapshotPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param DiskIds: 要解綁定期快照策略的雲盤ID清單。
        :type DiskIds: list of str
        :param AutoSnapshotPolicyId: 要解綁的定期快照策略ID。
        :type AutoSnapshotPolicyId: str
        """
        self.DiskIds = None
        self.AutoSnapshotPolicyId = None


    def _deserialize(self, params):
        self.DiskIds = params.get("DiskIds")
        self.AutoSnapshotPolicyId = params.get("AutoSnapshotPolicyId")


class UnbindAutoSnapshotPolicyResponse(AbstractModel):
    """UnbindAutoSnapshotPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")