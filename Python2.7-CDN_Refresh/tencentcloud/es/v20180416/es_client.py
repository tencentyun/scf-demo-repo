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
from tencentcloud.es.v20180416 import models


class EsClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'es.tencentcloudapi.com'


    def CreateInstance(self, request):
        """創建指定規格的ES集群實例

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceResponse()
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


    def DeleteInstance(self, request):
        """銷毀集群實例

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteInstanceResponse()
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


    def DescribeInstanceLogs(self, request):
        """查詢用戶該地域下符合條件的ES集群的日志

        :param request: Request instance for DescribeInstanceLogs.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstanceLogsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstanceLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceLogsResponse()
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


    def DescribeInstanceOperations(self, request):
        """查詢實例指定條件下的操作記錄

        :param request: Request instance for DescribeInstanceOperations.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstanceOperationsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstanceOperationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceOperations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceOperationsResponse()
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


    def DescribeInstances(self, request):
        """查詢用戶該地域下符合條件的所有實例

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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


    def RestartInstance(self, request):
        """重啓ES集群實例(用于系統版本更新等操作)

        :param request: Request instance for RestartInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartInstanceResponse()
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


    def UpdateInstance(self, request):
        """對集群進行節點規格變更，修改實例名稱，修改配置，重置密碼， 添加Kibana黑白名單等操作。參數中InstanceId爲必傳參數，ForceRestart爲選填參數，剩餘參數傳遞組合及含義如下：
        - InstanceName：修改實例名稱(僅用于标識實例)
        - NodeInfoList: 修改節點配置（節點橫向擴縮容，縱向擴縮容，增加主節點，增加冷節點等）
        - EsConfig：修改集群配置
        - Password：修改預設用戶elastic的密碼
        - EsAcl：修改訪問控制清單
        - CosBackUp: 設置集群COS自動備份訊息
        以上參數組合只能傳遞一種，多傳或少傳均會導緻請求失敗

        :param request: Request instance for UpdateInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateInstanceResponse()
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


    def UpgradeInstance(self, request):
        """升級ES集群版本

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeInstanceResponse()
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


    def UpgradeLicense(self, request):
        """升級ES商業特性

        :param request: Request instance for UpgradeLicense.
        :type request: :class:`tencentcloud.es.v20180416.models.UpgradeLicenseRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpgradeLicenseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeLicense", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeLicenseResponse()
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