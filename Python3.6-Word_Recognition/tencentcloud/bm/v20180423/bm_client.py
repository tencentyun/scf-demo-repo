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
from tencentcloud.bm.v20180423 import models


class BmClient(AbstractClient):
    _apiVersion = '2018-04-23'
    _endpoint = 'bm.tencentcloudapi.com'


    def BindPsaTag(self, request):
        """爲預授權規則綁定标簽

        :param request: 調用BindPsaTag所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.BindPsaTagRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.BindPsaTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindPsaTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindPsaTagResponse()
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


    def BuyDevices(self, request):
        """購買黑石物理機

        :param request: 調用BuyDevices所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.BuyDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.BuyDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BuyDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BuyDevicesResponse()
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


    def CreateCustomImage(self, request):
        """創建自定義映像<br>
        每個AppId在每個可用區最多保留20個自定義映像

        :param request: 調用CreateCustomImage所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.CreateCustomImageRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreateCustomImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCustomImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCustomImageResponse()
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


    def CreatePsaRegulation(self, request):
        """創建預授權規則

        :param request: 調用CreatePsaRegulation所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.CreatePsaRegulationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreatePsaRegulationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePsaRegulation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePsaRegulationResponse()
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


    def CreateSpotDevice(self, request):
        """創建黑石競價實例

        :param request: 調用CreateSpotDevice所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.CreateSpotDeviceRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreateSpotDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSpotDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSpotDeviceResponse()
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


    def CreateUserCmd(self, request):
        """創建自定義腳本

        :param request: 調用CreateUserCmd所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.CreateUserCmdRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreateUserCmdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUserCmd", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUserCmdResponse()
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


    def DeleteCustomImages(self, request):
        """删除自定義映像<br>
        正用于佈署或重裝中的映像被删除後，映像文件将保留一段時間，直到佈署或重裝結束

        :param request: 調用DeleteCustomImages所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DeleteCustomImagesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DeleteCustomImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCustomImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCustomImagesResponse()
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


    def DeletePsaRegulation(self, request):
        """删除預授權規則

        :param request: 調用DeletePsaRegulation所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DeletePsaRegulationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DeletePsaRegulationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePsaRegulation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePsaRegulationResponse()
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


    def DeleteUserCmds(self, request):
        """删除自定義腳本

        :param request: 調用DeleteUserCmds所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DeleteUserCmdsRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DeleteUserCmdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUserCmds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserCmdsResponse()
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


    def DescribeCustomImageProcess(self, request):
        """查詢自定義映像制作進度

        :param request: 調用DescribeCustomImageProcess所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeCustomImageProcessRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeCustomImageProcessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomImageProcess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomImageProcessResponse()
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


    def DescribeCustomImages(self, request):
        """檢視自定義映像清單

        :param request: 調用DescribeCustomImages所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeCustomImagesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeCustomImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomImagesResponse()
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


    def DescribeDeviceClass(self, request):
        """獲取獲取設備類型

        :param request: 調用DescribeDeviceClass所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceClassRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceClassResponse()
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


    def DescribeDeviceClassPartition(self, request):
        """查詢機型支援的RAID方式， 并返回系統盤的分區和邏輯盤的清單

        :param request: 調用DescribeDeviceClassPartition所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceClassPartitionRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceClassPartitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceClassPartition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceClassPartitionResponse()
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


    def DescribeDeviceHardwareInfo(self, request):
        """查詢設備硬體配置訊息，如 CPU 型号，内存大小，磁盤大小和數量

        :param request: 調用DescribeDeviceHardwareInfo所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceHardwareInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceHardwareInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceHardwareInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceHardwareInfoResponse()
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


    def DescribeDeviceInventory(self, request):
        """查詢設備庫存

        :param request: 調用DescribeDeviceInventory所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceInventoryRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceInventoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceInventory", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceInventoryResponse()
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


    def DescribeDeviceOperationLog(self, request):
        """查詢設備操作日志， 如設備重啓，重裝，設置密碼等操作

        :param request: 調用DescribeDeviceOperationLog所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceOperationLogRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDeviceOperationLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceOperationLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceOperationLogResponse()
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


    def DescribeDevicePartition(self, request):
        """獲取物理機的分區格式

        :param request: 調用DescribeDevicePartition所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePartitionRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePartitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevicePartition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicePartitionResponse()
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


    def DescribeDevicePosition(self, request):
        """查詢服務器所在的位置，如機架，上聯交換機等訊息

        :param request: 調用DescribeDevicePosition所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePositionRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePositionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevicePosition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicePositionResponse()
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


    def DescribeDevicePriceInfo(self, request):
        """查詢服務器價格訊息，支援設備的批次查找，支援标準機型和彈性機型的混合查找

        :param request: 調用DescribeDevicePriceInfo所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePriceInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDevicePriceInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevicePriceInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicePriceInfoResponse()
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
        """查詢物理服務器，可以按照實例，業務IP等過濾

        :param request: 調用DescribeDevices所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDevicesResponse`

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


    def DescribeHardwareSpecification(self, request):
        """查詢自定義機型部件訊息，包括CpuId對應的型号，DiskTypeId對應的磁盤類型

        :param request: 調用DescribeHardwareSpecification所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeHardwareSpecificationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeHardwareSpecificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHardwareSpecification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHardwareSpecificationResponse()
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


    def DescribeHostedDeviceOutBandInfo(self, request):
        """查詢托管設備帶外訊息

        :param request: 調用DescribeHostedDeviceOutBandInfo所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeHostedDeviceOutBandInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeHostedDeviceOutBandInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHostedDeviceOutBandInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHostedDeviceOutBandInfoResponse()
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


    def DescribeOperationResult(self, request):
        """獲取異步操作狀态的完成狀态

        :param request: 調用DescribeOperationResult所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeOperationResultRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeOperationResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOperationResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOperationResultResponse()
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


    def DescribeOsInfo(self, request):
        """查詢指定機型所支援的作業系統

        :param request: 調用DescribeOsInfo所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeOsInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeOsInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOsInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOsInfoResponse()
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


    def DescribePsaRegulations(self, request):
        """獲取預授權規則清單

        :param request: 調用DescribePsaRegulations所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribePsaRegulationsRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribePsaRegulationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePsaRegulations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePsaRegulationsResponse()
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


    def DescribeRegions(self, request):
        """查詢地域以及可用區

        :param request: 調用DescribeRegions所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def DescribeRepairTaskConstant(self, request):
        """維修任務配置獲取

        :param request: 調用DescribeRepairTaskConstant所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeRepairTaskConstantRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeRepairTaskConstantResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRepairTaskConstant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRepairTaskConstantResponse()
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


    def DescribeTaskInfo(self, request):
        """獲取用戶維修任務清單及詳細訊息<br>
        <br>
        TaskStatus（任務狀态ID）與狀态中文名的對應關系如下：<br>
        1：未授權<br>
        2：處理中<br>
        3：待确認<br>
        4：未授權-暫不處理<br>
        5：已恢複<br>
        6：待确認-未恢複<br>

        :param request: 調用DescribeTaskInfo所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeTaskInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeTaskInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskInfoResponse()
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


    def DescribeTaskOperationLog(self, request):
        """獲取維修任務操作日志

        :param request: 調用DescribeTaskOperationLog所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeTaskOperationLogRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeTaskOperationLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskOperationLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskOperationLogResponse()
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


    def DescribeUserCmdTaskInfo(self, request):
        """獲取自定義腳本任務詳細訊息

        :param request: 調用DescribeUserCmdTaskInfo所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdTaskInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdTaskInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserCmdTaskInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserCmdTaskInfoResponse()
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


    def DescribeUserCmdTasks(self, request):
        """獲取自定義腳本任務清單

        :param request: 調用DescribeUserCmdTasks所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdTasksRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserCmdTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserCmdTasksResponse()
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


    def DescribeUserCmds(self, request):
        """獲取自定義腳本訊息清單

        :param request: 調用DescribeUserCmds所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdsRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeUserCmdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserCmds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserCmdsResponse()
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


    def ModifyCustomImageAttribute(self, request):
        """用于修改自定義映像名或描述

        :param request: 調用ModifyCustomImageAttribute所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyCustomImageAttributeRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyCustomImageAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCustomImageAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCustomImageAttributeResponse()
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


    def ModifyDeviceAliases(self, request):
        """修改服務器名稱

        :param request: 調用ModifyDeviceAliases所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyDeviceAliasesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyDeviceAliasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDeviceAliases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDeviceAliasesResponse()
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


    def ModifyDeviceAutoRenewFlag(self, request):
        """修改物理機服務器自動續約标志

        :param request: 調用ModifyDeviceAutoRenewFlag所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyDeviceAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyDeviceAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDeviceAutoRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDeviceAutoRenewFlagResponse()
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


    def ModifyLanIp(self, request):
        """修改物理機内網IP（不重灌系統）

        :param request: 調用ModifyLanIp所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyLanIpRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyLanIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLanIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLanIpResponse()
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


    def ModifyPayModePre2Post(self, request):
        """将設備的預付費模式修改爲後付費計費模式，支援批次轉換。（前提是客戶要加入黑石物理機後付費計費的白名單，申請黑石物理機後付費可以聯系Top Cloud 客服）

        :param request: 調用ModifyPayModePre2Post所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyPayModePre2PostRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyPayModePre2PostResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPayModePre2Post", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPayModePre2PostResponse()
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


    def ModifyPsaRegulation(self, request):
        """允許修改規則訊息及關聯故障類型

        :param request: 調用ModifyPsaRegulation所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyPsaRegulationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyPsaRegulationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPsaRegulation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPsaRegulationResponse()
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


    def ModifyUserCmd(self, request):
        """修改自定義腳本

        :param request: 調用ModifyUserCmd所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyUserCmdRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyUserCmdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyUserCmd", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUserCmdResponse()
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


    def OfflineDevices(self, request):
        """銷毀黑石物理機實例：可以銷毀物理機清單中的競價實例，或資源回收筒清單中所有計費模式的實例

        :param request: 調用OfflineDevices所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.OfflineDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.OfflineDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OfflineDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OfflineDevicesResponse()
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


    def RebootDevices(self, request):
        """重啓機器

        :param request: 調用RebootDevices所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.RebootDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.RebootDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RebootDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RebootDevicesResponse()
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


    def RecoverDevices(self, request):
        """恢複資源回收筒中的物理機（僅限後付費的物理機）

        :param request: 調用RecoverDevices所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.RecoverDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.RecoverDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecoverDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecoverDevicesResponse()
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


    def RepairTaskControl(self, request):
        """此介面用于操作維修任務<br>
        入參TaskId爲維修任務ID<br>
        入參Operate表示對維修任務的操作，支援如下取值：<br>
        AuthorizeRepair（授權維修）<br>
        Ignore（暫不提醒）<br>
        ConfirmRecovered（維修完成後，确認故障恢複）<br>
        ConfirmUnRecovered（維修完成後，确認故障未恢複）<br>
        <br>
        操作約束（當前任務狀态(TaskStatus)->對應可執行的操作）：<br>
        未授權(1)->授權維修；暫不處理<br>
        暫不處理(4)->授權維修<br>
        待确認(3)->确認故障恢複；确認故障未恢複<br>
        未恢複(6)->确認故障恢複<br>
        <br>
        對于Ping不可達故障的任務，還允許：<br>
        未授權->确認故障恢複<br>
        暫不處理->确認故障恢複<br>
        <br>
        處理中與已恢複狀态的任務不允許進行操作。<br>
        <br>
        詳細訊息請訪問：https://cloud.tencent.com/document/product/386/18190

        :param request: 調用RepairTaskControl所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.RepairTaskControlRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.RepairTaskControlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RepairTaskControl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RepairTaskControlResponse()
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


    def ResetDevicePassword(self, request):
        """重置服務器密碼

        :param request: 調用ResetDevicePassword所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.ResetDevicePasswordRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ResetDevicePasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetDevicePassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetDevicePasswordResponse()
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


    def ReturnDevices(self, request):
        """退回物理機至資源回收筒，支援批次退還不同計費模式的物理機（包括預付費、後付費、預付費轉後付費）

        :param request: 調用ReturnDevices所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.ReturnDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ReturnDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReturnDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReturnDevicesResponse()
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


    def RunUserCmd(self, request):
        """運作自定義腳本

        :param request: 調用RunUserCmd所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.RunUserCmdRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.RunUserCmdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunUserCmd", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunUserCmdResponse()
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


    def SetOutBandVpnAuthPassword(self, request):
        """設置帶外VPN認證用戶密碼

        :param request: 調用SetOutBandVpnAuthPassword所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.SetOutBandVpnAuthPasswordRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.SetOutBandVpnAuthPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetOutBandVpnAuthPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetOutBandVpnAuthPasswordResponse()
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


    def ShutdownDevices(self, request):
        """關閉服務器

        :param request: 調用ShutdownDevices所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.ShutdownDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ShutdownDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ShutdownDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ShutdownDevicesResponse()
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


    def StartDevices(self, request):
        """開啓服務器

        :param request: 調用StartDevices所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.StartDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.StartDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartDevicesResponse()
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


    def UnbindPsaTag(self, request):
        """解除标簽與預授權規則的綁定

        :param request: 調用UnbindPsaTag所需參數的結構體。
        :type request: :class:`tencentcloud.bm.v20180423.models.UnbindPsaTagRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.UnbindPsaTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindPsaTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindPsaTagResponse()
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