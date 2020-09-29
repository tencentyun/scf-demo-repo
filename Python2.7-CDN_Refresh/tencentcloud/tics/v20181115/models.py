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


class DescribeDomainInfoRequest(AbstractModel):
    """DescribeDomainInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Key: 要查詢的域名
        :type Key: str
        :param Option: 附加欄位，是否返回上下文。當爲0時不返回上下文，當爲1時返回上下文。
        :type Option: int
        """
        self.Key = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Option = params.get("Option")


class DescribeDomainInfoResponse(AbstractModel):
    """DescribeDomainInfo返回參數結構體

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有數據，0代表有數據，1代表沒有數據
        :type ReturnCode: int
        :param Result: 判定結果，如：black、white、grey
        :type Result: str
        :param Confidence: 置信度，取值0-100
        :type Confidence: int
        :param ThreatTypes: 威脅類型。
botnet = 僵屍網絡
trojan = 木馬
ransomware = 勒索軟體
worm = 蠕蟲
dga = 域名生成算法
c2 = c&c
compromised = 失陷主機
dynamicIP = 動态IP
proxy = 代理
idc = idc 機房
whitelist = 白名單
tor = 暗網
miner = 挖礦
maleware site = 惡意站點
malware IP = 惡意IP
等等
        :type ThreatTypes: list of str
        :param Tags: 惡意標簽，對應的團夥，家族等訊息。
        :type Tags: list of TagType
        :param Intelligences: 對應的曆史上的威脅情報事件
        :type Intelligences: list of IntelligenceType
        :param Context: 情報相關的上下文
        :type Context: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.ThreatTypes = None
        self.Tags = None
        self.Intelligences = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        self.ThreatTypes = params.get("ThreatTypes")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Intelligences") is not None:
            self.Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self.Intelligences.append(obj)
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class DescribeFileInfoRequest(AbstractModel):
    """DescribeFileInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Key: 要查詢文件的MD5
        :type Key: str
        :param Option: 附加欄位，是否返回上下文。當爲0時不返回上下文，當爲1時返回上下文。
        :type Option: int
        """
        self.Key = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Option = params.get("Option")


class DescribeFileInfoResponse(AbstractModel):
    """DescribeFileInfo返回參數結構體

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有數據，0代表有數據，1代表沒有數據
        :type ReturnCode: int
        :param Result: 判定結果，如：black、white、grey
        :type Result: str
        :param Confidence: 置信度，取值0-100
        :type Confidence: int
        :param FileInfo: 文件類型，文件hash
（md5,sha1,sha256）,文件大小等等文件
基礎訊息
        :type FileInfo: list of FileInfoType
        :param Tags: 惡意標簽，對應的團夥，家族等訊息。
        :type Tags: list of TagType
        :param Intelligences: 對應的曆史上的威脅情報事件
        :type Intelligences: list of IntelligenceType
        :param Context: 情報相關的上下文
        :type Context: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.FileInfo = None
        self.Tags = None
        self.Intelligences = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        if params.get("FileInfo") is not None:
            self.FileInfo = []
            for item in params.get("FileInfo"):
                obj = FileInfoType()
                obj._deserialize(item)
                self.FileInfo.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Intelligences") is not None:
            self.Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self.Intelligences.append(obj)
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class DescribeIpInfoRequest(AbstractModel):
    """DescribeIpInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Key: 要查詢的IP
        :type Key: str
        :param Option: 附加欄位，是否返回上下文。當爲0時不返回上下文，當爲1時返回上下文。
        :type Option: int
        """
        self.Key = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Option = params.get("Option")


class DescribeIpInfoResponse(AbstractModel):
    """DescribeIpInfo返回參數結構體

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有數據，0代表有數據，1代表沒有數據
        :type ReturnCode: int
        :param Result: 判定結果，如：black、white、grey
        :type Result: str
        :param Confidence: 置信度，取值0-100
        :type Confidence: int
        :param ThreatTypes: 威脅類型。
botnet = 僵屍網絡
trojan = 木馬
ransomware = 勒索軟體
worm = 蠕蟲
dga = 域名生成算法
c2 = c&c
compromised = 失陷主機
dynamicIP = 動态IP
proxy = 代理
idc = idc 機房
whitelist = 白名單
tor = 暗網
miner = 挖礦
maleware site = 惡意站點
malware IP = 惡意IP
等等
        :type ThreatTypes: list of str
        :param Tags: 惡意標簽，對應的團夥，家族等訊息。
        :type Tags: list of TagType
        :param Intelligences: 對應的曆史上的威脅情報事件
        :type Intelligences: list of IntelligenceType
        :param Context: 情報相關的上下文
        :type Context: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.ThreatTypes = None
        self.Tags = None
        self.Intelligences = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        self.ThreatTypes = params.get("ThreatTypes")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagType()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("Intelligences") is not None:
            self.Intelligences = []
            for item in params.get("Intelligences"):
                obj = IntelligenceType()
                obj._deserialize(item)
                self.Intelligences.append(obj)
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class DescribeThreatInfoRequest(AbstractModel):
    """DescribeThreatInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Key: 查詢對象，域名或IP
        :type Key: str
        :param Type: 查詢類型，當前取值爲domain或ip
        :type Type: str
        :param Option: 附加欄位，是否返回上下文。當爲0時不返回上下文，當爲1時返回上下文。
        :type Option: int
        """
        self.Key = None
        self.Type = None
        self.Option = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Type = params.get("Type")
        self.Option = params.get("Option")


class DescribeThreatInfoResponse(AbstractModel):
    """DescribeThreatInfo返回參數結構體

    """

    def __init__(self):
        """
        :param ReturnCode: 是否有數據，0代表有數據，1代表沒有數據
        :type ReturnCode: int
        :param Result: 判定結果，如：black、white、grey
        :type Result: str
        :param Confidence: 置信度，取值0-100
        :type Confidence: int
        :param ThreatTypes: 威脅類型。
botnet = 僵屍網絡
trojan = 木馬
ransomware = 勒索軟體
worm = 蠕蟲
dga = 域名生成算法
c2 = c&c
compromised = 失陷主機
dynamicIP = 動态IP
proxy = 代理
idc = idc 機房
whitelist = 白名單
tor = 暗網
miner = 挖礦
maleware site = 惡意站點
malware IP = 惡意IP
等等
        :type ThreatTypes: list of str
        :param Tags: 惡意標簽，對應的團夥，家族等訊息。
        :type Tags: list of str
        :param Status: 當前狀态
active = 活躍
sinkholed = sinkholed
inactive = 不活躍
unknown = 未知
expired = 過期
        :type Status: str
        :param Context: 情報相關的上下文，參數option=1 的時候提供
每個數據預設爲3 條
        :type Context: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ReturnCode = None
        self.Result = None
        self.Confidence = None
        self.ThreatTypes = None
        self.Tags = None
        self.Status = None
        self.Context = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.Result = params.get("Result")
        self.Confidence = params.get("Confidence")
        self.ThreatTypes = params.get("ThreatTypes")
        self.Tags = params.get("Tags")
        self.Status = params.get("Status")
        self.Context = params.get("Context")
        self.RequestId = params.get("RequestId")


class FileInfoType(AbstractModel):
    """文件訊息類型

    """

    def __init__(self):
        """
        :param DetectId: 判定管道
        :type DetectId: str
        :param DetectPriority: 檢測優先級
        :type DetectPriority: str
        :param EnginePriority: 引擎優先級
        :type EnginePriority: str
        :param FileExist: 樣本是否存在
        :type FileExist: str
        :param FileForceUpload: 文件上傳
        :type FileForceUpload: str
        :param FileSize: 文件大小
        :type FileSize: str
        :param FileupTime: 文件上傳時間
        :type FileupTime: str
        :param FullVirusName: 病毒文件全名
        :type FullVirusName: str
        :param IdcPosition: IDC位置
        :type IdcPosition: str
        :param Md5Type: 文件md5值
        :type Md5Type: str
        :param PeExist: PE結構是否存在
        :type PeExist: str
        :param PeForceUpload: PE結構上傳
        :type PeForceUpload: str
        :param SafeLevel: 安全性等級
        :type SafeLevel: str
        :param ScanModiTime: 掃描時間
        :type ScanModiTime: str
        :param SubdetectId: 子判定管道
        :type SubdetectId: str
        :param UserDefName: 病毒名
        :type UserDefName: str
        :param VirusType: 病毒類型
        :type VirusType: str
        :param WhiteScore: 白名單分數
        :type WhiteScore: str
        """
        self.DetectId = None
        self.DetectPriority = None
        self.EnginePriority = None
        self.FileExist = None
        self.FileForceUpload = None
        self.FileSize = None
        self.FileupTime = None
        self.FullVirusName = None
        self.IdcPosition = None
        self.Md5Type = None
        self.PeExist = None
        self.PeForceUpload = None
        self.SafeLevel = None
        self.ScanModiTime = None
        self.SubdetectId = None
        self.UserDefName = None
        self.VirusType = None
        self.WhiteScore = None


    def _deserialize(self, params):
        self.DetectId = params.get("DetectId")
        self.DetectPriority = params.get("DetectPriority")
        self.EnginePriority = params.get("EnginePriority")
        self.FileExist = params.get("FileExist")
        self.FileForceUpload = params.get("FileForceUpload")
        self.FileSize = params.get("FileSize")
        self.FileupTime = params.get("FileupTime")
        self.FullVirusName = params.get("FullVirusName")
        self.IdcPosition = params.get("IdcPosition")
        self.Md5Type = params.get("Md5Type")
        self.PeExist = params.get("PeExist")
        self.PeForceUpload = params.get("PeForceUpload")
        self.SafeLevel = params.get("SafeLevel")
        self.ScanModiTime = params.get("ScanModiTime")
        self.SubdetectId = params.get("SubdetectId")
        self.UserDefName = params.get("UserDefName")
        self.VirusType = params.get("VirusType")
        self.WhiteScore = params.get("WhiteScore")


class IntelligenceType(AbstractModel):
    """{ "source": "inergj_ai_predict", "stamp": "msraminer", "time": 1531994023 }

    """

    def __init__(self):
        """
        :param Source: 來源
        :type Source: str
        :param Stamp: 標記
        :type Stamp: str
        :param Time: 時間
        :type Time: int
        """
        self.Source = None
        self.Stamp = None
        self.Time = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Stamp = params.get("Stamp")
        self.Time = params.get("Time")


class TagType(AbstractModel):
    """標簽及對應的解釋

    """

    def __init__(self):
        """
        :param Tag: 標簽
        :type Tag: str
        :param Desc: 標簽對應的中文解釋
        :type Desc: str
        """
        self.Tag = None
        self.Desc = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Desc = params.get("Desc")