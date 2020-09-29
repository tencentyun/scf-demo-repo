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


class AudioModerationRequest(AbstractModel):
    """AudioModeration請求參數結構體

    """

    def __init__(self):
        """
        :param CallbackUrl: 回調url
        :type CallbackUrl: str
        :param FileContent: 音訊内容的base64
        :type FileContent: str
        :param FileMD5: 音訊文件的MD5值
        :type FileMD5: str
        :param FileUrl: 音訊内容Url ，其中FileUrl和FileContent二選一
        :type FileUrl: str
        """
        self.CallbackUrl = None
        self.FileContent = None
        self.FileMD5 = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.CallbackUrl = params.get("CallbackUrl")
        self.FileContent = params.get("FileContent")
        self.FileMD5 = params.get("FileMD5")
        self.FileUrl = params.get("FileUrl")


class AudioModerationResponse(AbstractModel):
    """AudioModeration返回參數結構體

    """

    def __init__(self):
        """
        :param BusinessCode: 業務返回碼 
60001：成功請求回調任務
        :type BusinessCode: int
        :param Data: 識别返回結果
        :type Data: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BusinessCode = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeModerationOverviewRequest(AbstractModel):
    """DescribeModerationOverview請求參數結構體

    """

    def __init__(self):
        """
        :param Date: 日期，如2019-01-01， 查詢該日期的概覽數據
        :type Date: str
        :param ServiceTypes: 服務類型數組，可以動态配置，Text:文本，Image:圖片，Audio:音訊，Video:視訊, 使用"ALL"表示所有類型, 不區分大小寫，如 ["Text", "Image"]查詢文本和圖片服務的數據，["all"]查詢所有服務的數據。
        :type ServiceTypes: list of str
        :param Channels: 管道號數組，1:直播 2:點播 3:IM 4:GME，統計指定管道組合的匯總數據，如[1,2]表示獲取直播和點播兩個管道的匯總數據，不填[]爲所有管道匯總數據
        :type Channels: list of int non-negative
        """
        self.Date = None
        self.ServiceTypes = None
        self.Channels = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.ServiceTypes = params.get("ServiceTypes")
        self.Channels = params.get("Channels")


class DescribeModerationOverviewResponse(AbstractModel):
    """DescribeModerationOverview返回參數結構體

    """

    def __init__(self):
        """
        :param Results: 概覽數據集合
        :type Results: list of OverviewRecord
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = OverviewRecord()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class ImageData(AbstractModel):
    """圖片識别結果詳情

    """

    def __init__(self):
        """
        :param EvilFlag: 是否惡意 0：正常 1：可疑
        :type EvilFlag: int
        :param EvilType: 惡意類型
100：正常 
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
24001：暴恐
21000：綜合
        :type EvilType: int
        :param IllegalDetect: 圖片違法詳情
        :type IllegalDetect: :class:`taifucloudcloud.cms.v20190321.models.ImageIllegalDetect`
        :param PolityDetect: 圖片涉政詳情
        :type PolityDetect: :class:`taifucloudcloud.cms.v20190321.models.ImagePolityDetect`
        :param PornDetect: 圖片涉黃詳情
        :type PornDetect: :class:`taifucloudcloud.cms.v20190321.models.ImagePornDetect`
        :param Similar: 圖片相似度詳情
        :type Similar: :class:`taifucloudcloud.cms.v20190321.models.Similar`
        :param TerrorDetect: 圖片暴恐詳情
        :type TerrorDetect: :class:`taifucloudcloud.cms.v20190321.models.ImageTerrorDetect`
        """
        self.EvilFlag = None
        self.EvilType = None
        self.IllegalDetect = None
        self.PolityDetect = None
        self.PornDetect = None
        self.Similar = None
        self.TerrorDetect = None


    def _deserialize(self, params):
        self.EvilFlag = params.get("EvilFlag")
        self.EvilType = params.get("EvilType")
        if params.get("IllegalDetect") is not None:
            self.IllegalDetect = ImageIllegalDetect()
            self.IllegalDetect._deserialize(params.get("IllegalDetect"))
        if params.get("PolityDetect") is not None:
            self.PolityDetect = ImagePolityDetect()
            self.PolityDetect._deserialize(params.get("PolityDetect"))
        if params.get("PornDetect") is not None:
            self.PornDetect = ImagePornDetect()
            self.PornDetect._deserialize(params.get("PornDetect"))
        if params.get("Similar") is not None:
            self.Similar = Similar()
            self.Similar._deserialize(params.get("Similar"))
        if params.get("TerrorDetect") is not None:
            self.TerrorDetect = ImageTerrorDetect()
            self.TerrorDetect._deserialize(params.get("TerrorDetect"))


class ImageIllegalDetect(AbstractModel):
    """圖片違法詳情

    """

    def __init__(self):
        """
        :param EvilType: 惡意類型
100：正常 
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
24001：暴恐
21000：綜合
        :type EvilType: int
        :param HitFlag: 處置判定 0：正常 1：可疑
        :type HitFlag: int
        :param Keywords: 關鍵詞明細
        :type Keywords: list of str
        :param Labels: 違法標簽：返回違法特征中文描述，如賭桌，槍支
        :type Labels: list of str
        :param Score: 違法分：分值範圍 0-100，分數越高違法傾向越明顯
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")


class ImageModerationRequest(AbstractModel):
    """ImageModeration請求參數結構體

    """

    def __init__(self):
        """
        :param FileContent: 文件内容 Base64,與FileUrl必須二填一
        :type FileContent: str
        :param FileMD5: 文件MD5值
        :type FileMD5: str
        :param FileUrl: 文件網址
        :type FileUrl: str
        """
        self.FileContent = None
        self.FileMD5 = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.FileMD5 = params.get("FileMD5")
        self.FileUrl = params.get("FileUrl")


class ImageModerationResponse(AbstractModel):
    """ImageModeration返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 識别結果
        :type Data: :class:`taifucloudcloud.cms.v20190321.models.ImageData`
        :param BusinessCode: 業務返回碼
        :type BusinessCode: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.BusinessCode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = ImageData()
            self.Data._deserialize(params.get("Data"))
        self.BusinessCode = params.get("BusinessCode")
        self.RequestId = params.get("RequestId")


class ImagePolityDetect(AbstractModel):
    """圖片涉政詳情

    """

    def __init__(self):
        """
        :param EvilType: 惡意類型
100：正常 
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
24001：暴恐
21000：綜合
        :type EvilType: int
        :param HitFlag: 處置判定  0：正常 1：可疑
        :type HitFlag: int
        :param FaceNames: 命中的人臉名稱
        :type FaceNames: list of str
        :param Keywords: 關鍵詞明細
        :type Keywords: list of str
        :param Score: 政治（人臉）分：分值範圍 0-100，分數越高可疑程度越高
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.FaceNames = None
        self.Keywords = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.FaceNames = params.get("FaceNames")
        self.Keywords = params.get("Keywords")
        self.Score = params.get("Score")


class ImagePornDetect(AbstractModel):
    """圖片涉黃詳情

    """

    def __init__(self):
        """
        :param EvilType: 惡意類型
100：正常 
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
24001：暴恐
21000：綜合
        :type EvilType: int
        :param HitFlag: 處置判定 0：正常 1：可疑
        :type HitFlag: int
        :param Keywords: 關鍵詞明細
        :type Keywords: list of str
        :param Labels: 色情標簽：色情特征中文描述
        :type Labels: list of str
        :param Score: 色情分：分值範圍 0-100，分數越高色情傾向越明顯
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")


class ImageTerrorDetect(AbstractModel):
    """圖片暴恐詳情

    """

    def __init__(self):
        """
        :param EvilType: 惡意類型
100：正常 
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
24001：暴恐
21000：綜合
        :type EvilType: int
        :param HitFlag: 處置判定 0：正常 1：可疑
        :type HitFlag: int
        :param Keywords: 關鍵詞明細
        :type Keywords: list of str
        :param Labels: 暴恐標簽：返回暴恐特征中文描述
        :type Labels: list of str
        :param Score: 暴恐分：分值範圍0--100，分數越高暴恐傾向越明顯
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.Keywords = None
        self.Labels = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.Keywords = params.get("Keywords")
        self.Labels = params.get("Labels")
        self.Score = params.get("Score")


class OverviewRecord(AbstractModel):
    """概覽數據

    """

    def __init__(self):
        """
        :param EvilCount: 調用惡意量
        :type EvilCount: int
        :param ServiceType: Text表示文本，Image表示圖片，Audio表示音訊，Video表示視訊
        :type ServiceType: str
        :param TotalCount: 調用總量
        :type TotalCount: int
        :param Yoy: 惡意量同比增長率
        :type Yoy: str
        """
        self.EvilCount = None
        self.ServiceType = None
        self.TotalCount = None
        self.Yoy = None


    def _deserialize(self, params):
        self.EvilCount = params.get("EvilCount")
        self.ServiceType = params.get("ServiceType")
        self.TotalCount = params.get("TotalCount")
        self.Yoy = params.get("Yoy")


class Similar(AbstractModel):
    """相似度詳情

    """

    def __init__(self):
        """
        :param EvilType: 惡意類型
100：正常 
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
24001：暴恐
21000：綜合
        :type EvilType: int
        :param HitFlag: 處置判定 0：未比對到 1：惡意 2：白樣本
        :type HitFlag: int
        :param SeedUrl: 返回的種子url
        :type SeedUrl: str
        """
        self.EvilType = None
        self.HitFlag = None
        self.SeedUrl = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        self.SeedUrl = params.get("SeedUrl")


class TextData(AbstractModel):
    """文本識别結果詳情

    """

    def __init__(self):
        """
        :param EvilFlag: 是否惡意 0：正常 1：可疑
        :type EvilFlag: int
        :param EvilType: 惡意類型
100：正常
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
24001：暴恐
21000：綜合
        :type EvilType: int
        :param Keywords: 命中的關鍵詞
        :type Keywords: list of str
        """
        self.EvilFlag = None
        self.EvilType = None
        self.Keywords = None


    def _deserialize(self, params):
        self.EvilFlag = params.get("EvilFlag")
        self.EvilType = params.get("EvilType")
        self.Keywords = params.get("Keywords")


class TextModerationRequest(AbstractModel):
    """TextModeration請求參數結構體

    """

    def __init__(self):
        """
        :param Content: 文本内容Base64編碼
        :type Content: str
        """
        self.Content = None


    def _deserialize(self, params):
        self.Content = params.get("Content")


class TextModerationResponse(AbstractModel):
    """TextModeration返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 識别結果
        :type Data: :class:`taifucloudcloud.cms.v20190321.models.TextData`
        :param BusinessCode: 業務返回碼
        :type BusinessCode: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.BusinessCode = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = TextData()
            self.Data._deserialize(params.get("Data"))
        self.BusinessCode = params.get("BusinessCode")
        self.RequestId = params.get("RequestId")


class VideoModerationRequest(AbstractModel):
    """VideoModeration請求參數結構體

    """

    def __init__(self):
        """
        :param CallbackUrl: 回調Url
        :type CallbackUrl: str
        :param FileMD5: 視訊文件MD5
        :type FileMD5: str
        :param FileContent: 視訊内容base64
        :type FileContent: str
        :param FileUrl: 視訊内容Url,其中FileUrl與FileContent二選一
        :type FileUrl: str
        """
        self.CallbackUrl = None
        self.FileMD5 = None
        self.FileContent = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.CallbackUrl = params.get("CallbackUrl")
        self.FileMD5 = params.get("FileMD5")
        self.FileContent = params.get("FileContent")
        self.FileUrl = params.get("FileUrl")


class VideoModerationResponse(AbstractModel):
    """VideoModeration返回參數結構體

    """

    def __init__(self):
        """
        :param BusinessCode: 業務返回碼
60001：成功請求回調任務
        :type BusinessCode: int
        :param Data: 識别返回結果
        :type Data: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BusinessCode = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessCode = params.get("BusinessCode")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")