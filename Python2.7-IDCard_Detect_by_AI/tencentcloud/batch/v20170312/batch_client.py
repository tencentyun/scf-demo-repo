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
from taifucloudcloud.batch.v20170312 import models


class BatchClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'batch.taifucloudcloudapi.com'


    def CreateComputeEnv(self, request):
        """用于創建計算環境

        :param request: 調用CreateComputeEnv所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.CreateComputeEnvRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.CreateComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateComputeEnvResponse()
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


    def CreateTaskTemplate(self, request):
        """用于創建任務範本

        :param request: 調用CreateTaskTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.CreateTaskTemplateRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.CreateTaskTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTaskTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskTemplateResponse()
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


    def DeleteComputeEnv(self, request):
        """用于删除計算環境

        :param request: 調用DeleteComputeEnv所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DeleteComputeEnvRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DeleteComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteComputeEnvResponse()
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


    def DeleteJob(self, request):
        """用于删除作業記錄。
        删除作業的效果相當于删除作業相關的所有訊息。删除成功後，作業相關的所有訊息都無法查詢。
        待删除的作業必須處于完結狀态，且其内部包含的所有任務實例也必須處于完結狀态，否則會禁止操作。完結狀态，是指處于 SUCCEED 或 FAILED 狀态。

        :param request: 調用DeleteJob所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DeleteJobRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DeleteJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteJobResponse()
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


    def DeleteTaskTemplates(self, request):
        """用于删除任務範本訊息

        :param request: 調用DeleteTaskTemplates所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DeleteTaskTemplatesRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DeleteTaskTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTaskTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTaskTemplatesResponse()
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


    def DescribeAvailableCvmInstanceTypes(self, request):
        """檢視可用的CVM機型配置訊息

        :param request: 調用DescribeAvailableCvmInstanceTypes所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAvailableCvmInstanceTypes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailableCvmInstanceTypesResponse()
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


    def DescribeComputeEnv(self, request):
        """用于查詢計算環境的詳細訊息

        :param request: 調用DescribeComputeEnv所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeComputeEnvRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvResponse()
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


    def DescribeComputeEnvActivities(self, request):
        """用于查詢計算環境的活動訊息

        :param request: 調用DescribeComputeEnvActivities所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeComputeEnvActivitiesRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeComputeEnvActivitiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvActivities", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvActivitiesResponse()
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


    def DescribeComputeEnvCreateInfo(self, request):
        """檢視計算環境的創建訊息。

        :param request: 調用DescribeComputeEnvCreateInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeComputeEnvCreateInfoRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeComputeEnvCreateInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvCreateInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvCreateInfoResponse()
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


    def DescribeComputeEnvCreateInfos(self, request):
        """用于檢視計算環境創建訊息清單，包括名稱、描述、類型、環境參數、通知及期望節點數等。

        :param request: 調用DescribeComputeEnvCreateInfos所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeComputeEnvCreateInfosRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeComputeEnvCreateInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvCreateInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvCreateInfosResponse()
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


    def DescribeComputeEnvs(self, request):
        """用于檢視計算環境清單

        :param request: 調用DescribeComputeEnvs所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeComputeEnvsRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeComputeEnvsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeComputeEnvs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeComputeEnvsResponse()
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


    def DescribeCvmZoneInstanceConfigInfos(self, request):
        """獲取批次計算可用區機型配置訊息

        :param request: 調用DescribeCvmZoneInstanceConfigInfos所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCvmZoneInstanceConfigInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCvmZoneInstanceConfigInfosResponse()
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


    def DescribeInstanceCategories(self, request):
        """目前對CVM現有實例族劃分爲四類，每一類包含若幹實例族。該介面用于查詢實例分類訊息。

        :param request: 調用DescribeInstanceCategories所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeInstanceCategoriesRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeInstanceCategoriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceCategories", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceCategoriesResponse()
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


    def DescribeJob(self, request):
        """用于檢視一個作業的詳細訊息，包括内部任務（Task）和依賴（Dependence）訊息。

        :param request: 調用DescribeJob所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeJobRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobResponse()
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


    def DescribeJobSubmitInfo(self, request):
        """用于查詢指定作業的提交訊息，其返回内容包括 JobId 和 SubmitJob 介面中作爲輸入參數的作業提交訊息

        :param request: 調用DescribeJobSubmitInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeJobSubmitInfoRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeJobSubmitInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJobSubmitInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobSubmitInfoResponse()
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


    def DescribeJobs(self, request):
        """用于查詢若幹個作業的概覽訊息

        :param request: 調用DescribeJobs所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeJobsRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobsResponse()
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


    def DescribeTask(self, request):
        """用于查詢指定任務的詳細訊息，包括任務内部的任務實例訊息。

        :param request: 調用DescribeTask所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeTaskRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResponse()
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


    def DescribeTaskLogs(self, request):
        """用于獲取任務多個實例标準輸出和标準錯誤日志。

        :param request: 調用DescribeTaskLogs所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeTaskLogsRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeTaskLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskLogsResponse()
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


    def DescribeTaskTemplates(self, request):
        """用于查詢任務範本訊息

        :param request: 調用DescribeTaskTemplates所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.DescribeTaskTemplatesRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.DescribeTaskTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskTemplatesResponse()
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


    def ModifyComputeEnv(self, request):
        """用于修改計算環境屬性

        :param request: 調用ModifyComputeEnv所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.ModifyComputeEnvRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.ModifyComputeEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyComputeEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyComputeEnvResponse()
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


    def ModifyTaskTemplate(self, request):
        """用于修改任務範本

        :param request: 調用ModifyTaskTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.ModifyTaskTemplateRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.ModifyTaskTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTaskTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTaskTemplateResponse()
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


    def RetryJobs(self, request):
        """用于重試作業中失敗的任務實例。
        當且僅當作業處于“FAILED”狀态，支援重試操作。重試操作成功後，作業會按照“DAG”中指定的任務依賴關系，依次重試各個任務中失敗的任務實例。任務實例的曆史訊息将被重置，如同首次運作一樣，參與後續的調度和執行。

        :param request: 調用RetryJobs所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.RetryJobsRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.RetryJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RetryJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RetryJobsResponse()
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


    def SubmitJob(self, request):
        """用于提交一個作業

        :param request: 調用SubmitJob所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.SubmitJobRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.SubmitJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitJobResponse()
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


    def TerminateComputeNode(self, request):
        """用于銷毀計算節點。
        對于狀态爲CREATED、CREATION_FAILED、RUNNING和ABNORMAL的節點，允許銷毀處理。

        :param request: 調用TerminateComputeNode所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.TerminateComputeNodeRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.TerminateComputeNodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateComputeNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateComputeNodeResponse()
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


    def TerminateComputeNodes(self, request):
        """用于批次銷毀計算節點，不允許重複銷毀同一個節點。

        :param request: 調用TerminateComputeNodes所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.TerminateComputeNodesRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.TerminateComputeNodesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateComputeNodes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateComputeNodesResponse()
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


    def TerminateJob(self, request):
        """用于終止作業。
        當作業處于“SUBMITTED”狀态時，禁止終止操作；當作業處于“SUCCEED”狀态時，終止操作不會生效。
        終止作業是一個異步過程。整個終止過程的耗時和任務總數成正比。終止的效果相當于所含的所有任務實例進行TerminateTaskInstance操作。具體效果和用法可參考TerminateTaskInstance。

        :param request: 調用TerminateJob所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.TerminateJobRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.TerminateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateJobResponse()
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


    def TerminateTaskInstance(self, request):
        """用于終止任務實例。
        對于狀态已經爲“SUCCEED”和“FAILED”的任務實例，不做處理。
        對于狀态爲“SUBMITTED”、“PENDING”、“RUNNABLE”的任務實例，狀态将置爲“FAILED”狀态。
        對于狀态爲“STARTING”、“RUNNING”、“FAILED_INTERRUPTED”的任務實例，分區兩種情況：如果未顯示指定計算環境，會先銷毀CVM服務器，然後将狀态置爲“FAILED”，具有一定耗時；如果指定了計算環境EnvId，任務實例狀态置爲“FAILED”，并重啓執行該任務的CVM服務器，具有一定的耗時。
        對于狀态爲“FAILED_INTERRUPTED”的任務實例，終止操作實際成功之後，相關資源和配額才會釋放。

        :param request: 調用TerminateTaskInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.batch.v20170312.models.TerminateTaskInstanceRequest`
        :rtype: :class:`taifucloudcloud.batch.v20170312.models.TerminateTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateTaskInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateTaskInstanceResponse()
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