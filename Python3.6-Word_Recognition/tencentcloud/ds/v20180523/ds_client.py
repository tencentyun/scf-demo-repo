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
from taifucloudcloud.ds.v20180523 import models


class DsClient(AbstractClient):
    _apiVersion = '2018-05-23'
    _endpoint = 'ds.taifucloudcloudapi.com'


    def CheckVcode(self, request):
        """檢測驗證碼介面。此介面用於企業電子合同平台通過給用戶發送簡訊驗證碼，以簡訊授權方式簽署合同。此介面配合發送驗證碼介面使用。

        用戶在企業電子合同平台輸入收到的驗證碼後，由企業電子合同平台調用該介面向Top Cloud 提交确認受托簽署合同驗證碼命令。驗證碼驗證正确時，本次合同簽署的授權成功。

        :param request: 調用CheckVcode所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.CheckVcodeRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.CheckVcodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckVcode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckVcodeResponse()
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


    def CreateContractByUpload(self, request):
        """此介面适用於：客戶平台通過上傳PDF文件作爲合同，以備未來進行簽署。介面返回任務號，可調用DescribeTaskStatus介面檢視任務執行結果。

        :param request: 調用CreateContractByUpload所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.CreateContractByUploadRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.CreateContractByUploadResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateContractByUpload", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateContractByUploadResponse()
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


    def CreateEnterpriseAccount(self, request):
        """爲企業電子合同平台的最終企業用戶進行開戶。在企業電子合同平台進行操作的企業用戶，企業電子合同平台向Top Cloud 發送企業用戶的訊息，提交開戶命令。Top Cloud 接到請求後，自動爲企業電子合同平台的企業用戶生成一張數字證書。

        :param request: 調用CreateEnterpriseAccount所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.CreateEnterpriseAccountRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.CreateEnterpriseAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEnterpriseAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEnterpriseAccountResponse()
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


    def CreatePersonalAccount(self, request):
        """爲企業電子合同平台的最終個人用戶進行開戶。在企業電子合同平台進行操作的個人用戶，企業電子合同平台向Top Cloud 發送個人用戶的訊息，提交開戶命令。Top Cloud 接到請求後，自動爲企業電子合同平台的個人用戶生成一張數字證書。

        :param request: 調用CreatePersonalAccount所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.CreatePersonalAccountRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.CreatePersonalAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePersonalAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePersonalAccountResponse()
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


    def CreateSeal(self, request):
        """此介面用於客戶電子合同平台增加某用戶的印章圖片。客戶平台可以調用此介面增加某用戶的印章圖片。

        :param request: 調用CreateSeal所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.CreateSealRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.CreateSealResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSeal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSealResponse()
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


    def DeleteAccount(self, request):
        """删除企業電子合同平台的最終用戶。調用該介面後，Top Cloud 将删除該用戶賬號。删除賬號後，已經簽名的合同不受影響。

        :param request: 調用DeleteAccount所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.DeleteAccountRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccountResponse()
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


    def DeleteSeal(self, request):
        """删除印章介面，删除指定賬號的某個印章

        :param request: 調用DeleteSeal所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.DeleteSealRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.DeleteSealResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSeal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSealResponse()
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


    def DescribeTaskStatus(self, request):
        """介面使用於：客戶平台可使用該介面查詢任務執行狀态或者執行結果

        :param request: 調用DescribeTaskStatus所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.DescribeTaskStatusRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskStatusResponse()
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


    def DownloadContract(self, request):
        """下載合同介面。調用該介面可以下載簽署中和簽署完成的合同。介面返回任務號，可調用DescribeTaskStatus介面檢視任務執行結果。

        :param request: 調用DownloadContract所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.DownloadContractRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.DownloadContractResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadContract", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadContractResponse()
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


    def SendVcode(self, request):
        """發送驗證碼介面。此介面用於：企業電子合同平台需要Top Cloud 發送驗證碼對其用戶進行驗證時調用，Top Cloud 将向其用戶聯系手機(企業電子合同平台爲用戶開戶時通過介面傳入)發送驗證碼，以驗證碼授權方式簽署合同。用戶驗證工作由企業電子合同平台自身完成。

        :param request: 調用SendVcode所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.SendVcodeRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.SendVcodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendVcode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendVcodeResponse()
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


    def SignContractByCoordinate(self, request):
        """此介面适用於：客戶平台在創建好合同後，由合同簽署方對創建的合同内容進行确認，無誤後再進行簽署。客戶平台使用該介面提供詳細的PDF文件簽名坐標進行簽署。

        :param request: 調用SignContractByCoordinate所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.SignContractByCoordinateRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.SignContractByCoordinateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SignContractByCoordinate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SignContractByCoordinateResponse()
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


    def SignContractByKeyword(self, request):
        """此介面适用於：客戶平台在創建好合同後，由合同簽署方對創建的合同内容進行确認，無誤後再進行簽署。客戶平台使用該介面對PDF合同文件按照關鍵字和坐標進行簽署。

        :param request: 調用SignContractByKeyword所需參數的結構體。
        :type request: :class:`taifucloudcloud.ds.v20180523.models.SignContractByKeywordRequest`
        :rtype: :class:`taifucloudcloud.ds.v20180523.models.SignContractByKeywordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SignContractByKeyword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SignContractByKeywordResponse()
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