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

from tencentcloud.common.abstract_model import AbstractModel


class AddFairPlayPemRequest(AbstractModel):
    """AddFairPlayPem請求參數結構體

    """

    def __init__(self):
        """
        :param Pem: 加密後的fairplay方案申請時使用的私鑰。
請使用Top Cloud DRM 提供的公鑰，使用rsa加密算法，PKCS1填充方式對私鑰文件中的欄位進行加密，并對加密結果進行base64編碼。
        :type Pem: str
        :param Ask: 加密後的fairplay方案申請返回的ask數據。
請使用Top Cloud DRM 提供的公鑰，使用rsa加密算法，PKCS1填充方式對Ask字串進行加密，并對加密結果進行base64編碼。
        :type Ask: str
        :param PemDecryptKey: 私鑰的解密金鑰。
openssl在生成rsa時，可能會需要設置加密金鑰，請記住設置的金鑰。
請使用Top Cloud DRM 提供的公鑰，使用rsa加密算法，PKCS1填充方式對解密金鑰進行加密，并對加密結果進行base64編碼。
        :type PemDecryptKey: str
        :param BailorId: 委托者Id,适用于托管自身證書的客戶。普通客戶無需填該欄位。
        :type BailorId: int
        :param Priority: 私鑰的優先級，優先級數值越高，優先級越高。
該值可以不傳，後台将自動分配一個優先級。
        :type Priority: int
        """
        self.Pem = None
        self.Ask = None
        self.PemDecryptKey = None
        self.BailorId = None
        self.Priority = None


    def _deserialize(self, params):
        self.Pem = params.get("Pem")
        self.Ask = params.get("Ask")
        self.PemDecryptKey = params.get("PemDecryptKey")
        self.BailorId = params.get("BailorId")
        self.Priority = params.get("Priority")


class AddFairPlayPemResponse(AbstractModel):
    """AddFairPlayPem返回參數結構體

    """

    def __init__(self):
        """
        :param FairPlayPemId: 設置私鑰後，後台返回的pem id，用來唯一标識一個私鑰。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FairPlayPemId: int
        :param Priority: 私鑰的優先級，優先級數值越高，優先級越高。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Priority: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FairPlayPemId = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FairPlayPemId = params.get("FairPlayPemId")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")


class CreateEncryptKeysRequest(AbstractModel):
    """CreateEncryptKeys請求參數結構體

    """

    def __init__(self):
        """
        :param DrmType: 使用的DRM方案類型，介面取值WIDEVINE、FAIRPLAY、NORMALAES。
        :type DrmType: str
        :param Keys: 設置的加密金鑰清單。
        :type Keys: list of KeyParam
        :param ContentId: 一個加密内容的唯一标識。
        :type ContentId: str
        :param ContentType: 内容類型。介面取值VodVideo,LiveVideo。
        :type ContentType: str
        """
        self.DrmType = None
        self.Keys = None
        self.ContentId = None
        self.ContentType = None


    def _deserialize(self, params):
        self.DrmType = params.get("DrmType")
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = KeyParam()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.ContentId = params.get("ContentId")
        self.ContentType = params.get("ContentType")


class CreateEncryptKeysResponse(AbstractModel):
    """CreateEncryptKeys返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLicenseRequest(AbstractModel):
    """CreateLicense請求參數結構體

    """

    def __init__(self):
        """
        :param DrmType: DRM方案類型，介面取值：WIDEVINE，FAIRPLAY。
        :type DrmType: str
        :param LicenseRequest: Base64編碼的終端設備License Request數據。
        :type LicenseRequest: str
        :param ContentType: 内容類型，介面取值：VodVideo,LiveVideo。
        :type ContentType: str
        :param Tracks: 授權播放的Track清單。
該值爲空時，預設授權所有track播放。
        :type Tracks: list of str
        :param PlaybackPolicy: 播放策略參數。
        :type PlaybackPolicy: :class:`tencentcloud.drm.v20181115.models.PlaybackPolicy`
        """
        self.DrmType = None
        self.LicenseRequest = None
        self.ContentType = None
        self.Tracks = None
        self.PlaybackPolicy = None


    def _deserialize(self, params):
        self.DrmType = params.get("DrmType")
        self.LicenseRequest = params.get("LicenseRequest")
        self.ContentType = params.get("ContentType")
        self.Tracks = params.get("Tracks")
        if params.get("PlaybackPolicy") is not None:
            self.PlaybackPolicy = PlaybackPolicy()
            self.PlaybackPolicy._deserialize(params.get("PlaybackPolicy"))


class CreateLicenseResponse(AbstractModel):
    """CreateLicense返回參數結構體

    """

    def __init__(self):
        """
        :param License: Base64 編碼的許可證二進制數據。
        :type License: str
        :param ContentId: 加密内容的内容ID
        :type ContentId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.License = None
        self.ContentId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.License = params.get("License")
        self.ContentId = params.get("ContentId")
        self.RequestId = params.get("RequestId")


class DeleteFairPlayPemRequest(AbstractModel):
    """DeleteFairPlayPem請求參數結構體

    """

    def __init__(self):
        """
        :param BailorId: 委托者Id,适用于托管自身證書的客戶。普通客戶無需填該欄位。
        :type BailorId: int
        :param FairPlayPemId: 要删除的pem id。
當未傳入該值時，将删除所有的私鑰。
        :type FairPlayPemId: int
        """
        self.BailorId = None
        self.FairPlayPemId = None


    def _deserialize(self, params):
        self.BailorId = params.get("BailorId")
        self.FairPlayPemId = params.get("FairPlayPemId")


class DeleteFairPlayPemResponse(AbstractModel):
    """DeleteFairPlayPem返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAllKeysRequest(AbstractModel):
    """DescribeAllKeys請求參數結構體

    """

    def __init__(self):
        """
        :param DrmType: 使用的DRM方案類型，介面取值WIDEVINE、FAIRPLAY、NORMALAES。
        :type DrmType: str
        :param RsaPublicKey: Base64編碼的Rsa公鑰，用來加密出參中的SessionKey。
如果該參數爲空，則出參中SessionKey爲明文。
        :type RsaPublicKey: str
        :param ContentId: 一個加密内容的唯一标識。
        :type ContentId: str
        :param ContentType: 内容類型。介面取值VodVideo,LiveVideo。
        :type ContentType: str
        """
        self.DrmType = None
        self.RsaPublicKey = None
        self.ContentId = None
        self.ContentType = None


    def _deserialize(self, params):
        self.DrmType = params.get("DrmType")
        self.RsaPublicKey = params.get("RsaPublicKey")
        self.ContentId = params.get("ContentId")
        self.ContentType = params.get("ContentType")


class DescribeAllKeysResponse(AbstractModel):
    """DescribeAllKeys返回參數結構體

    """

    def __init__(self):
        """
        :param Keys: 加密金鑰清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Keys: list of Key
        :param SessionKey: 用來加密金鑰。
如果入參中帶有RsaPublicKey，則SessionKey爲使用Rsa公鑰加密後的二進制數據，Base64編碼字串。
如果入參中沒有RsaPublicKey，則SessionKey爲原始數據的字串形式。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionKey: str
        :param ContentId: 内容ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContentId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Keys = None
        self.SessionKey = None
        self.ContentId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.SessionKey = params.get("SessionKey")
        self.ContentId = params.get("ContentId")
        self.RequestId = params.get("RequestId")


class DescribeFairPlayPemRequest(AbstractModel):
    """DescribeFairPlayPem請求參數結構體

    """

    def __init__(self):
        """
        :param BailorId: 委托者Id,适用于托管自身證書的客戶。普通客戶無需填該欄位。
        :type BailorId: int
        :param FairPlayPemId: 需要查詢的pem id。
當該值未填入時，将返回所有的私鑰訊息。
        :type FairPlayPemId: int
        """
        self.BailorId = None
        self.FairPlayPemId = None


    def _deserialize(self, params):
        self.BailorId = params.get("BailorId")
        self.FairPlayPemId = params.get("FairPlayPemId")


class DescribeFairPlayPemResponse(AbstractModel):
    """DescribeFairPlayPem返回參數結構體

    """

    def __init__(self):
        """
        :param FairPlayPems: 該帳戶下，所有設置的FairPlay私鑰摘要訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type FairPlayPems: list of FairPlayPemDigestInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FairPlayPems = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FairPlayPems") is not None:
            self.FairPlayPems = []
            for item in params.get("FairPlayPems"):
                obj = FairPlayPemDigestInfo()
                obj._deserialize(item)
                self.FairPlayPems.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys請求參數結構體

    """

    def __init__(self):
        """
        :param DrmType: 使用的DRM方案類型，介面取值WIDEVINE、FAIRPLAY、NORMALAES。
        :type DrmType: str
        :param Tracks: 加密的track清單，介面取值VIDEO、AUDIO。
        :type Tracks: list of str
        :param ContentType: 内容類型。介面取值VodVideo,LiveVideo
        :type ContentType: str
        :param RsaPublicKey: Base64編碼的Rsa公鑰，用來加密出參中的SessionKey。
如果該參數爲空，則出參中SessionKey爲明文。
        :type RsaPublicKey: str
        :param ContentId: 一個加密内容的唯一标識。
如果該參數爲空，則後台自動生成
        :type ContentId: str
        """
        self.DrmType = None
        self.Tracks = None
        self.ContentType = None
        self.RsaPublicKey = None
        self.ContentId = None


    def _deserialize(self, params):
        self.DrmType = params.get("DrmType")
        self.Tracks = params.get("Tracks")
        self.ContentType = params.get("ContentType")
        self.RsaPublicKey = params.get("RsaPublicKey")
        self.ContentId = params.get("ContentId")


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys返回參數結構體

    """

    def __init__(self):
        """
        :param Keys: 加密金鑰清單
        :type Keys: list of Key
        :param SessionKey: 用來加密金鑰。
如果入參中帶有RsaPublicKey，則SessionKey爲使用Rsa公鑰加密後的二進制數據，Base64編碼字串。
如果入參中沒有RsaPublicKey，則SessionKey爲原始數據的字串形式。
        :type SessionKey: str
        :param ContentId: 内容ID
        :type ContentId: str
        :param Pssh: Widevine方案的Pssh數據，Base64編碼。
Fairplay方案無該值。
        :type Pssh: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Keys = None
        self.SessionKey = None
        self.ContentId = None
        self.Pssh = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.SessionKey = params.get("SessionKey")
        self.ContentId = params.get("ContentId")
        self.Pssh = params.get("Pssh")
        self.RequestId = params.get("RequestId")


class DrmOutputObject(AbstractModel):
    """DRM加密後的輸出對象

    """

    def __init__(self):
        """
        :param BucketName: 輸出的桶名稱。
        :type BucketName: str
        :param ObjectName: 輸出的對象名稱。
        :type ObjectName: str
        :param Para: 輸出對象參數。
        :type Para: :class:`tencentcloud.drm.v20181115.models.DrmOutputPara`
        """
        self.BucketName = None
        self.ObjectName = None
        self.Para = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.ObjectName = params.get("ObjectName")
        if params.get("Para") is not None:
            self.Para = DrmOutputPara()
            self.Para._deserialize(params.get("Para"))


class DrmOutputPara(AbstractModel):
    """Drm加密對象輸出參數

    """

    def __init__(self):
        """
        :param Type: 内容類型。例:video，audio，mpd，m3u8
        :type Type: str
        :param Language: 語言,例: en, zh-cn
        :type Language: str
        """
        self.Type = None
        self.Language = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Language = params.get("Language")


class DrmSourceObject(AbstractModel):
    """用于DRM加密的源對象

    """

    def __init__(self):
        """
        :param BucketName: 輸入的桶名稱。
        :type BucketName: str
        :param ObjectName: 輸入對象名稱。
        :type ObjectName: str
        """
        self.BucketName = None
        self.ObjectName = None


    def _deserialize(self, params):
        self.BucketName = params.get("BucketName")
        self.ObjectName = params.get("ObjectName")


class FairPlayPemDigestInfo(AbstractModel):
    """FairPlay 私鑰摘要訊息。

    """

    def __init__(self):
        """
        :param FairPlayPemId: fairplay 私鑰pem id。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FairPlayPemId: int
        :param Priority: 私鑰的優先級。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Priority: int
        :param Md5Pem: 私鑰的md5 訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Md5Pem: str
        :param Md5Ask: ASK的md5訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Md5Ask: str
        :param Md5PemDecryptKey: 私鑰解密金鑰的md5值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Md5PemDecryptKey: str
        """
        self.FairPlayPemId = None
        self.Priority = None
        self.Md5Pem = None
        self.Md5Ask = None
        self.Md5PemDecryptKey = None


    def _deserialize(self, params):
        self.FairPlayPemId = params.get("FairPlayPemId")
        self.Priority = params.get("Priority")
        self.Md5Pem = params.get("Md5Pem")
        self.Md5Ask = params.get("Md5Ask")
        self.Md5PemDecryptKey = params.get("Md5PemDecryptKey")


class Key(AbstractModel):
    """DRM加密金鑰

    """

    def __init__(self):
        """
        :param Track: 加密track類型。Widevine支援SD、HD、UHD1、UHD2、AUDIO。Fairplay只支援HD。
        :type Track: str
        :param KeyId: 金鑰ID。
        :type KeyId: str
        :param Key: 原始Key使用AES-128 ECB模式和SessionKey加密的後的二進制數據，Base64編碼的字串。
        :type Key: str
        :param Iv: 原始IV使用AES-128 ECB模式和SessionKey加密的後的二進制數據，Base64編碼的字串。
        :type Iv: str
        :param InsertTimestamp: 該key生成時的時間戳
注意：此欄位可能返回 null，表示取不到有效值。
        :type InsertTimestamp: int
        """
        self.Track = None
        self.KeyId = None
        self.Key = None
        self.Iv = None
        self.InsertTimestamp = None


    def _deserialize(self, params):
        self.Track = params.get("Track")
        self.KeyId = params.get("KeyId")
        self.Key = params.get("Key")
        self.Iv = params.get("Iv")
        self.InsertTimestamp = params.get("InsertTimestamp")


class KeyParam(AbstractModel):
    """設置加密金鑰所需的參數

    """

    def __init__(self):
        """
        :param Track: 加密track類型。取值範圍：
SD、HD、UHD1、UHD2、AUDIO
        :type Track: str
        :param Key: 請使用Top Cloud DRM 提供的公鑰，使用rsa加密算法，PKCS1填充方式對解密金鑰進行加密，并對加密結果進行base64編碼。
        :type Key: str
        :param KeyId: 金鑰ID。
        :type KeyId: str
        :param Iv: 請使用Top Cloud DRM 提供的公鑰，使用rsa加密算法，PKCS1填充方式對解密金鑰進行加密，并對加密結果進行base64編碼。
        :type Iv: str
        """
        self.Track = None
        self.Key = None
        self.KeyId = None
        self.Iv = None


    def _deserialize(self, params):
        self.Track = params.get("Track")
        self.Key = params.get("Key")
        self.KeyId = params.get("KeyId")
        self.Iv = params.get("Iv")


class ModifyFairPlayPemRequest(AbstractModel):
    """ModifyFairPlayPem請求參數結構體

    """

    def __init__(self):
        """
        :param Pem: 加密後的fairplay方案申請時使用的私鑰。
請使用Top Cloud DRM 提供的公鑰，使用rsa加密算法，PKCS1填充方式對私鑰文件中的欄位進行加密，并對加密結果進行base64編碼。
        :type Pem: str
        :param Ask: 加密後的fairplay方案申請返回的ask數據。
請使用Top Cloud DRM 提供的公鑰，使用rsa加密算法，PKCS1填充方式對Ask字串進行加密，并對加密結果進行base64編碼。
        :type Ask: str
        :param FairPlayPemId: 要修改的私鑰id
        :type FairPlayPemId: int
        :param PemDecryptKey: 私鑰的解密金鑰。
openssl在生成rsa時，可能會需要設置加密金鑰，請記住設置的金鑰。
請使用Top Cloud DRM 提供的公鑰，使用rsa加密算法，PKCS1填充方式對解密金鑰進行加密，并對加密結果進行base64編碼。
        :type PemDecryptKey: str
        :param BailorId: 委托者Id,适用于托管自身證書的客戶。普通客戶無需填該欄位。
        :type BailorId: int
        :param Priority: 私鑰的優先級，優先級數值越高，優先級越高。
該值可以不傳，後台将自動分配一個優先級。
        :type Priority: int
        """
        self.Pem = None
        self.Ask = None
        self.FairPlayPemId = None
        self.PemDecryptKey = None
        self.BailorId = None
        self.Priority = None


    def _deserialize(self, params):
        self.Pem = params.get("Pem")
        self.Ask = params.get("Ask")
        self.FairPlayPemId = params.get("FairPlayPemId")
        self.PemDecryptKey = params.get("PemDecryptKey")
        self.BailorId = params.get("BailorId")
        self.Priority = params.get("Priority")


class ModifyFairPlayPemResponse(AbstractModel):
    """ModifyFairPlayPem返回參數結構體

    """

    def __init__(self):
        """
        :param FairPlayPemId: 設置私鑰後，後台返回的pem id，用來唯一标識一個私鑰。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FairPlayPemId: int
        :param Priority: 私鑰的優先級，優先級數值越高，優先級越高。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Priority: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FairPlayPemId = None
        self.Priority = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FairPlayPemId = params.get("FairPlayPemId")
        self.Priority = params.get("Priority")
        self.RequestId = params.get("RequestId")


class PlaybackPolicy(AbstractModel):
    """播放控制參數

    """

    def __init__(self):
        """
        :param LicenseDurationSeconds: 播放許可證的有效期
        :type LicenseDurationSeconds: int
        :param PlaybackDurationSeconds: 開始播放後，允許最長播放時間
        :type PlaybackDurationSeconds: int
        """
        self.LicenseDurationSeconds = None
        self.PlaybackDurationSeconds = None


    def _deserialize(self, params):
        self.LicenseDurationSeconds = params.get("LicenseDurationSeconds")
        self.PlaybackDurationSeconds = params.get("PlaybackDurationSeconds")


class StartEncryptionRequest(AbstractModel):
    """StartEncryption請求參數結構體

    """

    def __init__(self):
        """
        :param CosEndPoint: cos的end point。
        :type CosEndPoint: str
        :param CosSecretId: cos api金鑰id。
        :type CosSecretId: str
        :param CosSecretKey: cos api金鑰。
        :type CosSecretKey: str
        :param DrmType: 使用的DRM方案類型，介面取值WIDEVINE,FAIRPLAY
        :type DrmType: str
        :param SourceObject: 儲存在COS上的原始内容訊息
        :type SourceObject: :class:`tencentcloud.drm.v20181115.models.DrmSourceObject`
        :param OutputObjects: 加密後的内容儲存到COS的對象
        :type OutputObjects: list of DrmOutputObject
        """
        self.CosEndPoint = None
        self.CosSecretId = None
        self.CosSecretKey = None
        self.DrmType = None
        self.SourceObject = None
        self.OutputObjects = None


    def _deserialize(self, params):
        self.CosEndPoint = params.get("CosEndPoint")
        self.CosSecretId = params.get("CosSecretId")
        self.CosSecretKey = params.get("CosSecretKey")
        self.DrmType = params.get("DrmType")
        if params.get("SourceObject") is not None:
            self.SourceObject = DrmSourceObject()
            self.SourceObject._deserialize(params.get("SourceObject"))
        if params.get("OutputObjects") is not None:
            self.OutputObjects = []
            for item in params.get("OutputObjects"):
                obj = DrmOutputObject()
                obj._deserialize(item)
                self.OutputObjects.append(obj)


class StartEncryptionResponse(AbstractModel):
    """StartEncryption返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")