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
from taifucloudcloud.tag.v20180813 import models


class TagClient(AbstractClient):
    _apiVersion = '2018-08-13'
    _endpoint = 'tag.taifucloudcloudapi.com'


    def AddResourceTag(self, request):
        """本介面用于給标簽關聯資源

        :param request: Request instance for AddResourceTag.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.AddResourceTagRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.AddResourceTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddResourceTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddResourceTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTag(self, request):
        """本介面用于創建一對标簽鍵和标簽值

        :param request: Request instance for CreateTag.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.CreateTagRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.CreateTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteResourceTag(self, request):
        """本介面用于解除标簽和資源的關聯關系

        :param request: Request instance for DeleteResourceTag.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.DeleteResourceTagRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.DeleteResourceTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteResourceTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteResourceTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTag(self, request):
        """本介面用于删除一對标簽鍵和标簽值

        :param request: Request instance for DeleteTag.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.DeleteTagRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.DeleteTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceTags(self, request):
        """查詢資源關聯标簽

        :param request: Request instance for DescribeResourceTags.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.DescribeResourceTagsRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.DescribeResourceTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceTagsByResourceIds(self, request):
        """用于查詢已有資源标簽鍵值對

        :param request: Request instance for DescribeResourceTagsByResourceIds.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTagsByResourceIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTagsByResourceIdsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceTagsByTagKeys(self, request):
        """根據标簽鍵獲取資源标簽

        :param request: Request instance for DescribeResourceTagsByTagKeys.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.DescribeResourceTagsByTagKeysRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.DescribeResourceTagsByTagKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTagsByTagKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTagsByTagKeysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourcesByTags(self, request):
        """通過标簽查詢資源清單

        :param request: Request instance for DescribeResourcesByTags.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.DescribeResourcesByTagsRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.DescribeResourcesByTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourcesByTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourcesByTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTagKeys(self, request):
        """用于查詢已建立的标簽清單中的标簽鍵。

        :param request: Request instance for DescribeTagKeys.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.DescribeTagKeysRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.DescribeTagKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagKeysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTagValues(self, request):
        """用于查詢已建立的标簽清單中的标簽值。

        :param request: Request instance for DescribeTagValues.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.DescribeTagValuesRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.DescribeTagValuesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagValues", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagValuesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTags(self, request):
        """用于查詢已建立的标簽清單。

        :param request: Request instance for DescribeTags.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.DescribeTagsRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyResourceTags(self, request):
        """本介面用于修改資源關聯的所有标簽

        :param request: Request instance for ModifyResourceTags.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.ModifyResourceTagsRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.ModifyResourceTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyResourceTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyResourceTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateResourceTagValue(self, request):
        """本介面用于修改資源已關聯的标簽值（标簽鍵不變）

        :param request: Request instance for UpdateResourceTagValue.
        :type request: :class:`taifucloudcloud.tag.v20180813.models.UpdateResourceTagValueRequest`
        :rtype: :class:`taifucloudcloud.tag.v20180813.models.UpdateResourceTagValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateResourceTagValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateResourceTagValueResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)