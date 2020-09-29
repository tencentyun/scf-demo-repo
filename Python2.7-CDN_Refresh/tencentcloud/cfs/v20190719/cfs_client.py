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
from taifucloudcloud.cfs.v20190719 import models


class CfsClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'cfs.taifucloudcloudapi.com'


    def CreateCfsFileSystem(self, request):
        """用於添加新文件系統

        :param request: Request instance for CreateCfsFileSystem.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.CreateCfsFileSystemRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.CreateCfsFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCfsFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCfsFileSystemResponse()
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


    def CreateCfsPGroup(self, request):
        """本介面（CreateCfsPGroup）用於創建權限組

        :param request: Request instance for CreateCfsPGroup.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.CreateCfsPGroupRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.CreateCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCfsPGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCfsPGroupResponse()
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


    def CreateCfsRule(self, request):
        """本介面（CreateCfsRule）用於創建權限組規則。

        :param request: Request instance for CreateCfsRule.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.CreateCfsRuleRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.CreateCfsRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCfsRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCfsRuleResponse()
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


    def DeleteCfsFileSystem(self, request):
        """用於删除文件系統

        :param request: Request instance for DeleteCfsFileSystem.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.DeleteCfsFileSystemRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.DeleteCfsFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCfsFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCfsFileSystemResponse()
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


    def DeleteCfsPGroup(self, request):
        """本介面（DeleteCfsPGroup）用於删除權限組。

        :param request: Request instance for DeleteCfsPGroup.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.DeleteCfsPGroupRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.DeleteCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCfsPGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCfsPGroupResponse()
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


    def DeleteCfsRule(self, request):
        """本介面（DeleteCfsRule）用於删除權限組規則。

        :param request: Request instance for DeleteCfsRule.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.DeleteCfsRuleRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.DeleteCfsRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCfsRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCfsRuleResponse()
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


    def DeleteMountTarget(self, request):
        """本介面（DeleteMountTarget）用於删除掛載點

        :param request: Request instance for DeleteMountTarget.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.DeleteMountTargetRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.DeleteMountTargetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMountTarget", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMountTargetResponse()
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


    def DescribeAvailableZoneInfo(self, request):
        """本介面（DescribeAvailableZoneInfo）用於查詢區域的可用情況。

        :param request: Request instance for DescribeAvailableZoneInfo.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.DescribeAvailableZoneInfoRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.DescribeAvailableZoneInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAvailableZoneInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailableZoneInfoResponse()
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


    def DescribeCfsFileSystems(self, request):
        """本介面（DescribeCfsFileSystems）用於查詢文件系統

        :param request: Request instance for DescribeCfsFileSystems.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.DescribeCfsFileSystemsRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.DescribeCfsFileSystemsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCfsFileSystems", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsFileSystemsResponse()
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


    def DescribeCfsPGroups(self, request):
        """本介面（DescribeCfsPGroups）用於查詢權限組清單。

        :param request: Request instance for DescribeCfsPGroups.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.DescribeCfsPGroupsRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.DescribeCfsPGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCfsPGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsPGroupsResponse()
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


    def DescribeCfsRules(self, request):
        """本介面（DescribeCfsRules）用於查詢權限組規則清單。

        :param request: Request instance for DescribeCfsRules.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.DescribeCfsRulesRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.DescribeCfsRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCfsRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsRulesResponse()
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


    def DescribeCfsServiceStatus(self, request):
        """本介面（DescribeCfsServiceStatus）用於查詢用戶使用CFS的服務狀态。

        :param request: Request instance for DescribeCfsServiceStatus.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.DescribeCfsServiceStatusRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.DescribeCfsServiceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCfsServiceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCfsServiceStatusResponse()
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


    def DescribeMountTargets(self, request):
        """本介面（DescribeMountTargets）用於查詢文件系統掛載點訊息

        :param request: Request instance for DescribeMountTargets.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.DescribeMountTargetsRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.DescribeMountTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMountTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMountTargetsResponse()
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


    def SignUpCfsService(self, request):
        """本介面（SignUpCfsService）用於開通CFS服務。

        :param request: Request instance for SignUpCfsService.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.SignUpCfsServiceRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.SignUpCfsServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SignUpCfsService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SignUpCfsServiceResponse()
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


    def UpdateCfsFileSystemName(self, request):
        """本介面（UpdateCfsFileSystemName）用於更新文件系統名

        :param request: Request instance for UpdateCfsFileSystemName.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.UpdateCfsFileSystemNameRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.UpdateCfsFileSystemNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCfsFileSystemName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsFileSystemNameResponse()
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


    def UpdateCfsFileSystemPGroup(self, request):
        """本介面（UpdateCfsFileSystemPGroup）用於更新文件系統所使用的權限組

        :param request: Request instance for UpdateCfsFileSystemPGroup.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.UpdateCfsFileSystemPGroupRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.UpdateCfsFileSystemPGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCfsFileSystemPGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsFileSystemPGroupResponse()
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


    def UpdateCfsFileSystemSizeLimit(self, request):
        """本介面（UpdateCfsFileSystemSizeLimit）用於更新文件系統儲存容量限制。

        :param request: Request instance for UpdateCfsFileSystemSizeLimit.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.UpdateCfsFileSystemSizeLimitRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.UpdateCfsFileSystemSizeLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCfsFileSystemSizeLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsFileSystemSizeLimitResponse()
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


    def UpdateCfsPGroup(self, request):
        """本介面（UpdateCfsPGroup）更新權限組訊息。

        :param request: Request instance for UpdateCfsPGroup.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.UpdateCfsPGroupRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.UpdateCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCfsPGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsPGroupResponse()
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


    def UpdateCfsRule(self, request):
        """本介面（UpdateCfsRule）用於更新權限規則。

        :param request: Request instance for UpdateCfsRule.
        :type request: :class:`taifucloudcloud.cfs.v20190719.models.UpdateCfsRuleRequest`
        :rtype: :class:`taifucloudcloud.cfs.v20190719.models.UpdateCfsRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateCfsRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCfsRuleResponse()
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