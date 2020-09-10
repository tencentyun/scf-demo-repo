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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cme.v20191029 import models


class CmeClient(AbstractClient):
    _apiVersion = '2019-10-29'
    _endpoint = 'cme.tencentcloudapi.com'


    def AddTeamMember(self, request):
        """向一個團隊中團隊成員，并且指定成員的角色。

        :param request: Request instance for AddTeamMember.
        :type request: :class:`tencentcloud.cme.v20191029.models.AddTeamMemberRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.AddTeamMemberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddTeamMember", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddTeamMemberResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateClass(self, request):
        """新增分類，用于管理素材。
        <li>分類層數不能超過10；</li>
        <li>子分類數不能超過10。</li>

        :param request: Request instance for CreateClass.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateClassRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClassResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLink(self, request):
        """創建素材連結或分類路徑連結，将源資源訊息連結到目标。

        :param request: Request instance for CreateLink.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateLinkRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateLinkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLink", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLinkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProject(self, request):
        """創建雲剪的編輯項目，支援創建視訊剪輯及直播剪輯兩大類項目。

        :param request: Request instance for CreateProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTeam(self, request):
        """創建一個團隊。

        :param request: Request instance for CreateTeam.
        :type request: :class:`tencentcloud.cme.v20191029.models.CreateTeamRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.CreateTeamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTeam", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTeamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteClass(self, request):
        """删除分類訊息，删除時檢驗下述限制：
        <li>分類路徑必須存在；</li>
        <li>分類下沒有綁定素材。</li>

        :param request: Request instance for DeleteClass.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteClassRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClassResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLoginStatus(self, request):
        """删除用戶登入态，使用戶登出雲剪平台。

        :param request: Request instance for DeleteLoginStatus.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteLoginStatusRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteLoginStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoginStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoginStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMaterial(self, request):
        """根據素材 Id 删除素材。

        :param request: Request instance for DeleteMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMaterialResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteProject(self, request):
        """删除雲剪編輯項目。

        :param request: Request instance for DeleteProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTeam(self, request):
        """删除一個團隊。
        <li>要删除的團隊必須沒有歸屬的素材；</li>
        <li>要删除的團隊必須沒有歸屬的分類。</li>

        :param request: Request instance for DeleteTeam.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteTeamRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteTeamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTeam", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTeamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTeamMembers(self, request):
        """将團隊成員從團隊中删除，預設只有 Owner 及管理員才有此權限。

        :param request: Request instance for DeleteTeamMembers.
        :type request: :class:`tencentcloud.cme.v20191029.models.DeleteTeamMembersRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DeleteTeamMembersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTeamMembers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTeamMembersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClass(self, request):
        """獲取指定歸屬者下所有的分類訊息。

        :param request: Request instance for DescribeClass.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeClassRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeJoinTeams(self, request):
        """獲取指定的團隊成員所加入的團隊清單。

        :param request: Request instance for DescribeJoinTeams.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeJoinTeamsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeJoinTeamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJoinTeams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJoinTeamsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLoginStatus(self, request):
        """查詢指定用戶的登入态。

        :param request: Request instance for DescribeLoginStatus.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeLoginStatusRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeLoginStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoginStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoginStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMaterials(self, request):
        """根據素材 Id 批次獲取素材詳情。

        :param request: Request instance for DescribeMaterials.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeMaterialsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeMaterialsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMaterials", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMaterialsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProjects(self, request):
        """支援根據多種條件過濾出項目清單。

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceAuthorization(self, request):
        """查詢指定資源的授權清單。

        :param request: Request instance for DescribeResourceAuthorization.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeResourceAuthorizationRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeResourceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceAuthorization", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceAuthorizationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSharedSpace(self, request):
        """獲取共享空間。當實體A對實體B授權某資源以後，實體B的共享空間就會增加實體A。

        :param request: Request instance for DescribeSharedSpace.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeSharedSpaceRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeSharedSpaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSharedSpace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSharedSpaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskDetail(self, request):
        """獲取任務詳情訊息，包含下面幾個部分：
        <li>任務基礎訊息：包括任務狀态、錯誤訊息、創建時間等；</li>
        <li>導出項目輸出訊息：包括輸出的素材 Id 等。</li>

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasks(self, request):
        """獲取任務清單，支援條件篩選，返回對應的任務基礎訊息清單。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTeamMembers(self, request):
        """獲取指定成員 ID 的訊息，同時支援拉取所有團隊成員訊息。

        :param request: Request instance for DescribeTeamMembers.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTeamMembersRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTeamMembersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTeamMembers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTeamMembersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTeams(self, request):
        """獲取指定團隊的訊息。

        :param request: Request instance for DescribeTeams.
        :type request: :class:`tencentcloud.cme.v20191029.models.DescribeTeamsRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.DescribeTeamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTeams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTeamsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExportVideoEditProject(self, request):
        """導出視訊編輯項目，支援指定輸出的範本。

        :param request: Request instance for ExportVideoEditProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ExportVideoEditProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ExportVideoEditProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportVideoEditProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportVideoEditProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FlattenListMedia(self, request):
        """平鋪分類路徑下及其子分類下的所有素材。

        :param request: Request instance for FlattenListMedia.
        :type request: :class:`tencentcloud.cme.v20191029.models.FlattenListMediaRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.FlattenListMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FlattenListMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FlattenListMediaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GrantResourceAuthorization(self, request):
        """資源所屬實體對目标實體授予目标資源的相應權限。

        :param request: Request instance for GrantResourceAuthorization.
        :type request: :class:`tencentcloud.cme.v20191029.models.GrantResourceAuthorizationRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.GrantResourceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GrantResourceAuthorization", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GrantResourceAuthorizationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportMaterial(self, request):
        """将雲點播媒資文件導入到雲剪素材庫。

        :param request: Request instance for ImportMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.ImportMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ImportMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportMaterialResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportMediaToProject(self, request):
        """将雲點播中的媒資添加到素材庫中，供後續視訊編輯使用。

        :param request: Request instance for ImportMediaToProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ImportMediaToProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ImportMediaToProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportMediaToProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportMediaToProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListMedia(self, request):
        """浏覽當前分類路徑下的資源，包括素材和子分類。

        :param request: Request instance for ListMedia.
        :type request: :class:`tencentcloud.cme.v20191029.models.ListMediaRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ListMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListMediaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMaterial(self, request):
        """修改素材訊息，支援修改素材名稱、分類路徑、标簽等訊息。

        :param request: Request instance for ModifyMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMaterialResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyProject(self, request):
        """修改雲剪編輯項目的訊息。

        :param request: Request instance for ModifyProject.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyProjectRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTeam(self, request):
        """修改團隊訊息，目前支援修改的操作有：
        <li>修改團隊名稱。</li>

        :param request: Request instance for ModifyTeam.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyTeamRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyTeamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTeam", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTeamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTeamMember(self, request):
        """修改團隊成員訊息，包括成員備注、角色等。

        :param request: Request instance for ModifyTeamMember.
        :type request: :class:`tencentcloud.cme.v20191029.models.ModifyTeamMemberRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.ModifyTeamMemberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTeamMember", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTeamMemberResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MoveClass(self, request):
        """移動某一個分類到另外一個分類下，也可用于分類重命名。
        <li>如果 SourceClassPath = /素材/視訊/NBA，DestinationClassPath = /素材/視訊/籃球，當 DestinationClassPath 不存在時候，操作結果爲重命名 ClassPath，如果 DestinationClassPath 存在時候，操作結果爲産生新目錄 /素材/視訊/籃球/NBA。</li>

        :param request: Request instance for MoveClass.
        :type request: :class:`tencentcloud.cme.v20191029.models.MoveClassRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.MoveClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MoveClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MoveClassResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RevokeResourceAuthorization(self, request):
        """資源所屬實體對目标實體回收目标資源的相應權限，若原本沒有相應權限則不産生變更。

        :param request: Request instance for RevokeResourceAuthorization.
        :type request: :class:`tencentcloud.cme.v20191029.models.RevokeResourceAuthorizationRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.RevokeResourceAuthorizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevokeResourceAuthorization", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevokeResourceAuthorizationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchMaterial(self, request):
        """根據檢索條件搜索素材，返回素材的基本訊息。

        :param request: Request instance for SearchMaterial.
        :type request: :class:`tencentcloud.cme.v20191029.models.SearchMaterialRequest`
        :rtype: :class:`tencentcloud.cme.v20191029.models.SearchMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchMaterialResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)