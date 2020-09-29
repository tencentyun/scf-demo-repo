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
from taifucloudcloud.redis.v20180412 import models


class RedisClient(AbstractClient):
    _apiVersion = '2018-04-12'
    _endpoint = 'redis.taifucloudcloudapi.com'


    def AssociateSecurityGroups(self, request):
        """本介面 (AssociateSecurityGroups) 用於綁定安全組到指定實例。

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateSecurityGroupsResponse()
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


    def CleanUpInstance(self, request):
        """資源回收筒實例立即下線

        :param request: Request instance for CleanUpInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.CleanUpInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.CleanUpInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CleanUpInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CleanUpInstanceResponse()
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


    def ClearInstance(self, request):
        """清空Redis實例的實例數據。

        :param request: Request instance for ClearInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.ClearInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.ClearInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ClearInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearInstanceResponse()
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


    def CreateInstanceAccount(self, request):
        """創建實例子賬號

        :param request: Request instance for CreateInstanceAccount.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.CreateInstanceAccountRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.CreateInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceAccountResponse()
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


    def CreateInstances(self, request):
        """創建redis實例

        :param request: Request instance for CreateInstances.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.CreateInstancesRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstancesResponse()
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


    def DeleteInstanceAccount(self, request):
        """删除實例子賬號

        :param request: Request instance for DeleteInstanceAccount.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DeleteInstanceAccountRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DeleteInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteInstanceAccountResponse()
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


    def DescribeAutoBackupConfig(self, request):
        """獲取備份配置

        :param request: Request instance for DescribeAutoBackupConfig.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeAutoBackupConfigRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeAutoBackupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoBackupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoBackupConfigResponse()
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


    def DescribeBackupUrl(self, request):
        """查詢備份Rdb下載網址(介面灰度中，需要加白名單使用)

        :param request: Request instance for DescribeBackupUrl.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeBackupUrlRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeBackupUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupUrlResponse()
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


    def DescribeDBSecurityGroups(self, request):
        """本介面(DescribeDBSecurityGroups)用於查詢實例的安全組詳情。

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSecurityGroupsResponse()
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


    def DescribeInstanceAccount(self, request):
        """檢視實例子賬號訊息

        :param request: Request instance for DescribeInstanceAccount.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceAccountRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceAccountResponse()
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


    def DescribeInstanceBackups(self, request):
        """查詢 CRS 實例備份清單

        :param request: Request instance for DescribeInstanceBackups.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceBackupsRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceBackupsResponse()
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


    def DescribeInstanceDTSInfo(self, request):
        """查詢實例DTS訊息

        :param request: Request instance for DescribeInstanceDTSInfo.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceDTSInfoRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceDTSInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceDTSInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceDTSInfoResponse()
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


    def DescribeInstanceDealDetail(self, request):
        """查詢訂單訊息

        :param request: Request instance for DescribeInstanceDealDetail.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceDealDetailRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceDealDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceDealDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceDealDetailResponse()
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


    def DescribeInstanceMonitorBigKey(self, request):
        """查詢實例大Key

        :param request: Request instance for DescribeInstanceMonitorBigKey.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorBigKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorBigKeyResponse()
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


    def DescribeInstanceMonitorBigKeySizeDist(self, request):
        """查詢實例大Key大小分布

        :param request: Request instance for DescribeInstanceMonitorBigKeySizeDist.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeySizeDistRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeySizeDistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorBigKeySizeDist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorBigKeySizeDistResponse()
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


    def DescribeInstanceMonitorBigKeyTypeDist(self, request):
        """查詢實例大Key類型分布

        :param request: Request instance for DescribeInstanceMonitorBigKeyTypeDist.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyTypeDistRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyTypeDistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorBigKeyTypeDist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorBigKeyTypeDistResponse()
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


    def DescribeInstanceMonitorHotKey(self, request):
        """查詢實例熱Key

        :param request: Request instance for DescribeInstanceMonitorHotKey.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorHotKeyRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorHotKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorHotKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorHotKeyResponse()
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


    def DescribeInstanceMonitorSIP(self, request):
        """查詢實例訪問來源訊息

        :param request: Request instance for DescribeInstanceMonitorSIP.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorSIPRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorSIPResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorSIP", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorSIPResponse()
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


    def DescribeInstanceMonitorTookDist(self, request):
        """查詢實例訪問的耗時分布

        :param request: Request instance for DescribeInstanceMonitorTookDist.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorTookDistRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorTookDistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorTookDist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorTookDistResponse()
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


    def DescribeInstanceMonitorTopNCmd(self, request):
        """查詢實例訪問命令

        :param request: Request instance for DescribeInstanceMonitorTopNCmd.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorTopNCmd", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorTopNCmdResponse()
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


    def DescribeInstanceMonitorTopNCmdTook(self, request):
        """查詢實例CPU耗時

        :param request: Request instance for DescribeInstanceMonitorTopNCmdTook.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdTookRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdTookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorTopNCmdTook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorTopNCmdTookResponse()
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


    def DescribeInstanceParamRecords(self, request):
        """查詢參數修改曆史清單

        :param request: Request instance for DescribeInstanceParamRecords.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceParamRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceParamRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceParamRecordsResponse()
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


    def DescribeInstanceParams(self, request):
        """查詢實例參數清單

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceParamsRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceParams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceParamsResponse()
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


    def DescribeInstanceSecurityGroup(self, request):
        """查詢實例安全組訊息

        :param request: Request instance for DescribeInstanceSecurityGroup.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceSecurityGroupRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceSecurityGroupResponse()
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


    def DescribeInstanceShards(self, request):
        """獲取集群版實例分片訊息

        :param request: Request instance for DescribeInstanceShards.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceShardsRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstanceShardsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceShards", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceShardsResponse()
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


    def DescribeInstances(self, request):
        """查詢Redis實例清單

        :param request: Request instance for DescribeInstances.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstancesRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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


    def DescribeProductInfo(self, request):
        """本介面查詢指定可用區和實例類型下 Redis 的售賣規格， 如果用戶不在購買白名單中，将不能查詢該可用區或該類型的售賣規格詳情。申請購買某地域白名單可以提交工單

        :param request: Request instance for DescribeProductInfo.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeProductInfoRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeProductInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductInfoResponse()
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


    def DescribeProjectSecurityGroup(self, request):
        """查詢項目安全組訊息

        :param request: Request instance for DescribeProjectSecurityGroup.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeProjectSecurityGroupRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeProjectSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjectSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupResponse()
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


    def DescribeProjectSecurityGroups(self, request):
        """本介面(DescribeProjectSecurityGroups)用於查詢項目的安全組詳情。

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjectSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupsResponse()
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


    def DescribeSlowLog(self, request):
        """查詢實例慢查詢記錄

        :param request: Request instance for DescribeSlowLog.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeSlowLogRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeSlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogResponse()
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


    def DescribeTaskInfo(self, request):
        """用於查詢任務結果

        :param request: Request instance for DescribeTaskInfo.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeTaskInfoRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeTaskInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskInfoResponse()
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


    def DescribeTaskList(self, request):
        """查詢任務清單訊息

        :param request: Request instance for DescribeTaskList.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DescribeTaskListRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DescribeTaskListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskListResponse()
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


    def DestroyPostpaidInstance(self, request):
        """按量計費實例銷毀

        :param request: Request instance for DestroyPostpaidInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DestroyPostpaidInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DestroyPostpaidInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyPostpaidInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyPostpaidInstanceResponse()
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


    def DestroyPrepaidInstance(self, request):
        """包年包月實例退還

        :param request: Request instance for DestroyPrepaidInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DestroyPrepaidInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DestroyPrepaidInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyPrepaidInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyPrepaidInstanceResponse()
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


    def DisableReplicaReadonly(self, request):
        """禁用讀寫分離

        :param request: Request instance for DisableReplicaReadonly.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DisableReplicaReadonlyRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DisableReplicaReadonlyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableReplicaReadonly", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableReplicaReadonlyResponse()
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


    def DisassociateSecurityGroups(self, request):
        """本介面(DisassociateSecurityGroups)用於安全組批次解綁實例。

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateSecurityGroupsResponse()
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


    def EnableReplicaReadonly(self, request):
        """啓用讀寫分離

        :param request: Request instance for EnableReplicaReadonly.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.EnableReplicaReadonlyRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.EnableReplicaReadonlyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableReplicaReadonly", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableReplicaReadonlyResponse()
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


    def InquiryPriceCreateInstance(self, request):
        """查詢新購實例價格

        :param request: Request instance for InquiryPriceCreateInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.InquiryPriceCreateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateInstanceResponse()
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


    def InquiryPriceRenewInstance(self, request):
        """查詢實例續約價格（包年包月）

        :param request: Request instance for InquiryPriceRenewInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.InquiryPriceRenewInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.InquiryPriceRenewInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewInstanceResponse()
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


    def InquiryPriceUpgradeInstance(self, request):
        """查詢實例擴容價格

        :param request: Request instance for InquiryPriceUpgradeInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.InquiryPriceUpgradeInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.InquiryPriceUpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceUpgradeInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpgradeInstanceResponse()
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


    def ManualBackupInstance(self, request):
        """手動備份Redis實例

        :param request: Request instance for ManualBackupInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.ManualBackupInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.ManualBackupInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManualBackupInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManualBackupInstanceResponse()
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


    def ModfiyInstancePassword(self, request):
        """修改redis密碼

        :param request: Request instance for ModfiyInstancePassword.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.ModfiyInstancePasswordRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.ModfiyInstancePasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModfiyInstancePassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModfiyInstancePasswordResponse()
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


    def ModifyAutoBackupConfig(self, request):
        """設置自動備份時間

        :param request: Request instance for ModifyAutoBackupConfig.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.ModifyAutoBackupConfigRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.ModifyAutoBackupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoBackupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoBackupConfigResponse()
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


    def ModifyDBInstanceSecurityGroups(self, request):
        """本介面(ModifyDBInstanceSecurityGroups)用於修改實例綁定的安全組

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSecurityGroupsResponse()
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


    def ModifyInstance(self, request):
        """修改實例相關訊息

        :param request: Request instance for ModifyInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.ModifyInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceResponse()
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


    def ModifyInstanceAccount(self, request):
        """修改實例子賬號

        :param request: Request instance for ModifyInstanceAccount.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.ModifyInstanceAccountRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.ModifyInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceAccountResponse()
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


    def ModifyInstanceParams(self, request):
        """修改實例參數

        :param request: Request instance for ModifyInstanceParams.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.ModifyInstanceParamsRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.ModifyInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceParams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceParamsResponse()
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


    def ModifyNetworkConfig(self, request):
        """修改實例網絡配置

        :param request: Request instance for ModifyNetworkConfig.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.ModifyNetworkConfigRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.ModifyNetworkConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetworkConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkConfigResponse()
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


    def RenewInstance(self, request):
        """續約實例

        :param request: Request instance for RenewInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.RenewInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewInstanceResponse()
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


    def ResetPassword(self, request):
        """重置密碼

        :param request: Request instance for ResetPassword.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.ResetPasswordRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.ResetPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetPasswordResponse()
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


    def RestoreInstance(self, request):
        """恢複 CRS 實例

        :param request: Request instance for RestoreInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.RestoreInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.RestoreInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestoreInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestoreInstanceResponse()
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


    def StartupInstance(self, request):
        """實例解隔離

        :param request: Request instance for StartupInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.StartupInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.StartupInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartupInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartupInstanceResponse()
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


    def SwitchInstanceVip(self, request):
        """在通過DTS支援跨可用區災備的場景中，通過該介面交換實例VIP完成實例災備切換。交換VIP後目標實例可寫，源和目標實例VIP互換，同時源與目標實例間DTS同步任務斷開

        :param request: Request instance for SwitchInstanceVip.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.SwitchInstanceVipRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.SwitchInstanceVipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwitchInstanceVip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchInstanceVipResponse()
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


    def UpgradeInstance(self, request):
        """升級實例

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`taifucloudcloud.redis.v20180412.models.UpgradeInstanceRequest`
        :rtype: :class:`taifucloudcloud.redis.v20180412.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeInstanceResponse()
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