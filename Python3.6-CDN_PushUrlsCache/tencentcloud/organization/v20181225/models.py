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


class AcceptOrganizationInvitationRequest(AbstractModel):
    """AcceptOrganizationInvitation請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 邀請ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class AcceptOrganizationInvitationResponse(AbstractModel):
    """AcceptOrganizationInvitation返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddOrganizationNodeRequest(AbstractModel):
    """AddOrganizationNode請求參數結構體

    """

    def __init__(self):
        """
        :param ParentNodeId: 父組織單元ID
        :type ParentNodeId: int
        :param Name: 組織單元名字
        :type Name: str
        """
        self.ParentNodeId = None
        self.Name = None


    def _deserialize(self, params):
        self.ParentNodeId = params.get("ParentNodeId")
        self.Name = params.get("Name")


class AddOrganizationNodeResponse(AbstractModel):
    """AddOrganizationNode返回參數結構體

    """

    def __init__(self):
        """
        :param NodeId: 組織單元ID
        :type NodeId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.NodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.RequestId = params.get("RequestId")


class CancelOrganizationInvitationRequest(AbstractModel):
    """CancelOrganizationInvitation請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 邀請ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class CancelOrganizationInvitationResponse(AbstractModel):
    """CancelOrganizationInvitation返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateOrganizationRequest(AbstractModel):
    """CreateOrganization請求參數結構體

    """

    def __init__(self):
        """
        :param OrgType: 組織類型（目前固定爲1）
        :type OrgType: int
        """
        self.OrgType = None


    def _deserialize(self, params):
        self.OrgType = params.get("OrgType")


class CreateOrganizationResponse(AbstractModel):
    """CreateOrganization返回參數結構體

    """

    def __init__(self):
        """
        :param OrgId: 企業組織ID
        :type OrgId: int
        :param Nickname: 創建者昵稱
        :type Nickname: str
        :param Mail: 創建者電子信箱
        :type Mail: str
        :param OrgType: 組織類型
        :type OrgType: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OrgId = None
        self.Nickname = None
        self.Mail = None
        self.OrgType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        self.Nickname = params.get("Nickname")
        self.Mail = params.get("Mail")
        self.OrgType = params.get("OrgType")
        self.RequestId = params.get("RequestId")


class DeleteOrganizationMemberFromNodeRequest(AbstractModel):
    """DeleteOrganizationMemberFromNode請求參數結構體

    """

    def __init__(self):
        """
        :param MemberUin: 被删除成員UIN
        :type MemberUin: int
        :param NodeId: 組織單元ID
        :type NodeId: int
        """
        self.MemberUin = None
        self.NodeId = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.NodeId = params.get("NodeId")


class DeleteOrganizationMemberFromNodeResponse(AbstractModel):
    """DeleteOrganizationMemberFromNode返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOrganizationMembersRequest(AbstractModel):
    """DeleteOrganizationMembers請求參數結構體

    """

    def __init__(self):
        """
        :param Uins: 被删除成員的UIN清單
        :type Uins: list of int non-negative
        """
        self.Uins = None


    def _deserialize(self, params):
        self.Uins = params.get("Uins")


class DeleteOrganizationMembersResponse(AbstractModel):
    """DeleteOrganizationMembers返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOrganizationNodesRequest(AbstractModel):
    """DeleteOrganizationNodes請求參數結構體

    """

    def __init__(self):
        """
        :param NodeIds: 組織單元ID清單
        :type NodeIds: list of int non-negative
        """
        self.NodeIds = None


    def _deserialize(self, params):
        self.NodeIds = params.get("NodeIds")


class DeleteOrganizationNodesResponse(AbstractModel):
    """DeleteOrganizationNodes返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteOrganizationRequest(AbstractModel):
    """DeleteOrganization請求參數結構體

    """


class DeleteOrganizationResponse(AbstractModel):
    """DeleteOrganization返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DenyOrganizationInvitationRequest(AbstractModel):
    """DenyOrganizationInvitation請求參數結構體

    """

    def __init__(self):
        """
        :param Id: 邀請ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")


class DenyOrganizationInvitationResponse(AbstractModel):
    """DenyOrganizationInvitation返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GetOrganizationMemberRequest(AbstractModel):
    """GetOrganizationMember請求參數結構體

    """

    def __init__(self):
        """
        :param MemberUin: 組織成員UIN
        :type MemberUin: int
        """
        self.MemberUin = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")


class GetOrganizationMemberResponse(AbstractModel):
    """GetOrganizationMember返回參數結構體

    """

    def __init__(self):
        """
        :param Uin: 組織成員UIN
        :type Uin: int
        :param Name: 組織成員名稱
        :type Name: str
        :param Remark: 備注
        :type Remark: str
        :param JoinTime: 加入時間
        :type JoinTime: str
        :param NodeId: 組織單元ID
        :type NodeId: int
        :param NodeName: 組織單元名稱
        :type NodeName: str
        :param ParentNodeId: 父組織單元ID
        :type ParentNodeId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Uin = None
        self.Name = None
        self.Remark = None
        self.JoinTime = None
        self.NodeId = None
        self.NodeName = None
        self.ParentNodeId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.JoinTime = params.get("JoinTime")
        self.NodeId = params.get("NodeId")
        self.NodeName = params.get("NodeName")
        self.ParentNodeId = params.get("ParentNodeId")
        self.RequestId = params.get("RequestId")


class GetOrganizationRequest(AbstractModel):
    """GetOrganization請求參數結構體

    """


class GetOrganizationResponse(AbstractModel):
    """GetOrganization返回參數結構體

    """

    def __init__(self):
        """
        :param OrgId: 企業組織ID
        :type OrgId: int
        :param HostUin: 創建者UIN
        :type HostUin: int
        :param Nickname: 創建者昵稱
        :type Nickname: str
        :param Mail: 創建者電子信箱
        :type Mail: str
        :param OrgType: 企業組織類型
        :type OrgType: int
        :param IsEmpty: 是否爲空
        :type IsEmpty: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OrgId = None
        self.HostUin = None
        self.Nickname = None
        self.Mail = None
        self.OrgType = None
        self.IsEmpty = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")
        self.HostUin = params.get("HostUin")
        self.Nickname = params.get("Nickname")
        self.Mail = params.get("Mail")
        self.OrgType = params.get("OrgType")
        self.IsEmpty = params.get("IsEmpty")
        self.RequestId = params.get("RequestId")


class ListOrganizationInvitationsRequest(AbstractModel):
    """ListOrganizationInvitations請求參數結構體

    """

    def __init__(self):
        """
        :param Invited: 是否被邀請。1：被邀請，0：發出的邀請
        :type Invited: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        """
        self.Invited = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Invited = params.get("Invited")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class ListOrganizationInvitationsResponse(AbstractModel):
    """ListOrganizationInvitations返回參數結構體

    """

    def __init__(self):
        """
        :param Invitations: 邀請訊息清單
        :type Invitations: list of OrgInvitation
        :param TotalCount: 總數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Invitations = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Invitations") is not None:
            self.Invitations = []
            for item in params.get("Invitations"):
                obj = OrgInvitation()
                obj._deserialize(item)
                self.Invitations.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListOrganizationMembersRequest(AbstractModel):
    """ListOrganizationMembers請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class ListOrganizationMembersResponse(AbstractModel):
    """ListOrganizationMembers返回參數結構體

    """

    def __init__(self):
        """
        :param Members: 成員清單
        :type Members: list of OrgMember
        :param TotalCount: 總數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Members = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Members") is not None:
            self.Members = []
            for item in params.get("Members"):
                obj = OrgMember()
                obj._deserialize(item)
                self.Members.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListOrganizationNodeMembersRequest(AbstractModel):
    """ListOrganizationNodeMembers請求參數結構體

    """

    def __init__(self):
        """
        :param NodeId: 企業組織單元ID
        :type NodeId: int
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制數目
        :type Limit: int
        """
        self.NodeId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class ListOrganizationNodeMembersResponse(AbstractModel):
    """ListOrganizationNodeMembers返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 總數目
        :type TotalCount: int
        :param Members: 成員清單
        :type Members: list of OrgMember
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Members = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Members") is not None:
            self.Members = []
            for item in params.get("Members"):
                obj = OrgMember()
                obj._deserialize(item)
                self.Members.append(obj)
        self.RequestId = params.get("RequestId")


class ListOrganizationNodesRequest(AbstractModel):
    """ListOrganizationNodes請求參數結構體

    """


class ListOrganizationNodesResponse(AbstractModel):
    """ListOrganizationNodes返回參數結構體

    """

    def __init__(self):
        """
        :param Nodes: 企業組織單元清單
        :type Nodes: list of OrgNode
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Nodes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = OrgNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        self.RequestId = params.get("RequestId")


class MoveOrganizationMembersToNodeRequest(AbstractModel):
    """MoveOrganizationMembersToNode請求參數結構體

    """

    def __init__(self):
        """
        :param NodeId: 組織單元ID
        :type NodeId: int
        :param Uins: 成員UIN清單
        :type Uins: list of int non-negative
        """
        self.NodeId = None
        self.Uins = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Uins = params.get("Uins")


class MoveOrganizationMembersToNodeResponse(AbstractModel):
    """MoveOrganizationMembersToNode返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OrgInvitation(AbstractModel):
    """企業組織邀請

    """

    def __init__(self):
        """
        :param Id: 邀請ID
        :type Id: int
        :param Uin: 被邀請UIN
        :type Uin: int
        :param HostUin: 創建者UIN
        :type HostUin: int
        :param HostName: 創建者名稱
        :type HostName: str
        :param HostMail: 創建者電子信箱
        :type HostMail: str
        :param Status: 邀請狀态。-1：已過期，0：正常，1：已接受，2：已失效，3：已取消
        :type Status: int
        :param Name: 名稱
        :type Name: str
        :param Remark: 備注
        :type Remark: str
        :param OrgType: 企業組織類型
        :type OrgType: int
        :param InviteTime: 邀請時間
        :type InviteTime: str
        :param ExpireTime: 過期時間
        :type ExpireTime: str
        """
        self.Id = None
        self.Uin = None
        self.HostUin = None
        self.HostName = None
        self.HostMail = None
        self.Status = None
        self.Name = None
        self.Remark = None
        self.OrgType = None
        self.InviteTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uin = params.get("Uin")
        self.HostUin = params.get("HostUin")
        self.HostName = params.get("HostName")
        self.HostMail = params.get("HostMail")
        self.Status = params.get("Status")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.OrgType = params.get("OrgType")
        self.InviteTime = params.get("InviteTime")
        self.ExpireTime = params.get("ExpireTime")


class OrgMember(AbstractModel):
    """企業組織成員

    """

    def __init__(self):
        """
        :param Uin: UIN
        :type Uin: int
        :param Name: 名稱
        :type Name: str
        :param Remark: 備注
        :type Remark: str
        :param JoinTime: 加入時間
        :type JoinTime: str
        """
        self.Uin = None
        self.Name = None
        self.Remark = None
        self.JoinTime = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.JoinTime = params.get("JoinTime")


class OrgNode(AbstractModel):
    """企業組織單元

    """

    def __init__(self):
        """
        :param NodeId: 組織單元ID
        :type NodeId: int
        :param Name: 名稱
        :type Name: str
        :param ParentNodeId: 父單元ID
        :type ParentNodeId: int
        :param MemberCount: 成員數量
        :type MemberCount: int
        """
        self.NodeId = None
        self.Name = None
        self.ParentNodeId = None
        self.MemberCount = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Name = params.get("Name")
        self.ParentNodeId = params.get("ParentNodeId")
        self.MemberCount = params.get("MemberCount")


class QuitOrganizationRequest(AbstractModel):
    """QuitOrganization請求參數結構體

    """

    def __init__(self):
        """
        :param OrgId: 企業組織ID
        :type OrgId: int
        """
        self.OrgId = None


    def _deserialize(self, params):
        self.OrgId = params.get("OrgId")


class QuitOrganizationResponse(AbstractModel):
    """QuitOrganization返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SendOrganizationInvitationRequest(AbstractModel):
    """SendOrganizationInvitation請求參數結構體

    """

    def __init__(self):
        """
        :param InviteUin: 被邀請帳戶UIN
        :type InviteUin: int
        :param Name: 名稱
        :type Name: str
        :param Remark: 備注
        :type Remark: str
        """
        self.InviteUin = None
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.InviteUin = params.get("InviteUin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")


class SendOrganizationInvitationResponse(AbstractModel):
    """SendOrganizationInvitation返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateOrganizationMemberRequest(AbstractModel):
    """UpdateOrganizationMember請求參數結構體

    """

    def __init__(self):
        """
        :param MemberUin: 成員UIN
        :type MemberUin: int
        :param Name: 名稱
        :type Name: str
        :param Remark: 備注
        :type Remark: str
        """
        self.MemberUin = None
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.MemberUin = params.get("MemberUin")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")


class UpdateOrganizationMemberResponse(AbstractModel):
    """UpdateOrganizationMember返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateOrganizationNodeRequest(AbstractModel):
    """UpdateOrganizationNode請求參數結構體

    """

    def __init__(self):
        """
        :param NodeId: 企業組織單元ID
        :type NodeId: int
        :param Name: 名稱
        :type Name: str
        :param ParentNodeId: 父單元ID
        :type ParentNodeId: int
        """
        self.NodeId = None
        self.Name = None
        self.ParentNodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        self.Name = params.get("Name")
        self.ParentNodeId = params.get("ParentNodeId")


class UpdateOrganizationNodeResponse(AbstractModel):
    """UpdateOrganizationNode返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")