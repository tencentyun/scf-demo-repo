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

from taifucloudcloud.common.abstract_model import AbstractModel


class AlgorithmInfo(AbstractModel):
    """算法的名稱 和 標識

    """

    def __init__(self):
        """
        :param KeyUsage: 算法的標識
        :type KeyUsage: str
        :param Algorithm: 算法的名稱
        :type Algorithm: str
        """
        self.KeyUsage = None
        self.Algorithm = None


    def _deserialize(self, params):
        self.KeyUsage = params.get("KeyUsage")
        self.Algorithm = params.get("Algorithm")


class AsymmetricRsaDecryptRequest(AbstractModel):
    """AsymmetricRsaDecrypt請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一標識
        :type KeyId: str
        :param Ciphertext: 使用PublicKey加密的密文，Base64編碼
        :type Ciphertext: str
        :param Algorithm: 在使用公鑰加密時對應的算法：當前支援RSAES_PKCS1_V1_5、RSAES_OAEP_SHA_1、RSAES_OAEP_SHA_256
        :type Algorithm: str
        """
        self.KeyId = None
        self.Ciphertext = None
        self.Algorithm = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Ciphertext = params.get("Ciphertext")
        self.Algorithm = params.get("Algorithm")


class AsymmetricRsaDecryptResponse(AbstractModel):
    """AsymmetricRsaDecrypt返回參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一標識
        :type KeyId: str
        :param Plaintext: 解密後的明文，base64編碼
        :type Plaintext: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class AsymmetricSm2DecryptRequest(AbstractModel):
    """AsymmetricSm2Decrypt請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一標識
        :type KeyId: str
        :param Ciphertext: 使用PublicKey加密的密文，Base64編碼。密文長度不能超過256位元。
        :type Ciphertext: str
        """
        self.KeyId = None
        self.Ciphertext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Ciphertext = params.get("Ciphertext")


class AsymmetricSm2DecryptResponse(AbstractModel):
    """AsymmetricSm2Decrypt返回參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一標識
        :type KeyId: str
        :param Plaintext: 解密後的明文，base64編碼
        :type Plaintext: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class CancelKeyDeletionRequest(AbstractModel):
    """CancelKeyDeletion請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 需要被取消删除的CMK的唯一標志
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class CancelKeyDeletionResponse(AbstractModel):
    """CancelKeyDeletion返回參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 唯一標志被取消删除的CMK。
        :type KeyId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class CreateKeyRequest(AbstractModel):
    """CreateKey請求參數結構體

    """

    def __init__(self):
        """
        :param Alias: 作爲金鑰更容易辨識，更容易被人看懂的别名， 不可爲空，1-60個字母數字 - _ 的組合，首字元必須爲字母或者數字。以 kms- 作爲前綴的用於雲産品使用，Alias 不可重複。
        :type Alias: str
        :param Description: CMK 的描述，最大1024位元
        :type Description: str
        :param KeyUsage: 指定key的用途，預設爲  "ENCRYPT_DECRYPT" 表示創建對稱加解密金鑰，其它支援用途 “ASYMMETRIC_DECRYPT_RSA_2048” 表示創建用於加解密的RSA2048非對稱金鑰，“ASYMMETRIC_DECRYPT_SM2” 表示創建用於加解密的SM2非對稱金鑰
        :type KeyUsage: str
        :param Type: 指定key類型，預設爲1，1表示預設類型，由KMS創建CMK金鑰，2 表示EXTERNAL 類型，該類型需要用戶導入金鑰材料，參考 GetParametersForImport 和 ImportKeyMaterial 介面
        :type Type: int
        """
        self.Alias = None
        self.Description = None
        self.KeyUsage = None
        self.Type = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.Description = params.get("Description")
        self.KeyUsage = params.get("KeyUsage")
        self.Type = params.get("Type")


class CreateKeyResponse(AbstractModel):
    """CreateKey返回參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一標識符
        :type KeyId: str
        :param Alias: 作爲金鑰更容易辨識，更容易被人看懂的别名
        :type Alias: str
        :param CreateTime: 金鑰創建時間，unix時間戳
        :type CreateTime: int
        :param Description: CMK的描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param KeyState: CMK的狀态
        :type KeyState: str
        :param KeyUsage: CMK的用途
        :type KeyUsage: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.Alias = None
        self.CreateTime = None
        self.Description = None
        self.KeyState = None
        self.KeyUsage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.Description = params.get("Description")
        self.KeyState = params.get("KeyState")
        self.KeyUsage = params.get("KeyUsage")
        self.RequestId = params.get("RequestId")


class CreateWhiteBoxKeyRequest(AbstractModel):
    """CreateWhiteBoxKey請求參數結構體

    """

    def __init__(self):
        """
        :param Alias: 作爲金鑰更容易辨識，更容易被人看懂的别名， 不可爲空，1-60個字母數字 - _ 的組合，首字元必須爲字母或者數字。Alias不可重複。
        :type Alias: str
        :param Algorithm: 創建金鑰所有的算法類型，支援的取值：AES_256,SM4
        :type Algorithm: str
        :param Description: 金鑰的描述，最大1024位元
        :type Description: str
        """
        self.Alias = None
        self.Algorithm = None
        self.Description = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.Algorithm = params.get("Algorithm")
        self.Description = params.get("Description")


class CreateWhiteBoxKeyResponse(AbstractModel):
    """CreateWhiteBoxKey返回參數結構體

    """

    def __init__(self):
        """
        :param EncryptKey: 用於加密的金鑰，base64編碼
        :type EncryptKey: str
        :param DecryptKey: 用於解密的金鑰，base64編碼
        :type DecryptKey: str
        :param KeyId: 白盒金鑰的全局唯一標識符
        :type KeyId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.EncryptKey = None
        self.DecryptKey = None
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EncryptKey = params.get("EncryptKey")
        self.DecryptKey = params.get("DecryptKey")
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class DecryptRequest(AbstractModel):
    """Decrypt請求參數結構體

    """

    def __init__(self):
        """
        :param CiphertextBlob: 待解密的密文數據
        :type CiphertextBlob: str
        :param EncryptionContext: key/value對的json字串，如果Encrypt指定了該參數，則在調用Decrypt API時需要提供同樣的參數，最大支援1024字元
        :type EncryptionContext: str
        """
        self.CiphertextBlob = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.EncryptionContext = params.get("EncryptionContext")


class DecryptResponse(AbstractModel):
    """Decrypt返回參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一標識
        :type KeyId: str
        :param Plaintext: 解密後的明文。該欄位是base64編碼的，爲了得到原始明文，調用方需要進行base64解碼
        :type Plaintext: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class DeleteImportedKeyMaterialRequest(AbstractModel):
    """DeleteImportedKeyMaterial請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 指定需要删除金鑰材料的EXTERNAL CMK。
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DeleteImportedKeyMaterialResponse(AbstractModel):
    """DeleteImportedKeyMaterial返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWhiteBoxKeyRequest(AbstractModel):
    """DeleteWhiteBoxKey請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 白盒金鑰的全局唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DeleteWhiteBoxKeyResponse(AbstractModel):
    """DeleteWhiteBoxKey返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeKeyRequest(AbstractModel):
    """DescribeKey請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK全局唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DescribeKeyResponse(AbstractModel):
    """DescribeKey返回參數結構體

    """

    def __init__(self):
        """
        :param KeyMetadata: 金鑰屬性訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyMetadata: :class:`taifucloudcloud.kms.v20190118.models.KeyMetadata`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyMetadata = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyMetadata") is not None:
            self.KeyMetadata = KeyMetadata()
            self.KeyMetadata._deserialize(params.get("KeyMetadata"))
        self.RequestId = params.get("RequestId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys請求參數結構體

    """

    def __init__(self):
        """
        :param KeyIds: 查詢CMK的ID清單，批次查詢一次最多支援100個KeyId
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys返回參數結構體

    """

    def __init__(self):
        """
        :param KeyMetadatas: 返回的屬性訊息清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyMetadatas: list of KeyMetadata
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyMetadatas") is not None:
            self.KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self.KeyMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxDecryptKeyRequest(AbstractModel):
    """DescribeWhiteBoxDecryptKey請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 白盒金鑰的全局唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DescribeWhiteBoxDecryptKeyResponse(AbstractModel):
    """DescribeWhiteBoxDecryptKey返回參數結構體

    """

    def __init__(self):
        """
        :param DecryptKey: 白盒解密金鑰，base64編碼
        :type DecryptKey: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DecryptKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DecryptKey = params.get("DecryptKey")
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxKeyDetailsRequest(AbstractModel):
    """DescribeWhiteBoxKeyDetails請求參數結構體

    """

    def __init__(self):
        """
        :param KeyStatus: 過濾條件：金鑰的狀态，0：disabled，1：enabled
        :type KeyStatus: int
        """
        self.KeyStatus = None


    def _deserialize(self, params):
        self.KeyStatus = params.get("KeyStatus")


class DescribeWhiteBoxKeyDetailsResponse(AbstractModel):
    """DescribeWhiteBoxKeyDetails返回參數結構體

    """

    def __init__(self):
        """
        :param KeyInfos: 白盒金鑰訊息清單
        :type KeyInfos: list of WhiteboxKeyInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyInfos") is not None:
            self.KeyInfos = []
            for item in params.get("KeyInfos"):
                obj = WhiteboxKeyInfo()
                obj._deserialize(item)
                self.KeyInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxKeyRequest(AbstractModel):
    """DescribeWhiteBoxKey請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 白盒金鑰的全局唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DescribeWhiteBoxKeyResponse(AbstractModel):
    """DescribeWhiteBoxKey返回參數結構體

    """

    def __init__(self):
        """
        :param KeyInfo: 白盒金鑰訊息
        :type KeyInfo: :class:`taifucloudcloud.kms.v20190118.models.WhiteboxKeyInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyInfo") is not None:
            self.KeyInfo = WhiteboxKeyInfo()
            self.KeyInfo._deserialize(params.get("KeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxServiceStatusRequest(AbstractModel):
    """DescribeWhiteBoxServiceStatus請求參數結構體

    """


class DescribeWhiteBoxServiceStatusResponse(AbstractModel):
    """DescribeWhiteBoxServiceStatus返回參數結構體

    """

    def __init__(self):
        """
        :param ServiceEnabled: 用戶的白盒金鑰服務是否可用
        :type ServiceEnabled: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ServiceEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.RequestId = params.get("RequestId")


class DisableKeyRequest(AbstractModel):
    """DisableKey請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DisableKeyResponse(AbstractModel):
    """DisableKey返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeyRotationRequest(AbstractModel):
    """DisableKeyRotation請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DisableKeyRotationResponse(AbstractModel):
    """DisableKeyRotation返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeysRequest(AbstractModel):
    """DisableKeys請求參數結構體

    """

    def __init__(self):
        """
        :param KeyIds: 需要批次禁用的CMK Id 清單，CMK數量最大支援100
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class DisableKeysResponse(AbstractModel):
    """DisableKeys返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableWhiteBoxKeyRequest(AbstractModel):
    """DisableWhiteBoxKey請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 白盒金鑰的全局唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DisableWhiteBoxKeyResponse(AbstractModel):
    """DisableWhiteBoxKey返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableWhiteBoxKeysRequest(AbstractModel):
    """DisableWhiteBoxKeys請求參數結構體

    """

    def __init__(self):
        """
        :param KeyIds: 白盒金鑰的全局唯一標識符清單。注意：要确保所有提供的KeyId是格式有效的，沒有重複，個數不超過50個，並且都是有效存在的。
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class DisableWhiteBoxKeysResponse(AbstractModel):
    """DisableWhiteBoxKeys返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRequest(AbstractModel):
    """EnableKey請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class EnableKeyResponse(AbstractModel):
    """EnableKey返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRotationRequest(AbstractModel):
    """EnableKeyRotation請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class EnableKeyRotationResponse(AbstractModel):
    """EnableKeyRotation返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeysRequest(AbstractModel):
    """EnableKeys請求參數結構體

    """

    def __init__(self):
        """
        :param KeyIds: 需要批次啓用的CMK Id 清單， CMK數量最大支援100
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class EnableKeysResponse(AbstractModel):
    """EnableKeys返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableWhiteBoxKeyRequest(AbstractModel):
    """EnableWhiteBoxKey請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 白盒金鑰的全局唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class EnableWhiteBoxKeyResponse(AbstractModel):
    """EnableWhiteBoxKey返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableWhiteBoxKeysRequest(AbstractModel):
    """EnableWhiteBoxKeys請求參數結構體

    """

    def __init__(self):
        """
        :param KeyIds: 白盒金鑰的全局唯一標識符清單。注意：要确保所有提供的KeyId是格式有效的，沒有重複，個數不超過50個，並且都是有效存在的。
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class EnableWhiteBoxKeysResponse(AbstractModel):
    """EnableWhiteBoxKeys返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EncryptByWhiteBoxRequest(AbstractModel):
    """EncryptByWhiteBox請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 白盒金鑰的全局唯一標識符
        :type KeyId: str
        :param PlainText: 待加密的文本， base64編碼，文本的原始長度最大不超過4KB
        :type PlainText: str
        :param InitializationVector: 初始化向量，大小爲 16 Bytes，加密算法會使用到, base64編碼；如果不傳，則由後端服務随機生成。用戶需要自行保存該值，作爲解密的參數。
        :type InitializationVector: str
        """
        self.KeyId = None
        self.PlainText = None
        self.InitializationVector = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.PlainText = params.get("PlainText")
        self.InitializationVector = params.get("InitializationVector")


class EncryptByWhiteBoxResponse(AbstractModel):
    """EncryptByWhiteBox返回參數結構體

    """

    def __init__(self):
        """
        :param InitializationVector: 初始化向量，加密算法會使用到, base64編碼。如果由調用方在入參中傳入，則原樣返回。如果調用方沒有傳入，則後端服務随機生成，並返回
        :type InitializationVector: str
        :param CipherText: 加密後的密文，base64編碼
        :type CipherText: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InitializationVector = None
        self.CipherText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InitializationVector = params.get("InitializationVector")
        self.CipherText = params.get("CipherText")
        self.RequestId = params.get("RequestId")


class EncryptRequest(AbstractModel):
    """Encrypt請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: 調用CreateKey生成的CMK全局唯一標識符
        :type KeyId: str
        :param Plaintext: 被加密的明文數據，該欄位必須使用base64編碼，原文最大長度支援4K
        :type Plaintext: str
        :param EncryptionContext: key/value對的json字串，如果指定了該參數，則在調用Decrypt API時需要提供同樣的參數，最大支援1024個字元
        :type EncryptionContext: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.EncryptionContext = params.get("EncryptionContext")


class EncryptResponse(AbstractModel):
    """Encrypt返回參數結構體

    """

    def __init__(self):
        """
        :param CiphertextBlob: 加密後經過base64編碼的密文
        :type CiphertextBlob: str
        :param KeyId: 加密使用的CMK的全局唯一標識
        :type KeyId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CiphertextBlob = None
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class GenerateDataKeyRequest(AbstractModel):
    """GenerateDataKey請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK全局唯一標識符
        :type KeyId: str
        :param KeySpec: 指定生成Datakey的加密算法以及Datakey大小，AES_128或者AES_256。KeySpec 和 NumberOfBytes 必須指定一個
        :type KeySpec: str
        :param NumberOfBytes: 生成的DataKey的長度，同時指定NumberOfBytes和KeySpec時，以NumberOfBytes爲準。最小值爲1， 最大值爲1024。KeySpec 和 NumberOfBytes 必須指定一個
        :type NumberOfBytes: int
        :param EncryptionContext: key/value對的json字串，如果使用該欄位，則返回的DataKey在解密時需要填入相同的字串
        :type EncryptionContext: str
        """
        self.KeyId = None
        self.KeySpec = None
        self.NumberOfBytes = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeySpec = params.get("KeySpec")
        self.NumberOfBytes = params.get("NumberOfBytes")
        self.EncryptionContext = params.get("EncryptionContext")


class GenerateDataKeyResponse(AbstractModel):
    """GenerateDataKey返回參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一標識
        :type KeyId: str
        :param Plaintext: 生成的DataKey的明文，該明文使用base64編碼，用戶需要使用base64解碼得到明文
        :type Plaintext: str
        :param CiphertextBlob: DataKey加密後經過base64編碼的密文，用戶需要自行保存密文
        :type CiphertextBlob: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.CiphertextBlob = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.RequestId = params.get("RequestId")


class GenerateRandomRequest(AbstractModel):
    """GenerateRandom請求參數結構體

    """

    def __init__(self):
        """
        :param NumberOfBytes: 生成的随機數的長度。最小值爲1， 最大值爲1024。
        :type NumberOfBytes: int
        """
        self.NumberOfBytes = None


    def _deserialize(self, params):
        self.NumberOfBytes = params.get("NumberOfBytes")


class GenerateRandomResponse(AbstractModel):
    """GenerateRandom返回參數結構體

    """

    def __init__(self):
        """
        :param Plaintext: 生成的随機數的明文，該明文使用base64編碼，用戶需要使用base64解碼得到明文。
        :type Plaintext: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class GetKeyRotationStatusRequest(AbstractModel):
    """GetKeyRotationStatus請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一標識符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class GetKeyRotationStatusResponse(AbstractModel):
    """GetKeyRotationStatus返回參數結構體

    """

    def __init__(self):
        """
        :param KeyRotationEnabled: 金鑰輪換是否開啓
        :type KeyRotationEnabled: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyRotationEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyRotationEnabled = params.get("KeyRotationEnabled")
        self.RequestId = params.get("RequestId")


class GetParametersForImportRequest(AbstractModel):
    """GetParametersForImport請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一標識，獲取金鑰參數的CMK必須是EXTERNAL類型，即在CreateKey時指定Type=2 類型的CMK。
        :type KeyId: str
        :param WrappingAlgorithm: 指定加密金鑰材料的算法，目前支援RSAES_PKCS1_V1_5、RSAES_OAEP_SHA_1、RSAES_OAEP_SHA_256
        :type WrappingAlgorithm: str
        :param WrappingKeySpec: 指定加密金鑰材料的類型，目前只支援RSA_2048
        :type WrappingKeySpec: str
        """
        self.KeyId = None
        self.WrappingAlgorithm = None
        self.WrappingKeySpec = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.WrappingAlgorithm = params.get("WrappingAlgorithm")
        self.WrappingKeySpec = params.get("WrappingKeySpec")


class GetParametersForImportResponse(AbstractModel):
    """GetParametersForImport返回參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一標識，用於指定目標導入金鑰材料的CMK。
        :type KeyId: str
        :param ImportToken: 導入金鑰材料需要的token，用於作爲 ImportKeyMaterial 的參數。
        :type ImportToken: str
        :param PublicKey: 用於加密金鑰材料的RSA公鑰，base64編碼。使用PublicKey base64解碼後的公鑰将導入金鑰進行加密後作爲 ImportKeyMaterial 的參數。
        :type PublicKey: str
        :param ParametersValidTo: 該導出token和公鑰的有效期，超過該時間後無法導入，需要重新調用GetParametersForImport獲取。
        :type ParametersValidTo: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.ImportToken = None
        self.PublicKey = None
        self.ParametersValidTo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.ImportToken = params.get("ImportToken")
        self.PublicKey = params.get("PublicKey")
        self.ParametersValidTo = params.get("ParametersValidTo")
        self.RequestId = params.get("RequestId")


class GetPublicKeyRequest(AbstractModel):
    """GetPublicKey請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一標識。
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class GetPublicKeyResponse(AbstractModel):
    """GetPublicKey返回參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一標識。
        :type KeyId: str
        :param PublicKey: 經過base64編碼的公鑰内容。
        :type PublicKey: str
        :param PublicKeyPem: PEM格式的公鑰内容。
        :type PublicKeyPem: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.PublicKey = None
        self.PublicKeyPem = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.PublicKey = params.get("PublicKey")
        self.PublicKeyPem = params.get("PublicKeyPem")
        self.RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus請求參數結構體

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus返回參數結構體

    """

    def __init__(self):
        """
        :param ServiceEnabled: KMS服務是否開通， true 表示已開通
        :type ServiceEnabled: bool
        :param InvalidType: 服務不可用類型： 0-未購買，1-正常， 2-欠費停服， 3-資源釋放
注意：此欄位可能返回 null，表示取不到有效值。
        :type InvalidType: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ServiceEnabled = None
        self.InvalidType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.InvalidType = params.get("InvalidType")
        self.RequestId = params.get("RequestId")


class ImportKeyMaterialRequest(AbstractModel):
    """ImportKeyMaterial請求參數結構體

    """

    def __init__(self):
        """
        :param EncryptedKeyMaterial: 使用GetParametersForImport 返回的PublicKey加密後的金鑰材料base64編碼。對於國密版本region的KMS，導入的金鑰材料長度要求爲 128 bit，FIPS版本region的KMS， 導入的金鑰材料長度要求爲 256 bit。
        :type EncryptedKeyMaterial: str
        :param ImportToken: 通過調用GetParametersForImport獲得的導入令牌。
        :type ImportToken: str
        :param KeyId: 指定導入金鑰材料的CMK，需要和GetParametersForImport 指定的CMK相同。
        :type KeyId: str
        :param ValidTo: 金鑰材料過期時間 unix 時間戳，不指定或者 0 表示金鑰材料不會過期，若指定過期時間，需要大於當前時間點，最大支援 2147443200。
        :type ValidTo: int
        """
        self.EncryptedKeyMaterial = None
        self.ImportToken = None
        self.KeyId = None
        self.ValidTo = None


    def _deserialize(self, params):
        self.EncryptedKeyMaterial = params.get("EncryptedKeyMaterial")
        self.ImportToken = params.get("ImportToken")
        self.KeyId = params.get("KeyId")
        self.ValidTo = params.get("ValidTo")


class ImportKeyMaterialResponse(AbstractModel):
    """ImportKeyMaterial返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Key(AbstractModel):
    """返回CMK清單訊息

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一標識。
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class KeyMetadata(AbstractModel):
    """CMK屬性訊息

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一標識
        :type KeyId: str
        :param Alias: 作爲金鑰更容易辨識，更容易被人看懂的别名
        :type Alias: str
        :param CreateTime: 金鑰創建時間
        :type CreateTime: int
        :param Description: CMK的描述
        :type Description: str
        :param KeyState: CMK的狀态， 取值爲：Enabled | Disabled | PendingDelete | PendingImport
        :type KeyState: str
        :param KeyUsage: CMK用途，取值爲: ENCRYPT_DECRYPT | ASYMMETRIC_DECRYPT_RSA_2048 | ASYMMETRIC_DECRYPT_SM2
        :type KeyUsage: str
        :param Type: CMK類型，2 表示符合FIPS標準，4表示符合國密標準
        :type Type: int
        :param CreatorUin: 創建者
        :type CreatorUin: int
        :param KeyRotationEnabled: 是否開啓了金鑰輪換功能
        :type KeyRotationEnabled: bool
        :param Owner: CMK的創建者，用戶創建的爲 user，授權各雲産品自動創建的爲對應的産品名
        :type Owner: str
        :param NextRotateTime: 在金鑰輪換開啓狀态下，下次輪換的時間
        :type NextRotateTime: int
        :param DeletionDate: 計劃删除的時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeletionDate: int
        :param Origin: CMK 金鑰材料類型，由KMS創建的爲： TENCENT_KMS， 由用戶導入的類型爲：EXTERNAL
注意：此欄位可能返回 null，表示取不到有效值。
        :type Origin: str
        :param ValidTo: 在Origin爲  EXTERNAL 時有效，表示金鑰材料的有效日期， 0 表示不過期
注意：此欄位可能返回 null，表示取不到有效值。
        :type ValidTo: int
        :param ResourceId: 資源ID，格式：creatorUin/$creatorUin/$keyId
        :type ResourceId: str
        """
        self.KeyId = None
        self.Alias = None
        self.CreateTime = None
        self.Description = None
        self.KeyState = None
        self.KeyUsage = None
        self.Type = None
        self.CreatorUin = None
        self.KeyRotationEnabled = None
        self.Owner = None
        self.NextRotateTime = None
        self.DeletionDate = None
        self.Origin = None
        self.ValidTo = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.Description = params.get("Description")
        self.KeyState = params.get("KeyState")
        self.KeyUsage = params.get("KeyUsage")
        self.Type = params.get("Type")
        self.CreatorUin = params.get("CreatorUin")
        self.KeyRotationEnabled = params.get("KeyRotationEnabled")
        self.Owner = params.get("Owner")
        self.NextRotateTime = params.get("NextRotateTime")
        self.DeletionDate = params.get("DeletionDate")
        self.Origin = params.get("Origin")
        self.ValidTo = params.get("ValidTo")
        self.ResourceId = params.get("ResourceId")


class ListAlgorithmsRequest(AbstractModel):
    """ListAlgorithms請求參數結構體

    """


class ListAlgorithmsResponse(AbstractModel):
    """ListAlgorithms返回參數結構體

    """

    def __init__(self):
        """
        :param SymmetricAlgorithms: 本地區支援的對稱加密算法
        :type SymmetricAlgorithms: list of AlgorithmInfo
        :param AsymmetricAlgorithms: 本地區支援的非對稱加密算法
        :type AsymmetricAlgorithms: list of AlgorithmInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SymmetricAlgorithms = None
        self.AsymmetricAlgorithms = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SymmetricAlgorithms") is not None:
            self.SymmetricAlgorithms = []
            for item in params.get("SymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self.SymmetricAlgorithms.append(obj)
        if params.get("AsymmetricAlgorithms") is not None:
            self.AsymmetricAlgorithms = []
            for item in params.get("AsymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self.AsymmetricAlgorithms.append(obj)
        self.RequestId = params.get("RequestId")


class ListKeyDetailRequest(AbstractModel):
    """ListKeyDetail請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 含義跟 SQL 查詢的 Offset 一緻，表示本次獲取從按一定順序排列數組的第 Offset 個元素開始，缺省爲0
        :type Offset: int
        :param Limit: 含義跟 SQL 查詢的 Limit 一緻，表示本次最多獲取 Limit 個元素。缺省值爲10，最大值爲200
        :type Limit: int
        :param Role: 根據創建者角色篩選，預設 0 表示用戶自己創建的cmk， 1 表示授權其它雲産品自動創建的cmk
        :type Role: int
        :param OrderType: 根據CMK創建時間排序， 0 表示按照降序排序，1表示按照升序排序
        :type OrderType: int
        :param KeyState: 根據CMK狀态篩選， 0表示全部CMK， 1 表示僅查詢Enabled CMK， 2 表示僅查詢Disabled CMK，3 表示查詢PendingDelete 狀态的CMK(處於計劃删除狀态的Key)，4 表示查詢 PendingImport 狀态的CMK
        :type KeyState: int
        :param SearchKeyAlias: 根據KeyId或者Alias進行模糊比對查詢
        :type SearchKeyAlias: str
        :param Origin: 根據CMK類型篩選， "TENCENT_KMS" 表示篩選金鑰材料由KMS創建的CMK， "EXTERNAL" 表示篩選金鑰材料需要用戶導入的 EXTERNAL類型CMK，"ALL" 或者不設置表示兩種類型都查詢，大小寫敏感。
        :type Origin: str
        :param KeyUsage: 根據CMK的KeyUsage篩選，ALL表示篩選全部，可使用的參數爲：ALL 或 ENCRYPT_DECRYPT 或 ASYMMETRIC_DECRYPT_RSA_2048 或 ASYMMETRIC_DECRYPT_SM2，爲空則預設篩選ENCRYPT_DECRYPT類型
        :type KeyUsage: str
        """
        self.Offset = None
        self.Limit = None
        self.Role = None
        self.OrderType = None
        self.KeyState = None
        self.SearchKeyAlias = None
        self.Origin = None
        self.KeyUsage = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Role = params.get("Role")
        self.OrderType = params.get("OrderType")
        self.KeyState = params.get("KeyState")
        self.SearchKeyAlias = params.get("SearchKeyAlias")
        self.Origin = params.get("Origin")
        self.KeyUsage = params.get("KeyUsage")


class ListKeyDetailResponse(AbstractModel):
    """ListKeyDetail返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: CMK的總數量
        :type TotalCount: int
        :param KeyMetadatas: 返回的屬性訊息清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyMetadatas: list of KeyMetadata
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.KeyMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KeyMetadatas") is not None:
            self.KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self.KeyMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class ListKeysRequest(AbstractModel):
    """ListKeys請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 含義跟 SQL 查詢的 Offset 一緻，表示本次獲取從按一定順序排列數組的第 Offset 個元素開始，缺省爲0
        :type Offset: int
        :param Limit: 含義跟 SQL 查詢的 Limit 一緻，表示本次獲最多獲取 Limit 個元素。缺省值爲10，最大值爲200
        :type Limit: int
        :param Role: 根據創建者角色篩選，預設 0 表示用戶自己創建的cmk， 1 表示授權其它雲産品自動創建的cmk
        :type Role: int
        """
        self.Offset = None
        self.Limit = None
        self.Role = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Role = params.get("Role")


class ListKeysResponse(AbstractModel):
    """ListKeys返回參數結構體

    """

    def __init__(self):
        """
        :param Keys: CMK清單數組
注意：此欄位可能返回 null，表示取不到有效值。
        :type Keys: list of Key
        :param TotalCount: CMK的總數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Keys = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ReEncryptRequest(AbstractModel):
    """ReEncrypt請求參數結構體

    """

    def __init__(self):
        """
        :param CiphertextBlob: 需要重新加密的密文
        :type CiphertextBlob: str
        :param DestinationKeyId: 重新加密使用的CMK，如果爲空，則使用密文原有的CMK重新加密（若金鑰沒有輪換則密文不會重新整理）
        :type DestinationKeyId: str
        :param SourceEncryptionContext: CiphertextBlob 密文加密時使用的key/value對的json字串。如果加密時未使用，則爲空
        :type SourceEncryptionContext: str
        :param DestinationEncryptionContext: 重新加密使用的key/value對的json字串，如果使用該欄位，則返回的新密文在解密時需要填入相同的字串
        :type DestinationEncryptionContext: str
        """
        self.CiphertextBlob = None
        self.DestinationKeyId = None
        self.SourceEncryptionContext = None
        self.DestinationEncryptionContext = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.DestinationKeyId = params.get("DestinationKeyId")
        self.SourceEncryptionContext = params.get("SourceEncryptionContext")
        self.DestinationEncryptionContext = params.get("DestinationEncryptionContext")


class ReEncryptResponse(AbstractModel):
    """ReEncrypt返回參數結構體

    """

    def __init__(self):
        """
        :param CiphertextBlob: 重新加密後的密文
        :type CiphertextBlob: str
        :param KeyId: 重新加密使用的CMK
        :type KeyId: str
        :param SourceKeyId: 重新加密前密文使用的CMK
        :type SourceKeyId: str
        :param ReEncrypted: true表示密文已經重新加密。同一個CMK進行重加密，在金鑰沒有發生輪換的情況下不會進行實際重新加密操作，返回原密文
        :type ReEncrypted: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CiphertextBlob = None
        self.KeyId = None
        self.SourceKeyId = None
        self.ReEncrypted = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.KeyId = params.get("KeyId")
        self.SourceKeyId = params.get("SourceKeyId")
        self.ReEncrypted = params.get("ReEncrypted")
        self.RequestId = params.get("RequestId")


class ScheduleKeyDeletionRequest(AbstractModel):
    """ScheduleKeyDeletion請求參數結構體

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一標志
        :type KeyId: str
        :param PendingWindowInDays: 計劃删除時間區間[7,30]
        :type PendingWindowInDays: int
        """
        self.KeyId = None
        self.PendingWindowInDays = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.PendingWindowInDays = params.get("PendingWindowInDays")


class ScheduleKeyDeletionResponse(AbstractModel):
    """ScheduleKeyDeletion返回參數結構體

    """

    def __init__(self):
        """
        :param DeletionDate: 計劃删除執行時間
        :type DeletionDate: int
        :param KeyId: 唯一標志被計劃删除的CMK
        :type KeyId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeletionDate = None
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeletionDate = params.get("DeletionDate")
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias請求參數結構體

    """

    def __init__(self):
        """
        :param Alias: 新的别名，1-60個字元或數字的組合
        :type Alias: str
        :param KeyId: CMK的全局唯一標識符
        :type KeyId: str
        """
        self.Alias = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.KeyId = params.get("KeyId")


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateKeyDescriptionRequest(AbstractModel):
    """UpdateKeyDescription請求參數結構體

    """

    def __init__(self):
        """
        :param Description: 新的描述訊息，最大支援1024位元
        :type Description: str
        :param KeyId: 需要修改描述訊息的CMK ID
        :type KeyId: str
        """
        self.Description = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.KeyId = params.get("KeyId")


class UpdateKeyDescriptionResponse(AbstractModel):
    """UpdateKeyDescription返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WhiteboxKeyInfo(AbstractModel):
    """白盒金鑰訊息

    """

    def __init__(self):
        """
        :param KeyId: 白盒金鑰的全局唯一標識符
        :type KeyId: str
        :param Alias: 作爲金鑰更容易辨識，更容易被人看懂的别名， 不可爲空，1-60個字母數字 - _ 的組合，首字元必須爲字母或者數字. 不可重複
        :type Alias: str
        :param CreatorUin: 創建者
        :type CreatorUin: int
        :param Description: 金鑰的描述訊息
        :type Description: str
        :param CreateTime: 金鑰創建時間，Unix時間戳
        :type CreateTime: int
        :param Status: 白盒金鑰的狀态， 取值爲：Enabled | Disabled
        :type Status: str
        :param OwnerUin: 創建者
        :type OwnerUin: int
        :param Algorithm: 金鑰所用的算法類型
        :type Algorithm: str
        :param EncryptKey: 白盒加密金鑰，base64編碼
        :type EncryptKey: str
        :param DecryptKey: 白盒解密金鑰，base64編碼
        :type DecryptKey: str
        :param ResourceId: 資源ID，格式：creatorUin/$creatorUin/$keyId
        :type ResourceId: str
        """
        self.KeyId = None
        self.Alias = None
        self.CreatorUin = None
        self.Description = None
        self.CreateTime = None
        self.Status = None
        self.OwnerUin = None
        self.Algorithm = None
        self.EncryptKey = None
        self.DecryptKey = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreatorUin = params.get("CreatorUin")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.OwnerUin = params.get("OwnerUin")
        self.Algorithm = params.get("Algorithm")
        self.EncryptKey = params.get("EncryptKey")
        self.DecryptKey = params.get("DecryptKey")
        self.ResourceId = params.get("ResourceId")