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
from tencentcloud.bda.v20200324 import models


class BdaClient(AbstractClient):
    _apiVersion = '2020-03-24'
    _endpoint = 'bda.tencentcloudapi.com'


    def CreateGroup(self, request):
        """用于創建一個空的人體庫，如果人體庫已存在返回錯誤。

        1個APPID下最多有2000W個人體軌迹（Trace），最多1W個人體庫（Group）。

        單個人體庫（Group）最多10W個人體軌迹（Trace）。

        單個人員（Person）最多添加 5 個人體軌迹（Trace）。

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.bda.v20200324.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.CreateGroupResponse`

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


    def CreatePerson(self, request):
        """創建人員，添加對應人員的人體軌迹訊息。

        請注意：
        - 我們希望您的輸入爲 嚴格符合軌迹圖片 要求的圖片。如果您輸入的圖片不符合軌迹圖片要求，會對最終效果産生較大負面影響。請您盡量保證一個Trace中的圖片人體清晰、無遮擋、連貫；
        - 一個人體軌迹（Trace）可以包含1-5張人體圖片。提供越多質量高的人體圖片有助于提升最終識别結果；
        - 無論您在單個Trace中提供了多少張人體圖片，我們都将生成一個對應的軌迹（Trace）訊息。即，Trace僅和本次輸入的圖片序列相關，和圖片的個數無關；
        - 輸入的圖片組中，若有部分圖片輸入不合法（如圖片大小過大、分辨率過大、無法解碼等），我們将舍棄這部分圖片，确保合法圖片被正确搜索。即，我們将盡可能保證請求成功，去除不合法的輸入；
        - 構成人體軌迹單張圖片大小不得超過2M，分辨率不得超過1920*1080。

        :param request: Request instance for CreatePerson.
        :type request: :class:`tencentcloud.bda.v20200324.models.CreatePersonRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.CreatePersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePersonResponse()
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


    def CreateTrace(self, request):
        """将一個人體軌迹添加到一個人員中。一個人員最多允許包含 5 個人體軌迹。同一人的人體軌迹越多，搜索識别效果越好。

        >請注意：
        - 我們希望您的輸入爲 嚴格符合軌迹圖片 要求的圖片。如果您輸入的圖片不符合軌迹圖片要求，會對最終效果産生較大負面影響。請您盡量保證一個Trace中的圖片人體清晰、無遮擋、連貫。
        - 一個人體軌迹（Trace）可以包含1-5張人體圖片。提供越多質量高的人體圖片有助于提升最終識别結果。
        - 無論您在單個Trace中提供了多少張人體圖片，我們都将生成一個對應的軌迹（Trace）訊息。即，Trace僅和本次輸入的圖片序列相關，和圖片的個數無關。
        - 輸入的圖片組中，若有部分圖片輸入不合法（如圖片大小過大、分辨率過大、無法解碼等），我們将舍棄這部分圖片，确保合法圖片被正确搜索。即，我們将盡可能保證請求成功，去除不合法的輸入；
        - 構成人體軌迹單張圖片大小限制爲2M，分辨率限制爲1920*1080。

        :param request: Request instance for CreateTrace.
        :type request: :class:`tencentcloud.bda.v20200324.models.CreateTraceRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.CreateTraceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTrace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTraceResponse()
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
        """删除該人體庫及包含的所有的人員。

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.bda.v20200324.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.DeleteGroupResponse`

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


    def DeletePerson(self, request):
        """删除人員。

        :param request: Request instance for DeletePerson.
        :type request: :class:`tencentcloud.bda.v20200324.models.DeletePersonRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.DeletePersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePersonResponse()
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


    def DetectBody(self, request):
        """檢測給定圖片中的人體（Body）的位置訊息（屬性訊息将在後續開放）。

        :param request: Request instance for DetectBody.
        :type request: :class:`tencentcloud.bda.v20200324.models.DetectBodyRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.DetectBodyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectBody", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectBodyResponse()
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


    def GetGroupList(self, request):
        """獲取人體庫清單。

        :param request: Request instance for GetGroupList.
        :type request: :class:`tencentcloud.bda.v20200324.models.GetGroupListRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.GetGroupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetGroupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetGroupListResponse()
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


    def GetPersonList(self, request):
        """獲取指定人體庫中的人員清單。

        :param request: Request instance for GetPersonList.
        :type request: :class:`tencentcloud.bda.v20200324.models.GetPersonListRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.GetPersonListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPersonList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPersonListResponse()
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


    def ModifyGroup(self, request):
        """修改人體庫名稱、備注。

        :param request: Request instance for ModifyGroup.
        :type request: :class:`tencentcloud.bda.v20200324.models.ModifyGroupRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.ModifyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyGroupResponse()
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


    def ModifyPersonInfo(self, request):
        """修改人員訊息。

        :param request: Request instance for ModifyPersonInfo.
        :type request: :class:`tencentcloud.bda.v20200324.models.ModifyPersonInfoRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.ModifyPersonInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonInfoResponse()
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


    def SearchTrace(self, request):
        """本介面用于對一組待識别的人體軌迹（Trace）圖片，在人體庫中識别出最相似的 TopK 人體，按照相似度從大到小排列。

        人體軌迹（Trace）圖片要求：圖片中當且僅包含一個人體。人體完整、無遮擋。

        > 請注意：
        - 我們希望您的輸入爲嚴格符合軌迹圖片要求的圖片。如果您輸入的圖片不符合軌迹圖片要求，會對最終效果産生較大負面影響；
        - 人體軌迹，是一個包含1-5張圖片的圖片序列。您可以輸入1張圖片作爲軌迹，也可以輸入多張。單個軌迹中包含越多符合質量的圖片，搜索效果越好。
        - 構成人體軌迹單張圖片大小不得超過2M，分辨率不得超過1920*1080。

        :param request: Request instance for SearchTrace.
        :type request: :class:`tencentcloud.bda.v20200324.models.SearchTraceRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.SearchTraceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchTrace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchTraceResponse()
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


    def SegmentPortraitPic(self, request):
        """識别傳入圖片中人體的完整輪廓，進行摳像。

        :param request: Request instance for SegmentPortraitPic.
        :type request: :class:`tencentcloud.bda.v20200324.models.SegmentPortraitPicRequest`
        :rtype: :class:`tencentcloud.bda.v20200324.models.SegmentPortraitPicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SegmentPortraitPic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SegmentPortraitPicResponse()
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