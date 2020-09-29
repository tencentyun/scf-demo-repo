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


class CodeDetail(AbstractModel):
    """從圖片中檢測到的二維碼，可能爲多個

    """

    def __init__(self):
        """
        :param CodePosition: 二維碼在圖片中的位置，由邊界點的坐標表示
        :type CodePosition: list of CodePosition
        :param CodeCharset: 二維碼文本的編碼格式
        :type CodeCharset: str
        :param CodeText: 二維碼的文本内容
        :type CodeText: str
        :param CodeType: 二維碼的類型：1:ONED_BARCODE，2:QRCOD，3:WXCODE，4:PDF417，5:DATAMATRIX
        :type CodeType: int
        """
        self.CodePosition = None
        self.CodeCharset = None
        self.CodeText = None
        self.CodeType = None


    def _deserialize(self, params):
        if params.get("CodePosition") is not None:
            self.CodePosition = []
            for item in params.get("CodePosition"):
                obj = CodePosition()
                obj._deserialize(item)
                self.CodePosition.append(obj)
        self.CodeCharset = params.get("CodeCharset")
        self.CodeText = params.get("CodeText")
        self.CodeType = params.get("CodeType")


class CodeDetect(AbstractModel):
    """圖片二維碼詳情

    """

    def __init__(self):
        """
        :param ModerationDetail: 從圖片中檢測到的二維碼，可能爲多個
        :type ModerationDetail: list of CodeDetail
        :param ModerationCode: 檢測是否成功，0：成功，-1：出錯
        :type ModerationCode: int
        """
        self.ModerationDetail = None
        self.ModerationCode = None


    def _deserialize(self, params):
        if params.get("ModerationDetail") is not None:
            self.ModerationDetail = []
            for item in params.get("ModerationDetail"):
                obj = CodeDetail()
                obj._deserialize(item)
                self.ModerationDetail.append(obj)
        self.ModerationCode = params.get("ModerationCode")


class CodePosition(AbstractModel):
    """二維碼在圖片中的位置，由邊界點的坐標表示

    """

    def __init__(self):
        """
        :param FloatX: 二維碼邊界點X軸坐標
        :type FloatX: float
        :param FloatY: 二維碼邊界點Y軸坐標
        :type FloatY: float
        """
        self.FloatX = None
        self.FloatY = None


    def _deserialize(self, params):
        self.FloatX = params.get("FloatX")
        self.FloatY = params.get("FloatY")


class CreateFileSampleRequest(AbstractModel):
    """CreateFileSample請求參數結構體

    """

    def __init__(self):
        """
        :param Contents: 文件類型結構數組
        :type Contents: list of FileSample
        :param EvilType: 惡意類型
100：正常
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
24001：暴恐
20105：廣告引流
        :type EvilType: int
        :param FileType: image：圖片
        :type FileType: str
        :param Label: 樣本類型
1：黑庫
2：白庫
        :type Label: int
        """
        self.Contents = None
        self.EvilType = None
        self.FileType = None
        self.Label = None


    def _deserialize(self, params):
        if params.get("Contents") is not None:
            self.Contents = []
            for item in params.get("Contents"):
                obj = FileSample()
                obj._deserialize(item)
                self.Contents.append(obj)
        self.EvilType = params.get("EvilType")
        self.FileType = params.get("FileType")
        self.Label = params.get("Label")


class CreateFileSampleResponse(AbstractModel):
    """CreateFileSample返回參數結構體

    """

    def __init__(self):
        """
        :param Progress: 任務狀态
1：已完成
2：處理中
        :type Progress: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class CreateTextSampleRequest(AbstractModel):
    """CreateTextSample請求參數結構體

    """

    def __init__(self):
        """
        :param Contents: 關鍵詞數組
        :type Contents: list of str
        :param EvilType: 惡意類型
100：正常
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
24001：暴恐
20105：廣告引流
        :type EvilType: int
        :param Label: 樣本類型
1：黑庫
2：白庫
        :type Label: int
        :param Test: 測試修改參數
        :type Test: str
        """
        self.Contents = None
        self.EvilType = None
        self.Label = None
        self.Test = None


    def _deserialize(self, params):
        self.Contents = params.get("Contents")
        self.EvilType = params.get("EvilType")
        self.Label = params.get("Label")
        self.Test = params.get("Test")


class CreateTextSampleResponse(AbstractModel):
    """CreateTextSample返回參數結構體

    """

    def __init__(self):
        """
        :param ErrMsg: 操作樣本失敗時返回的錯誤訊息範例：  "樣本1":錯誤碼，"樣本2":錯誤碼
        :type ErrMsg: str
        :param Progress: 任務狀态
1：已完成
2：處理中
        :type Progress: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ErrMsg = None
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrMsg = params.get("ErrMsg")
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DeleteFileSampleRequest(AbstractModel):
    """DeleteFileSample請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 唯一標識數組
        :type Ids: list of str
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteFileSampleResponse(AbstractModel):
    """DeleteFileSample返回參數結構體

    """

    def __init__(self):
        """
        :param Progress: 任務狀态
1：已完成
2：處理中
        :type Progress: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DeleteTextSampleRequest(AbstractModel):
    """DeleteTextSample請求參數結構體

    """

    def __init__(self):
        """
        :param Ids: 唯一標識數組，目前暫時只支援單個删除
        :type Ids: list of str
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")


class DeleteTextSampleResponse(AbstractModel):
    """DeleteTextSample返回參數結構體

    """

    def __init__(self):
        """
        :param Progress: 任務狀态
1：已完成
2：處理中
        :type Progress: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Progress = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.RequestId = params.get("RequestId")


class DescribeFileSampleRequest(AbstractModel):
    """DescribeFileSample請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 支援通過標簽值進行篩選
        :type Filters: list of Filter
        :param Limit: 數量限制，預設爲20，最大值爲100
        :type Limit: int
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param OrderDirection: 升序（asc）還是降序（desc），預設：desc
        :type OrderDirection: str
        :param OrderField: 按某個欄位排序，目前僅支援CreatedAt排序
        :type OrderField: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderDirection = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderDirection = params.get("OrderDirection")
        self.OrderField = params.get("OrderField")


class DescribeFileSampleResponse(AbstractModel):
    """DescribeFileSample返回參數結構體

    """

    def __init__(self):
        """
        :param FileSampleSet: 符合要求的樣本的訊息
        :type FileSampleSet: list of FileSampleInfo
        :param TotalCount: 符合要求的樣本的數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.FileSampleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileSampleSet") is not None:
            self.FileSampleSet = []
            for item in params.get("FileSampleSet"):
                obj = FileSampleInfo()
                obj._deserialize(item)
                self.FileSampleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTextSampleRequest(AbstractModel):
    """DescribeTextSample請求參數結構體

    """

    def __init__(self):
        """
        :param Filters: 支援通過標簽值進行篩選
        :type Filters: list of Filter
        :param Limit: 數量限制，預設爲20，最大值爲100
        :type Limit: int
        :param Offset: 偏移量，預設爲0
        :type Offset: int
        :param OrderDirection: 升序（asc）還是降序（desc），預設：desc
        :type OrderDirection: str
        :param OrderField: 按某個欄位排序，目前僅支援CreatedAt排序
        :type OrderField: str
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None
        self.OrderDirection = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderDirection = params.get("OrderDirection")
        self.OrderField = params.get("OrderField")


class DescribeTextSampleResponse(AbstractModel):
    """DescribeTextSample返回參數結構體

    """

    def __init__(self):
        """
        :param TextSampleSet: 符合要求的樣本的訊息
        :type TextSampleSet: list of TextSample
        :param TotalCount: 符合要求的樣本的數量
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TextSampleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TextSampleSet") is not None:
            self.TextSampleSet = []
            for item in params.get("TextSampleSet"):
                obj = TextSample()
                obj._deserialize(item)
                self.TextSampleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class FileSample(AbstractModel):
    """文件類型樣本

    """

    def __init__(self):
        """
        :param FileMd5: 文件md5
        :type FileMd5: str
        :param FileName: 文件名稱
        :type FileName: str
        :param FileUrl: 文件url
        :type FileUrl: str
        :param CompressFileUrl: 文件壓縮後雲url
        :type CompressFileUrl: str
        """
        self.FileMd5 = None
        self.FileName = None
        self.FileUrl = None
        self.CompressFileUrl = None


    def _deserialize(self, params):
        self.FileMd5 = params.get("FileMd5")
        self.FileName = params.get("FileName")
        self.FileUrl = params.get("FileUrl")
        self.CompressFileUrl = params.get("CompressFileUrl")


class FileSampleInfo(AbstractModel):
    """文件樣本返回訊息

    """

    def __init__(self):
        """
        :param Code: 處理錯誤碼
        :type Code: int
        :param CreatedAt: 創建時間戳
        :type CreatedAt: int
        :param EvilType: 惡意類型
100：正常
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
24001：暴恐
        :type EvilType: int
        :param FileMd5: 文件的md5
        :type FileMd5: str
        :param FileName: 文件名稱
        :type FileName: str
        :param FileType: 文件類型
        :type FileType: str
        :param Id: 唯一標識
        :type Id: str
        :param Label: 樣本類型
1：黑庫
2：白庫
        :type Label: int
        :param Status: 任務狀态
1：已完成
2：處理中
        :type Status: int
        :param CompressFileUrl: 文件壓縮後雲url
        :type CompressFileUrl: str
        :param FileUrl: 文件的url
        :type FileUrl: str
        """
        self.Code = None
        self.CreatedAt = None
        self.EvilType = None
        self.FileMd5 = None
        self.FileName = None
        self.FileType = None
        self.Id = None
        self.Label = None
        self.Status = None
        self.CompressFileUrl = None
        self.FileUrl = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.CreatedAt = params.get("CreatedAt")
        self.EvilType = params.get("EvilType")
        self.FileMd5 = params.get("FileMd5")
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.Id = params.get("Id")
        self.Label = params.get("Label")
        self.Status = params.get("Status")
        self.CompressFileUrl = params.get("CompressFileUrl")
        self.FileUrl = params.get("FileUrl")


class Filter(AbstractModel):
    """篩選數據結構

    """

    def __init__(self):
        """
        :param Name: 需要過濾的欄位
        :type Name: str
        :param Value: 需要過濾欄位的值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


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
20103：性感
24001：暴恐
        :type EvilType: int
        :param CodeDetect: 圖片二維碼詳情
        :type CodeDetect: :class:`taifucloudcloud.cms.v20190321.models.CodeDetect`
        :param HotDetect: 圖片性感詳情
        :type HotDetect: :class:`taifucloudcloud.cms.v20190321.models.ImageHotDetect`
        :param IllegalDetect: 圖片違法詳情
        :type IllegalDetect: :class:`taifucloudcloud.cms.v20190321.models.ImageIllegalDetect`
        :param LogoDetect: logo詳情
        :type LogoDetect: :class:`taifucloudcloud.cms.v20190321.models.LogoDetail`
        :param OCRDetect: 圖片OCR詳情
        :type OCRDetect: :class:`taifucloudcloud.cms.v20190321.models.OCRDetect`
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
        self.CodeDetect = None
        self.HotDetect = None
        self.IllegalDetect = None
        self.LogoDetect = None
        self.OCRDetect = None
        self.PolityDetect = None
        self.PornDetect = None
        self.Similar = None
        self.TerrorDetect = None


    def _deserialize(self, params):
        self.EvilFlag = params.get("EvilFlag")
        self.EvilType = params.get("EvilType")
        if params.get("CodeDetect") is not None:
            self.CodeDetect = CodeDetect()
            self.CodeDetect._deserialize(params.get("CodeDetect"))
        if params.get("HotDetect") is not None:
            self.HotDetect = ImageHotDetect()
            self.HotDetect._deserialize(params.get("HotDetect"))
        if params.get("IllegalDetect") is not None:
            self.IllegalDetect = ImageIllegalDetect()
            self.IllegalDetect._deserialize(params.get("IllegalDetect"))
        if params.get("LogoDetect") is not None:
            self.LogoDetect = LogoDetail()
            self.LogoDetect._deserialize(params.get("LogoDetect"))
        if params.get("OCRDetect") is not None:
            self.OCRDetect = OCRDetect()
            self.OCRDetect._deserialize(params.get("OCRDetect"))
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


class ImageHotDetect(AbstractModel):
    """圖片性感詳情

    """

    def __init__(self):
        """
        :param EvilType: 惡意類型
100：正常
20103：性感
        :type EvilType: int
        :param HitFlag: 處置判定 0：正常 1：可疑
        :type HitFlag: int
        :param Keywords: 關鍵詞明細
        :type Keywords: list of str
        :param Labels: 性感標簽：性感特征中文描述
        :type Labels: list of str
        :param Score: 性感分：分值範圍 0-100，分數越高性感傾向越明顯
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


class ImageIllegalDetect(AbstractModel):
    """圖片違法詳情

    """

    def __init__(self):
        """
        :param EvilType: 惡意類型
100：正常 
20006：涉毒違法
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
        :type EvilType: int
        :param HitFlag: 處置判定  0：正常 1：可疑
        :type HitFlag: int
        :param PolityLogoDetail: 命中的logo標簽訊息
        :type PolityLogoDetail: list of Logo
        :param FaceNames: 命中的人臉名稱
        :type FaceNames: list of str
        :param Keywords: 關鍵詞明細
        :type Keywords: list of str
        :param PolityItems: 命中的政治物品名稱
        :type PolityItems: list of str
        :param Score: 政治（人臉）分：分值範圍 0-100，分數越高可疑程度越高
        :type Score: int
        """
        self.EvilType = None
        self.HitFlag = None
        self.PolityLogoDetail = None
        self.FaceNames = None
        self.Keywords = None
        self.PolityItems = None
        self.Score = None


    def _deserialize(self, params):
        self.EvilType = params.get("EvilType")
        self.HitFlag = params.get("HitFlag")
        if params.get("PolityLogoDetail") is not None:
            self.PolityLogoDetail = []
            for item in params.get("PolityLogoDetail"):
                obj = Logo()
                obj._deserialize(item)
                self.PolityLogoDetail.append(obj)
        self.FaceNames = params.get("FaceNames")
        self.Keywords = params.get("Keywords")
        self.PolityItems = params.get("PolityItems")
        self.Score = params.get("Score")


class ImagePornDetect(AbstractModel):
    """圖片涉黃詳情

    """

    def __init__(self):
        """
        :param EvilType: 惡意類型
100：正常
20002：色情
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
24001：暴恐
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


class Logo(AbstractModel):
    """Logo

    """

    def __init__(self):
        """
        :param RrectF: logo圖標坐標訊息
        :type RrectF: :class:`taifucloudcloud.cms.v20190321.models.RrectF`
        :param Confidence: logo圖標置信度
        :type Confidence: float
        :param Name: logo圖標名稱
        :type Name: str
        """
        self.RrectF = None
        self.Confidence = None
        self.Name = None


    def _deserialize(self, params):
        if params.get("RrectF") is not None:
            self.RrectF = RrectF()
            self.RrectF._deserialize(params.get("RrectF"))
        self.Confidence = params.get("Confidence")
        self.Name = params.get("Name")


class LogoDetail(AbstractModel):
    """LogoDetail

    """

    def __init__(self):
        """
        :param AppLogoDetail: 命中的Applogo詳情
        :type AppLogoDetail: list of Logo
        """
        self.AppLogoDetail = None


    def _deserialize(self, params):
        if params.get("AppLogoDetail") is not None:
            self.AppLogoDetail = []
            for item in params.get("AppLogoDetail"):
                obj = Logo()
                obj._deserialize(item)
                self.AppLogoDetail.append(obj)


class OCRDetect(AbstractModel):
    """OCR識别結果詳情

    """

    def __init__(self):
        """
        :param TextInfo: 識别到的文本訊息
        :type TextInfo: str
        """
        self.TextInfo = None


    def _deserialize(self, params):
        self.TextInfo = params.get("TextInfo")


class RrectF(AbstractModel):
    """logo位置訊息

    """

    def __init__(self):
        """
        :param Cx: logo橫坐標
        :type Cx: float
        :param Cy: logo縱坐標
        :type Cy: float
        :param Height: logo圖標高度
        :type Height: float
        :param Rotate: logo圖標中心旋轉度
        :type Rotate: float
        :param Width: logo圖標寬度
        :type Width: float
        """
        self.Cx = None
        self.Cy = None
        self.Height = None
        self.Rotate = None
        self.Width = None


    def _deserialize(self, params):
        self.Cx = params.get("Cx")
        self.Cy = params.get("Cy")
        self.Height = params.get("Height")
        self.Rotate = params.get("Rotate")
        self.Width = params.get("Width")


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
20105：廣告引流 
24001：暴恐
        :type EvilType: int
        :param Common: 訊息類公共相關參數
        :type Common: :class:`taifucloudcloud.cms.v20190321.models.TextOutputComm`
        :param ID: 訊息類ID訊息
        :type ID: :class:`taifucloudcloud.cms.v20190321.models.TextOutputID`
        :param Res: 訊息類輸出結果
        :type Res: :class:`taifucloudcloud.cms.v20190321.models.TextOutputRes`
        :param Keywords: 命中的關鍵詞
        :type Keywords: list of str
        """
        self.EvilFlag = None
        self.EvilType = None
        self.Common = None
        self.ID = None
        self.Res = None
        self.Keywords = None


    def _deserialize(self, params):
        self.EvilFlag = params.get("EvilFlag")
        self.EvilType = params.get("EvilType")
        if params.get("Common") is not None:
            self.Common = TextOutputComm()
            self.Common._deserialize(params.get("Common"))
        if params.get("ID") is not None:
            self.ID = TextOutputID()
            self.ID._deserialize(params.get("ID"))
        if params.get("Res") is not None:
            self.Res = TextOutputRes()
            self.Res._deserialize(params.get("Res"))
        self.Keywords = params.get("Keywords")


class TextModerationRequest(AbstractModel):
    """TextModeration請求參數結構體

    """

    def __init__(self):
        """
        :param Content: 文本内容Base64編碼。原文長度需小於15000位元，即5000個漢字以内。
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


class TextOutputComm(AbstractModel):
    """訊息類輸出公共參數

    """

    def __init__(self):
        """
        :param AppID: 接入業務的唯一ID
        :type AppID: int
        :param BUCtrlID: 介面唯一ID，旁路調用介面返回有該欄位，標識唯一介面
        :type BUCtrlID: int
        :param SendTime: 訊息發送時間
        :type SendTime: int
        :param Uin: 請求欄位裏的Common.Uin
        :type Uin: int
        """
        self.AppID = None
        self.BUCtrlID = None
        self.SendTime = None
        self.Uin = None


    def _deserialize(self, params):
        self.AppID = params.get("AppID")
        self.BUCtrlID = params.get("BUCtrlID")
        self.SendTime = params.get("SendTime")
        self.Uin = params.get("Uin")


class TextOutputID(AbstractModel):
    """訊息類輸出ID參數

    """

    def __init__(self):
        """
        :param MsgID: 接入業務的唯一ID
        :type MsgID: str
        :param Uin: 用戶賬號uin，對應請求協議裏的Content.User.Uin。旁路結果有回帶，串聯結果無該欄位
        :type Uin: str
        """
        self.MsgID = None
        self.Uin = None


    def _deserialize(self, params):
        self.MsgID = params.get("MsgID")
        self.Uin = params.get("Uin")


class TextOutputRes(AbstractModel):
    """訊息類輸出結果參數

    """

    def __init__(self):
        """
        :param Operator: 操作人,信安處理人企業 ID
        :type Operator: str
        :param ResultCode: 惡意操作碼，
删除（1）， 通過（2）， 先審後發（100012）
        :type ResultCode: int
        :param ResultMsg: 操作結果備注說明
        :type ResultMsg: str
        :param ResultType: 惡意類型，廣告（10001）， 政治（20001）， 色情（20002）， 社會事件（20004）， 暴力（20011）， 低俗（20012）， 違法犯罪（20006）， 欺詐（20008）， 版權（20013）， 謠言（20104）， 其他（21000）
        :type ResultType: int
        """
        self.Operator = None
        self.ResultCode = None
        self.ResultMsg = None
        self.ResultType = None


    def _deserialize(self, params):
        self.Operator = params.get("Operator")
        self.ResultCode = params.get("ResultCode")
        self.ResultMsg = params.get("ResultMsg")
        self.ResultType = params.get("ResultType")


class TextSample(AbstractModel):
    """文字樣本訊息

    """

    def __init__(self):
        """
        :param Code: 處理錯誤碼
        :type Code: int
        :param Content: 關鍵詞
        :type Content: str
        :param CreatedAt: 創建時間戳
        :type CreatedAt: int
        :param EvilType: 惡意類型
100：正常
20001：政治
20002：色情 
20006：涉毒違法
20007：謾罵 
20105：廣告引流 
24001：暴恐
        :type EvilType: int
        :param Id: 唯一標識
        :type Id: str
        :param Label: 樣本類型
1：黑庫
2：白庫
        :type Label: int
        :param Status: 任務狀态
1：已完成
2：處理中
        :type Status: int
        """
        self.Code = None
        self.Content = None
        self.CreatedAt = None
        self.EvilType = None
        self.Id = None
        self.Label = None
        self.Status = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Content = params.get("Content")
        self.CreatedAt = params.get("CreatedAt")
        self.EvilType = params.get("EvilType")
        self.Id = params.get("Id")
        self.Label = params.get("Label")
        self.Status = params.get("Status")