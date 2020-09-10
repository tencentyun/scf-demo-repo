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


class Album(AbstractModel):
    """Album

    """

    def __init__(self):
        """
        :param AlbumName: 專輯名
        :type AlbumName: str
        :param ImagePathMap: 專輯圖片大小及類别
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImagePathMap: list of ImagePath
        """
        self.AlbumName = None
        self.ImagePathMap = None


    def _deserialize(self, params):
        self.AlbumName = params.get("AlbumName")
        if params.get("ImagePathMap") is not None:
            self.ImagePathMap = []
            for item in params.get("ImagePathMap"):
                obj = ImagePath()
                obj._deserialize(item)
                self.ImagePathMap.append(obj)


class Artist(AbstractModel):
    """Artist

    """

    def __init__(self):
        """
        :param ArtistName: 歌手名
        :type ArtistName: str
        """
        self.ArtistName = None


    def _deserialize(self, params):
        self.ArtistName = params.get("ArtistName")


class DataInfo(AbstractModel):
    """數據訊息

    """

    def __init__(self):
        """
        :param Name: Song Name
        :type Name: str
        :param Version: 歌曲版本
        :type Version: str
        :param Duration: 歌曲總時長（非試聽時長）
        :type Duration: str
        :param AuditionBegin: 試聽開始時間
        :type AuditionBegin: int
        :param AuditionEnd: 試聽結束時間
        :type AuditionEnd: int
        """
        self.Name = None
        self.Version = None
        self.Duration = None
        self.AuditionBegin = None
        self.AuditionEnd = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Duration = params.get("Duration")
        self.AuditionBegin = params.get("AuditionBegin")
        self.AuditionEnd = params.get("AuditionEnd")


class DescribeItemsRequest(AbstractModel):
    """DescribeItems請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: offset (Default = 0)，(當前頁-1) * Limit
        :type Offset: int
        :param Limit: 條數，必須大于0，最大值爲30
        :type Limit: int
        :param CategoryId: （電台/歌單）ID，CategoryId和CategoryCode兩個必傳1個，可以從<a href="https://cloud.taifucloud.com/document/product/1155/40109">獲取分類内容（Station）清單介面</a>中獲取。
        :type CategoryId: str
        :param CategoryCode: （電台/歌單）ID，CategoryId和CategoryCode兩個必傳1個，可以從<a href="https://cloud.taifucloud.com/document/product/1155/40109">獲取分類内容（Station）清單介面</a>中獲取。
        :type CategoryCode: str
        """
        self.Offset = None
        self.Limit = None
        self.CategoryId = None
        self.CategoryCode = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CategoryId = params.get("CategoryId")
        self.CategoryCode = params.get("CategoryCode")


class DescribeItemsResponse(AbstractModel):
    """DescribeItems返回參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁偏移量
        :type Offset: int
        :param Size: 當前頁歌曲數量
        :type Size: int
        :param Total: 總數據條數
        :type Total: int
        :param HaveMore: 剩餘數量（total-offset-size），通過這個值判斷是否
還有下一頁
        :type HaveMore: int
        :param Items: Items 歌曲清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Items: list of Item
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Offset = None
        self.Size = None
        self.Total = None
        self.HaveMore = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Size = params.get("Size")
        self.Total = params.get("Total")
        self.HaveMore = params.get("HaveMore")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLyricRequest(AbstractModel):
    """DescribeLyric請求參數結構體

    """

    def __init__(self):
        """
        :param ItemId: 歌曲ID
        :type ItemId: str
        :param SubItemType: 歌詞格式，可選項，可不填寫，目前填寫只能填LRC-LRC。該欄位爲預留的擴展欄位。後續如果不填，會返回歌曲的所有格式的歌詞。如果填寫某個正确的格式，則只返回該格式的歌詞。
        :type SubItemType: str
        """
        self.ItemId = None
        self.SubItemType = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.SubItemType = params.get("SubItemType")


class DescribeLyricResponse(AbstractModel):
    """DescribeLyric返回參數結構體

    """

    def __init__(self):
        """
        :param Lyric: 歌詞詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type Lyric: :class:`taifucloudcloud.ame.v20190916.models.Lyric`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Lyric = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Lyric") is not None:
            self.Lyric = Lyric()
            self.Lyric._deserialize(params.get("Lyric"))
        self.RequestId = params.get("RequestId")


class DescribeMusicRequest(AbstractModel):
    """DescribeMusic請求參數結構體

    """

    def __init__(self):
        """
        :param ItemId: 歌曲ID
        :type ItemId: str
        :param IdentityId: 在應用前端播放音樂C端用戶的唯一标識。無需是帳戶訊息，用戶唯一标識即可。
        :type IdentityId: str
        :param SubItemType: 填 MP3-64K-FTD-P 獲取歌曲熱門片段
        :type SubItemType: str
        :param Ssl: CDN URL Protocol:HTTP or HTTPS/SSL
Values:Y , N(default)
        :type Ssl: str
        """
        self.ItemId = None
        self.IdentityId = None
        self.SubItemType = None
        self.Ssl = None


    def _deserialize(self, params):
        self.ItemId = params.get("ItemId")
        self.IdentityId = params.get("IdentityId")
        self.SubItemType = params.get("SubItemType")
        self.Ssl = params.get("Ssl")


class DescribeMusicResponse(AbstractModel):
    """DescribeMusic返回參數結構體

    """

    def __init__(self):
        """
        :param Music: 音樂相關訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Music: :class:`taifucloudcloud.ame.v20190916.models.Music`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Music = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Music") is not None:
            self.Music = Music()
            self.Music._deserialize(params.get("Music"))
        self.RequestId = params.get("RequestId")


class DescribeStationsRequest(AbstractModel):
    """DescribeStations請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 條數，必須大于0
        :type Limit: int
        :param Offset: offset (Default = 0)，(當前頁-1) * Limit
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeStationsResponse(AbstractModel):
    """DescribeStations返回參數結構體

    """

    def __init__(self):
        """
        :param Total: 總數量
        :type Total: int
        :param Offset: 分頁偏移量
        :type Offset: int
        :param Size: 當前頁station數量
        :type Size: int
        :param HaveMore: 剩餘數量（total-offset-size），通過這個值判斷是否還有下一頁
        :type HaveMore: int
        :param Stations: Stations 素材庫清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Stations: list of Station
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Offset = None
        self.Size = None
        self.HaveMore = None
        self.Stations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Offset = params.get("Offset")
        self.Size = params.get("Size")
        self.HaveMore = params.get("HaveMore")
        if params.get("Stations") is not None:
            self.Stations = []
            for item in params.get("Stations"):
                obj = Station()
                obj._deserialize(item)
                self.Stations.append(obj)
        self.RequestId = params.get("RequestId")


class ImagePath(AbstractModel):
    """圖片路徑

    """

    def __init__(self):
        """
        :param Key: station圖片大小及類别
注意：此欄位可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: station圖片網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class Item(AbstractModel):
    """Item

    """

    def __init__(self):
        """
        :param ItemID: Song ID
        :type ItemID: str
        :param DataInfo: Song info
注意：此欄位可能返回 null，表示取不到有效值。
        :type DataInfo: :class:`taifucloudcloud.ame.v20190916.models.DataInfo`
        :param Album: 專輯訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type Album: :class:`taifucloudcloud.ame.v20190916.models.Album`
        :param Artists: 多個歌手集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type Artists: list of Artist
        """
        self.ItemID = None
        self.DataInfo = None
        self.Album = None
        self.Artists = None


    def _deserialize(self, params):
        self.ItemID = params.get("ItemID")
        if params.get("DataInfo") is not None:
            self.DataInfo = DataInfo()
            self.DataInfo._deserialize(params.get("DataInfo"))
        if params.get("Album") is not None:
            self.Album = Album()
            self.Album._deserialize(params.get("Album"))
        if params.get("Artists") is not None:
            self.Artists = []
            for item in params.get("Artists"):
                obj = Artist()
                obj._deserialize(item)
                self.Artists.append(obj)


class Lyric(AbstractModel):
    """歌詞訊息

    """

    def __init__(self):
        """
        :param Url: 歌詞cdn網址
        :type Url: str
        :param FileNameExt: 歌詞後綴名
        :type FileNameExt: str
        :param SubItemType: 歌詞類型
        :type SubItemType: str
        """
        self.Url = None
        self.FileNameExt = None
        self.SubItemType = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileNameExt = params.get("FileNameExt")
        self.SubItemType = params.get("SubItemType")


class Music(AbstractModel):
    """音樂詳情

    """

    def __init__(self):
        """
        :param Url: 音樂播放連結相對路徑，必須通過在正版曲庫直通車控制台上登記的域名進行拼接。
        :type Url: str
        :param FileSize: 音訊文件大小
        :type FileSize: int
        :param FileExtension: 音訊文件類型
        :type FileExtension: str
        :param AuditionBegin: Song fragment start.試聽片段開始時間，試聽時長爲auditionEnd-auditionBegin
Unit :ms
        :type AuditionBegin: int
        :param AuditionEnd: Song fragment end.試聽片段結束時間, 試聽時長爲auditionEnd-auditionBegin
Unit :ms
        :type AuditionEnd: int
        :param FullUrl: 音樂播放連結全路徑，前提是在正版曲庫直通車控制台添加過域名，否則返回空字元。
如果添加過多個域名只返回第一個添加域名的播放全路徑。
        :type FullUrl: str
        """
        self.Url = None
        self.FileSize = None
        self.FileExtension = None
        self.AuditionBegin = None
        self.AuditionEnd = None
        self.FullUrl = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.FileSize = params.get("FileSize")
        self.FileExtension = params.get("FileExtension")
        self.AuditionBegin = params.get("AuditionBegin")
        self.AuditionEnd = params.get("AuditionEnd")
        self.FullUrl = params.get("FullUrl")


class ReportDataRequest(AbstractModel):
    """ReportData請求參數結構體

    """

    def __init__(self):
        """
        :param ReportData: 上報數據
注:reportData爲用戶端壓縮後的上報數據進行16進制轉換的字串數據
壓縮說明：
a) 上報的json格式字串通過流的轉換（ByteArrayInputStream, java.util.zip.GZIPOutputStream），獲取到壓縮後的位元數組。
b) 将壓縮後的位元數組轉成16進制字串。

reportData由兩部分數據組成：
1）report_type（上報類型）
2）data（歌曲上報數據）
不同的report_type對應的data數據結構不一樣。

詳細說明請參考文件reportdata.docx：
https://github.com/ame-demo/doc
        :type ReportData: str
        """
        self.ReportData = None


    def _deserialize(self, params):
        self.ReportData = params.get("ReportData")


class ReportDataResponse(AbstractModel):
    """ReportData返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Station(AbstractModel):
    """分類内容

    """

    def __init__(self):
        """
        :param CategoryID: StationID
        :type CategoryID: str
        :param CategoryCode: Station MCCode
注意：此欄位可能返回 null，表示取不到有效值。
        :type CategoryCode: str
        :param Name: Category Name
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param Rank: Station的排序值，供參考（返回結果已按其升序）
注意：此欄位可能返回 null，表示取不到有效值。
        :type Rank: int
        :param ImagePathMap: station圖片集合
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImagePathMap: list of ImagePath
        """
        self.CategoryID = None
        self.CategoryCode = None
        self.Name = None
        self.Rank = None
        self.ImagePathMap = None


    def _deserialize(self, params):
        self.CategoryID = params.get("CategoryID")
        self.CategoryCode = params.get("CategoryCode")
        self.Name = params.get("Name")
        self.Rank = params.get("Rank")
        if params.get("ImagePathMap") is not None:
            self.ImagePathMap = []
            for item in params.get("ImagePathMap"):
                obj = ImagePath()
                obj._deserialize(item)
                self.ImagePathMap.append(obj)