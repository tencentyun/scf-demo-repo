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


class CheckDomainRequest(AbstractModel):
    """CheckDomain請求參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 所查詢域名名稱
        :type DomainName: str
        :param Period: 年限
        :type Period: str
        """
        self.DomainName = None
        self.Period = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Period = params.get("Period")


class CheckDomainResponse(AbstractModel):
    """CheckDomain返回參數結構體

    """

    def __init__(self):
        """
        :param DomainName: 所查詢域名名稱
        :type DomainName: str
        :param Available: 是否能夠注冊
        :type Available: bool
        :param Reason: 不能注冊原因
        :type Reason: str
        :param Premium: 是否是溢價詞
        :type Premium: bool
        :param Price: 域名價格
        :type Price: int
        :param BlackWord: 是否是敏感詞
        :type BlackWord: bool
        :param Describe: 溢價詞描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Describe: str
        :param FeeRenew: 溢價詞的續約價格
注意：此欄位可能返回 null，表示取不到有效值。
        :type FeeRenew: int
        :param RealPrice: 域名真實價格
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealPrice: int
        :param FeeTransfer: 溢價詞的轉入價格
注意：此欄位可能返回 null，表示取不到有效值。
        :type FeeTransfer: int
        :param FeeRestore: 溢價詞的贖回價格
        :type FeeRestore: int
        :param Period: 檢測年限
        :type Period: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DomainName = None
        self.Available = None
        self.Reason = None
        self.Premium = None
        self.Price = None
        self.BlackWord = None
        self.Describe = None
        self.FeeRenew = None
        self.RealPrice = None
        self.FeeTransfer = None
        self.FeeRestore = None
        self.Period = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Available = params.get("Available")
        self.Reason = params.get("Reason")
        self.Premium = params.get("Premium")
        self.Price = params.get("Price")
        self.BlackWord = params.get("BlackWord")
        self.Describe = params.get("Describe")
        self.FeeRenew = params.get("FeeRenew")
        self.RealPrice = params.get("RealPrice")
        self.FeeTransfer = params.get("FeeTransfer")
        self.FeeRestore = params.get("FeeRestore")
        self.Period = params.get("Period")
        self.RequestId = params.get("RequestId")


class DescribeDomainPriceListRequest(AbstractModel):
    """DescribeDomainPriceList請求參數結構體

    """

    def __init__(self):
        """
        :param TldList: 查詢價格的後綴清單。預設則爲全部後綴
        :type TldList: list of str
        :param Year: 查詢購買的年份，預設會列出所有年份的價格
        :type Year: list of int
        :param Operation: 域名的購買類型：new  新購，renew 續約，redem 贖回，tran 轉入
        :type Operation: list of str
        """
        self.TldList = None
        self.Year = None
        self.Operation = None


    def _deserialize(self, params):
        self.TldList = params.get("TldList")
        self.Year = params.get("Year")
        self.Operation = params.get("Operation")


class DescribeDomainPriceListResponse(AbstractModel):
    """DescribeDomainPriceList返回參數結構體

    """

    def __init__(self):
        """
        :param PriceList: 域名價格清單
        :type PriceList: list of PriceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PriceList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PriceList") is not None:
            self.PriceList = []
            for item in params.get("PriceList"):
                obj = PriceInfo()
                obj._deserialize(item)
                self.PriceList.append(obj)
        self.RequestId = params.get("RequestId")


class PriceInfo(AbstractModel):
    """域名價格訊息

    """

    def __init__(self):
        """
        :param Tld: 域名後綴，例如.com
        :type Tld: str
        :param Year: 購買年限，範圍[1-10]
        :type Year: int
        :param Price: 域名原價
        :type Price: int
        :param RealPrice: 域名現價
        :type RealPrice: int
        :param Operation: 商品的購買類型，新購，續約，贖回，轉入，續約并轉入
        :type Operation: str
        """
        self.Tld = None
        self.Year = None
        self.Price = None
        self.RealPrice = None
        self.Operation = None


    def _deserialize(self, params):
        self.Tld = params.get("Tld")
        self.Year = params.get("Year")
        self.Price = params.get("Price")
        self.RealPrice = params.get("RealPrice")
        self.Operation = params.get("Operation")