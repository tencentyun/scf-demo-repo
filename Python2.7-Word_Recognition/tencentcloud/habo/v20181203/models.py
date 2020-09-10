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


class DescribeStatusRequest(AbstractModel):
    """DescribeStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Pk: 購買服務後獲得的授權帳号，用于保證請求有效性
        :type Pk: str
        :param Md5: 需要獲取分析結果的樣本md5
        :type Md5: str
        """
        self.Pk = None
        self.Md5 = None


    def _deserialize(self, params):
        self.Pk = params.get("Pk")
        self.Md5 = params.get("Md5")


class DescribeStatusResponse(AbstractModel):
    """DescribeStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 介面調用狀态，1表示成功，非1表示失敗
        :type Status: int
        :param Info: 成功時返回success，失敗時返回具體的失敗原因，如樣本分析未完成
        :type Info: str
        :param Data: 成功時返回樣本日志下載網址，該網址10分鍾内有效
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class StartAnalyseRequest(AbstractModel):
    """StartAnalyse請求參數結構體

    """

    def __init__(self):
        """
        :param Pk: 購買服務後獲得的授權帳号，用于保證請求有效性
        :type Pk: str
        :param Md5: 樣本md5，用于對下載獲得的樣本完整性進行校驗
        :type Md5: str
        :param DlUrl: 待分析樣本下載網址
        :type DlUrl: str
        """
        self.Pk = None
        self.Md5 = None
        self.DlUrl = None


    def _deserialize(self, params):
        self.Pk = params.get("Pk")
        self.Md5 = params.get("Md5")
        self.DlUrl = params.get("DlUrl")


class StartAnalyseResponse(AbstractModel):
    """StartAnalyse返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 介面調用狀态，1表示成功，非1表示失敗
        :type Status: int
        :param Info: 成功時返回success，失敗時返回具體的失敗原因
        :type Info: str
        :param Data: 保留欄位
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Info = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Info = params.get("Info")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")