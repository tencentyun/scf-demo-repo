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
from taifucloudcloud.es.v20180416 import models


class EsClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'es.taifucloudcloudapi.com'


    def CreateInstance(self, request):
        """創建指定規格的ES集群實例

        :param request: 調用CreateInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.es.v20180416.models.CreateInstanceRequest`
        :rtype: :class:`taifucloudcloud.es.v20180416.models.CreateInstanceResponse`

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

        :param request: 調用DeleteInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.es.v20180416.models.DeleteInstanceRequest`
        :rtype: :class:`taifucloudcloud.es.v20180416.models.DeleteInstanceResponse`

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

        :param request: 調用DescribeInstanceLogs所需參數的結構體。
        :type request: :class:`taifucloudcloud.es.v20180416.models.DescribeInstanceLogsRequest`
        :rtype: :class:`taifucloudcloud.es.v20180416.models.DescribeInstanceLogsResponse`

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

        :param request: 調用DescribeInstanceOperations所需參數的結構體。
        :type request: :class:`taifucloudcloud.es.v20180416.models.DescribeInstanceOperationsRequest`
        :rtype: :class:`taifucloudcloud.es.v20180416.models.DescribeInstanceOperationsResponse`

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

        :param request: 調用DescribeInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.es.v20180416.models.DescribeInstancesRequest`
        :rtype: :class:`taifucloudcloud.es.v20180416.models.DescribeInstancesResponse`

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
        """重啓ES集群實例(用於系統版本更新等操作)

        :param request: 調用RestartInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.es.v20180416.models.RestartInstanceRequest`
        :rtype: :class:`taifucloudcloud.es.v20180416.models.RestartInstanceResponse`

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
        """對集群進行擴縮容，修改實例名稱，修改配置，重置密碼， 添加Kibana黑白名單等操作。參數中InstanceId爲必傳參數，ForceRestart爲選填參數，剩餘參數傳遞組合及含義如下：
        - InstanceName：修改實例名稱(僅用於標識實例)
        - NodeNum：集群數據節點橫向擴縮容
        - NodeType, DiskSize：集群數據節點縱向擴縮容
        - MasterNodeNum: 集群專用主節點橫向擴縮容
        - MasterNodeType, MasterNodeDiskSize: 集群專用主節點縱向擴縮容
        - EsConfig：修改集群配置
        - Password：修改預設用戶elastic的密碼
        - EsAcl：修改訪問控制清單
        - CosBackUp: 設置集群COS自動備份訊息
        以上參數組合只能傳遞一種，多傳或少傳均會導緻請求失敗

        :param request: 調用UpdateInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.es.v20180416.models.UpdateInstanceRequest`
        :rtype: :class:`taifucloudcloud.es.v20180416.models.UpdateInstanceResponse`

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