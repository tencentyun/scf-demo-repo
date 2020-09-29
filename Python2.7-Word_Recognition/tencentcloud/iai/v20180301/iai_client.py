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
from taifucloudcloud.iai.v20180301 import models


class IaiClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'iai.taifucloudcloudapi.com'


    def AnalyzeFace(self, request):
        """對請求圖片進行五官定位（也稱人臉關鍵點定位），計算構成人臉輪廓的 90 個點，包括眉毛（左右各 8 點）、眼睛（左右各 8 點）、鼻子（13 點）、嘴巴（22 點）、臉型輪廓（21 點）、眼珠[或瞳孔]（2點）。

        :param request: 調用AnalyzeFace所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.AnalyzeFaceRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.AnalyzeFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AnalyzeFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AnalyzeFaceResponse()
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


    def CompareFace(self, request):
        """對兩張圖片中的人臉進行相似度比對，返回人臉相似度分數。

        若您需要判斷 “此人是否是某人”，即驗證某張圖片中的人是否是已知身份的某人，如常見的人臉登入場景，建議使用[人臉驗證](https://cloud.taifucloud.com/document/product/867/32806)介面。

        若您需要判斷圖片中人臉的具體身份訊息，如是否是身份證上對應的人，建議使用[人臉核身·雲智慧眼](https://cloud.taifucloud.com/product/facein)産品。

        :param request: 調用CompareFace所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.CompareFaceRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.CompareFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompareFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompareFaceResponse()
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


    def CopyPerson(self, request):
        """将已存在於某人員庫的人員複制到其他人員庫，該人員的描述訊息不會被複制。單個人員最多只能同時存在100個人員庫中。

        :param request: 調用CopyPerson所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.CopyPersonRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.CopyPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CopyPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CopyPersonResponse()
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


    def CreateFace(self, request):
        """将一組人臉圖片添加到一個人員中。一個人員最多允許包含 5 張圖片。若該人員存在多個人員庫中，所有人員庫中該人員圖片均會增加。

        :param request: 調用CreateFace所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.CreateFaceRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.CreateFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFaceResponse()
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
        """用於創建一個空的人員庫，如果人員庫已存在返回錯誤。可根據需要創建自定義描述欄位，用於輔助描述該人員庫下的人員訊息。1個APPID下最多創建2萬個人員庫（Group）、最多包含1000萬張人臉（Face），單個人員庫（Group）最多包含100萬張人臉（Face）。

        :param request: 調用CreateGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.CreateGroupRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.CreateGroupResponse`

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
        """創建人員，添加人臉、姓名、性别及其他相關訊息。

        :param request: 調用CreatePerson所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.CreatePersonRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.CreatePersonResponse`

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


    def DeleteFace(self, request):
        """删除一個人員下的人臉圖片。如果該人員只有一張人臉圖片，則返回錯誤。

        :param request: 調用DeleteFace所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.DeleteFaceRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.DeleteFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFaceResponse()
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
        """删除該人員庫及包含的所有的人員。同時，人員對應的所有人臉訊息将被删除。若某人員同時存在多個人員庫中，該人員不會被删除，但屬於該人員庫中的自定義描述欄位訊息會被删除。

        注：删除人員庫的操作爲異步執行，删除單張人臉時間約爲10ms，即一小時内可以删除36萬張。删除期間，無法向該人員庫添加人員。

        :param request: 調用DeleteGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.DeleteGroupRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.DeleteGroupResponse`

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
        """删除該人員訊息，此操作會導緻所有人員庫均删除此人員。同時，該人員的所有人臉訊息将被删除。

        :param request: 調用DeletePerson所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.DeletePersonRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.DeletePersonResponse`

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


    def DeletePersonFromGroup(self, request):
        """從某人員庫中删除人員，此操作僅影響該人員庫。若該人員僅存在於指定的人員庫中，該人員将被删除，其所有的人臉訊息也将被删除。

        :param request: 調用DeletePersonFromGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.DeletePersonFromGroupRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.DeletePersonFromGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePersonFromGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePersonFromGroupResponse()
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


    def DetectFace(self, request):
        """檢測給定圖片中的人臉（Face）的位置、相應的面部屬性和人臉質量訊息，位置包括 (x，y，w，h)，面部屬性包括性别（gender）、年齡（age）、表情（expression）、魅力（beauty）、眼鏡（glass）、發型（hair）、口罩（mask）和姿态 (pitch，roll，yaw)，人臉質量訊息包括整體質量分（score）、模糊分（sharpness）、光照分（brightness）和五官遮擋分（completeness）。


        其中，人臉質量訊息主要用於評價輸入的人臉圖片的質量。在使用人臉識别服務時，建議您對輸入的人臉圖片進行質量檢測，提升後續業務處理的效果。該功能的應用場景包括：

        1） 人員庫[創建人員](https://cloud.taifucloud.com/document/product/867/32793)/[增加人臉](https://cloud.taifucloud.com/document/product/867/32795)：保證人員人臉訊息的質量，便於後續的業務處理。

        2） [人臉搜索](https://cloud.taifucloud.com/document/product/867/32798)：保證輸入的圖片質量，快速準确比對到對應的人員。

        3） [人臉驗證](https://cloud.taifucloud.com/document/product/867/32806)：保證人臉訊息的質量，避免明明是本人卻認證不通過的情況。

        4） [人臉融合](https://cloud.taifucloud.com/product/facefusion)：保證上傳的人臉質量，人臉融合的效果更好。


        :param request: 調用DetectFace所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.DetectFaceRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.DetectFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectFaceResponse()
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


    def DetectLiveFace(self, request):
        """用於對用戶上傳的靜态圖片進行人臉活體檢測。與動态活體檢測的區别是：靜态活體檢測中，用戶不需要通過唇語或搖頭眨眼等動作來識别。

        靜态活體檢測适用於手機自拍的場景，或對防攻擊要求不高的場景。如果對活體檢測有更高安全性要求，請使用[人臉核身·雲智慧眼](https://cloud.taifucloud.com/product/faceid)産品。

        >
        - 圖片的寬高比請接近3：4，不符合寬高比的圖片返回的分值不具備參考意義。本介面适用於類手機自拍場景，非類手機自拍照返回的分值不具備參考意義。

        :param request: 調用DetectLiveFace所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.DetectLiveFaceRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.DetectLiveFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectLiveFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectLiveFaceResponse()
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
        """獲取人員庫清單。

        :param request: 調用GetGroupList所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.GetGroupListRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.GetGroupListResponse`

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


    def GetPersonBaseInfo(self, request):
        """獲取指定人員的訊息，包括姓名、性别、人臉等。

        :param request: 調用GetPersonBaseInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.GetPersonBaseInfoRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.GetPersonBaseInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPersonBaseInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPersonBaseInfoResponse()
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


    def GetPersonGroupInfo(self, request):
        """獲取指定人員的訊息，包括加入的人員庫、描述内容等。

        :param request: 調用GetPersonGroupInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.GetPersonGroupInfoRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.GetPersonGroupInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPersonGroupInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPersonGroupInfoResponse()
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
        """獲取指定人員庫中的人員清單。

        :param request: 調用GetPersonList所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.GetPersonListRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.GetPersonListResponse`

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


    def GetPersonListNum(self, request):
        """獲取指定人員庫中人員數量。

        :param request: 調用GetPersonListNum所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.GetPersonListNumRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.GetPersonListNumResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPersonListNum", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPersonListNumResponse()
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
        """修改人員庫名稱、備注、自定義描述欄位名稱。

        :param request: 調用ModifyGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.ModifyGroupRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.ModifyGroupResponse`

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


    def ModifyPersonBaseInfo(self, request):
        """修改人員訊息，包括名稱、性别等。人員名稱和性别修改會同步到包含該人員的所有人員庫。

        :param request: 調用ModifyPersonBaseInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.ModifyPersonBaseInfoRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.ModifyPersonBaseInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonBaseInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonBaseInfoResponse()
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


    def ModifyPersonGroupInfo(self, request):
        """修改指定人員庫人員描述内容。

        :param request: 調用ModifyPersonGroupInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.ModifyPersonGroupInfoRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.ModifyPersonGroupInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonGroupInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonGroupInfoResponse()
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


    def SearchFaces(self, request):
        """用於對一張待識别的人臉圖片，在一個或多個人員庫中識别出最相似的 TopN 人員，識别結果按照相似度從大到小排序。單次搜索的人員庫人臉總數量不得超過 100 萬張。
        此介面需與[人員庫管理相關介面](https://cloud.taifucloud.com/document/product/867/32794)結合使用。

        :param request: 調用SearchFaces所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.SearchFacesRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.SearchFacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchFaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchFacesResponse()
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


    def VerifyFace(self, request):
        """給定一張人臉圖片和一個 PersonId，判斷圖片中的人和 PersonId 對應的人是否爲同一人。PersonId 請參考[人員庫管理相關介面](https://cloud.taifucloud.com/document/product/867/32794)。 和[人臉比對](https://cloud.taifucloud.com/document/product/867/32802)介面不同的是，[人臉驗證](https://cloud.taifucloud.com/document/product/867/32806)用於判斷 “此人是否是此人”，“此人”的訊息已存於人員庫中，“此人”可能存在多張人臉圖片；而[人臉比對](https://cloud.taifucloud.com/document/product/867/32802)用於判斷兩張人臉的相似度。

        :param request: 調用VerifyFace所需參數的結構體。
        :type request: :class:`taifucloudcloud.iai.v20180301.models.VerifyFaceRequest`
        :rtype: :class:`taifucloudcloud.iai.v20180301.models.VerifyFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyFaceResponse()
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