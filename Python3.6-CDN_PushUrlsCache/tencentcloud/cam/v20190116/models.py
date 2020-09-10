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


class AddUserRequest(AbstractModel):
    """AddUser請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 子用戶用戶名
        :type Name: str
        :param Remark: 子用戶備注
        :type Remark: str
        :param ConsoleLogin: 子用戶是否可以登入控制台。傳0子用戶無法登入控制台，傳1子用戶可以登入控制台。
        :type ConsoleLogin: int
        :param UseApi: 是否生成子用戶金鑰。傳0不生成子用戶金鑰，傳1生成子用戶金鑰。
        :type UseApi: int
        :param Password: 子用戶控制台登入密碼，若未進行密碼規則設置則預設密碼規則爲8位以上同時包含大小寫字母、數字和特殊字元。只有可以登入控制台時才有效，如果傳空并且上面指定允許登入控制台，則自動生成随機密碼，随機密碼規則爲32位包含大小寫字母、數字和特殊字元。
        :type Password: str
        :param NeedResetPassword: 子用戶是否要在下次登入時重置密碼。傳0子用戶下次登入控制台不需重置密碼，傳1子用戶下次登入控制台需要重置密碼。
        :type NeedResetPassword: int
        :param PhoneNum: 手機号
        :type PhoneNum: str
        :param CountryCode: 區号
        :type CountryCode: str
        :param Email: 電子信箱
        :type Email: str
        """
        self.Name = None
        self.Remark = None
        self.ConsoleLogin = None
        self.UseApi = None
        self.Password = None
        self.NeedResetPassword = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.UseApi = params.get("UseApi")
        self.Password = params.get("Password")
        self.NeedResetPassword = params.get("NeedResetPassword")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")


class AddUserResponse(AbstractModel):
    """AddUser返回參數結構體

    """

    def __init__(self):
        """
        :param Uin: 子用戶 UIN
        :type Uin: int
        :param Name: 子用戶用戶名
        :type Name: str
        :param Password: 如果輸入參數組合爲自動生成随機密碼，則返回生成的密碼
        :type Password: str
        :param SecretId: 子用戶金鑰 ID
        :type SecretId: str
        :param SecretKey: 子用戶金鑰 Key
        :type SecretKey: str
        :param Uid: 子用戶 UID
        :type Uid: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.Name = None
        self.Password = None
        self.SecretId = None
        self.SecretKey = None
        self.Uid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Uid = params.get("Uid")
        self.RequestId = params.get("RequestId")


class AddUserToGroupRequest(AbstractModel):
    """AddUserToGroup請求參數結構體

    """

    def __init__(self):
        """
        :param Info: 添加的子用戶 UID 和用戶組 ID 關聯關系
        :type Info: list of GroupIdOfUidInfo
        """
        self.Info = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self.Info.append(obj)


class AddUserToGroupResponse(AbstractModel):
    """AddUserToGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachEntityOfPolicy(AbstractModel):
    """策略關聯的實體訊息

    """

    def __init__(self):
        """
        :param Id: 實體ID
        :type Id: str
        :param Name: 實體名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type Name: str
        :param Uin: 實體Uin
注意：此欄位可能返回 null，表示取不到有效值。
        :type Uin: int
        :param RelatedType: 關聯類型。1 用戶關聯 ； 2 用戶組關聯
        :type RelatedType: int
        """
        self.Id = None
        self.Name = None
        self.Uin = None
        self.RelatedType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Uin = params.get("Uin")
        self.RelatedType = params.get("RelatedType")


class AttachGroupPolicyRequest(AbstractModel):
    """AttachGroupPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param AttachGroupId: 用戶組 id
        :type AttachGroupId: int
        """
        self.PolicyId = None
        self.AttachGroupId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachGroupId = params.get("AttachGroupId")


class AttachGroupPolicyResponse(AbstractModel):
    """AttachGroupPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachPolicyInfo(AbstractModel):
    """關聯策略訊息

    """

    def __init__(self):
        """
        :param PolicyId: 策略id
        :type PolicyId: int
        :param PolicyName: 策略名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param AddTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param CreateMode: 創建來源，1 通過控制台創建, 2 通過策略語法創建。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateMode: int
        :param PolicyType: 取值爲user和QCS
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param Remark: 策略備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type Remark: str
        :param OperateOwnerUin: 策略關聯操作者主張号
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperateOwnerUin: str
        :param OperateUin: 策略關聯操作者ID，如果UinType爲0表示子帳号Uin，如果UinType爲1表示角色ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperateUin: str
        :param OperateUinType: UinType爲0表示OperateUin欄位是子帳号Uin，如果UinType爲1表示OperateUin欄位是角色ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type OperateUinType: int
        :param Deactived: 是否已下線
注意：此欄位可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param DeactivedDetail: 已下線的産品清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.CreateMode = None
        self.PolicyType = None
        self.Remark = None
        self.OperateOwnerUin = None
        self.OperateUin = None
        self.OperateUinType = None
        self.Deactived = None
        self.DeactivedDetail = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.CreateMode = params.get("CreateMode")
        self.PolicyType = params.get("PolicyType")
        self.Remark = params.get("Remark")
        self.OperateOwnerUin = params.get("OperateOwnerUin")
        self.OperateUin = params.get("OperateUin")
        self.OperateUinType = params.get("OperateUinType")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")


class AttachRolePolicyRequest(AbstractModel):
    """AttachRolePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID，入參PolicyId與PolicyName二選一
        :type PolicyId: int
        :param AttachRoleId: 角色ID，用于指定角色，入參 AttachRoleId 與 AttachRoleName 二選一
        :type AttachRoleId: str
        :param AttachRoleName: 角色名稱，用于指定角色，入參 AttachRoleId 與 AttachRoleName 二選一
        :type AttachRoleName: str
        :param PolicyName: 策略名，入參PolicyId與PolicyName二選一
        :type PolicyName: str
        """
        self.PolicyId = None
        self.AttachRoleId = None
        self.AttachRoleName = None
        self.PolicyName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachRoleId = params.get("AttachRoleId")
        self.AttachRoleName = params.get("AttachRoleName")
        self.PolicyName = params.get("PolicyName")


class AttachRolePolicyResponse(AbstractModel):
    """AttachRolePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param AttachUin: 子賬号 uin
        :type AttachUin: int
        """
        self.PolicyId = None
        self.AttachUin = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.AttachUin = params.get("AttachUin")


class AttachUserPolicyResponse(AbstractModel):
    """AttachUserPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachedPolicyOfRole(AbstractModel):
    """角色關聯的策略訊息

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param PolicyName: 策略名稱
        :type PolicyName: str
        :param AddTime: 綁定時間
        :type AddTime: str
        :param PolicyType: 策略類型，User表示自定義策略，QCS表示預設策略
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolicyType: str
        :param CreateMode: 策略創建方式，1表示按産品功能或項目權限創建，其他表示按策略語法創建
        :type CreateMode: int
        :param Deactived: 是否已下線(0:否 1:是)
注意：此欄位可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param DeactivedDetail: 已下線的産品清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        :param Description: 策略描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.PolicyType = None
        self.CreateMode = None
        self.Deactived = None
        self.DeactivedDetail = None
        self.Description = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.PolicyType = params.get("PolicyType")
        self.CreateMode = params.get("CreateMode")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        self.Description = params.get("Description")


class ConsumeCustomMFATokenRequest(AbstractModel):
    """ConsumeCustomMFAToken請求參數結構體

    """

    def __init__(self):
        """
        :param MFAToken: 自定義多因子驗證Token
        :type MFAToken: str
        """
        self.MFAToken = None


    def _deserialize(self, params):
        self.MFAToken = params.get("MFAToken")


class ConsumeCustomMFATokenResponse(AbstractModel):
    """ConsumeCustomMFAToken返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    """CreateGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupName: 用戶組名
        :type GroupName: str
        :param Remark: 用戶組描述
        :type Remark: str
        """
        self.GroupName = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.Remark = params.get("Remark")


class CreateGroupResponse(AbstractModel):
    """CreateGroup返回參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 用戶組 ID
        :type GroupId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreatePolicyRequest(AbstractModel):
    """CreatePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyName: 策略名
        :type PolicyName: str
        :param PolicyDocument: 策略文件，範例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.taifucloud.com","cls.cloud.taifucloud.com"]}}]}，principal用于指定角色的授權對象。獲取該參數可參閱 獲取角色詳情（https://cloud.taifucloud.com/document/product/598/36221） 輸出參數RoleInfo
        :type PolicyDocument: str
        :param Description: 策略描述
        :type Description: str
        """
        self.PolicyName = None
        self.PolicyDocument = None
        self.Description = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")


class CreatePolicyResponse(AbstractModel):
    """CreatePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 新增策略ID
        :type PolicyId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreatePolicyVersionRequest(AbstractModel):
    """CreatePolicyVersion請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param PolicyDocument: 策略文本訊息
        :type PolicyDocument: str
        :param SetAsDefault: 是否設置爲當前策略的版本
        :type SetAsDefault: bool
        """
        self.PolicyId = None
        self.PolicyDocument = None
        self.SetAsDefault = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyDocument = params.get("PolicyDocument")
        self.SetAsDefault = params.get("SetAsDefault")


class CreatePolicyVersionResponse(AbstractModel):
    """CreatePolicyVersion返回參數結構體

    """

    def __init__(self):
        """
        :param VersionId: 策略版本号
注意：此欄位可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    """CreateRole請求參數結構體

    """

    def __init__(self):
        """
        :param RoleName: 角色名稱
        :type RoleName: str
        :param PolicyDocument: 策略文件，範例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.taifucloud.com","cls.cloud.taifucloud.com"]}}]}，principal用于指定角色的授權對象。獲取該參數可參閱 獲取角色詳情（https://cloud.taifucloud.com/document/product/598/36221） 輸出參數RoleInfo
        :type PolicyDocument: str
        :param Description: 角色描述
        :type Description: str
        :param ConsoleLogin: 是否允許登入 1 爲允許 0 爲不允許
        :type ConsoleLogin: int
        :param SessionDuration: 申請角色臨時金鑰的最長有效期限制(範圍：0~43200)
        :type SessionDuration: int
        """
        self.RoleName = None
        self.PolicyDocument = None
        self.Description = None
        self.ConsoleLogin = None
        self.SessionDuration = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.SessionDuration = params.get("SessionDuration")


class CreateRoleResponse(AbstractModel):
    """CreateRole返回參數結構體

    """

    def __init__(self):
        """
        :param RoleId: 角色ID
注意：此欄位可能返回 null，表示取不到有效值。
        :type RoleId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RoleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RequestId = params.get("RequestId")


class CreateSAMLProviderRequest(AbstractModel):
    """CreateSAMLProvider請求參數結構體

    """

    def __init__(self):
        """
        :param Name: SAML身份提供商名稱
        :type Name: str
        :param Description: SAML身份提供商描述
        :type Description: str
        :param SAMLMetadataDocument: SAML身份提供商Base64編碼的中繼資料文件
        :type SAMLMetadataDocument: str
        """
        self.Name = None
        self.Description = None
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")


class CreateSAMLProviderResponse(AbstractModel):
    """CreateSAMLProvider返回參數結構體

    """

    def __init__(self):
        """
        :param ProviderArn: SAML身份提供商資源描述符
        :type ProviderArn: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProviderArn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProviderArn = params.get("ProviderArn")
        self.RequestId = params.get("RequestId")


class CreateServiceLinkedRoleRequest(AbstractModel):
    """CreateServiceLinkedRole請求參數結構體

    """

    def __init__(self):
        """
        :param QCSServiceName: 授權服務，附加了此角色的Top Cloud 服務主體。
        :type QCSServiceName: list of str
        :param CustomSuffix: 自定義後綴，根據您提供的字串，與服務提供的前綴組合在一起以形成完整的角色名稱。
        :type CustomSuffix: str
        :param Description: 角色說明。
        :type Description: str
        """
        self.QCSServiceName = None
        self.CustomSuffix = None
        self.Description = None


    def _deserialize(self, params):
        self.QCSServiceName = params.get("QCSServiceName")
        self.CustomSuffix = params.get("CustomSuffix")
        self.Description = params.get("Description")


class CreateServiceLinkedRoleResponse(AbstractModel):
    """CreateServiceLinkedRole返回參數結構體

    """

    def __init__(self):
        """
        :param RoleId: 角色ID
        :type RoleId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RoleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    """DeleteGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 用戶組 ID
        :type GroupId: int
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteGroupResponse(AbstractModel):
    """DeleteGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePolicyRequest(AbstractModel):
    """DeletePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 數組，數組成員是策略 id，支援批次删除策略
        :type PolicyId: list of int non-negative
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")


class DeletePolicyResponse(AbstractModel):
    """DeletePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePolicyVersionRequest(AbstractModel):
    """DeletePolicyVersion請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param VersionId: 策略版本号
        :type VersionId: list of int non-negative
        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")


class DeletePolicyVersionResponse(AbstractModel):
    """DeletePolicyVersion返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoleRequest(AbstractModel):
    """DeleteRole請求參數結構體

    """

    def __init__(self):
        """
        :param RoleId: 角色ID，用于指定角色，入參 RoleId 與 RoleName 二選一
        :type RoleId: str
        :param RoleName: 角色名稱，用于指定角色，入參 RoleId 與 RoleName 二選一
        :type RoleName: str
        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")


class DeleteRoleResponse(AbstractModel):
    """DeleteRole返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSAMLProviderRequest(AbstractModel):
    """DeleteSAMLProvider請求參數結構體

    """

    def __init__(self):
        """
        :param Name: SAML身份提供商名稱
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")


class DeleteSAMLProviderResponse(AbstractModel):
    """DeleteSAMLProvider返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceLinkedRoleRequest(AbstractModel):
    """DeleteServiceLinkedRole請求參數結構體

    """

    def __init__(self):
        """
        :param RoleName: 要删除的服務相關角色的名稱。
        :type RoleName: str
        """
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")


class DeleteServiceLinkedRoleResponse(AbstractModel):
    """DeleteServiceLinkedRole返回參數結構體

    """

    def __init__(self):
        """
        :param DeletionTaskId: 删除任務ID，可用于檢查删除服務相關角色狀态。
        :type DeletionTaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeletionTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeletionTaskId = params.get("DeletionTaskId")
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 子用戶用戶名
        :type Name: str
        :param Force: 是否強制删除該子用戶，預設入參爲0。0：若該用戶存在未删除API金鑰，則不删除用戶；1：若該用戶存在未删除API金鑰，則先删除金鑰後删除用戶。删除金鑰需要您擁有cam:DeleteApiKey權限，您将可以删除該用戶下啓用或禁用狀态的所有金鑰，無權限則删除金鑰和用戶失敗
        :type Force: int
        """
        self.Name = None
        self.Force = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Force = params.get("Force")


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeRoleListRequest(AbstractModel):
    """DescribeRoleList請求參數結構體

    """

    def __init__(self):
        """
        :param Page: 頁碼，從1開始
        :type Page: int
        :param Rp: 每頁行數，不能大于200
        :type Rp: int
        """
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")


class DescribeRoleListResponse(AbstractModel):
    """DescribeRoleList返回參數結構體

    """

    def __init__(self):
        """
        :param List: 角色詳情清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type List: list of RoleInfo
        :param TotalNum: 角色總數
        :type TotalNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = RoleInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class DetachGroupPolicyRequest(AbstractModel):
    """DetachGroupPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param DetachGroupId: 用戶組 id
        :type DetachGroupId: int
        """
        self.PolicyId = None
        self.DetachGroupId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachGroupId = params.get("DetachGroupId")


class DetachGroupPolicyResponse(AbstractModel):
    """DetachGroupPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachRolePolicyRequest(AbstractModel):
    """DetachRolePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID，入參PolicyId與PolicyName二選一
        :type PolicyId: int
        :param DetachRoleId: 角色ID，用于指定角色，入參 AttachRoleId 與 AttachRoleName 二選一
        :type DetachRoleId: str
        :param DetachRoleName: 角色名稱，用于指定角色，入參 AttachRoleId 與 AttachRoleName 二選一
        :type DetachRoleName: str
        :param PolicyName: 策略名，入參PolicyId與PolicyName二選一
        :type PolicyName: str
        """
        self.PolicyId = None
        self.DetachRoleId = None
        self.DetachRoleName = None
        self.PolicyName = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachRoleId = params.get("DetachRoleId")
        self.DetachRoleName = params.get("DetachRoleName")
        self.PolicyName = params.get("PolicyName")


class DetachRolePolicyResponse(AbstractModel):
    """DetachRolePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachUserPolicyRequest(AbstractModel):
    """DetachUserPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param DetachUin: 子賬号 uin
        :type DetachUin: int
        """
        self.PolicyId = None
        self.DetachUin = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.DetachUin = params.get("DetachUin")


class DetachUserPolicyResponse(AbstractModel):
    """DetachUserPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GetCustomMFATokenInfoRequest(AbstractModel):
    """GetCustomMFATokenInfo請求參數結構體

    """

    def __init__(self):
        """
        :param MFAToken: 自定義多因子驗證Token
        :type MFAToken: str
        """
        self.MFAToken = None


    def _deserialize(self, params):
        self.MFAToken = params.get("MFAToken")


class GetCustomMFATokenInfoResponse(AbstractModel):
    """GetCustomMFATokenInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Uin: 自定義多因子驗證Token對應的帳号Id
        :type Uin: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class GetGroupRequest(AbstractModel):
    """GetGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 用戶組 ID
        :type GroupId: int
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class GetGroupResponse(AbstractModel):
    """GetGroup返回參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 用戶組 ID
        :type GroupId: int
        :param GroupName: 用戶組名稱
        :type GroupName: str
        :param GroupNum: 用戶組成員數量
        :type GroupNum: int
        :param Remark: 用戶組描述
        :type Remark: str
        :param CreateTime: 用戶組創建時間
        :type CreateTime: str
        :param UserInfo: 用戶組成員訊息
        :type UserInfo: list of GroupMemberInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.GroupName = None
        self.GroupNum = None
        self.Remark = None
        self.CreateTime = None
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.GroupNum = params.get("GroupNum")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.RequestId = params.get("RequestId")


class GetPolicyRequest(AbstractModel):
    """GetPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略Id
        :type PolicyId: int
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")


class GetPolicyResponse(AbstractModel):
    """GetPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param PolicyName: 策略名
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param Description: 策略描述
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param Type: 1 表示自定義策略，2 表示預設策略
注意：此欄位可能返回 null，表示取不到有效值。
        :type Type: int
        :param AddTime: 創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param UpdateTime: 最近更新時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param PolicyDocument: 策略文件
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolicyDocument: str
        :param PresetAlias: 備注
注意：此欄位可能返回 null，表示取不到有效值。
        :type PresetAlias: str
        :param IsServiceLinkedRolePolicy: 是否服務相關策略
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsServiceLinkedRolePolicy: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PolicyName = None
        self.Description = None
        self.Type = None
        self.AddTime = None
        self.UpdateTime = None
        self.PolicyDocument = None
        self.PresetAlias = None
        self.IsServiceLinkedRolePolicy = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.Type = params.get("Type")
        self.AddTime = params.get("AddTime")
        self.UpdateTime = params.get("UpdateTime")
        self.PolicyDocument = params.get("PolicyDocument")
        self.PresetAlias = params.get("PresetAlias")
        self.IsServiceLinkedRolePolicy = params.get("IsServiceLinkedRolePolicy")
        self.RequestId = params.get("RequestId")


class GetPolicyVersionRequest(AbstractModel):
    """GetPolicyVersion請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param VersionId: 策略版本号
        :type VersionId: int
        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")


class GetPolicyVersionResponse(AbstractModel):
    """GetPolicyVersion返回參數結構體

    """

    def __init__(self):
        """
        :param PolicyVersion: 策略版本詳情
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolicyVersion: :class:`taifucloudcloud.cam.v20190116.models.PolicyVersionDetail`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PolicyVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PolicyVersion") is not None:
            self.PolicyVersion = PolicyVersionDetail()
            self.PolicyVersion._deserialize(params.get("PolicyVersion"))
        self.RequestId = params.get("RequestId")


class GetRoleRequest(AbstractModel):
    """GetRole請求參數結構體

    """

    def __init__(self):
        """
        :param RoleId: 角色 ID，用于指定角色，入參 RoleId 與 RoleName 二選一
        :type RoleId: str
        :param RoleName: 角色名，用于指定角色，入參 RoleId 與 RoleName 二選一
        :type RoleName: str
        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")


class GetRoleResponse(AbstractModel):
    """GetRole返回參數結構體

    """

    def __init__(self):
        """
        :param RoleInfo: 角色詳情
        :type RoleInfo: :class:`taifucloudcloud.cam.v20190116.models.RoleInfo`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RoleInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RoleInfo") is not None:
            self.RoleInfo = RoleInfo()
            self.RoleInfo._deserialize(params.get("RoleInfo"))
        self.RequestId = params.get("RequestId")


class GetSAMLProviderRequest(AbstractModel):
    """GetSAMLProvider請求參數結構體

    """

    def __init__(self):
        """
        :param Name: SAML身份提供商名稱
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")


class GetSAMLProviderResponse(AbstractModel):
    """GetSAMLProvider返回參數結構體

    """

    def __init__(self):
        """
        :param Name: SAML身份提供商名稱
        :type Name: str
        :param Description: SAML身份提供商描述
        :type Description: str
        :param CreateTime: SAML身份提供商創建時間
        :type CreateTime: str
        :param ModifyTime: SAML身份提供商上次修改時間
        :type ModifyTime: str
        :param SAMLMetadata: SAML身份提供商中繼資料文件
        :type SAMLMetadata: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.ModifyTime = None
        self.SAMLMetadata = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.SAMLMetadata = params.get("SAMLMetadata")
        self.RequestId = params.get("RequestId")


class GetServiceLinkedRoleDeletionStatusRequest(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus請求參數結構體

    """

    def __init__(self):
        """
        :param DeletionTaskId: 删除任務ID
        :type DeletionTaskId: str
        """
        self.DeletionTaskId = None


    def _deserialize(self, params):
        self.DeletionTaskId = params.get("DeletionTaskId")


class GetServiceLinkedRoleDeletionStatusResponse(AbstractModel):
    """GetServiceLinkedRoleDeletionStatus返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 狀态：NOT_STARTED，IN_PROGRESS，SUCCEEDED，FAILED
        :type Status: str
        :param Reason: 失敗原因
        :type Reason: str
        :param ServiceType: 服務類型
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param ServiceName: 服務名稱
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Reason = None
        self.ServiceType = None
        self.ServiceName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.ServiceType = params.get("ServiceType")
        self.ServiceName = params.get("ServiceName")
        self.RequestId = params.get("RequestId")


class GetUserRequest(AbstractModel):
    """GetUser請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 子用戶用戶名
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")


class GetUserResponse(AbstractModel):
    """GetUser返回參數結構體

    """

    def __init__(self):
        """
        :param Uin: 子用戶用戶 UIN
        :type Uin: int
        :param Name: 子用戶用戶名
        :type Name: str
        :param Uid: 子用戶 UID
        :type Uid: int
        :param Remark: 子用戶備注
        :type Remark: str
        :param ConsoleLogin: 子用戶能否登入控制台
        :type ConsoleLogin: int
        :param PhoneNum: 手機号
        :type PhoneNum: str
        :param CountryCode: 區号
        :type CountryCode: str
        :param Email: 電子信箱
        :type Email: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.ConsoleLogin = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")
        self.RequestId = params.get("RequestId")


class GroupIdOfUidInfo(AbstractModel):
    """子用戶和用戶組關聯訊息

    """

    def __init__(self):
        """
        :param Uid: 子用戶 UID
        :type Uid: int
        :param GroupId: 用戶組 ID
        :type GroupId: int
        """
        self.Uid = None
        self.GroupId = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.GroupId = params.get("GroupId")


class GroupInfo(AbstractModel):
    """用戶組訊息

    """

    def __init__(self):
        """
        :param GroupId: 用戶組 ID。
        :type GroupId: int
        :param GroupName: 用戶組名稱。
        :type GroupName: str
        :param CreateTime: 用戶組創建時間。
        :type CreateTime: str
        :param Remark: 用戶組描述。
        :type Remark: str
        """
        self.GroupId = None
        self.GroupName = None
        self.CreateTime = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.CreateTime = params.get("CreateTime")
        self.Remark = params.get("Remark")


class GroupMemberInfo(AbstractModel):
    """用戶組用戶訊息

    """

    def __init__(self):
        """
        :param Uid: 子用戶 Uid。
        :type Uid: int
        :param Uin: 子用戶 Uin。
        :type Uin: int
        :param Name: 子用戶名稱。
        :type Name: str
        :param PhoneNum: 手機号。
        :type PhoneNum: str
        :param CountryCode: 手機區域代碼。
        :type CountryCode: str
        :param PhoneFlag: 是否已驗證手機。
        :type PhoneFlag: int
        :param Email: 電子信箱網址。
        :type Email: str
        :param EmailFlag: 是否已驗證電子信箱。
        :type EmailFlag: int
        :param UserType: 用戶類型。
        :type UserType: int
        :param CreateTime: 創建時間。
        :type CreateTime: str
        :param IsReceiverOwner: 是否爲主訊息接收人。
        :type IsReceiverOwner: int
        """
        self.Uid = None
        self.Uin = None
        self.Name = None
        self.PhoneNum = None
        self.CountryCode = None
        self.PhoneFlag = None
        self.Email = None
        self.EmailFlag = None
        self.UserType = None
        self.CreateTime = None
        self.IsReceiverOwner = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.PhoneFlag = params.get("PhoneFlag")
        self.Email = params.get("Email")
        self.EmailFlag = params.get("EmailFlag")
        self.UserType = params.get("UserType")
        self.CreateTime = params.get("CreateTime")
        self.IsReceiverOwner = params.get("IsReceiverOwner")


class ListAttachedGroupPoliciesRequest(AbstractModel):
    """ListAttachedGroupPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param TargetGroupId: 用戶組ID
        :type TargetGroupId: int
        :param Page: 頁碼，預設值是 1，從 1 開始
        :type Page: int
        :param Rp: 每頁大小，預設值是 20
        :type Rp: int
        """
        self.TargetGroupId = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.TargetGroupId = params.get("TargetGroupId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")


class ListAttachedGroupPoliciesResponse(AbstractModel):
    """ListAttachedGroupPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 策略總數
        :type TotalNum: int
        :param List: 策略清單
        :type List: list of AttachPolicyInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListAttachedRolePoliciesRequest(AbstractModel):
    """ListAttachedRolePolicies請求參數結構體

    """

    def __init__(self):
        """
        :param Page: 頁碼，從 1 開始
        :type Page: int
        :param Rp: 每頁行數，不能大于200
        :type Rp: int
        :param RoleId: 角色 ID。用于指定角色，入參 RoleId 與 RoleName 二選一
        :type RoleId: str
        :param RoleName: 角色名。用于指定角色，入參 RoleId 與 RoleName 二選一
        :type RoleName: str
        :param PolicyType: 按策略類型過濾，User表示僅查詢自定義策略，QCS表示僅查詢預設策略
        :type PolicyType: str
        """
        self.Page = None
        self.Rp = None
        self.RoleId = None
        self.RoleName = None
        self.PolicyType = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        self.PolicyType = params.get("PolicyType")


class ListAttachedRolePoliciesResponse(AbstractModel):
    """ListAttachedRolePolicies返回參數結構體

    """

    def __init__(self):
        """
        :param List: 角色關聯的策略清單
        :type List: list of AttachedPolicyOfRole
        :param TotalNum: 角色關聯的策略總數
        :type TotalNum: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachedPolicyOfRole()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class ListAttachedUserPoliciesRequest(AbstractModel):
    """ListAttachedUserPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param TargetUin: 子賬号 uin
        :type TargetUin: int
        :param Page: 頁碼，預設值是 1，從 1 開始
        :type Page: int
        :param Rp: 每頁大小，預設值是 20
        :type Rp: int
        """
        self.TargetUin = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")


class ListAttachedUserPoliciesResponse(AbstractModel):
    """ListAttachedUserPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 策略總數
        :type TotalNum: int
        :param List: 策略清單
        :type List: list of AttachPolicyInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachPolicyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListCollaboratorsRequest(AbstractModel):
    """ListCollaborators請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 分頁條數，缺省爲20
        :type Limit: int
        :param Offset: 分頁起始值，缺省爲0
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class ListCollaboratorsResponse(AbstractModel):
    """ListCollaborators返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 總數
        :type TotalNum: int
        :param Data: 協作者訊息
        :type Data: list of SubAccountInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ListEntitiesForPolicyRequest(AbstractModel):
    """ListEntitiesForPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param Page: 頁碼，預設值是 1，從 1 開始
        :type Page: int
        :param Rp: 每頁大小，預設值是 20
        :type Rp: int
        :param EntityFilter: 可取值 'All'、'User'、'Group' 和 'Role'，'All' 表示獲取所有實體類型，'User' 表示只獲取子賬号，'Group' 表示只獲取用戶組，'Role' 表示只獲取角色，預設取 'All'
        :type EntityFilter: str
        """
        self.PolicyId = None
        self.Page = None
        self.Rp = None
        self.EntityFilter = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.EntityFilter = params.get("EntityFilter")


class ListEntitiesForPolicyResponse(AbstractModel):
    """ListEntitiesForPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 實體總數
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalNum: int
        :param List: 實體清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type List: list of AttachEntityOfPolicy
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = AttachEntityOfPolicy()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class ListGroupsForUserRequest(AbstractModel):
    """ListGroupsForUser請求參數結構體

    """

    def __init__(self):
        """
        :param Uid: 子用戶 UID
        :type Uid: int
        :param Rp: 每頁數量。預設爲20。
        :type Rp: int
        :param Page: 頁碼。預設爲1。
        :type Page: int
        :param SubUin: 子賬号UIN
        :type SubUin: int
        """
        self.Uid = None
        self.Rp = None
        self.Page = None
        self.SubUin = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")
        self.SubUin = params.get("SubUin")


class ListGroupsForUserResponse(AbstractModel):
    """ListGroupsForUser返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 子用戶加入的用戶組總數
        :type TotalNum: int
        :param GroupInfo: 用戶組訊息
        :type GroupInfo: list of GroupInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.GroupInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListGroupsRequest(AbstractModel):
    """ListGroups請求參數結構體

    """

    def __init__(self):
        """
        :param Page: 頁碼。預設爲1。
        :type Page: int
        :param Rp: 每頁數量。預設爲20。
        :type Rp: int
        :param Keyword: 按用戶組名稱比對。
        :type Keyword: str
        """
        self.Page = None
        self.Rp = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")
        self.Keyword = params.get("Keyword")


class ListGroupsResponse(AbstractModel):
    """ListGroups返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 用戶組總數。
        :type TotalNum: int
        :param GroupInfo: 用戶組數組訊息。
        :type GroupInfo: list of GroupInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.GroupInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("GroupInfo") is not None:
            self.GroupInfo = []
            for item in params.get("GroupInfo"):
                obj = GroupInfo()
                obj._deserialize(item)
                self.GroupInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListPoliciesRequest(AbstractModel):
    """ListPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param Rp: 每頁數量，預設值是 20，必須大于 0 且小於或等于 200
        :type Rp: int
        :param Page: 頁碼，預設值是 1，從 1開始，不能大于 200
        :type Page: int
        :param Scope: 可取值 'All'、'QCS' 和 'Local'，'All' 獲取所有策略，'QCS' 只獲取預設策略，'Local' 只獲取自定義策略，預設取 'All'
        :type Scope: str
        :param Keyword: 按策略名比對
        :type Keyword: str
        """
        self.Rp = None
        self.Page = None
        self.Scope = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")
        self.Scope = params.get("Scope")
        self.Keyword = params.get("Keyword")


class ListPoliciesResponse(AbstractModel):
    """ListPolicies返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 策略總數
        :type TotalNum: int
        :param List: 策略數組，數組每個成員包括 policyId、policyName、addTime、type、description、 createMode 欄位。其中： 
policyId：策略 id 
policyName：策略名
addTime：策略創建時間
type：1 表示自定義策略，2 表示預設策略 
description：策略描述 
createMode：1 表示按業務權限創建的策略，其他值表示可以檢視策略語法和通過策略語法更新策略
Attachments: 關聯的用戶數
ServiceType: 策略關聯的産品
IsAttached: 當需要查詢标記實體是否已經關聯策略時不爲null。0表示未關聯策略，1表示已關聯策略
        :type List: list of StrategyInfo
        :param ServiceTypeList: 保留欄位
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceTypeList: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.List = None
        self.ServiceTypeList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = StrategyInfo()
                obj._deserialize(item)
                self.List.append(obj)
        self.ServiceTypeList = params.get("ServiceTypeList")
        self.RequestId = params.get("RequestId")


class ListPolicyVersionsRequest(AbstractModel):
    """ListPolicyVersions請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID
        :type PolicyId: int
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")


class ListPolicyVersionsResponse(AbstractModel):
    """ListPolicyVersions返回參數結構體

    """

    def __init__(self):
        """
        :param Versions: 策略版本清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type Versions: list of PolicyVersionItem
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Versions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = PolicyVersionItem()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.RequestId = params.get("RequestId")


class ListSAMLProvidersRequest(AbstractModel):
    """ListSAMLProviders請求參數結構體

    """


class ListSAMLProvidersResponse(AbstractModel):
    """ListSAMLProviders返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: SAML身份提供商總數
        :type TotalCount: int
        :param SAMLProviderSet: SAML身份提供商清單
        :type SAMLProviderSet: list of SAMLProviderInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SAMLProviderSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SAMLProviderSet") is not None:
            self.SAMLProviderSet = []
            for item in params.get("SAMLProviderSet"):
                obj = SAMLProviderInfo()
                obj._deserialize(item)
                self.SAMLProviderSet.append(obj)
        self.RequestId = params.get("RequestId")


class ListUsersForGroupRequest(AbstractModel):
    """ListUsersForGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 用戶組 ID。
        :type GroupId: int
        :param Page: 頁碼。預設爲1。
        :type Page: int
        :param Rp: 每頁數量。預設爲20。
        :type Rp: int
        """
        self.GroupId = None
        self.Page = None
        self.Rp = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Page = params.get("Page")
        self.Rp = params.get("Rp")


class ListUsersForGroupResponse(AbstractModel):
    """ListUsersForGroup返回參數結構體

    """

    def __init__(self):
        """
        :param TotalNum: 用戶組關聯的用戶總數。
        :type TotalNum: int
        :param UserInfo: 子用戶訊息。
        :type UserInfo: list of GroupMemberInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalNum = None
        self.UserInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("UserInfo") is not None:
            self.UserInfo = []
            for item in params.get("UserInfo"):
                obj = GroupMemberInfo()
                obj._deserialize(item)
                self.UserInfo.append(obj)
        self.RequestId = params.get("RequestId")


class ListUsersRequest(AbstractModel):
    """ListUsers請求參數結構體

    """


class ListUsersResponse(AbstractModel):
    """ListUsers返回參數結構體

    """

    def __init__(self):
        """
        :param Data: 子用戶訊息
        :type Data: list of SubAccountInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubAccountInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class PolicyVersionDetail(AbstractModel):
    """策略版本詳情

    """

    def __init__(self):
        """
        :param VersionId: 策略版本号
注意：此欄位可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param CreateDate: 策略版本創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param IsDefaultVersion: 是否是正在生效的版本。0表示不是，1表示是
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDefaultVersion: int
        :param Document: 策略語法文本
注意：此欄位可能返回 null，表示取不到有效值。
        :type Document: str
        """
        self.VersionId = None
        self.CreateDate = None
        self.IsDefaultVersion = None
        self.Document = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateDate = params.get("CreateDate")
        self.IsDefaultVersion = params.get("IsDefaultVersion")
        self.Document = params.get("Document")


class PolicyVersionItem(AbstractModel):
    """策略版本清單元素結構

    """

    def __init__(self):
        """
        :param VersionId: 策略版本号
注意：此欄位可能返回 null，表示取不到有效值。
        :type VersionId: int
        :param CreateDate: 策略版本創建時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param IsDefaultVersion: 是否是正在生效的版本。0表示不是，1表示是
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsDefaultVersion: int
        """
        self.VersionId = None
        self.CreateDate = None
        self.IsDefaultVersion = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateDate = params.get("CreateDate")
        self.IsDefaultVersion = params.get("IsDefaultVersion")


class RemoveUserFromGroupRequest(AbstractModel):
    """RemoveUserFromGroup請求參數結構體

    """

    def __init__(self):
        """
        :param Info: 要删除的用戶 UID和用戶組 ID對應數組
        :type Info: list of GroupIdOfUidInfo
        """
        self.Info = None


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self.Info = []
            for item in params.get("Info"):
                obj = GroupIdOfUidInfo()
                obj._deserialize(item)
                self.Info.append(obj)


class RemoveUserFromGroupResponse(AbstractModel):
    """RemoveUserFromGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoleInfo(AbstractModel):
    """角色詳細訊息

    """

    def __init__(self):
        """
        :param RoleId: 角色ID
        :type RoleId: str
        :param RoleName: 角色名稱
        :type RoleName: str
        :param PolicyDocument: 角色的策略文件
        :type PolicyDocument: str
        :param Description: 角色描述
        :type Description: str
        :param AddTime: 角色的創建時間
        :type AddTime: str
        :param UpdateTime: 角色的最近一次時間
        :type UpdateTime: str
        :param ConsoleLogin: 角色是否允許登入
        :type ConsoleLogin: int
        :param RoleType: 角色類型，取user、system或service_linked
注意：此欄位可能返回 null，表示取不到有效值。
        :type RoleType: str
        :param SessionDuration: 有效時間
注意：此欄位可能返回 null，表示取不到有效值。
        :type SessionDuration: int
        :param DeletionTaskId: 服務相關角色删除TaskId
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeletionTaskId: str
        """
        self.RoleId = None
        self.RoleName = None
        self.PolicyDocument = None
        self.Description = None
        self.AddTime = None
        self.UpdateTime = None
        self.ConsoleLogin = None
        self.RoleType = None
        self.SessionDuration = None
        self.DeletionTaskId = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Description = params.get("Description")
        self.AddTime = params.get("AddTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.RoleType = params.get("RoleType")
        self.SessionDuration = params.get("SessionDuration")
        self.DeletionTaskId = params.get("DeletionTaskId")


class SAMLProviderInfo(AbstractModel):
    """SAML身份提供商

    """

    def __init__(self):
        """
        :param Name: SAML身份提供商名稱
        :type Name: str
        :param Description: SAML身份提供商描述
        :type Description: str
        :param CreateTime: SAML身份提供商創建時間
        :type CreateTime: str
        :param ModifyTime: SAML身份提供商上次修改時間
        :type ModifyTime: str
        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")


class SetDefaultPolicyVersionRequest(AbstractModel):
    """SetDefaultPolicyVersion請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param VersionId: 策略版本号
        :type VersionId: int
        """
        self.PolicyId = None
        self.VersionId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.VersionId = params.get("VersionId")


class SetDefaultPolicyVersionResponse(AbstractModel):
    """SetDefaultPolicyVersion返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StrategyInfo(AbstractModel):
    """策略訊息

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID。
        :type PolicyId: int
        :param PolicyName: 策略名稱。
        :type PolicyName: str
        :param AddTime: 策略創建時間。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AddTime: str
        :param Type: 策略類型。1 表示自定義策略，2 表示預設策略。
        :type Type: int
        :param Description: 策略描述。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateMode: 創建來源，1 通過控制台創建, 2 通過策略語法創建。
        :type CreateMode: int
        :param Attachments: 關聯的用戶數
        :type Attachments: int
        :param ServiceType: 策略關聯的産品
注意：此欄位可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param IsAttached: 當需要查詢标記實體是否已經關聯策略時不爲null。0表示未關聯策略，1表示已關聯策略
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsAttached: int
        :param Deactived: 是否已下線
注意：此欄位可能返回 null，表示取不到有效值。
        :type Deactived: int
        :param DeactivedDetail: 已下線産品清單
注意：此欄位可能返回 null，表示取不到有效值。
        :type DeactivedDetail: list of str
        :param IsServiceLinkedPolicy: 是否是服務相關角色策略
注意：此欄位可能返回 null，表示取不到有效值。
        :type IsServiceLinkedPolicy: int
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.Type = None
        self.Description = None
        self.CreateMode = None
        self.Attachments = None
        self.ServiceType = None
        self.IsAttached = None
        self.Deactived = None
        self.DeactivedDetail = None
        self.IsServiceLinkedPolicy = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.Type = params.get("Type")
        self.Description = params.get("Description")
        self.CreateMode = params.get("CreateMode")
        self.Attachments = params.get("Attachments")
        self.ServiceType = params.get("ServiceType")
        self.IsAttached = params.get("IsAttached")
        self.Deactived = params.get("Deactived")
        self.DeactivedDetail = params.get("DeactivedDetail")
        self.IsServiceLinkedPolicy = params.get("IsServiceLinkedPolicy")


class SubAccountInfo(AbstractModel):
    """子用戶訊息

    """

    def __init__(self):
        """
        :param Uin: 子用戶用戶 ID
        :type Uin: int
        :param Name: 子用戶用戶名
        :type Name: str
        :param Uid: 子用戶 UID
        :type Uid: int
        :param Remark: 子用戶備注
        :type Remark: str
        :param ConsoleLogin: 子用戶能否登入控制台
        :type ConsoleLogin: int
        :param PhoneNum: 手機号
        :type PhoneNum: str
        :param CountryCode: 區号
        :type CountryCode: str
        :param Email: 電子信箱
        :type Email: str
        """
        self.Uin = None
        self.Name = None
        self.Uid = None
        self.Remark = None
        self.ConsoleLogin = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Uid = params.get("Uid")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")


class UpdateAssumeRolePolicyRequest(AbstractModel):
    """UpdateAssumeRolePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyDocument: 策略文件，範例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.taifucloud.com","cls.cloud.taifucloud.com"]}}]}，principal用于指定角色的授權對象。獲取該參數可參閱 獲取角色詳情（https://cloud.taifucloud.com/document/product/598/36221） 輸出參數RoleInfo
        :type PolicyDocument: str
        :param RoleId: 角色ID，用于指定角色，入參 RoleId 與 RoleName 二選一
        :type RoleId: str
        :param RoleName: 角色名稱，用于指定角色，入參 RoleId 與 RoleName 二選一
        :type RoleName: str
        """
        self.PolicyDocument = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.PolicyDocument = params.get("PolicyDocument")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")


class UpdateAssumeRolePolicyResponse(AbstractModel):
    """UpdateAssumeRolePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateGroupRequest(AbstractModel):
    """UpdateGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 用戶組 ID
        :type GroupId: int
        :param GroupName: 用戶組名
        :type GroupName: str
        :param Remark: 用戶組描述
        :type Remark: str
        """
        self.GroupId = None
        self.GroupName = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.Remark = params.get("Remark")


class UpdateGroupResponse(AbstractModel):
    """UpdateGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePolicyRequest(AbstractModel):
    """UpdatePolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略ID
        :type PolicyId: int
        :param PolicyName: 策略名
        :type PolicyName: str
        :param Description: 策略描述
        :type Description: str
        :param PolicyDocument: 策略文件，範例：{"version":"2.0","statement":[{"action":"name/sts:AssumeRole","effect":"allow","principal":{"service":["cloudaudit.cloud.taifucloud.com","cls.cloud.taifucloud.com"]}}]}，principal用于指定角色的授權對象。獲取該參數可參閱 獲取角色詳情（https://cloud.taifucloud.com/document/product/598/36221） 輸出參數RoleInfo
        :type PolicyDocument: str
        :param Alias: 預設策略備注
        :type Alias: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.Description = None
        self.PolicyDocument = None
        self.Alias = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.PolicyDocument = params.get("PolicyDocument")
        self.Alias = params.get("Alias")


class UpdatePolicyResponse(AbstractModel):
    """UpdatePolicy返回參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略id
注意：此欄位可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class UpdateRoleConsoleLoginRequest(AbstractModel):
    """UpdateRoleConsoleLogin請求參數結構體

    """

    def __init__(self):
        """
        :param ConsoleLogin: 是否可登入，可登入：1，不可登入：0
        :type ConsoleLogin: int
        :param RoleId: 角色ID
        :type RoleId: int
        :param RoleName: 角色名
        :type RoleName: str
        """
        self.ConsoleLogin = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")


class UpdateRoleConsoleLoginResponse(AbstractModel):
    """UpdateRoleConsoleLogin返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateRoleDescriptionRequest(AbstractModel):
    """UpdateRoleDescription請求參數結構體

    """

    def __init__(self):
        """
        :param Description: 角色描述
        :type Description: str
        :param RoleId: 角色ID，用于指定角色，入參 RoleId 與 RoleName 二選一
        :type RoleId: str
        :param RoleName: 角色名稱，用于指定角色，入參 RoleId 與 RoleName 二選一
        :type RoleName: str
        """
        self.Description = None
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")


class UpdateRoleDescriptionResponse(AbstractModel):
    """UpdateRoleDescription返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateSAMLProviderRequest(AbstractModel):
    """UpdateSAMLProvider請求參數結構體

    """

    def __init__(self):
        """
        :param Name: SAML身份提供商名稱
        :type Name: str
        :param Description: SAML身份提供商描述
        :type Description: str
        :param SAMLMetadataDocument: SAML身份提供商Base64編碼的中繼資料文件
        :type SAMLMetadataDocument: str
        """
        self.Name = None
        self.Description = None
        self.SAMLMetadataDocument = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.SAMLMetadataDocument = params.get("SAMLMetadataDocument")


class UpdateSAMLProviderResponse(AbstractModel):
    """UpdateSAMLProvider返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateUserRequest(AbstractModel):
    """UpdateUser請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 子用戶用戶名
        :type Name: str
        :param Remark: 子用戶備注
        :type Remark: str
        :param ConsoleLogin: 子用戶是否可以登入控制台。傳0子用戶無法登入控制台，傳1子用戶可以登入控制台。
        :type ConsoleLogin: int
        :param Password: 子用戶控制台登入密碼，若未進行密碼規則設置則預設密碼規則爲8位以上同時包含大小寫字母、數字和特殊字元。只有可以登入控制台時才有效，如果傳空并且上面指定允許登入控制台，則自動生成随機密碼，随機密碼規則爲32位包含大小寫字母、數字和特殊字元。
        :type Password: str
        :param NeedResetPassword: 子用戶是否要在下次登入時重置密碼。傳0子用戶下次登入控制台不需重置密碼，傳1子用戶下次登入控制台需要重置密碼。
        :type NeedResetPassword: int
        :param PhoneNum: 手機号
        :type PhoneNum: str
        :param CountryCode: 區号
        :type CountryCode: str
        :param Email: 電子信箱
        :type Email: str
        """
        self.Name = None
        self.Remark = None
        self.ConsoleLogin = None
        self.Password = None
        self.NeedResetPassword = None
        self.PhoneNum = None
        self.CountryCode = None
        self.Email = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.ConsoleLogin = params.get("ConsoleLogin")
        self.Password = params.get("Password")
        self.NeedResetPassword = params.get("NeedResetPassword")
        self.PhoneNum = params.get("PhoneNum")
        self.CountryCode = params.get("CountryCode")
        self.Email = params.get("Email")


class UpdateUserResponse(AbstractModel):
    """UpdateUser返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")