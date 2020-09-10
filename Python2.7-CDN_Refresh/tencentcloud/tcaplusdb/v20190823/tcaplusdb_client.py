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

from taifucloudcloud.common.exception.taifucloud_cloud_sdk_exception import TencentCloudSDKException
from taifucloudcloud.common.abstract_client import AbstractClient
from taifucloudcloud.tcaplusdb.v20190823 import models


class TcaplusdbClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'tcaplusdb.taifucloudcloudapi.com'


    def ClearTables(self, request):
        """根據給定的表訊息，清除表數據。

        :param request: Request instance for ClearTables.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ClearTablesRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ClearTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ClearTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearTablesResponse()
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


    def CompareIdlFiles(self, request):
        """選中目标表格，上傳并校驗改表文件，返回是否允許修改表格結構的結果。

        :param request: Request instance for CompareIdlFiles.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.CompareIdlFilesRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.CompareIdlFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompareIdlFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompareIdlFilesResponse()
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


    def CreateBackup(self, request):
        """用戶創建備份任務

        :param request: Request instance for CreateBackup.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.CreateBackupRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBackup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBackupResponse()
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


    def CreateCluster(self, request):
        """本介面用于創建TcaplusDB集群

        :param request: Request instance for CreateCluster.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.CreateClusterRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterResponse()
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


    def CreateTableGroup(self, request):
        """在TcaplusDB集群下創建表格組

        :param request: Request instance for CreateTableGroup.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.CreateTableGroupRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.CreateTableGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTableGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTableGroupResponse()
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


    def CreateTables(self, request):
        """根據選擇的IDL文件清單，批次創建表格

        :param request: Request instance for CreateTables.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.CreateTablesRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.CreateTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTablesResponse()
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


    def DeleteCluster(self, request):
        """删除TcaplusDB集群，必須在集群所屬所有資源（包括表格組，表）都已經釋放的情況下才會成功。

        :param request: Request instance for DeleteCluster.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DeleteClusterRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterResponse()
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


    def DeleteIdlFiles(self, request):
        """指定集群ID和待删除IDL文件的訊息，删除目标文件，如果文件正在被表關聯則删除失敗。

        :param request: Request instance for DeleteIdlFiles.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DeleteIdlFilesRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DeleteIdlFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteIdlFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteIdlFilesResponse()
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


    def DeleteTableGroup(self, request):
        """删除表格組

        :param request: Request instance for DeleteTableGroup.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DeleteTableGroupRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DeleteTableGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTableGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTableGroupResponse()
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


    def DeleteTables(self, request):
        """删除指定的表,第一次調用此介面代表将表 至資源回收筒，再次調用代表将此表格從資源回收筒中徹底删除。

        :param request: Request instance for DeleteTables.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DeleteTablesRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DeleteTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTablesResponse()
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


    def DescribeClusters(self, request):
        """查詢TcaplusDB集群清單，包含集群詳細訊息。

        :param request: Request instance for DescribeClusters.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeClustersRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClustersResponse()
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


    def DescribeIdlFileInfos(self, request):
        """查詢表描述文件詳情

        :param request: Request instance for DescribeIdlFileInfos.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeIdlFileInfosRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeIdlFileInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIdlFileInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIdlFileInfosResponse()
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


    def DescribeRegions(self, request):
        """查詢TcaplusDB服務支援的地域清單

        :param request: Request instance for DescribeRegions.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeRegionsRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
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


    def DescribeTableGroups(self, request):
        """查詢表格組清單

        :param request: Request instance for DescribeTableGroups.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeTableGroupsRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeTableGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTableGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTableGroupsResponse()
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


    def DescribeTables(self, request):
        """查詢表詳情

        :param request: Request instance for DescribeTables.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeTablesRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTablesResponse()
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


    def DescribeTablesInRecycle(self, request):
        """查詢資源回收筒中的表詳情

        :param request: Request instance for DescribeTablesInRecycle.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeTablesInRecycleRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeTablesInRecycleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTablesInRecycle", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTablesInRecycleResponse()
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
        """查詢任務清單

        :param request: Request instance for DescribeTasks.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeTasksRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeTasksResponse`

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


    def DescribeUinInWhitelist(self, request):
        """查詢本用戶是否在白名單中，控制是否能創建TDR類型的APP或表

        :param request: Request instance for DescribeUinInWhitelist.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeUinInWhitelistRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.DescribeUinInWhitelistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUinInWhitelist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUinInWhitelistResponse()
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


    def ModifyClusterName(self, request):
        """修改指定的集群名稱

        :param request: Request instance for ModifyClusterName.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyClusterNameRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyClusterNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterNameResponse()
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


    def ModifyClusterPassword(self, request):
        """修改指定集群的密碼，後台将在舊密碼失效之前同時支援TcaplusDB SDK使用舊密碼和新密碼訪問資料庫。在舊密碼失效之前不能提交新的密碼修改請求，在舊密碼失效之後不能提交修改舊密碼過期時間的請求。

        :param request: Request instance for ModifyClusterPassword.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyClusterPasswordRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyClusterPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterPasswordResponse()
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


    def ModifyTableGroupName(self, request):
        """修改TcaplusDB表格組名稱

        :param request: Request instance for ModifyTableGroupName.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyTableGroupNameRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyTableGroupNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableGroupName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableGroupNameResponse()
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


    def ModifyTableMemos(self, request):
        """修改表備注訊息

        :param request: Request instance for ModifyTableMemos.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyTableMemosRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyTableMemosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableMemos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableMemosResponse()
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


    def ModifyTableQuotas(self, request):
        """表格擴縮容

        :param request: Request instance for ModifyTableQuotas.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyTableQuotasRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyTableQuotasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableQuotas", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableQuotasResponse()
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


    def ModifyTables(self, request):
        """根據用戶選定的表定義IDL文件，批次修改指定的表

        :param request: Request instance for ModifyTables.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyTablesRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.ModifyTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTablesResponse()
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


    def RecoverRecycleTables(self, request):
        """恢複資源回收筒中，用戶自行删除的表。對欠費待釋放的表無效。

        :param request: Request instance for RecoverRecycleTables.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.RecoverRecycleTablesRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.RecoverRecycleTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecoverRecycleTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecoverRecycleTablesResponse()
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


    def RollbackTables(self, request):
        """表格數據回檔

        :param request: Request instance for RollbackTables.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.RollbackTablesRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.RollbackTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RollbackTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RollbackTablesResponse()
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


    def VerifyIdlFiles(self, request):
        """上傳并校驗創建表格文件，返回校驗合法的表格定義

        :param request: Request instance for VerifyIdlFiles.
        :type request: :class:`taifucloudcloud.tcaplusdb.v20190823.models.VerifyIdlFilesRequest`
        :rtype: :class:`taifucloudcloud.tcaplusdb.v20190823.models.VerifyIdlFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyIdlFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyIdlFilesResponse()
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