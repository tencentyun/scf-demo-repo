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
from tencentcloud.postgres.v20170312 import models


class PostgresClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'postgres.tencentcloudapi.com'


    def CloseDBExtranetAccess(self, request):
        """本介面（CloseDBExtranetAccess）用于關閉實例外網連結。

        :param request: 調用CloseDBExtranetAccess所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloseDBExtranetAccessResponse`

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


    def CreateDBInstances(self, request):
        """本介面 (CreateDBInstances) 用于創建一個或者多個PostgreSQL實例。

        :param request: 調用CreateDBInstances所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstancesResponse()
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
        """本介面（DescribeAccounts）用于獲取實例用戶清單。

        :param request: 調用DescribeAccounts所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountsResponse`

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


    def DescribeDBBackups(self, request):
        """本介面（DescribeDBBackups）用于查詢實例備份清單。

        :param request: 調用DescribeDBBackups所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBBackupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBBackupsResponse`

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


    def DescribeDBErrlogs(self, request):
        """本介面（DescribeDBErrlogs）用于獲取錯誤日志。

        :param request: 調用DescribeDBErrlogs所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBErrlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBErrlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBErrlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBErrlogsResponse()
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


    def DescribeDBInstanceAttribute(self, request):
        """本介面 (DescribeDBInstanceAttribute) 用于查詢某個實例的詳情訊息。

        :param request: 調用DescribeDBInstanceAttribute所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceAttributeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceAttributeResponse()
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
        """本介面 (DescribeDBInstances) 用于查詢一個或多個實例的詳細訊息。

        :param request: 調用DescribeDBInstances所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstancesResponse`

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


    def DescribeDBSlowlogs(self, request):
        """本介面（DescribeDBSlowlogs）用于獲取慢查詢日志。

        :param request: 調用DescribeDBSlowlogs所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBSlowlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBSlowlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSlowlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSlowlogsResponse()
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


    def DescribeDBXlogs(self, request):
        """本介面（DescribeDBXlogs）用于獲取實例Xlog清單。

        :param request: 調用DescribeDBXlogs所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBXlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBXlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBXlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBXlogsResponse()
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
        """本介面（DescribeOrders）用于獲取訂單訊息。

        :param request: 調用DescribeOrders所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeOrdersResponse`

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


    def DescribeProductConfig(self, request):
        """本介面 (DescribeProductConfig) 用于查詢售賣規格配置。

        :param request: 調用DescribeProductConfig所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeProductConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeProductConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductConfigResponse()
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


    def DescribeRegions(self, request):
        """本介面 (DescribeRegions) 用于查詢售賣地域訊息。

        :param request: 調用DescribeRegions所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def DescribeZones(self, request):
        """本介面 (DescribeZones) 用于查詢支援的可用區訊息。

        :param request: 調用DescribeZones所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZones", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
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


    def InitDBInstances(self, request):
        """本介面 (InitDBInstances) 用于初始化雲資料庫PostgreSQL實例。

        :param request: 調用InitDBInstances所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDBInstancesResponse()
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


    def InquiryPriceCreateDBInstances(self, request):
        """本介面 (InquiryPriceCreateDBInstances) 用于查詢購買一個或多個實例的價格訊息。

        :param request: 調用InquiryPriceCreateDBInstances所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceCreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateDBInstancesResponse()
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


    def InquiryPriceRenewDBInstance(self, request):
        """本介面（InquiryPriceRenewDBInstance）用于查詢續約實例的價格。

        :param request: 調用InquiryPriceRenewDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceRenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceRenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewDBInstanceResponse()
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


    def InquiryPriceUpgradeDBInstance(self, request):
        """本介面（InquiryPriceUpgradeDBInstance）用于查詢升級實例的價格。

        :param request: 調用InquiryPriceUpgradeDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceUpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceUpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceUpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpgradeDBInstanceResponse()
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


    def ModifyAccountRemark(self, request):
        """本介面（ModifyAccountRemark）用于修改帳号備注。

        :param request: 調用ModifyAccountRemark所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountRemarkRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountRemarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountRemark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountRemarkResponse()
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


    def ModifyDBInstanceName(self, request):
        """本介面（ModifyDBInstanceName）用于修改postgresql實例名字。

        :param request: 調用ModifyDBInstanceName所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceNameResponse()
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
        """本介面（ModifyDBInstancesProject）用于将實例轉至其他項目。

        :param request: 調用ModifyDBInstancesProject所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstancesProjectResponse`

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


    def OpenDBExtranetAccess(self, request):
        """本介面（OpenDBExtranetAccess）用于開通外網。

        :param request: 調用OpenDBExtranetAccess所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.OpenDBExtranetAccessResponse`

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


    def RenewInstance(self, request):
        """本介面（RenewInstance）用于續約實例。

        :param request: 調用RenewInstance所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewInstanceResponse()
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
        """本介面（ResetAccountPassword）用于重置實例的帳戶密碼。

        :param request: 調用ResetAccountPassword所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ResetAccountPasswordResponse`

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


    def RestartDBInstance(self, request):
        """本介面（RestartDBInstance）用于重啓實例。

        :param request: 調用RestartDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.RestartDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RestartDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartDBInstanceResponse()
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


    def SetAutoRenewFlag(self, request):
        """本介面（SetAutoRenewFlag）用于設置自動續約。

        :param request: 調用SetAutoRenewFlag所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.SetAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.SetAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetAutoRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetAutoRenewFlagResponse()
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
        """本介面（UpgradeDBInstance）用于升級實例。

        :param request: 調用UpgradeDBInstance所需參數的結構體。
        :type request: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceResponse`

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