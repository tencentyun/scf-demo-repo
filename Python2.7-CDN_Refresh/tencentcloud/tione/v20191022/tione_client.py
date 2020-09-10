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
from taifucloudcloud.tione.v20191022 import models


class TioneClient(AbstractClient):
    _apiVersion = '2019-10-22'
    _endpoint = 'tione.taifucloudcloudapi.com'


    def CreateCodeRepository(self, request):
        """創建儲存庫

        :param request: Request instance for CreateCodeRepository.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.CreateCodeRepositoryRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.CreateCodeRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCodeRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCodeRepositoryResponse()
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


    def CreateNotebookInstance(self, request):
        """創建Notebook實例

        :param request: Request instance for CreateNotebookInstance.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.CreateNotebookInstanceRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.CreateNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNotebookInstanceResponse()
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


    def CreateNotebookLifecycleScript(self, request):
        """創建Notebook生命週期腳本

        :param request: Request instance for CreateNotebookLifecycleScript.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.CreateNotebookLifecycleScriptRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.CreateNotebookLifecycleScriptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNotebookLifecycleScript", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNotebookLifecycleScriptResponse()
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


    def CreatePresignedNotebookInstanceUrl(self, request):
        """創建Notebook授權Url

        :param request: Request instance for CreatePresignedNotebookInstanceUrl.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.CreatePresignedNotebookInstanceUrlRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.CreatePresignedNotebookInstanceUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePresignedNotebookInstanceUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePresignedNotebookInstanceUrlResponse()
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


    def CreateTrainingJob(self, request):
        """創建訓練任務

        :param request: Request instance for CreateTrainingJob.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.CreateTrainingJobRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.CreateTrainingJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTrainingJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTrainingJobResponse()
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


    def DeleteCodeRepository(self, request):
        """删除儲存庫

        :param request: Request instance for DeleteCodeRepository.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.DeleteCodeRepositoryRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.DeleteCodeRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCodeRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCodeRepositoryResponse()
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


    def DeleteNotebookInstance(self, request):
        """删除notebook實例

        :param request: Request instance for DeleteNotebookInstance.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.DeleteNotebookInstanceRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.DeleteNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNotebookInstanceResponse()
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


    def DeleteNotebookLifecycleScript(self, request):
        """删除Notebook生命週期腳本

        :param request: Request instance for DeleteNotebookLifecycleScript.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.DeleteNotebookLifecycleScriptRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.DeleteNotebookLifecycleScriptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNotebookLifecycleScript", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNotebookLifecycleScriptResponse()
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


    def DescribeCodeRepositories(self, request):
        """查詢儲存庫清單

        :param request: Request instance for DescribeCodeRepositories.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.DescribeCodeRepositoriesRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.DescribeCodeRepositoriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCodeRepositories", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCodeRepositoriesResponse()
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


    def DescribeCodeRepository(self, request):
        """查詢儲存庫詳情

        :param request: Request instance for DescribeCodeRepository.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.DescribeCodeRepositoryRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.DescribeCodeRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCodeRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCodeRepositoryResponse()
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


    def DescribeNotebookInstance(self, request):
        """查詢Notebook實例詳情

        :param request: Request instance for DescribeNotebookInstance.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.DescribeNotebookInstanceRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.DescribeNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNotebookInstanceResponse()
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


    def DescribeNotebookInstances(self, request):
        """查詢Notebook實例清單

        :param request: Request instance for DescribeNotebookInstances.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.DescribeNotebookInstancesRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.DescribeNotebookInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNotebookInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNotebookInstancesResponse()
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


    def DescribeNotebookLifecycleScript(self, request):
        """檢視notebook生命週期腳本詳情

        :param request: Request instance for DescribeNotebookLifecycleScript.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.DescribeNotebookLifecycleScriptRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.DescribeNotebookLifecycleScriptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNotebookLifecycleScript", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNotebookLifecycleScriptResponse()
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


    def DescribeNotebookLifecycleScripts(self, request):
        """檢視notebook生命週期腳本清單

        :param request: Request instance for DescribeNotebookLifecycleScripts.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.DescribeNotebookLifecycleScriptsRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.DescribeNotebookLifecycleScriptsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNotebookLifecycleScripts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNotebookLifecycleScriptsResponse()
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


    def DescribeTrainingJob(self, request):
        """查詢訓練任務

        :param request: Request instance for DescribeTrainingJob.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.DescribeTrainingJobRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.DescribeTrainingJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrainingJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrainingJobResponse()
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


    def StartNotebookInstance(self, request):
        """啓動Notebook實例

        :param request: Request instance for StartNotebookInstance.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.StartNotebookInstanceRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.StartNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartNotebookInstanceResponse()
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


    def StopNotebookInstance(self, request):
        """停止Notebook實例

        :param request: Request instance for StopNotebookInstance.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.StopNotebookInstanceRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.StopNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopNotebookInstanceResponse()
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


    def StopTrainingJob(self, request):
        """停止訓練任務

        :param request: Request instance for StopTrainingJob.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.StopTrainingJobRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.StopTrainingJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopTrainingJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopTrainingJobResponse()
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


    def UpdateCodeRepository(self, request):
        """更新儲存庫

        :param request: Request instance for UpdateCodeRepository.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.UpdateCodeRepositoryRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.UpdateCodeRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCodeRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCodeRepositoryResponse()
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


    def UpdateNotebookInstance(self, request):
        """更新Notebook實例

        :param request: Request instance for UpdateNotebookInstance.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.UpdateNotebookInstanceRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.UpdateNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateNotebookInstanceResponse()
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


    def UpdateNotebookLifecycleScript(self, request):
        """更新notebook生命週期腳本

        :param request: Request instance for UpdateNotebookLifecycleScript.
        :type request: :class:`taifucloudcloud.tione.v20191022.models.UpdateNotebookLifecycleScriptRequest`
        :rtype: :class:`taifucloudcloud.tione.v20191022.models.UpdateNotebookLifecycleScriptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateNotebookLifecycleScript", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateNotebookLifecycleScriptResponse()
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