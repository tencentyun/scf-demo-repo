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
from tencentcloud.mongodb.v20190725 import models


class MongodbClient(AbstractClient):
    _apiVersion = '2019-07-25'
    _endpoint = 'mongodb.tencentcloudapi.com'


    def AssignProject(self, request):
        """本介面(AssignProject)用于指定雲資料庫實例的所屬項目。

        :param request: Request instance for AssignProject.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.AssignProjectRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.AssignProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignProjectResponse()
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


    def CreateDBInstance(self, request):
        """本介面(CreateDBInstance)用于創建包年包月的MongoDB雲資料庫實例。介面支援的售賣規格，可從查詢雲資料庫的售賣規格（DescribeSpecInfo）獲取。

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceResponse`

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
        """本介面(CreateDBInstanceHour)用于創建按量計費的MongoDB雲資料庫實例。

        :param request: Request instance for CreateDBInstanceHour.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceHourResponse`

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


    def DescribeBackupAccess(self, request):
        """本介面（DescribeBackupAccess）用于獲取備份文件的下載授權，具體的備份文件訊息可通過查詢實例備份清單（DescribeDBBackups）介面獲取

        :param request: Request instance for DescribeBackupAccess.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupAccessRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupAccessResponse()
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


    def DescribeClientConnections(self, request):
        """本介面(DescribeClientConnections)用于查詢實例用戶端連接訊息，包括連接IP和連接數量。

        :param request: Request instance for DescribeClientConnections.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeClientConnectionsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeClientConnectionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClientConnections", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClientConnectionsResponse()
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


    def DescribeDBBackups(self, request):
        """本介面（DescribeDBBackups）用于查詢實例備份清單，目前只支援7天内的備份查詢。

        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBBackupsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBBackupsResponse()
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


    def DescribeDBInstanceDeal(self, request):
        """本介面（DescribeDBInstanceDeal）用于獲取MongoDB購買、續約及變配訂單詳細。

        :param request: Request instance for DescribeDBInstanceDeal.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceDealRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceDealResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceDeal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceDealResponse()
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


    def DescribeDBInstances(self, request):
        """本介面(DescribeDBInstances)用于查詢雲資料庫實例清單，支援通過項目ID、實例ID、實例狀态等過濾條件來篩選實例。支援查詢主實例、災備實例和只讀實例訊息清單。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstancesResponse()
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


    def DescribeSlowLogPatterns(self, request):
        """本介面（DescribeSlowLogPatterns）用于獲取資料庫實例慢日志的統計訊息。

        :param request: Request instance for DescribeSlowLogPatterns.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogPatternsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogPatternsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogPatterns", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogPatternsResponse()
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


    def DescribeSlowLogs(self, request):
        """本介面（DescribeSlowLogs）用于獲取雲資料庫慢日志訊息。介面只支援查詢最近7天内慢日志。

        :param request: Request instance for DescribeSlowLogs.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogsResponse()
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


    def DescribeSpecInfo(self, request):
        """本介面(DescribeSpecInfo)用于查詢實例的售賣規格。

        :param request: Request instance for DescribeSpecInfo.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSpecInfoRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSpecInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSpecInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSpecInfoResponse()
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


    def InquirePriceCreateDBInstances(self, request):
        """本介面用于創建資料庫實例詢價。本介面參數中必須傳入region參數，否則無法通過校驗。本介面僅允許針對購買限制範圍内的實例配置進行詢價。

        :param request: Request instance for InquirePriceCreateDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceCreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquirePriceCreateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquirePriceCreateDBInstancesResponse()
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


    def InquirePriceModifyDBInstanceSpec(self, request):
        """本介面 (InquirePriceModifyDBInstanceSpec) 用于調整實例的配置詢價。

        :param request: Request instance for InquirePriceModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceModifyDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquirePriceModifyDBInstanceSpec", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquirePriceModifyDBInstanceSpecResponse()
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


    def InquirePriceRenewDBInstances(self, request):
        """本介面 (InquiryPriceRenewDBInstances) 用于續約包年包月實例詢價。

        :param request: Request instance for InquirePriceRenewDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceRenewDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceRenewDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquirePriceRenewDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquirePriceRenewDBInstancesResponse()
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


    def IsolateDBInstance(self, request):
        """本介面(IsolateDBInstance)用于隔離MongoDB雲資料庫按量計費實例。隔離後實例保留在資源回收筒中，不能再寫入數據。隔離一定時間後，實例會徹底删除，資源回收筒保存時間請參考按量計費的服務條款。在隔離中的按量計費實例無法恢複，請謹慎操作。

        :param request: Request instance for IsolateDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.IsolateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.IsolateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IsolateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateDBInstanceResponse()
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


    def ModifyDBInstanceSpec(self, request):
        """本介面(ModifyDBInstanceSpec)用于調整MongoDB雲資料庫實例配置。介面支援的售賣規格，可從查詢雲資料庫的售賣規格（DescribeSpecInfo）獲取。

        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceSpec", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSpecResponse()
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


    def OfflineIsolatedDBInstance(self, request):
        """本介面(OfflineIsolatedInstances)用于立即下線隔離狀态的雲資料庫實例。進行操作的實例狀态必須爲隔離狀态。

        :param request: Request instance for OfflineIsolatedDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.OfflineIsolatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.OfflineIsolatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OfflineIsolatedDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OfflineIsolatedDBInstanceResponse()
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


    def RenameInstance(self, request):
        """本介面(RenameInstance)用于修改雲資料庫實例的名稱。

        :param request: Request instance for RenameInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.RenameInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.RenameInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenameInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenameInstanceResponse()
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


    def RenewDBInstances(self, request):
        """本介面(RenewDBInstance)用于續約雲資料庫實例，僅支援付費模式爲包年包月的實例。按量計費實例不需要續約。

        :param request: Request instance for RenewDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.RenewDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.RenewDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDBInstancesResponse()
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