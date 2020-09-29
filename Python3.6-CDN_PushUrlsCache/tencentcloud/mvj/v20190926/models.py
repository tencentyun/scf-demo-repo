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


class Data(AbstractModel):
    """返回結構

    """

    def __init__(self):
        """
        :param PostTime: 操作時間戳，單位秒
        :type PostTime: int
        :param Uid: 用戶ID 
accountType不同對應不同的用戶ID。如果是 或 用戶則填入對應的openId
        :type Uid: str
        :param UserIp: 操作來源的外網IP
        :type UserIp: str
        :param ValueScore: 0~100：營銷價值評分，分值越高，價值越大
[0,50]低價值
[50,70]價值一般
[70,100]高價值
        :type ValueScore: int
        """
        self.PostTime = None
        self.Uid = None
        self.UserIp = None
        self.ValueScore = None


    def _deserialize(self, params):
        self.PostTime = params.get("PostTime")
        self.Uid = params.get("Uid")
        self.UserIp = params.get("UserIp")
        self.ValueScore = params.get("ValueScore")


class MarketingValueJudgementRequest(AbstractModel):
    """MarketingValueJudgement請求參數結構體

    """

    def __init__(self):
        """
        :param AccountType: 手機賬號類型填寫4
        :type AccountType: int
        :param Uid: 填寫手機號碼，如15317537488
        :type Uid: str
        :param UserIp: 用戶請求時的用戶端外網IP
        :type UserIp: str
        :param PostTime: 用戶操作時間戳，單位秒（格林威治時間精确到秒，如1501590972）
        :type PostTime: int
        :param Imei: 用戶設備號imei/idfa(建議填寫)
        :type Imei: str
        :param Referer: 活動連結(建議填寫)
        :type Referer: str
        """
        self.AccountType = None
        self.Uid = None
        self.UserIp = None
        self.PostTime = None
        self.Imei = None
        self.Referer = None


    def _deserialize(self, params):
        self.AccountType = params.get("AccountType")
        self.Uid = params.get("Uid")
        self.UserIp = params.get("UserIp")
        self.PostTime = params.get("PostTime")
        self.Imei = params.get("Imei")
        self.Referer = params.get("Referer")


class MarketingValueJudgementResponse(AbstractModel):
    """MarketingValueJudgement返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 返回數據
        :type Data: :class:`taifucloudcloud.mvj.v20190926.models.Data`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = Data()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")