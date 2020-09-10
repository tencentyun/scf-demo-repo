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


class CreateSecretRequest(AbstractModel):
    """CreateSecret請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 憑據名稱，同一region内不可重複，最長128位元，使用字母、數字或者 - _ 的組合，第一個字元必須爲字母或者數字。
        :type SecretName: str
        :param VersionId: 憑據版本，查詢憑據訊息時需要根據SecretName 和 VersionId進行查詢，最長64 位元，使用字母、數字或者 - _ . 的組合并且以字母或數字開頭。
        :type VersionId: str
        :param Description: 描述訊息，用于詳細描述用途等，最大支援2048位元。
        :type Description: str
        :param KmsKeyId: 指定對憑據進行加密的KMS CMK。如果爲空則表示使用Secrets Manager爲您預設創建的CMK進行加密。您也可以指定在同region 下自行創建的KMS CMK進行加密。
        :type KmsKeyId: str
        :param SecretBinary: 二進制憑據訊息base64編碼後的明文。SecretBinary 和 SecretString 必須且只能設置一個，最大支援4096位元。
        :type SecretBinary: str
        :param SecretString: 文本類型憑據訊息明文（不需要進行base64編碼）。SecretBinary 和 SecretString 必須且只能設置一個，，最大支援4096位元。
        :type SecretString: str
        """
        self.SecretName = None
        self.VersionId = None
        self.Description = None
        self.KmsKeyId = None
        self.SecretBinary = None
        self.SecretString = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")


class CreateSecretResponse(AbstractModel):
    """CreateSecret返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 新創建的憑據名稱。
        :type SecretName: str
        :param VersionId: 新創建的憑據版本。
        :type VersionId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class DeleteSecretRequest(AbstractModel):
    """DeleteSecret請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定需要删除的憑據名稱。
        :type SecretName: str
        :param RecoveryWindowInDays: 指定計劃删除日期，單位（天），0（預設）表示立即删除， 1-30 表示預留的天數，超出該日期之後徹底删除。
        :type RecoveryWindowInDays: int
        """
        self.SecretName = None
        self.RecoveryWindowInDays = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RecoveryWindowInDays = params.get("RecoveryWindowInDays")


class DeleteSecretResponse(AbstractModel):
    """DeleteSecret返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定删除的憑據名稱。
        :type SecretName: str
        :param DeleteTime: 憑據删除的日期，unix時間戳。
        :type DeleteTime: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.DeleteTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.DeleteTime = params.get("DeleteTime")
        self.RequestId = params.get("RequestId")


class DeleteSecretVersionRequest(AbstractModel):
    """DeleteSecretVersion請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定憑據名稱。
        :type SecretName: str
        :param VersionId: 指定該名稱下需要删除的憑據的版本号。
        :type VersionId: str
        """
        self.SecretName = None
        self.VersionId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")


class DeleteSecretVersionResponse(AbstractModel):
    """DeleteSecretVersion返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 憑據名稱。
        :type SecretName: str
        :param VersionId: 憑據版本号。
        :type VersionId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class DescribeSecretRequest(AbstractModel):
    """DescribeSecret請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定需要獲取憑據詳細訊息的憑據名稱。
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")


class DescribeSecretResponse(AbstractModel):
    """DescribeSecret返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 憑據名稱。
        :type SecretName: str
        :param Description: 憑據描述訊息。
        :type Description: str
        :param KmsKeyId: 用于加密的KMS CMK ID。
        :type KmsKeyId: str
        :param CreateUin: 創建者UIN。
        :type CreateUin: int
        :param Status: 憑據狀态：Enabled、Disabled、PendingDelete
        :type Status: str
        :param DeleteTime: 删除日期，uinx 時間戳，非計劃删除狀态的憑據爲0。
        :type DeleteTime: int
        :param CreateTime: 創建日期。
        :type CreateTime: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.Description = None
        self.KmsKeyId = None
        self.CreateUin = None
        self.Status = None
        self.DeleteTime = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.CreateUin = params.get("CreateUin")
        self.Status = params.get("Status")
        self.DeleteTime = params.get("DeleteTime")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class DisableSecretRequest(AbstractModel):
    """DisableSecret請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定停用的憑據名稱。
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")


class DisableSecretResponse(AbstractModel):
    """DisableSecret返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 停用的憑據名稱。
        :type SecretName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class EnableSecretRequest(AbstractModel):
    """EnableSecret請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定啓用憑據的名稱。
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")


class EnableSecretResponse(AbstractModel):
    """EnableSecret返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 啓用的憑據名稱。
        :type SecretName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class GetRegionsRequest(AbstractModel):
    """GetRegions請求參數結構體

    """


class GetRegionsResponse(AbstractModel):
    """GetRegions返回參數結構體

    """

    def __init__(self):
        """
        :param Regions: region清單。
        :type Regions: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Regions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Regions = params.get("Regions")
        self.RequestId = params.get("RequestId")


class GetSecretValueRequest(AbstractModel):
    """GetSecretValue請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定憑據的名稱。
        :type SecretName: str
        :param VersionId: 指定對應憑據的版本号。
        :type VersionId: str
        """
        self.SecretName = None
        self.VersionId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")


class GetSecretValueResponse(AbstractModel):
    """GetSecretValue返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 憑據的名稱。
        :type SecretName: str
        :param VersionId: 該憑據對應的版本号。
        :type VersionId: str
        :param SecretBinary: 在創建憑據(CreateSecret)時，如果指定的是二進制數據，則該欄位爲返回結果，并且使用base64進行編碼，應用方需要進行base64解碼後獲取原始數據。SecretBinary和SecretString只有一個不爲空。
        :type SecretBinary: str
        :param SecretString: 在創建憑據(CreateSecret)時，如果指定的是普通文本數據，則該欄位爲返回結果。SecretBinary和SecretString只有一個不爲空。
        :type SecretString: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.SecretBinary = None
        self.SecretString = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")
        self.RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus請求參數結構體

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus返回參數結構體

    """

    def __init__(self):
        """
        :param ServiceEnabled: true表示服務已開通，false 表示服務尚未開通。
        :type ServiceEnabled: bool
        :param InvalidType: 服務不可用類型： 0-未購買，1-正常， 2-欠費停服， 3-資源釋放。
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


class ListSecretVersionIdsRequest(AbstractModel):
    """ListSecretVersionIds請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 憑據名稱。
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")


class ListSecretVersionIdsResponse(AbstractModel):
    """ListSecretVersionIds返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 憑據名稱。
        :type SecretName: str
        :param Versions: VersionId清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Versions: list of VersionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.Versions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = VersionInfo()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.RequestId = params.get("RequestId")


class ListSecretsRequest(AbstractModel):
    """ListSecrets請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 查詢清單的起始位置，以0開始，不設置預設爲0。
        :type Offset: int
        :param Limit: 單次查詢返回的最大數量，0或不設置則使用預設值 20。
        :type Limit: int
        :param OrderType: 根據創建時間的排序方式，0或者不設置則使用降序排序， 1 表示升序排序。
        :type OrderType: int
        :param State: 根據憑據狀态進行過濾，預設爲0表示查詢全部，1 表示查詢Enabed 憑據清單，2表示查詢Disabled 憑據清單， 3 表示查詢PendingDelete 憑據清單。
        :type State: int
        :param SearchSecretName: 根據憑據名稱進行過濾，爲空表示不過濾。
        :type SearchSecretName: str
        """
        self.Offset = None
        self.Limit = None
        self.OrderType = None
        self.State = None
        self.SearchSecretName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderType = params.get("OrderType")
        self.State = params.get("State")
        self.SearchSecretName = params.get("SearchSecretName")


class ListSecretsResponse(AbstractModel):
    """ListSecrets返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 根據State和SearchSecretName 篩選的憑據總數。
        :type TotalCount: int
        :param SecretMetadatas: 返回憑據訊息清單。
        :type SecretMetadatas: list of SecretMetadata
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SecretMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SecretMetadatas") is not None:
            self.SecretMetadatas = []
            for item in params.get("SecretMetadatas"):
                obj = SecretMetadata()
                obj._deserialize(item)
                self.SecretMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class PutSecretValueRequest(AbstractModel):
    """PutSecretValue請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定需要增加版本的憑據名稱。
        :type SecretName: str
        :param VersionId: 指定新增加的版本号，最長64 位元，使用字母、數字或者 - _ . 的組合并且以字母或數字開頭。
        :type VersionId: str
        :param SecretBinary: 二進制憑據訊息，使用base64編碼。SecretBinary 和 SecretString 必須且只能設置一個。
        :type SecretBinary: str
        :param SecretString: 文本類型憑據訊息明文（不需要進行base64編碼），SecretBinary 和 SecretString 必須且只能設置一個。
        :type SecretString: str
        """
        self.SecretName = None
        self.VersionId = None
        self.SecretBinary = None
        self.SecretString = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")


class PutSecretValueResponse(AbstractModel):
    """PutSecretValue返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 憑據名稱。
        :type SecretName: str
        :param VersionId: 新增加的版本号。
        :type VersionId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class RestoreSecretRequest(AbstractModel):
    """RestoreSecret請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定需要恢複的憑據名稱。
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")


class RestoreSecretResponse(AbstractModel):
    """RestoreSecret返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 憑據名稱。
        :type SecretName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class SecretMetadata(AbstractModel):
    """憑據的基礎訊息

    """

    def __init__(self):
        """
        :param SecretName: 憑據名稱。
        :type SecretName: str
        :param Description: 憑據的描述訊息。
        :type Description: str
        :param KmsKeyId: 用于加密憑據的KMS KeyId。
        :type KmsKeyId: str
        :param CreateUin: 創建者UIN。
        :type CreateUin: int
        :param Status: 憑據狀态：Enabled、Disabled、PendingDelete
        :type Status: str
        :param DeleteTime: 憑據删除日期，對于status爲PendingDelete 的有效，unix時間戳。
        :type DeleteTime: int
        :param CreateTime: 憑據創建時間，unix時間戳。
        :type CreateTime: int
        :param KmsKeyType: 用于加密憑據的KMS CMK類型，DEFAULT 表示SecretsManager 創建的預設金鑰， CUSTOMER 表示用戶指定的金鑰。
        :type KmsKeyType: str
        """
        self.SecretName = None
        self.Description = None
        self.KmsKeyId = None
        self.CreateUin = None
        self.Status = None
        self.DeleteTime = None
        self.CreateTime = None
        self.KmsKeyType = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.CreateUin = params.get("CreateUin")
        self.Status = params.get("Status")
        self.DeleteTime = params.get("DeleteTime")
        self.CreateTime = params.get("CreateTime")
        self.KmsKeyType = params.get("KmsKeyType")


class UpdateDescriptionRequest(AbstractModel):
    """UpdateDescription請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定需要更新描述訊息的憑據名。
        :type SecretName: str
        :param Description: 新的描述訊息，最大長度2048個位元。
        :type Description: str
        """
        self.SecretName = None
        self.Description = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")


class UpdateDescriptionResponse(AbstractModel):
    """UpdateDescription返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 憑據名稱。
        :type SecretName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class UpdateSecretRequest(AbstractModel):
    """UpdateSecret請求參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 指定需要更新憑據内容的名稱。
        :type SecretName: str
        :param VersionId: 指定需要更新憑據内容的版本号。
        :type VersionId: str
        :param SecretBinary: 新的憑據内容爲二進制的場景使用該欄位，并使用base64進行編碼。SecretBinary 和 SecretString 只能一個不爲空。
        :type SecretBinary: str
        :param SecretString: 新的憑據内容爲文本的場景使用該欄位，不需要base64編碼。SecretBinary 和 SecretString 只能一個不爲空。
        :type SecretString: str
        """
        self.SecretName = None
        self.VersionId = None
        self.SecretBinary = None
        self.SecretString = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")


class UpdateSecretResponse(AbstractModel):
    """UpdateSecret返回參數結構體

    """

    def __init__(self):
        """
        :param SecretName: 憑據名稱。
        :type SecretName: str
        :param VersionId: 憑據版本号。
        :type VersionId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class VersionInfo(AbstractModel):
    """憑據版本号清單訊息

    """

    def __init__(self):
        """
        :param VersionId: 版本号。
        :type VersionId: str
        :param CreateTime: 創建時間，unix時間戳。
        :type CreateTime: int
        """
        self.VersionId = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateTime = params.get("CreateTime")