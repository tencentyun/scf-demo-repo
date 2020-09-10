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

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.dts.v20180330 import models


class DtsClient(AbstractClient):
    _apiVersion = '2018-03-30'
    _endpoint = 'dts.tencentcloudapi.com'


    def CompleteMigrateJob(self, request):
        """完成數據遷移任務.
        選擇采用增量遷移方式的任務, 需要在遷移進度進入準備完成階段後, 調用本介面, 停止遷移增量數據.
        只有當正在遷移的任務, 進入了準備完成階段, 才能調用本介面完成遷移.

        :param request: 調用CompleteMigrateJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.CompleteMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CompleteMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompleteMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompleteMigrateJobResponse()
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


    def CreateMigrateCheckJob(self, request):
        """創建校驗遷移任務
        在開始遷移前, 必須調用本介面創建校驗, 且校驗成功後才能開始遷移. 校驗的結果可以通過DescribeMigrateCheckJob檢視.
        校驗成功後,遷移任務若有修改, 則必須重新創建校驗并通過後, 才能開始遷移.

        :param request: 調用CreateMigrateCheckJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateMigrateCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateMigrateCheckJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMigrateCheckJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMigrateCheckJobResponse()
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


    def CreateMigrateJob(self, request):
        """本介面用于創建數據遷移任務。

        如果是金融區鏈路, 請使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: 調用CreateMigrateJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMigrateJobResponse()
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


    def CreateSyncCheckJob(self, request):
        """在調用 StartSyncJob 介面啓動災備同步前, 必須調用本介面創建校驗, 且校驗成功後才能開始同步數據. 校驗的結果可以通過 DescribeSyncCheckJob 檢視.
        校驗成功後才能啓動同步.

        :param request: 調用CreateSyncCheckJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateSyncCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateSyncCheckJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSyncCheckJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSyncCheckJobResponse()
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


    def CreateSyncJob(self, request):
        """本介面(CreateSyncJob)用于創建災備同步任務。
        創建同步任務後，可以通過 CreateSyncCheckJob 介面發起校驗任務。校驗成功後才可以通過 StartSyncJob 介面啓動同步任務。

        :param request: 調用CreateSyncJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateSyncJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSyncJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSyncJobResponse()
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


    def DeleteMigrateJob(self, request):
        """删除數據遷移任務. 正在校驗和正在遷移的任務不允許删除

        :param request: 調用DeleteMigrateJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.DeleteMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DeleteMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMigrateJobResponse()
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


    def DeleteSyncJob(self, request):
        """删除災備同步任務 （運作中的同步任務不能删除）。

        :param request: 調用DeleteSyncJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.DeleteSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DeleteSyncJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSyncJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSyncJobResponse()
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


    def DescribeMigrateCheckJob(self, request):
        """本介面用于創建校驗後,獲取校驗的結果. 能查詢到當前校驗的狀态和進度.
        若通過校驗, 則可調用'StartMigrateJob' 開始遷移.
        若未通過校驗, 則能查詢到校驗失敗的原因. 請按照報錯, 通過'ModifyMigrateJob'修改遷移配置或是調整源/目标實例的相關參數.

        :param request: 調用DescribeMigrateCheckJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateCheckJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrateCheckJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrateCheckJobResponse()
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


    def DescribeMigrateJobs(self, request):
        """查詢數據遷移任務.
        如果是金融區鏈路, 請使用域名: https://dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: 調用DescribeMigrateJobs所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeMigrateJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrateJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrateJobsResponse()
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


    def DescribeSyncCheckJob(self, request):
        """本介面用于在通過 CreateSyncCheckJob 介面創建災備同步校驗任務後，獲取校驗的結果。能查詢到當前校驗的狀态和進度。
        若通過校驗, 則可調用 StartSyncJob 啓動同步任務。
        若未通過校驗, 則會返回校驗失敗的原因。 可通過 ModifySyncJob 修改配置，然後再次發起校驗。
        校驗任務需要大概約30秒，當返回的 Status 不爲 finished 時表示尚未校驗完成，需要輪詢該介面。
        如果 Status=finished 且 CheckFlag=1 時表示校驗成功。
        如果 Status=finished 且 CheckFlag !=1 時表示校驗失敗。

        :param request: 調用DescribeSyncCheckJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeSyncCheckJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeSyncCheckJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSyncCheckJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSyncCheckJobResponse()
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


    def DescribeSyncJobs(self, request):
        """查詢在遷移平台發起的災備同步任務

        :param request: 調用DescribeSyncJobs所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeSyncJobsRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeSyncJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSyncJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSyncJobsResponse()
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


    def ModifyMigrateJob(self, request):
        """修改數據遷移任務.
        當遷移任務處于下述狀态時, 允許調用本介面: 遷移創建中, 創建完成, 校驗成功, 校驗失敗, 遷移失敗.
        源實例和目标實例類型不允許修改, 目标實例地域不允許修改。

        如果是金融區鏈路, 請使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: 調用ModifyMigrateJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifyMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifyMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMigrateJobResponse()
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


    def ModifySyncJob(self, request):
        """修改災備同步任務.
        當同步任務處于下述狀态時, 允許調用本介面: 同步任務創建中, 創建完成, 校驗成功, 校驗失敗.
        源實例和目标實例訊息不允許修改，可以修改任務名、需要同步的庫表。

        :param request: 調用ModifySyncJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySyncJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySyncJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySyncJobResponse()
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


    def StartMigrateJob(self, request):
        """非定時任務會在調用後立即開始遷移，定時任務則會開始倒計時。
        調用此介面前，請務必先校驗數據遷移任務通過。

        :param request: 調用StartMigrateJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.StartMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.StartMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMigrateJobResponse()
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


    def StartSyncJob(self, request):
        """創建的災備同步任務在通過 CreateSyncCheckJob 和 DescribeSyncCheckJob 确定校驗成功後，可以調用該介面啓動同步

        :param request: 調用StartSyncJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.StartSyncJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.StartSyncJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartSyncJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartSyncJobResponse()
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


    def StopMigrateJob(self, request):
        """撤銷數據遷移任務.
        在遷移過程中允許調用該介面撤銷遷移, 撤銷遷移的任務會失敗.

        :param request: 調用StopMigrateJob所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.StopMigrateJobRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.StopMigrateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopMigrateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopMigrateJobResponse()
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


    def SwitchDrToMaster(self, request):
        """将災備升級爲主實例，停止從原來所屬主實例的同步，斷開主備關系。

        :param request: 調用SwitchDrToMaster所需參數的結構體。
        :type request: :class:`tencentcloud.dts.v20180330.models.SwitchDrToMasterRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.SwitchDrToMasterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwitchDrToMaster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchDrToMasterResponse()
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