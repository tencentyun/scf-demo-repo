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


class AddMemberInfo(AbstractModel):
    """添加的團隊成員訊息

    """

    def __init__(self):
        """
        :param MemberId: 團隊成員 ID。
        :type MemberId: str
        :param Remark: 團隊成員備注。
        :type Remark: str
        """
        self.MemberId = None
        self.Remark = None


    def _deserialize(self, params):
        self.MemberId = params.get("MemberId")
        self.Remark = params.get("Remark")


class AddTeamMemberRequest(AbstractModel):
    """AddTeamMember請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param TeamId: 團隊 ID。
        :type TeamId: str
        :param TeamMembers: 要添加的成員清單，一次最多添加30個成員。
        :type TeamMembers: list of AddMemberInfo
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.TeamMembers = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        if params.get("TeamMembers") is not None:
            self.TeamMembers = []
            for item in params.get("TeamMembers"):
                obj = AddMemberInfo()
                obj._deserialize(item)
                self.TeamMembers.append(obj)
        self.Operator = params.get("Operator")


class AddTeamMemberResponse(AbstractModel):
    """AddTeamMember返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AudioMaterial(AbstractModel):
    """音訊素材訊息

    """

    def __init__(self):
        """
        :param MetaData: 素材元訊息。
        :type MetaData: :class:`taifucloudcloud.cme.v20191029.models.MediaMetaData`
        :param MaterialUrl: 素材媒體文件的 URL 網址。
        :type MaterialUrl: str
        :param CoverUrl: 素材媒體文件的封面圖片網址。
        :type CoverUrl: str
        :param MaterialStatus: 素材狀态。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaterialStatus: :class:`taifucloudcloud.cme.v20191029.models.MaterialStatus`
        """
        self.MetaData = None
        self.MaterialUrl = None
        self.CoverUrl = None
        self.MaterialStatus = None


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        self.MaterialUrl = params.get("MaterialUrl")
        self.CoverUrl = params.get("CoverUrl")
        if params.get("MaterialStatus") is not None:
            self.MaterialStatus = MaterialStatus()
            self.MaterialStatus._deserialize(params.get("MaterialStatus"))


class AudioStreamInfo(AbstractModel):
    """音訊流訊息。

    """

    def __init__(self):
        """
        :param Bitrate: 碼率，單位：bps。
        :type Bitrate: int
        :param SamplingRate: 采樣率，單位：hz。
        :type SamplingRate: int
        :param Codec: 編碼格式。
        :type Codec: str
        """
        self.Bitrate = None
        self.SamplingRate = None
        self.Codec = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.SamplingRate = params.get("SamplingRate")
        self.Codec = params.get("Codec")


class AuthorizationInfo(AbstractModel):
    """資源權限訊息

    """

    def __init__(self):
        """
        :param Authorizee: 被授權者實體。
        :type Authorizee: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param PermissionSet: 詳細授權值。 取值有：
<li>R：可讀，可以浏覽素材，但不能使用該素材（将其添加到 Project），或複制到自己的媒資庫中</li>
<li>X：可用，可以使用該素材（将其添加到 Project），但不能将其複制到自己的媒資庫中，意味着被授權者無法将該資源進一步擴散給其他個人或團隊。</li>
<li>C：可複制，既可以使用該素材（将其添加到 Project），也可以将其複制到自己的媒資庫中。</li>
<li>W：可修改、删除媒資。</li>
        :type PermissionSet: list of str
        """
        self.Authorizee = None
        self.PermissionSet = None


    def _deserialize(self, params):
        if params.get("Authorizee") is not None:
            self.Authorizee = Entity()
            self.Authorizee._deserialize(params.get("Authorizee"))
        self.PermissionSet = params.get("PermissionSet")


class Authorizer(AbstractModel):
    """授權者

    """

    def __init__(self):
        """
        :param Type: 授權者類型，取值有：
<li>PERSON：個人。</li>
<li>TEAM：團隊。</li>
        :type Type: str
        :param Id: Id，當 Type=PERSON，取值爲用戶 Id。當Type=TEAM，取值爲團隊 ID。
        :type Id: str
        """
        self.Type = None
        self.Id = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")


class CMEExportInfo(AbstractModel):
    """雲剪導出訊息。

    """

    def __init__(self):
        """
        :param Owner: 導出的歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Name: 導出的素材名稱，不得超過30個字元。
        :type Name: str
        :param Description: 導出的素材訊息，不得超過50個字元。
        :type Description: str
        :param ClassPath: 導出的素材分類路徑，長度不能超過15字元。
        :type ClassPath: str
        :param TagSet: 導出的素材標簽，單個標簽不得超過10個字元。
        :type TagSet: list of str
        """
        self.Owner = None
        self.Name = None
        self.Description = None
        self.ClassPath = None
        self.TagSet = None


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.ClassPath = params.get("ClassPath")
        self.TagSet = params.get("TagSet")


class ClassInfo(AbstractModel):
    """分類訊息

    """

    def __init__(self):
        """
        :param Owner: 歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param ClassPath: 分類路徑。
        :type ClassPath: str
        """
        self.Owner = None
        self.ClassPath = None


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.ClassPath = params.get("ClassPath")


class CreateClassRequest(AbstractModel):
    """CreateClass請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Owner: 歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param ClassPath: 分類路徑。
        :type ClassPath: str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.ClassPath = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.ClassPath = params.get("ClassPath")
        self.Operator = params.get("Operator")


class CreateClassResponse(AbstractModel):
    """CreateClass返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLinkRequest(AbstractModel):
    """CreateLink請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Type: 連結類型，取值有:
<li>CLASS: 分類連結；</li>
<li> MATERIAL：素材連結。</li>
        :type Type: str
        :param Name: 連結名稱，不能超過30個字元。
        :type Name: str
        :param Owner: 連結歸屬實體。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param DestinationId: 目標資源Id。取值：
<li>當 Type 爲 MATERIAL 時填素材 ID；</li>
<li>當 Type 爲 CLASS 時填寫分類路徑。</li>
        :type DestinationId: str
        :param DestinationOwner: 目標資源歸屬者。
        :type DestinationOwner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param ClassPath: 連結的分類路徑，如填"/a/b"則代表連結屬於該分類路徑，不填則預設爲根路徑。
        :type ClassPath: str
        :param Tags: 連結標簽，單個標簽長度不能超過10，數組長度不能超過10。
        :type Tags: list of str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.Type = None
        self.Name = None
        self.Owner = None
        self.DestinationId = None
        self.DestinationOwner = None
        self.ClassPath = None
        self.Tags = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.DestinationId = params.get("DestinationId")
        if params.get("DestinationOwner") is not None:
            self.DestinationOwner = Entity()
            self.DestinationOwner._deserialize(params.get("DestinationOwner"))
        self.ClassPath = params.get("ClassPath")
        self.Tags = params.get("Tags")
        self.Operator = params.get("Operator")


class CreateLinkResponse(AbstractModel):
    """CreateLink返回參數結構體

    """

    def __init__(self):
        """
        :param MaterialId: 新建連結的素材 Id。
        :type MaterialId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MaterialId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.RequestId = params.get("RequestId")


class CreateProjectRequest(AbstractModel):
    """CreateProject請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Category: 項目類别，取值有：
<li>VIDEO_EDIT：視訊編輯。</li>
        :type Category: str
        :param Name: 項目名稱，不可超過30個字元。
        :type Name: str
        :param AspectRatio: 畫布寬高比，取值有：
<li>16:9；</li>
<li>9:16。</li>
        :type AspectRatio: str
        :param Owner: 歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        """
        self.Platform = None
        self.Category = None
        self.Name = None
        self.AspectRatio = None
        self.Owner = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Category = params.get("Category")
        self.Name = params.get("Name")
        self.AspectRatio = params.get("AspectRatio")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))


class CreateProjectResponse(AbstractModel):
    """CreateProject返回參數結構體

    """

    def __init__(self):
        """
        :param ProjectId: 項目 Id。
        :type ProjectId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RequestId = params.get("RequestId")


class CreateTeamRequest(AbstractModel):
    """CreateTeam請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Name: 團隊名稱，限30個字元。
        :type Name: str
        :param OwnerId: 團隊所有者，指定用戶 ID。
        :type OwnerId: str
        :param OwnerRemark: 團隊所有者的備注，限30個字元。
        :type OwnerRemark: str
        :param TeamId: 自定義團隊 ID。創建後不可修改，限20個英文字元及"-"。同時不能以 cmetid_開頭。不填會生成預設團隊 ID。
        :type TeamId: str
        """
        self.Platform = None
        self.Name = None
        self.OwnerId = None
        self.OwnerRemark = None
        self.TeamId = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.Name = params.get("Name")
        self.OwnerId = params.get("OwnerId")
        self.OwnerRemark = params.get("OwnerRemark")
        self.TeamId = params.get("TeamId")


class CreateTeamResponse(AbstractModel):
    """CreateTeam返回參數結構體

    """

    def __init__(self):
        """
        :param TeamId: 創建的團隊 ID。
        :type TeamId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TeamId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TeamId = params.get("TeamId")
        self.RequestId = params.get("RequestId")


class DeleteClassRequest(AbstractModel):
    """DeleteClass請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Owner: 歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param ClassPath: 分類路徑。
        :type ClassPath: str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.ClassPath = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.ClassPath = params.get("ClassPath")
        self.Operator = params.get("Operator")


class DeleteClassResponse(AbstractModel):
    """DeleteClass返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoginStatusRequest(AbstractModel):
    """DeleteLoginStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param UserIds: 用戶 Id 清單，N 從 0 開始取值，最大 19。
        :type UserIds: list of str
        """
        self.Platform = None
        self.UserIds = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.UserIds = params.get("UserIds")


class DeleteLoginStatusResponse(AbstractModel):
    """DeleteLoginStatus返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMaterialRequest(AbstractModel):
    """DeleteMaterial請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.MaterialId = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.MaterialId = params.get("MaterialId")
        self.Operator = params.get("Operator")


class DeleteMaterialResponse(AbstractModel):
    """DeleteMaterial返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteProjectRequest(AbstractModel):
    """DeleteProject請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param ProjectId: 項目 Id。
        :type ProjectId: str
        """
        self.Platform = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")


class DeleteProjectResponse(AbstractModel):
    """DeleteProject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTeamMembersRequest(AbstractModel):
    """DeleteTeamMembers請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param TeamId: 團隊 ID。
        :type TeamId: str
        :param MemberIds: 要删除的成員清單。
        :type MemberIds: list of str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.MemberIds = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        self.MemberIds = params.get("MemberIds")
        self.Operator = params.get("Operator")


class DeleteTeamMembersResponse(AbstractModel):
    """DeleteTeamMembers返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTeamRequest(AbstractModel):
    """DeleteTeam請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問平台。
        :type Platform: str
        :param TeamId: 要删除的團隊  ID。
        :type TeamId: str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        self.Operator = params.get("Operator")


class DeleteTeamResponse(AbstractModel):
    """DeleteTeam返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeClassRequest(AbstractModel):
    """DescribeClass請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Owner: 歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Operator = params.get("Operator")


class DescribeClassResponse(AbstractModel):
    """DescribeClass返回參數結構體

    """

    def __init__(self):
        """
        :param ClassInfoSet: 分類訊息清單。
        :type ClassInfoSet: list of ClassInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ClassInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClassInfoSet") is not None:
            self.ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = ClassInfo()
                obj._deserialize(item)
                self.ClassInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeJoinTeamsRequest(AbstractModel):
    """DescribeJoinTeams請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param MemberId: 團隊成員　ID。
        :type MemberId: str
        :param Offset: 分頁偏移量，預設值：0
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：30，最大值：30。
        :type Limit: int
        """
        self.Platform = None
        self.MemberId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.MemberId = params.get("MemberId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeJoinTeamsResponse(AbstractModel):
    """DescribeJoinTeams返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的記錄總數。
        :type TotalCount: int
        :param TeamSet: 團隊清單
        :type TeamSet: list of JoinTeamInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TeamSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TeamSet") is not None:
            self.TeamSet = []
            for item in params.get("TeamSet"):
                obj = JoinTeamInfo()
                obj._deserialize(item)
                self.TeamSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLoginStatusRequest(AbstractModel):
    """DescribeLoginStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param UserIds: 用戶 Id 清單，N 從 0 開始取值，最大 19。
        :type UserIds: list of str
        """
        self.Platform = None
        self.UserIds = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.UserIds = params.get("UserIds")


class DescribeLoginStatusResponse(AbstractModel):
    """DescribeLoginStatus返回參數結構體

    """

    def __init__(self):
        """
        :param LoginStatusInfoSet: 用戶登入狀态清單。
        :type LoginStatusInfoSet: list of LoginStatusInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.LoginStatusInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoginStatusInfoSet") is not None:
            self.LoginStatusInfoSet = []
            for item in params.get("LoginStatusInfoSet"):
                obj = LoginStatusInfo()
                obj._deserialize(item)
                self.LoginStatusInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMaterialsRequest(AbstractModel):
    """DescribeMaterials請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param MaterialIds: 素材 ID 清單，N 從 0 開始取值，最大 19。
        :type MaterialIds: list of str
        :param Sort: 清單排序，支援下列排序欄位：
<li>CreateTime：創建時間；</li>
<li>UpdateTime：更新時間。</li>
        :type Sort: :class:`taifucloudcloud.cme.v20191029.models.SortBy`
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.MaterialIds = None
        self.Sort = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.MaterialIds = params.get("MaterialIds")
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        self.Operator = params.get("Operator")


class DescribeMaterialsResponse(AbstractModel):
    """DescribeMaterials返回參數結構體

    """

    def __init__(self):
        """
        :param MaterialInfoSet: 素材清單訊息。
        :type MaterialInfoSet: list of MaterialInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MaterialInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MaterialInfoSet") is not None:
            self.MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self.MaterialInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param ProjectIds: 項目 Id 清單，N 從 0 開始取值，最大 19。
        :type ProjectIds: list of str
        :param AspectRatioSet: 畫布寬高比集合。
        :type AspectRatioSet: list of str
        :param CategorySet: 項目類别集合。
        :type CategorySet: list of str
        :param Sort: 清單排序，支援下列排序欄位：
<li>CreateTime：創建時間；</li>
<li>UpdateTime：更新時間。</li>
        :type Sort: :class:`taifucloudcloud.cme.v20191029.models.SortBy`
        :param Owner: 項目歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Offset: 分頁返回的起始偏移量，預設值：0。
        :type Offset: int
        :param Limit: 分頁返回的記錄條數，預設值：10。
        :type Limit: int
        """
        self.Platform = None
        self.ProjectIds = None
        self.AspectRatioSet = None
        self.CategorySet = None
        self.Sort = None
        self.Owner = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectIds = params.get("ProjectIds")
        self.AspectRatioSet = params.get("AspectRatioSet")
        self.CategorySet = params.get("CategorySet")
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的記錄總數。
        :type TotalCount: int
        :param ProjectInfoSet: 項目訊息清單。
        :type ProjectInfoSet: list of ProjectInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProjectInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProjectInfoSet") is not None:
            self.ProjectInfoSet = []
            for item in params.get("ProjectInfoSet"):
                obj = ProjectInfo()
                obj._deserialize(item)
                self.ProjectInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceAuthorizationRequest(AbstractModel):
    """DescribeResourceAuthorization請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Owner: 歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Resource: 資源。
        :type Resource: :class:`taifucloudcloud.cme.v20191029.models.Resource`
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.Resource = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        if params.get("Resource") is not None:
            self.Resource = Resource()
            self.Resource._deserialize(params.get("Resource"))
        self.Operator = params.get("Operator")


class DescribeResourceAuthorizationResponse(AbstractModel):
    """DescribeResourceAuthorization返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的資源授權記錄總數。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param AuthorizationInfoSet: 授權訊息清單。
        :type AuthorizationInfoSet: list of AuthorizationInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AuthorizationInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AuthorizationInfoSet") is not None:
            self.AuthorizationInfoSet = []
            for item in params.get("AuthorizationInfoSet"):
                obj = AuthorizationInfo()
                obj._deserialize(item)
                self.AuthorizationInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSharedSpaceRequest(AbstractModel):
    """DescribeSharedSpace請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Authorizee: 被授權目標實體。
        :type Authorizee: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.Authorizee = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Authorizee") is not None:
            self.Authorizee = Entity()
            self.Authorizee._deserialize(params.get("Authorizee"))
        self.Operator = params.get("Operator")


class DescribeSharedSpaceResponse(AbstractModel):
    """DescribeSharedSpace返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 查詢到的共享空間總數。
        :type TotalCount: int
        :param AuthorizerSet: 各個共享空間對應的授權者訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AuthorizerSet: list of Authorizer
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AuthorizerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AuthorizerSet") is not None:
            self.AuthorizerSet = []
            for item in params.get("AuthorizerSet"):
                obj = Authorizer()
                obj._deserialize(item)
                self.AuthorizerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param TaskId: 任務 Id。
        :type TaskId: str
        """
        self.Platform = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TaskId = params.get("TaskId")


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回參數結構體

    """

    def __init__(self):
        """
        :param Status: 任務狀态，取值有：
<li>PROCESSING：處理中：</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失敗。</li>
        :type Status: str
        :param Progress: 任務進度，取值爲：0~100。
        :type Progress: int
        :param ErrCode: 錯誤碼。
<li>0：成功；</li>
<li>其他值：失敗。</li>
        :type ErrCode: int
        :param ErrMsg: 錯誤訊息。
        :type ErrMsg: str
        :param TaskType: 任務類型，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：視訊編輯項目導出。</li>
        :type TaskType: str
        :param VideoEditProjectOutput: 導出項目輸出訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoEditProjectOutput: :class:`taifucloudcloud.cme.v20191029.models.VideoEditProjectOutput`
        :param CreateTime: 創建時間，格式按照 ISO 8601 標準表示。
        :type CreateTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Progress = None
        self.ErrCode = None
        self.ErrMsg = None
        self.TaskType = None
        self.VideoEditProjectOutput = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        self.TaskType = params.get("TaskType")
        if params.get("VideoEditProjectOutput") is not None:
            self.VideoEditProjectOutput = VideoEditProjectOutput()
            self.VideoEditProjectOutput._deserialize(params.get("VideoEditProjectOutput"))
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param ProjectId: 項目 Id。
        :type ProjectId: str
        :param TaskTypeSet: 任務類型集合，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：視訊編輯項目導出。</li>
        :type TaskTypeSet: list of str
        :param StatusSet: 任務狀态集合，取值有：
<li>PROCESSING：處理中；</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失敗。</li>
        :type StatusSet: list of str
        :param Offset: 分頁返回的起始偏移量，預設值：0。
        :type Offset: int
        :param Limit: 分頁返回的記錄條數，預設值：10。
        :type Limit: int
        """
        self.Platform = None
        self.ProjectId = None
        self.TaskTypeSet = None
        self.StatusSet = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.TaskTypeSet = params.get("TaskTypeSet")
        self.StatusSet = params.get("StatusSet")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合搜索條件的記錄總數。
        :type TotalCount: int
        :param TaskBaseInfoSet: 任務基礎訊息清單。
        :type TaskBaseInfoSet: list of TaskBaseInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskBaseInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskBaseInfoSet") is not None:
            self.TaskBaseInfoSet = []
            for item in params.get("TaskBaseInfoSet"):
                obj = TaskBaseInfo()
                obj._deserialize(item)
                self.TaskBaseInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTeamMembersRequest(AbstractModel):
    """DescribeTeamMembers請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param TeamId: 團隊 ID。
        :type TeamId: str
        :param MemberIds: 成員 ID 清單，限指定30個指定成員。
        :type MemberIds: list of str
        :param Offset: 分頁偏移量，預設值：0
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：30，最大值：30。
        :type Limit: int
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.MemberIds = None
        self.Offset = None
        self.Limit = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        self.MemberIds = params.get("MemberIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operator = params.get("Operator")


class DescribeTeamMembersResponse(AbstractModel):
    """DescribeTeamMembers返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的記錄總數。
        :type TotalCount: int
        :param MemberSet: 團隊成員清單。
        :type MemberSet: list of TeamMemberInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MemberSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MemberSet") is not None:
            self.MemberSet = []
            for item in params.get("MemberSet"):
                obj = TeamMemberInfo()
                obj._deserialize(item)
                self.MemberSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTeamsRequest(AbstractModel):
    """DescribeTeams請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param TeamIds: 團隊 ID 清單，限30個。
        :type TeamIds: list of str
        """
        self.Platform = None
        self.TeamIds = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamIds = params.get("TeamIds")


class DescribeTeamsResponse(AbstractModel):
    """DescribeTeams返回參數結構體

    """

    def __init__(self):
        """
        :param TeamSet: 團隊清單。
        :type TeamSet: list of TeamInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TeamSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TeamSet") is not None:
            self.TeamSet = []
            for item in params.get("TeamSet"):
                obj = TeamInfo()
                obj._deserialize(item)
                self.TeamSet.append(obj)
        self.RequestId = params.get("RequestId")


class Entity(AbstractModel):
    """用於描述資源的歸屬實體。

    """

    def __init__(self):
        """
        :param Type: 類型，取值有：
<li>PERSON：個人。</li>
<li>TEAM：團隊。</li>
        :type Type: str
        :param Id: Id，當 Type=PERSON，取值爲用戶 Id，當 Type=TEAM，取值爲團隊 Id。
        :type Id: str
        """
        self.Type = None
        self.Id = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")


class ExportVideoEditProjectRequest(AbstractModel):
    """ExportVideoEditProject請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param ProjectId: 項目 Id。
        :type ProjectId: str
        :param Definition: 導出範本 Id，目前不支援自定義創建，只支援下面的預置範本 Id。
<li>10：分辨率爲 480P，輸出視訊格式爲 MP4；</li>
<li>11：分辨率爲 720P，輸出視訊格式爲 MP4；</li>
<li>12：分辨率爲 1080P，輸出視訊格式爲 MP4。</li>
        :type Definition: int
        :param ExportDestination: 導出目標。
<li>CME：雲剪，即導出爲雲剪素材；</li>
<li>VOD：雲點播，即導出爲雲點播媒資。</li>
        :type ExportDestination: str
        :param CMEExportInfo: 導出的雲剪素材訊息。指定 ExportDestination = CME 時有效。
        :type CMEExportInfo: :class:`taifucloudcloud.cme.v20191029.models.CMEExportInfo`
        :param VODExportInfo: 導出的雲點播媒資訊息。指定 ExportDestination = VOD 時有效。
        :type VODExportInfo: :class:`taifucloudcloud.cme.v20191029.models.VODExportInfo`
        """
        self.Platform = None
        self.ProjectId = None
        self.Definition = None
        self.ExportDestination = None
        self.CMEExportInfo = None
        self.VODExportInfo = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Definition = params.get("Definition")
        self.ExportDestination = params.get("ExportDestination")
        if params.get("CMEExportInfo") is not None:
            self.CMEExportInfo = CMEExportInfo()
            self.CMEExportInfo._deserialize(params.get("CMEExportInfo"))
        if params.get("VODExportInfo") is not None:
            self.VODExportInfo = VODExportInfo()
            self.VODExportInfo._deserialize(params.get("VODExportInfo"))


class ExportVideoEditProjectResponse(AbstractModel):
    """ExportVideoEditProject返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務 Id。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class FlattenListMediaRequest(AbstractModel):
    """FlattenListMedia請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param ClassPath: 素材分類路徑，例如填寫"/a/b"，則代表平鋪該分類路徑下及其子分類路徑下的素材訊息。
        :type ClassPath: str
        :param Owner: 素材路徑的歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：50。
        :type Limit: int
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.ClassPath = None
        self.Owner = None
        self.Offset = None
        self.Limit = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ClassPath = params.get("ClassPath")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operator = params.get("Operator")


class FlattenListMediaResponse(AbstractModel):
    """FlattenListMedia返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的記錄總數。
        :type TotalCount: int
        :param MaterialInfoSet: 該分類路徑下及其子分類下的所有素材。
        :type MaterialInfoSet: list of MaterialInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MaterialInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MaterialInfoSet") is not None:
            self.MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self.MaterialInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class GrantResourceAuthorizationRequest(AbstractModel):
    """GrantResourceAuthorization請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Owner: 資源所屬實體。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Resources: 被授權資源。
        :type Resources: list of Resource
        :param Authorizees: 被授權目標實體。
        :type Authorizees: list of Entity
        :param Permissions: 詳細授權值。 取值有：
<li>R：可讀，可以浏覽素材，但不能使用該素材（将其添加到 Project），或複制到自己的媒資庫中</li>
<li>X：可用，可以使用該素材（将其添加到 Project），但不能将其複制到自己的媒資庫中，意味着被授權者無法将該資源進一步擴散給其他個人或團隊。</li>
<li>C：可複制，既可以使用該素材（将其添加到 Project），也可以将其複制到自己的媒資庫中。</li>
<li>W：可修改、删除媒資。</li>
        :type Permissions: list of str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.Resources = None
        self.Authorizees = None
        self.Permissions = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        if params.get("Authorizees") is not None:
            self.Authorizees = []
            for item in params.get("Authorizees"):
                obj = Entity()
                obj._deserialize(item)
                self.Authorizees.append(obj)
        self.Permissions = params.get("Permissions")
        self.Operator = params.get("Operator")


class GrantResourceAuthorizationResponse(AbstractModel):
    """GrantResourceAuthorization返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ImageMaterial(AbstractModel):
    """圖片素材訊息

    """

    def __init__(self):
        """
        :param Height: 圖片高度，單位：px。
        :type Height: int
        :param Width: 圖片寬度，單位：px。
        :type Width: int
        :param MaterialUrl: 素材媒體文件的 URL 網址。
        :type MaterialUrl: str
        :param Size: 圖片大小，單位：位元。
        :type Size: int
        """
        self.Height = None
        self.Width = None
        self.MaterialUrl = None
        self.Size = None


    def _deserialize(self, params):
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.MaterialUrl = params.get("MaterialUrl")
        self.Size = params.get("Size")


class ImportMaterialRequest(AbstractModel):
    """ImportMaterial請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param VodFileId: 雲點播媒資 FileId。
        :type VodFileId: str
        :param Owner: 素材歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Name: 素材名稱，不能超過30個字元。
        :type Name: str
        :param ClassPath: 素材分類路徑，形如："/a/b"，層級數不能超過10，每個層級長度不能超過15字元。若不填則預設爲根路徑。
        :type ClassPath: str
        :param Tags: 素材標簽，單個標簽長度不能超過10，數組長度不能超過10。
        :type Tags: list of str
        :param PreProcessDefinition: 素材預處理任務範本 ID。取值：
<li>10：進行編輯預處理。</li>
        :type PreProcessDefinition: int
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.VodFileId = None
        self.Owner = None
        self.Name = None
        self.ClassPath = None
        self.Tags = None
        self.PreProcessDefinition = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.VodFileId = params.get("VodFileId")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.ClassPath = params.get("ClassPath")
        self.Tags = params.get("Tags")
        self.PreProcessDefinition = params.get("PreProcessDefinition")
        self.Operator = params.get("Operator")


class ImportMaterialResponse(AbstractModel):
    """ImportMaterial返回參數結構體

    """

    def __init__(self):
        """
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param PreProcessTaskId: 素材預處理任務 ID，如果未指定發起預處理任務則爲空。
        :type PreProcessTaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MaterialId = None
        self.PreProcessTaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.PreProcessTaskId = params.get("PreProcessTaskId")
        self.RequestId = params.get("RequestId")


class ImportMediaToProjectRequest(AbstractModel):
    """ImportMediaToProject請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param ProjectId: 項目 Id。
        :type ProjectId: str
        :param VodFileId: 雲點播媒資 FileId。
        :type VodFileId: str
        :param Name: 素材名稱，不能超過30個字元。
        :type Name: str
        :param PreProcessDefinition: 素材預處理任務範本 ID，取值：
<li>10：進行編輯預處理。</li>
注意：如果填0則不進行處理。
        :type PreProcessDefinition: int
        """
        self.Platform = None
        self.ProjectId = None
        self.VodFileId = None
        self.Name = None
        self.PreProcessDefinition = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.VodFileId = params.get("VodFileId")
        self.Name = params.get("Name")
        self.PreProcessDefinition = params.get("PreProcessDefinition")


class ImportMediaToProjectResponse(AbstractModel):
    """ImportMediaToProject返回參數結構體

    """

    def __init__(self):
        """
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param TaskId: 素材預處理任務 ID，如果未指定發起預處理任務則爲空。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MaterialId = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class IntegerRange(AbstractModel):
    """整型範圍

    """

    def __init__(self):
        """
        :param LowerBound: 按整形代表值的下限檢索。
        :type LowerBound: int
        :param UpperBound: 按整形代表值的上限檢索。
        :type UpperBound: int
        """
        self.LowerBound = None
        self.UpperBound = None


    def _deserialize(self, params):
        self.LowerBound = params.get("LowerBound")
        self.UpperBound = params.get("UpperBound")


class JoinTeamInfo(AbstractModel):
    """加入的團隊訊息

    """

    def __init__(self):
        """
        :param TeamId: 團隊 ID。
        :type TeamId: str
        :param Name: 團隊名稱。
        :type Name: str
        :param MemberCount: 團隊成員個數
        :type MemberCount: int
        :param Role: 成員在團隊中的角色，取值有：
<li>Owner：團隊所有者，添加團隊成員及修改團隊成員解決時不能填此角色；</li>
<li>Admin：團隊管理員；</li>
<li>Member：普通成員。</li>
        :type Role: str
        """
        self.TeamId = None
        self.Name = None
        self.MemberCount = None
        self.Role = None


    def _deserialize(self, params):
        self.TeamId = params.get("TeamId")
        self.Name = params.get("Name")
        self.MemberCount = params.get("MemberCount")
        self.Role = params.get("Role")


class LinkMaterial(AbstractModel):
    """連結類型的素材訊息

    """

    def __init__(self):
        """
        :param LinkType: 連結類型取值:
<li>CLASS: 分類連結;</li>
<li> MATERIAL：素材連結。</li>
        :type LinkType: str
        :param LinkStatus: 連結狀态取值：
<li> Normal：正常 ；</li>
<li>NotFound：連結目標不存在；</li> <li>Forbidden：無權限。</li>
        :type LinkStatus: str
        :param LinkMaterialInfo: 素材連結詳細訊息，當LinkType="MATERIAL"時有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type LinkMaterialInfo: :class:`taifucloudcloud.cme.v20191029.models.LinkMaterialInfo`
        :param LinkClassInfo: 分類連結目標訊息，當LinkType=“CLASS”時有值。
注意：此欄位可能返回 null，表示取不到有效值。
        :type LinkClassInfo: :class:`taifucloudcloud.cme.v20191029.models.ClassInfo`
        """
        self.LinkType = None
        self.LinkStatus = None
        self.LinkMaterialInfo = None
        self.LinkClassInfo = None


    def _deserialize(self, params):
        self.LinkType = params.get("LinkType")
        self.LinkStatus = params.get("LinkStatus")
        if params.get("LinkMaterialInfo") is not None:
            self.LinkMaterialInfo = LinkMaterialInfo()
            self.LinkMaterialInfo._deserialize(params.get("LinkMaterialInfo"))
        if params.get("LinkClassInfo") is not None:
            self.LinkClassInfo = ClassInfo()
            self.LinkClassInfo._deserialize(params.get("LinkClassInfo"))


class LinkMaterialInfo(AbstractModel):
    """連結素材訊息

    """

    def __init__(self):
        """
        :param BasicInfo: 素材基本訊息。
        :type BasicInfo: :class:`taifucloudcloud.cme.v20191029.models.MaterialBasicInfo`
        :param VideoMaterial: 視訊素材訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoMaterial: :class:`taifucloudcloud.cme.v20191029.models.VideoMaterial`
        :param AudioMaterial: 音訊素材訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AudioMaterial: :class:`taifucloudcloud.cme.v20191029.models.AudioMaterial`
        :param ImageMaterial: 圖片素材訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageMaterial: :class:`taifucloudcloud.cme.v20191029.models.ImageMaterial`
        """
        self.BasicInfo = None
        self.VideoMaterial = None
        self.AudioMaterial = None
        self.ImageMaterial = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = MaterialBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("VideoMaterial") is not None:
            self.VideoMaterial = VideoMaterial()
            self.VideoMaterial._deserialize(params.get("VideoMaterial"))
        if params.get("AudioMaterial") is not None:
            self.AudioMaterial = AudioMaterial()
            self.AudioMaterial._deserialize(params.get("AudioMaterial"))
        if params.get("ImageMaterial") is not None:
            self.ImageMaterial = ImageMaterial()
            self.ImageMaterial._deserialize(params.get("ImageMaterial"))


class ListMediaRequest(AbstractModel):
    """ListMedia請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param ClassPath: 素材分類路徑，例如填寫"/a/b"，則代表浏覽該分類路徑下的素材和子分類訊息。
        :type ClassPath: str
        :param Owner: 素材和分類的歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Offset: 分頁偏移量，預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：10，最大值：50。
        :type Limit: int
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.ClassPath = None
        self.Owner = None
        self.Offset = None
        self.Limit = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ClassPath = params.get("ClassPath")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operator = params.get("Operator")


class ListMediaResponse(AbstractModel):
    """ListMedia返回參數結構體

    """

    def __init__(self):
        """
        :param MaterialTotalCount: 符合條件的素材記錄總數。
        :type MaterialTotalCount: int
        :param MaterialInfoSet: 浏覽分類路徑下的素材清單訊息。
        :type MaterialInfoSet: list of MaterialInfo
        :param ClassInfoSet: 浏覽分類路徑下的一級子類。
        :type ClassInfoSet: list of ClassInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MaterialTotalCount = None
        self.MaterialInfoSet = None
        self.ClassInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaterialTotalCount = params.get("MaterialTotalCount")
        if params.get("MaterialInfoSet") is not None:
            self.MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self.MaterialInfoSet.append(obj)
        if params.get("ClassInfoSet") is not None:
            self.ClassInfoSet = []
            for item in params.get("ClassInfoSet"):
                obj = ClassInfo()
                obj._deserialize(item)
                self.ClassInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class LoginStatusInfo(AbstractModel):
    """登入态訊息

    """

    def __init__(self):
        """
        :param UserId: 用戶 Id。
        :type UserId: str
        :param Status: 用戶登入狀态。
<li>Online：在線；</li>
<li>Offline：離線。</li>
        :type Status: str
        """
        self.UserId = None
        self.Status = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Status = params.get("Status")


class MaterialBasicInfo(AbstractModel):
    """素材基本訊息。

    """

    def __init__(self):
        """
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param MaterialType: 素材類型，取值爲：音訊（AUDIO）、視訊（VIDEO）、圖片（IMAGE）、連結（LINK）、字幕 （SUBTITLE）、轉場（TRANSITION）、濾鏡（FILTER）、文本文字（TEXT）、圖文動效（TEXT_IMAGE）。
        :type MaterialType: str
        :param Owner: 素材歸屬實體。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Name: 素材名稱。
        :type Name: str
        :param CreateTime: 素材文件的創建時間，使用 ISO 日期格式。
        :type CreateTime: str
        :param UpdateTime: 素材文件的最近更新時間（如修改視訊屬性、發起視訊處理等會觸發更新媒體文件訊息的操作），使用 ISO 日期格式。
        :type UpdateTime: str
        :param ClassPath: 素材的分類目錄路徑。
        :type ClassPath: str
        :param TagSet: 素材標簽訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagSet: list of str
        :param PreviewUrl: 素材媒體文件的預覽圖。
注意：此欄位可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        """
        self.MaterialId = None
        self.MaterialType = None
        self.Owner = None
        self.Name = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ClassPath = None
        self.TagSet = None
        self.PreviewUrl = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.MaterialType = params.get("MaterialType")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ClassPath = params.get("ClassPath")
        self.TagSet = params.get("TagSet")
        self.PreviewUrl = params.get("PreviewUrl")


class MaterialInfo(AbstractModel):
    """素材詳情訊息

    """

    def __init__(self):
        """
        :param BasicInfo: 素材基本訊息。
        :type BasicInfo: :class:`taifucloudcloud.cme.v20191029.models.MaterialBasicInfo`
        :param VideoMaterial: 視訊素材訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type VideoMaterial: :class:`taifucloudcloud.cme.v20191029.models.VideoMaterial`
        :param AudioMaterial: 音訊素材訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type AudioMaterial: :class:`taifucloudcloud.cme.v20191029.models.AudioMaterial`
        :param ImageMaterial: 圖片素材訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ImageMaterial: :class:`taifucloudcloud.cme.v20191029.models.ImageMaterial`
        :param LinkMaterial: 連結素材訊息。
注意：此欄位可能返回 null，表示取不到有效值。
        :type LinkMaterial: :class:`taifucloudcloud.cme.v20191029.models.LinkMaterial`
        """
        self.BasicInfo = None
        self.VideoMaterial = None
        self.AudioMaterial = None
        self.ImageMaterial = None
        self.LinkMaterial = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = MaterialBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("VideoMaterial") is not None:
            self.VideoMaterial = VideoMaterial()
            self.VideoMaterial._deserialize(params.get("VideoMaterial"))
        if params.get("AudioMaterial") is not None:
            self.AudioMaterial = AudioMaterial()
            self.AudioMaterial._deserialize(params.get("AudioMaterial"))
        if params.get("ImageMaterial") is not None:
            self.ImageMaterial = ImageMaterial()
            self.ImageMaterial._deserialize(params.get("ImageMaterial"))
        if params.get("LinkMaterial") is not None:
            self.LinkMaterial = LinkMaterial()
            self.LinkMaterial._deserialize(params.get("LinkMaterial"))


class MaterialStatus(AbstractModel):
    """素材的狀态，目前僅包含素材編輯可用狀态。

    """

    def __init__(self):
        """
        :param EditorUsableStatus: 素材編輯可用狀态，取值有：
<li>NORMAL：正常，可直接用於編輯；</li>
<li>ABNORMAL : 異常，不可用於編輯；</li>
<li>PROCESSING：處理中，暫不可用於編輯。</li>
        :type EditorUsableStatus: str
        """
        self.EditorUsableStatus = None


    def _deserialize(self, params):
        self.EditorUsableStatus = params.get("EditorUsableStatus")


class MediaImageSpriteInfo(AbstractModel):
    """雪碧圖

    """

    def __init__(self):
        """
        :param Height: 雪碧圖小圖的高度。
        :type Height: int
        :param Width: 雪碧圖小圖的寬度。
        :type Width: int
        :param TotalCount: 雪碧圖小圖的總數量。
        :type TotalCount: int
        :param ImageUrlSet: 截取雪碧圖輸出的網址。
        :type ImageUrlSet: list of str
        :param WebVttUrl: 雪碧圖子圖位置與時間關系的 WebVtt 文件網址。WebVtt 文件表明了各個雪碧圖小圖對應的時間點，以及在雪碧大圖裏的坐標位置，一般被播放器用於實現預覽。
        :type WebVttUrl: str
        """
        self.Height = None
        self.Width = None
        self.TotalCount = None
        self.ImageUrlSet = None
        self.WebVttUrl = None


    def _deserialize(self, params):
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.TotalCount = params.get("TotalCount")
        self.ImageUrlSet = params.get("ImageUrlSet")
        self.WebVttUrl = params.get("WebVttUrl")


class MediaMetaData(AbstractModel):
    """文件元訊息。

    """

    def __init__(self):
        """
        :param Size: 大小。
        :type Size: int
        :param Container: 容器類型。
        :type Container: str
        :param Bitrate: 視訊流碼率平均值與音訊流碼率平均值之和，單位：bps。
        :type Bitrate: int
        :param Height: 視訊流高度的最大值，單位：px。
        :type Height: int
        :param Width: 視訊流寬度的最大值，單位：px。
        :type Width: int
        :param Duration: 時長，單位：秒。
        :type Duration: float
        :param Rotate: 視訊拍攝時的選擇角度，單位：度
        :type Rotate: int
        :param VideoStreamInfoSet: 視訊流訊息。
        :type VideoStreamInfoSet: list of VideoStreamInfo
        :param AudioStreamInfoSet: 音訊流訊息。
        :type AudioStreamInfoSet: list of AudioStreamInfo
        """
        self.Size = None
        self.Container = None
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Duration = None
        self.Rotate = None
        self.VideoStreamInfoSet = None
        self.AudioStreamInfoSet = None


    def _deserialize(self, params):
        self.Size = params.get("Size")
        self.Container = params.get("Container")
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Duration = params.get("Duration")
        self.Rotate = params.get("Rotate")
        if params.get("VideoStreamInfoSet") is not None:
            self.VideoStreamInfoSet = []
            for item in params.get("VideoStreamInfoSet"):
                obj = VideoStreamInfo()
                obj._deserialize(item)
                self.VideoStreamInfoSet.append(obj)
        if params.get("AudioStreamInfoSet") is not None:
            self.AudioStreamInfoSet = []
            for item in params.get("AudioStreamInfoSet"):
                obj = AudioStreamInfo()
                obj._deserialize(item)
                self.AudioStreamInfoSet.append(obj)


class ModifyMaterialRequest(AbstractModel):
    """ModifyMaterial請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param MaterialId: 素材 Id。
        :type MaterialId: str
        :param Owner: 素材歸屬。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Name: 素材名稱，不能超過30個字元。
        :type Name: str
        :param Tags: 素材標簽，單個標簽長度不能超過10個字元，數組長度不能超過10。
        :type Tags: list of str
        :param ClassPath: 素材分類路徑，例如填寫"/a/b"，則代表該素材儲存的路徑爲"/a/b"。
        :type ClassPath: str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.MaterialId = None
        self.Owner = None
        self.Name = None
        self.Tags = None
        self.ClassPath = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.MaterialId = params.get("MaterialId")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.Name = params.get("Name")
        self.Tags = params.get("Tags")
        self.ClassPath = params.get("ClassPath")
        self.Operator = params.get("Operator")


class ModifyMaterialResponse(AbstractModel):
    """ModifyMaterial返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProjectRequest(AbstractModel):
    """ModifyProject請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param ProjectId: 項目 Id。
        :type ProjectId: str
        :param Name: 項目名稱，不可超過30個字元。
        :type Name: str
        :param AspectRatio: 畫布寬高比，取值有：
<li>16:9；</li>
<li>9:16。</li>
        :type AspectRatio: str
        :param Owner: 歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        """
        self.Platform = None
        self.ProjectId = None
        self.Name = None
        self.AspectRatio = None
        self.Owner = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.AspectRatio = params.get("AspectRatio")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))


class ModifyProjectResponse(AbstractModel):
    """ModifyProject返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTeamMemberRequest(AbstractModel):
    """ModifyTeamMember請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param TeamId: 團隊 ID。
        :type TeamId: str
        :param MemberId: 團隊成員 ID。
        :type MemberId: str
        :param Remark: 成員備注，允許設置備注爲空，不爲空時長度不能超過15個字元。
        :type Remark: str
        :param Role: 成員角色，取值：
<li>Admin：團隊管理員；</li>
<li>Member：普通成員。</li>
        :type Role: str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.MemberId = None
        self.Remark = None
        self.Role = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        self.MemberId = params.get("MemberId")
        self.Remark = params.get("Remark")
        self.Role = params.get("Role")
        self.Operator = params.get("Operator")


class ModifyTeamMemberResponse(AbstractModel):
    """ModifyTeamMember返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTeamRequest(AbstractModel):
    """ModifyTeam請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param TeamId: 團隊 ID。
        :type TeamId: str
        :param Name: 團隊名稱，不能超過 30 個字元。
        :type Name: str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.TeamId = None
        self.Name = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.TeamId = params.get("TeamId")
        self.Name = params.get("Name")
        self.Operator = params.get("Operator")


class ModifyTeamResponse(AbstractModel):
    """ModifyTeam返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MoveClassRequest(AbstractModel):
    """MoveClass請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Owner: 歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param SourceClassPath: 源分類路徑。
        :type SourceClassPath: str
        :param DestinationClassPath: 目標分類路徑。
        :type DestinationClassPath: str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.SourceClassPath = None
        self.DestinationClassPath = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.SourceClassPath = params.get("SourceClassPath")
        self.DestinationClassPath = params.get("DestinationClassPath")
        self.Operator = params.get("Operator")


class MoveClassResponse(AbstractModel):
    """MoveClass返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProjectInfo(AbstractModel):
    """項目訊息。

    """

    def __init__(self):
        """
        :param ProjectId: 項目 Id。
        :type ProjectId: str
        :param Name: 項目名稱。
        :type Name: str
        :param AspectRatio: 畫布寬高比。
        :type AspectRatio: str
        :param Category: 項目類别。
        :type Category: str
        :param Owner: 歸屬者。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param CoverUrl: 項目封面圖片網址。
        :type CoverUrl: str
        :param CreateTime: 項目創建時間，格式按照 ISO 8601 標準表示。
        :type CreateTime: str
        :param UpdateTime: 項目更新時間，格式按照 ISO 8601 標準表示。
        :type UpdateTime: str
        """
        self.ProjectId = None
        self.Name = None
        self.AspectRatio = None
        self.Category = None
        self.Owner = None
        self.CoverUrl = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Name = params.get("Name")
        self.AspectRatio = params.get("AspectRatio")
        self.Category = params.get("Category")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.CoverUrl = params.get("CoverUrl")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class Resource(AbstractModel):
    """用於描述資源

    """

    def __init__(self):
        """
        :param Type: 類型，取值有：
<li>MATERIAL：素材。</li>
<li>CLASS：分類。</li>
        :type Type: str
        :param Id: 資源 Id，當 Type 爲 MATERIAL 時，取值爲素材 Id；當 Type 爲 CLASS 時，取值爲分類路徑 ClassPath。
        :type Id: str
        """
        self.Type = None
        self.Id = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Id = params.get("Id")


class RevokeResourceAuthorizationRequest(AbstractModel):
    """RevokeResourceAuthorization請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param Owner: 資源所屬實體。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param Resources: 被授權資源。
        :type Resources: list of Resource
        :param Authorizees: 被授權目標實體。
        :type Authorizees: list of Entity
        :param Permissions: 詳細授權值。 取值有：
<li>R：可讀，可以浏覽素材，但不能使用該素材（将其添加到 Project），或複制到自己的媒資庫中</li>
<li>X：可用，可以使用該素材（将其添加到 Project），但不能将其複制到自己的媒資庫中，意味着被授權者無法将該資源進一步擴散給其他個人或團隊。</li>
<li>C：可複制，既可以使用該素材（将其添加到 Project），也可以将其複制到自己的媒資庫中。</li>
<li>W：可修改、删除媒資。</li>
        :type Permissions: list of str
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.Owner = None
        self.Resources = None
        self.Authorizees = None
        self.Permissions = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = Resource()
                obj._deserialize(item)
                self.Resources.append(obj)
        if params.get("Authorizees") is not None:
            self.Authorizees = []
            for item in params.get("Authorizees"):
                obj = Entity()
                obj._deserialize(item)
                self.Authorizees.append(obj)
        self.Permissions = params.get("Permissions")
        self.Operator = params.get("Operator")


class RevokeResourceAuthorizationResponse(AbstractModel):
    """RevokeResourceAuthorization返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchMaterialRequest(AbstractModel):
    """SearchMaterial請求參數結構體

    """

    def __init__(self):
        """
        :param Platform: 平台名稱，指定訪問的平台。
        :type Platform: str
        :param SearchScopes: 指定搜索空間，數組長度不得超過5。
        :type SearchScopes: list of SearchScope
        :param MaterialTypes: 素材類型，取值：
<li>AUDIO：音訊；</li>
<li>VIDEO：視訊 ；</li>
<li>IMAGE：圖片。</li>
        :type MaterialTypes: list of str
        :param Text: 搜索文本，模糊比對素材名稱或描述訊息，比對項越多，比對度越高，排序越優先。長度限制：64 個字元。
        :type Text: str
        :param Resolution: 按畫質檢索，取值爲：LD/SD/HD/FHD/2K/4K。
        :type Resolution: str
        :param DurationRange: 按素材時長檢索，單位s。
        :type DurationRange: :class:`taifucloudcloud.cme.v20191029.models.IntegerRange`
        :param CreateTimeRange: 按照素材創建時間檢索。
        :type CreateTimeRange: :class:`taifucloudcloud.cme.v20191029.models.TimeRange`
        :param Tags: 標簽集合，比對集合中任意元素。單個標簽長度限制：10 個字元。數組長度限制：10。
        :type Tags: list of str
        :param Sort: 排序方式。Sort.Field 可選值：CreateTime。指定 Text 搜索時，将根據比對度排序，該欄位無效。
        :type Sort: :class:`taifucloudcloud.cme.v20191029.models.SortBy`
        :param Offset: 偏移量。預設值：0。
        :type Offset: int
        :param Limit: 返回記錄條數，預設值：50。
        :type Limit: int
        :param Operator: 操作者。填寫用戶的 Id，用於標識調用者及校驗操作權限。
        :type Operator: str
        """
        self.Platform = None
        self.SearchScopes = None
        self.MaterialTypes = None
        self.Text = None
        self.Resolution = None
        self.DurationRange = None
        self.CreateTimeRange = None
        self.Tags = None
        self.Sort = None
        self.Offset = None
        self.Limit = None
        self.Operator = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        if params.get("SearchScopes") is not None:
            self.SearchScopes = []
            for item in params.get("SearchScopes"):
                obj = SearchScope()
                obj._deserialize(item)
                self.SearchScopes.append(obj)
        self.MaterialTypes = params.get("MaterialTypes")
        self.Text = params.get("Text")
        self.Resolution = params.get("Resolution")
        if params.get("DurationRange") is not None:
            self.DurationRange = IntegerRange()
            self.DurationRange._deserialize(params.get("DurationRange"))
        if params.get("CreateTimeRange") is not None:
            self.CreateTimeRange = TimeRange()
            self.CreateTimeRange._deserialize(params.get("CreateTimeRange"))
        self.Tags = params.get("Tags")
        if params.get("Sort") is not None:
            self.Sort = SortBy()
            self.Sort._deserialize(params.get("Sort"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Operator = params.get("Operator")


class SearchMaterialResponse(AbstractModel):
    """SearchMaterial返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合記錄總條數。
        :type TotalCount: int
        :param MaterialInfoSet: 素材訊息，僅返回基礎訊息。
        :type MaterialInfoSet: list of MaterialInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.MaterialInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("MaterialInfoSet") is not None:
            self.MaterialInfoSet = []
            for item in params.get("MaterialInfoSet"):
                obj = MaterialInfo()
                obj._deserialize(item)
                self.MaterialInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class SearchScope(AbstractModel):
    """搜索空間

    """

    def __init__(self):
        """
        :param Owner: 分類路徑歸屬。
        :type Owner: :class:`taifucloudcloud.cme.v20191029.models.Entity`
        :param ClassPath: 按分類路徑檢索。 不填則預設按根分類路徑檢索。
        :type ClassPath: str
        """
        self.Owner = None
        self.ClassPath = None


    def _deserialize(self, params):
        if params.get("Owner") is not None:
            self.Owner = Entity()
            self.Owner._deserialize(params.get("Owner"))
        self.ClassPath = params.get("ClassPath")


class SortBy(AbstractModel):
    """排序

    """

    def __init__(self):
        """
        :param Field: 排序欄位。
        :type Field: str
        :param Order: 排序方式，可選值：Asc（升序）、Desc（降序），預設降序。
        :type Order: str
        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")


class TaskBaseInfo(AbstractModel):
    """任務基礎訊息。

    """

    def __init__(self):
        """
        :param TaskId: 任務 Id。
        :type TaskId: str
        :param TaskType: 任務類型，取值有：
<li>VIDEO_EDIT_PROJECT_EXPORT：項目導出。</li>
        :type TaskType: str
        :param Status: 任務狀态，取值有：
<li>PROCESSING：處理中：</li>
<li>SUCCESS：成功；</li>
<li>FAIL：失敗。</li>
        :type Status: str
        :param Progress: 任務進度，取值爲：0~100。
        :type Progress: int
        :param ErrCode: 錯誤碼。
<li>0：成功；</li>
<li>其他值：失敗。</li>
        :type ErrCode: int
        :param ErrMsg: 錯誤訊息。
        :type ErrMsg: str
        :param CreateTime: 創建時間，格式按照 ISO 8601 標準表示。
        :type CreateTime: str
        """
        self.TaskId = None
        self.TaskType = None
        self.Status = None
        self.Progress = None
        self.ErrCode = None
        self.ErrMsg = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        self.CreateTime = params.get("CreateTime")


class TeamInfo(AbstractModel):
    """團隊訊息

    """

    def __init__(self):
        """
        :param TeamId: 團隊 ID。
        :type TeamId: str
        :param Name: 團隊名稱。
        :type Name: str
        :param MemberCount: 團隊成員個數
        :type MemberCount: int
        :param CreateTime: 團隊創建時間，格式按照 ISO 8601 標準表示。
        :type CreateTime: str
        :param UpdateTime: 團隊最後更新時間，格式按照 ISO 8601 標準表示。
        :type UpdateTime: str
        """
        self.TeamId = None
        self.Name = None
        self.MemberCount = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TeamId = params.get("TeamId")
        self.Name = params.get("Name")
        self.MemberCount = params.get("MemberCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class TeamMemberInfo(AbstractModel):
    """團隊成員訊息

    """

    def __init__(self):
        """
        :param MemberId: 團隊成員 ID。
        :type MemberId: str
        :param Remark: 團隊成員備注。
        :type Remark: str
        :param Role: 團隊成員角色，取值：
<li>Owner：團隊所有者，添加團隊成員及修改團隊成員解決時不能填此角色；</li>
<li>Admin：團隊管理員；</li>
<li>Member：普通成員。</li>
        :type Role: str
        """
        self.MemberId = None
        self.Remark = None
        self.Role = None


    def _deserialize(self, params):
        self.MemberId = params.get("MemberId")
        self.Remark = params.get("Remark")
        self.Role = params.get("Role")


class TimeRange(AbstractModel):
    """時間範圍

    """

    def __init__(self):
        """
        :param StartTime: 開始時間，使用 ISO 日期格式。
        :type StartTime: str
        :param EndTime: 結束時間，使用 ISO 日期格式。
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class VODExportInfo(AbstractModel):
    """雲點播導出訊息。

    """

    def __init__(self):
        """
        :param Name: 導出的媒資名稱。
        :type Name: str
        :param ClassId: 導出的媒資分類 Id。
        :type ClassId: int
        """
        self.Name = None
        self.ClassId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ClassId = params.get("ClassId")


class VideoEditProjectOutput(AbstractModel):
    """項目導出訊息。

    """

    def __init__(self):
        """
        :param VodFileId: 雲點播媒資 FileId。
        :type VodFileId: str
        :param URL: 導出的媒資 URL。
        :type URL: str
        :param MetaData: 元訊息。
        :type MetaData: :class:`taifucloudcloud.cme.v20191029.models.MediaMetaData`
        """
        self.VodFileId = None
        self.URL = None
        self.MetaData = None


    def _deserialize(self, params):
        self.VodFileId = params.get("VodFileId")
        self.URL = params.get("URL")
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))


class VideoMaterial(AbstractModel):
    """視訊素材訊息

    """

    def __init__(self):
        """
        :param MetaData: 素材元訊息。
        :type MetaData: :class:`taifucloudcloud.cme.v20191029.models.MediaMetaData`
        :param ImageSpriteInfo: 雪碧圖訊息。
        :type ImageSpriteInfo: :class:`taifucloudcloud.cme.v20191029.models.MediaImageSpriteInfo`
        :param MaterialUrl: 素材媒體文件的 URL 網址
        :type MaterialUrl: str
        :param CoverUrl: 素材媒體文件的封面圖片網址。
        :type CoverUrl: str
        :param Resolution: 媒體文件分辨率。取值爲：LD/SD/HD/FHD/2K/4K。
        :type Resolution: str
        :param MaterialStatus: 素材狀态。
注意：此欄位可能返回 null，表示取不到有效值。
        :type MaterialStatus: :class:`taifucloudcloud.cme.v20191029.models.MaterialStatus`
        """
        self.MetaData = None
        self.ImageSpriteInfo = None
        self.MaterialUrl = None
        self.CoverUrl = None
        self.Resolution = None
        self.MaterialStatus = None


    def _deserialize(self, params):
        if params.get("MetaData") is not None:
            self.MetaData = MediaMetaData()
            self.MetaData._deserialize(params.get("MetaData"))
        if params.get("ImageSpriteInfo") is not None:
            self.ImageSpriteInfo = MediaImageSpriteInfo()
            self.ImageSpriteInfo._deserialize(params.get("ImageSpriteInfo"))
        self.MaterialUrl = params.get("MaterialUrl")
        self.CoverUrl = params.get("CoverUrl")
        self.Resolution = params.get("Resolution")
        if params.get("MaterialStatus") is not None:
            self.MaterialStatus = MaterialStatus()
            self.MaterialStatus._deserialize(params.get("MaterialStatus"))


class VideoStreamInfo(AbstractModel):
    """視訊流訊息。

    """

    def __init__(self):
        """
        :param Bitrate: 碼率，單位：bps。
        :type Bitrate: int
        :param Height: 高度，單位：px。
        :type Height: int
        :param Width: 寬度，單位：px。
        :type Width: int
        :param Codec: 編碼格式。
        :type Codec: str
        :param Fps: 幀率，單位：hz。
        :type Fps: int
        """
        self.Bitrate = None
        self.Height = None
        self.Width = None
        self.Codec = None
        self.Fps = None


    def _deserialize(self, params):
        self.Bitrate = params.get("Bitrate")
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.Codec = params.get("Codec")
        self.Fps = params.get("Fps")