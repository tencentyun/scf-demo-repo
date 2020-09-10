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


    def ActivateSubscribe(self, request):
        """本介面用于配置數據訂閱，只有在未配置狀态的訂閱實例才能調用此介面。

        :param request: Request instance for ActivateSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.ActivateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ActivateSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ActivateSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ActivateSubscribeResponse()
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


    def CompleteMigrateJob(self, request):
        """本介面（CompleteMigrateJob）用于完成數據遷移任務。
        選擇采用增量遷移方式的任務, 需要在遷移進度進入準備完成階段後, 調用本介面, 停止遷移增量數據。
        通過DescribeMigrateJobs介面查詢到任務的狀态爲準備完成（status=8）時，此時可以調用本介面完成遷移任務。

        :param request: Request instance for CompleteMigrateJob.
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

        :param request: Request instance for CreateMigrateCheckJob.
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
        """本介面（CreateMigrateJob）用于創建數據遷移任務。

        如果是金融區鏈路, 請使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: Request instance for CreateMigrateJob.
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


    def CreateSubscribe(self, request):
        """本介面(CreateSubscribe)用于創建一個數據訂閱實例。

        :param request: Request instance for CreateSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.CreateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.CreateSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubscribeResponse()
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

        :param request: Request instance for CreateSyncCheckJob.
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

        :param request: Request instance for CreateSyncJob.
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
        """本介面（DeleteMigrationJob）用于删除數據遷移任務。當通過DescribeMigrateJobs介面查詢到任務的狀态爲：檢驗中（status=3）、運作中（status=7）、準備完成（status=8）、撤銷中（status=11）或者完成中（status=12）時，不允許删除任務。

        :param request: Request instance for DeleteMigrateJob.
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

        :param request: Request instance for DeleteSyncJob.
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


    def DescribeAsyncRequestInfo(self, request):
        """本介面（DescribeAsyncRequestInfo）用于查詢任務執行結果

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeAsyncRequestInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAsyncRequestInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAsyncRequestInfoResponse()
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

        :param request: Request instance for DescribeMigrateCheckJob.
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

        :param request: Request instance for DescribeMigrateJobs.
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


    def DescribeRegionConf(self, request):
        """本介面（DescribeRegionConf）用于查詢可售賣訂閱實例的地域

        :param request: Request instance for DescribeRegionConf.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeRegionConfRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeRegionConfResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegionConf", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionConfResponse()
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


    def DescribeSubscribeConf(self, request):
        """本介面（DescribeSubscribeConf）用于查詢訂閱實例配置

        :param request: Request instance for DescribeSubscribeConf.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribeConfRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribeConfResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubscribeConf", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubscribeConfResponse()
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


    def DescribeSubscribes(self, request):
        """本介面(DescribeSubscribes)獲取數據訂閱實例訊息清單，預設分頁，每次返回20條

        :param request: Request instance for DescribeSubscribes.
        :type request: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribesRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.DescribeSubscribesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubscribes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubscribesResponse()
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

        :param request: Request instance for DescribeSyncCheckJob.
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

        :param request: Request instance for DescribeSyncJobs.
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


    def IsolateSubscribe(self, request):
        """本介面（IsolateSubscribe）用于隔離小時計費的訂閱實例。調用後，訂閱實例将不能使用，同時停止計費。

        :param request: Request instance for IsolateSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.IsolateSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.IsolateSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IsolateSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateSubscribeResponse()
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
        """本介面（ModifyMigrateJob）用于修改數據遷移任務。
        當遷移任務處于下述狀态時，允許調用本介面修改遷移任務：遷移創建中（status=1）、 校驗成功(status=4)、校驗失敗(status=5)、遷移失敗(status=10)。但源實例、目标實例類型和目标實例地域不允許修改。

        如果是金融區鏈路, 請使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com

        :param request: Request instance for ModifyMigrateJob.
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


    def ModifySubscribeConsumeTime(self, request):
        """本介面(ModifySubscribeConsumeTime)用于修改數據訂閱通道的消費時間點

        :param request: Request instance for ModifySubscribeConsumeTime.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeConsumeTimeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeConsumeTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubscribeConsumeTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubscribeConsumeTimeResponse()
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


    def ModifySubscribeName(self, request):
        """本介面(ModifySubscribeName)用于修改數據訂閱實例的名稱

        :param request: Request instance for ModifySubscribeName.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeNameRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubscribeName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubscribeNameResponse()
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


    def ModifySubscribeObjects(self, request):
        """本介面(ModifySubscribeObjects)用于修改數據訂閱通道的訂閱規則

        :param request: Request instance for ModifySubscribeObjects.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeObjectsRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeObjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubscribeObjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubscribeObjectsResponse()
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


    def ModifySubscribeVipVport(self, request):
        """本介面(ModifySubscribeVipVport)用于修改數據訂閱實例的IP和端口号

        :param request: Request instance for ModifySubscribeVipVport.
        :type request: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeVipVportRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ModifySubscribeVipVportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubscribeVipVport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubscribeVipVportResponse()
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

        :param request: Request instance for ModifySyncJob.
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


    def OfflineIsolatedSubscribe(self, request):
        """本介面（OfflineIsolatedSubscribe）用于下線已隔離的數據訂閱實例

        :param request: Request instance for OfflineIsolatedSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.OfflineIsolatedSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.OfflineIsolatedSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OfflineIsolatedSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OfflineIsolatedSubscribeResponse()
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


    def ResetSubscribe(self, request):
        """本介面(ResetSubscribe)用于重置數據訂閱實例，已經啟動的數據訂閱實例，重置後可以使用ActivateSubscribe介面綁定其他的資料庫實例

        :param request: Request instance for ResetSubscribe.
        :type request: :class:`tencentcloud.dts.v20180330.models.ResetSubscribeRequest`
        :rtype: :class:`tencentcloud.dts.v20180330.models.ResetSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetSubscribeResponse()
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
        """本介面（StartMigrationJob）用于啓動遷移任務。非定時遷移任務會在調用後立即開始遷移，定時任務則會開始倒計時。
        調用此介面前，請務必先使用CreateMigrateCheckJob校驗數據遷移任務，并通過DescribeMigrateJobs介面查詢到任務狀态爲校驗通過（status=4）時，才能啓動數據遷移任務。

        :param request: Request instance for StartMigrateJob.
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

        :param request: Request instance for StartSyncJob.
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
        """本介面（StopMigrateJob）用于撤銷數據遷移任務。
        在遷移過程中允許調用該介面撤銷遷移, 撤銷遷移的任務會失敗。通過DescribeMigrateJobs介面查詢到任務狀态爲運作中（status=7）或準備完成（status=8）時，才能撤銷數據遷移任務。

        :param request: Request instance for StopMigrateJob.
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

        :param request: Request instance for SwitchDrToMaster.
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