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
from taifucloudcloud.chdfs.v20190718 import models


class ChdfsClient(AbstractClient):
    _apiVersion = '2019-07-18'
    _endpoint = 'chdfs.taifucloudcloudapi.com'


    def CreateAccessGroup(self, request):
        """創建權限組。

        :param request: Request instance for CreateAccessGroup.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.CreateAccessGroupRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.CreateAccessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccessGroupResponse()
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


    def CreateAccessRules(self, request):
        """批次創建權限規則，權限規則ID和創建時間無需填寫。

        :param request: Request instance for CreateAccessRules.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.CreateAccessRulesRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.CreateAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccessRulesResponse()
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


    def CreateFileSystem(self, request):
        """創建文件系統（異步）。

        :param request: Request instance for CreateFileSystem.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.CreateFileSystemRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.CreateFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFileSystemResponse()
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


    def CreateMountPoint(self, request):
        """創建文件系統掛載點，僅限於創建成功的文件系統。

        :param request: Request instance for CreateMountPoint.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.CreateMountPointRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.CreateMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMountPointResponse()
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


    def DeleteAccessGroup(self, request):
        """删除權限組。

        :param request: Request instance for DeleteAccessGroup.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.DeleteAccessGroupRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.DeleteAccessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccessGroupResponse()
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


    def DeleteAccessRules(self, request):
        """批次删除權限規則。

        :param request: Request instance for DeleteAccessRules.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.DeleteAccessRulesRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.DeleteAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccessRulesResponse()
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


    def DeleteFileSystem(self, request):
        """删除文件系統，不允許删除非空文件系統。

        :param request: Request instance for DeleteFileSystem.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.DeleteFileSystemRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.DeleteFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFileSystemResponse()
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


    def DeleteMountPoint(self, request):
        """删除掛載點。

        :param request: Request instance for DeleteMountPoint.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.DeleteMountPointRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.DeleteMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMountPointResponse()
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


    def DescribeAccessGroups(self, request):
        """檢視權限組清單。

        :param request: Request instance for DescribeAccessGroups.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeAccessGroupsRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeAccessGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessGroupsResponse()
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


    def DescribeAccessRules(self, request):
        """通過權限組ID檢視權限規則清單。

        :param request: Request instance for DescribeAccessRules.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeAccessRulesRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessRulesResponse()
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


    def DescribeFileSystem(self, request):
        """檢視文件系統詳細訊息。

        :param request: Request instance for DescribeFileSystem.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeFileSystemRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileSystemResponse()
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


    def DescribeFileSystems(self, request):
        """檢視文件系統清單。

        :param request: Request instance for DescribeFileSystems.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeFileSystemsRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeFileSystemsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileSystems", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileSystemsResponse()
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


    def DescribeMountPoint(self, request):
        """檢視掛載點詳細訊息。

        :param request: Request instance for DescribeMountPoint.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeMountPointRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMountPointResponse()
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


    def DescribeMountPoints(self, request):
        """通過文件系統ID或者權限組ID檢視掛載點清單。

        :param request: Request instance for DescribeMountPoints.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeMountPointsRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.DescribeMountPointsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMountPoints", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMountPointsResponse()
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


    def ModifyAccessGroup(self, request):
        """修改權限組屬性。

        :param request: Request instance for ModifyAccessGroup.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.ModifyAccessGroupRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.ModifyAccessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessGroupResponse()
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


    def ModifyAccessRules(self, request):
        """批次修改權限規則屬性，需要指定權限規則ID。

        :param request: Request instance for ModifyAccessRules.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.ModifyAccessRulesRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.ModifyAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessRulesResponse()
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


    def ModifyFileSystem(self, request):
        """修改文件系統屬性，僅限於創建成功的文件系統。

        :param request: Request instance for ModifyFileSystem.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.ModifyFileSystemRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.ModifyFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyFileSystemResponse()
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


    def ModifyMountPoint(self, request):
        """修改掛載點屬性。

        :param request: Request instance for ModifyMountPoint.
        :type request: :class:`taifucloudcloud.chdfs.v20190718.models.ModifyMountPointRequest`
        :rtype: :class:`taifucloudcloud.chdfs.v20190718.models.ModifyMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMountPointResponse()
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