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
from taifucloudcloud.live.v20180801 import models


class LiveClient(AbstractClient):
    _apiVersion = '2018-08-01'
    _endpoint = 'live.taifucloudcloudapi.com'


    def AddDelayLiveStream(self, request):
        """對流設置延播時間
        注意：如果在推流前設置延播，需要提前5分鍾設置。
        目前該介面只支援流粒度的，域名及應用粒度功能支援當前開發中。

        :param request: 調用AddDelayLiveStream所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.AddDelayLiveStreamRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.AddDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddDelayLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddDelayLiveStreamResponse()
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


    def AddLiveDomain(self, request):
        """添加域名，一次只能提交一個域名。域名必須已備案。

        :param request: 調用AddLiveDomain所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.AddLiveDomainRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.AddLiveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddLiveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddLiveDomainResponse()
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


    def AddLiveWatermark(self, request):
        """添加浮水印，成功返回水印id後，需要調用[CreateLiveWatermarkRule](/document/product/267/32629)介面将水印id綁定到流使用。

        :param request: 調用AddLiveWatermark所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.AddLiveWatermarkRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.AddLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddLiveWatermarkResponse()
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


    def BindLiveDomainCert(self, request):
        """域名綁定證書

        :param request: 調用BindLiveDomainCert所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.BindLiveDomainCertRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.BindLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindLiveDomainCertResponse()
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


    def CreateLiveCallbackRule(self, request):
        """創建回調規則，需要先調用[CreateLiveCallbackTemplate](/document/product/267/32637)介面創建回調範本，将返回的範本id綁定到域名/路徑進行使用。
        <br>回調協議相關文件：[事件訊息通知](/document/product/267/32744)。

        :param request: 調用CreateLiveCallbackRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveCallbackRuleRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveCallbackRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveCallbackRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveCallbackRuleResponse()
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


    def CreateLiveCallbackTemplate(self, request):
        """創建回調範本，成功返回範本id後，需要調用[CreateLiveCallbackRule](/document/product/267/32638)介面将範本id綁定到域名/路徑使用。
        <br>回調協議相關文件：[事件訊息通知](/document/product/267/32744)。

        :param request: 調用CreateLiveCallbackTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveCallbackTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveCallbackTemplateResponse()
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


    def CreateLiveCert(self, request):
        """添加證書

        :param request: 調用CreateLiveCert所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveCertRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveCertResponse()
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


    def CreateLiveRecord(self, request):
        """- 使用前提
          1. 錄制文件存放于點播平台，所以用戶如需使用錄制功能，需首先自行開通點播服務。
          2. 錄制文件存放後相關費用（含儲存以及下行播放流量）按照點播平台計費方式收取，具體請參考 [對應文件](https://cloud.taifucloud.com/document/product/266/2838)。

        - 模式說明
          該介面支援兩種錄制模式：
          1. 定時錄制模式【預設模式】。
            需要傳入開始時間與結束時間，錄制任務根據時間自動開始與結束。
          2. 實時視訊錄制模式。
            忽略傳入的開始時間，在錄制任務創建後立即開始錄制，錄制時長支援最大爲30分鍾，如果傳入的結束時間與當前時間差大于30分鍾，則按30分鍾計算，實時視訊錄制主要用于錄制精彩視訊場景，時長建議控制在5分鍾以内。

        - 注意事項
          1. 調用介面超時設置應大于3秒，小於3秒重試以及頻繁調用都有可能産生重複錄制任務。

        :param request: 調用CreateLiveRecord所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveRecordRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordResponse()
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


    def CreateLiveRecordRule(self, request):
        """創建錄制規則，需要先調用[CreateLiveRecordTemplate](/document/product/267/32614)介面創建錄制範本，将返回的範本id綁定到流使用。
        <br>錄制相關文件：[直播錄制](/document/product/267/32739)。

        :param request: 調用CreateLiveRecordRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveRecordRuleRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveRecordRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveRecordRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordRuleResponse()
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


    def CreateLiveRecordTemplate(self, request):
        """創建錄制範本，成功返回範本id後，需要調用[CreateLiveRecordRule](/document/product/267/32615)介面，将範本id綁定到流進行使用。
        <br>錄制相關文件：[直播錄制](/document/product/267/32739)。

        :param request: 調用CreateLiveRecordTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveRecordTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveRecordTemplateResponse()
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


    def CreateLiveSnapshotRule(self, request):
        """創建截圖規則，需要先調用[CreateLiveSnapshotTemplate](/document/product/267/32624)介面創建截圖範本，然後将返回的範本id綁定到流進行使用。
        <br>截圖相關文件：[直播截圖](/document/product/267/32737)。

        :param request: 調用CreateLiveSnapshotRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveSnapshotRuleRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveSnapshotRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveSnapshotRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveSnapshotRuleResponse()
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


    def CreateLiveSnapshotTemplate(self, request):
        """創建截圖範本，成功返回範本id後，需要調用[CreateLiveSnapshotRule](/document/product/267/32625)介面，将範本id綁定到流使用。
        <br>截圖相關文件：[直播截圖](/document/product/267/32737)。

        :param request: 調用CreateLiveSnapshotTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveSnapshotTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveSnapshotTemplateResponse()
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


    def CreateLiveTranscodeRule(self, request):
        """創建轉碼規則，需要先調用[CreateLiveTranscodeTemplate](/document/product/267/32646)介面創建轉碼範本，将返回的範本id綁定到流使用。
        <br>轉碼相關文件：[直播轉封裝及轉碼](/document/product/267/32736)。

        :param request: 調用CreateLiveTranscodeRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveTranscodeRuleRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveTranscodeRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveTranscodeRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveTranscodeRuleResponse()
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


    def CreateLiveTranscodeTemplate(self, request):
        """創建轉碼範本，成功返回範本id後，需要調用[CreateLiveTranscodeRule](/document/product/267/32647)介面，将返回的範本id綁定到流使用。
        <br>轉碼相關文件：[直播轉封裝及轉碼](/document/product/267/32736)。

        :param request: 調用CreateLiveTranscodeTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveTranscodeTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveTranscodeTemplateResponse()
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


    def CreateLiveWatermarkRule(self, request):
        """創建浮水印規則，需要先調用[AddLiveWatermark](/document/product/267/30154)介面添加水印，将返回的水印id綁定到流使用。

        :param request: 調用CreateLiveWatermarkRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreateLiveWatermarkRuleRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreateLiveWatermarkRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLiveWatermarkRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLiveWatermarkRuleResponse()
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


    def CreatePullStreamConfig(self, request):
        """創建臨時拉流轉推任務，目前限制添加10條任務。

        注意：該介面用于創建臨時拉流轉推任務，
        拉流源網址即FromUrl 可以是 或非 數據源，
        但轉推目标網址即ToUrl 目前限制爲已注冊的 直播域名。

        :param request: 調用CreatePullStreamConfig所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.CreatePullStreamConfigRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.CreatePullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePullStreamConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePullStreamConfigResponse()
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


    def DeleteLiveCallbackRule(self, request):
        """删除回調規則

        :param request: 調用DeleteLiveCallbackRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveCallbackRuleRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveCallbackRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveCallbackRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveCallbackRuleResponse()
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


    def DeleteLiveCallbackTemplate(self, request):
        """删除回調範本

        :param request: 調用DeleteLiveCallbackTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveCallbackTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveCallbackTemplateResponse()
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


    def DeleteLiveCert(self, request):
        """删除域名對應的證書

        :param request: 調用DeleteLiveCert所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveCertRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveCertResponse()
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


    def DeleteLiveDomain(self, request):
        """删除已添加的直播域名

        :param request: 調用DeleteLiveDomain所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveDomainRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveDomainResponse()
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


    def DeleteLiveRecord(self, request):
        """用于删除錄制任務。

        :param request: 調用DeleteLiveRecord所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveRecordRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordResponse()
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


    def DeleteLiveRecordRule(self, request):
        """删除錄制規則

        :param request: 調用DeleteLiveRecordRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveRecordRuleRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveRecordRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveRecordRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordRuleResponse()
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


    def DeleteLiveRecordTemplate(self, request):
        """删除錄制範本

        :param request: 調用DeleteLiveRecordTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveRecordTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveRecordTemplateResponse()
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


    def DeleteLiveSnapshotRule(self, request):
        """删除截圖規則

        :param request: 調用DeleteLiveSnapshotRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveSnapshotRuleRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveSnapshotRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveSnapshotRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveSnapshotRuleResponse()
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


    def DeleteLiveSnapshotTemplate(self, request):
        """删除截圖範本

        :param request: 調用DeleteLiveSnapshotTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveSnapshotTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveSnapshotTemplateResponse()
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


    def DeleteLiveTranscodeRule(self, request):
        """删除轉碼規則

        :param request: 調用DeleteLiveTranscodeRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveTranscodeRuleRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveTranscodeRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveTranscodeRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveTranscodeRuleResponse()
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


    def DeleteLiveTranscodeTemplate(self, request):
        """删除轉碼範本

        :param request: 調用DeleteLiveTranscodeTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveTranscodeTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveTranscodeTemplateResponse()
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


    def DeleteLiveWatermark(self, request):
        """删除浮水印

        :param request: 調用DeleteLiveWatermark所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveWatermarkRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveWatermarkResponse()
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


    def DeleteLiveWatermarkRule(self, request):
        """删除浮水印規則

        :param request: 調用DeleteLiveWatermarkRule所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveWatermarkRuleRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeleteLiveWatermarkRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLiveWatermarkRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLiveWatermarkRuleResponse()
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


    def DeletePullStreamConfig(self, request):
        """删除直播拉流配置

        :param request: 調用DeletePullStreamConfig所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DeletePullStreamConfigRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DeletePullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePullStreamConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePullStreamConfigResponse()
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


    def DescribeLiveCallbackRules(self, request):
        """獲取回調規則清單

        :param request: 調用DescribeLiveCallbackRules所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveCallbackRulesRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveCallbackRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCallbackRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCallbackRulesResponse()
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


    def DescribeLiveCallbackTemplate(self, request):
        """獲取單個回調範本

        :param request: 調用DescribeLiveCallbackTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveCallbackTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCallbackTemplateResponse()
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


    def DescribeLiveCallbackTemplates(self, request):
        """獲取回調範本清單

        :param request: 調用DescribeLiveCallbackTemplates所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveCallbackTemplatesRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveCallbackTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCallbackTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCallbackTemplatesResponse()
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


    def DescribeLiveCert(self, request):
        """獲驗證書訊息

        :param request: 調用DescribeLiveCert所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveCertRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCertResponse()
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


    def DescribeLiveCerts(self, request):
        """獲驗證書訊息清單

        :param request: 調用DescribeLiveCerts所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveCertsRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveCertsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveCerts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveCertsResponse()
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


    def DescribeLiveDomain(self, request):
        """查詢直播域名訊息。

        :param request: 調用DescribeLiveDomain所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveDomainRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveDomainResponse()
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


    def DescribeLiveDomainCert(self, request):
        """獲取域名證書訊息

        :param request: 調用DescribeLiveDomainCert所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveDomainCertRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveDomainCertResponse()
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


    def DescribeLiveDomains(self, request):
        """根據域名狀态、類型等訊息查詢用戶的域名訊息

        :param request: 調用DescribeLiveDomains所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveDomainsRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveDomainsResponse()
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


    def DescribeLiveForbidStreamList(self, request):
        """獲取禁推流清單

        :param request: 調用DescribeLiveForbidStreamList所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveForbidStreamListRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveForbidStreamListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveForbidStreamList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveForbidStreamListResponse()
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


    def DescribeLivePlayAuthKey(self, request):
        """查詢播放鑒權key

        :param request: 調用DescribeLivePlayAuthKey所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLivePlayAuthKeyRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLivePlayAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLivePlayAuthKeyResponse()
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


    def DescribeLivePushAuthKey(self, request):
        """查詢直播推流鑒權key

        :param request: 調用DescribeLivePushAuthKey所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLivePushAuthKeyRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLivePushAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLivePushAuthKeyResponse()
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


    def DescribeLiveRecordRules(self, request):
        """獲取錄制規則清單

        :param request: 調用DescribeLiveRecordRules所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveRecordRulesRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveRecordRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveRecordRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordRulesResponse()
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


    def DescribeLiveRecordTemplate(self, request):
        """獲取單個錄制範本

        :param request: 調用DescribeLiveRecordTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveRecordTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordTemplateResponse()
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


    def DescribeLiveRecordTemplates(self, request):
        """獲取錄制範本清單

        :param request: 調用DescribeLiveRecordTemplates所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveRecordTemplatesRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveRecordTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveRecordTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveRecordTemplatesResponse()
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


    def DescribeLiveSnapshotRules(self, request):
        """獲取截圖規則清單

        :param request: 調用DescribeLiveSnapshotRules所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveSnapshotRulesRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveSnapshotRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveSnapshotRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveSnapshotRulesResponse()
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


    def DescribeLiveSnapshotTemplate(self, request):
        """獲取單個截圖範本

        :param request: 調用DescribeLiveSnapshotTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveSnapshotTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveSnapshotTemplateResponse()
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


    def DescribeLiveSnapshotTemplates(self, request):
        """獲取截圖範本清單

        :param request: 調用DescribeLiveSnapshotTemplates所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveSnapshotTemplatesRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveSnapshotTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveSnapshotTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveSnapshotTemplatesResponse()
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


    def DescribeLiveStreamEventList(self, request):
        """用于查詢推斷流事件。

        注意：該介面可通過使用IsFilter進行過濾，返回推流曆史記錄。

        :param request: 調用DescribeLiveStreamEventList所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamEventListRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamEventListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamEventList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamEventListResponse()
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


    def DescribeLiveStreamOnlineInfo(self, request):
        """查詢在線推流訊息清單

        :param request: 調用DescribeLiveStreamOnlineInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamOnlineInfoRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamOnlineInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamOnlineInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamOnlineInfoResponse()
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


    def DescribeLiveStreamOnlineList(self, request):
        """返回正在直播中的流清單

        :param request: 調用DescribeLiveStreamOnlineList所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamOnlineListRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamOnlineListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamOnlineList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamOnlineListResponse()
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


    def DescribeLiveStreamPublishedList(self, request):
        """返回已經推過流的流清單

        :param request: 調用DescribeLiveStreamPublishedList所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamPublishedListRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamPublishedListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamPublishedList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamPublishedListResponse()
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


    def DescribeLiveStreamPushInfoList(self, request):
        """查詢所有實時流的推流訊息，包括用戶端IP，服務端IP，幀率，碼率，域名，開始推流時間。

        :param request: 調用DescribeLiveStreamPushInfoList所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamPushInfoListRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamPushInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamPushInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamPushInfoListResponse()
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


    def DescribeLiveStreamState(self, request):
        """返回直播中、無推流或者禁播等狀态

        :param request: 調用DescribeLiveStreamState所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamStateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveStreamStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveStreamState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveStreamStateResponse()
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


    def DescribeLiveTranscodeDetailInfo(self, request):
        """支援查詢某天的轉碼詳細訊息。
        注意：當前只支援查詢近30天内某天的詳細數據。

        :param request: 調用DescribeLiveTranscodeDetailInfo所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveTranscodeDetailInfoRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveTranscodeDetailInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveTranscodeDetailInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveTranscodeDetailInfoResponse()
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


    def DescribeLiveTranscodeRules(self, request):
        """獲取轉碼規則清單

        :param request: 調用DescribeLiveTranscodeRules所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveTranscodeRulesRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveTranscodeRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveTranscodeRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveTranscodeRulesResponse()
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


    def DescribeLiveTranscodeTemplate(self, request):
        """獲取單個轉碼範本

        :param request: 調用DescribeLiveTranscodeTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveTranscodeTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveTranscodeTemplateResponse()
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


    def DescribeLiveTranscodeTemplates(self, request):
        """獲取轉碼範本清單

        :param request: 調用DescribeLiveTranscodeTemplates所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveTranscodeTemplatesRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveTranscodeTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveTranscodeTemplatesResponse()
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


    def DescribeLiveWatermark(self, request):
        """獲取單個浮水印訊息

        :param request: 調用DescribeLiveWatermark所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveWatermarkRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveWatermarkResponse()
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


    def DescribeLiveWatermarkRules(self, request):
        """獲取浮水印規則清單

        :param request: 調用DescribeLiveWatermarkRules所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveWatermarkRulesRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveWatermarkRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveWatermarkRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveWatermarkRulesResponse()
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


    def DescribeLiveWatermarks(self, request):
        """查詢浮水印清單

        :param request: 調用DescribeLiveWatermarks所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveWatermarksRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLiveWatermarksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLiveWatermarks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLiveWatermarksResponse()
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


    def DescribeLogDownloadList(self, request):
        """批次獲取日志URL。

        :param request: 調用DescribeLogDownloadList所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeLogDownloadListRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeLogDownloadListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLogDownloadList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogDownloadListResponse()
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


    def DescribeProIspPlaySumInfoList(self, request):
        """查詢某段時間内每個 每個運營商的平均每秒流量，總流量，總請求數訊息。

        :param request: 調用DescribeProIspPlaySumInfoList所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeProIspPlaySumInfoListRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeProIspPlaySumInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProIspPlaySumInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProIspPlaySumInfoListResponse()
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


    def DescribeProvinceIspPlayInfoList(self, request):
        """查詢某 某運營商下行播放數據，包括頻寬，流量，請求數，并發連接數訊息。

        :param request: 調用DescribeProvinceIspPlayInfoList所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeProvinceIspPlayInfoListRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeProvinceIspPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProvinceIspPlayInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProvinceIspPlayInfoListResponse()
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


    def DescribePullStreamConfigs(self, request):
        """查詢拉流配置

        :param request: 調用DescribePullStreamConfigs所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribePullStreamConfigsRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribePullStreamConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePullStreamConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePullStreamConfigsResponse()
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


    def DescribeStreamDayPlayInfoList(self, request):
        """查詢天維度每條流的播放數據，包括總流量等。

        :param request: 調用DescribeStreamDayPlayInfoList所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeStreamDayPlayInfoListRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeStreamDayPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStreamDayPlayInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStreamDayPlayInfoListResponse()
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


    def DescribeStreamPlayInfoList(self, request):
        """查詢播放數據，支援按流名稱查詢詳細播放數據，也可按播放域名查詢詳細總數據。

        :param request: 調用DescribeStreamPlayInfoList所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DescribeStreamPlayInfoListRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DescribeStreamPlayInfoListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStreamPlayInfoList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStreamPlayInfoListResponse()
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


    def DropLiveStream(self, request):
        """斷開推流連接，但可以重新推流

        :param request: 調用DropLiveStream所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.DropLiveStreamRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.DropLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DropLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DropLiveStreamResponse()
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


    def EnableLiveDomain(self, request):
        """啓用狀态爲停用的直播域名

        :param request: 調用EnableLiveDomain所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.EnableLiveDomainRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.EnableLiveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableLiveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableLiveDomainResponse()
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


    def ForbidLiveDomain(self, request):
        """停用使用某個直播域名

        :param request: 調用ForbidLiveDomain所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ForbidLiveDomainRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ForbidLiveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ForbidLiveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForbidLiveDomainResponse()
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


    def ForbidLiveStream(self, request):
        """禁止某條流的推送，可以預設某個時刻将流恢複。

        :param request: 調用ForbidLiveStream所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ForbidLiveStreamRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ForbidLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ForbidLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForbidLiveStreamResponse()
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


    def ModifyLiveCallbackTemplate(self, request):
        """修改回調範本

        :param request: 調用ModifyLiveCallbackTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveCallbackTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveCallbackTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveCallbackTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveCallbackTemplateResponse()
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


    def ModifyLiveCert(self, request):
        """修改證書

        :param request: 調用ModifyLiveCert所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveCertRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveCertResponse()
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


    def ModifyLiveDomainCert(self, request):
        """修改域名和證書綁定訊息

        :param request: 調用ModifyLiveDomainCert所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveDomainCertRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveDomainCertResponse()
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


    def ModifyLivePlayAuthKey(self, request):
        """修改播放鑒權key

        :param request: 調用ModifyLivePlayAuthKey所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyLivePlayAuthKeyRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyLivePlayAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLivePlayAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLivePlayAuthKeyResponse()
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


    def ModifyLivePlayDomain(self, request):
        """修改播放域名訊息

        :param request: 調用ModifyLivePlayDomain所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyLivePlayDomainRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyLivePlayDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLivePlayDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLivePlayDomainResponse()
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


    def ModifyLivePushAuthKey(self, request):
        """修改直播推流鑒權key

        :param request: 調用ModifyLivePushAuthKey所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyLivePushAuthKeyRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyLivePushAuthKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLivePushAuthKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLivePushAuthKeyResponse()
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


    def ModifyLiveRecordTemplate(self, request):
        """修改錄制範本配置

        :param request: 調用ModifyLiveRecordTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveRecordTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveRecordTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveRecordTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveRecordTemplateResponse()
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


    def ModifyLiveSnapshotTemplate(self, request):
        """修改截圖範本配置

        :param request: 調用ModifyLiveSnapshotTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveSnapshotTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveSnapshotTemplateResponse()
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


    def ModifyLiveTranscodeTemplate(self, request):
        """修改轉碼範本配置

        :param request: 調用ModifyLiveTranscodeTemplate所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveTranscodeTemplateRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyLiveTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLiveTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLiveTranscodeTemplateResponse()
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


    def ModifyPullStreamConfig(self, request):
        """更新拉流配置

        :param request: 調用ModifyPullStreamConfig所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyPullStreamConfigRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyPullStreamConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPullStreamConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPullStreamConfigResponse()
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


    def ModifyPullStreamStatus(self, request):
        """修改直播拉流配置狀态

        :param request: 調用ModifyPullStreamStatus所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ModifyPullStreamStatusRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ModifyPullStreamStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPullStreamStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPullStreamStatusResponse()
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


    def ResumeDelayLiveStream(self, request):
        """恢複延遲播放設置

        :param request: 調用ResumeDelayLiveStream所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ResumeDelayLiveStreamRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ResumeDelayLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResumeDelayLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeDelayLiveStreamResponse()
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


    def ResumeLiveStream(self, request):
        """恢複某條流的推送。

        :param request: 調用ResumeLiveStream所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.ResumeLiveStreamRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.ResumeLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResumeLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeLiveStreamResponse()
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


    def SetLiveWatermarkStatus(self, request):
        """設置浮水印是否啓用

        :param request: 調用SetLiveWatermarkStatus所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.SetLiveWatermarkStatusRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.SetLiveWatermarkStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetLiveWatermarkStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetLiveWatermarkStatusResponse()
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


    def StopLiveRecord(self, request):
        """說明：錄制後的文件存放于點播平台。用戶如需使用錄制功能，需首先自行開通點播賬号并确保賬号可用。錄制文件存放後，相關費用（含儲存以及下行播放流量）按照點播平台計費方式收取，請參考對應文件。

        :param request: 調用StopLiveRecord所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.StopLiveRecordRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.StopLiveRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopLiveRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopLiveRecordResponse()
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


    def UnBindLiveDomainCert(self, request):
        """解綁域名證書

        :param request: 調用UnBindLiveDomainCert所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.UnBindLiveDomainCertRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.UnBindLiveDomainCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindLiveDomainCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindLiveDomainCertResponse()
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


    def UpdateLiveWatermark(self, request):
        """更新浮水印

        :param request: 調用UpdateLiveWatermark所需參數的結構體。
        :type request: :class:`taifucloudcloud.live.v20180801.models.UpdateLiveWatermarkRequest`
        :rtype: :class:`taifucloudcloud.live.v20180801.models.UpdateLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateLiveWatermark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateLiveWatermarkResponse()
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