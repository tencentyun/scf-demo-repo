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


class ArrivedMallInfo(AbstractModel):
    """客戶到場訊息

    """

    def __init__(self):
        """
        :param ArrivedTime: 到場時間
        :type ArrivedTime: str
        :param LeaveTime: 出場時間
        :type LeaveTime: str
        :param StaySecond: 停留時間，秒
        :type StaySecond: int
        :param InCapPic: 到場抓拍圖片
        :type InCapPic: str
        :param OutCapPic: 出場抓拍圖片
        :type OutCapPic: str
        :param TraceId: 軌迹編碼
        :type TraceId: str
        """
        self.ArrivedTime = None
        self.LeaveTime = None
        self.StaySecond = None
        self.InCapPic = None
        self.OutCapPic = None
        self.TraceId = None


    def _deserialize(self, params):
        self.ArrivedTime = params.get("ArrivedTime")
        self.LeaveTime = params.get("LeaveTime")
        self.StaySecond = params.get("StaySecond")
        self.InCapPic = params.get("InCapPic")
        self.OutCapPic = params.get("OutCapPic")
        self.TraceId = params.get("TraceId")


class CameraPersonInfo(AbstractModel):
    """攝像頭抓圖人物屬性

    """

    def __init__(self):
        """
        :param TempId: 臨時id，還未生成face id時返回
        :type TempId: str
        :param FaceId: 人臉face id
        :type FaceId: int
        :param IdType: 确定當次返回的哪個id有效，1-FaceId，2-TempId
        :type IdType: int
        :param FacePic: 當次抓拍到的人臉圖片base編碼
        :type FacePic: str
        :param Time: 當次抓拍時間戳
        :type Time: int
        :param PersonInfo: 當前的person基本訊息，圖片以FacePic爲準，結構體内未填
        :type PersonInfo: :class:`tencentcloud.youmall.v20180228.models.PersonInfo`
        """
        self.TempId = None
        self.FaceId = None
        self.IdType = None
        self.FacePic = None
        self.Time = None
        self.PersonInfo = None


    def _deserialize(self, params):
        self.TempId = params.get("TempId")
        self.FaceId = params.get("FaceId")
        self.IdType = params.get("IdType")
        self.FacePic = params.get("FacePic")
        self.Time = params.get("Time")
        if params.get("PersonInfo") is not None:
            self.PersonInfo = PersonInfo()
            self.PersonInfo._deserialize(params.get("PersonInfo"))


class CreateAccountRequest(AbstractModel):
    """CreateAccount請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param Name: 賬号名；需要是手機号
        :type Name: str
        :param Password: 密碼；需要是(`~!@#$%^&*()_+=-）中的至少兩種且八位以上
        :type Password: str
        :param ShopCode: 客戶門店編碼
        :type ShopCode: str
        :param Remark: 備注說明; 30個字元以内
        :type Remark: str
        """
        self.CompanyId = None
        self.Name = None
        self.Password = None
        self.ShopCode = None
        self.Remark = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.ShopCode = params.get("ShopCode")
        self.Remark = params.get("Remark")


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFacePictureRequest(AbstractModel):
    """CreateFacePicture請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param PersonType: 人物類型（0表示普通顧客，1 白名單，2 表示黑名單，101表示集團白名單，102表示集團黑名單）
        :type PersonType: int
        :param Picture: 圖片BASE編碼
        :type Picture: str
        :param PictureName: 圖片名稱
        :type PictureName: str
        :param ShopId: 店鋪ID，如果不填表示操作集團身份庫
        :type ShopId: int
        :param IsForceUpload: 是否強制更新：爲ture時會爲用戶創建一個新的指定PersonType的身份;目前這個參數已廢棄，可不傳
        :type IsForceUpload: bool
        """
        self.CompanyId = None
        self.PersonType = None
        self.Picture = None
        self.PictureName = None
        self.ShopId = None
        self.IsForceUpload = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.PersonType = params.get("PersonType")
        self.Picture = params.get("Picture")
        self.PictureName = params.get("PictureName")
        self.ShopId = params.get("ShopId")
        self.IsForceUpload = params.get("IsForceUpload")


class CreateFacePictureResponse(AbstractModel):
    """CreateFacePicture返回參數結構體

    """

    def __init__(self):
        """
        :param PersonId: 人物ID
        :type PersonId: int
        :param Status: 0.正常建檔 1.重複身份 2.未檢測到人臉 3.檢測到多個人臉 4.人臉大小過小 5.人臉質量不達标 6.其他錯誤
        :type Status: int
        :param PictureUrl: 圖片url
        :type PictureUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PersonId = None
        self.Status = None
        self.PictureUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Status = params.get("Status")
        self.PictureUrl = params.get("PictureUrl")
        self.RequestId = params.get("RequestId")


class DailyTracePoint(AbstractModel):
    """客戶天軌迹

    """

    def __init__(self):
        """
        :param TraceDate: 軌迹日期
        :type TraceDate: str
        :param TracePointSet: 軌迹點序列
        :type TracePointSet: list of PersonTracePoint
        """
        self.TraceDate = None
        self.TracePointSet = None


    def _deserialize(self, params):
        self.TraceDate = params.get("TraceDate")
        if params.get("TracePointSet") is not None:
            self.TracePointSet = []
            for item in params.get("TracePointSet"):
                obj = PersonTracePoint()
                obj._deserialize(item)
                self.TracePointSet.append(obj)


class DeletePersonFeatureRequest(AbstractModel):
    """DeletePersonFeature請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param PersonId: 顧客ID
        :type PersonId: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.PersonId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.PersonId = params.get("PersonId")


class DeletePersonFeatureResponse(AbstractModel):
    """DeletePersonFeature返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCameraPersonRequest(AbstractModel):
    """DescribeCameraPerson請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 優mall集團id，通過"指定身份标識獲取客戶門店清單"介面獲取
        :type CompanyId: str
        :param ShopId: 優mall店鋪id，通過"指定身份标識獲取客戶門店清單"介面獲取
        :type ShopId: int
        :param CameraId: 攝像頭id
        :type CameraId: int
        :param StartTime: 拉取開始時間戳，單位秒
        :type StartTime: int
        :param EndTime: 拉取結束時間戳，單位秒，不超過StartTime+10秒，超過預設爲StartTime+10
        :type EndTime: int
        :param PosId: pos機id
        :type PosId: str
        :param Num: 拉取圖片數，預設爲1，最大爲3
        :type Num: int
        :param IsNeedPic: 是否需要base64的圖片，0-不需要，1-需要，預設0
        :type IsNeedPic: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.CameraId = None
        self.StartTime = None
        self.EndTime = None
        self.PosId = None
        self.Num = None
        self.IsNeedPic = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.CameraId = params.get("CameraId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PosId = params.get("PosId")
        self.Num = params.get("Num")
        self.IsNeedPic = params.get("IsNeedPic")


class DescribeCameraPersonResponse(AbstractModel):
    """DescribeCameraPerson返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團id
        :type CompanyId: str
        :param ShopId: 店鋪id
        :type ShopId: int
        :param CameraId: 攝像機id
        :type CameraId: int
        :param PosId: pos機id
        :type PosId: str
        :param Infos: 抓取的顧客訊息
        :type Infos: list of CameraPersonInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.CameraId = None
        self.PosId = None
        self.Infos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.CameraId = params.get("CameraId")
        self.PosId = params.get("PosId")
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = CameraPersonInfo()
                obj._deserialize(item)
                self.Infos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterPersonArrivedMallRequest(AbstractModel):
    """DescribeClusterPersonArrivedMall請求參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場編碼
        :type MallId: str
        :param PersonId: 客戶編碼
        :type PersonId: str
        :param StartTime: 查詢開始時間
        :type StartTime: str
        :param EndTime: 查詢結束時間
        :type EndTime: str
        """
        self.MallId = None
        self.PersonId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeClusterPersonArrivedMallResponse(AbstractModel):
    """DescribeClusterPersonArrivedMall返回參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場系統編碼
        :type MallId: str
        :param MallCode: 賣場客戶編碼
        :type MallCode: str
        :param PersonId: 客戶編碼
        :type PersonId: str
        :param ArrivedMallSet: 到場訊息
        :type ArrivedMallSet: list of ArrivedMallInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MallId = None
        self.MallCode = None
        self.PersonId = None
        self.ArrivedMallSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.MallCode = params.get("MallCode")
        self.PersonId = params.get("PersonId")
        if params.get("ArrivedMallSet") is not None:
            self.ArrivedMallSet = []
            for item in params.get("ArrivedMallSet"):
                obj = ArrivedMallInfo()
                obj._deserialize(item)
                self.ArrivedMallSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterPersonTraceRequest(AbstractModel):
    """DescribeClusterPersonTrace請求參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場編碼
        :type MallId: str
        :param PersonId: 客戶編碼
        :type PersonId: str
        :param StartTime: 查詢開始時間
        :type StartTime: str
        :param EndTime: 查詢結束時間
        :type EndTime: str
        """
        self.MallId = None
        self.PersonId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeClusterPersonTraceResponse(AbstractModel):
    """DescribeClusterPersonTrace返回參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場系統編碼
        :type MallId: str
        :param MallCode: 賣場用戶編碼
        :type MallCode: str
        :param PersonId: 客戶編碼
        :type PersonId: str
        :param TracePointSet: 軌迹序列
        :type TracePointSet: list of DailyTracePoint
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MallId = None
        self.MallCode = None
        self.PersonId = None
        self.TracePointSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.MallCode = params.get("MallCode")
        self.PersonId = params.get("PersonId")
        if params.get("TracePointSet") is not None:
            self.TracePointSet = []
            for item in params.get("TracePointSet"):
                obj = DailyTracePoint()
                obj._deserialize(item)
                self.TracePointSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFaceIdByTempIdRequest(AbstractModel):
    """DescribeFaceIdByTempId請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 優mall集團id，通過"指定身份标識獲取客戶門店清單"介面獲取
        :type CompanyId: str
        :param ShopId: 優mall店鋪id，通過"指定身份标識獲取客戶門店清單"介面獲取
        :type ShopId: int
        :param TempId: 臨時id
        :type TempId: str
        :param CameraId: 攝像頭id
        :type CameraId: int
        :param PosId: pos機id
        :type PosId: str
        :param PictureExpires: 圖片url過期時間：在當前時間+PictureExpires秒後，圖片url無法繼續正常訪問；單位s；預設值1*24*60*60（1天）
        :type PictureExpires: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.TempId = None
        self.CameraId = None
        self.PosId = None
        self.PictureExpires = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TempId = params.get("TempId")
        self.CameraId = params.get("CameraId")
        self.PosId = params.get("PosId")
        self.PictureExpires = params.get("PictureExpires")


class DescribeFaceIdByTempIdResponse(AbstractModel):
    """DescribeFaceIdByTempId返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團id
        :type CompanyId: str
        :param ShopId: 店鋪id
        :type ShopId: int
        :param CameraId: 攝像機id
        :type CameraId: int
        :param PosId: pos機id
        :type PosId: str
        :param TempId: 請求的臨時id
        :type TempId: str
        :param FaceId: 臨時id對應的face id
        :type FaceId: int
        :param PersonInfo: 顧客屬性訊息
        :type PersonInfo: :class:`tencentcloud.youmall.v20180228.models.PersonInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.CameraId = None
        self.PosId = None
        self.TempId = None
        self.FaceId = None
        self.PersonInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.CameraId = params.get("CameraId")
        self.PosId = params.get("PosId")
        self.TempId = params.get("TempId")
        self.FaceId = params.get("FaceId")
        if params.get("PersonInfo") is not None:
            self.PersonInfo = PersonInfo()
            self.PersonInfo._deserialize(params.get("PersonInfo"))
        self.RequestId = params.get("RequestId")


class DescribeHistoryNetworkInfoRequest(AbstractModel):
    """DescribeHistoryNetworkInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Time: 請求時間戳
        :type Time: int
        :param CompanyId: 優mall集團id，通過"指定身份标識獲取客戶門店清單"介面獲取
        :type CompanyId: str
        :param ShopId: 優mall店鋪id，通過"指定身份标識獲取客戶門店清單"介面獲取，爲0則拉取集團全部店鋪當前
        :type ShopId: int
        :param StartDay: 拉取開始日期，格式：2018-09-05
        :type StartDay: str
        :param EndDay: 拉取結束日期，格式L:2018-09-05，超過StartDay 90天，按StartDay+90天算
        :type EndDay: str
        :param Limit: 拉取條數，預設10
        :type Limit: int
        :param Offset: 拉取偏移，返回offset之後的數據
        :type Offset: int
        """
        self.Time = None
        self.CompanyId = None
        self.ShopId = None
        self.StartDay = None
        self.EndDay = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDay = params.get("StartDay")
        self.EndDay = params.get("EndDay")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeHistoryNetworkInfoResponse(AbstractModel):
    """DescribeHistoryNetworkInfo返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceSet: 網絡狀态數據
        :type InstanceSet: :class:`tencentcloud.youmall.v20180228.models.NetworkHistoryInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = NetworkHistoryInfo()
            self.InstanceSet._deserialize(params.get("InstanceSet"))
        self.RequestId = params.get("RequestId")


class DescribeNetworkInfoRequest(AbstractModel):
    """DescribeNetworkInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Time: 請求時間戳
        :type Time: int
        :param CompanyId: 優mall集團id，通過"指定身份标識獲取客戶門店清單"介面獲取
        :type CompanyId: str
        :param ShopId: 優mall店鋪id，通過"指定身份标識獲取客戶門店清單"介面獲取，不填則拉取集團全部店鋪當前
        :type ShopId: int
        """
        self.Time = None
        self.CompanyId = None
        self.ShopId = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")


class DescribeNetworkInfoResponse(AbstractModel):
    """DescribeNetworkInfo返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceSet: 網絡狀态詳情
        :type InstanceSet: :class:`tencentcloud.youmall.v20180228.models.NetworkLastInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = NetworkLastInfo()
            self.InstanceSet._deserialize(params.get("InstanceSet"))
        self.RequestId = params.get("RequestId")


class DescribePersonArrivedMallRequest(AbstractModel):
    """DescribePersonArrivedMall請求參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場編碼
        :type MallId: str
        :param PersonId: 客戶編碼
        :type PersonId: str
        :param StartTime: 查詢開始時間
        :type StartTime: str
        :param EndTime: 查詢結束時間
        :type EndTime: str
        """
        self.MallId = None
        self.PersonId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribePersonArrivedMallResponse(AbstractModel):
    """DescribePersonArrivedMall返回參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場系統編碼
        :type MallId: str
        :param MallCode: 賣場用戶編碼
        :type MallCode: str
        :param PersonId: 客戶編碼
        :type PersonId: str
        :param ArrivedMallSet: 到場軌迹
        :type ArrivedMallSet: list of ArrivedMallInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MallId = None
        self.MallCode = None
        self.PersonId = None
        self.ArrivedMallSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.MallCode = params.get("MallCode")
        self.PersonId = params.get("PersonId")
        if params.get("ArrivedMallSet") is not None:
            self.ArrivedMallSet = []
            for item in params.get("ArrivedMallSet"):
                obj = ArrivedMallInfo()
                obj._deserialize(item)
                self.ArrivedMallSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonInfoByFacePictureRequest(AbstractModel):
    """DescribePersonInfoByFacePicture請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 優mall集團id，通過"指定身份标識獲取客戶門店清單"介面獲取
        :type CompanyId: str
        :param ShopId: 優mall店鋪id，通過"指定身份标識獲取客戶門店清單"介面獲取
        :type ShopId: int
        :param Picture: 人臉圖片BASE編碼
        :type Picture: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.Picture = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.Picture = params.get("Picture")


class DescribePersonInfoByFacePictureResponse(AbstractModel):
    """DescribePersonInfoByFacePicture返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團id
        :type CompanyId: str
        :param ShopId: 店鋪id
        :type ShopId: int
        :param PersonId: 顧客face id
        :type PersonId: int
        :param PictureUrl: 顧客底圖url
        :type PictureUrl: str
        :param PersonType: 顧客類型（0表示普通顧客，1 白名單，2 表示黑名單，101表示集團白名單，102表示集團黑名單）
        :type PersonType: int
        :param FirstVisitTime: 顧客首次進店時間
        :type FirstVisitTime: str
        :param VisitTimes: 顧客曆史到訪次數
        :type VisitTimes: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.PersonId = None
        self.PictureUrl = None
        self.PersonType = None
        self.FirstVisitTime = None
        self.VisitTimes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.PersonId = params.get("PersonId")
        self.PictureUrl = params.get("PictureUrl")
        self.PersonType = params.get("PersonType")
        self.FirstVisitTime = params.get("FirstVisitTime")
        self.VisitTimes = params.get("VisitTimes")
        self.RequestId = params.get("RequestId")


class DescribePersonInfoRequest(AbstractModel):
    """DescribePersonInfo請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param StartPersonId: 起始ID，第一次拉取時StartPersonId傳0，後續送入的值爲上一頁最後一條數據項的PersonId
        :type StartPersonId: int
        :param Offset: 偏移量：分頁控制參數，第一頁傳0，第n頁Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每頁的數據項，最大100，超過100會被強制指定爲100
        :type Limit: int
        :param PictureExpires: 圖片url過期時間：在當前時間+PictureExpires秒後，圖片url無法繼續正常訪問；單位s；預設值1*24*60*60（1天）
        :type PictureExpires: int
        :param PersonType: 身份類型(0表示普通顧客，1 白名單，2 表示黑名單）
        :type PersonType: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartPersonId = None
        self.Offset = None
        self.Limit = None
        self.PictureExpires = None
        self.PersonType = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartPersonId = params.get("StartPersonId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.PictureExpires = params.get("PictureExpires")
        self.PersonType = params.get("PersonType")


class DescribePersonInfoResponse(AbstractModel):
    """DescribePersonInfo返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param TotalCount: 總數
        :type TotalCount: int
        :param PersonInfoSet: 用戶訊息
        :type PersonInfoSet: list of PersonInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalCount = None
        self.PersonInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonInfoSet") is not None:
            self.PersonInfoSet = []
            for item in params.get("PersonInfoSet"):
                obj = PersonInfo()
                obj._deserialize(item)
                self.PersonInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonRequest(AbstractModel):
    """DescribePerson請求參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場編碼
        :type MallId: str
        :param Offset: 查詢偏移
        :type Offset: int
        :param Limit: 查詢數量，預設20，最大查詢數量100
        :type Limit: int
        """
        self.MallId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribePersonResponse(AbstractModel):
    """DescribePerson返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總計客戶數量
        :type TotalCount: int
        :param PersonSet: 客戶訊息
        :type PersonSet: list of PersonProfile
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PersonSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonSet") is not None:
            self.PersonSet = []
            for item in params.get("PersonSet"):
                obj = PersonProfile()
                obj._deserialize(item)
                self.PersonSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonTraceDetailRequest(AbstractModel):
    """DescribePersonTraceDetail請求參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場編碼
        :type MallId: str
        :param PersonId: 客戶編碼
        :type PersonId: str
        :param TraceId: 軌迹編碼
        :type TraceId: str
        """
        self.MallId = None
        self.PersonId = None
        self.TraceId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.TraceId = params.get("TraceId")


class DescribePersonTraceDetailResponse(AbstractModel):
    """DescribePersonTraceDetail返回參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場編碼
        :type MallId: str
        :param PersonId: 客戶編碼
        :type PersonId: str
        :param TraceId: 軌迹編碼
        :type TraceId: str
        :param CoordinateSet: 軌迹點坐标序列
        :type CoordinateSet: list of PersonCoordinate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MallId = None
        self.PersonId = None
        self.TraceId = None
        self.CoordinateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.TraceId = params.get("TraceId")
        if params.get("CoordinateSet") is not None:
            self.CoordinateSet = []
            for item in params.get("CoordinateSet"):
                obj = PersonCoordinate()
                obj._deserialize(item)
                self.CoordinateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonTraceRequest(AbstractModel):
    """DescribePersonTrace請求參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場編碼
        :type MallId: str
        :param PersonId: 客戶編碼
        :type PersonId: str
        :param StartTime: 查詢開始時間
        :type StartTime: str
        :param EndTime: 查詢結束時間
        :type EndTime: str
        """
        self.MallId = None
        self.PersonId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.PersonId = params.get("PersonId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribePersonTraceResponse(AbstractModel):
    """DescribePersonTrace返回參數結構體

    """

    def __init__(self):
        """
        :param MallId: 賣場系統編碼
        :type MallId: str
        :param MallCode: 賣場用戶編碼
        :type MallCode: str
        :param PersonId: 客戶編碼
        :type PersonId: str
        :param TraceRouteSet: 軌迹清單
        :type TraceRouteSet: list of PersonTraceRoute
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MallId = None
        self.MallCode = None
        self.PersonId = None
        self.TraceRouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MallId = params.get("MallId")
        self.MallCode = params.get("MallCode")
        self.PersonId = params.get("PersonId")
        if params.get("TraceRouteSet") is not None:
            self.TraceRouteSet = []
            for item in params.get("TraceRouteSet"):
                obj = PersonTraceRoute()
                obj._deserialize(item)
                self.TraceRouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePersonVisitInfoRequest(AbstractModel):
    """DescribePersonVisitInfo請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param Offset: 偏移量：分頁控制參數，第一頁傳0，第n頁Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每頁的數據項，最大100，超過100會被強制指定爲100
        :type Limit: int
        :param StartDate: 開始日期，格式yyyy-MM-dd，已廢棄，請使用StartDateTime
        :type StartDate: str
        :param EndDate: 結束日期，格式yyyy-MM-dd，已廢棄，請使用EndDateTime
        :type EndDate: str
        :param PictureExpires: 圖片url過期時間：在當前時間+PictureExpires秒後，圖片url無法繼續正常訪問；單位s；預設值1*24*60*60（1天）
        :type PictureExpires: int
        :param StartDateTime: 開始時間，格式yyyy-MM-dd HH:mm:ss
        :type StartDateTime: str
        :param EndDateTime: 結束時間，格式yyyy-MM-dd HH:mm:ss
        :type EndDateTime: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.Offset = None
        self.Limit = None
        self.StartDate = None
        self.EndDate = None
        self.PictureExpires = None
        self.StartDateTime = None
        self.EndDateTime = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.PictureExpires = params.get("PictureExpires")
        self.StartDateTime = params.get("StartDateTime")
        self.EndDateTime = params.get("EndDateTime")


class DescribePersonVisitInfoResponse(AbstractModel):
    """DescribePersonVisitInfo返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param TotalCount: 總數
        :type TotalCount: int
        :param PersonVisitInfoSet: 用戶到訪明細
        :type PersonVisitInfoSet: list of PersonVisitInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalCount = None
        self.PersonVisitInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalCount = params.get("TotalCount")
        if params.get("PersonVisitInfoSet") is not None:
            self.PersonVisitInfoSet = []
            for item in params.get("PersonVisitInfoSet"):
                obj = PersonVisitInfo()
                obj._deserialize(item)
                self.PersonVisitInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShopHourTrafficInfoRequest(AbstractModel):
    """DescribeShopHourTrafficInfo請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param StartDate: 開始日期，格式：yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 結束日期，格式：yyyy-MM-dd
        :type EndDate: str
        :param Offset: 偏移量：分頁控制參數，第一頁傳0，第n頁Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每頁的數據項，最大100，超過100會被強制指定爲100
        :type Limit: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeShopHourTrafficInfoResponse(AbstractModel):
    """DescribeShopHourTrafficInfo返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param TotalCount: 查詢結果總數
        :type TotalCount: int
        :param ShopHourTrafficInfoSet: 分時客流訊息
        :type ShopHourTrafficInfoSet: list of ShopHourTrafficInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalCount = None
        self.ShopHourTrafficInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalCount = params.get("TotalCount")
        if params.get("ShopHourTrafficInfoSet") is not None:
            self.ShopHourTrafficInfoSet = []
            for item in params.get("ShopHourTrafficInfoSet"):
                obj = ShopHourTrafficInfo()
                obj._deserialize(item)
                self.ShopHourTrafficInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShopInfoRequest(AbstractModel):
    """DescribeShopInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量：分頁控制參數，第一頁傳0，第n頁Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每頁的數據項，最大100，超過100會被強制指定爲100
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeShopInfoResponse(AbstractModel):
    """DescribeShopInfo返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 門店總數
        :type TotalCount: int
        :param ShopInfoSet: 門店清單訊息
        :type ShopInfoSet: list of ShopInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ShopInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ShopInfoSet") is not None:
            self.ShopInfoSet = []
            for item in params.get("ShopInfoSet"):
                obj = ShopInfo()
                obj._deserialize(item)
                self.ShopInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeShopTrafficInfoRequest(AbstractModel):
    """DescribeShopTrafficInfo請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param StartDate: 開始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 介紹日期，格式yyyy-MM-dd
        :type EndDate: str
        :param Offset: 偏移量：分頁控制參數，第一頁傳0，第n頁Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每頁的數據項，最大100，超過100會被強制指定爲100
        :type Limit: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeShopTrafficInfoResponse(AbstractModel):
    """DescribeShopTrafficInfo返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param TotalCount: 查詢結果總數
        :type TotalCount: int
        :param ShopDayTrafficInfoSet: 客流訊息清單
        :type ShopDayTrafficInfoSet: list of ShopDayTrafficInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalCount = None
        self.ShopDayTrafficInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalCount = params.get("TotalCount")
        if params.get("ShopDayTrafficInfoSet") is not None:
            self.ShopDayTrafficInfoSet = []
            for item in params.get("ShopDayTrafficInfoSet"):
                obj = ShopDayTrafficInfo()
                obj._deserialize(item)
                self.ShopDayTrafficInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTrajectoryDataRequest(AbstractModel):
    """DescribeTrajectoryData請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param StartDate: 開始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 結束日期，格式yyyy-MM-dd
        :type EndDate: str
        :param Limit: 限制返回數據的最大條數，最大 400（負數代爲 400）
        :type Limit: int
        :param Gender: 顧客性别顧慮，0是男，1是女，其它代表不分性别
        :type Gender: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None
        self.Limit = None
        self.Gender = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Limit = params.get("Limit")
        self.Gender = params.get("Gender")


class DescribeTrajectoryDataResponse(AbstractModel):
    """DescribeTrajectoryData返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param TotalPerson: 總人數
        :type TotalPerson: int
        :param TotalTrajectory: 總動迹數目
        :type TotalTrajectory: int
        :param Person: 返回動迹中的總人數
        :type Person: int
        :param Trajectory: 返回動迹的數目
        :type Trajectory: int
        :param Data: 返回動迹的具體訊息
        :type Data: list of TrajectorySunData
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalPerson = None
        self.TotalTrajectory = None
        self.Person = None
        self.Trajectory = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalPerson = params.get("TotalPerson")
        self.TotalTrajectory = params.get("TotalTrajectory")
        self.Person = params.get("Person")
        self.Trajectory = params.get("Trajectory")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TrajectorySunData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowAgeInfoByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowAgeInfoByZoneId請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param StartDate: 開始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 結束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeZoneFlowAgeInfoByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowAgeInfoByZoneId返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param ZoneName: 區域名稱
        :type ZoneName: str
        :param Data: 當前年齡段占比
        :type Data: list of float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.ZoneName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowAndStayTimeRequest(AbstractModel):
    """DescribeZoneFlowAndStayTime請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param StartDate: 開始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 結束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeZoneFlowAndStayTimeResponse(AbstractModel):
    """DescribeZoneFlowAndStayTime返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團id
        :type CompanyId: str
        :param ShopId: 店鋪id
        :type ShopId: int
        :param Data: 各區域人流數目和停留時長
        :type Data: list of ZoneFlowAndAvrStayTime
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ZoneFlowAndAvrStayTime()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowDailyByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowDailyByZoneId請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param StartDate: 開始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 結束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeZoneFlowDailyByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowDailyByZoneId返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團id
        :type CompanyId: str
        :param ShopId: 店鋪id
        :type ShopId: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param ZoneName: 區域名稱
        :type ZoneName: str
        :param Data: 每日人流量
        :type Data: list of ZoneDayFlow
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.ZoneName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ZoneDayFlow()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowGenderAvrStayTimeByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowGenderAvrStayTimeByZoneId請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param StartDate: 開始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 結束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeZoneFlowGenderAvrStayTimeByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowGenderAvrStayTimeByZoneId返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param ZoneName: 區域名稱
        :type ZoneName: str
        :param Data: 不同年齡段男女停留時間（返回格式爲數組，從第 1 個到最後一個數據，年齡段分别爲 0-17，18 - 23,  24 - 30, 31 - 40, 41 - 50, 51 - 60, 61 - 100）
        :type Data: list of ZoneAgeGroupAvrStayTime
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.ZoneName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ZoneAgeGroupAvrStayTime()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowGenderInfoByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowGenderInfoByZoneId請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param StartDate: 開始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 結束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeZoneFlowGenderInfoByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowGenderInfoByZoneId返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param ZoneName: 區域名稱
        :type ZoneName: str
        :param MalePercent: 男性占比
        :type MalePercent: float
        :param FemalePercent: 女性占比
        :type FemalePercent: float
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.ZoneName = None
        self.MalePercent = None
        self.FemalePercent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.MalePercent = params.get("MalePercent")
        self.FemalePercent = params.get("FemalePercent")
        self.RequestId = params.get("RequestId")


class DescribeZoneFlowHourlyByZoneIdRequest(AbstractModel):
    """DescribeZoneFlowHourlyByZoneId請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param StartDate: 開始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 結束日期，格式yyyy-MM-dd
        :type EndDate: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.StartDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")


class DescribeZoneFlowHourlyByZoneIdResponse(AbstractModel):
    """DescribeZoneFlowHourlyByZoneId返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param ZoneName: 區域名稱
        :type ZoneName: str
        :param Data: 各個分時人流量
        :type Data: list of ZoneHourFlow
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ZoneId = None
        self.ZoneName = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ZoneHourFlow()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeZoneTrafficInfoRequest(AbstractModel):
    """DescribeZoneTrafficInfo請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 店鋪ID
        :type ShopId: int
        :param StartDate: 開始日期，格式yyyy-MM-dd
        :type StartDate: str
        :param EndDate: 結束日期，格式yyyy-MM-dd
        :type EndDate: str
        :param Offset: 偏移量：分頁控制參數，第一頁傳0，第n頁Offset=(n-1)*Limit
        :type Offset: int
        :param Limit: Limit:每頁的數據項，最大100，超過100會被強制指定爲100
        :type Limit: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeZoneTrafficInfoResponse(AbstractModel):
    """DescribeZoneTrafficInfo返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param TotalCount: 查詢結果總數
        :type TotalCount: int
        :param ZoneTrafficInfoSet: 區域客流訊息清單
        :type ZoneTrafficInfoSet: list of ZoneTrafficInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.TotalCount = None
        self.ZoneTrafficInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.TotalCount = params.get("TotalCount")
        if params.get("ZoneTrafficInfoSet") is not None:
            self.ZoneTrafficInfoSet = []
            for item in params.get("ZoneTrafficInfoSet"):
                obj = ZoneTrafficInfo()
                obj._deserialize(item)
                self.ZoneTrafficInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class GenderAgeTrafficDetail(AbstractModel):
    """性别年齡分組下的客流訊息

    """

    def __init__(self):
        """
        :param Gender: 性别: 0男1女
        :type Gender: int
        :param AgeGap: 年齡區間，列舉值：0-17、18-23、24-30、31-40、41-50、51-60、>60
        :type AgeGap: str
        :param TrafficCount: 客流量
        :type TrafficCount: int
        """
        self.Gender = None
        self.AgeGap = None
        self.TrafficCount = None


    def _deserialize(self, params):
        self.Gender = params.get("Gender")
        self.AgeGap = params.get("AgeGap")
        self.TrafficCount = params.get("TrafficCount")


class HourTrafficInfoDetail(AbstractModel):
    """分時客流量詳細訊息

    """

    def __init__(self):
        """
        :param Hour: 小時 取值爲：0，1，2，3，4，5，6，7，8，9，10，11，12，13，14，15，16，17，18，19，20，21，22，23
        :type Hour: int
        :param HourTrafficTotalCount: 分時客流量
        :type HourTrafficTotalCount: int
        """
        self.Hour = None
        self.HourTrafficTotalCount = None


    def _deserialize(self, params):
        self.Hour = params.get("Hour")
        self.HourTrafficTotalCount = params.get("HourTrafficTotalCount")


class ModifyPersonFeatureInfoRequest(AbstractModel):
    """ModifyPersonFeatureInfo請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param PersonId: 需要修改的顧客id
        :type PersonId: int
        :param Picture: 圖片BASE編碼
        :type Picture: str
        :param PictureName: 圖片名稱（盡量不要重複）
        :type PictureName: str
        :param PersonType: 人物類型，僅能操作黑白名單顧客（1 白名單，2 表示黑名單，101表示集團白名單，102表示集團黑名單）
        :type PersonType: int
        :param ShopId: 店鋪ID，如果不填表示操作集團身份庫
        :type ShopId: int
        """
        self.CompanyId = None
        self.PersonId = None
        self.Picture = None
        self.PictureName = None
        self.PersonType = None
        self.ShopId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.PersonId = params.get("PersonId")
        self.Picture = params.get("Picture")
        self.PictureName = params.get("PictureName")
        self.PersonType = params.get("PersonType")
        self.ShopId = params.get("ShopId")


class ModifyPersonFeatureInfoResponse(AbstractModel):
    """ModifyPersonFeatureInfo返回參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 店鋪ID，如果不填表示操作集團身份庫
        :type ShopId: int
        :param PersonId: 請求的顧客id
        :type PersonId: int
        :param PersonIdBind: 圖片實際綁定person_id，可能與請求的person_id不同，以此id爲準
        :type PersonIdBind: int
        :param PersonType: 請求的顧客類型
        :type PersonType: int
        :param SimilarPersonIds: 與請求的person_id類型相同、與請求圖片特征相似的一個或多個person_id，需要額外确認這些id是否是同一個人
        :type SimilarPersonIds: list of int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.PersonId = None
        self.PersonIdBind = None
        self.PersonType = None
        self.SimilarPersonIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.PersonId = params.get("PersonId")
        self.PersonIdBind = params.get("PersonIdBind")
        self.PersonType = params.get("PersonType")
        self.SimilarPersonIds = params.get("SimilarPersonIds")
        self.RequestId = params.get("RequestId")


class ModifyPersonTagInfoRequest(AbstractModel):
    """ModifyPersonTagInfo請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 優mall集團id，通過"指定身份标識獲取客戶門店清單"介面獲取
        :type CompanyId: str
        :param ShopId: 優mall店鋪id，通過"指定身份标識獲取客戶門店清單"介面獲取，爲0則拉取集團全部店鋪當前
        :type ShopId: int
        :param Tags: 需要設置的顧客訊息，批次設置最大爲10個
        :type Tags: list of PersonTagInfo
        """
        self.CompanyId = None
        self.ShopId = None
        self.Tags = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = PersonTagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)


class ModifyPersonTagInfoResponse(AbstractModel):
    """ModifyPersonTagInfo返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPersonTypeRequest(AbstractModel):
    """ModifyPersonType請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param PersonId: 顧客ID
        :type PersonId: int
        :param PersonType: 身份類型(0表示普通顧客，1 白名單，2 表示黑名單）
        :type PersonType: int
        :param PersonSubType: 身份子類型:
PersonType=0時(普通顧客)，0普通顧客
PersonType=1時(白名單)，0店員，1商場人員，2其他類型人員，3區域經理，4注冊會員，5VIP用戶
PersonType=2時(黑名單)，0普通黑名單，1小偷)
        :type PersonSubType: int
        """
        self.CompanyId = None
        self.ShopId = None
        self.PersonId = None
        self.PersonType = None
        self.PersonSubType = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.PersonId = params.get("PersonId")
        self.PersonType = params.get("PersonType")
        self.PersonSubType = params.get("PersonSubType")


class ModifyPersonTypeResponse(AbstractModel):
    """ModifyPersonType返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NetworkAndShopInfo(AbstractModel):
    """網絡狀态

    """

    def __init__(self):
        """
        :param CompanyId: 集團id
        :type CompanyId: str
        :param ShopId: 店鋪id
        :type ShopId: int
        :param Province: 店鋪省份
        :type Province: str
        :param City: 店鋪城市
        :type City: str
        :param ShopName: 店鋪名
        :type ShopName: str
        :param Upload: 上傳頻寬，單位Mb/s，-1：未知
        :type Upload: float
        :param Download: 下載頻寬，單位Mb/s，-1：未知
        :type Download: float
        :param MinRtt: 最小延遲，單位ms，-1：未知
        :type MinRtt: float
        :param AvgRtt: 平均延遲，單位ms，-1：未知
        :type AvgRtt: float
        :param MaxRtt: 最大延遲，單位ms，-1：未知
        :type MaxRtt: float
        :param MdevRtt: 平均偏差延遲，單位ms，-1：未知
        :type MdevRtt: float
        :param Loss: 丢包率百分比，-1：未知
        :type Loss: float
        :param UpdateTime: 更新時間戳
        :type UpdateTime: int
        :param Mac: 上報網絡狀态設備
        :type Mac: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.Province = None
        self.City = None
        self.ShopName = None
        self.Upload = None
        self.Download = None
        self.MinRtt = None
        self.AvgRtt = None
        self.MaxRtt = None
        self.MdevRtt = None
        self.Loss = None
        self.UpdateTime = None
        self.Mac = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.ShopName = params.get("ShopName")
        self.Upload = params.get("Upload")
        self.Download = params.get("Download")
        self.MinRtt = params.get("MinRtt")
        self.AvgRtt = params.get("AvgRtt")
        self.MaxRtt = params.get("MaxRtt")
        self.MdevRtt = params.get("MdevRtt")
        self.Loss = params.get("Loss")
        self.UpdateTime = params.get("UpdateTime")
        self.Mac = params.get("Mac")


class NetworkHistoryInfo(AbstractModel):
    """查詢網絡狀态曆史數據輸出

    """

    def __init__(self):
        """
        :param Count: 總數
        :type Count: int
        :param CompanyId: 集團id
        :type CompanyId: str
        :param ShopId: 店鋪id
        :type ShopId: int
        :param Province: 店鋪省份
        :type Province: str
        :param City: 店鋪城市
        :type City: str
        :param ShopName: 店鋪名稱
        :type ShopName: str
        :param Infos: 網絡訊息
        :type Infos: list of NetworkInfo
        """
        self.Count = None
        self.CompanyId = None
        self.ShopId = None
        self.Province = None
        self.City = None
        self.ShopName = None
        self.Infos = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.ShopName = params.get("ShopName")
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = NetworkInfo()
                obj._deserialize(item)
                self.Infos.append(obj)


class NetworkInfo(AbstractModel):
    """沒有店鋪訊息的網絡狀态

    """

    def __init__(self):
        """
        :param Upload: 上傳頻寬，單位Mb/s，-1：未知
        :type Upload: float
        :param Download: 下載頻寬，單位Mb/s，-1：未知
        :type Download: float
        :param MinRtt: 最小延遲，單位ms，-1：未知
        :type MinRtt: float
        :param AvgRtt: 平均延遲，單位ms，-1：未知
        :type AvgRtt: float
        :param MaxRtt: 最大延遲，單位ms，-1：未知
        :type MaxRtt: float
        :param MdevRtt: 平均偏差延遲，單位ms，-1：未知
        :type MdevRtt: float
        :param Loss: 丢包率百分比，-1：未知
        :type Loss: float
        :param UpdateTime: 更新時間戳
        :type UpdateTime: int
        :param Mac: 上報網絡狀态設備
        :type Mac: str
        """
        self.Upload = None
        self.Download = None
        self.MinRtt = None
        self.AvgRtt = None
        self.MaxRtt = None
        self.MdevRtt = None
        self.Loss = None
        self.UpdateTime = None
        self.Mac = None


    def _deserialize(self, params):
        self.Upload = params.get("Upload")
        self.Download = params.get("Download")
        self.MinRtt = params.get("MinRtt")
        self.AvgRtt = params.get("AvgRtt")
        self.MaxRtt = params.get("MaxRtt")
        self.MdevRtt = params.get("MdevRtt")
        self.Loss = params.get("Loss")
        self.UpdateTime = params.get("UpdateTime")
        self.Mac = params.get("Mac")


class NetworkLastInfo(AbstractModel):
    """獲取當前門店最新網絡狀态數據返回結構

    """

    def __init__(self):
        """
        :param Count: 總數
        :type Count: int
        :param Infos: 網絡狀态
        :type Infos: list of NetworkAndShopInfo
        """
        self.Count = None
        self.Infos = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        if params.get("Infos") is not None:
            self.Infos = []
            for item in params.get("Infos"):
                obj = NetworkAndShopInfo()
                obj._deserialize(item)
                self.Infos.append(obj)


class PersonCoordinate(AbstractModel):
    """軌迹點坐标

    """

    def __init__(self):
        """
        :param CADX: CAD圖X坐标
        :type CADX: float
        :param CADY: CAD圖Y坐标
        :type CADY: float
        :param CapTime: 抓拍時間點
        :type CapTime: str
        :param CapPic: 抓拍圖片
        :type CapPic: str
        :param MallAreaType: 賣場區域類型
        :type MallAreaType: int
        :param PosId: 坐标編号
        :type PosId: int
        :param ShopId: 門店編号
        :type ShopId: int
        :param Event: 事件
        :type Event: str
        """
        self.CADX = None
        self.CADY = None
        self.CapTime = None
        self.CapPic = None
        self.MallAreaType = None
        self.PosId = None
        self.ShopId = None
        self.Event = None


    def _deserialize(self, params):
        self.CADX = params.get("CADX")
        self.CADY = params.get("CADY")
        self.CapTime = params.get("CapTime")
        self.CapPic = params.get("CapPic")
        self.MallAreaType = params.get("MallAreaType")
        self.PosId = params.get("PosId")
        self.ShopId = params.get("ShopId")
        self.Event = params.get("Event")


class PersonInfo(AbstractModel):
    """用戶訊息

    """

    def __init__(self):
        """
        :param PersonId: 用戶ID
        :type PersonId: int
        :param PersonPicture: 人臉圖片Base64内容，已棄用，返回預設空值
        :type PersonPicture: str
        :param Gender: 性别：0男1女
        :type Gender: int
        :param Age: 年齡
        :type Age: int
        :param PersonType: 身份類型（0表示普通顧客，1 白名單，2 表示黑名單）
        :type PersonType: int
        :param PersonPictureUrl: 人臉圖片Url，在有效期内可以訪問下載
        :type PersonPictureUrl: str
        :param PersonSubType: 身份子類型:
PersonType=0時(普通顧客)，0普通顧客
PersonType=1時(白名單)，0店員，1商場人員，2其他類型人員，3區域經理，4注冊用戶，5VIP用戶
PersonType=2時(黑名單)，0普通黑名單，1小偷)
        :type PersonSubType: int
        :param VisitTimes: 到訪次數，-1表示未知
        :type VisitTimes: int
        :param VisitDays: 到訪天數，-1表示未知
        :type VisitDays: int
        """
        self.PersonId = None
        self.PersonPicture = None
        self.Gender = None
        self.Age = None
        self.PersonType = None
        self.PersonPictureUrl = None
        self.PersonSubType = None
        self.VisitTimes = None
        self.VisitDays = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.PersonPicture = params.get("PersonPicture")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.PersonType = params.get("PersonType")
        self.PersonPictureUrl = params.get("PersonPictureUrl")
        self.PersonSubType = params.get("PersonSubType")
        self.VisitTimes = params.get("VisitTimes")
        self.VisitDays = params.get("VisitDays")


class PersonProfile(AbstractModel):
    """來訪客人基本資料

    """

    def __init__(self):
        """
        :param PersonId: 客人編碼
        :type PersonId: str
        :param Gender: 性别
        :type Gender: int
        :param Age: 年齡
        :type Age: int
        :param FirstArrivedTime: 首次到場時間
        :type FirstArrivedTime: str
        :param ArrivedCount: 來訪次數
        :type ArrivedCount: int
        :param PicUrl: 客戶圖片
        :type PicUrl: str
        :param Similarity: 置信度
        :type Similarity: float
        """
        self.PersonId = None
        self.Gender = None
        self.Age = None
        self.FirstArrivedTime = None
        self.ArrivedCount = None
        self.PicUrl = None
        self.Similarity = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.Gender = params.get("Gender")
        self.Age = params.get("Age")
        self.FirstArrivedTime = params.get("FirstArrivedTime")
        self.ArrivedCount = params.get("ArrivedCount")
        self.PicUrl = params.get("PicUrl")
        self.Similarity = params.get("Similarity")


class PersonTagInfo(AbstractModel):
    """修改顧客屬性參數

    """

    def __init__(self):
        """
        :param OldType: 顧客原類型
        :type OldType: int
        :param NewType: 顧客新類型
        :type NewType: int
        :param PersonId: 顧客face id
        :type PersonId: int
        """
        self.OldType = None
        self.NewType = None
        self.PersonId = None


    def _deserialize(self, params):
        self.OldType = params.get("OldType")
        self.NewType = params.get("NewType")
        self.PersonId = params.get("PersonId")


class PersonTracePoint(AbstractModel):
    """客戶軌迹點

    """

    def __init__(self):
        """
        :param MallAreaId: 賣場區域編碼
        :type MallAreaId: int
        :param ShopId: 門店編碼
        :type ShopId: int
        :param MallAreaType: 賣場區域類型
        :type MallAreaType: int
        :param TraceEventType: 軌迹事件
        :type TraceEventType: int
        :param TraceEventTime: 軌迹事件發生時間點
        :type TraceEventTime: str
        :param CapPic: 抓拍圖片
        :type CapPic: str
        :param ShoppingBagType: 購物袋類型
        :type ShoppingBagType: int
        :param ShoppingBagCount: 購物袋數量
        :type ShoppingBagCount: int
        """
        self.MallAreaId = None
        self.ShopId = None
        self.MallAreaType = None
        self.TraceEventType = None
        self.TraceEventTime = None
        self.CapPic = None
        self.ShoppingBagType = None
        self.ShoppingBagCount = None


    def _deserialize(self, params):
        self.MallAreaId = params.get("MallAreaId")
        self.ShopId = params.get("ShopId")
        self.MallAreaType = params.get("MallAreaType")
        self.TraceEventType = params.get("TraceEventType")
        self.TraceEventTime = params.get("TraceEventTime")
        self.CapPic = params.get("CapPic")
        self.ShoppingBagType = params.get("ShoppingBagType")
        self.ShoppingBagCount = params.get("ShoppingBagCount")


class PersonTraceRoute(AbstractModel):
    """客戶軌迹序列

    """

    def __init__(self):
        """
        :param TraceId: 軌迹編碼
        :type TraceId: str
        :param TracePointSet: 軌迹點序列
        :type TracePointSet: list of PersonTracePoint
        """
        self.TraceId = None
        self.TracePointSet = None


    def _deserialize(self, params):
        self.TraceId = params.get("TraceId")
        if params.get("TracePointSet") is not None:
            self.TracePointSet = []
            for item in params.get("TracePointSet"):
                obj = PersonTracePoint()
                obj._deserialize(item)
                self.TracePointSet.append(obj)


class PersonVisitInfo(AbstractModel):
    """用戶到訪明細

    """

    def __init__(self):
        """
        :param PersonId: 用戶ID
        :type PersonId: int
        :param VisitId: 用戶到訪ID
        :type VisitId: int
        :param InTime: 到訪時間：Unix時間戳
        :type InTime: int
        :param CapturedPicture: 抓拍到的頭像Base64内容，已棄用，返回預設空值
        :type CapturedPicture: str
        :param MaskType: 口罩類型：0不戴口罩，1戴口罩
        :type MaskType: int
        :param GlassType: 眼鏡類型：0不戴眼鏡，1普通眼鏡 , 2墨鏡
        :type GlassType: int
        :param HairType: 發型：0 短發,  1長發
        :type HairType: int
        :param CapturedPictureUrl: 抓拍到的頭像Url，在有效期内可以訪問下載
        :type CapturedPictureUrl: str
        :param SceneInfo: 抓拍頭像的場景圖訊息
        :type SceneInfo: :class:`tencentcloud.youmall.v20180228.models.SceneInfo`
        """
        self.PersonId = None
        self.VisitId = None
        self.InTime = None
        self.CapturedPicture = None
        self.MaskType = None
        self.GlassType = None
        self.HairType = None
        self.CapturedPictureUrl = None
        self.SceneInfo = None


    def _deserialize(self, params):
        self.PersonId = params.get("PersonId")
        self.VisitId = params.get("VisitId")
        self.InTime = params.get("InTime")
        self.CapturedPicture = params.get("CapturedPicture")
        self.MaskType = params.get("MaskType")
        self.GlassType = params.get("GlassType")
        self.HairType = params.get("HairType")
        self.CapturedPictureUrl = params.get("CapturedPictureUrl")
        if params.get("SceneInfo") is not None:
            self.SceneInfo = SceneInfo()
            self.SceneInfo._deserialize(params.get("SceneInfo"))


class RegisterCallbackRequest(AbstractModel):
    """RegisterCallback請求參數結構體

    """

    def __init__(self):
        """
        :param CompanyId: 集團id，通過"指定身份标識獲取客戶門店清單"介面獲取
        :type CompanyId: str
        :param BackUrl: 通知回調網址，完整url，範例（http://youmall.tencentcloudapi.com/）
        :type BackUrl: str
        :param Time: 請求時間戳
        :type Time: int
        :param NeedFacePic: 是否需要顧客圖片，1-需要圖片，其它-不需要圖片
        :type NeedFacePic: int
        """
        self.CompanyId = None
        self.BackUrl = None
        self.Time = None
        self.NeedFacePic = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.BackUrl = params.get("BackUrl")
        self.Time = params.get("Time")
        self.NeedFacePic = params.get("NeedFacePic")


class RegisterCallbackResponse(AbstractModel):
    """RegisterCallback返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SceneInfo(AbstractModel):
    """場景圖訊息

    """

    def __init__(self):
        """
        :param ScenePictureURL: 場景圖
        :type ScenePictureURL: str
        :param HeadX: 抓拍頭像左上角X坐标在場景圖中的像素點位置
        :type HeadX: int
        :param HeadY: 抓拍頭像左上角Y坐标在場景圖中的像素點位置
        :type HeadY: int
        :param HeadWidth: 抓拍頭像在場景圖中占有的像素寬度
        :type HeadWidth: int
        :param HeadHeight: 抓拍頭像在場景圖中占有的像素高度
        :type HeadHeight: int
        """
        self.ScenePictureURL = None
        self.HeadX = None
        self.HeadY = None
        self.HeadWidth = None
        self.HeadHeight = None


    def _deserialize(self, params):
        self.ScenePictureURL = params.get("ScenePictureURL")
        self.HeadX = params.get("HeadX")
        self.HeadY = params.get("HeadY")
        self.HeadWidth = params.get("HeadWidth")
        self.HeadHeight = params.get("HeadHeight")


class ShopDayTrafficInfo(AbstractModel):
    """門店客流量清單訊息

    """

    def __init__(self):
        """
        :param Date: 日期
        :type Date: str
        :param DayTrafficTotalCount: 客流量
        :type DayTrafficTotalCount: int
        :param GenderAgeTrafficDetailSet: 性别年齡分組下的客流訊息
        :type GenderAgeTrafficDetailSet: list of GenderAgeTrafficDetail
        """
        self.Date = None
        self.DayTrafficTotalCount = None
        self.GenderAgeTrafficDetailSet = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.DayTrafficTotalCount = params.get("DayTrafficTotalCount")
        if params.get("GenderAgeTrafficDetailSet") is not None:
            self.GenderAgeTrafficDetailSet = []
            for item in params.get("GenderAgeTrafficDetailSet"):
                obj = GenderAgeTrafficDetail()
                obj._deserialize(item)
                self.GenderAgeTrafficDetailSet.append(obj)


class ShopHourTrafficInfo(AbstractModel):
    """分時客流量訊息

    """

    def __init__(self):
        """
        :param Date: 日期，格式yyyy-MM-dd
        :type Date: str
        :param HourTrafficInfoDetailSet: 分時客流詳細訊息
        :type HourTrafficInfoDetailSet: list of HourTrafficInfoDetail
        """
        self.Date = None
        self.HourTrafficInfoDetailSet = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        if params.get("HourTrafficInfoDetailSet") is not None:
            self.HourTrafficInfoDetailSet = []
            for item in params.get("HourTrafficInfoDetailSet"):
                obj = HourTrafficInfoDetail()
                obj._deserialize(item)
                self.HourTrafficInfoDetailSet.append(obj)


class ShopInfo(AbstractModel):
    """客戶所屬的門店訊息

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID
        :type CompanyId: str
        :param ShopId: 門店ID
        :type ShopId: int
        :param ShopName: 門店名稱
        :type ShopName: str
        :param ShopCode: 客戶門店編碼
        :type ShopCode: str
        :param Province: 省
        :type Province: str
        :param City: 市
        :type City: str
        :param CompanyName: 公司名稱
        :type CompanyName: str
        """
        self.CompanyId = None
        self.ShopId = None
        self.ShopName = None
        self.ShopCode = None
        self.Province = None
        self.City = None
        self.CompanyName = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.ShopId = params.get("ShopId")
        self.ShopName = params.get("ShopName")
        self.ShopCode = params.get("ShopCode")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.CompanyName = params.get("CompanyName")


class TrajectorySunData(AbstractModel):
    """軌迹動線訊息子結構

    """

    def __init__(self):
        """
        :param Zones: 區域動線，形如 x-x-x-x-x，其中 x 爲區域 ID
        :type Zones: str
        :param Count: 該動線出現次數
        :type Count: int
        :param AvgStayTime: 該動線平均停留時間（秒）
        :type AvgStayTime: int
        """
        self.Zones = None
        self.Count = None
        self.AvgStayTime = None


    def _deserialize(self, params):
        self.Zones = params.get("Zones")
        self.Count = params.get("Count")
        self.AvgStayTime = params.get("AvgStayTime")


class ZoneAgeGroupAvrStayTime(AbstractModel):
    """區域性别平均停留時間子結構

    """

    def __init__(self):
        """
        :param MaleAvrStayTime: 男性平均停留時間
        :type MaleAvrStayTime: float
        :param FemaleAvrStayTime: 女性平均停留時間
        :type FemaleAvrStayTime: float
        """
        self.MaleAvrStayTime = None
        self.FemaleAvrStayTime = None


    def _deserialize(self, params):
        self.MaleAvrStayTime = params.get("MaleAvrStayTime")
        self.FemaleAvrStayTime = params.get("FemaleAvrStayTime")


class ZoneDayFlow(AbstractModel):
    """每日客流統計子結構

    """

    def __init__(self):
        """
        :param Day: 日期，如 2018-08-6
        :type Day: str
        :param FlowCount: 客流量
        :type FlowCount: int
        """
        self.Day = None
        self.FlowCount = None


    def _deserialize(self, params):
        self.Day = params.get("Day")
        self.FlowCount = params.get("FlowCount")


class ZoneFlowAndAvrStayTime(AbstractModel):
    """客流停留統計子結構

    """

    def __init__(self):
        """
        :param ZoneId: 區域id
        :type ZoneId: int
        :param ZoneName: 區域名稱
        :type ZoneName: str
        :param FlowCount: 人流量
        :type FlowCount: int
        :param AvrStayTime: 平均停留時長
        :type AvrStayTime: int
        """
        self.ZoneId = None
        self.ZoneName = None
        self.FlowCount = None
        self.AvrStayTime = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.FlowCount = params.get("FlowCount")
        self.AvrStayTime = params.get("AvrStayTime")


class ZoneHourFlow(AbstractModel):
    """客流統計分時數據子結構

    """

    def __init__(self):
        """
        :param Hour: 分時 0~23
        :type Hour: int
        :param FlowCount: 客流量
        :type FlowCount: int
        """
        self.Hour = None
        self.FlowCount = None


    def _deserialize(self, params):
        self.Hour = params.get("Hour")
        self.FlowCount = params.get("FlowCount")


class ZoneTrafficInfo(AbstractModel):
    """門店區域客流訊息

    """

    def __init__(self):
        """
        :param Date: 日期
        :type Date: str
        :param ZoneTrafficInfoDetailSet: 門店區域客流詳細訊息
        :type ZoneTrafficInfoDetailSet: list of ZoneTrafficInfoDetail
        """
        self.Date = None
        self.ZoneTrafficInfoDetailSet = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        if params.get("ZoneTrafficInfoDetailSet") is not None:
            self.ZoneTrafficInfoDetailSet = []
            for item in params.get("ZoneTrafficInfoDetailSet"):
                obj = ZoneTrafficInfoDetail()
                obj._deserialize(item)
                self.ZoneTrafficInfoDetailSet.append(obj)


class ZoneTrafficInfoDetail(AbstractModel):
    """門店區域客流詳細訊息

    """

    def __init__(self):
        """
        :param ZoneId: 區域ID
        :type ZoneId: int
        :param ZoneName: 區域名稱
        :type ZoneName: str
        :param TrafficTotalCount: 客流量
        :type TrafficTotalCount: int
        :param AvgStayTime: 平均停留時間
        :type AvgStayTime: int
        """
        self.ZoneId = None
        self.ZoneName = None
        self.TrafficTotalCount = None
        self.AvgStayTime = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.TrafficTotalCount = params.get("TrafficTotalCount")
        self.AvgStayTime = params.get("AvgStayTime")