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
from taifucloudcloud.youmall.v20180228 import models


class YoumallClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'youmall.taifucloudcloudapi.com'


    def CreateAccount(self, request):
        """創建集團門店管理員賬号

        :param request: 調用CreateAccount所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.CreateAccountRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountResponse()
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


    def CreateFacePicture(self, request):
        """通過上傳指定規格的人臉圖片，創建黑名單用戶或者白名單用戶。

        :param request: 調用CreateFacePicture所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.CreateFacePictureRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.CreateFacePictureResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFacePicture", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFacePictureResponse()
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


    def DeletePersonFeature(self, request):
        """删除顧客特征，僅支援删除黑名單或者白名單用戶特征。

        :param request: 調用DeletePersonFeature所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DeletePersonFeatureRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DeletePersonFeatureResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePersonFeature", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePersonFeatureResponse()
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


    def DescribeCameraPerson(self, request):
        """通過指定設備ID和指定時段，獲取該時段内中收銀台攝像設備抓取到顧客頭像及身份ID

        :param request: 調用DescribeCameraPerson所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeCameraPersonRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeCameraPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCameraPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCameraPersonResponse()
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


    def DescribeClusterPersonArrivedMall(self, request):
        """輸出開始時間到結束時間段内的進出場數據。按天聚合的情況下，每天多次進出場算一次，以最初進場時間爲進場時間，最後離場時間爲離場時間。停留時間爲多次進出場的停留時間之和。

        :param request: 調用DescribeClusterPersonArrivedMall所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeClusterPersonArrivedMallRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeClusterPersonArrivedMallResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterPersonArrivedMall", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterPersonArrivedMallResponse()
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


    def DescribeClusterPersonTrace(self, request):
        """輸出開始時間到結束時間段内的進出場數據。按天聚合的情況下，每天多次進出場算一次，以最初進場時間爲進場時間，最後離場時間爲離場時間。

        :param request: 調用DescribeClusterPersonTrace所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeClusterPersonTraceRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeClusterPersonTraceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterPersonTrace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterPersonTraceResponse()
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


    def DescribeFaceIdByTempId(self, request):
        """通過DescribeCameraPerson介面上報的收銀台身份ID查詢顧客的FaceID。查詢最佳時間爲收銀台上報的次日1點後。

        :param request: 調用DescribeFaceIdByTempId所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeFaceIdByTempIdRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeFaceIdByTempIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFaceIdByTempId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFaceIdByTempIdResponse()
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


    def DescribeHistoryNetworkInfo(self, request):
        """返回當前門店曆史網絡狀态數據

        :param request: 調用DescribeHistoryNetworkInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeHistoryNetworkInfoRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeHistoryNetworkInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHistoryNetworkInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHistoryNetworkInfoResponse()
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


    def DescribeNetworkInfo(self, request):
        """返回當前門店最新網絡狀态數據

        :param request: 調用DescribeNetworkInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeNetworkInfoRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeNetworkInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetworkInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkInfoResponse()
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


    def DescribePerson(self, request):
        """查詢指定某一賣場的用戶訊息

        :param request: 調用DescribePerson所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonResponse()
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


    def DescribePersonArrivedMall(self, request):
        """輸出開始時間到結束時間段内的進出場數據。不做按天聚合的情況下，每次進出場，産生一條進出場數據。


        :param request: 調用DescribePersonArrivedMall所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonArrivedMallRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonArrivedMallResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonArrivedMall", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonArrivedMallResponse()
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


    def DescribePersonInfo(self, request):
        """指定門店獲取所有顧客詳情清單，包含客戶ID、圖片、年齡、性别

        :param request: 調用DescribePersonInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonInfoRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonInfoResponse()
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


    def DescribePersonInfoByFacePicture(self, request):
        """通過上傳人臉圖片檢索系統face id、顧客身份訊息及底圖

        :param request: 調用DescribePersonInfoByFacePicture所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonInfoByFacePictureRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonInfoByFacePictureResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonInfoByFacePicture", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonInfoByFacePictureResponse()
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


    def DescribePersonTrace(self, request):
        """輸出開始時間到結束時間段内的進出場數據。

        :param request: 調用DescribePersonTrace所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonTraceRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonTraceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonTrace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonTraceResponse()
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


    def DescribePersonTraceDetail(self, request):
        """查詢客戶單次到場軌迹明細

        :param request: 調用DescribePersonTraceDetail所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonTraceDetailRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonTraceDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonTraceDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonTraceDetailResponse()
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


    def DescribePersonVisitInfo(self, request):
        """獲取門店指定時間範圍内的所有用戶到訪訊息記錄，支援的時間範圍：過去365天，含當天。

        :param request: 調用DescribePersonVisitInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonVisitInfoRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribePersonVisitInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonVisitInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonVisitInfoResponse()
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


    def DescribeShopHourTrafficInfo(self, request):
        """按小時提供查詢日期範圍内門店的每天每小時累計客流人數數據，支援的時間範圍：過去365天，含當天。

        :param request: 調用DescribeShopHourTrafficInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeShopHourTrafficInfoRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeShopHourTrafficInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShopHourTrafficInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShopHourTrafficInfoResponse()
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


    def DescribeShopInfo(self, request):
        """根據客戶身份标識獲取客戶下所有的門店訊息清單

        :param request: 調用DescribeShopInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeShopInfoRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeShopInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShopInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShopInfoResponse()
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


    def DescribeShopTrafficInfo(self, request):
        """按天提供查詢日期範圍内門店的單日累計客流人數，支援的時間範圍：過去365天，含當天。

        :param request: 調用DescribeShopTrafficInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeShopTrafficInfoRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeShopTrafficInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShopTrafficInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShopTrafficInfoResponse()
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


    def DescribeTrajectoryData(self, request):
        """獲取動線軌迹訊息

        :param request: 調用DescribeTrajectoryData所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeTrajectoryDataRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeTrajectoryDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrajectoryData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrajectoryDataResponse()
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


    def DescribeZoneFlowAgeInfoByZoneId(self, request):
        """獲取指定區域人流各年齡占比

        :param request: 調用DescribeZoneFlowAgeInfoByZoneId所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowAgeInfoByZoneIdRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowAgeInfoByZoneIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowAgeInfoByZoneId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowAgeInfoByZoneIdResponse()
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


    def DescribeZoneFlowAndStayTime(self, request):
        """獲取區域人流和停留時間

        :param request: 調用DescribeZoneFlowAndStayTime所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowAndStayTimeRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowAndStayTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowAndStayTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowAndStayTimeResponse()
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


    def DescribeZoneFlowDailyByZoneId(self, request):
        """獲取指定區域每日客流量

        :param request: 調用DescribeZoneFlowDailyByZoneId所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowDailyByZoneIdRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowDailyByZoneIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowDailyByZoneId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowDailyByZoneIdResponse()
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


    def DescribeZoneFlowGenderAvrStayTimeByZoneId(self, request):
        """獲取指定區域不同年齡段男女平均停留時間

        :param request: 調用DescribeZoneFlowGenderAvrStayTimeByZoneId所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowGenderAvrStayTimeByZoneIdRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowGenderAvrStayTimeByZoneIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowGenderAvrStayTimeByZoneId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowGenderAvrStayTimeByZoneIdResponse()
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


    def DescribeZoneFlowGenderInfoByZoneId(self, request):
        """獲取指定區域性别占比

        :param request: 調用DescribeZoneFlowGenderInfoByZoneId所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowGenderInfoByZoneIdRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowGenderInfoByZoneIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowGenderInfoByZoneId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowGenderInfoByZoneIdResponse()
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


    def DescribeZoneFlowHourlyByZoneId(self, request):
        """獲取指定區域分時客流量

        :param request: 調用DescribeZoneFlowHourlyByZoneId所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowHourlyByZoneIdRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneFlowHourlyByZoneIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneFlowHourlyByZoneId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneFlowHourlyByZoneIdResponse()
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


    def DescribeZoneTrafficInfo(self, request):
        """按天提供查詢日期範圍内，客戶指定門店下的所有區域（優Mall佈署時已配置區域）的累計客流人次和平均停留時間。支援的時間範圍：過去365天，含當天。

        :param request: 調用DescribeZoneTrafficInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneTrafficInfoRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.DescribeZoneTrafficInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneTrafficInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneTrafficInfoResponse()
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


    def ModifyPersonFeatureInfo(self, request):
        """支援修改黑白名單類型的顧客特征

        :param request: 調用ModifyPersonFeatureInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.ModifyPersonFeatureInfoRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.ModifyPersonFeatureInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonFeatureInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonFeatureInfoResponse()
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


    def ModifyPersonTagInfo(self, request):
        """标記到店顧客的身份類型，例如黑名單、白名單等

        :param request: 調用ModifyPersonTagInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.ModifyPersonTagInfoRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.ModifyPersonTagInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonTagInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonTagInfoResponse()
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


    def ModifyPersonType(self, request):
        """修改顧客身份類型介面

        :param request: 調用ModifyPersonType所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.ModifyPersonTypeRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.ModifyPersonTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonTypeResponse()
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


    def RegisterCallback(self, request):
        """調用本介面在優Mall中注冊自己集團的到店通知回調介面網址，介面協議爲HTTP或HTTPS。注冊後，若集團有特殊身份（例如老客）到店通知，優Mall後台将主動将到店訊息push給該介面

        :param request: 調用RegisterCallback所需參數的結構體。
        :type request: :class:`taifucloudcloud.youmall.v20180228.models.RegisterCallbackRequest`
        :rtype: :class:`taifucloudcloud.youmall.v20180228.models.RegisterCallbackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterCallback", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterCallbackResponse()
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