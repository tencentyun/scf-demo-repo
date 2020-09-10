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


class DeleteCertRequest(AbstractModel):
    """DeleteCert請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 證書 ID，即通過 GetList 拿到的證書清單的 ID 欄位。
        :type Id: str
        :param ModuleType: 模組名稱，應填 ssl。
        :type ModuleType: str
        """
        self.Id = None
        self.ModuleType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.ModuleType = params.get("ModuleType")


class DeleteCertResponse(AbstractModel):
    """DeleteCert返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCertListRequest(AbstractModel):
    """DescribeCertList請求參數結構體

    """

    def __init__(self):
        """
        :param ModuleType: 模組名稱，應填 ssl。
        :type ModuleType: str
        :param Offset: 頁數，預設第一頁。
        :type Offset: int
        :param Limit: 每頁條數，預設每頁20條。
        :type Limit: int
        :param SearchKey: 搜索關鍵字。
        :type SearchKey: str
        :param CertType: 證書類型（目前支援:CA=用戶端證書,SVR=服務器證書）。
        :type CertType: str
        :param Id: 證書ID。
        :type Id: str
        :param WithCert: 是否同時獲驗證書内容。
        :type WithCert: str
        :param AltDomain: 如傳，則只返回可以給該域名使用的證書。
        :type AltDomain: str
        """
        self.ModuleType = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.CertType = None
        self.Id = None
        self.WithCert = None
        self.AltDomain = None


    def _deserialize(self, params):
        self.ModuleType = params.get("ModuleType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.CertType = params.get("CertType")
        self.Id = params.get("Id")
        self.WithCert = params.get("WithCert")
        self.AltDomain = params.get("AltDomain")


class DescribeCertListResponse(AbstractModel):
    """DescribeCertList返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總數量。
        :type TotalCount: int
        :param CertificateSet: 清單。
        :type CertificateSet: list of SSLCertificate
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CertificateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CertificateSet") is not None:
            self.CertificateSet = []
            for item in params.get("CertificateSet"):
                obj = SSLCertificate()
                obj._deserialize(item)
                self.CertificateSet.append(obj)
        self.RequestId = params.get("RequestId")


class SSLCertificate(AbstractModel):
    """獲驗證書清單（SSLCertificate）返回參數鍵爲 CertificateSet 的内容。

    """

    def __init__(self):
        """
        :param OwnerUin: 所屬帳戶
注意：此欄位可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param ProjectId: 項目ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param From: 證書來源：trustasia = 亞洲誠信， upload = 用戶上傳
注意：此欄位可能返回 null，表示取不到有效值。
        :type From: str
        :param Type: 證書類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: str
        :param CertType: 證書類型（目前支援：CA = 用戶端證書，SVR = 服務器證書）
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertType: str
        :param ProductZhName: 證書辦法者名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param Domain: 主域名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Alias: 别名
注意：此欄位可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Status: 狀态值 0：審核中，1：已通過，2：審核失敗，3：已過期，4：已添加雲解析記錄，5：OV/EV 證書，待提交資料，6：訂單取消中，7：已取消，8：已提交資料， 待上傳确認函
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        :param VulnerabilityStatus: 漏洞掃描狀态：INACTIVE = 未開啓，ACTIVE = 已開啓
注意：此欄位可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param StatusMsg: 狀态訊息
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param VerifyType: 驗證類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param CertBeginTime: 證書生效時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param CertEndTime: 證書過期時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ValidityPeriod: 證書過期時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param InsertTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param ProjectInfo: 項目訊息，ProjectId：項目ID，OwnerUin：項目所屬的 uin（預設項目爲0），Name：項目名稱，CreatorUin：創建項目的 uin，CreateTime：項目創建時間，Info：項目說明
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectInfo: :class:`taifucloudcloud.wss.v20180426.models.SSLProjectInfo`
        :param Id: 證書ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type Id: str
        :param SubjectAltName: 證書包含的多個域名（包含主域名）
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param TypeName: 證書類型名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type TypeName: str
        :param StatusName: 狀态名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param IsVip: 是否爲 VIP 客戶
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param IsDv: 是否我 DV 版證書
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param IsWildcard: 是否爲泛域名證書
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param IsVulnerability: 是否啓用了漏洞掃描功能
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param Cert: 證書
注意：此欄位可能返回 null，表示取不到有效值。
        :type Cert: str
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.Type = None
        self.CertType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.VulnerabilityStatus = None
        self.StatusMsg = None
        self.VerifyType = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.ProjectInfo = None
        self.Id = None
        self.SubjectAltName = None
        self.TypeName = None
        self.StatusName = None
        self.IsVip = None
        self.IsDv = None
        self.IsWildcard = None
        self.IsVulnerability = None
        self.Cert = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.Type = params.get("Type")
        self.CertType = params.get("CertType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        if params.get("ProjectInfo") is not None:
            self.ProjectInfo = SSLProjectInfo()
            self.ProjectInfo._deserialize(params.get("ProjectInfo"))
        self.Id = params.get("Id")
        self.SubjectAltName = params.get("SubjectAltName")
        self.TypeName = params.get("TypeName")
        self.StatusName = params.get("StatusName")
        self.IsVip = params.get("IsVip")
        self.IsDv = params.get("IsDv")
        self.IsWildcard = params.get("IsWildcard")
        self.IsVulnerability = params.get("IsVulnerability")
        self.Cert = params.get("Cert")


class SSLProjectInfo(AbstractModel):
    """獲驗證書清單介面（SSLProjectInfo）出參鍵爲CertificateSet下的元素ProjectIno詳情

    """

    def __init__(self):
        """
        :param ProjectId: 項目ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param OwnerUin: 項目所屬的 uin（預設項目爲0）
注意：此欄位可能返回 null，表示取不到有效值。
        :type OwnerUin: int
        :param Name: 項目名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param CreatorUin: 創建項目的 uin
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreatorUin: int
        :param CreateTime: 項目創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Info: 項目說明
注意：此欄位可能返回 null，表示取不到有效值。
        :type Info: str
        """
        self.ProjectId = None
        self.OwnerUin = None
        self.Name = None
        self.CreatorUin = None
        self.CreateTime = None
        self.Info = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.OwnerUin = params.get("OwnerUin")
        self.Name = params.get("Name")
        self.CreatorUin = params.get("CreatorUin")
        self.CreateTime = params.get("CreateTime")
        self.Info = params.get("Info")


class UploadCertRequest(AbstractModel):
    """UploadCert請求參數結構體

    """

    def __init__(self):
        """
        :param Cert: 證書内容。
        :type Cert: str
        :param CertType: 證書類型（目前支援：CA 爲用戶端證書，SVR 爲服務器證書）。
        :type CertType: str
        :param ProjectId: 項目ID，詳見用戶指南的 [項目與标簽](https://cloud.taifucloud.com/document/product/598/32738)。
        :type ProjectId: str
        :param ModuleType: 模組名稱，應填 ssl。
        :type ModuleType: str
        :param Key: 證書私鑰，certType=SVR 時必填。
        :type Key: str
        :param Alias: 證書備注。
        :type Alias: str
        """
        self.Cert = None
        self.CertType = None
        self.ProjectId = None
        self.ModuleType = None
        self.Key = None
        self.Alias = None


    def _deserialize(self, params):
        self.Cert = params.get("Cert")
        self.CertType = params.get("CertType")
        self.ProjectId = params.get("ProjectId")
        self.ModuleType = params.get("ModuleType")
        self.Key = params.get("Key")
        self.Alias = params.get("Alias")


class UploadCertResponse(AbstractModel):
    """UploadCert返回參數結構體

    """

    def __init__(self):
        """
        :param Id: 證書ID。
        :type Id: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")