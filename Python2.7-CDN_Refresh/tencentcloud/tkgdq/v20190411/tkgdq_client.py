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
from tencentcloud.tkgdq.v20190411 import models


class TkgdqClient(AbstractClient):
    _apiVersion = '2019-04-11'
    _endpoint = 'tkgdq.tencentcloudapi.com'


    def DescribeEntity(self, request):
        """輸入實體名稱，返回實體相關的訊息如實體别名、實體英文名、實體詳細訊息、相關實體等

        :param request: Request instance for DescribeEntity.
        :type request: :class:`tencentcloud.tkgdq.v20190411.models.DescribeEntityRequest`
        :rtype: :class:`tencentcloud.tkgdq.v20190411.models.DescribeEntityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEntity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEntityResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRelation(self, request):
        """輸入兩個實體，返回兩個實體間的關系，例如馬化騰與騰訊公司不僅是相關實體，二者還存在隸屬關系（馬化騰屬于騰訊公司）。

        :param request: Request instance for DescribeRelation.
        :type request: :class:`tencentcloud.tkgdq.v20190411.models.DescribeRelationRequest`
        :rtype: :class:`tencentcloud.tkgdq.v20190411.models.DescribeRelationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRelation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRelationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTriple(self, request):
        """三元組查詢，主要分爲兩類，SP查詢和PO查詢。SP查詢表示已知主語和謂語查詢賓語，PO查詢表示已知賓語和謂語查詢主語。每一個SP或PO查詢都是一個可獨立執行的查詢，TQL支援SP查詢的嵌套查詢，即主語可以是一個嵌套的子查詢。其他複雜的三元組查詢方法，請參考官網API文件範例。

        :param request: Request instance for DescribeTriple.
        :type request: :class:`tencentcloud.tkgdq.v20190411.models.DescribeTripleRequest`
        :rtype: :class:`tencentcloud.tkgdq.v20190411.models.DescribeTripleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTriple", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTripleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)