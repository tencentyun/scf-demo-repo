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
from taifucloudcloud.cam.v20190116 import models


class CamClient(AbstractClient):
    _apiVersion = '2019-01-16'
    _endpoint = 'cam.taifucloudcloudapi.com'


    def AddUser(self, request):
        """添加子用戶

        :param request: 調用AddUser所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.AddUserRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.AddUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUserResponse()
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


    def AddUserToGroup(self, request):
        """用戶加入到用戶組

        :param request: 調用AddUserToGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.AddUserToGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.AddUserToGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddUserToGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUserToGroupResponse()
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


    def AttachGroupPolicy(self, request):
        """本介面（AttachGroupPolicy）可用於綁定策略到用戶組。

        :param request: 調用AttachGroupPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.AttachGroupPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.AttachGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachGroupPolicyResponse()
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


    def AttachUserPolicy(self, request):
        """本介面（AttachUserPolicy）可用於綁定到用戶的策略。

        :param request: 調用AttachUserPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.AttachUserPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.AttachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachUserPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachUserPolicyResponse()
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
        """創建用戶組

        :param request: 調用CreateGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.CreateGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.CreateGroupResponse`

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


    def CreatePolicy(self, request):
        """本介面（CreatePolicy）可用於創建策略。

        :param request: 調用CreatePolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.CreatePolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.CreatePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePolicyResponse()
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


    def CreateSAMLProvider(self, request):
        """創建SAML身份提供商

        :param request: 調用CreateSAMLProvider所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.CreateSAMLProviderRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.CreateSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSAMLProviderResponse()
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
        """删除用戶組

        :param request: 調用DeleteGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeleteGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeleteGroupResponse`

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


    def DeletePolicy(self, request):
        """本介面（DeletePolicy）可用於删除策略。

        :param request: 調用DeletePolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeletePolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeletePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePolicyResponse()
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


    def DeleteSAMLProvider(self, request):
        """删除SAML身份提供商

        :param request: 調用DeleteSAMLProvider所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeleteSAMLProviderRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeleteSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSAMLProviderResponse()
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


    def DeleteUser(self, request):
        """删除子用戶

        :param request: 調用DeleteUser所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DeleteUserRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserResponse()
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


    def DetachGroupPolicy(self, request):
        """本介面（DetachGroupPolicy）可用於解除綁定到用戶組的策略。

        :param request: 調用DetachGroupPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DetachGroupPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DetachGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachGroupPolicyResponse()
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


    def DetachUserPolicy(self, request):
        """本介面（DetachUserPolicy）可用於解除綁定到用戶的策略。

        :param request: 調用DetachUserPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.DetachUserPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.DetachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachUserPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachUserPolicyResponse()
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


    def GetGroup(self, request):
        """查詢用戶組詳情

        :param request: 調用GetGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetGroupResponse()
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


    def GetPolicy(self, request):
        """本介面（GetPolicy）可用於查詢檢視策略詳情。

        :param request: 調用GetPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPolicyResponse()
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


    def GetSAMLProvider(self, request):
        """查詢SAML身份提供商詳情

        :param request: 調用GetSAMLProvider所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetSAMLProviderRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSAMLProviderResponse()
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


    def GetUser(self, request):
        """查詢子用戶

        :param request: 調用GetUser所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.GetUserRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.GetUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUserResponse()
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


    def ListAttachedGroupPolicies(self, request):
        """本介面（ListAttachedGroupPolicies）可用於查詢用戶組關聯的策略清單。

        :param request: 調用ListAttachedGroupPolicies所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListAttachedGroupPoliciesRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListAttachedGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAttachedGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedGroupPoliciesResponse()
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


    def ListAttachedUserPolicies(self, request):
        """本介面（ListAttachedUserPolicies）可用於查詢子賬號關聯的策略清單。

        :param request: 調用ListAttachedUserPolicies所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListAttachedUserPoliciesRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListAttachedUserPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAttachedUserPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAttachedUserPoliciesResponse()
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


    def ListEntitiesForPolicy(self, request):
        """本介面（ListEntitiesForPolicy）可用於查詢策略關聯的實體清單。

        :param request: 調用ListEntitiesForPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListEntitiesForPolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListEntitiesForPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEntitiesForPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEntitiesForPolicyResponse()
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


    def ListGroups(self, request):
        """查詢用戶組清單

        :param request: 調用ListGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListGroupsRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListGroupsResponse()
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


    def ListGroupsForUser(self, request):
        """列出用戶關聯的用戶組

        :param request: 調用ListGroupsForUser所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListGroupsForUserRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListGroupsForUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListGroupsForUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListGroupsForUserResponse()
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


    def ListPolicies(self, request):
        """本介面（ListPolicies）可用於查詢策略清單

        :param request: 調用ListPolicies所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListPoliciesRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListPoliciesResponse()
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


    def ListSAMLProviders(self, request):
        """查詢SAML身份提供商清單

        :param request: 調用ListSAMLProviders所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListSAMLProvidersRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListSAMLProvidersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSAMLProviders", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSAMLProvidersResponse()
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


    def ListUsers(self, request):
        """拉取子用戶

        :param request: 調用ListUsers所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListUsersRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListUsersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListUsers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUsersResponse()
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


    def ListUsersForGroup(self, request):
        """查詢用戶組關聯的用戶清單

        :param request: 調用ListUsersForGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.ListUsersForGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.ListUsersForGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListUsersForGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListUsersForGroupResponse()
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


    def RemoveUserFromGroup(self, request):
        """從用戶組删除用戶

        :param request: 調用RemoveUserFromGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.RemoveUserFromGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.RemoveUserFromGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveUserFromGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveUserFromGroupResponse()
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


    def UpdateGroup(self, request):
        """更新用戶組

        :param request: 調用UpdateGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdateGroupRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGroupResponse()
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


    def UpdatePolicy(self, request):
        """本介面（UpdatePolicy ）可用於更新策略。

        :param request: 調用UpdatePolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdatePolicyRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdatePolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdatePolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePolicyResponse()
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


    def UpdateSAMLProvider(self, request):
        """更新SAML身份提供商訊息

        :param request: 調用UpdateSAMLProvider所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdateSAMLProviderRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdateSAMLProviderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateSAMLProvider", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateSAMLProviderResponse()
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


    def UpdateUser(self, request):
        """更新子用戶

        :param request: 調用UpdateUser所需參數的結構體。
        :type request: :class:`taifucloudcloud.cam.v20190116.models.UpdateUserRequest`
        :rtype: :class:`taifucloudcloud.cam.v20190116.models.UpdateUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateUserResponse()
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