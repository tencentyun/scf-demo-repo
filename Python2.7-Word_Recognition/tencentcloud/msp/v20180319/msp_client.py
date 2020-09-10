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
from taifucloudcloud.msp.v20180319 import models


class MspClient(AbstractClient):
    _apiVersion = '2018-03-19'
    _endpoint = 'msp.taifucloudcloudapi.com'


    def DeregisterMigrationTask(self, request):
        """取消注冊遷移任務

        :param request: 調用DeregisterMigrationTask所需參數的結構體。
        :type request: :class:`taifucloudcloud.msp.v20180319.models.DeregisterMigrationTaskRequest`
        :rtype: :class:`taifucloudcloud.msp.v20180319.models.DeregisterMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeregisterMigrationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeregisterMigrationTaskResponse()
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


    def DescribeMigrationTask(self, request):
        """獲取指定遷移任務詳情

        :param request: 調用DescribeMigrationTask所需參數的結構體。
        :type request: :class:`taifucloudcloud.msp.v20180319.models.DescribeMigrationTaskRequest`
        :rtype: :class:`taifucloudcloud.msp.v20180319.models.DescribeMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrationTaskResponse()
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


    def ListMigrationProject(self, request):
        """獲取遷移項目名稱清單

        :param request: 調用ListMigrationProject所需參數的結構體。
        :type request: :class:`taifucloudcloud.msp.v20180319.models.ListMigrationProjectRequest`
        :rtype: :class:`taifucloudcloud.msp.v20180319.models.ListMigrationProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListMigrationProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListMigrationProjectResponse()
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


    def ListMigrationTask(self, request):
        """獲取遷移任務清單

        :param request: 調用ListMigrationTask所需參數的結構體。
        :type request: :class:`taifucloudcloud.msp.v20180319.models.ListMigrationTaskRequest`
        :rtype: :class:`taifucloudcloud.msp.v20180319.models.ListMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListMigrationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListMigrationTaskResponse()
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


    def ModifyMigrationTaskBelongToProject(self, request):
        """更改遷移任務所屬項目

        :param request: 調用ModifyMigrationTaskBelongToProject所需參數的結構體。
        :type request: :class:`taifucloudcloud.msp.v20180319.models.ModifyMigrationTaskBelongToProjectRequest`
        :rtype: :class:`taifucloudcloud.msp.v20180319.models.ModifyMigrationTaskBelongToProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMigrationTaskBelongToProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMigrationTaskBelongToProjectResponse()
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


    def ModifyMigrationTaskStatus(self, request):
        """更新遷移任務狀态

        :param request: 調用ModifyMigrationTaskStatus所需參數的結構體。
        :type request: :class:`taifucloudcloud.msp.v20180319.models.ModifyMigrationTaskStatusRequest`
        :rtype: :class:`taifucloudcloud.msp.v20180319.models.ModifyMigrationTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMigrationTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMigrationTaskStatusResponse()
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


    def RegisterMigrationTask(self, request):
        """注冊遷移任務

        :param request: 調用RegisterMigrationTask所需參數的結構體。
        :type request: :class:`taifucloudcloud.msp.v20180319.models.RegisterMigrationTaskRequest`
        :rtype: :class:`taifucloudcloud.msp.v20180319.models.RegisterMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterMigrationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterMigrationTaskResponse()
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