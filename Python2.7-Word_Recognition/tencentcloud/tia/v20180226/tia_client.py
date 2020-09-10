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
from tencentcloud.tia.v20180226 import models


class TiaClient(AbstractClient):
    _apiVersion = '2018-02-26'
    _endpoint = 'tia.tencentcloudapi.com'


    def CreateJob(self, request):
        """創建訓練任務

        :param request: 調用CreateJob所需參數的結構體。
        :type request: :class:`tencentcloud.tia.v20180226.models.CreateJobRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.CreateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateJobResponse()
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


    def CreateModel(self, request):
        """佈署模型，用以對外提供服務。有兩種佈署模式：`無服務器模式` 和 `集群模式`。`無服務器模式` 下，模型文件被佈署到無服務器雲函數，即 [SCF](https://cloud.tencent.com/product/scf)，用戶可以在其控制台上進一步操作。`集群模式` 下，模型文件被佈署到 TI-A 的計算集群中。

        :param request: 調用CreateModel所需參數的結構體。
        :type request: :class:`tencentcloud.tia.v20180226.models.CreateModelRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.CreateModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateModelResponse()
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
        """删除訓練任務

        :param request: 調用DeleteJob所需參數的結構體。
        :type request: :class:`tencentcloud.tia.v20180226.models.DeleteJobRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DeleteJobResponse`

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


    def DeleteModel(self, request):
        """删除指定的佈署模型。模型有兩種佈署模式：`無服務器模式` 和 `集群模式`。`無服務器模式` 下，模型文件被佈署到無服務器雲函數，即 [SCF](https://cloud.tencent.com/product/scf)，用戶可以在其控制台上進一步操作。`集群模式` 下，模型文件被佈署到 TI-A 的計算集群中。

        :param request: 調用DeleteModel所需參數的結構體。
        :type request: :class:`tencentcloud.tia.v20180226.models.DeleteModelRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DeleteModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteModelResponse()
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
        """獲取訓練任務詳情

        :param request: 調用DescribeJob所需參數的結構體。
        :type request: :class:`tencentcloud.tia.v20180226.models.DescribeJobRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DescribeJobResponse`

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


    def DescribeModel(self, request):
        """描述已經佈署的某個模型。而模型佈署有兩種模式：`無服務器模式` 和 `集群模式`。`無服務器模式` 下，模型文件被佈署到無服務器雲函數，即 [SCF](https://cloud.tencent.com/product/scf)，用戶可以在其控制台上進一步操作。`集群模式` 下，模型文件被佈署到 TI-A 的計算集群中。

        :param request: 調用DescribeModel所需參數的結構體。
        :type request: :class:`tencentcloud.tia.v20180226.models.DescribeModelRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DescribeModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModelResponse()
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


    def InstallAgent(self, request):
        """安裝agent

        :param request: 調用InstallAgent所需參數的結構體。
        :type request: :class:`tencentcloud.tia.v20180226.models.InstallAgentRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.InstallAgentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InstallAgent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InstallAgentResponse()
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


    def ListJobs(self, request):
        """列舉訓練任務

        :param request: 調用ListJobs所需參數的結構體。
        :type request: :class:`tencentcloud.tia.v20180226.models.ListJobsRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.ListJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListJobsResponse()
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


    def ListModels(self, request):
        """用以列舉已經佈署的模型。而佈署有兩種模式：`無服務器模式` 和 `集群模式`。`無服務器模式` 下，模型文件被佈署到無服務器雲函數，即 [SCF](https://cloud.tencent.com/product/scf)，用戶可以在其控制台上進一步操作。`集群模式` 下，模型文件被佈署到 TI-A 的計算集群中。不同佈署模式下的模型分開列出。

        :param request: 調用ListModels所需參數的結構體。
        :type request: :class:`tencentcloud.tia.v20180226.models.ListModelsRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.ListModelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListModels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListModelsResponse()
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


    def QueryLogs(self, request):
        """查詢 TI-A 訓練任務的日志

        :param request: 調用QueryLogs所需參數的結構體。
        :type request: :class:`tencentcloud.tia.v20180226.models.QueryLogsRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.QueryLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryLogsResponse()
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