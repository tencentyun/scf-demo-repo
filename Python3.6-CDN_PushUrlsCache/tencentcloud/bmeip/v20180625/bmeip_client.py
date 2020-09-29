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
from taifucloudcloud.bmeip.v20180625 import models


class BmeipClient(AbstractClient):
    _apiVersion = '2018-06-25'
    _endpoint = 'bmeip.taifucloudcloudapi.com'


    def BindEipAcls(self, request):
        """此介面用於爲某個 EIP 關聯 ACL。

        :param request: Request instance for BindEipAcls.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.BindEipAclsRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.BindEipAclsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindEipAcls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindEipAclsResponse()
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


    def BindHosted(self, request):
        """BindHosted介面用於綁定黑石彈性公網IP到黑石托管機器上

        :param request: Request instance for BindHosted.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.BindHostedRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.BindHostedResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindHosted", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindHostedResponse()
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


    def BindRs(self, request):
        """綁定黑石EIP

        :param request: Request instance for BindRs.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.BindRsRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.BindRsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindRs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindRsResponse()
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


    def BindVpcIp(self, request):
        """黑石EIP綁定VPCIP

        :param request: Request instance for BindVpcIp.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.BindVpcIpRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.BindVpcIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindVpcIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindVpcIpResponse()
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


    def CreateEip(self, request):
        """創建黑石彈性公網IP

        :param request: Request instance for CreateEip.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.CreateEipRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.CreateEipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEipResponse()
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


    def CreateEipAcl(self, request):
        """創建黑石彈性公網 EIPACL

        :param request: Request instance for CreateEipAcl.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.CreateEipAclRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.CreateEipAclResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEipAcl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEipAclResponse()
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


    def DeleteEip(self, request):
        """釋放黑石彈性公網IP

        :param request: Request instance for DeleteEip.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.DeleteEipRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.DeleteEipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEipResponse()
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


    def DeleteEipAcl(self, request):
        """删除彈性公網IP ACL

        :param request: Request instance for DeleteEipAcl.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.DeleteEipAclRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.DeleteEipAclResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEipAcl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEipAclResponse()
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


    def DescribeEipAcls(self, request):
        """查詢彈性公網IP ACL

        :param request: Request instance for DescribeEipAcls.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.DescribeEipAclsRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.DescribeEipAclsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEipAcls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEipAclsResponse()
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


    def DescribeEipQuota(self, request):
        """查詢黑石EIP 限額

        :param request: Request instance for DescribeEipQuota.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.DescribeEipQuotaRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.DescribeEipQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEipQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEipQuotaResponse()
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


    def DescribeEipTask(self, request):
        """黑石EIP查詢任務狀态

        :param request: Request instance for DescribeEipTask.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.DescribeEipTaskRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.DescribeEipTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEipTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEipTaskResponse()
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


    def DescribeEips(self, request):
        """黑石EIP查詢介面

        :param request: Request instance for DescribeEips.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.DescribeEipsRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.DescribeEipsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEips", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEipsResponse()
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


    def ModifyEipAcl(self, request):
        """修改彈性公網IP ACL

        :param request: Request instance for ModifyEipAcl.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.ModifyEipAclRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.ModifyEipAclResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyEipAcl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEipAclResponse()
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


    def ModifyEipCharge(self, request):
        """黑石EIP修改計費方式

        :param request: Request instance for ModifyEipCharge.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.ModifyEipChargeRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.ModifyEipChargeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyEipCharge", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEipChargeResponse()
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


    def ModifyEipName(self, request):
        """更新黑石EIP名稱

        :param request: Request instance for ModifyEipName.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.ModifyEipNameRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.ModifyEipNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyEipName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEipNameResponse()
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


    def UnbindEipAcls(self, request):
        """解綁彈性公網IP ACL

        :param request: Request instance for UnbindEipAcls.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.UnbindEipAclsRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.UnbindEipAclsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindEipAcls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindEipAclsResponse()
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


    def UnbindHosted(self, request):
        """UnbindHosted介面用於解綁托管機器上的EIP

        :param request: Request instance for UnbindHosted.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.UnbindHostedRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.UnbindHostedResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindHosted", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindHostedResponse()
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


    def UnbindRs(self, request):
        """解綁黑石EIP

        :param request: Request instance for UnbindRs.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.UnbindRsRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.UnbindRsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindRs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindRsResponse()
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


    def UnbindRsList(self, request):
        """批次解綁物理機彈性公網IP介面

        :param request: Request instance for UnbindRsList.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.UnbindRsListRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.UnbindRsListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindRsList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindRsListResponse()
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


    def UnbindVpcIp(self, request):
        """黑石EIP解綁VPCIP

        :param request: Request instance for UnbindVpcIp.
        :type request: :class:`taifucloudcloud.bmeip.v20180625.models.UnbindVpcIpRequest`
        :rtype: :class:`taifucloudcloud.bmeip.v20180625.models.UnbindVpcIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindVpcIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindVpcIpResponse()
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