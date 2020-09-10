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


class ApplyCertificateRequest(AbstractModel):
    """ApplyCertificate請求參數結構體

    """

    def __init__(self):
        """
        :param DvAuthMethod: 驗證方式：DNS_AUTO = 自動DNS驗證，DNS = 手動DNS驗證，FILE = 文件驗證。
        :type DvAuthMethod: str
        :param DomainName: 域名。
        :type DomainName: str
        :param ProjectId: 項目 ID。
        :type ProjectId: int
        :param PackageType: 證書類型，目前僅支援類型2。2 = TrustAsia TLS RSA CA。
        :type PackageType: str
        :param ContactEmail: 電子信箱。
        :type ContactEmail: str
        :param ContactPhone: 手機。
        :type ContactPhone: str
        :param ValidityPeriod: 有效期，預設12個月，目前僅支援12個月。
        :type ValidityPeriod: str
        :param CsrEncryptAlgo: 加密算法，僅支援 RSA。
        :type CsrEncryptAlgo: str
        :param CsrKeyParameter: 金鑰對參數，僅支援2048。
        :type CsrKeyParameter: str
        :param CsrKeyPassword: CSR 的加密密碼。
        :type CsrKeyPassword: str
        :param Alias: 備注名稱。
        :type Alias: str
        :param OldCertificateId: 原證書 ID，用于重新申請。
        :type OldCertificateId: str
        """
        self.DvAuthMethod = None
        self.DomainName = None
        self.ProjectId = None
        self.PackageType = None
        self.ContactEmail = None
        self.ContactPhone = None
        self.ValidityPeriod = None
        self.CsrEncryptAlgo = None
        self.CsrKeyParameter = None
        self.CsrKeyPassword = None
        self.Alias = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.DvAuthMethod = params.get("DvAuthMethod")
        self.DomainName = params.get("DomainName")
        self.ProjectId = params.get("ProjectId")
        self.PackageType = params.get("PackageType")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactPhone = params.get("ContactPhone")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.CsrEncryptAlgo = params.get("CsrEncryptAlgo")
        self.CsrKeyParameter = params.get("CsrKeyParameter")
        self.CsrKeyPassword = params.get("CsrKeyPassword")
        self.Alias = params.get("Alias")
        self.OldCertificateId = params.get("OldCertificateId")


class ApplyCertificateResponse(AbstractModel):
    """ApplyCertificate返回參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CancelCertificateOrderRequest(AbstractModel):
    """CancelCertificateOrder請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class CancelCertificateOrderResponse(AbstractModel):
    """CancelCertificateOrder返回參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 取消訂單成功的證書 ID。
        :type CertificateId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CertificateExtra(AbstractModel):
    """獲驗證書清單（DescribeCertificates）返回參數鍵爲 Certificates 數組下，key爲CertificateExtra 的内容。

    """

    def __init__(self):
        """
        :param DomainNumber: 證書可配置域名數量。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DomainNumber: str
        :param OriginCertificateId: 原始證書 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OriginCertificateId: str
        :param ReplacedBy: 重頒發證書原始 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReplacedBy: str
        :param ReplacedFor: 重頒發證書新 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ReplacedFor: str
        :param RenewOrder: 新訂單證書 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RenewOrder: str
        """
        self.DomainNumber = None
        self.OriginCertificateId = None
        self.ReplacedBy = None
        self.ReplacedFor = None
        self.RenewOrder = None


    def _deserialize(self, params):
        self.DomainNumber = params.get("DomainNumber")
        self.OriginCertificateId = params.get("OriginCertificateId")
        self.ReplacedBy = params.get("ReplacedBy")
        self.ReplacedFor = params.get("ReplacedFor")
        self.RenewOrder = params.get("RenewOrder")


class Certificates(AbstractModel):
    """獲驗證書清單（DescribeCertificates）返回參數鍵爲 Certificates 的内容。

    """

    def __init__(self):
        """
        :param OwnerUin: 用戶 UIN。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param ProjectId: 項目 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param From: 證書來源。
注意：此欄位可能返回 null，表示取不到有效值。
        :type From: str
        :param PackageType: 證書套餐類型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增強型企業版（EV Pro）， 4 = SecureSite 增強型（EV）， 5 = SecureSite 企業型專業版（OV Pro）， 6 = SecureSite 企業型（OV）， 7 = SecureSite 企業型（OV）通配符， 8 = Geotrust 增強型（EV）， 9 = Geotrust 企業型（OV）， 10 = Geotrust 企業型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 證書， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企業型通配符（OV）SSL 證書（D3）， 14 = TrustAsia 企業型（OV）SSL 證書（D3）， 15 = TrustAsia 企業型多域名 （OV）SSL 證書（D3）， 16 = TrustAsia 增強型 （EV）SSL 證書（D3）， 17 = TrustAsia 增強型多域名（EV）SSL 證書（D3）， 18 = GlobalSign 企業型（OV）SSL 證書， 19 = GlobalSign 企業型通配符 （OV）SSL 證書， 20 = GlobalSign 增強型 （EV）SSL 證書， 21 = TrustAsia 企業型通配符多域名（OV）SSL 證書（D3）， 22 = GlobalSign 企業型多域名（OV）SSL 證書， 23 = GlobalSign 企業型通配符多域名（OV）SSL 證書， 24 = GlobalSign 增強型多域名（EV）SSL 證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param CertificateType: 證書類型：CA = 用戶端證書，SVR = 服務器證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param ProductZhName: 頒發者。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param Domain: 主域名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Alias: 備注名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Status: 狀态值 0：審核中，1：已通過，2：審核失敗，3：已過期，4：已添加雲解析記錄，5：OV/EV 證書，待提交資料，6：訂單取消中，7：已取消，8：已提交資料， 待上傳确認函。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        :param CertificateExtra: 證書擴展訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`taifucloudcloud.ssl.v20191205.models.CertificateExtra`
        :param VulnerabilityStatus: 漏洞掃描狀态：INACTIVE = 未開啓，ACTIVE = 已開啓
注意：此欄位可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param StatusMsg: 狀态訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param VerifyType: 驗證類型：DNS_AUTO = 自動DNS驗證，DNS = 手動DNS驗證，FILE = 文件驗證，EMAIL = 郵件驗證。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param CertBeginTime: 證書生效時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param CertEndTime: 證書過期時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ValidityPeriod: 證書有效期，單位（月）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param InsertTime: 創建時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param CertificateId: 證書 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param SubjectAltName: 證書包含的多個域名（包含主域名）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param PackageTypeName: 證書類型名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PackageTypeName: str
        :param StatusName: 狀态名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param IsVip: 是否爲 VIP 客戶。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param IsDv: 是否爲 DV 版證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param IsWildcard: 是否爲泛域名證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param IsVulnerability: 是否啓用了漏洞掃描功能。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param RenewAble: 是否可重頒發證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param ProjectInfo: 項目訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectInfo: :class:`taifucloudcloud.ssl.v20191205.models.ProjectInfo`
        :param BoundResource: 關聯的雲資源，暫不可用
注意：此欄位可能返回 null，表示取不到有效值。
        :type BoundResource: list of str
        :param Deployable: 是否可部署。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Deployable: bool
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.PackageType = None
        self.CertificateType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.CertificateExtra = None
        self.VulnerabilityStatus = None
        self.StatusMsg = None
        self.VerifyType = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.CertificateId = None
        self.SubjectAltName = None
        self.PackageTypeName = None
        self.StatusName = None
        self.IsVip = None
        self.IsDv = None
        self.IsWildcard = None
        self.IsVulnerability = None
        self.RenewAble = None
        self.ProjectInfo = None
        self.BoundResource = None
        self.Deployable = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.PackageType = params.get("PackageType")
        self.CertificateType = params.get("CertificateType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.CertificateId = params.get("CertificateId")
        self.SubjectAltName = params.get("SubjectAltName")
        self.PackageTypeName = params.get("PackageTypeName")
        self.StatusName = params.get("StatusName")
        self.IsVip = params.get("IsVip")
        self.IsDv = params.get("IsDv")
        self.IsWildcard = params.get("IsWildcard")
        self.IsVulnerability = params.get("IsVulnerability")
        self.RenewAble = params.get("RenewAble")
        if params.get("ProjectInfo") is not None:
            self.ProjectInfo = ProjectInfo()
            self.ProjectInfo._deserialize(params.get("ProjectInfo"))
        self.BoundResource = params.get("BoundResource")
        self.Deployable = params.get("Deployable")


class CommitCertificateInformationRequest(AbstractModel):
    """CommitCertificateInformation請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class CommitCertificateInformationResponse(AbstractModel):
    """CommitCertificateInformation返回參數結構體

    """

    def __init__(self):
        """
        :param OrderId: 亞信訂單号。
        :type OrderId: str
        :param Status: 證書狀态：0 = 審核中，1 = 已通過，2 = 審核失敗，3 = 已過期，4 = 已添加DNS記錄，5 = 企業證書，待提交，6 = 訂單取消中，7 = 已取消，8 = 已提交資料， 待上傳确認函，9 = 證書吊銷中，10 = 已吊銷，11 = 重頒發中，12 = 待上傳吊銷确認函。
        :type Status: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OrderId = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate返回參數結構體

    """

    def __init__(self):
        """
        :param DeleteResult: 删除結果。
        :type DeleteResult: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeleteResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeleteResult = params.get("DeleteResult")
        self.RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail返回參數結構體

    """

    def __init__(self):
        """
        :param OwnerUin: 用戶 UIN。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param ProjectId: 項目 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param From: 證書來源：trustasia = 亞洲誠信，upload = 用戶上傳。
注意：此欄位可能返回 null，表示取不到有效值。
        :type From: str
        :param CertificateType: 證書類型：CA = 用戶端證書，SVR = 服務器證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param PackageType: 證書套餐類型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增強型企業版（EV Pro）， 4 = SecureSite 增強型（EV）， 5 = SecureSite 企業型專業版（OV Pro）， 6 = SecureSite 企業型（OV）， 7 = SecureSite 企業型（OV）通配符， 8 = Geotrust 增強型（EV）， 9 = Geotrust 企業型（OV）， 10 = Geotrust 企業型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 證書， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企業型通配符（OV）SSL 證書（D3）， 14 = TrustAsia 企業型（OV）SSL 證書（D3）， 15 = TrustAsia 企業型多域名 （OV）SSL 證書（D3）， 16 = TrustAsia 增強型 （EV）SSL 證書（D3）， 17 = TrustAsia 增強型多域名（EV）SSL 證書（D3）， 18 = GlobalSign 企業型（OV）SSL 證書， 19 = GlobalSign 企業型通配符 （OV）SSL 證書， 20 = GlobalSign 增強型 （EV）SSL 證書， 21 = TrustAsia 企業型通配符多域名（OV）SSL 證書（D3）， 22 = GlobalSign 企業型多域名（OV）SSL 證書， 23 = GlobalSign 企業型通配符多域名（OV）SSL 證書， 24 = GlobalSign 增強型多域名（EV）SSL 證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param ProductZhName: 頒發者。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param Domain: 域名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Alias: 備注名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Status: 證書狀态：0 = 審核中，1 = 已通過，2 = 審核失敗，3 = 已過期，4 = 已添加DNS記錄，5 = 企業證書，待提交，6 = 訂單取消中，7 = 已取消，8 = 已提交資料， 待上傳确認函，9 = 證書吊銷中，10 = 已吊銷，11 = 重頒發中，12 = 待上傳吊銷确認函。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        :param StatusMsg: 狀态訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param VerifyType: 驗證類型：DNS_AUTO = 自動DNS驗證，DNS = 手動DNS驗證，FILE = 文件驗證，EMAIL = 郵件驗證。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param VulnerabilityStatus: 漏洞掃描狀态。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param CertBeginTime: 證書生效時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param CertEndTime: 證書失效時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ValidityPeriod: 證書有效期：單位（月）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param InsertTime: 申請時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param OrderId: 訂單 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param CertificateExtra: 證書擴展訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`taifucloudcloud.ssl.v20191205.models.CertificateExtra`
        :param CertificatePrivateKey: 證書私鑰
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificatePrivateKey: str
        :param CertificatePublicKey: 證書公鑰
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificatePublicKey: str
        :param DvAuthDetail: DV 認證訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthDetail: :class:`taifucloudcloud.ssl.v20191205.models.DvAuthDetail`
        :param VulnerabilityReport: 漏洞掃描評估報告。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VulnerabilityReport: str
        :param CertificateId: 證書 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param TypeName: 證書類型名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TypeName: str
        :param StatusName: 狀态描述。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param SubjectAltName: 證書包含的多個域名（包含主域名）
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param IsVip: 是否爲 VIP 客戶。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param IsWildcard: 是否爲泛域名證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param IsDv: 是否爲 DV 版證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param IsVulnerability: 是否啓用了漏洞掃描功能。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param SubmittedData: 提交的資料訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubmittedData: :class:`taifucloudcloud.ssl.v20191205.models.SubmittedData`
        :param RenewAble: 是否可重頒發證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param Deployable: 是否可部署。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.CertificateType = None
        self.PackageType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.StatusMsg = None
        self.VerifyType = None
        self.VulnerabilityStatus = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.OrderId = None
        self.CertificateExtra = None
        self.CertificatePrivateKey = None
        self.CertificatePublicKey = None
        self.DvAuthDetail = None
        self.VulnerabilityReport = None
        self.CertificateId = None
        self.TypeName = None
        self.StatusName = None
        self.SubjectAltName = None
        self.IsVip = None
        self.IsWildcard = None
        self.IsDv = None
        self.IsVulnerability = None
        self.SubmittedData = None
        self.RenewAble = None
        self.Deployable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.CertificateType = params.get("CertificateType")
        self.PackageType = params.get("PackageType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        self.CertificatePrivateKey = params.get("CertificatePrivateKey")
        self.CertificatePublicKey = params.get("CertificatePublicKey")
        if params.get("DvAuthDetail") is not None:
            self.DvAuthDetail = DvAuthDetail()
            self.DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self.VulnerabilityReport = params.get("VulnerabilityReport")
        self.CertificateId = params.get("CertificateId")
        self.TypeName = params.get("TypeName")
        self.StatusName = params.get("StatusName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.IsVip = params.get("IsVip")
        self.IsWildcard = params.get("IsWildcard")
        self.IsDv = params.get("IsDv")
        self.IsVulnerability = params.get("IsVulnerability")
        if params.get("SubmittedData") is not None:
            self.SubmittedData = SubmittedData()
            self.SubmittedData._deserialize(params.get("SubmittedData"))
        self.RenewAble = params.get("RenewAble")
        self.Deployable = params.get("Deployable")
        self.RequestId = params.get("RequestId")


class DescribeCertificateOperateLogsRequest(AbstractModel):
    """DescribeCertificateOperateLogs請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量，預設爲0。
        :type Offset: int
        :param Limit: 請求日志數量，預設爲20。
        :type Limit: int
        :param StartTime: 開始時間，預設15天前。
        :type StartTime: str
        :param EndTime: 結束時間，預設現在時間。
        :type EndTime: str
        """
        self.Offset = None
        self.Limit = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeCertificateOperateLogsResponse(AbstractModel):
    """DescribeCertificateOperateLogs返回參數結構體

    """

    def __init__(self):
        """
        :param AllTotal: 當前查詢條件日志總數。
        :type AllTotal: int
        :param TotalCount: 本次請求返回的日志數量。
        :type TotalCount: int
        :param OperateLogs: 證書操作日志清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperateLogs: list of OperationLog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AllTotal = None
        self.TotalCount = None
        self.OperateLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllTotal = params.get("AllTotal")
        self.TotalCount = params.get("TotalCount")
        if params.get("OperateLogs") is not None:
            self.OperateLogs = []
            for item in params.get("OperateLogs"):
                obj = OperationLog()
                obj._deserialize(item)
                self.OperateLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCertificateRequest(AbstractModel):
    """DescribeCertificate請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class DescribeCertificateResponse(AbstractModel):
    """DescribeCertificate返回參數結構體

    """

    def __init__(self):
        """
        :param OwnerUin: 用戶 UIN。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param ProjectId: 項目 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param From: 證書來源：trustasia = 亞洲誠信，upload = 用戶上傳。
注意：此欄位可能返回 null，表示取不到有效值。
        :type From: str
        :param CertificateType: 證書類型：CA = 用戶端證書，SVR = 服務器證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param PackageType: 證書套餐類型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增強型企業版（EV Pro）， 4 = SecureSite 增強型（EV）， 5 = SecureSite 企業型專業版（OV Pro）， 6 = SecureSite 企業型（OV）， 7 = SecureSite 企業型（OV）通配符， 8 = Geotrust 增強型（EV）， 9 = Geotrust 企業型（OV）， 10 = Geotrust 企業型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 證書， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企業型通配符（OV）SSL 證書（D3）， 14 = TrustAsia 企業型（OV）SSL 證書（D3）， 15 = TrustAsia 企業型多域名 （OV）SSL 證書（D3）， 16 = TrustAsia 增強型 （EV）SSL 證書（D3）， 17 = TrustAsia 增強型多域名（EV）SSL 證書（D3）， 18 = GlobalSign 企業型（OV）SSL 證書， 19 = GlobalSign 企業型通配符 （OV）SSL 證書， 20 = GlobalSign 增強型 （EV）SSL 證書， 21 = TrustAsia 企業型通配符多域名（OV）SSL 證書（D3）， 22 = GlobalSign 企業型多域名（OV）SSL 證書， 23 = GlobalSign 企業型通配符多域名（OV）SSL 證書， 24 = GlobalSign 增強型多域名（EV）SSL 證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param ProductZhName: 證書辦法者名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param Domain: 域名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Alias: 備注名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Status: 證書狀态：0 = 審核中，1 = 已通過，2 = 審核失敗，3 = 已過期，4 = 已添加DNS記錄，5 = 企業證書，待提交，6 = 訂單取消中，7 = 已取消，8 = 已提交資料， 待上傳确認函，9 = 證書吊銷中，10 = 已吊銷，11 = 重頒發中，12 = 待上傳吊銷确認函。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Status: int
        :param StatusMsg: 狀态訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param VerifyType: 驗證類型：DNS_AUTO = 自動DNS驗證，DNS = 手動DNS驗證，FILE = 文件驗證，EMAIL = 郵件驗證。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param VulnerabilityStatus: 漏洞掃描狀态。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param CertBeginTime: 證書生效時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param CertEndTime: 證書失效時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ValidityPeriod: 證書有效期：單位(月)。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param InsertTime: 申請時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param OrderId: 訂單 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param CertificateExtra: 證書擴展訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`taifucloudcloud.ssl.v20191205.models.CertificateExtra`
        :param DvAuthDetail: DV 認證訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthDetail: :class:`taifucloudcloud.ssl.v20191205.models.DvAuthDetail`
        :param VulnerabilityReport: 漏洞掃描評估報告。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VulnerabilityReport: str
        :param CertificateId: 證書 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param PackageTypeName: 證書類型名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PackageTypeName: str
        :param StatusName: 狀态描述。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param SubjectAltName: 證書包含的多個域名（包含主域名）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param IsVip: 是否爲 VIP 客戶。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param IsWildcard: 是否爲泛域名證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param IsDv: 是否爲 DV 版證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param IsVulnerability: 是否啓用了漏洞掃描功能。
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param RenewAble: 是否可重頒發證書。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param SubmittedData: 提交的資料訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SubmittedData: :class:`taifucloudcloud.ssl.v20191205.models.SubmittedData`
        :param Deployable: 是否可部署。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.CertificateType = None
        self.PackageType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.StatusMsg = None
        self.VerifyType = None
        self.VulnerabilityStatus = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.OrderId = None
        self.CertificateExtra = None
        self.DvAuthDetail = None
        self.VulnerabilityReport = None
        self.CertificateId = None
        self.PackageTypeName = None
        self.StatusName = None
        self.SubjectAltName = None
        self.IsVip = None
        self.IsWildcard = None
        self.IsDv = None
        self.IsVulnerability = None
        self.RenewAble = None
        self.SubmittedData = None
        self.Deployable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.CertificateType = params.get("CertificateType")
        self.PackageType = params.get("PackageType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        if params.get("DvAuthDetail") is not None:
            self.DvAuthDetail = DvAuthDetail()
            self.DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self.VulnerabilityReport = params.get("VulnerabilityReport")
        self.CertificateId = params.get("CertificateId")
        self.PackageTypeName = params.get("PackageTypeName")
        self.StatusName = params.get("StatusName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.IsVip = params.get("IsVip")
        self.IsWildcard = params.get("IsWildcard")
        self.IsDv = params.get("IsDv")
        self.IsVulnerability = params.get("IsVulnerability")
        self.RenewAble = params.get("RenewAble")
        if params.get("SubmittedData") is not None:
            self.SubmittedData = SubmittedData()
            self.SubmittedData._deserialize(params.get("SubmittedData"))
        self.Deployable = params.get("Deployable")
        self.RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 分頁偏移量，從0開始。
        :type Offset: int
        :param Limit: 每頁數量，預設20。
        :type Limit: int
        :param SearchKey: 搜索關鍵詞，可搜索證書 ID、備注名稱、域名。例如： a8xHcaIs。
        :type SearchKey: str
        :param CertificateType: 證書類型：CA = 用戶端證書，SVR = 服務器證書。
        :type CertificateType: str
        :param ProjectId: 項目 ID。
        :type ProjectId: int
        :param ExpirationSort: 按到期時間排序：DESC = 降序， ASC = 升序。
        :type ExpirationSort: str
        :param CertificateStatus: 證書狀态。
        :type CertificateStatus: list of int non-negative
        :param Deployable: 是否可佈署，可選值：1 = 可佈署，0 =  不可佈署。
        :type Deployable: int
        """
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.CertificateType = None
        self.ProjectId = None
        self.ExpirationSort = None
        self.CertificateStatus = None
        self.Deployable = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.CertificateType = params.get("CertificateType")
        self.ProjectId = params.get("ProjectId")
        self.ExpirationSort = params.get("ExpirationSort")
        self.CertificateStatus = params.get("CertificateStatus")
        self.Deployable = params.get("Deployable")


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總數量。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Certificates: 清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Certificates: list of Certificates
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Certificates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Certificates") is not None:
            self.Certificates = []
            for item in params.get("Certificates"):
                obj = Certificates()
                obj._deserialize(item)
                self.Certificates.append(obj)
        self.RequestId = params.get("RequestId")


class DownloadCertificateRequest(AbstractModel):
    """DownloadCertificate請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class DownloadCertificateResponse(AbstractModel):
    """DownloadCertificate返回參數結構體

    """

    def __init__(self):
        """
        :param Content: ZIP base64 編碼内容，base64 解碼後可保存爲 ZIP 文件。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Content: str
        :param ContentType: MIME 類型：application/zip = ZIP 壓縮文件。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContentType: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.ContentType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.ContentType = params.get("ContentType")
        self.RequestId = params.get("RequestId")


class DvAuthDetail(AbstractModel):
    """獲驗證書清單（DescribeCertificate）返回參數鍵爲 DvAuthDetail 的内容。

    """

    def __init__(self):
        """
        :param DvAuthKey: DV 認證金鑰。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthKey: str
        :param DvAuthValue: DV 認證值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthValue: str
        :param DvAuthDomain: DV 認證值域名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthDomain: str
        :param DvAuthPath: DV 認證值路徑。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthPath: str
        :param DvAuthKeySubDomain: DV 認證子域名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthKeySubDomain: str
        :param DvAuths: DV 認證訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuths: list of DvAuths
        """
        self.DvAuthKey = None
        self.DvAuthValue = None
        self.DvAuthDomain = None
        self.DvAuthPath = None
        self.DvAuthKeySubDomain = None
        self.DvAuths = None


    def _deserialize(self, params):
        self.DvAuthKey = params.get("DvAuthKey")
        self.DvAuthValue = params.get("DvAuthValue")
        self.DvAuthDomain = params.get("DvAuthDomain")
        self.DvAuthPath = params.get("DvAuthPath")
        self.DvAuthKeySubDomain = params.get("DvAuthKeySubDomain")
        if params.get("DvAuths") is not None:
            self.DvAuths = []
            for item in params.get("DvAuths"):
                obj = DvAuths()
                obj._deserialize(item)
                self.DvAuths.append(obj)


class DvAuths(AbstractModel):
    """獲驗證書清單（Certificate）返回參數鍵爲 DvAuths 的内容。

    """

    def __init__(self):
        """
        :param DvAuthKey: DV 認證金鑰。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthKey: str
        :param DvAuthValue: DV 認證值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthValue: str
        :param DvAuthDomain: DV 認證值域名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthDomain: str
        :param DvAuthPath: DV 認證值路徑。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthPath: str
        :param DvAuthSubDomain: DV 認證子域名，
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthSubDomain: str
        :param DvAuthVerifyType: DV 認證類型。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DvAuthVerifyType: str
        """
        self.DvAuthKey = None
        self.DvAuthValue = None
        self.DvAuthDomain = None
        self.DvAuthPath = None
        self.DvAuthSubDomain = None
        self.DvAuthVerifyType = None


    def _deserialize(self, params):
        self.DvAuthKey = params.get("DvAuthKey")
        self.DvAuthValue = params.get("DvAuthValue")
        self.DvAuthDomain = params.get("DvAuthDomain")
        self.DvAuthPath = params.get("DvAuthPath")
        self.DvAuthSubDomain = params.get("DvAuthSubDomain")
        self.DvAuthVerifyType = params.get("DvAuthVerifyType")


class ModifyCertificateAliasRequest(AbstractModel):
    """ModifyCertificateAlias請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        :param Alias: 備注名稱。
        :type Alias: str
        """
        self.CertificateId = None
        self.Alias = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.Alias = params.get("Alias")


class ModifyCertificateAliasResponse(AbstractModel):
    """ModifyCertificateAlias返回參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 修改成功的證書 ID。
        :type CertificateId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class ModifyCertificateProjectRequest(AbstractModel):
    """ModifyCertificateProject請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateIdList: 需要修改所屬項目的證書 ID 集合，最多100個證書。
        :type CertificateIdList: list of str
        :param ProjectId: 項目 ID。
        :type ProjectId: int
        """
        self.CertificateIdList = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.CertificateIdList = params.get("CertificateIdList")
        self.ProjectId = params.get("ProjectId")


class ModifyCertificateProjectResponse(AbstractModel):
    """ModifyCertificateProject返回參數結構體

    """

    def __init__(self):
        """
        :param SuccessCertificates: 修改所屬項目成功的證書集合。
注意：此欄位可能返回 null，表示取不到有效值。
        :type SuccessCertificates: list of str
        :param FailCertificates: 修改所屬項目失敗的證書集合。
注意：此欄位可能返回 null，表示取不到有效值。
        :type FailCertificates: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCertificates = None
        self.FailCertificates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCertificates = params.get("SuccessCertificates")
        self.FailCertificates = params.get("FailCertificates")
        self.RequestId = params.get("RequestId")


class OperationLog(AbstractModel):
    """證書操作日志。

    """

    def __init__(self):
        """
        :param Action: 操作證書動作。
        :type Action: str
        :param CreatedOn: 操作時間。
        :type CreatedOn: str
        """
        self.Action = None
        self.CreatedOn = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CreatedOn = params.get("CreatedOn")


class ProjectInfo(AbstractModel):
    """獲驗證書清單（DescribeCertificates）返回參數鍵爲 Certificates 下，key爲 ProjectInfo 的内容。

    """

    def __init__(self):
        """
        :param ProjectName: 項目名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param ProjectCreatorUin: 項目創建用戶 UIN。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectCreatorUin: int
        :param ProjectCreateTime: 項目創建時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectCreateTime: str
        :param ProjectResume: 項目訊息簡述。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectResume: str
        :param OwnerUin: 用戶 UIN。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OwnerUin: int
        :param ProjectId: 項目 ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProjectId: str
        """
        self.ProjectName = None
        self.ProjectCreatorUin = None
        self.ProjectCreateTime = None
        self.ProjectResume = None
        self.OwnerUin = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectCreatorUin = params.get("ProjectCreatorUin")
        self.ProjectCreateTime = params.get("ProjectCreateTime")
        self.ProjectResume = params.get("ProjectResume")
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")


class ReplaceCertificateRequest(AbstractModel):
    """ReplaceCertificate請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        :param ValidType: 驗證類型：DNS_AUTO = 自動DNS驗證，DNS = 手動DNS驗證，FILE = 文件驗證。
        :type ValidType: str
        :param CsrType: 類型，預設 Original。可選項：Original = 原證書 CSR，Upload = 手動上傳，Online = 在線生成。
        :type CsrType: str
        :param CsrContent: CSR 内容。
        :type CsrContent: str
        :param CsrkeyPassword: KEY 密碼。
        :type CsrkeyPassword: str
        """
        self.CertificateId = None
        self.ValidType = None
        self.CsrType = None
        self.CsrContent = None
        self.CsrkeyPassword = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ValidType = params.get("ValidType")
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CsrkeyPassword = params.get("CsrkeyPassword")


class ReplaceCertificateResponse(AbstractModel):
    """ReplaceCertificate返回參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class SubmitCertificateInformationRequest(AbstractModel):
    """SubmitCertificateInformation請求參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        :param CsrType: CSR 生成方式：online = 在線生成, parse = 手動上傳。
        :type CsrType: str
        :param CsrContent: 上傳的 CSR 内容。
        :type CsrContent: str
        :param CertificateDomain: 綁定證書的域名。
        :type CertificateDomain: str
        :param DomainList: 上傳的域名數組（多域名證書可以上傳）。
        :type DomainList: list of str
        :param KeyPassword: 私鑰密碼。
        :type KeyPassword: str
        :param OrganizationName: 公司名稱。
        :type OrganizationName: str
        :param OrganizationDivision: 部門名稱。
        :type OrganizationDivision: str
        :param OrganizationAddress: 公司詳細網址。
        :type OrganizationAddress: str
        :param OrganizationCountry: 國家名稱，如 ：CN 。
        :type OrganizationCountry: str
        :param OrganizationCity: 公司所在城市。
        :type OrganizationCity: str
        :param OrganizationRegion: 公司所在 。
        :type OrganizationRegion: str
        :param PostalCode: 公司郵編。
        :type PostalCode: str
        :param PhoneAreaCode: 公司座機區号。
        :type PhoneAreaCode: str
        :param PhoneNumber: 公司座機号碼。
        :type PhoneNumber: str
        :param VerifyType: 證書驗證方式。
        :type VerifyType: str
        :param AdminFirstName: 管理人姓。
        :type AdminFirstName: str
        :param AdminLastName: 管理人名。
        :type AdminLastName: str
        :param AdminPhoneNum: 管理人手機号碼。
        :type AdminPhoneNum: str
        :param AdminEmail: 管理人電子信箱網址。
        :type AdminEmail: str
        :param AdminPosition: 管理人職位。
        :type AdminPosition: str
        :param ContactFirstName: 聯系人姓。
        :type ContactFirstName: str
        :param ContactLastName: 聯系人名。
        :type ContactLastName: str
        :param ContactEmail: 聯系人電子信箱網址。
        :type ContactEmail: str
        :param ContactNumber: 聯系人手機号碼。
        :type ContactNumber: str
        :param ContactPosition: 聯系人職位。
        :type ContactPosition: str
        """
        self.CertificateId = None
        self.CsrType = None
        self.CsrContent = None
        self.CertificateDomain = None
        self.DomainList = None
        self.KeyPassword = None
        self.OrganizationName = None
        self.OrganizationDivision = None
        self.OrganizationAddress = None
        self.OrganizationCountry = None
        self.OrganizationCity = None
        self.OrganizationRegion = None
        self.PostalCode = None
        self.PhoneAreaCode = None
        self.PhoneNumber = None
        self.VerifyType = None
        self.AdminFirstName = None
        self.AdminLastName = None
        self.AdminPhoneNum = None
        self.AdminEmail = None
        self.AdminPosition = None
        self.ContactFirstName = None
        self.ContactLastName = None
        self.ContactEmail = None
        self.ContactNumber = None
        self.ContactPosition = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CertificateDomain = params.get("CertificateDomain")
        self.DomainList = params.get("DomainList")
        self.KeyPassword = params.get("KeyPassword")
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationDivision = params.get("OrganizationDivision")
        self.OrganizationAddress = params.get("OrganizationAddress")
        self.OrganizationCountry = params.get("OrganizationCountry")
        self.OrganizationCity = params.get("OrganizationCity")
        self.OrganizationRegion = params.get("OrganizationRegion")
        self.PostalCode = params.get("PostalCode")
        self.PhoneAreaCode = params.get("PhoneAreaCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.VerifyType = params.get("VerifyType")
        self.AdminFirstName = params.get("AdminFirstName")
        self.AdminLastName = params.get("AdminLastName")
        self.AdminPhoneNum = params.get("AdminPhoneNum")
        self.AdminEmail = params.get("AdminEmail")
        self.AdminPosition = params.get("AdminPosition")
        self.ContactFirstName = params.get("ContactFirstName")
        self.ContactLastName = params.get("ContactLastName")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactNumber = params.get("ContactNumber")
        self.ContactPosition = params.get("ContactPosition")


class SubmitCertificateInformationResponse(AbstractModel):
    """SubmitCertificateInformation返回參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class SubmittedData(AbstractModel):
    """獲驗證書清單（DescribeCertificate）返回參數鍵爲 SubmittedData 的内容。

    """

    def __init__(self):
        """
        :param CsrType: CSR 類型，（online = 在線生成CSR，parse = 粘貼 CSR）。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CsrType: str
        :param CsrContent: CSR 内容。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CsrContent: str
        :param CertificateDomain: 域名訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CertificateDomain: str
        :param DomainList: DNS 訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type DomainList: list of str
        :param KeyPassword: 私鑰密碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type KeyPassword: str
        :param OrganizationName: 企業或單位名稱。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        :param OrganizationDivision: 部門。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrganizationDivision: str
        :param OrganizationAddress: 網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrganizationAddress: str
        :param OrganizationCountry: 國家。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrganizationCountry: str
        :param OrganizationCity: 市。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrganizationCity: str
        :param OrganizationRegion: 省。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OrganizationRegion: str
        :param PostalCode: 郵政編碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PostalCode: str
        :param PhoneAreaCode: 座機區号。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PhoneAreaCode: str
        :param PhoneNumber: 座機号碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param AdminFirstName: 管理員名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdminFirstName: str
        :param AdminLastName: 管理員姓。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdminLastName: str
        :param AdminPhoneNum: 管理員電話号碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdminPhoneNum: str
        :param AdminEmail: 管理員電子信箱網址。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdminEmail: str
        :param AdminPosition: 管理員職位。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AdminPosition: str
        :param ContactFirstName: 聯系人名。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContactFirstName: str
        :param ContactLastName: 聯系人姓。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContactLastName: str
        :param ContactNumber: 聯系人電話号碼。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContactNumber: str
        :param ContactEmail: 聯系人電子信箱網址，
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContactEmail: str
        :param ContactPosition: 聯系人職位。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContactPosition: str
        :param VerifyType: 驗證類型。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VerifyType: str
        """
        self.CsrType = None
        self.CsrContent = None
        self.CertificateDomain = None
        self.DomainList = None
        self.KeyPassword = None
        self.OrganizationName = None
        self.OrganizationDivision = None
        self.OrganizationAddress = None
        self.OrganizationCountry = None
        self.OrganizationCity = None
        self.OrganizationRegion = None
        self.PostalCode = None
        self.PhoneAreaCode = None
        self.PhoneNumber = None
        self.AdminFirstName = None
        self.AdminLastName = None
        self.AdminPhoneNum = None
        self.AdminEmail = None
        self.AdminPosition = None
        self.ContactFirstName = None
        self.ContactLastName = None
        self.ContactNumber = None
        self.ContactEmail = None
        self.ContactPosition = None
        self.VerifyType = None


    def _deserialize(self, params):
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CertificateDomain = params.get("CertificateDomain")
        self.DomainList = params.get("DomainList")
        self.KeyPassword = params.get("KeyPassword")
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationDivision = params.get("OrganizationDivision")
        self.OrganizationAddress = params.get("OrganizationAddress")
        self.OrganizationCountry = params.get("OrganizationCountry")
        self.OrganizationCity = params.get("OrganizationCity")
        self.OrganizationRegion = params.get("OrganizationRegion")
        self.PostalCode = params.get("PostalCode")
        self.PhoneAreaCode = params.get("PhoneAreaCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.AdminFirstName = params.get("AdminFirstName")
        self.AdminLastName = params.get("AdminLastName")
        self.AdminPhoneNum = params.get("AdminPhoneNum")
        self.AdminEmail = params.get("AdminEmail")
        self.AdminPosition = params.get("AdminPosition")
        self.ContactFirstName = params.get("ContactFirstName")
        self.ContactLastName = params.get("ContactLastName")
        self.ContactNumber = params.get("ContactNumber")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactPosition = params.get("ContactPosition")
        self.VerifyType = params.get("VerifyType")


class UploadCertificateRequest(AbstractModel):
    """UploadCertificate請求參數結構體

    """

    def __init__(self):
        """
        :param CertificatePublicKey: 證書公鑰。
        :type CertificatePublicKey: str
        :param CertificatePrivateKey: 私鑰内容，證書類型爲 SVR 時必填，爲 CA 時可不填。
        :type CertificatePrivateKey: str
        :param CertificateType: 證書類型，預設 SVR。CA = 用戶端證書，SVR = 服務器證書。
        :type CertificateType: str
        :param Alias: 備注名稱。
        :type Alias: str
        :param ProjectId: 項目 ID。
        :type ProjectId: int
        """
        self.CertificatePublicKey = None
        self.CertificatePrivateKey = None
        self.CertificateType = None
        self.Alias = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.CertificatePublicKey = params.get("CertificatePublicKey")
        self.CertificatePrivateKey = params.get("CertificatePrivateKey")
        self.CertificateType = params.get("CertificateType")
        self.Alias = params.get("Alias")
        self.ProjectId = params.get("ProjectId")


class UploadCertificateResponse(AbstractModel):
    """UploadCertificate返回參數結構體

    """

    def __init__(self):
        """
        :param CertificateId: 證書 ID。
        :type CertificateId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")