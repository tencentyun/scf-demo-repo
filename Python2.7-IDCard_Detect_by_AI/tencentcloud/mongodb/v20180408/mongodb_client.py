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
from tencentcloud.mongodb.v20180408 import models


class MongodbClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'mongodb.tencentcloudapi.com'


    def CreateDBInstance(self, request):
        """本介面(CreateDBInstance)用于創建包年包月的MongoDB雲資料庫實例。

        :param request: 調用CreateDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceResponse()
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


    def CreateDBInstanceHour(self, request):
        """本介面(CreateDBInstanceHour)用于創建按量計費的MongoDB雲資料庫實例（包括主實例、災備實例和只讀實例），可通過傳入實例規格、實例類型、MongoDB版本、購買時長和數量等訊息創建雲資料庫實例。

        :param request: 調用CreateDBInstanceHour所需參數的結構體。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstanceHour", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceHourResponse()
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


    def TerminateDBInstance(self, request):
        """本介面(TerminateDBInstance)用于銷毀按量計費的MongoDB雲資料庫實例

        :param request: 調用TerminateDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.TerminateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.TerminateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateDBInstanceResponse()
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


    def UpgradeDBInstance(self, request):
        """本介面(UpgradeDBInstance)用于升級包年包月的MongoDB雲資料庫實例，可以擴容内存、儲存以及Oplog

        :param request: 調用UpgradeDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceResponse()
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


    def UpgradeDBInstanceHour(self, request):
        """本介面(UpgradeDBInstanceHour)用于升級按量計費的MongoDB雲資料庫實例，可以擴容内存、儲存以及oplog

        :param request: 調用UpgradeDBInstanceHour所需參數的結構體。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstanceHour", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceHourResponse()
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