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


    def CleanUpInstance(self, request):
        """資源回收筒實例立即下線

        :param request: 調用CleanUpInstance所需參數的結構體。
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

        :param request: 調用ClearInstance所需參數的結構體。
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


    def CreateInstances(self, request):
        """創建redis實例

        :param request: 調用CreateInstances所需參數的結構體。
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


    def DescribeAutoBackupConfig(self, request):
        """獲取備份配置

        :param request: 調用DescribeAutoBackupConfig所需參數的結構體。
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
        """查詢備份Rdb下載網址

        :param request: 調用DescribeBackupUrl所需參數的結構體。
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


    def DescribeInstanceBackups(self, request):
        """查詢 CRS 實例備份清單

        :param request: 調用DescribeInstanceBackups所需參數的結構體。
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


    def DescribeInstanceDealDetail(self, request):
        """查詢訂單訊息

        :param request: 調用DescribeInstanceDealDetail所需參數的結構體。
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


    def DescribeInstanceParamRecords(self, request):
        """查詢參數修改曆史清單

        :param request: 調用DescribeInstanceParamRecords所需參數的結構體。
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

        :param request: 調用DescribeInstanceParams所需參數的結構體。
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

        :param request: 調用DescribeInstanceSecurityGroup所需參數的結構體。
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

        :param request: 調用DescribeInstanceShards所需參數的結構體。
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

        :param request: 調用DescribeInstances所需參數的結構體。
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

        :param request: 調用DescribeProductInfo所需參數的結構體。
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

        :param request: 調用DescribeProjectSecurityGroup所需參數的結構體。
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


    def DescribeTaskInfo(self, request):
        """用于查詢任務結果

        :param request: 調用DescribeTaskInfo所需參數的結構體。
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


    def DestroyPostpaidInstance(self, request):
        """按量計費實例銷毀

        :param request: 調用DestroyPostpaidInstance所需參數的結構體。
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

        :param request: 調用DestroyPrepaidInstance所需參數的結構體。
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

        :param request: 調用DisableReplicaReadonly所需參數的結構體。
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


    def EnableReplicaReadonly(self, request):
        """啓用讀寫分離

        :param request: 調用EnableReplicaReadonly所需參數的結構體。
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


    def ManualBackupInstance(self, request):
        """手動備份Redis實例

        :param request: 調用ManualBackupInstance所需參數的結構體。
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

        :param request: 調用ModfiyInstancePassword所需參數的結構體。
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

        :param request: 調用ModifyAutoBackupConfig所需參數的結構體。
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


    def ModifyInstance(self, request):
        """修改實例相關訊息（目前支援：實例重命名）

        :param request: 調用ModifyInstance所需參數的結構體。
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


    def ModifyInstanceParams(self, request):
        """修改實例參數

        :param request: 調用ModifyInstanceParams所需參數的結構體。
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

        :param request: 調用ModifyNetworkConfig所需參數的結構體。
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

        :param request: 調用RenewInstance所需參數的結構體。
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

        :param request: 調用ResetPassword所需參數的結構體。
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

        :param request: 調用RestoreInstance所需參數的結構體。
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


    def UpgradeInstance(self, request):
        """升級實例

        :param request: 調用UpgradeInstance所需參數的結構體。
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