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
from taifucloudcloud.autoscaling.v20180419 import models


class AutoscalingClient(AbstractClient):
    _apiVersion = '2018-04-19'
    _endpoint = 'as.taifucloudcloudapi.com'


    def AttachInstances(self, request):
        """本介面（AttachInstances）用於将 CVM 實例添加到伸縮組。

        :param request: 調用AttachInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.AttachInstancesRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.AttachInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachInstancesResponse()
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


    def CompleteLifecycleAction(self, request):
        """本介面（CompleteLifecycleAction）用於完成生命週期動作。

        * 用戶通過調用本介面，指定一個具體的生命週期挂鈎的結果（“CONITNUE”或者“ABANDON”）。如果一直不調用本介面，則生命週期挂鈎會在超時後按照“DefaultResult”進行處理。

        :param request: 調用CompleteLifecycleAction所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.CompleteLifecycleActionRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.CompleteLifecycleActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompleteLifecycleAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompleteLifecycleActionResponse()
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


    def CreateAutoScalingGroup(self, request):
        """本介面（CreateAutoScalingGroup）用於創建伸縮組

        :param request: 調用CreateAutoScalingGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateAutoScalingGroupRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAutoScalingGroupResponse()
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


    def CreateLaunchConfiguration(self, request):
        """本介面（CreateLaunchConfiguration）用於創建新的啓動配置。

        * 啓動配置，可以通過 `ModifyLaunchConfigurationAttributes` 修改少量欄位。如需使用新的啓動配置，建議重新創建啓動配置。

        * 每個項目最多只能創建20個啓動配置，詳見[使用限制](https://cloud.taifucloud.com/document/product/377/3120)。

        :param request: 調用CreateLaunchConfiguration所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateLaunchConfigurationRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLaunchConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLaunchConfigurationResponse()
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


    def CreateLifecycleHook(self, request):
        """本介面（CreateLifecycleHook）用於創建生命週期挂鈎。

        * 您可以爲生命週期挂鈎配置訊息通知，彈性伸縮會通知您的CMQ訊息隊列，通知内容形如：

        ```
        {
        	"Service": "Tencent Cloud Auto Scaling",
        	"Time": "2019-03-14T10:15:11Z",
        	"AppId": "1251783334",
        	"ActivityId": "asa-fznnvrja",
        	"AutoScalingGroupId": "asg-rrrrtttt",
        	"LifecycleHookId": "ash-xxxxyyyy",
        	"LifecycleHookName": "my-hook",
        	"LifecycleActionToken": "3080e1c9-0efe-4dd7-ad3b-90cd6618298f",
        	"InstanceId": "ins-aaaabbbb",
        	"LifecycleTransition": "INSTANCE_LAUNCHING",
        	"NotificationMetadata": ""
        }
        ```

        :param request: 調用CreateLifecycleHook所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateLifecycleHookRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLifecycleHook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLifecycleHookResponse()
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


    def CreateNotificationConfiguration(self, request):
        """本介面（CreateNotificationConfiguration）用於創建通知。

        :param request: 調用CreateNotificationConfiguration所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateNotificationConfigurationRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNotificationConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNotificationConfigurationResponse()
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


    def CreatePaiInstance(self, request):
        """本介面 (CreatePaiInstance) 用於創建一個指定配置的PAI實例。

        :param request: 調用CreatePaiInstance所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.CreatePaiInstanceRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.CreatePaiInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePaiInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePaiInstanceResponse()
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


    def CreateScalingPolicy(self, request):
        """本介面（CreateScalingPolicy）用於創建告警觸發策略。

        :param request: 調用CreateScalingPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateScalingPolicyRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScalingPolicyResponse()
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


    def CreateScheduledAction(self, request):
        """本介面（CreateScheduledAction）用於創建定時任務。

        :param request: 調用CreateScheduledAction所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateScheduledActionRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.CreateScheduledActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScheduledAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScheduledActionResponse()
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


    def DeleteAutoScalingGroup(self, request):
        """本介面（DeleteAutoScalingGroup）用於删除指定伸縮組，删除前提是伸縮組内無實例且當前未在執行伸縮活動。

        :param request: 調用DeleteAutoScalingGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteAutoScalingGroupRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAutoScalingGroupResponse()
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


    def DeleteLaunchConfiguration(self, request):
        """本介面（DeleteLaunchConfiguration）用於删除啓動配置。

        * 若啓動配置在伸縮組中屬於生效狀态，則該啓動配置不允許删除。

        :param request: 調用DeleteLaunchConfiguration所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteLaunchConfigurationRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLaunchConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLaunchConfigurationResponse()
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


    def DeleteLifecycleHook(self, request):
        """本介面（DeleteLifecycleHook）用於删除生命週期挂鈎。

        :param request: 調用DeleteLifecycleHook所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteLifecycleHookRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLifecycleHook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLifecycleHookResponse()
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


    def DeleteNotificationConfiguration(self, request):
        """本介面（DeleteNotificationConfiguration）用於删除特定的通知。

        :param request: 調用DeleteNotificationConfiguration所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteNotificationConfigurationRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNotificationConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNotificationConfigurationResponse()
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


    def DeleteScalingPolicy(self, request):
        """本介面（DeleteScalingPolicy）用於删除告警觸發策略。

        :param request: 調用DeleteScalingPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteScalingPolicyRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScalingPolicyResponse()
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


    def DeleteScheduledAction(self, request):
        """本介面（DeleteScheduledAction）用於删除特定的定時任務。

        :param request: 調用DeleteScheduledAction所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteScheduledActionRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DeleteScheduledActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScheduledAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScheduledActionResponse()
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


    def DescribeAccountLimits(self, request):
        """本介面（DescribeAccountLimits）用於查詢用戶帳戶在彈性伸縮中的資源限制。

        :param request: 調用DescribeAccountLimits所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeAccountLimitsRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeAccountLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountLimitsResponse()
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


    def DescribeAutoScalingActivities(self, request):
        """本介面（DescribeAutoScalingActivities）用於查詢伸縮組的伸縮活動記錄。

        :param request: 調用DescribeAutoScalingActivities所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeAutoScalingActivitiesRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeAutoScalingActivitiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingActivities", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingActivitiesResponse()
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


    def DescribeAutoScalingGroups(self, request):
        """本介面（DescribeAutoScalingGroups）用於查詢伸縮組訊息。

        * 可以根據伸縮組ID、伸縮組名稱或者啓動配置ID等訊息來查詢伸縮組的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的伸縮組。

        :param request: 調用DescribeAutoScalingGroups所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupsRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeAutoScalingGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingGroupsResponse()
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


    def DescribeAutoScalingInstances(self, request):
        """本介面（DescribeAutoScalingInstances）用於查詢彈性伸縮關聯實例的訊息。

        * 可以根據實例ID、伸縮組ID等訊息來查詢實例的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的實例。

        :param request: 調用DescribeAutoScalingInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeAutoScalingInstancesRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeAutoScalingInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoScalingInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoScalingInstancesResponse()
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


    def DescribeLaunchConfigurations(self, request):
        """本介面（DescribeLaunchConfigurations）用於查詢啓動配置的訊息。

        * 可以根據啓動配置ID、啓動配置名稱等訊息來查詢啓動配置的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的啓動配置。

        :param request: 調用DescribeLaunchConfigurations所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeLaunchConfigurationsRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeLaunchConfigurationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLaunchConfigurations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLaunchConfigurationsResponse()
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


    def DescribeLifecycleHooks(self, request):
        """本介面（DescribeLifecycleHooks）用於查詢生命週期挂鈎訊息。

        * 可以根據伸縮組ID、生命週期挂鈎ID或者生命週期挂鈎名稱等訊息來查詢生命週期挂鈎的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的生命週期挂鈎。

        :param request: 調用DescribeLifecycleHooks所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeLifecycleHooksRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeLifecycleHooksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLifecycleHooks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLifecycleHooksResponse()
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


    def DescribeNotificationConfigurations(self, request):
        """本介面 (DescribeNotificationConfigurations) 用於查詢一個或多個通知的詳細訊息。

        可以根據通知ID、伸縮組ID等訊息來查詢通知的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        如果參數爲空，返回當前用戶一定數量（Limit所指定的數量，預設爲20）的通知。

        :param request: 調用DescribeNotificationConfigurations所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeNotificationConfigurationsRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeNotificationConfigurationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNotificationConfigurations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNotificationConfigurationsResponse()
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


    def DescribePaiInstances(self, request):
        """本介面（DescribePaiInstances）用於查詢PAI實例訊息。

        * 可以根據實例ID、實例域名等訊息來查詢PAI實例的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（`Limit`所指定的數量，預設爲20）的PAI實例。

        :param request: 調用DescribePaiInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribePaiInstancesRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribePaiInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePaiInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePaiInstancesResponse()
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


    def DescribeScalingPolicies(self, request):
        """本介面（DescribeScalingPolicies）用於查詢告警觸發策略。

        :param request: 調用DescribeScalingPolicies所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeScalingPoliciesRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeScalingPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScalingPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScalingPoliciesResponse()
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


    def DescribeScheduledActions(self, request):
        """本介面 (DescribeScheduledActions) 用於查詢一個或多個定時任務的詳細訊息。

        * 可以根據定時任務ID、定時任務名稱或者伸縮組ID等訊息來查詢定時任務的詳細訊息。過濾訊息詳細請見過濾器`Filter`。
        * 如果參數爲空，返回當前用戶一定數量（Limit所指定的數量，預設爲20）的定時任務。

        :param request: 調用DescribeScheduledActions所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeScheduledActionsRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DescribeScheduledActionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScheduledActions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScheduledActionsResponse()
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


    def DetachInstances(self, request):
        """本介面（DetachInstances）用於從伸縮組移出 CVM 實例，本介面不會銷毀實例。

        :param request: 調用DetachInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DetachInstancesRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DetachInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachInstancesResponse()
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


    def DisableAutoScalingGroup(self, request):
        """本介面（DisableAutoScalingGroup）用於停用指定伸縮組。

        :param request: 調用DisableAutoScalingGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.DisableAutoScalingGroupRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.DisableAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableAutoScalingGroupResponse()
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


    def EnableAutoScalingGroup(self, request):
        """本介面（EnableAutoScalingGroup）用於啓用指定伸縮組。

        :param request: 調用EnableAutoScalingGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.EnableAutoScalingGroupRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.EnableAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableAutoScalingGroupResponse()
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


    def ModifyAutoScalingGroup(self, request):
        """本介面（ModifyAutoScalingGroup）用於修改伸縮組。

        :param request: 調用ModifyAutoScalingGroup所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyAutoScalingGroupRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyAutoScalingGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoScalingGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoScalingGroupResponse()
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


    def ModifyDesiredCapacity(self, request):
        """本介面（ModifyDesiredCapacity）用於修改指定伸縮組的期望實例數

        :param request: 調用ModifyDesiredCapacity所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyDesiredCapacityRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyDesiredCapacityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDesiredCapacity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDesiredCapacityResponse()
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


    def ModifyLaunchConfigurationAttributes(self, request):
        """本介面（ModifyLaunchConfigurationAttributes）用於修改啓動配置部分屬性。

        * 修改啓動配置後，已經使用該啓動配置擴容的存量實例不會發生變更，此後使用該啓動配置的新增實例會按照新的配置進行擴容。
        * 本介面支援修改部分簡單類型。

        :param request: 調用ModifyLaunchConfigurationAttributes所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyLaunchConfigurationAttributesRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyLaunchConfigurationAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLaunchConfigurationAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLaunchConfigurationAttributesResponse()
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


    def ModifyLoadBalancers(self, request):
        """本介面（ModifyLoadBalancers）用於修改伸縮組的負載均衡器。

        * 本介面用於爲伸縮組指定新的負載均衡器配置，采用“完全函蓋”風格，無論之前配置如何，統一按照介面參數配置爲新的負載均衡器。
        * 如果要爲伸縮組清空負載均衡器，則在調用本介面時僅指定伸縮組ID，不指定具體負載均衡器。
        * 本介面會立即修改伸縮組的負載均衡器，並生成一個伸縮活動，異步修改存量實例的負載均衡器。

        :param request: 調用ModifyLoadBalancers所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyLoadBalancersRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancersResponse()
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


    def ModifyNotificationConfiguration(self, request):
        """本介面（ModifyNotificationConfiguration）用於修改通知。

        :param request: 調用ModifyNotificationConfiguration所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyNotificationConfigurationRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyNotificationConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNotificationConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNotificationConfigurationResponse()
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


    def ModifyScalingPolicy(self, request):
        """本介面（ModifyScalingPolicy）用於修改告警觸發策略。

        :param request: 調用ModifyScalingPolicy所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyScalingPolicyRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyScalingPolicyResponse()
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


    def ModifyScheduledAction(self, request):
        """本介面（ModifyScheduledAction）用於修改定時任務。

        :param request: 調用ModifyScheduledAction所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyScheduledActionRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.ModifyScheduledActionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyScheduledAction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyScheduledActionResponse()
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


    def PreviewPaiDomainName(self, request):
        """本介面（PreviewPaiDomainName）用於預覽PAI實例域名。

        :param request: 調用PreviewPaiDomainName所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.PreviewPaiDomainNameRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.PreviewPaiDomainNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PreviewPaiDomainName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PreviewPaiDomainNameResponse()
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


    def RemoveInstances(self, request):
        """本介面（RemoveInstances）用於從伸縮組删除 CVM 實例。根據當前的産品邏輯，如果實例由彈性伸縮自動創建，則實例會被銷毀；如果實例系創建後加入伸縮組的，則會從伸縮組中移除，保留實例。

        :param request: 調用RemoveInstances所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.RemoveInstancesRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.RemoveInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveInstancesResponse()
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


    def SetInstancesProtection(self, request):
        """本介面（SetInstancesProtection）用於設置實例移除保護。
        子機設置爲移除保護之後，當發生不健康替換、報警策略、期望值變更等觸發縮容時，将不對此子機縮容操作。

        :param request: 調用SetInstancesProtection所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.SetInstancesProtectionRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.SetInstancesProtectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetInstancesProtection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetInstancesProtectionResponse()
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


    def UpgradeLaunchConfiguration(self, request):
        """本介面（UpgradeLaunchConfiguration）用於升級啓動配置。

        * 本介面用於升級啓動配置，采用“完全函蓋”風格，無論之前參數如何，統一按照介面參數設置爲新的配置。對於非必填欄位，不填寫則按照預設值賦值。

        :param request: 調用UpgradeLaunchConfiguration所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.UpgradeLaunchConfigurationRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.UpgradeLaunchConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeLaunchConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeLaunchConfigurationResponse()
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


    def UpgradeLifecycleHook(self, request):
        """本介面（UpgradeLifecycleHook）用於升級生命週期挂鈎。

        * 本介面用於升級生命週期挂鈎，采用“完全函蓋”風格，無論之前參數如何，統一按照介面參數設置爲新的配置。對於非必填欄位，不填寫則按照預設值賦值。

        :param request: 調用UpgradeLifecycleHook所需參數的結構體。
        :type request: :class:`taifucloudcloud.autoscaling.v20180419.models.UpgradeLifecycleHookRequest`
        :rtype: :class:`taifucloudcloud.autoscaling.v20180419.models.UpgradeLifecycleHookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeLifecycleHook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeLifecycleHookResponse()
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