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


class AgePortrait(AbstractModel):
    """用戶年齡畫像

    """

    def __init__(self):
        """
        :param AgeRange: 年齡區間
        :type AgeRange: str
        :param Percent: 百分比
        :type Percent: float
        """
        self.AgeRange = None
        self.Percent = None


    def _deserialize(self, params):
        self.AgeRange = params.get("AgeRange")
        self.Percent = params.get("Percent")


class AgePortraitInfo(AbstractModel):
    """用戶年齡畫像元素數組

    """

    def __init__(self):
        """
        :param PortraitSet: 用戶年齡畫像數組
        :type PortraitSet: list of AgePortrait
        """
        self.PortraitSet = None


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self.PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = AgePortrait()
                obj._deserialize(item)
                self.PortraitSet.append(obj)


class BrandReportArticle(AbstractModel):
    """文章訊息

    """

    def __init__(self):
        """
        :param Title: 文章標題
        :type Title: str
        :param Url: 文章url網址
        :type Url: str
        :param FromSite: 文章來源
        :type FromSite: str
        :param PubTime: 文章發表日期
        :type PubTime: str
        :param Flag: 文章標識
        :type Flag: int
        :param Hot: 文章熱度值
        :type Hot: int
        :param Level: 文章來源等級
        :type Level: int
        :param Abstract: 文章摘要
        :type Abstract: str
        :param ArticleId: 文章ID
        :type ArticleId: str
        """
        self.Title = None
        self.Url = None
        self.FromSite = None
        self.PubTime = None
        self.Flag = None
        self.Hot = None
        self.Level = None
        self.Abstract = None
        self.ArticleId = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Url = params.get("Url")
        self.FromSite = params.get("FromSite")
        self.PubTime = params.get("PubTime")
        self.Flag = params.get("Flag")
        self.Hot = params.get("Hot")
        self.Level = params.get("Level")
        self.Abstract = params.get("Abstract")
        self.ArticleId = params.get("ArticleId")


class Comment(AbstractModel):
    """用戶好評差評個數訊息

    """

    def __init__(self):
        """
        :param Date: 評論的日期
        :type Date: str
        :param NegCommentCount: 差評的個數
        :type NegCommentCount: int
        :param PosCommentCount: 好評的個數
        :type PosCommentCount: int
        """
        self.Date = None
        self.NegCommentCount = None
        self.PosCommentCount = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.NegCommentCount = params.get("NegCommentCount")
        self.PosCommentCount = params.get("PosCommentCount")


class CommentInfo(AbstractModel):
    """用戶評論内容類型

    """

    def __init__(self):
        """
        :param Comment: 用戶評論内容
        :type Comment: str
        :param Date: 評論的時間
        :type Date: str
        """
        self.Comment = None
        self.Date = None


    def _deserialize(self, params):
        self.Comment = params.get("Comment")
        self.Date = params.get("Date")


class DateCount(AbstractModel):
    """按日期的統計數據

    """

    def __init__(self):
        """
        :param Date: 統計日期
        :type Date: str
        :param Count: 統計值
        :type Count: int
        """
        self.Date = None
        self.Count = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.Count = params.get("Count")


class DescribeBrandCommentCountRequest(AbstractModel):
    """DescribeBrandCommentCount請求參數結構體

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID
        :type BrandId: str
        :param StartDate: 查詢開始日期
        :type StartDate: str
        :param EndDate: 查詢結束日期
        :type EndDate: str
        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeBrandCommentCountResponse(AbstractModel):
    """DescribeBrandCommentCount返回參數結構體

    """

    def __init__(self):
        """
        :param CommentSet: 按天統計好評/差評數
        :type CommentSet: list of Comment
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CommentSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CommentSet") is not None:
            self.CommentSet = []
            for item in params.get("CommentSet"):
                obj = Comment()
                obj._deserialize(item)
                self.CommentSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBrandExposureRequest(AbstractModel):
    """DescribeBrandExposure請求參數結構體

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID
        :type BrandId: str
        :param StartDate: 查詢開始時間
        :type StartDate: str
        :param EndDate: 查詢結束時間
        :type EndDate: str
        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeBrandExposureResponse(AbstractModel):
    """DescribeBrandExposure返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 累計曝光量
        :type TotalCount: int
        :param DateCountSet: 按天計算的統計數據
        :type DateCountSet: list of DateCount
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DateCountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DateCountSet") is not None:
            self.DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self.DateCountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBrandMediaReportRequest(AbstractModel):
    """DescribeBrandMediaReport請求參數結構體

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID
        :type BrandId: str
        :param StartDate: 查詢開始時間
        :type StartDate: str
        :param EndDate: 查詢結束時間
        :type EndDate: str
        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeBrandMediaReportResponse(AbstractModel):
    """DescribeBrandMediaReport返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 查詢範圍内文章總數
        :type TotalCount: int
        :param DateCountSet: 按天計算的每天文章數
        :type DateCountSet: list of DateCount
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DateCountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DateCountSet") is not None:
            self.DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self.DateCountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBrandNegCommentsRequest(AbstractModel):
    """DescribeBrandNegComments請求參數結構體

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID
        :type BrandId: str
        :param StartDate: 查詢開始時間
        :type StartDate: str
        :param EndDate: 查詢結束時間
        :type EndDate: str
        :param Limit: 查詢條數上限，預設20
        :type Limit: int
        :param Offset: 查詢偏移，預設從0開始
        :type Offset: int
        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeBrandNegCommentsResponse(AbstractModel):
    """DescribeBrandNegComments返回參數結構體

    """

    def __init__(self):
        """
        :param BrandCommentSet: 評論清單
        :type BrandCommentSet: list of CommentInfo
        :param TotalComments: 總的差評個數
        :type TotalComments: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BrandCommentSet = None
        self.TotalComments = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BrandCommentSet") is not None:
            self.BrandCommentSet = []
            for item in params.get("BrandCommentSet"):
                obj = CommentInfo()
                obj._deserialize(item)
                self.BrandCommentSet.append(obj)
        self.TotalComments = params.get("TotalComments")
        self.RequestId = params.get("RequestId")


class DescribeBrandPosCommentsRequest(AbstractModel):
    """DescribeBrandPosComments請求參數結構體

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID
        :type BrandId: str
        :param StartDate: 查詢開始時間
        :type StartDate: str
        :param EndDate: 查詢結束時間
        :type EndDate: str
        :param Limit: 查詢條數上限，預設20
        :type Limit: int
        :param Offset: 查詢偏移，從0開始
        :type Offset: int
        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeBrandPosCommentsResponse(AbstractModel):
    """DescribeBrandPosComments返回參數結構體

    """

    def __init__(self):
        """
        :param BrandCommentSet: 評論清單
        :type BrandCommentSet: list of CommentInfo
        :param TotalComments: 總的好評個數
        :type TotalComments: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.BrandCommentSet = None
        self.TotalComments = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BrandCommentSet") is not None:
            self.BrandCommentSet = []
            for item in params.get("BrandCommentSet"):
                obj = CommentInfo()
                obj._deserialize(item)
                self.BrandCommentSet.append(obj)
        self.TotalComments = params.get("TotalComments")
        self.RequestId = params.get("RequestId")


class DescribeBrandSocialOpinionRequest(AbstractModel):
    """DescribeBrandSocialOpinion請求參數結構體

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID
        :type BrandId: str
        :param StartDate: 檢索開始時間
        :type StartDate: str
        :param EndDate: 檢索結束時間
        :type EndDate: str
        :param Offset: 查詢偏移，預設從0開始
        :type Offset: int
        :param Limit: 查詢條數上限，預設20
        :type Limit: int
        :param ShowList: 清單顯示標記，若爲true，則返回文章清單詳情
        :type ShowList: bool
        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None
        self.ShowList = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ShowList = params.get("ShowList")


class DescribeBrandSocialOpinionResponse(AbstractModel):
    """DescribeBrandSocialOpinion返回參數結構體

    """

    def __init__(self):
        """
        :param ArticleCount: 文章總數
        :type ArticleCount: int
        :param FromCount: 來源統計總數
        :type FromCount: int
        :param AdverseCount: 疑似負面報道總數
        :type AdverseCount: int
        :param ArticleSet: 文章清單詳情
        :type ArticleSet: list of BrandReportArticle
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ArticleCount = None
        self.FromCount = None
        self.AdverseCount = None
        self.ArticleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ArticleCount = params.get("ArticleCount")
        self.FromCount = params.get("FromCount")
        self.AdverseCount = params.get("AdverseCount")
        if params.get("ArticleSet") is not None:
            self.ArticleSet = []
            for item in params.get("ArticleSet"):
                obj = BrandReportArticle()
                obj._deserialize(item)
                self.ArticleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBrandSocialReportRequest(AbstractModel):
    """DescribeBrandSocialReport請求參數結構體

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID
        :type BrandId: str
        :param StartDate: 查詢開始時間
        :type StartDate: str
        :param EndDate: 查詢結束時間
        :type EndDate: str
        """
        self.BrandId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeBrandSocialReportResponse(AbstractModel):
    """DescribeBrandSocialReport返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 累計統計數據
        :type TotalCount: int
        :param DateCountSet: 按天計算的統計數據
        :type DateCountSet: list of DateCount
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DateCountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DateCountSet") is not None:
            self.DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self.DateCountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIndustryNewsRequest(AbstractModel):
    """DescribeIndustryNews請求參數結構體

    """

    def __init__(self):
        """
        :param IndustryId: 行業ID
        :type IndustryId: str
        :param StartDate: 查詢開始時間
        :type StartDate: str
        :param EndDate: 查詢結束時間
        :type EndDate: str
        :param ShowList: 是否顯示清單，若爲 true，則返回文章清單
        :type ShowList: bool
        :param Offset: 查詢偏移，預設從0開始
        :type Offset: int
        :param Limit: 查詢條數上限，預設20
        :type Limit: int
        """
        self.IndustryId = None
        self.StartDate = None
        self.EndDate = None
        self.ShowList = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.IndustryId = params.get("IndustryId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.ShowList = params.get("ShowList")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeIndustryNewsResponse(AbstractModel):
    """DescribeIndustryNews返回參數結構體

    """

    def __init__(self):
        """
        :param NewsCount: 總計文章數量
        :type NewsCount: int
        :param FromCount: 總計來源數量
        :type FromCount: int
        :param AdverseCount: 總計疑似負面數量
        :type AdverseCount: int
        :param NewsSet: 文章清單
        :type NewsSet: list of IndustryNews
        :param DateCountSet: 按天統計的數量清單
        :type DateCountSet: list of DateCount
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NewsCount = None
        self.FromCount = None
        self.AdverseCount = None
        self.NewsSet = None
        self.DateCountSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NewsCount = params.get("NewsCount")
        self.FromCount = params.get("FromCount")
        self.AdverseCount = params.get("AdverseCount")
        if params.get("NewsSet") is not None:
            self.NewsSet = []
            for item in params.get("NewsSet"):
                obj = IndustryNews()
                obj._deserialize(item)
                self.NewsSet.append(obj)
        if params.get("DateCountSet") is not None:
            self.DateCountSet = []
            for item in params.get("DateCountSet"):
                obj = DateCount()
                obj._deserialize(item)
                self.DateCountSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserPortraitRequest(AbstractModel):
    """DescribeUserPortrait請求參數結構體

    """

    def __init__(self):
        """
        :param BrandId: 品牌ID
        :type BrandId: str
        """
        self.BrandId = None


    def _deserialize(self, params):
        self.BrandId = params.get("BrandId")


class DescribeUserPortraitResponse(AbstractModel):
    """DescribeUserPortrait返回參數結構體

    """

    def __init__(self):
        """
        :param Age: 年齡畫像
        :type Age: :class:`taifucloudcloud.tbm.v20180129.models.AgePortraitInfo`
        :param Gender: 性别畫像
        :type Gender: :class:`taifucloudcloud.tbm.v20180129.models.GenderPortraitInfo`
        :param Province:  畫像
        :type Province: :class:`taifucloudcloud.tbm.v20180129.models.ProvincePortraitInfo`
        :param Movie: 電影喜好畫像
        :type Movie: :class:`taifucloudcloud.tbm.v20180129.models.MoviePortraitInfo`
        :param Star: 明星喜好畫像
        :type Star: :class:`taifucloudcloud.tbm.v20180129.models.StarPortraitInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Age = None
        self.Gender = None
        self.Province = None
        self.Movie = None
        self.Star = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Age") is not None:
            self.Age = AgePortraitInfo()
            self.Age._deserialize(params.get("Age"))
        if params.get("Gender") is not None:
            self.Gender = GenderPortraitInfo()
            self.Gender._deserialize(params.get("Gender"))
        if params.get("Province") is not None:
            self.Province = ProvincePortraitInfo()
            self.Province._deserialize(params.get("Province"))
        if params.get("Movie") is not None:
            self.Movie = MoviePortraitInfo()
            self.Movie._deserialize(params.get("Movie"))
        if params.get("Star") is not None:
            self.Star = StarPortraitInfo()
            self.Star._deserialize(params.get("Star"))
        self.RequestId = params.get("RequestId")


class GenderPortrait(AbstractModel):
    """性别畫像元素

    """

    def __init__(self):
        """
        :param Gender: 性别
        :type Gender: str
        :param Percent: 百分比
        :type Percent: int
        """
        self.Gender = None
        self.Percent = None


    def _deserialize(self, params):
        self.Gender = params.get("Gender")
        self.Percent = params.get("Percent")


class GenderPortraitInfo(AbstractModel):
    """用戶性别畫像元素數組

    """

    def __init__(self):
        """
        :param PortraitSet: 用戶性别畫像數組
        :type PortraitSet: list of GenderPortrait
        """
        self.PortraitSet = None


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self.PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = GenderPortrait()
                obj._deserialize(item)
                self.PortraitSet.append(obj)


class IndustryNews(AbstractModel):
    """行業報道新聞

    """

    def __init__(self):
        """
        :param IndustryId: 行業報道ID
        :type IndustryId: str
        :param PubTime: 報道發表時間
        :type PubTime: str
        :param FromSite: 報道來源
        :type FromSite: str
        :param Title: 報道標題
        :type Title: str
        :param Url: 報道來源url
        :type Url: str
        :param Level: 報道來源等級
        :type Level: int
        :param Hot: 熱度值
        :type Hot: int
        :param Flag: 報道標識
        :type Flag: int
        :param Abstract: 報道摘要
        :type Abstract: str
        """
        self.IndustryId = None
        self.PubTime = None
        self.FromSite = None
        self.Title = None
        self.Url = None
        self.Level = None
        self.Hot = None
        self.Flag = None
        self.Abstract = None


    def _deserialize(self, params):
        self.IndustryId = params.get("IndustryId")
        self.PubTime = params.get("PubTime")
        self.FromSite = params.get("FromSite")
        self.Title = params.get("Title")
        self.Url = params.get("Url")
        self.Level = params.get("Level")
        self.Hot = params.get("Hot")
        self.Flag = params.get("Flag")
        self.Abstract = params.get("Abstract")


class MoviePortrait(AbstractModel):
    """電影喜好畫像元素

    """

    def __init__(self):
        """
        :param Name: 電影名稱
        :type Name: str
        :param Percent: 百分比
        :type Percent: float
        """
        self.Name = None
        self.Percent = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Percent = params.get("Percent")


class MoviePortraitInfo(AbstractModel):
    """用戶喜好電影畫像元素數組

    """

    def __init__(self):
        """
        :param PortraitSet: 用戶喜好電影畫像數組
        :type PortraitSet: list of MoviePortrait
        """
        self.PortraitSet = None


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self.PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = MoviePortrait()
                obj._deserialize(item)
                self.PortraitSet.append(obj)


class ProvincePortrait(AbstractModel):
    """ 畫像元素

    """

    def __init__(self):
        """
        :param Province:  名稱
        :type Province: str
        :param Percent: 百分比
        :type Percent: float
        """
        self.Province = None
        self.Percent = None


    def _deserialize(self, params):
        self.Province = params.get("Province")
        self.Percent = params.get("Percent")


class ProvincePortraitInfo(AbstractModel):
    """用戶 畫像元素數組

    """

    def __init__(self):
        """
        :param PortraitSet: 用戶 畫像數組
        :type PortraitSet: list of ProvincePortrait
        """
        self.PortraitSet = None


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self.PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = ProvincePortrait()
                obj._deserialize(item)
                self.PortraitSet.append(obj)


class StarPortrait(AbstractModel):
    """明星喜好畫像元素

    """

    def __init__(self):
        """
        :param Name: 喜歡的明星名字
        :type Name: str
        :param Percent: 百分比
        :type Percent: float
        """
        self.Name = None
        self.Percent = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Percent = params.get("Percent")


class StarPortraitInfo(AbstractModel):
    """用戶喜好的明星畫像元素數組

    """

    def __init__(self):
        """
        :param PortraitSet: 用戶喜好的明星畫像數組
        :type PortraitSet: list of StarPortrait
        """
        self.PortraitSet = None


    def _deserialize(self, params):
        if params.get("PortraitSet") is not None:
            self.PortraitSet = []
            for item in params.get("PortraitSet"):
                obj = StarPortrait()
                obj._deserialize(item)
                self.PortraitSet.append(obj)