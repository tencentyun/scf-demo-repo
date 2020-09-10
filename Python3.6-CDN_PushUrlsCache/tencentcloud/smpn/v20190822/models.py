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


class CHPRequest(AbstractModel):
    """終端騷擾保護請求内容

    """

    def __init__(self):
        """
        :param PhoneNumber: 電話号碼
        :type PhoneNumber: str
        """
        self.PhoneNumber = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")


class CHPResponse(AbstractModel):
    """終端騷擾保護

    """

    def __init__(self):
        """
        :param TagType: 标記類型
 0: 無标記
 50:騷擾電話
 51:房産中介
 52:保險理财
 53:廣告推銷
 54:詐騙電話
 55:快遞電話
 56:出租車專車
        :type TagType: int
        :param TagCount: 标記次數
        :type TagCount: int
        """
        self.TagType = None
        self.TagCount = None


    def _deserialize(self, params):
        self.TagType = params.get("TagType")
        self.TagCount = params.get("TagCount")


class CreateSmpnEpaRequest(AbstractModel):
    """CreateSmpnEpa請求參數結構體

    """

    def __init__(self):
        """
        :param RequestData: 企業号碼認證請求内容
        :type RequestData: :class:`taifucloudcloud.smpn.v20190822.models.EPARequest`
        :param ResourceId: 用于計費的資源ID
        :type ResourceId: str
        """
        self.RequestData = None
        self.ResourceId = None


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self.RequestData = EPARequest()
            self.RequestData._deserialize(params.get("RequestData"))
        self.ResourceId = params.get("ResourceId")


class CreateSmpnEpaResponse(AbstractModel):
    """CreateSmpnEpa返回參數結構體

    """

    def __init__(self):
        """
        :param ResponseData: 業号碼認證回應内容
        :type ResponseData: :class:`taifucloudcloud.smpn.v20190822.models.EPAResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = EPAResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")


class DescribeSmpnChpRequest(AbstractModel):
    """DescribeSmpnChp請求參數結構體

    """

    def __init__(self):
        """
        :param ResourceId: 客戶用于計費的資源Id
        :type ResourceId: str
        :param RequestData: 終端騷擾保護請求
        :type RequestData: :class:`taifucloudcloud.smpn.v20190822.models.CHPRequest`
        """
        self.ResourceId = None
        self.RequestData = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        if params.get("RequestData") is not None:
            self.RequestData = CHPRequest()
            self.RequestData._deserialize(params.get("RequestData"))


class DescribeSmpnChpResponse(AbstractModel):
    """DescribeSmpnChp返回參數結構體

    """

    def __init__(self):
        """
        :param ResponseData: 終端騷擾保護回應
        :type ResponseData: :class:`taifucloudcloud.smpn.v20190822.models.CHPResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = CHPResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")


class DescribeSmpnFnrRequest(AbstractModel):
    """DescribeSmpnFnr請求參數結構體

    """

    def __init__(self):
        """
        :param RequestData: 虛假号碼識别請求内容
        :type RequestData: :class:`taifucloudcloud.smpn.v20190822.models.FNRRequest`
        :param ResourceId: 用于計費的資源ID
        :type ResourceId: str
        """
        self.RequestData = None
        self.ResourceId = None


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self.RequestData = FNRRequest()
            self.RequestData._deserialize(params.get("RequestData"))
        self.ResourceId = params.get("ResourceId")


class DescribeSmpnFnrResponse(AbstractModel):
    """DescribeSmpnFnr返回參數結構體

    """

    def __init__(self):
        """
        :param ResponseData: 虛假号碼識别回應内容
        :type ResponseData: :class:`taifucloudcloud.smpn.v20190822.models.FNRResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = FNRResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")


class DescribeSmpnMhmRequest(AbstractModel):
    """DescribeSmpnMhm請求參數結構體

    """

    def __init__(self):
        """
        :param RequestData: 号碼營銷監控請求内容
        :type RequestData: :class:`taifucloudcloud.smpn.v20190822.models.MHMRequest`
        :param ResourceId: 用于計費的資源ID
        :type ResourceId: str
        """
        self.RequestData = None
        self.ResourceId = None


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self.RequestData = MHMRequest()
            self.RequestData._deserialize(params.get("RequestData"))
        self.ResourceId = params.get("ResourceId")


class DescribeSmpnMhmResponse(AbstractModel):
    """DescribeSmpnMhm返回參數結構體

    """

    def __init__(self):
        """
        :param ResponseData: 号碼營銷監控回應内容
        :type ResponseData: :class:`taifucloudcloud.smpn.v20190822.models.MHMResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = MHMResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")


class DescribeSmpnMrlRequest(AbstractModel):
    """DescribeSmpnMrl請求參數結構體

    """

    def __init__(self):
        """
        :param RequestData: 惡意标記等級請求内容
        :type RequestData: :class:`taifucloudcloud.smpn.v20190822.models.MRLRequest`
        :param ResourceId: 用于計費的資源ID
        :type ResourceId: str
        """
        self.RequestData = None
        self.ResourceId = None


    def _deserialize(self, params):
        if params.get("RequestData") is not None:
            self.RequestData = MRLRequest()
            self.RequestData._deserialize(params.get("RequestData"))
        self.ResourceId = params.get("ResourceId")


class DescribeSmpnMrlResponse(AbstractModel):
    """DescribeSmpnMrl返回參數結構體

    """

    def __init__(self):
        """
        :param ResponseData: 惡意标記等級回應内容
        :type ResponseData: :class:`taifucloudcloud.smpn.v20190822.models.MRLResponse`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResponseData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResponseData") is not None:
            self.ResponseData = MRLResponse()
            self.ResponseData._deserialize(params.get("ResponseData"))
        self.RequestId = params.get("RequestId")


class EPARequest(AbstractModel):
    """企業号碼認證請求

    """

    def __init__(self):
        """
        :param PhoneNumber: 電話号碼
        :type PhoneNumber: str
        :param Name: 黃頁名稱
        :type Name: str
        """
        self.PhoneNumber = None
        self.Name = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")
        self.Name = params.get("Name")


class EPAResponse(AbstractModel):
    """企業号碼認證回應

    """

    def __init__(self):
        """
        :param RetCode: 0成功 其他失敗
        :type RetCode: int
        """
        self.RetCode = None


    def _deserialize(self, params):
        self.RetCode = params.get("RetCode")


class FNRRequest(AbstractModel):
    """虛假号碼識别請求

    """

    def __init__(self):
        """
        :param PhoneNumber: 電話号碼
        :type PhoneNumber: str
        """
        self.PhoneNumber = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")


class FNRResponse(AbstractModel):
    """虛假号碼識别回應

    """

    def __init__(self):
        """
        :param Status: 虛假号碼描述
        :type Status: int
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")


class MHMRequest(AbstractModel):
    """号碼營銷監控請求

    """

    def __init__(self):
        """
        :param PhoneNumber: 電話号碼
        :type PhoneNumber: str
        """
        self.PhoneNumber = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")


class MHMResponse(AbstractModel):
    """号碼營銷監控回應

    """

    def __init__(self):
        """
        :param TagType: 标記類型
 0: 無标記
 50:騷擾電話
 51:房産中介
 52:保險理财
 53:廣告推銷
 54:詐騙電話
 55:快遞電話
 56:出租車專車
        :type TagType: int
        :param TagCount: 标記次數
        :type TagCount: int
        """
        self.TagType = None
        self.TagCount = None


    def _deserialize(self, params):
        self.TagType = params.get("TagType")
        self.TagCount = params.get("TagCount")


class MRLRequest(AbstractModel):
    """号碼惡意标記等級請求

    """

    def __init__(self):
        """
        :param PhoneNumber: 電話号碼
        :type PhoneNumber: str
        """
        self.PhoneNumber = None


    def _deserialize(self, params):
        self.PhoneNumber = params.get("PhoneNumber")


class MRLResponse(AbstractModel):
    """号碼惡意标記等級

    """

    def __init__(self):
        """
        :param DisturbLevel: 騷擾電話惡意标記等級
        :type DisturbLevel: int
        :param HouseAgentLevel: 房産中介惡意标記等級
        :type HouseAgentLevel: int
        :param InsuranceLevel: 保險理财惡意标記等級
        :type InsuranceLevel: int
        :param SalesLevel: 廣告推銷惡意标記等級
        :type SalesLevel: int
        :param CheatLevel: 詐騙電話惡意标記等級
        :type CheatLevel: int
        """
        self.DisturbLevel = None
        self.HouseAgentLevel = None
        self.InsuranceLevel = None
        self.SalesLevel = None
        self.CheatLevel = None


    def _deserialize(self, params):
        self.DisturbLevel = params.get("DisturbLevel")
        self.HouseAgentLevel = params.get("HouseAgentLevel")
        self.InsuranceLevel = params.get("InsuranceLevel")
        self.SalesLevel = params.get("SalesLevel")
        self.CheatLevel = params.get("CheatLevel")