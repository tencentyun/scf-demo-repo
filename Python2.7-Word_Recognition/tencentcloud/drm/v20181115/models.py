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


class Key(AbstractModel):
    """DRM加密金鑰

    """

    def __init__(self):
        """
        :param Track: 加密track類型。
        :type Track: str
        :param KeyId: 金鑰ID。
        :type KeyId: str
        :param Key: 原始Key使用AES-128 ECB模式和SessionKey加密的後的二進制數據，Base64編碼的字串。
        :type Key: str
        :param Iv: 原始IV使用AES-128 ECB模式和SessionKey加密的後的二進制數據，Base64編碼的字串。
        :type Iv: str
        """
        self.Track = None
        self.KeyId = None
        self.Key = None
        self.Iv = None


    def _deserialize(self, params):
        self.Track = params.get("Track")
        self.KeyId = params.get("KeyId")
        self.Key = params.get("Key")
        self.Iv = params.get("Iv")


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