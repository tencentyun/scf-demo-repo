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
from tencentcloud.iai.v20180301 import models


class IaiClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'iai.tencentcloudapi.com'


    def AnalyzeFace(self, request):
        """對請求圖片進行五官定位（也稱人臉關鍵點定位），計算構成人臉輪廓的 90 個點，包括眉毛（左右各 8 點）、眼睛（左右各 8 點）、鼻子（13 點）、嘴巴（22 點）、臉型輪廓（21 點）、眼珠[或瞳孔]（2點）。

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for AnalyzeFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.AnalyzeFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.AnalyzeFaceResponse`

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


    def CheckSimilarPerson(self, request):
        """對指定的人員庫進行人員查重，給出疑似相同人的訊息。

        可以使用本介面對已有的單個人員庫進行人員查重，避免同一人在單個人員庫中擁有多個身份；也可以使用本介面對已有的多個人員庫進行人員查重，查詢同一人是否同時存在多個人員庫中。

        不支援跨算法模型版本查重，且目前僅支援算法模型爲3.0的人員庫使用查重功能。

        >
        - 若對完全相同的指定人員庫進行查重操作，需等待上次操作完成才可。即，若兩次請求輸入的 GroupIds 相同，第一次請求若未完成，第二次請求将返回失敗。

        >
        - 查重的人員庫狀态爲Top Cloud 開始進行查重任務的那一刻，即您可以理解爲當您發起查重請求後，若您的查重任務需要排隊，在排隊期間您對人員庫的增删操作均會會影響查重的結果。Top Cloud 将以開始進行查重任務的那一刻人員庫的狀态進行查重。查重任務開始後，您對人員庫的任何操作均不影響查重任務的進行。但建議查重任務開始後，請不要對人員庫中人員和人臉進行增删操作。

        :param request: Request instance for CheckSimilarPerson.
        :type request: :class:`tencentcloud.iai.v20180301.models.CheckSimilarPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CheckSimilarPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckSimilarPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckSimilarPersonResponse()
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

        若您需要判斷 “此人是否是某人”，即驗證某張圖片中的人是否是已知身份的某人，如常見的人臉登入場景，建議使用[人臉驗證](https://cloud.tencent.com/document/product/867/32806)或[人員驗證](https://cloud.tencent.com/document/product/867/38879)介面。

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for CompareFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.CompareFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CompareFaceResponse`

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
        """将已存在于某人員庫的人員複制到其他人員庫，該人員的描述訊息不會被複制。單個人員最多只能同時存在100個人員庫中。
        >
        - 注：若該人員創建時算法模型版本爲2.0，複制到非2.0算法模型版本的Group中時，複制操作将會失敗。

        :param request: Request instance for CopyPerson.
        :type request: :class:`tencentcloud.iai.v20180301.models.CopyPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CopyPersonResponse`

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

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for CreateFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.CreateFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CreateFaceResponse`

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
        """用于創建一個空的人員庫，如果人員庫已存在返回錯誤。
        可根據需要創建自定義描述欄位，用于輔助描述該人員庫下的人員訊息。

        1個APPID下最多創建10萬個人員庫（Group）、最多包含5000萬張人臉（Face）。

        不同算法模型版本（FaceModelVersion）的人員庫（Group）最多可包含人臉（Face）數不同。算法模型版本爲2.0的人員庫最多包含100萬張人臉，算法模型版本爲3.0的人員庫最多可包含300萬張人臉。

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CreateGroupResponse`

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

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for CreatePerson.
        :type request: :class:`tencentcloud.iai.v20180301.models.CreatePersonRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CreatePersonResponse`

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

        :param request: Request instance for DeleteFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.DeleteFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DeleteFaceResponse`

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
        """删除該人員庫及包含的所有的人員。同時，人員對應的所有人臉訊息将被删除。若某人員同時存在多個人員庫中，該人員不會被删除，但屬于該人員庫中的自定義描述欄位訊息會被删除，屬于其他人員庫的自定義描述欄位訊息不受影響。

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DeleteGroupResponse`

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

        :param request: Request instance for DeletePerson.
        :type request: :class:`tencentcloud.iai.v20180301.models.DeletePersonRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DeletePersonResponse`

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
        """從某人員庫中删除人員，此操作僅影響該人員庫。若該人員僅存在于指定的人員庫中，該人員将被删除，其所有的人臉訊息也将被删除。

        :param request: Request instance for DeletePersonFromGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.DeletePersonFromGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DeletePersonFromGroupResponse`

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


        其中，人臉質量訊息主要用于評價輸入的人臉圖片的質量。在使用人臉識别服務時，建議您對輸入的人臉圖片進行質量檢測，提升後續業務處理的效果。該功能的應用場景包括：

        1） 人員庫[創建人員](https://cloud.tencent.com/document/product/867/32793)/[增加人臉](https://cloud.tencent.com/document/product/867/32795)：保證人員人臉訊息的質量，便于後續的業務處理。

        2） [人臉搜索](https://cloud.tencent.com/document/product/867/32798)：保證輸入的圖片質量，快速準确比對到對應的人員。

        3） [人臉驗證](https://cloud.tencent.com/document/product/867/32806)：保證人臉訊息的質量，避免明明是本人卻認證不通過的情況。

        4） [人臉融合](https://cloud.tencent.com/product/facefusion)：保證上傳的人臉質量，人臉融合的效果更好。

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。


        :param request: Request instance for DetectFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.DetectFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DetectFaceResponse`

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
        """用于對用戶上傳的靜态圖片進行人臉活體檢測。與動态活體檢測的區别是：靜态活體檢測中，用戶不需要通過唇語或搖頭眨眼等動作來識别。

        靜态活體檢測适用于手機自拍的場景，或對防攻擊要求不高的場景。如果對活體檢測有更高安全性要求，請使用[人臉核身·雲智慧眼](https://cloud.tencent.com/product/faceid)産品。

        >
        - 圖片的寬高比請接近3：4，不符合寬高比的圖片返回的分值不具備參考意義。本介面适用于類手機自拍場景，非類手機自拍照返回的分值不具備參考意義。

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for DetectLiveFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.DetectLiveFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DetectLiveFaceResponse`

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


    def EstimateCheckSimilarPersonCostTime(self, request):
        """獲取若要開始一個人員查重任務，這個任務結束的預估時間。

        若EndTimestamp符合您預期，請您盡快發起人員查重請求，否則導緻可能需要更多處理時間。

        若預估時間超過5小時，則無法使用人員查重功能。

        :param request: Request instance for EstimateCheckSimilarPersonCostTime.
        :type request: :class:`tencentcloud.iai.v20180301.models.EstimateCheckSimilarPersonCostTimeRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.EstimateCheckSimilarPersonCostTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EstimateCheckSimilarPersonCostTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EstimateCheckSimilarPersonCostTimeResponse()
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


    def GetCheckSimilarPersonJobIdList(self, request):
        """獲取人員查重任務清單，按任務創建時間逆序（最新的在前面）。

        只保留最近1年的數據。

        :param request: Request instance for GetCheckSimilarPersonJobIdList.
        :type request: :class:`tencentcloud.iai.v20180301.models.GetCheckSimilarPersonJobIdListRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetCheckSimilarPersonJobIdListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetCheckSimilarPersonJobIdList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetCheckSimilarPersonJobIdListResponse()
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


    def GetGroupInfo(self, request):
        """獲取人員庫訊息。

        :param request: Request instance for GetGroupInfo.
        :type request: :class:`tencentcloud.iai.v20180301.models.GetGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetGroupInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetGroupInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetGroupInfoResponse()
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

        :param request: Request instance for GetGroupList.
        :type request: :class:`tencentcloud.iai.v20180301.models.GetGroupListRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetGroupListResponse`

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

        :param request: Request instance for GetPersonBaseInfo.
        :type request: :class:`tencentcloud.iai.v20180301.models.GetPersonBaseInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetPersonBaseInfoResponse`

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

        :param request: Request instance for GetPersonGroupInfo.
        :type request: :class:`tencentcloud.iai.v20180301.models.GetPersonGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetPersonGroupInfoResponse`

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

        :param request: Request instance for GetPersonList.
        :type request: :class:`tencentcloud.iai.v20180301.models.GetPersonListRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetPersonListResponse`

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

        :param request: Request instance for GetPersonListNum.
        :type request: :class:`tencentcloud.iai.v20180301.models.GetPersonListNumRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetPersonListNumResponse`

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


    def GetSimilarPersonResult(self, request):
        """獲取人員查重介面（CheckSimilarPerson）結果。

        :param request: Request instance for GetSimilarPersonResult.
        :type request: :class:`tencentcloud.iai.v20180301.models.GetSimilarPersonResultRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetSimilarPersonResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSimilarPersonResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSimilarPersonResultResponse()
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

        :param request: Request instance for ModifyGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.ModifyGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.ModifyGroupResponse`

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

        :param request: Request instance for ModifyPersonBaseInfo.
        :type request: :class:`tencentcloud.iai.v20180301.models.ModifyPersonBaseInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.ModifyPersonBaseInfoResponse`

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

        :param request: Request instance for ModifyPersonGroupInfo.
        :type request: :class:`tencentcloud.iai.v20180301.models.ModifyPersonGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.ModifyPersonGroupInfoResponse`

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
        """用于對一張待識别的人臉圖片，在一個或多個人員庫中識别出最相似的 TopK 人員，識别結果按照相似度從大到小排序。

        支援一次性識别圖片中的最多 10 張人臉，支援一次性跨 100 個人員庫（Group）搜索。

        單次搜索的人員庫人臉總數量和人員庫的算法模型版本（FaceModelVersion）相關。算法模型版本爲2.0的人員庫，單次搜索人員庫人臉總數量不得超過 100 萬張；算法模型版本爲3.0的人員庫，單次搜索人員庫人臉總數量不得超過 300 萬張。

        與[人員搜索](https://cloud.tencent.com/document/product/867/38881)及[人員搜索按庫返回](https://cloud.tencent.com/document/product/867/38880)介面不同的是，本介面将該人員（Person）下的每個人臉（Face）都作爲單獨個體進行驗證，而人員搜索及人員搜索按庫返回介面 會将該人員（Person）下的所有人臉（Face）進行融合特征處理，即若某個Person下有4張 Face，本介面會将4張 Face 的特征進行融合處理，生成對應這個 Person 的特征，使搜索更加準确。


        本介面需與[人員庫管理相關介面](https://cloud.tencent.com/document/product/867/32794)結合使用。

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for SearchFaces.
        :type request: :class:`tencentcloud.iai.v20180301.models.SearchFacesRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.SearchFacesResponse`

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


    def SearchFacesReturnsByGroup(self, request):
        """用于對一張待識别的人臉圖片，在一個或多個人員庫中識别出最相似的 TopK 人員，按照**人員庫的維度**以人員相似度從大到小順序排列。

        支援一次性識别圖片中的最多 10 張人臉，支援跨人員庫（Group）搜索。

        單次搜索的人員庫人臉總數量和人員庫的算法模型版本（FaceModelVersion）相關。算法模型版本爲2.0的人員庫，單次搜索人員庫人臉總數量不得超過 100 萬張；算法模型版本爲3.0的人員庫，單次搜索人員庫人臉總數量不得超過 300 萬張。

        與[人員搜索](https://cloud.tencent.com/document/product/867/38881)及[人員搜索按庫返回](https://cloud.tencent.com/document/product/867/38880)介面不同的是，本介面将該人員（Person）下的每個人臉（Face）都作爲單獨個體進行驗證，而[人員搜索](https://cloud.tencent.com/document/product/867/38881)及[人員搜索按庫返回](https://cloud.tencent.com/document/product/867/38880)介面 會将該人員（Person）下的所有人臉（Face）進行融合特征處理，即若某個Person下有4張 Face，本介面會将4張 Face 的特征進行融合處理，生成對應這個 Person 的特征，使搜索更加準确。

        本介面需與[人員庫管理相關介面](https://cloud.tencent.com/document/product/867/32794)結合使用。

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。


        :param request: Request instance for SearchFacesReturnsByGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.SearchFacesReturnsByGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.SearchFacesReturnsByGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchFacesReturnsByGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchFacesReturnsByGroupResponse()
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


    def SearchPersons(self, request):
        """用于對一張待識别的人臉圖片，在一個或多個人員庫中識别出最相似的 TopK 人員，按照相似度從大到小排列。

        支援一次性識别圖片中的最多 10 張人臉，支援一次性跨 100 個人員庫（Group）搜索。

        單次搜索的人員庫人臉總數量和人員庫的算法模型版本（FaceModelVersion）相關。算法模型版本爲2.0的人員庫，單次搜索人員庫人臉總數量不得超過 100 萬張；算法模型版本爲3.0的人員庫，單次搜索人員庫人臉總數量不得超過 300 萬張。

        本介面會将該人員（Person）下的所有人臉（Face）進行融合特征處理，即若某個 Person 下有4張 Face ，本介面會将4張 Face 的特征進行融合處理，生成對應這個 Person 的特征，使人員搜索（确定待識别的人臉圖片是某人）更加準确。而[人臉搜索](https://cloud.tencent.com/document/product/867/32798)及[人臉搜索按庫返回介面](https://cloud.tencent.com/document/product/867/38882)将該人員（Person）下的每個人臉（Face）都作爲單獨個體進行搜索。

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。
        - 僅支援算法模型版本（FaceModelVersion）爲3.0的人員庫。

        :param request: Request instance for SearchPersons.
        :type request: :class:`tencentcloud.iai.v20180301.models.SearchPersonsRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.SearchPersonsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchPersons", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchPersonsResponse()
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


    def SearchPersonsReturnsByGroup(self, request):
        """用于對一張待識别的人臉圖片，在一個或多個人員庫中識别出最相似的 TopK 人員，按照**人員庫的維度**以人員相似度從大到小順序排列。

        支援一次性識别圖片中的最多 10 張人臉，支援跨人員庫（Group）搜索。

        單次搜索的人員庫人臉總數量和人員庫的算法模型版本（FaceModelVersion）相關。算法模型版本爲2.0的人員庫，單次搜索人員庫人臉總數量不得超過 100 萬張；算法模型版本爲3.0的人員庫，單次搜索人員庫人臉總數量不得超過 300 萬張。

        本介面會将該人員（Person）下的所有人臉（Face）進行融合特征處理，即若某個 Person 下有4張 Face ，本介面會将4張 Face 的特征進行融合處理，生成對應這個 Person 的特征，使人員搜索（确定待識别的人臉圖片是某人）更加準确。而[人臉搜索](https://cloud.tencent.com/document/product/867/32798)及[人臉搜索按庫返回介面](https://cloud.tencent.com/document/product/867/38882)将該人員（Person）下的每個人臉（Face）都作爲單獨個體進行搜索。
        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。
        - 僅支援算法模型版本（FaceModelVersion）爲3.0的人員庫。

        :param request: Request instance for SearchPersonsReturnsByGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.SearchPersonsReturnsByGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.SearchPersonsReturnsByGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchPersonsReturnsByGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchPersonsReturnsByGroupResponse()
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
        """給定一張人臉圖片和一個 PersonId，判斷圖片中的人和 PersonId 對應的人是否爲同一人。PersonId 請參考[人員庫管理相關介面](https://cloud.tencent.com/document/product/867/32794)。

        與[人臉比對](https://cloud.tencent.com/document/product/867/32802)介面不同的是，人臉驗證用于判斷 “此人是否是此人”，“此人”的訊息已存于人員庫中，“此人”可能存在多張人臉圖片；而[人臉比對](https://cloud.tencent.com/document/product/867/32802)用于判斷兩張人臉的相似度。

        與[人員驗證](https://cloud.tencent.com/document/product/867/38879)介面不同的是，人臉驗證将該人員（Person）下的每個人臉（Face）都作爲單獨個體進行驗證，而[人員驗證](https://cloud.tencent.com/document/product/867/38879)會将該人員（Person）下的所有人臉（Face）進行融合特征處理，即若某個 Person下有4張 Face，本介面會将4張 Face 的特征進行融合處理，生成對應這個 Person 的特征，使人員驗證（确定待識别的人臉圖片是某人員）更加準确。

        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for VerifyFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.VerifyFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.VerifyFaceResponse`

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


    def VerifyPerson(self, request):
        """給定一張人臉圖片和一個 PersonId，判斷圖片中的人和 PersonId 對應的人是否爲同一人。PersonId 請參考[人員庫管理相關介面](https://cloud.tencent.com/document/product/867/32794)。
        本介面會将該人員（Person）下的所有人臉（Face）進行融合特征處理，即若某個Person下有4張 Face，本介面會将4張 Face 的特征進行融合處理，生成對應這個 Person 的特征，使人員驗證（确定待識别的人臉圖片是某人員）更加準确。

         和人臉比對相關介面不同的是，人臉驗證相關介面用于判斷 “此人是否是此人”，“此人”的訊息已存于人員庫中，“此人”可能存在多張人臉圖片；而人臉比對相關介面用于判斷兩張人臉的相似度。


        >
        - 公共參數中的簽名方式請使用V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。
        - 僅支援算法模型版本（FaceModelVersion）爲3.0的人員庫。

        :param request: Request instance for VerifyPerson.
        :type request: :class:`tencentcloud.iai.v20180301.models.VerifyPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.VerifyPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyPersonResponse()
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