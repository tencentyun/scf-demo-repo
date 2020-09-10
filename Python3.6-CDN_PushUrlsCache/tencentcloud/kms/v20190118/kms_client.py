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


    def AsymmetricRsaDecrypt(self, request):
        """使用指定的RSA非對稱金鑰的私鑰進行數據解密，密文必須是使用對應公鑰加密的。處于Enabled 狀态的非對稱金鑰才能進行解密操作。

        :param request: Request instance for AsymmetricRsaDecrypt.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.AsymmetricRsaDecryptRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.AsymmetricRsaDecryptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AsymmetricRsaDecrypt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AsymmetricRsaDecryptResponse()
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


    def AsymmetricSm2Decrypt(self, request):
        """使用指定的SM2非對稱金鑰的私鑰進行數據解密，密文必須是使用對應公鑰加密的。處于Enabled 狀态的非對稱金鑰才能進行解密操作。傳入的密文的長度不能超過256位元。

        :param request: Request instance for AsymmetricSm2Decrypt.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.AsymmetricSm2DecryptRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.AsymmetricSm2DecryptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AsymmetricSm2Decrypt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AsymmetricSm2DecryptResponse()
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


    def CancelKeyDeletion(self, request):
        """取消CMK的計劃删除操作

        :param request: Request instance for CancelKeyDeletion.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.CancelKeyDeletionRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.CancelKeyDeletionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelKeyDeletion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelKeyDeletionResponse()
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


    def CreateKey(self, request):
        """創建用戶管理數據金鑰的主金鑰CMK（Custom Master Key）。

        :param request: Request instance for CreateKey.
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


    def CreateWhiteBoxKey(self, request):
        """創建白盒金鑰。 金鑰個數的上限爲 50。

        :param request: Request instance for CreateWhiteBoxKey.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.CreateWhiteBoxKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.CreateWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWhiteBoxKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWhiteBoxKeyResponse()
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
        """本介面用于解密密文，得到明文數據。

        :param request: Request instance for Decrypt.
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


    def DeleteImportedKeyMaterial(self, request):
        """用于删除導入的金鑰材料，僅對EXTERNAL類型的CMK有效，該介面将CMK設置爲PendingImport 狀态，并不會删除CMK，在重新進行金鑰導入後可繼續使用。徹底删除CMK請使用 ScheduleKeyDeletion 介面。

        :param request: Request instance for DeleteImportedKeyMaterial.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DeleteImportedKeyMaterialRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DeleteImportedKeyMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImportedKeyMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImportedKeyMaterialResponse()
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


    def DeleteWhiteBoxKey(self, request):
        """删除白盒金鑰, 注意：必須先禁用後，才可以删除。

        :param request: Request instance for DeleteWhiteBoxKey.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DeleteWhiteBoxKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DeleteWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWhiteBoxKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWhiteBoxKeyResponse()
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
        """用于獲取指定KeyId的主金鑰屬性詳情訊息。

        :param request: Request instance for DescribeKey.
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
        """該介面用于批次獲取主金鑰屬性訊息。

        :param request: Request instance for DescribeKeys.
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


    def DescribeWhiteBoxDecryptKey(self, request):
        """獲取白盒解密金鑰

        :param request: Request instance for DescribeWhiteBoxDecryptKey.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DescribeWhiteBoxDecryptKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DescribeWhiteBoxDecryptKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWhiteBoxDecryptKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWhiteBoxDecryptKeyResponse()
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


    def DescribeWhiteBoxKey(self, request):
        """展示白盒金鑰的訊息

        :param request: Request instance for DescribeWhiteBoxKey.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DescribeWhiteBoxKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DescribeWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWhiteBoxKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWhiteBoxKeyResponse()
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


    def DescribeWhiteBoxKeyDetails(self, request):
        """獲取白盒金鑰清單

        :param request: Request instance for DescribeWhiteBoxKeyDetails.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DescribeWhiteBoxKeyDetailsRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DescribeWhiteBoxKeyDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWhiteBoxKeyDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWhiteBoxKeyDetailsResponse()
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


    def DescribeWhiteBoxServiceStatus(self, request):
        """獲取白盒金鑰服務狀态

        :param request: Request instance for DescribeWhiteBoxServiceStatus.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DescribeWhiteBoxServiceStatusRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DescribeWhiteBoxServiceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWhiteBoxServiceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWhiteBoxServiceStatusResponse()
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
        """本介面用于禁用一個主金鑰，處于禁用狀态的Key無法用于加密、解密操作。

        :param request: Request instance for DisableKey.
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

        :param request: Request instance for DisableKeyRotation.
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
        """該介面用于批次禁止CMK的使用。

        :param request: Request instance for DisableKeys.
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


    def DisableWhiteBoxKey(self, request):
        """禁用白盒金鑰

        :param request: Request instance for DisableWhiteBoxKey.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DisableWhiteBoxKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DisableWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableWhiteBoxKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableWhiteBoxKeyResponse()
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


    def DisableWhiteBoxKeys(self, request):
        """批次禁用白盒金鑰

        :param request: Request instance for DisableWhiteBoxKeys.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.DisableWhiteBoxKeysRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.DisableWhiteBoxKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableWhiteBoxKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableWhiteBoxKeysResponse()
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
        """用于啓用一個指定的CMK。

        :param request: Request instance for EnableKey.
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

        :param request: Request instance for EnableKeyRotation.
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
        """該介面用于批次啓用CMK。

        :param request: Request instance for EnableKeys.
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


    def EnableWhiteBoxKey(self, request):
        """啓用白盒金鑰

        :param request: Request instance for EnableWhiteBoxKey.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.EnableWhiteBoxKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.EnableWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableWhiteBoxKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableWhiteBoxKeyResponse()
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


    def EnableWhiteBoxKeys(self, request):
        """批次啓用白盒金鑰

        :param request: Request instance for EnableWhiteBoxKeys.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.EnableWhiteBoxKeysRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.EnableWhiteBoxKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableWhiteBoxKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableWhiteBoxKeysResponse()
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
        """本介面用于加密最多爲4KB任意數據，可用于加密資料庫密碼，RSA Key，或其它較小的敏感訊息。對于應用的數據加密，使用GenerateDataKey生成的DataKey進行本地數據的加解密操作

        :param request: Request instance for Encrypt.
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


    def EncryptByWhiteBox(self, request):
        """使用白盒金鑰進行加密

        :param request: Request instance for EncryptByWhiteBox.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.EncryptByWhiteBoxRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.EncryptByWhiteBoxResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EncryptByWhiteBox", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EncryptByWhiteBoxResponse()
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

        :param request: Request instance for GenerateDataKey.
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


    def GenerateRandom(self, request):
        """随機數生成介面。

        :param request: Request instance for GenerateRandom.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.GenerateRandomRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.GenerateRandomResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GenerateRandom", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenerateRandomResponse()
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

        :param request: Request instance for GetKeyRotationStatus.
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


    def GetParametersForImport(self, request):
        """獲取導入主金鑰（CMK）材料的參數，返回的Token作爲執行ImportKeyMaterial的參數之一，返回的PublicKey用于對自主導入金鑰材料進行加密。返回的Token和PublicKey 24小時後失效，失效後如需重新導入，需要再次調用該介面獲取新的Token和PublicKey。

        :param request: Request instance for GetParametersForImport.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.GetParametersForImportRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.GetParametersForImportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetParametersForImport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetParametersForImportResponse()
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


    def GetPublicKey(self, request):
        """該介面用戶獲取 KeyUsage爲ASYMMETRIC_DECRYPT_RSA_2048 和 ASYMMETRIC_DECRYPT_SM2 的非對稱金鑰的公鑰訊息，使用該公鑰用戶可在本地進行數據加密，使用該公鑰加密的數據只能通過KMS使用對應的私鑰進行解密。只有處于Enabled狀态的非對稱金鑰才可能獲取公鑰。

        :param request: Request instance for GetPublicKey.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.GetPublicKeyRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.GetPublicKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPublicKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPublicKeyResponse()
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
        """用于查詢該用戶是否已開通KMS服務

        :param request: Request instance for GetServiceStatus.
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


    def ImportKeyMaterial(self, request):
        """用于導入金鑰材料。只有類型爲EXTERNAL 的CMK 才可以導入，導入的金鑰材料使用 GetParametersForImport 獲取的金鑰進行加密。可以爲指定的 CMK 重新導入金鑰材料，并重新指定過期時間，但必須導入相同的金鑰材料。CMK 金鑰材料導入後不可以更換金鑰材料。導入的金鑰材料過期或者被删除後，指定的CMK将無法使用，需要再次導入相同的金鑰材料才能正常使用。CMK是獨立的，同樣的金鑰材料可導入不同的 CMK 中，但使用其中一個 CMK 加密的數據無法使用另一個 CMK解密。
        只有Enabled 和 PendingImport狀态的CMK可以導入金鑰材料。

        :param request: Request instance for ImportKeyMaterial.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.ImportKeyMaterialRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.ImportKeyMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportKeyMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportKeyMaterialResponse()
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


    def ListAlgorithms(self, request):
        """列出當前Region支援的加密方式

        :param request: Request instance for ListAlgorithms.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.ListAlgorithmsRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.ListAlgorithmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAlgorithms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAlgorithmsResponse()
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

        :param request: Request instance for ListKeyDetail.
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
        """列出賬号下面狀态爲Enabled， Disabled 和 PendingImport 的CMK KeyId 清單

        :param request: Request instance for ListKeys.
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

        :param request: Request instance for ReEncrypt.
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


    def ScheduleKeyDeletion(self, request):
        """CMK計劃删除介面，用于指定CMK删除的時間，可選時間區間爲[7,30]天

        :param request: Request instance for ScheduleKeyDeletion.
        :type request: :class:`taifucloudcloud.kms.v20190118.models.ScheduleKeyDeletionRequest`
        :rtype: :class:`taifucloudcloud.kms.v20190118.models.ScheduleKeyDeletionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScheduleKeyDeletion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScheduleKeyDeletionResponse()
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
        """用于修改CMK的别名。對于處于PendingDelete狀态的CMK禁止修改。

        :param request: Request instance for UpdateAlias.
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
        """該介面用于對指定的cmk修改描述訊息。對于處于PendingDelete狀态的CMK禁止修改。

        :param request: Request instance for UpdateKeyDescription.
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