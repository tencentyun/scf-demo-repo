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

import json

from taifucloudcloud.common.exception.taifucloud_cloud_sdk_exception import TencentCloudSDKException
from taifucloudcloud.common.abstract_client import AbstractClient
from taifucloudcloud.cbs.v20170312 import models


class CbsClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'cbs.taifucloudcloudapi.com'


    def ApplySnapshot(self, request):
        """本介面（ApplySnapshot）用于回滾快照到原雲硬碟。

        * 僅支援回滾到原雲硬碟上。對于數據盤快照，如果您需要複制快照數據到其它雲硬碟上，請使用[CreateDisks](/document/product/362/16312)介面創建新的彈性雲盤，将快照數據複制到新購雲盤上。
        * 用于回滾的快照必須處于NORMAL狀态。快照狀态可以通過[DescribeSnapshots](/document/product/362/15647)介面查詢，見輸出參數中SnapshotState欄位解釋。
        * 如果是彈性雲盤，則雲盤必須處于未掛載狀态，雲硬碟掛載狀态可以通過[DescribeDisks](/document/product/362/16315)介面查詢，見Attached欄位解釋；如果是随實例一起購買的非彈性雲盤，則實例必須處于關機狀态，實例狀态可以通過[DescribeInstancesStatus](/document/product/213/15738)介面查詢。

        :param request: Request instance for ApplySnapshot.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.ApplySnapshotRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.ApplySnapshotResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplySnapshot", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplySnapshotResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachDisks(self, request):
        """本介面（AttachDisks）用于掛載雲硬碟。

        * 支援批次操作，将多塊雲盤掛載到同一雲主機。如果多個雲盤存在不允許掛載的雲盤，則操作不執行，以返回特定的錯誤碼返回。
        * 本介面爲異步介面，當掛載雲盤的請求成功返回時，表示後台已發起掛載雲盤的操作，可通過介面[DescribeDisks](/document/product/362/16315)來查詢對應雲盤的狀态，如果雲盤的狀态由“ATTACHING”變爲“ATTACHED”，則爲掛載成功。

        :param request: Request instance for AttachDisks.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.AttachDisksRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.AttachDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindAutoSnapshotPolicy(self, request):
        """本介面（BindAutoSnapshotPolicy）用于綁定雲硬碟到指定的定期快照策略。

        * 每個地域下的定期快照策略配額限制請參考文件[定期快照](/document/product/362/8191)。
        * 當已綁定定期快照策略的雲硬碟處于未使用狀态（即彈性雲盤未掛載或非彈性雲盤的主機處于關機狀态）将不會創建定期快照。

        :param request: Request instance for BindAutoSnapshotPolicy.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.BindAutoSnapshotPolicyRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.BindAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindAutoSnapshotPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindAutoSnapshotPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAutoSnapshotPolicy(self, request):
        """本介面（CreateAutoSnapshotPolicy）用于創建定期快照策略。

        * 每個地域可創建的定期快照策略數量限制請參考文件[定期快照](/document/product/362/8191)。
        * 每個地域可創建的快照有數量和容量的限制，具體請見Top Cloud 控制台快照頁面提示，如果快照超配額，定期快照創建會失敗。

        :param request: Request instance for CreateAutoSnapshotPolicy.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.CreateAutoSnapshotPolicyRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.CreateAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAutoSnapshotPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAutoSnapshotPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDisks(self, request):
        """本介面（CreateDisks）用于創建雲硬碟。

        * 預付費雲盤的購買會預先扣除本次雲盤購買所需金額，在調用本介面前請确保帳戶餘額充足。
        * 本介面支援傳入數據盤快照來創建雲盤，實現将快照數據複制到新購雲盤上。
        * 本介面爲異步介面，當創建請求下發成功後會返回一個新建的雲盤ID清單，此時雲盤的創建并未立即完成。可以通過調用[DescribeDisks](/document/product/362/16315)介面根據DiskId查詢對應雲盤，如果能查到雲盤，且狀态爲'UNATTACHED'或'ATTACHED'，則表示創建成功。

        :param request: Request instance for CreateDisks.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.CreateDisksRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.CreateDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSnapshot(self, request):
        """本介面（CreateSnapshot）用于對指定雲盤創建快照。

        * 只有具有快照能力的雲硬碟才能創建快照。雲硬碟是否具有快照能力可由[DescribeDisks](/document/product/362/16315)介面查詢，見SnapshotAbility欄位。
        * 可創建快照數量限制見[産品使用限制](https://cloud.taifucloud.com/doc/product/362/5145)。

        :param request: Request instance for CreateSnapshot.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.CreateSnapshotRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.CreateSnapshotResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSnapshot", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSnapshotResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAutoSnapshotPolicies(self, request):
        """本介面（DeleteAutoSnapshotPolicies）用于删除定期快照策略。

        *  支援批次操作。如果多個定期快照策略存在無法删除的，則操作不執行，以特定錯誤碼返回。

        :param request: Request instance for DeleteAutoSnapshotPolicies.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DeleteAutoSnapshotPoliciesRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DeleteAutoSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAutoSnapshotPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAutoSnapshotPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSnapshots(self, request):
        """本介面（DeleteSnapshots）用于删除快照。

        * 快照必須處于NORMAL狀态，快照狀态可以通過[DescribeSnapshots](/document/product/362/15647)介面查詢，見輸出參數中SnapshotState欄位解釋。
        * 支援批次操作。如果多個快照存在無法删除的快照，則操作不執行，以返回特定的錯誤碼返回。

        :param request: Request instance for DeleteSnapshots.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DeleteSnapshotsRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DeleteSnapshotsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSnapshots", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSnapshotsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAutoSnapshotPolicies(self, request):
        """本介面（DescribeAutoSnapshotPolicies）用于查詢定期快照策略。

        * 可以根據定期快照策略ID、名稱或者狀态等訊息來查詢定期快照策略的詳細訊息，不同條件之間爲與(AND)的關系，過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的定期快照策略表。

        :param request: Request instance for DescribeAutoSnapshotPolicies.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DescribeAutoSnapshotPoliciesRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DescribeAutoSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoSnapshotPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoSnapshotPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDiskAssociatedAutoSnapshotPolicy(self, request):
        """本介面（DescribeDiskAssociatedAutoSnapshotPolicy）用于查詢雲盤綁定的定期快照策略。

        :param request: Request instance for DescribeDiskAssociatedAutoSnapshotPolicy.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DescribeDiskAssociatedAutoSnapshotPolicyRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DescribeDiskAssociatedAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDiskAssociatedAutoSnapshotPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDiskAssociatedAutoSnapshotPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDiskConfigQuota(self, request):
        """本介面（DescribeDiskConfigQuota）用于查詢雲硬碟配額。

        :param request: Request instance for DescribeDiskConfigQuota.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DescribeDiskConfigQuotaRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DescribeDiskConfigQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDiskConfigQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDiskConfigQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDiskOperationLogs(self, request):
        """本介面（DescribeDiskOperationLogs）用于查詢雲盤操作日志清單。

        可根據雲盤ID過濾。雲盤ID形如：disk-a1kmcp13。

        :param request: Request instance for DescribeDiskOperationLogs.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DescribeDiskOperationLogsRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DescribeDiskOperationLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDiskOperationLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDiskOperationLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDisks(self, request):
        """本介面（DescribeDisks）用于查詢雲硬碟清單。

        * 可以根據雲硬碟ID、雲硬碟類型或者雲硬碟狀态等訊息來查詢雲硬碟的詳細訊息，不同條件之間爲與(AND)的關系，過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的雲硬碟清單。

        :param request: Request instance for DescribeDisks.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DescribeDisksRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DescribeDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstancesDiskNum(self, request):
        """本介面（DescribeInstancesDiskNum）用于查詢實例已掛載雲硬碟數量。

        * 支援批次操作，當傳入多個雲伺服器實例ID，返回結果會分别列出每個雲伺服器掛載的雲硬碟數量。

        :param request: Request instance for DescribeInstancesDiskNum.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DescribeInstancesDiskNumRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DescribeInstancesDiskNumResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesDiskNum", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesDiskNumResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSnapshotOperationLogs(self, request):
        """本介面（DescribeSnapshotOperationLogs）用于查詢快照操作日志清單。

        可根據快照ID過濾。快照ID形如：snap-a1kmcp13。

        :param request: Request instance for DescribeSnapshotOperationLogs.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DescribeSnapshotOperationLogsRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DescribeSnapshotOperationLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSnapshotOperationLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSnapshotOperationLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSnapshotSharePermission(self, request):
        """本介面（DescribeSnapshotSharePermission）用于查詢快照的分享訊息。

        :param request: Request instance for DescribeSnapshotSharePermission.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DescribeSnapshotSharePermissionRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DescribeSnapshotSharePermissionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSnapshotSharePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSnapshotSharePermissionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSnapshots(self, request):
        """本介面（DescribeSnapshots）用于查詢快照的詳細訊息。

        * 根據快照ID、創建快照的雲硬碟ID、創建快照的雲硬碟類型等對結果進行過濾，不同條件之間爲與(AND)的關系，過濾訊息詳細請見過濾器`Filter`。
        *  如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的快照清單。

        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DescribeSnapshotsRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DescribeSnapshotsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSnapshots", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSnapshotsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachDisks(self, request):
        """本介面（DetachDisks）用于解挂雲硬碟。

        * 支援批次操作，解挂掛載在同一主機上的多塊雲盤。如果多塊雲盤存在不允許解掛載的雲盤，則操作不執行，以返回特定的錯誤碼返回。
        * 本介面爲異步介面，當請求成功返回時，雲盤并未立即從主機解掛載，可通過介面[DescribeDisks](/document/product/362/16315)來查詢對應雲盤的狀态，如果雲盤的狀态由“ATTACHED”變爲“UNATTACHED”，則爲解掛載成功。

        :param request: Request instance for DetachDisks.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.DetachDisksRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.DetachDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetSnapOverview(self, request):
        """獲取快照概覽訊息

        :param request: Request instance for GetSnapOverview.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.GetSnapOverviewRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.GetSnapOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSnapOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSnapOverviewResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceCreateDisks(self, request):
        """本介面（InquiryPriceCreateDisks）用于創建雲硬碟詢價。

        * 支援查詢創建多塊雲硬碟的價格，此時返回結果爲總價格。

        :param request: Request instance for InquiryPriceCreateDisks.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.InquiryPriceCreateDisksRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.InquiryPriceCreateDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceRenewDisks(self, request):
        """本介面（InquiryPriceRenewDisks）用于續約雲硬碟詢價。

        * 只支援查詢預付費模式的彈性雲盤續約價格。
        * 支援與掛載實例一起續約的場景，需要在[DiskChargePrepaid](/document/product/362/15669#DiskChargePrepaid)參數中指定CurInstanceDeadline，此時會按對齊到實例續約後的到期時間來續約詢價。
        * 支援爲多塊雲盤指定不同的續約時長，此時返回的價格爲多塊雲盤續約的總價格。

        :param request: Request instance for InquiryPriceRenewDisks.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.InquiryPriceRenewDisksRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.InquiryPriceRenewDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceResizeDisk(self, request):
        """本介面（InquiryPriceResizeDisk）用于擴容雲硬碟詢價。

        * 只支援預付費模式的雲硬碟擴容詢價。

        :param request: Request instance for InquiryPriceResizeDisk.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.InquiryPriceResizeDiskRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.InquiryPriceResizeDiskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResizeDisk", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResizeDiskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAutoSnapshotPolicyAttribute(self, request):
        """本介面（ModifyAutoSnapshotPolicyAttribute）用于修改定期快照策略屬性。

        * 可通過該介面修改定期快照策略的執行策略、名稱、是否啟動等屬性。
        * 修改保留天數時必須保證不與是否永久保留屬性沖突，否則整個操作失敗，以特定的錯誤碼返回。

        :param request: Request instance for ModifyAutoSnapshotPolicyAttribute.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.ModifyAutoSnapshotPolicyAttributeRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.ModifyAutoSnapshotPolicyAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoSnapshotPolicyAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoSnapshotPolicyAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDiskAttributes(self, request):
        """* 只支援修改彈性雲盤的項目ID。随雲主機創建的雲硬碟項目ID與雲主機聯動。可以通過[DescribeDisks](/document/product/362/16315)介面查詢，見輸出參數中Portable欄位解釋。
        * “雲硬碟名稱”僅爲方便用戶自己管理之用，Top Cloud 并不以此名稱作爲提交工單或是進行雲盤管理操作的依據。
        * 支援批次操作，如果傳入多個雲盤ID，則所有雲盤修改爲同一屬性。如果存在不允許操作的雲盤，則操作不執行，以特定錯誤碼返回。

        :param request: Request instance for ModifyDiskAttributes.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.ModifyDiskAttributesRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.ModifyDiskAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDiskAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDiskAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDisksChargeType(self, request):
        """介面請求域名： cbs.taifucloudcloudapi.com 。

        本介面 (ModifyDisksChargeType) 用于切換雲盤的計費模式。

        只支援從 POSTPAID_BY_HOUR 計費模式切換爲PREPAID計費模式。
        非彈性雲盤不支援此介面，請通過修改實例計費模式介面将實例連同非彈性雲盤一起轉換。
        預設介面請求頻率限制：10次/秒。

        :param request: Request instance for ModifyDisksChargeType.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.ModifyDisksChargeTypeRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.ModifyDisksChargeTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDisksChargeType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDisksChargeTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDisksRenewFlag(self, request):
        """本介面（ModifyDisksRenewFlag）用于修改雲硬碟續約标識，支援批次修改。

        :param request: Request instance for ModifyDisksRenewFlag.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.ModifyDisksRenewFlagRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.ModifyDisksRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDisksRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDisksRenewFlagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySnapshotAttribute(self, request):
        """本介面（ModifySnapshotAttribute）用于修改指定快照的屬性。

        * 當前僅支援修改快照名稱及将非永久快照修改爲永久快照。
        * “快照名稱”僅爲方便用戶自己管理之用，Top Cloud 并不以此名稱作爲提交工單或是進行快照管理操作的依據。

        :param request: Request instance for ModifySnapshotAttribute.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.ModifySnapshotAttributeRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.ModifySnapshotAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySnapshotAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySnapshotAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySnapshotsSharePermission(self, request):
        """本介面（ModifySnapshotsSharePermission）用于修改快照分享訊息。

        分享快照後，被分享帳戶可以通過該快照創建雲硬碟。
        * 每個快照最多可分享給50個帳戶。
        * 分享快照無法更改名稱，描述，僅可用于創建雲硬碟。
        * 只支援分享到對方帳戶相同地域。
        * 僅支援分享數據盤快照。

        :param request: Request instance for ModifySnapshotsSharePermission.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.ModifySnapshotsSharePermissionRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.ModifySnapshotsSharePermissionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySnapshotsSharePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySnapshotsSharePermissionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewDisk(self, request):
        """本介面（RenewDisk）用于續約雲硬碟。

        * 只支援預付費的雲硬碟。雲硬碟類型可以通過[DescribeDisks](/document/product/362/16315)介面查詢，見輸出參數中DiskChargeType欄位解釋。
        * 支援與掛載實例一起續約的場景，需要在[DiskChargePrepaid](/document/product/362/15669#DiskChargePrepaid)參數中指定CurInstanceDeadline，此時會按對齊到子機續約後的到期時間來續約。

        :param request: Request instance for RenewDisk.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.RenewDiskRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.RenewDiskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDisk", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDiskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResizeDisk(self, request):
        """本介面（ResizeDisk）用于擴容雲硬碟。

        * 只支援擴容彈性雲盤。雲硬碟類型可以通過[DescribeDisks](/document/product/362/16315)介面查詢，見輸出參數中Portable欄位解釋。随雲主機創建的雲硬碟需通過[ResizeInstanceDisks](/document/product/213/15731)介面擴容。
        * 本介面爲異步介面，介面成功返回時，雲盤并未立即擴容到指定大小，可通過介面[DescribeDisks](/document/product/362/16315)來查詢對應雲盤的狀态，如果雲盤的狀态爲“EXPANDING”，表示正在擴容中，當狀态變爲“UNATTACHED”，表示擴容完成。

        :param request: Request instance for ResizeDisk.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.ResizeDiskRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.ResizeDiskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResizeDisk", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResizeDiskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateDisks(self, request):
        """本介面（TerminateDisks）用于退還雲硬碟。

        * 不再使用的雲盤，可通過本介面主動退還。
        * 本介面支援退還預付費雲盤和按小時後付費雲盤。按小時後付費雲盤可直接退還，預付費雲盤需符合退還規則。
        * 支援批次操作，每次請求批次雲硬碟的上限爲50。如果批次雲盤存在不允許操作的，請求會以特定錯誤碼返回。

        :param request: Request instance for TerminateDisks.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.TerminateDisksRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.TerminateDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnbindAutoSnapshotPolicy(self, request):
        """本介面（UnbindAutoSnapshotPolicy）用于解除雲硬碟綁定的定期快照策略。

        * 支援批次操作，可一次解除多個雲盤與同一定期快照策略的綁定。
        * 如果傳入的雲盤未綁定到當前定期快照策略，介面将自動跳過，僅解綁與當前定期快照策略綁定的雲盤。

        :param request: Request instance for UnbindAutoSnapshotPolicy.
        :type request: :class:`taifucloudcloud.cbs.v20170312.models.UnbindAutoSnapshotPolicyRequest`
        :rtype: :class:`taifucloudcloud.cbs.v20170312.models.UnbindAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindAutoSnapshotPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindAutoSnapshotPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)