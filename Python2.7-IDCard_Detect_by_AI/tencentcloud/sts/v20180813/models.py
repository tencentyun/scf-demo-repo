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


class AssumeRoleRequest(AbstractModel):
    """AssumeRole請求參數結構體

    """

    def __init__(self):
        """
        :param RoleArn: 角色的資源描述。例如：qcs::cam::uin/12345678:role/4611686018427397919、qcs::cam::uin/12345678:roleName/testRoleName
        :type RoleArn: str
        :param RoleSessionName: 臨時會話名稱，由用戶自定義名稱
        :type RoleSessionName: str
        :param DurationSeconds: 指定臨時證書的有效期，單位：秒，預設 7200 秒，最長可設定有效期爲 43200 秒
        :type DurationSeconds: int
        """
        self.RoleArn = None
        self.RoleSessionName = None
        self.DurationSeconds = None


    def _deserialize(self, params):
        self.RoleArn = params.get("RoleArn")
        self.RoleSessionName = params.get("RoleSessionName")
        self.DurationSeconds = params.get("DurationSeconds")


class AssumeRoleResponse(AbstractModel):
    """AssumeRole返回參數結構體

    """

    def __init__(self):
        """
        :param Credentials: 臨時安全證書
        :type Credentials: :class:`taifucloudcloud.sts.v20180813.models.Credentials`
        :param ExpiredTime: 證書無效的時間，返回 Unix 時間戳，精确到秒
        :type ExpiredTime: int
        :param Expiration: 證書無效的時間，以 iso8601 格式的 UTC 時間表示
        :type Expiration: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Credentials = None
        self.ExpiredTime = None
        self.Expiration = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.ExpiredTime = params.get("ExpiredTime")
        self.Expiration = params.get("Expiration")
        self.RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """臨時證書

    """

    def __init__(self):
        """
        :param Token: token
        :type Token: str
        :param TmpSecretId: 臨時證書金鑰ID
        :type TmpSecretId: str
        :param TmpSecretKey: 臨時證書金鑰Key
        :type TmpSecretKey: str
        """
        self.Token = None
        self.TmpSecretId = None
        self.TmpSecretKey = None


    def _deserialize(self, params):
        self.Token = params.get("Token")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")


class GetFederationTokenRequest(AbstractModel):
    """GetFederationToken請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 聯合身份用戶昵稱
        :type Name: str
        :param Policy: 策略描述
注意：
1、policy 需要做 urlencode（如果通過 GET 方法請求雲 API，發送請求前，所有參數都需要按照雲 API 規範再 urlencode 一次）。
2、策略語法參照 CAM 策略語法。
3、策略中不能包含 principal 元素。
        :type Policy: str
        :param DurationSeconds: 指定臨時證書的有效期，單位：秒，預設1800秒，最長可設定有效期爲7200秒
        :type DurationSeconds: int
        """
        self.Name = None
        self.Policy = None
        self.DurationSeconds = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Policy = params.get("Policy")
        self.DurationSeconds = params.get("DurationSeconds")


class GetFederationTokenResponse(AbstractModel):
    """GetFederationToken返回參數結構體

    """

    def __init__(self):
        """
        :param Credentials: 臨時證書
        :type Credentials: :class:`taifucloudcloud.sts.v20180813.models.Credentials`
        :param ExpiredTime: 臨時證書有效的時間，返回 Unix 時間戳，精确到秒
        :type ExpiredTime: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Credentials = None
        self.ExpiredTime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.ExpiredTime = params.get("ExpiredTime")
        self.RequestId = params.get("RequestId")