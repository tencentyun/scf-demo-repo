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


class BRIRequest(AbstractModel):
    """BRI請求

    """

    def __init__(self):
        """
        :param Service: 業務名, 必須是以下五個業務名之一(bri_num,bri_dev,bri_ip_bri_apk,bri_url)
        :type Service: str
        :param CertMd5: Apk證書Md5  (業務名爲bri_apk時必填，除非已填FileMd5)
        :type CertMd5: str
        :param FileMd5: Apk文件Md5 (業務名爲bri_apk時必填，除非已填PackageName,CertMd5,FileSize)
        :type FileMd5: str
        :param FileSize: Apk文件大小  (業務名爲bri_apk時必填，除非已填FileMd5)
        :type FileSize: int
        :param Imei: 安卓設備的Imei (業務名爲bri_dev時必填)
        :type Imei: str
        :param Ip: 點分格式的IP (業務名爲bri_ip時必填)
        :type Ip: str
        :param PackageName: Apk安裝包名 (業務名爲bri_apk時必填，除非已填FileMd5)
        :type PackageName: str
        :param PhoneNumber: 電話號碼 (業務名爲bri_num時必填)
        :type PhoneNumber: str
        :param Url: 網址 (業務名爲bri_url時必填)
        :type Url: str
        """
        self.Service = None
        self.CertMd5 = None
        self.FileMd5 = None
        self.FileSize = None
        self.Imei = None
        self.Ip = None
        self.PackageName = None
        self.PhoneNumber = None
        self.Url = None


    def _deserialize(self, params):
        self.Service = params.get("Service")
        self.CertMd5 = params.get("CertMd5")
        self.FileMd5 = params.get("FileMd5")
        self.FileSize = params.get("FileSize")
        self.Imei = params.get("Imei")
        self.Ip = params.get("Ip")
        self.PackageName = params.get("PackageName")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Url = params.get("Url")


class BRIResponse(AbstractModel):
    """響應

    """

    def __init__(self):
        """
        :param Score: 風險分值，取值[0,100], 分值越高風險越高
        :type Score: float
        :param Tags: 當Service爲bri_num時,返回的風險標簽有:
1) 疑似垃圾流量     說明: 結合號碼的曆史數據表現，判斷該號碼曆史用網際網路業務作惡行爲，其産生的網際網路行爲對於其他業務來說屬於作弊或垃圾流量。 
2) 疑似新客戶       說明: 通過號碼網際網路行爲（社交，浏覽等）是否異常判斷爲小號或接碼平台帳號。 

當Service爲bri_dev時,返回的風險標簽有:
1) 疑似真機假用戶    說明: 根據設備的一些數據表現，我們判定爲群控設備
2) 疑似假機         說明: 根據設備的一些數據表現，我們判定爲模拟器或虛假設備ID
3) 疑似真用戶假行爲  說明: 根據設備的用戶使用情況，我們判定該用戶存在使用腳本、外挂、病毒等作弊行爲

當Service爲bri_ip時,返回的風險標簽有:
1) 疑似垃圾流量     說明:結合IP的曆史數據表現，判斷該IP曆史用網際網路業務作惡行爲，其産生的網際網路行爲對於其他業務來說屬於作弊或垃圾流量。

當Service爲bri_url時,返回的風險標簽有:
1) 社工欺詐    說明: URL爲社工欺詐
2) 訊息詐騙    說明: URL爲訊息詐騙
3) 虛假銷售    說明: URL爲虛假銷售
4) 惡意文件    說明: URL爲惡意文件
5) 博彩網站    說明: URL爲博彩網站
6) 色情網站    說明: URL爲色情網站

當Service爲bri_apk時,返回的風險標簽有:
1) 安全   說明: APK爲正規應用
2) 一般   說明: APK爲未發現問題的正常應用
3) 風險   說明: APK爲外挂或色情等風險應用
4) 病毒   說明: APK爲包含惡意代碼的惡意軟體嗎,可能破壞系統或者其他app正常使用
        :type Tags: list of str
        """
        self.Score = None
        self.Tags = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.Tags = params.get("Tags")


class DescribeBRIRequest(AbstractModel):
    """DescribeBRI請求參數結構體

    """

    def __init__(self):
        """
        :param RequestData: 業務風險情報請求體
        :type RequestData: :class:`taifucloudcloud.bri.v20190328.models.BRIRequest`
        :param ResourceId: 客戶用於計費的資源ID
        :type ResourceId: str
        """
        self.RequestData = None
        self.ResourceId = None


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self.RequestData = BRIRequest()
            self.RequestData._deserialize(params.get("RequestData"))
        self.ResourceId = params.get("ResourceId")


class DescribeBRIResponse(AbstractModel):
    """DescribeBRI返回參數結構體

    """

    def __init__(self):
        """
        :param ResponseData: 業務風險情報響應體
        :type ResponseData: :class:`taifucloudcloud.bri.v20190328.models.BRIResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = BRIResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")