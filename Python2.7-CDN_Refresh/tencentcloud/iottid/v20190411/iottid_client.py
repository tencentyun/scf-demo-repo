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
from taifucloudcloud.iottid.v20190411 import models


class IottidClient(AbstractClient):
    _apiVersion = '2019-04-11'
    _endpoint = 'iottid.taifucloudcloudapi.com'


    def AuthTestTid(self, request):
        """單向認證測試TID

        :param request: Request instance for AuthTestTid.
        :type request: :class:`taifucloudcloud.iottid.v20190411.models.AuthTestTidRequest`
        :rtype: :class:`taifucloudcloud.iottid.v20190411.models.AuthTestTidResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AuthTestTid", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AuthTestTidResponse()
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


    def BurnTidNotify(self, request):
        """安全晶片TID燒錄回執

        :param request: Request instance for BurnTidNotify.
        :type request: :class:`taifucloudcloud.iottid.v20190411.models.BurnTidNotifyRequest`
        :rtype: :class:`taifucloudcloud.iottid.v20190411.models.BurnTidNotifyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BurnTidNotify", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BurnTidNotifyResponse()
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


    def DeliverTidNotify(self, request):
        """安全晶片爲載體的TID空發回執，綁定TID與訂單號。

        :param request: Request instance for DeliverTidNotify.
        :type request: :class:`taifucloudcloud.iottid.v20190411.models.DeliverTidNotifyRequest`
        :rtype: :class:`taifucloudcloud.iottid.v20190411.models.DeliverTidNotifyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeliverTidNotify", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeliverTidNotifyResponse()
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


    def DeliverTids(self, request):
        """設備服務商請求空發産品訂單的TID訊息

        :param request: Request instance for DeliverTids.
        :type request: :class:`taifucloudcloud.iottid.v20190411.models.DeliverTidsRequest`
        :rtype: :class:`taifucloudcloud.iottid.v20190411.models.DeliverTidsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeliverTids", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeliverTidsResponse()
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


    def DescribeAvailableLibCount(self, request):
        """查詢指定訂單的可空發的白盒金鑰數量

        :param request: Request instance for DescribeAvailableLibCount.
        :type request: :class:`taifucloudcloud.iottid.v20190411.models.DescribeAvailableLibCountRequest`
        :rtype: :class:`taifucloudcloud.iottid.v20190411.models.DescribeAvailableLibCountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAvailableLibCount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailableLibCountResponse()
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


    def DescribePermission(self, request):
        """查詢企業用戶TID平台控制台權限

        :param request: Request instance for DescribePermission.
        :type request: :class:`taifucloudcloud.iottid.v20190411.models.DescribePermissionRequest`
        :rtype: :class:`taifucloudcloud.iottid.v20190411.models.DescribePermissionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePermissionResponse()
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


    def DownloadTids(self, request):
        """下載晶片訂單的TID

        :param request: Request instance for DownloadTids.
        :type request: :class:`taifucloudcloud.iottid.v20190411.models.DownloadTidsRequest`
        :rtype: :class:`taifucloudcloud.iottid.v20190411.models.DownloadTidsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadTids", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadTidsResponse()
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


    def UploadDeviceUniqueCode(self, request):
        """上傳硬體唯一標識碼，是軟加固設備身份參數。本介面如遇到錯誤數據，則所有當次上傳數據失效。

        :param request: Request instance for UploadDeviceUniqueCode.
        :type request: :class:`taifucloudcloud.iottid.v20190411.models.UploadDeviceUniqueCodeRequest`
        :rtype: :class:`taifucloudcloud.iottid.v20190411.models.UploadDeviceUniqueCodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadDeviceUniqueCode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadDeviceUniqueCodeResponse()
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


    def VerifyChipBurnInfo(self, request):
        """下載控制台驗證晶片燒錄訊息，保證TID與中心訊息一緻

        :param request: Request instance for VerifyChipBurnInfo.
        :type request: :class:`taifucloudcloud.iottid.v20190411.models.VerifyChipBurnInfoRequest`
        :rtype: :class:`taifucloudcloud.iottid.v20190411.models.VerifyChipBurnInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyChipBurnInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyChipBurnInfoResponse()
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