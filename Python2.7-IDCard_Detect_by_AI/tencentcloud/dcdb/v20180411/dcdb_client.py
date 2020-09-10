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
from tencentcloud.dcdb.v20180411 import models


class DcdbClient(AbstractClient):
    _apiVersion = '2018-04-11'
    _endpoint = 'dcdb.tencentcloudapi.com'


    def CloneAccount(self, request):
        """本介面（CloneAccount）用于複製實例帳戶。

        :param request: 調用CloneAccount所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloneAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloneAccountResponse()
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


    def CloseDBExtranetAccess(self, request):
        """本介面(CloseDBExtranetAccess)用于關閉雲資料庫實例的外網訪問。關閉外網訪問後，外網網址将不可訪問，查詢實例清單介面将不返回對應實例的外網域名和端口訊息。

        :param request: 調用CloseDBExtranetAccess所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseDBExtranetAccessResponse()
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


    def CopyAccountPrivileges(self, request):
        """本介面（CopyAccountPrivileges）用于複制雲資料庫賬号的權限。
        注意：相同用戶名，不同Host是不同的賬号，Readonly屬性相同的賬号之間才能複制權限。

        :param request: 調用CopyAccountPrivileges所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CopyAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CopyAccountPrivilegesResponse()
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


    def CreateAccount(self, request):
        """本介面（CreateAccount）用于創建雲資料庫賬号。一個實例可以創建多個不同的賬号，相同的用戶名+不同的host是不同的賬号。

        :param request: 調用CreateAccount所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountResponse()
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


    def CreateDCDBInstance(self, request):
        """本介面（CreateDCDBInstance）用于創建包年包月的雲資料庫實例，可通過傳入實例規格、資料庫版本号、購買時長等訊息創建雲資料庫實例。

        :param request: 調用CreateDCDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDCDBInstanceResponse()
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


    def DeleteAccount(self, request):
        """本介面（DeleteAccount）用于删除雲資料庫賬号。用戶名+host唯一确定一個賬号。

        :param request: 調用DeleteAccount所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccountResponse()
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


    def DescribeAccountPrivileges(self, request):
        """本介面（DescribeAccountPrivileges）用于查詢雲資料庫賬号權限。
        注意：注意：相同用戶名，不同Host是不同的賬号。

        :param request: 調用DescribeAccountPrivileges所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountPrivilegesResponse()
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


    def DescribeAccounts(self, request):
        """本介面（DescribeAccounts）用于查詢指定雲資料庫實例的賬号清單。

        :param request: 調用DescribeAccounts所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
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


    def DescribeDBLogFiles(self, request):
        """本介面(DescribeDBLogFiles)用于獲取資料庫的各種日志清單，包括冷備、binlog、errlog和slowlog。

        :param request: 調用DescribeDBLogFiles所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBLogFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBLogFilesResponse()
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


    def DescribeDBParameters(self, request):
        """本介面(DescribeDBParameters)用于獲取資料庫的當前參數設置。

        :param request: 調用DescribeDBParameters所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBParameters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBParametersResponse()
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


    def DescribeDBSyncMode(self, request):
        """本介面（DescribeDBSyncMode）用于查詢雲資料庫實例的同步模式。

        :param request: 調用DescribeDBSyncMode所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSyncMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSyncModeResponse()
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


    def DescribeDCDBInstances(self, request):
        """查詢雲資料庫實例清單，支援通過項目ID、實例ID、内網網址、實例名稱等來篩選實例。
        如果不指定任何篩選條件，則預設返回10條實例記錄，單次請求最多支援返回100條實例記錄。

        :param request: 調用DescribeDCDBInstances所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBInstancesResponse()
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


    def DescribeDCDBPrice(self, request):
        """本介面（DescribeDCDBPrice）用于在購買實例前，查詢實例的價格。

        :param request: 調用DescribeDCDBPrice所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBPriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBPriceResponse()
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


    def DescribeDCDBRenewalPrice(self, request):
        """本介面（DescribeDCDBRenewalPrice）用于在續約分布式資料庫實例時，查詢續約的價格。

        :param request: 調用DescribeDCDBRenewalPrice所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBRenewalPriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBRenewalPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBRenewalPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBRenewalPriceResponse()
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


    def DescribeDCDBSaleInfo(self, request):
        """本介面(DescribeDCDBSaleInfo)用于查詢分布式資料庫可售賣的地域和可用區訊息。

        :param request: 調用DescribeDCDBSaleInfo所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBSaleInfoRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBSaleInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBSaleInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBSaleInfoResponse()
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


    def DescribeDCDBShards(self, request):
        """本介面（DescribeDCDBShards）用于查詢雲資料庫實例的分片訊息。

        :param request: 調用DescribeDCDBShards所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBShards", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBShardsResponse()
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


    def DescribeDCDBUpgradePrice(self, request):
        """本介面（DescribeDCDBUpgradePrice）用于查詢升級分布式資料庫實例價格。

        :param request: 調用DescribeDCDBUpgradePrice所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBUpgradePriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBUpgradePriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBUpgradePrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBUpgradePriceResponse()
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


    def DescribeDatabaseObjects(self, request):
        """本介面（DescribeDatabaseObjects）用于查詢雲資料庫實例的資料庫中的對象清單，包含表、儲存過程、視圖和函數。

        :param request: 調用DescribeDatabaseObjects所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabaseObjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseObjectsResponse()
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


    def DescribeDatabaseTable(self, request):
        """本介面（DescribeDatabaseObjects）用于查詢雲資料庫實例的表訊息。

        :param request: 調用DescribeDatabaseTable所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabaseTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseTableResponse()
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


    def DescribeDatabases(self, request):
        """本介面（DescribeDatabases）用于查詢雲資料庫實例的資料庫清單。

        :param request: 調用DescribeDatabases所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabasesResponse()
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


    def DescribeOrders(self, request):
        """本介面（DescribeOrders）用于查詢分布式資料庫訂單訊息。傳入訂單Id來查詢訂單關聯的分布式資料庫實例，和對應的任務流程ID。

        :param request: 調用DescribeOrders所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeOrdersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOrders", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOrdersResponse()
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


    def DescribeShardSpec(self, request):
        """查詢可創建的分布式資料庫可售賣的分片規格配置。

        :param request: 調用DescribeShardSpec所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeShardSpecRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeShardSpecResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShardSpec", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShardSpecResponse()
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


    def DescribeSqlLogs(self, request):
        """本介面（DescribeSqlLogs）用于獲取實例SQL日志。

        :param request: 調用DescribeSqlLogs所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeSqlLogsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeSqlLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSqlLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSqlLogsResponse()
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


    def GrantAccountPrivileges(self, request):
        """本介面（GrantAccountPrivileges）用于給雲資料庫賬号賦權。
        注意：相同用戶名，不同Host是不同的賬号。

        :param request: 調用GrantAccountPrivileges所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GrantAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GrantAccountPrivilegesResponse()
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


    def InitDCDBInstances(self, request):
        """本介面(InitDCDBInstances)用于初始化雲資料庫實例，包括設置預設字元集、表名大小寫敏感等。

        :param request: 調用InitDCDBInstances所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitDCDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDCDBInstancesResponse()
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


    def ModifyAccountDescription(self, request):
        """本介面（ModifyAccountDescription）用于修改雲資料庫賬号備注。
        注意：相同用戶名，不同Host是不同的賬号。

        :param request: 調用ModifyAccountDescription所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountDescriptionResponse()
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


    def ModifyDBInstancesProject(self, request):
        """本介面（ModifyDBInstancesProject）用于修改雲資料庫實例所屬項目。

        :param request: 調用ModifyDBInstancesProject所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstancesProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstancesProjectResponse()
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


    def ModifyDBParameters(self, request):
        """本介面(ModifyDBParameters)用于修改資料庫參數。

        :param request: 調用ModifyDBParameters所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBParameters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBParametersResponse()
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


    def ModifyDBSyncMode(self, request):
        """本介面（ModifyDBSyncMode）用于修改雲資料庫實例的同步模式。

        :param request: 調用ModifyDBSyncMode所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBSyncMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBSyncModeResponse()
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


    def OpenDBExtranetAccess(self, request):
        """本介面（OpenDBExtranetAccess）用于開通雲資料庫實例的外網訪問。開通外網訪問後，您可通過外網域名和端口訪問實例，可使用查詢實例清單介面獲取外網域名和端口訊息。

        :param request: 調用OpenDBExtranetAccess所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.OpenDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenDBExtranetAccessResponse()
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


    def RenewDCDBInstance(self, request):
        """本介面（RenewDCDBInstance）用于續約分布式資料庫實例。

        :param request: 調用RenewDCDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.RenewDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.RenewDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDCDBInstanceResponse()
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


    def ResetAccountPassword(self, request):
        """本介面（ResetAccountPassword）用于重置雲資料庫賬号的密碼。
        注意：相同用戶名，不同Host是不同的賬号。

        :param request: 調用ResetAccountPassword所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetAccountPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetAccountPasswordResponse()
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


    def UpgradeDCDBInstance(self, request):
        """本介面（UpgradeDCDBInstance）用于升級分布式資料庫實例。本介面完成下單和支付兩個動作，如果發生支付失敗的錯誤，調用用戶帳戶相關介面中的支付訂單介面（PayDeals）重新支付即可。

        :param request: 調用UpgradeDCDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDCDBInstanceResponse()
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