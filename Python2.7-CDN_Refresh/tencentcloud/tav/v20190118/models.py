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


class GetLocalEngineRequest(AbstractModel):
    """GetLocalEngine請求參數結構體

    """

    def __init__(self):
        """
        :param Key: 購買服務後獲得的授權訊息，用于保證請求有效性
        :type Key: str
        """
        self.Key = None


    def _deserialize(self, params):
        self.Key = params.get("Key")


class GetLocalEngineResponse(AbstractModel):
    """GetLocalEngine返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 介面調用狀态，成功返回200，失敗返回400
        :type Status: int
        :param Info: 介面調用描述訊息，成功返回"scan success"，失敗返回"scan error"
        :type Info: str
        :param Data: 本地引擎下載網址
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


class GetScanResultRequest(AbstractModel):
    """GetScanResult請求參數結構體

    """

    def __init__(self):
        """
        :param Key: 購買服務後獲得的授權訊息，用于保證請求有效性
        :type Key: str
        :param Md5: 需要獲取掃描介面的md5（只允許單個md5）
        :type Md5: str
        """
        self.Key = None
        self.Md5 = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Md5 = params.get("Md5")


class GetScanResultResponse(AbstractModel):
    """GetScanResult返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 介面調用狀态，成功返回200，失敗返回400
        :type Status: int
        :param Info: 介面調用描述訊息，成功返回"scan success"，失敗返回"scan error"
        :type Info: str
        :param Data: 實際結果訊息，包括md5、scan_status、virus_name三個欄位；virus_name報毒名："torjan.**":黑樣本的報毒名、".":樣本不報毒、"" :樣本無檢出訊息，需上傳掃描；
scan_status樣本狀态：-1無檢出訊息需上傳掃描、0樣本掃描中、1樣本掃描結束且不報毒、2樣本掃描結束且報黑、3樣本下載失敗；
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


class ScanFileHashRequest(AbstractModel):
    """ScanFileHash請求參數結構體

    """

    def __init__(self):
        """
        :param Key: 購買服務後獲得的授權訊息，用于保證請求有效性
        :type Key: str
        :param Md5s: 需要查詢的md5值（支援單個和多個，多個md5間用逗号分格）
        :type Md5s: str
        :param WithCategory: 保留欄位預設填0
        :type WithCategory: str
        :param SensitiveLevel: 松嚴規則控制欄位預設填10（5-松、10-标準、15-嚴）
        :type SensitiveLevel: str
        """
        self.Key = None
        self.Md5s = None
        self.WithCategory = None
        self.SensitiveLevel = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Md5s = params.get("Md5s")
        self.WithCategory = params.get("WithCategory")
        self.SensitiveLevel = params.get("SensitiveLevel")


class ScanFileHashResponse(AbstractModel):
    """ScanFileHash返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 介面調用狀态，成功返回200，失敗返回400
        :type Status: int
        :param Info: 介面調用描述訊息，成功返回"scan success"，失敗返回"scan error"
        :type Info: str
        :param Data: 雲查實際結果訊息，包括md5、return_state、virus_state、virus_name字元逗号間隔；        
return_state查詢狀态：-1/0代表失敗、1/2代表成功；
virus_state文狀件态：0文件不存在、1白、2黑、3未知、4感染性、5低可信白；
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


class ScanFileRequest(AbstractModel):
    """ScanFile請求參數結構體

    """

    def __init__(self):
        """
        :param Key: 購買服務後獲得的授權訊息，用于保證請求有效性
        :type Key: str
        :param Sample: 文件下載url網址
        :type Sample: str
        :param Md5: 文件的md5值
        :type Md5: str
        """
        self.Key = None
        self.Sample = None
        self.Md5 = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sample = params.get("Sample")
        self.Md5 = params.get("Md5")


class ScanFileResponse(AbstractModel):
    """ScanFile返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 介面調用狀态，成功返回200，失敗返回400
        :type Status: int
        :param Info: 介面調用描述訊息，成功返回"success"，失敗返回"invalid request"
        :type Info: str
        :param Data: 異步掃描任務提交成功返回success
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