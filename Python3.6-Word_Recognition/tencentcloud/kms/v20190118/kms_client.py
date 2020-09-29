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
from taifucloudcloud.kms.v20190118 import models


class KmsClient(AbstractClient):
    _apiVersion = '2019-01-18'
    _endpoint = 'kms.taifucloudcloudapi.com'


    def CreateKey(self, request):
        """創建用戶管理數據金鑰的主金鑰CMK（Custom Master Key）。

        :param request: 調用CreateKey所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.CreateKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.CreateKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateKeyResponse()
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


    def Decrypt(self, request):
        """本介面用於解密密文，得到明文數據。

        :param request: 調用Decrypt所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DecryptRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DecryptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Decrypt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DecryptResponse()
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


    def DescribeKey(self, request):
        """用於獲取指定KeyId的主金鑰屬性詳情訊息。

        :param request: 調用DescribeKey所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DescribeKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DescribeKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKeyResponse()
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


    def DescribeKeys(self, request):
        """該介面用於批次獲取主金鑰屬性訊息。

        :param request: 調用DescribeKeys所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DescribeKeysRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DescribeKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKeysResponse()
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


    def DisableKey(self, request):
        """本介面用於禁用一個主金鑰，處於禁用狀态的Key無法用於加密、解密操作。

        :param request: 調用DisableKey所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DisableKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DisableKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableKeyResponse()
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


    def DisableKeyRotation(self, request):
        """對指定的CMK禁止金鑰輪換功能。

        :param request: 調用DisableKeyRotation所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DisableKeyRotationRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DisableKeyRotationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableKeyRotation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableKeyRotationResponse()
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


    def DisableKeys(self, request):
        """該介面用於批次禁止CMK的使用。

        :param request: 調用DisableKeys所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DisableKeysRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DisableKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableKeysResponse()
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


    def EnableKey(self, request):
        """用於啓用一個指定的CMK。

        :param request: 調用EnableKey所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.EnableKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.EnableKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableKeyResponse()
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


    def EnableKeyRotation(self, request):
        """對指定的CMK開啓金鑰輪換功能。

        :param request: 調用EnableKeyRotation所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.EnableKeyRotationRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.EnableKeyRotationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableKeyRotation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableKeyRotationResponse()
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


    def EnableKeys(self, request):
        """該介面用於批次啓用CMK。

        :param request: 調用EnableKeys所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.EnableKeysRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.EnableKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableKeysResponse()
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


    def Encrypt(self, request):
        """本介面用於加密最多爲4KB任意數據，可用於加密資料庫密碼，RSA Key，或其它較小的敏感訊息。對於應用的數據加密，使用GenerateDataKey生成的DataKey進行本地數據的加解密操作

        :param request: 調用Encrypt所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.EncryptRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.EncryptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Encrypt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EncryptResponse()
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


    def GenerateDataKey(self, request):
        """本介面生成一個數據金鑰，您可以用這個金鑰進行本地數據的加密。

        :param request: 調用GenerateDataKey所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.GenerateDataKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.GenerateDataKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GenerateDataKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenerateDataKeyResponse()
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


    def GetKeyRotationStatus(self, request):
        """查詢指定的CMK是否開啓了金鑰輪換功能。

        :param request: 調用GetKeyRotationStatus所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.GetKeyRotationStatusRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.GetKeyRotationStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetKeyRotationStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetKeyRotationStatusResponse()
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


    def GetServiceStatus(self, request):
        """用於查詢該用戶是否已開通KMS服務

        :param request: 調用GetServiceStatus所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.GetServiceStatusRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.GetServiceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetServiceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetServiceStatusResponse()
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


    def ListKeyDetail(self, request):
        """根據指定Offset和Limit獲取主金鑰清單詳情。

        :param request: 調用ListKeyDetail所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.ListKeyDetailRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.ListKeyDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListKeyDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListKeyDetailResponse()
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


    def ListKeys(self, request):
        """列出賬號下面的金鑰清單（KeyId訊息）。

        :param request: 調用ListKeys所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.ListKeysRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.ListKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListKeysResponse()
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


    def ReEncrypt(self, request):
        """使用指定CMK對密文重新加密。

        :param request: 調用ReEncrypt所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.ReEncryptRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.ReEncryptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReEncrypt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReEncryptResponse()
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


    def UpdateAlias(self, request):
        """用於修改CMK的别名。

        :param request: 調用UpdateAlias所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.UpdateAliasRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.UpdateAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAliasResponse()
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


    def UpdateKeyDescription(self, request):
        """該介面用於對指定的cmk修改描述訊息。

        :param request: 調用UpdateKeyDescription所需參數的結構體。
        :type request: :class:`taifucloudcloud.kms.v20190118.models.UpdateKeyDescriptionRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.UpdateKeyDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateKeyDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateKeyDescriptionResponse()
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