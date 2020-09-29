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


class CreateKeyRequest(AbstractModel):
    """CreateKey請求參數結構體

    """

    def __init__(self):
        """
        :param Alias: 作爲金鑰更容易辨識，更容易被人看懂的别名， 不可爲空，1-60個字元或數字的組合
        :type Alias: str
        :param Description: CMK 的描述，最大1024位元
        :type Description: str
        :param KeyUsage: 指定key的用途。目前，僅支援"ENCRYPT_DECRYPT"，預設爲  "ENCRYPT_DECRYPT"，即key用於加密和解密
        :type KeyUsage: str
        :param Type: 指定key類型，1爲當前地域預設類型，預設爲1，且當前只支援該類型
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


class DecryptRequest(AbstractModel):
    """Decrypt請求參數結構體

    """

    def __init__(self):
        """
        :param CiphertextBlob: 被加密的密文數據
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
        :param CiphertextBlob: 加密後的密文
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
        :param KeySpec: 指定生成Datakey的加密算法以及Datakey大小，AES_128或者AES_256。預設爲AES_256
        :type KeySpec: str
        :param NumberOfBytes: 生成的DataKey的長度，同時指定NumberOfBytes和KeySpec時，以NumberOfBytes爲準。最小值爲1， 最大值爲1024
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
        :param CiphertextBlob: DataKey加密後的密文，用戶需要自行保存密文
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
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ServiceEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
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
        :param KeyState: CMK的狀态， Enabled 或者 Disabled 或者 Deleted
        :type KeyState: str
        :param KeyUsage: CMK用途，當前是 ENCRYPT_DECRYPT
        :type KeyUsage: str
        :param Type: CMK類型，當前爲 1 普通類型
        :type Type: int
        :param CreatorUin: 創建者
        :type CreatorUin: int
        :param KeyRotationEnabled: 是否開啓了金鑰輪換功能
        :type KeyRotationEnabled: bool
        :param Owner: CMK的創建者，用戶創建的爲 user，授權各雲産品自動創建的爲對應的産品名
        :type Owner: str
        :param NextRotateTime: 在金鑰輪換開啓狀态下，下次輪換的時間
        :type NextRotateTime: int
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


class ListKeyDetailRequest(AbstractModel):
    """ListKeyDetail請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 含義跟 SQL 查詢的 Offset 一緻，表示本次獲取從按一定順序排列數組的第 Offset 個元素開始，缺省爲0
        :type Offset: int
        :param Limit: 含義跟 SQL 查詢的 Limit 一緻，表示本次獲最多獲取 Limit 個元素。缺省值爲10，最大值爲200
        :type Limit: int
        :param Role: 根據創建者角色篩選，預設 0 表示用戶自己創建的cmk， 1 表示授權其它雲産品自動創建的cmk
        :type Role: int
        :param OrderType: 根據CMK創建時間排序， 0 表示按照降序排序，1表示按照升序排序
        :type OrderType: int
        :param KeyState: 根據CMK狀态篩選， 0表示全部CMK， 1 表示僅查詢Enabled CMK， 2 表示僅查詢Disabled CMK
        :type KeyState: int
        :param SearchKeyAlias: 根據KeyId或者Alias進行模糊比對查詢
        :type SearchKeyAlias: str
        """
        self.Offset = None
        self.Limit = None
        self.Role = None
        self.OrderType = None
        self.KeyState = None
        self.SearchKeyAlias = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Role = params.get("Role")
        self.OrderType = params.get("OrderType")
        self.KeyState = params.get("KeyState")
        self.SearchKeyAlias = params.get("SearchKeyAlias")


class ListKeyDetailResponse(AbstractModel):
    """ListKeyDetail返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: CMK的總數量
        :type TotalCount: int
        :param KeyMetadatas: 返回的屬性訊息清單，此欄位可能返回 null，表示取不到有效值。
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


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias請求參數結構體

    """

    def __init__(self):
        """
        :param Alias: 新的别名，1-64個字元或數字的組合
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
        :param KeyId: 需要修改描述訊息的的CMK ID
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