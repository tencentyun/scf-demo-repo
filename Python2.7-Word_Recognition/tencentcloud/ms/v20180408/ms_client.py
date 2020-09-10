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
from tencentcloud.ms.v20180408 import models


class MsClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'ms.tencentcloudapi.com'


    def CreateBindInstance(self, request):
        """将應用和資源進行綁定

        :param request: 調用CreateBindInstance所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateBindInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateBindInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBindInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBindInstanceResponse()
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


    def CreateCosSecKeyInstance(self, request):
        """獲取雲COS文件儲存臨時金鑰，金鑰僅限于臨時上傳文件，有訪問限制和時效性。

        :param request: 調用CreateCosSecKeyInstance所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateCosSecKeyInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateCosSecKeyInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCosSecKeyInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCosSecKeyInstanceResponse()
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


    def CreateResourceInstances(self, request):
        """用戶可以使用該介面自建資源，只支援白名單用戶

        :param request: 調用CreateResourceInstances所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateResourceInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateResourceInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateResourceInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateResourceInstancesResponse()
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


    def CreateScanInstances(self, request):
        """用戶通過該介面批次提交應用進行應用掃描，掃描後需通過DescribeScanResults介面查詢掃描結果

        :param request: 調用CreateScanInstances所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateScanInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateScanInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScanInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScanInstancesResponse()
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


    def CreateShieldInstance(self, request):
        """用戶通過該介面提交應用進行應用加固，加固後需通過DescribeShieldResult介面查詢加固結果

        :param request: 調用CreateShieldInstance所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateShieldInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateShieldInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateShieldInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateShieldInstanceResponse()
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


    def CreateShieldPlanInstance(self, request):
        """對資源進行策略新增

        :param request: 調用CreateShieldPlanInstance所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.CreateShieldPlanInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.CreateShieldPlanInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateShieldPlanInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateShieldPlanInstanceResponse()
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


    def DeleteScanInstances(self, request):
        """删除一個或者多個app掃描訊息

        :param request: 調用DeleteScanInstances所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.DeleteScanInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DeleteScanInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScanInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScanInstancesResponse()
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


    def DeleteShieldInstances(self, request):
        """删除一個或者多個app加固訊息

        :param request: 調用DeleteShieldInstances所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.DeleteShieldInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DeleteShieldInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteShieldInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteShieldInstancesResponse()
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


    def DescribeResourceInstances(self, request):
        """獲取某個用戶的所有資源訊息

        :param request: 調用DescribeResourceInstances所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeResourceInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeResourceInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceInstancesResponse()
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


    def DescribeScanInstances(self, request):
        """本介面用于檢視app清單。
        可以通過指定任務唯一标識ItemId來查詢指定app的詳細訊息，或通過設定過濾器來查詢滿足過濾條件的app的詳細訊息。 指定偏移(Offset)和限制(Limit)來選擇結果中的一部分，預設返回滿足條件的前20個app訊息。

        :param request: 調用DescribeScanInstances所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeScanInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeScanInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScanInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanInstancesResponse()
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


    def DescribeScanResults(self, request):
        """用戶通過CreateScanInstances介面提交應用進行風險批次掃描後，用此介面批次獲取風險詳細訊息,包含漏洞訊息，廣告訊息，插件訊息和病毒訊息

        :param request: 調用DescribeScanResults所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeScanResultsRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeScanResultsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScanResults", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanResultsResponse()
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


    def DescribeShieldInstances(self, request):
        """本介面用于檢視app清單。
        可以通過指定任務唯一标識ItemId來查詢指定app的詳細訊息，或通過設定過濾器來查詢滿足過濾條件的app的詳細訊息。 指定偏移(Offset)和限制(Limit)來選擇結果中的一部分，預設返回滿足條件的前20個app訊息。

        :param request: 調用DescribeShieldInstances所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeShieldInstancesRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeShieldInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShieldInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShieldInstancesResponse()
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


    def DescribeShieldPlanInstance(self, request):
        """查詢加固策略

        :param request: 調用DescribeShieldPlanInstance所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeShieldPlanInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeShieldPlanInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShieldPlanInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShieldPlanInstanceResponse()
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


    def DescribeShieldResult(self, request):
        """通過唯一标識獲取加固的結果

        :param request: 調用DescribeShieldResult所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeShieldResultRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeShieldResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShieldResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShieldResultResponse()
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


    def DescribeUserBaseInfoInstance(self, request):
        """獲取用戶基礎訊息

        :param request: 調用DescribeUserBaseInfoInstance所需參數的結構體。
        :type request: :class:`tencentcloud.ms.v20180408.models.DescribeUserBaseInfoInstanceRequest`
        :rtype: :class:`tencentcloud.ms.v20180408.models.DescribeUserBaseInfoInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserBaseInfoInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserBaseInfoInstanceResponse()
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