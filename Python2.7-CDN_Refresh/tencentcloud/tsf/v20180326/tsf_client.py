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
from taifucloudcloud.tsf.v20180326 import models


class TsfClient(AbstractClient):
    _apiVersion = '2018-03-26'
    _endpoint = 'tsf.taifucloudcloudapi.com'


    def AddClusterInstances(self, request):
        """添加雲主機節點至TSF集群

        :param request: Request instance for AddClusterInstances.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.AddClusterInstancesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.AddClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddClusterInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddClusterInstancesResponse()
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


    def AddInstances(self, request):
        """添加雲主機節點至TSF集群

        :param request: Request instance for AddInstances.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.AddInstancesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.AddInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddInstancesResponse()
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


    def CreateApplication(self, request):
        """創建應用

        :param request: Request instance for CreateApplication.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.CreateApplicationRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.CreateApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApplicationResponse()
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


    def CreateCluster(self, request):
        """創建集群

        :param request: Request instance for CreateCluster.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.CreateClusterRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterResponse()
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


    def CreateConfig(self, request):
        """創建配置項

        :param request: Request instance for CreateConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.CreateConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.CreateConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateConfigResponse()
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


    def CreateContainGroup(self, request):
        """創建容器佈署組

        :param request: Request instance for CreateContainGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.CreateContainGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.CreateContainGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateContainGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateContainGroupResponse()
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


    def CreateGroup(self, request):
        """創建虛拟機佈署組

        :param request: Request instance for CreateGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.CreateGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGroupResponse()
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


    def CreateMicroservice(self, request):
        """新增微服務

        :param request: Request instance for CreateMicroservice.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.CreateMicroserviceRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.CreateMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMicroserviceResponse()
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


    def CreateNamespace(self, request):
        """創建命名空間

        :param request: Request instance for CreateNamespace.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.CreateNamespaceRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNamespaceResponse()
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


    def CreatePublicConfig(self, request):
        """創建公共配置項

        :param request: Request instance for CreatePublicConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.CreatePublicConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.CreatePublicConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePublicConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePublicConfigResponse()
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


    def CreateServerlessGroup(self, request):
        """創建Serverless佈署組

        :param request: Request instance for CreateServerlessGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.CreateServerlessGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.CreateServerlessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServerlessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServerlessGroupResponse()
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


    def DeleteApplication(self, request):
        """删除應用

        :param request: Request instance for DeleteApplication.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeleteApplicationRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeleteApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApplicationResponse()
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


    def DeleteConfig(self, request):
        """删除配置項

        :param request: Request instance for DeleteConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeleteConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeleteConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteConfigResponse()
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


    def DeleteContainerGroup(self, request):
        """删除容器佈署組

        :param request: Request instance for DeleteContainerGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeleteContainerGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeleteContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteContainerGroupResponse()
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


    def DeleteGroup(self, request):
        """删除容器佈署組

        :param request: Request instance for DeleteGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeleteGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGroupResponse()
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


    def DeleteImageTags(self, request):
        """批次删除映像版本

        :param request: Request instance for DeleteImageTags.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeleteImageTagsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeleteImageTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImageTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImageTagsResponse()
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


    def DeleteMicroservice(self, request):
        """删除微服務

        :param request: Request instance for DeleteMicroservice.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeleteMicroserviceRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeleteMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMicroserviceResponse()
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


    def DeleteNamespace(self, request):
        """删除命名空間

        :param request: Request instance for DeleteNamespace.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeleteNamespaceRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeleteNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNamespaceResponse()
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


    def DeletePkgs(self, request):
        """從軟體倉庫批次删除程式包。
        一次最多支援删除1000個包，數量超過1000，返回UpperDeleteLimit錯誤。

        :param request: Request instance for DeletePkgs.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeletePkgsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeletePkgsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePkgs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePkgsResponse()
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


    def DeletePublicConfig(self, request):
        """删除公共配置項

        :param request: Request instance for DeletePublicConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeletePublicConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeletePublicConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePublicConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePublicConfigResponse()
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


    def DeleteServerlessGroup(self, request):
        """删除Serverless佈署組

        :param request: Request instance for DeleteServerlessGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeleteServerlessGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeleteServerlessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServerlessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServerlessGroupResponse()
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


    def DeployContainerGroup(self, request):
        """佈署容器應用

        :param request: Request instance for DeployContainerGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeployContainerGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeployContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeployContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployContainerGroupResponse()
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


    def DeployGroup(self, request):
        """佈署虛拟機佈署組應用

        :param request: Request instance for DeployGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeployGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeployGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeployGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployGroupResponse()
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


    def DeployServerlessGroup(self, request):
        """佈署Serverless應用

        :param request: Request instance for DeployServerlessGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DeployServerlessGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DeployServerlessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeployServerlessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployServerlessGroupResponse()
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


    def DescribeApplication(self, request):
        """獲取應用詳情

        :param request: Request instance for DescribeApplication.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeApplicationRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationResponse()
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


    def DescribeApplicationAttribute(self, request):
        """獲取應用清單其它欄位，如實例數量訊息等

        :param request: Request instance for DescribeApplicationAttribute.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeApplicationAttributeRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeApplicationAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplicationAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationAttributeResponse()
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


    def DescribeApplications(self, request):
        """獲取應用清單

        :param request: Request instance for DescribeApplications.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeApplicationsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeApplicationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplications", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationsResponse()
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


    def DescribeClusterInstances(self, request):
        """查詢集群實例

        :param request: Request instance for DescribeClusterInstances.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeClusterInstancesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterInstancesResponse()
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


    def DescribeConfig(self, request):
        """查詢配置

        :param request: Request instance for DescribeConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigResponse()
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


    def DescribeConfigReleaseLogs(self, request):
        """查詢配置發布曆史

        :param request: Request instance for DescribeConfigReleaseLogs.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeConfigReleaseLogsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeConfigReleaseLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfigReleaseLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigReleaseLogsResponse()
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


    def DescribeConfigReleases(self, request):
        """查詢配置發布訊息

        :param request: Request instance for DescribeConfigReleases.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeConfigReleasesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeConfigReleasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfigReleases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigReleasesResponse()
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


    def DescribeConfigSummary(self, request):
        """查詢配置匯總清單

        :param request: Request instance for DescribeConfigSummary.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeConfigSummaryRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeConfigSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfigSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigSummaryResponse()
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


    def DescribeConfigs(self, request):
        """查詢配置項清單

        :param request: Request instance for DescribeConfigs.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeConfigsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigsResponse()
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


    def DescribeContainerGroupDetail(self, request):
        """容器佈署組詳情

        :param request: Request instance for DescribeContainerGroupDetail.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeContainerGroupDetailRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeContainerGroupDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerGroupDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerGroupDetailResponse()
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


    def DescribeContainerGroups(self, request):
        """容器佈署組清單

        :param request: Request instance for DescribeContainerGroups.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeContainerGroupsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeContainerGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerGroupsResponse()
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


    def DescribeDownloadInfo(self, request):
        """TSF上傳的程式包存放在Top Cloud 物件儲存（COS）中，通過該API可以獲取從COS下載程式包需要的訊息，包括包所在的桶、儲存路徑、鑒權訊息等，之後使用COS API（或SDK）進行下載。
        COS相關文件請查閱：https://cloud.taifucloud.com/document/product/436

        :param request: Request instance for DescribeDownloadInfo.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeDownloadInfoRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeDownloadInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDownloadInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDownloadInfoResponse()
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


    def DescribeGroup(self, request):
        """查詢虛拟機佈署組詳情

        :param request: Request instance for DescribeGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupResponse()
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


    def DescribeGroupInstances(self, request):
        """查詢虛拟機佈署組雲主機清單

        :param request: Request instance for DescribeGroupInstances.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeGroupInstancesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupInstancesResponse()
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


    def DescribeGroups(self, request):
        """獲取虛拟機佈署組清單

        :param request: Request instance for DescribeGroups.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeGroupsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupsResponse()
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


    def DescribeImageTags(self, request):
        """映像版本清單

        :param request: Request instance for DescribeImageTags.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeImageTagsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeImageTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageTagsResponse()
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


    def DescribeMicroservice(self, request):
        """查詢微服務詳情

        :param request: Request instance for DescribeMicroservice.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeMicroserviceRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMicroserviceResponse()
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


    def DescribeMicroservices(self, request):
        """獲取微服務清單

        :param request: Request instance for DescribeMicroservices.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeMicroservicesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeMicroservicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMicroservices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMicroservicesResponse()
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


    def DescribePkgs(self, request):
        """無

        :param request: Request instance for DescribePkgs.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribePkgsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribePkgsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePkgs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePkgsResponse()
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


    def DescribePodInstances(self, request):
        """獲取佈署組實例清單

        :param request: Request instance for DescribePodInstances.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribePodInstancesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribePodInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePodInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePodInstancesResponse()
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


    def DescribePublicConfig(self, request):
        """查詢公共配置（單條）

        :param request: Request instance for DescribePublicConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribePublicConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribePublicConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicConfigResponse()
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


    def DescribePublicConfigReleaseLogs(self, request):
        """查詢公共配置發布曆史

        :param request: Request instance for DescribePublicConfigReleaseLogs.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribePublicConfigReleaseLogsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribePublicConfigReleaseLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicConfigReleaseLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicConfigReleaseLogsResponse()
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


    def DescribePublicConfigReleases(self, request):
        """查詢公共配置發布訊息

        :param request: Request instance for DescribePublicConfigReleases.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribePublicConfigReleasesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribePublicConfigReleasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicConfigReleases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicConfigReleasesResponse()
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


    def DescribePublicConfigSummary(self, request):
        """查詢公共配置匯總清單

        :param request: Request instance for DescribePublicConfigSummary.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribePublicConfigSummaryRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribePublicConfigSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicConfigSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicConfigSummaryResponse()
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


    def DescribePublicConfigs(self, request):
        """查詢公共配置項清單

        :param request: Request instance for DescribePublicConfigs.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribePublicConfigsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribePublicConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicConfigsResponse()
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


    def DescribeReleasedConfig(self, request):
        """查詢group發布的配置

        :param request: Request instance for DescribeReleasedConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeReleasedConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeReleasedConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReleasedConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReleasedConfigResponse()
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


    def DescribeServerlessGroup(self, request):
        """查詢Serverless佈署組明細

        :param request: Request instance for DescribeServerlessGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeServerlessGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeServerlessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServerlessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServerlessGroupResponse()
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


    def DescribeServerlessGroups(self, request):
        """查詢Serverless佈署組清單

        :param request: Request instance for DescribeServerlessGroups.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeServerlessGroupsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeServerlessGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServerlessGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServerlessGroupsResponse()
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


    def DescribeSimpleApplications(self, request):
        """查詢簡單應用清單

        :param request: Request instance for DescribeSimpleApplications.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeSimpleApplicationsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeSimpleApplicationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleApplications", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleApplicationsResponse()
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


    def DescribeSimpleClusters(self, request):
        """查詢簡單集群清單

        :param request: Request instance for DescribeSimpleClusters.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeSimpleClustersRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeSimpleClustersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleClusters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleClustersResponse()
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


    def DescribeSimpleGroups(self, request):
        """查詢簡單佈署組清單

        :param request: Request instance for DescribeSimpleGroups.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeSimpleGroupsRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeSimpleGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleGroupsResponse()
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


    def DescribeSimpleNamespaces(self, request):
        """查詢簡單命名空間清單

        :param request: Request instance for DescribeSimpleNamespaces.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeSimpleNamespacesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeSimpleNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleNamespacesResponse()
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


    def DescribeUploadInfo(self, request):
        """TSF會将軟體包上傳到Top Cloud 物件儲存（COS）。調用此介面獲取上傳訊息，如目標地域，桶，包Id，儲存路徑，鑒權訊息等，之後請使用COS API（或SDK）進行上傳。
        COS相關文件請查閱：https://cloud.taifucloud.com/document/product/436

        :param request: Request instance for DescribeUploadInfo.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.DescribeUploadInfoRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.DescribeUploadInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUploadInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUploadInfoResponse()
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


    def ExpandGroup(self, request):
        """虛拟機佈署組添加實例

        :param request: Request instance for ExpandGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.ExpandGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.ExpandGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExpandGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExpandGroupResponse()
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


    def ModifyContainerGroup(self, request):
        """修改容器佈署組

        :param request: Request instance for ModifyContainerGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.ModifyContainerGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.ModifyContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyContainerGroupResponse()
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


    def ModifyContainerReplicas(self, request):
        """修改容器佈署組實例數

        :param request: Request instance for ModifyContainerReplicas.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.ModifyContainerReplicasRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.ModifyContainerReplicasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyContainerReplicas", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyContainerReplicasResponse()
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


    def ModifyMicroservice(self, request):
        """修改微服務詳情

        :param request: Request instance for ModifyMicroservice.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.ModifyMicroserviceRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.ModifyMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMicroserviceResponse()
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


    def ModifyUploadInfo(self, request):
        """調用該介面和COS的上傳介面後，需要調用此介面更新TSF中保存的程式包狀态。
        調用此介面完成後，才標志上傳包流程結束。

        :param request: Request instance for ModifyUploadInfo.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.ModifyUploadInfoRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.ModifyUploadInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyUploadInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUploadInfoResponse()
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


    def ReleaseConfig(self, request):
        """發布配置

        :param request: Request instance for ReleaseConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.ReleaseConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.ReleaseConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseConfigResponse()
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


    def ReleasePublicConfig(self, request):
        """發布公共配置

        :param request: Request instance for ReleasePublicConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.ReleasePublicConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.ReleasePublicConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleasePublicConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleasePublicConfigResponse()
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


    def RemoveInstances(self, request):
        """從 TSF 集群中批次移除雲主機節點

        :param request: Request instance for RemoveInstances.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.RemoveInstancesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.RemoveInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveInstancesResponse()
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


    def RevocationConfig(self, request):
        """撤回已發布的配置

        :param request: Request instance for RevocationConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.RevocationConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.RevocationConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevocationConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevocationConfigResponse()
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


    def RevocationPublicConfig(self, request):
        """撤回已發布的公共配置

        :param request: Request instance for RevocationPublicConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.RevocationPublicConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.RevocationPublicConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevocationPublicConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevocationPublicConfigResponse()
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


    def RollbackConfig(self, request):
        """回滾配置

        :param request: Request instance for RollbackConfig.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.RollbackConfigRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.RollbackConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RollbackConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RollbackConfigResponse()
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


    def ShrinkGroup(self, request):
        """下線佈署組所有機器實例

        :param request: Request instance for ShrinkGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.ShrinkGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.ShrinkGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ShrinkGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ShrinkGroupResponse()
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


    def ShrinkInstances(self, request):
        """虛拟機佈署組下線實例

        :param request: Request instance for ShrinkInstances.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.ShrinkInstancesRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.ShrinkInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ShrinkInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ShrinkInstancesResponse()
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


    def StartContainerGroup(self, request):
        """啓動容器佈署組

        :param request: Request instance for StartContainerGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.StartContainerGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.StartContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartContainerGroupResponse()
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


    def StartGroup(self, request):
        """啓動分組

        :param request: Request instance for StartGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.StartGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.StartGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartGroupResponse()
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


    def StopContainerGroup(self, request):
        """停止容器佈署組

        :param request: Request instance for StopContainerGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.StopContainerGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.StopContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopContainerGroupResponse()
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


    def StopGroup(self, request):
        """停止虛拟機佈署組

        :param request: Request instance for StopGroup.
        :type request: :class:`taifucloudcloud.tsf.v20180326.models.StopGroupRequest`
        :rtype: :class:`taifucloudcloud.tsf.v20180326.models.StopGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopGroupResponse()
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