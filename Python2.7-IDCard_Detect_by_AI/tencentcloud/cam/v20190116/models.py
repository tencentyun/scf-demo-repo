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
        :param Password: 子用戶控制台登入密碼，若未進行密碼規則設置則預設密碼規則爲8位以上同時包含大寫小字母、數字和特殊字元。只有可以登入控制台時才有效，如果傳空並且上面指定允許登入控制台，則自動生成随機密碼，随機密碼規則爲32位包含大寫小字母、數字和特殊字元。
        :type Password: str
        :param NeedResetPassword: 子用戶是否要在下次登入時重置密碼。傳0子用戶下次登入控制台不需重置密碼，傳1子用戶下次登入控制台需要重置密碼。
        :type NeedResetPassword: int
        :param PhoneNum: 手機號
        :type PhoneNum: str
        :param CountryCode: 區號
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
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.CreateMode = None
        self.PolicyType = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.CreateMode = params.get("CreateMode")
        self.PolicyType = params.get("PolicyType")


class AttachUserPolicyRequest(AbstractModel):
    """AttachUserPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param AttachUin: 子賬號 uin
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
        :param PolicyDocument: 策略文件
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
        :param PolicyId: 新增策略id
        :type PolicyId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
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


class DeleteUserRequest(AbstractModel):
    """DeleteUser請求參數結構體

    """

    def __init__(self):
        """
        :param Name: 子用戶用戶名
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")


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


class DetachUserPolicyRequest(AbstractModel):
    """DetachUserPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param DetachUin: 子賬號 uin
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
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PolicyName = None
        self.Description = None
        self.Type = None
        self.AddTime = None
        self.UpdateTime = None
        self.PolicyDocument = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.Type = params.get("Type")
        self.AddTime = params.get("AddTime")
        self.UpdateTime = params.get("UpdateTime")
        self.PolicyDocument = params.get("PolicyDocument")
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
        :param PhoneNum: 手機號
        :type PhoneNum: str
        :param CountryCode: 區號
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
        :param PhoneNum: 手機號。
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
        :param TargetGroupId: 用戶組 id
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


class ListAttachedUserPoliciesRequest(AbstractModel):
    """ListAttachedUserPolicies請求參數結構體

    """

    def __init__(self):
        """
        :param TargetUin: 子賬號 uin
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
        :param EntityFilter: 可取值 'All'、'User'、'Group' 和 'Role'，'All' 表示獲取所有實體類型，'User' 表示只獲取子賬號，'Group' 表示只獲取用戶組，'Role' 表示只獲取角色，預設取 'All'
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
        """
        self.Uid = None
        self.Rp = None
        self.Page = None


    def _deserialize(self, params):
        self.Uid = params.get("Uid")
        self.Rp = params.get("Rp")
        self.Page = params.get("Page")


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
        :param Rp: 每頁數量，預設值是 20，必須大於 0 且小於或等於 200
        :type Rp: int
        :param Page: 頁碼，預設值是 1，從 1開始，不能大於 200
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
        """
        self.PolicyId = None
        self.PolicyName = None
        self.AddTime = None
        self.Type = None
        self.Description = None
        self.CreateMode = None
        self.Attachments = None
        self.ServiceType = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.AddTime = params.get("AddTime")
        self.Type = params.get("Type")
        self.Description = params.get("Description")
        self.CreateMode = params.get("CreateMode")
        self.Attachments = params.get("Attachments")
        self.ServiceType = params.get("ServiceType")


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
        :param PhoneNum: 手機號
        :type PhoneNum: str
        :param CountryCode: 區號
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
        :param PolicyId: 策略 id
        :type PolicyId: int
        :param PolicyName: 策略名
        :type PolicyName: str
        :param Description: 策略描述
        :type Description: str
        :param PolicyDocument: 策略文件
        :type PolicyDocument: str
        """
        self.PolicyId = None
        self.PolicyName = None
        self.Description = None
        self.PolicyDocument = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.PolicyName = params.get("PolicyName")
        self.Description = params.get("Description")
        self.PolicyDocument = params.get("PolicyDocument")


class UpdatePolicyResponse(AbstractModel):
    """UpdatePolicy返回參數結構體

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
        :param Password: 子用戶控制台登入密碼，若未進行密碼規則設置則預設密碼規則爲8位以上同時包含大寫小字母、數字和特殊字元。只有可以登入控制台時才有效，如果傳空並且上面指定允許登入控制台，則自動生成随機密碼，随機密碼規則爲32位包含大寫小字母、數字和特殊字元。
        :type Password: str
        :param NeedResetPassword: 子用戶是否要在下次登入時重置密碼。傳0子用戶下次登入控制台不需重置密碼，傳1子用戶下次登入控制台需要重置密碼。
        :type NeedResetPassword: int
        :param PhoneNum: 手機號
        :type PhoneNum: str
        :param CountryCode: 區號
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