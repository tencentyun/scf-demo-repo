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
from tencentcloud.iotvideo.v20191126 import models


class IotvideoClient(AbstractClient):
    _apiVersion = '2019-11-26'
    _endpoint = 'iotvideo.tencentcloudapi.com'


    def CreateAppUsr(self, request):
        """本介面（CreateAppUsr）用于接收由廠商雲發送過來的注冊請求,建立廠商雲終端用戶與IoT Video終端用戶的映射關系。

        :param request: Request instance for CreateAppUsr.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateAppUsrRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateAppUsrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAppUsr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAppUsrResponse()
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


    def CreateBinding(self, request):
        """本介面（CreateBinding）用于終端用戶和設備進行綁定，具體的應用場景如下：
            終端用戶與設備具有“強關聯”關系。用戶與設備綁定之後，用戶終端即具備了該設備的訪問權限,訪問或操作設備時，無需獲取設備訪問Token。

        :param request: Request instance for CreateBinding.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateBindingRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateBindingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBinding", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBindingResponse()
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


    def CreateDevToken(self, request):
        """本介面（CreateDevToken）用于以下場景：
        終端用戶與設備沒有強綁定關聯關系;
        允許終端用戶短時或一次性臨時訪問設備;
        當終端用戶與設備有強綁定關系時，可以不用調用此介面

        :param request: Request instance for CreateDevToken.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateDevTokenRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateDevTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDevToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDevTokenResponse()
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


    def CreateDevices(self, request):
        """本介面（CreateDevices）用于批次創建新的物聯網視訊通信設備。
        注意：Top Cloud 不會對設備私鑰進行保存，請自行保管好您的設備私鑰。

        :param request: Request instance for CreateDevices.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDevicesResponse()
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


    def CreateGencode(self, request):
        """本介面（CreateGencode）用于生成設備物模型原始碼

        :param request: Request instance for CreateGencode.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateGencodeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateGencodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateGencode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGencodeResponse()
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


    def CreateIotDataType(self, request):
        """本介面（CreateIotDataType）用于創建自定義物模型數據類型。

        :param request: Request instance for CreateIotDataType.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateIotDataTypeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateIotDataTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateIotDataType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateIotDataTypeResponse()
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


    def CreateIotModel(self, request):
        """本介面（CreateIotModel）用于定義的物模型提交。
        該介面實現了物模型草稿箱的功能，保存用戶最後一次編輯的物模型數據。

        :param request: Request instance for CreateIotModel.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateIotModelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateIotModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateIotModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateIotModelResponse()
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


    def CreateProduct(self, request):
        """本介面（CreateProduct）用于創建一個新的物聯網智慧視訊産品。

        :param request: Request instance for CreateProduct.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProductResponse()
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


    def CreateStorage(self, request):
        """本介面（CreateStorage）用于購買雲存套餐。

        :param request: Request instance for CreateStorage.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateStorageRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateStorageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStorage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStorageResponse()
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


    def CreateTraceIds(self, request):
        """本介面（CreateTraceIds）用于将設備加到日志跟蹤白名單。

        :param request: Request instance for CreateTraceIds.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateTraceIdsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateTraceIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTraceIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTraceIdsResponse()
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


    def CreateUploadPath(self, request):
        """本介面（CreateUploadPath）用于獲取固件上傳路徑。

        :param request: Request instance for CreateUploadPath.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateUploadPathRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateUploadPathResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUploadPath", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUploadPathResponse()
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


    def CreateUsrToken(self, request):
        """本介面（CreateUsrToken）用于終端用戶獲取IoT Video平台的accessToken，初始化SDK,連接到IoT Video接入服務器。

        :param request: Request instance for CreateUsrToken.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.CreateUsrTokenRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.CreateUsrTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUsrToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUsrTokenResponse()
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


    def DeleteAppUsr(self, request):
        """本介面（DeleteAppUsr）用于删除終端用戶。

        :param request: Request instance for DeleteAppUsr.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteAppUsrRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteAppUsrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAppUsr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAppUsrResponse()
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


    def DeleteBinding(self, request):
        """本介面（DeleteBinding）用于終端用戶和設備進行解綁定。

        :param request: Request instance for DeleteBinding.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteBindingRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteBindingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBinding", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBindingResponse()
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


    def DeleteDevice(self, request):
        """本介面（DeleteDevice）用于删除設備，可進行批次操作，每次操作最多100台設備。

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceResponse()
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


    def DeleteIotDataType(self, request):
        """本介面（DeleteIotDataType）用于删除自定義物模型數據類型。

        :param request: Request instance for DeleteIotDataType.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteIotDataTypeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteIotDataTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteIotDataType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteIotDataTypeResponse()
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


    def DeleteMessageQueue(self, request):
        """本介面（DeleteMessageQueue）用于删除物聯網智慧視訊産品的轉發訊息配置訊息。

        :param request: Request instance for DeleteMessageQueue.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteMessageQueueRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteMessageQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMessageQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMessageQueueResponse()
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


    def DeleteOtaVersion(self, request):
        """本介面（DeleteOtaVersion）用于删除固件版本訊息。

        :param request: Request instance for DeleteOtaVersion.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteOtaVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteOtaVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteOtaVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteOtaVersionResponse()
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


    def DeleteProduct(self, request):
        """本介面（DeleteProduct）用于删除一個物聯網智慧視訊産品。

        :param request: Request instance for DeleteProduct.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProductResponse()
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


    def DeleteTraceIds(self, request):
        """本介面（DeleteTraceIds）用于将設備從日志跟蹤白名單中删除，該介面可批次操作，最多支援同時操作100台設備。

        :param request: Request instance for DeleteTraceIds.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DeleteTraceIdsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DeleteTraceIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTraceIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTraceIdsResponse()
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


    def DescribeBindDev(self, request):
        """本介面（DescribeBindDev）用于查詢終端用戶綁定的設備清單。

        :param request: Request instance for DescribeBindDev.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeBindDevRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeBindDevResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBindDev", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBindDevResponse()
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


    def DescribeBindUsr(self, request):
        """本介面（DescribeBindUsr）用于查詢設備被分享的所有用戶清單。

        :param request: Request instance for DescribeBindUsr.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeBindUsrRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeBindUsrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBindUsr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBindUsrResponse()
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


    def DescribeDevice(self, request):
        """本介面（DescribeDevice）獲取設備訊息。

        :param request: Request instance for DescribeDevice.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceResponse()
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


    def DescribeDeviceModel(self, request):
        """本介面（DescribeDeviceModel）用于獲取設備物模型。

        :param request: Request instance for DescribeDeviceModel.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDeviceModelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDeviceModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceModelResponse()
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


    def DescribeDevices(self, request):
        """本介面（DescribeDevices）用于獲取設備訊息清單。

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicesResponse()
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


    def DescribeIotDataType(self, request):
        """本介面（DescribeIotDataType）用于查詢自定義的物模型數據類型。

        :param request: Request instance for DescribeIotDataType.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotDataTypeRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotDataTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIotDataType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIotDataTypeResponse()
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


    def DescribeIotModel(self, request):
        """本介面（DescribeIotModel）用于獲取物模型定義詳情。

        :param request: Request instance for DescribeIotModel.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotModelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIotModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIotModelResponse()
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


    def DescribeIotModels(self, request):
        """本介面（DescribeIotModels）用于列出物模型曆史版本清單。

        :param request: Request instance for DescribeIotModels.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotModelsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeIotModelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIotModels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIotModelsResponse()
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


    def DescribeLogs(self, request):
        """本介面（DescribeLogs）用于查詢設備日志清單。
        設備日志最長保留時長爲15天,超期自動清除。

        :param request: Request instance for DescribeLogs.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeLogsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogsResponse()
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


    def DescribeMessageQueue(self, request):
        """本介面（DescribeMessageQueue）用于查詢物聯網智慧視訊産品轉發訊息配置。

        :param request: Request instance for DescribeMessageQueue.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeMessageQueueRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeMessageQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMessageQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMessageQueueResponse()
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


    def DescribeModelDataRet(self, request):
        """本介面（DescribeModelDataRet）用于根據TaskId獲取對設備物模型操作最終響應的結果。

        :param request: Request instance for DescribeModelDataRet.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeModelDataRetRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeModelDataRetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModelDataRet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModelDataRetResponse()
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


    def DescribeOtaVersions(self, request):
        """本介面（DescribeOtaVersions）用于查詢固件版本訊息清單。

        :param request: Request instance for DescribeOtaVersions.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeOtaVersionsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeOtaVersionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOtaVersions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOtaVersionsResponse()
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


    def DescribeProduct(self, request):
        """本介面（DescribeProduct）用于獲取單個産品的詳細訊息。

        :param request: Request instance for DescribeProduct.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductResponse()
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


    def DescribeProducts(self, request):
        """本介面（DescribeProducts）用于列出用戶賬号下的物聯網智慧視訊産品清單。

        :param request: Request instance for DescribeProducts.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeProductsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeProductsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProducts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductsResponse()
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


    def DescribePubVersions(self, request):
        """本介面（DescribePubVersions）用于獲取某一産品發布過的全部固件版本。

        :param request: Request instance for DescribePubVersions.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribePubVersionsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribePubVersionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePubVersions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePubVersionsResponse()
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


    def DescribeRegistrationStatus(self, request):
        """本介面（DescribeRegistrationStatus）用于查詢終端用戶的注冊狀态。

        :param request: Request instance for DescribeRegistrationStatus.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeRegistrationStatusRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeRegistrationStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegistrationStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegistrationStatusResponse()
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


    def DescribeRunLog(self, request):
        """本介面（DescribeRunLog）用于獲取設備運作日志。

        :param request: Request instance for DescribeRunLog.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeRunLogRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeRunLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRunLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRunLogResponse()
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


    def DescribeTraceIds(self, request):
        """本介面（DescribeTraceIds）用于查詢設備日志跟蹤白名單。

        :param request: Request instance for DescribeTraceIds.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeTraceIdsRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeTraceIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTraceIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTraceIdsResponse()
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


    def DescribeTraceStatus(self, request):
        """本介面（DescribeTraceStatus）用于查詢指定設備是否在白名單中。

        :param request: Request instance for DescribeTraceStatus.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DescribeTraceStatusRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DescribeTraceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTraceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTraceStatusResponse()
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


    def DisableDevice(self, request):
        """本介面（DisableDevice）用于禁用設備，可進行批次操作，每次操作最多100台設備。

        :param request: Request instance for DisableDevice.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DisableDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DisableDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableDeviceResponse()
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


    def DisableDeviceStream(self, request):
        """本介面（DisableDeviceStream）用于停止設備推流，可進行批次操作，每次操作最多100台設備。

        :param request: Request instance for DisableDeviceStream.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DisableDeviceStreamRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DisableDeviceStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableDeviceStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableDeviceStreamResponse()
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


    def DisableOtaVersion(self, request):
        """本介面（DisableOtaVersion）用于禁用固件版本。

        :param request: Request instance for DisableOtaVersion.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.DisableOtaVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.DisableOtaVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableOtaVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableOtaVersionResponse()
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


    def ModifyDeviceAction(self, request):
        """本介面（ModifyDeviceAction）用于修改設備物模型的行爲（Action）。

        可對ctlVal數據屬性進行寫入,如:Action.takePhoto.ctlVal,設備在線且成功發送到設備才返回,物模型寫入數據時,不需要傳入時标訊息,平台以當前時标作爲數據的時标更新物模型中的時标訊息。
        注意:
          1.若設備當前不在線,會直接返回錯誤
          2.若設備網絡出現異常時,訊息發送可能超時,超時等待最長時間爲3秒
          3.value的内容必須與實際物模型的定義一緻

        :param request: Request instance for ModifyDeviceAction.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.ModifyDeviceActionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ModifyDeviceActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDeviceAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDeviceActionResponse()
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


    def ModifyDeviceProperty(self, request):
        """本介面（ModifyDeviceProperty）用于修改設備物模型的屬性（ProWritable）。
        可對setVal數據屬性進行寫入,如:
        ProWritable.Pos.setVal
        對于嵌套類型的可寫屬性，可以僅對其部分數據内容進行寫入，如:
        ProWritable.Pos.setVal.x;
        可寫屬性雲端寫入成功即返回;雲端向設備端發布屬性變更參數;若當前設備不在線,在設備下次上線時會自動更新這些屬性參數;
        物模型寫入數據時,不需要傳入時标訊息,平台以當前時标作爲數據的時标更新物模型中的時标訊息。

        :param request: Request instance for ModifyDeviceProperty.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.ModifyDevicePropertyRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ModifyDevicePropertyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDeviceProperty", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDevicePropertyResponse()
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


    def ModifyProduct(self, request):
        """本介面（ModifyProduct）用于編輯物聯網智慧視訊産品的相關訊息。

        :param request: Request instance for ModifyProduct.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.ModifyProductRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.ModifyProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProductResponse()
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


    def RunDevice(self, request):
        """本介面（RunDevice）用于啓用設備，可進行批次操作，每次操作最多100台設備。

        :param request: Request instance for RunDevice.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RunDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RunDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunDeviceResponse()
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


    def RunDeviceStream(self, request):
        """本介面（RunDeviceStream）用于開啓設備推流，可進行批次操作，每次操作最多100台設備。

        :param request: Request instance for RunDeviceStream.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RunDeviceStreamRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RunDeviceStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunDeviceStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunDeviceStreamResponse()
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


    def RunIotModel(self, request):
        """本介面（RunIotModel）用于對定義的物模型進行發布。

        :param request: Request instance for RunIotModel.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RunIotModelRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RunIotModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunIotModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunIotModelResponse()
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


    def RunOtaVersion(self, request):
        """本介面（RunOtaVersion）用于固件版本正式發布。

        :param request: Request instance for RunOtaVersion.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RunOtaVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RunOtaVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunOtaVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunOtaVersionResponse()
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


    def RunTestOtaVersion(self, request):
        """本介面（RunTestOtaVersion）用于固件版本測試發布。

        :param request: Request instance for RunTestOtaVersion.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.RunTestOtaVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.RunTestOtaVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunTestOtaVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunTestOtaVersionResponse()
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


    def SendOnlineMsg(self, request):
        """本介面（SendOnlineMsg）用于向設備發送在線訊息。
        注意：
        若設備當前不在線,會直接返回錯誤;
        若設備網絡出現異常時,訊息發送可能超時,超時等待最長時間爲3秒.waitresp非0情況下,會導緻本介面阻塞3秒。

        :param request: Request instance for SendOnlineMsg.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.SendOnlineMsgRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.SendOnlineMsgResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendOnlineMsg", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendOnlineMsgResponse()
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


    def SetMessageQueue(self, request):
        """本介面（SetMessageQueue）用于配置物聯網智慧視訊産品的轉發訊息隊列。

        :param request: Request instance for SetMessageQueue.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.SetMessageQueueRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.SetMessageQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetMessageQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetMessageQueueResponse()
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


    def UpgradeDevice(self, request):
        """本介面（UpgradeDevice）用于對設備進行固件升級。
        該介面向指定的設備下發固件更新指令,可将固件升級到任意版本(可實現固件降級)。
        警告:使能UpgradeNow參數存在一定的風險性！建議僅在debug場景下使用!

        :param request: Request instance for UpgradeDevice.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.UpgradeDeviceRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.UpgradeDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDeviceResponse()
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


    def UploadOtaVersion(self, request):
        """本介面（UploadOtaVersion）接收上傳到控制台的固件版本訊息。

        :param request: Request instance for UploadOtaVersion.
        :type request: :class:`tencentcloud.iotvideo.v20191126.models.UploadOtaVersionRequest`
        :rtype: :class:`tencentcloud.iotvideo.v20191126.models.UploadOtaVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadOtaVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadOtaVersionResponse()
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