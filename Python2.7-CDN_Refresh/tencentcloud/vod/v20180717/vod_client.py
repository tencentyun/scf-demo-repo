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
from taifucloudcloud.vod.v20180717 import models


class VodClient(AbstractClient):
    _apiVersion = '2018-07-17'
    _endpoint = 'vod.taifucloudcloudapi.com'


    def ApplyUpload(self, request):
        """* 該介面用於申請媒體文件（和封面文件）的上傳，獲取文件上傳到雲點播的元訊息（包括上傳路徑、上傳簽名等），用於後續上傳介面。
        * 上傳流程請參考 [服務端上傳綜述](/document/product/266/9759)。

        :param request: Request instance for ApplyUpload.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ApplyUploadRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ApplyUploadResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyUpload", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyUploadResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CommitUpload(self, request):
        """該介面用於确認媒體文件（和封面文件）上傳到Top Cloud 點播的結果，並儲存媒體訊息，返回文件的播放網址和文件 ID。

        :param request: Request instance for CommitUpload.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CommitUploadRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CommitUploadResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CommitUpload", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CommitUploadResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ComposeMedia(self, request):
        """該介面用於制作媒體文件，可以

        1. 對一個媒體文件進行剪輯，生成一個新的媒體文件；
        2. 對多個媒體文件進行裁剪拼接，生成一個新的媒體文件；
        3. 對多個媒體文件的媒體流進行裁剪拼接，生成一個新的媒體文件。

        如使用事件通知，事件通知的類型爲 [視訊合成完成](https://cloud.taifucloud.com/document/product/266/43000)。

        :param request: Request instance for ComposeMedia.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ComposeMediaRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ComposeMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ComposeMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ComposeMediaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ConfirmEvents(self, request):
        """* 開發者調用拉取事件通知，獲取到事件後，必須調用該介面來确認訊息已經收到；
        * 開發者獲取到事件句柄後，等待确認的有效時間爲 30 秒，超出 30 秒會報參數錯誤（4000）；
        * 更多參考事件通知的[可靠回調](https://cloud.taifucloud.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83)。

        :param request: Request instance for ConfirmEvents.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ConfirmEventsRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ConfirmEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ConfirmEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ConfirmEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAIAnalysisTemplate(self, request):
        """創建用戶自定義視訊内容分析範本，數量上限：50。

        :param request: Request instance for CreateAIAnalysisTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateAIAnalysisTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAIAnalysisTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAIAnalysisTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAIRecognitionTemplate(self, request):
        """創建用戶自定義視訊内容識别範本，數量上限：50。

        :param request: Request instance for CreateAIRecognitionTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateAIRecognitionTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAIRecognitionTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAIRecognitionTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAdaptiveDynamicStreamingTemplate(self, request):
        """創建轉自适應碼流範本，數量上限：100。

        :param request: Request instance for CreateAdaptiveDynamicStreamingTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAdaptiveDynamicStreamingTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAdaptiveDynamicStreamingTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAnimatedGraphicsTemplate(self, request):
        """創建用戶自定義轉動圖範本，數量上限：16。

        :param request: Request instance for CreateAnimatedGraphicsTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateAnimatedGraphicsTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAnimatedGraphicsTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAnimatedGraphicsTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """* 用於對媒體進行分類管理；
        * 該介面不影響既有媒體的分類，如需修改媒體分類，請調用[修改媒體文件屬性](/document/product/266/31762)介面。
        * 分類層次不可超過 4 層。
        * 每個分類的子類數量不可超過 500 個。

        :param request: Request instance for CreateClass.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateClassRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateClassResponse`

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


    def CreateContentReviewTemplate(self, request):
        """創建用戶自定義視訊内容審核範本，數量上限：50。

        :param request: Request instance for CreateContentReviewTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateContentReviewTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateContentReviewTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateContentReviewTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateImageSpriteTemplate(self, request):
        """創建用戶自定義雪碧圖範本，數量上限：16。

        :param request: Request instance for CreateImageSpriteTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateImageSpriteTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateImageSpriteTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImageSpriteTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePersonSample(self, request):
        """該介面用於創建人物樣本，用於通過人臉識别等技術，進行内容識别、内容審核等視訊處理。

        :param request: Request instance for CreatePersonSample.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreatePersonSampleRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreatePersonSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePersonSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePersonSampleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateProcedureTemplate(self, request):
        """創建用戶自定義的任務流範本，範本上限：50。

        :param request: Request instance for CreateProcedureTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateProcedureTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProcedureTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProcedureTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSampleSnapshotTemplate(self, request):
        """創建用戶自定義采樣截圖範本，數量上限：16。

        :param request: Request instance for CreateSampleSnapshotTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateSampleSnapshotTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateSampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSampleSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSampleSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSnapshotByTimeOffsetTemplate(self, request):
        """創建用戶自定義指定時間點截圖範本，數量上限：16。

        :param request: Request instance for CreateSnapshotByTimeOffsetTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateSnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSnapshotByTimeOffsetTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSnapshotByTimeOffsetTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSubAppId(self, request):
        """該介面用於創建點播子應用。

        :param request: Request instance for CreateSubAppId.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateSubAppIdRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateSubAppIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubAppId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubAppIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSuperPlayerConfig(self, request):
        """創建超級播放器配置，數量上限：100。

        :param request: Request instance for CreateSuperPlayerConfig.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateSuperPlayerConfigRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateSuperPlayerConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSuperPlayerConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSuperPlayerConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTranscodeTemplate(self, request):
        """創建用戶自定義轉碼範本，數量上限：100。

        :param request: Request instance for CreateTranscodeTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateTranscodeTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWatermarkTemplate(self, request):
        """創建用戶自定義浮水印範本，數量上限：1000。

        :param request: Request instance for CreateWatermarkTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateWatermarkTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWatermarkTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWatermarkTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWordSamples(self, request):
        """該介面用於批次創建關鍵詞樣本，樣本用於通過OCR、ASR技術，進行内容審核、内容識别等視訊處理。

        :param request: Request instance for CreateWordSamples.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.CreateWordSamplesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.CreateWordSamplesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWordSamples", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWordSamplesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAIAnalysisTemplate(self, request):
        """删除用戶自定義視訊内容分析範本。

        注意：範本 ID 爲 10000 以下的爲系統預置範本，不允許删除。

        :param request: Request instance for DeleteAIAnalysisTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteAIAnalysisTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAIAnalysisTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAIAnalysisTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAIRecognitionTemplate(self, request):
        """删除用戶自定義視訊内容識别範本。

        :param request: Request instance for DeleteAIRecognitionTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteAIRecognitionTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAIRecognitionTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAIRecognitionTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAdaptiveDynamicStreamingTemplate(self, request):
        """删除轉自适應碼流範本

        :param request: Request instance for DeleteAdaptiveDynamicStreamingTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAdaptiveDynamicStreamingTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAdaptiveDynamicStreamingTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAnimatedGraphicsTemplate(self, request):
        """删除用戶自定義轉動圖範本。

        :param request: Request instance for DeleteAnimatedGraphicsTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteAnimatedGraphicsTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAnimatedGraphicsTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAnimatedGraphicsTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """* 僅當待删分類無子分類且無媒體關聯情況下，可删除分類；
        * 否則，請先執行[删除媒體](/document/product/266/31764)及子分類，再删除該分類；

        :param request: Request instance for DeleteClass.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteClassRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteClassResponse`

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


    def DeleteContentReviewTemplate(self, request):
        """删除用戶自定義視訊内容審核範本。

        :param request: Request instance for DeleteContentReviewTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteContentReviewTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteContentReviewTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteContentReviewTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteImageSpriteTemplate(self, request):
        """删除雪碧圖範本。

        :param request: Request instance for DeleteImageSpriteTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteImageSpriteTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImageSpriteTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImageSpriteTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMedia(self, request):
        """* 删除媒體及其對應的視訊處理文件（如轉碼視訊、雪碧圖、截圖、 發布視訊等）；
        * 可單獨删除指定 ID 的視訊文件下的轉碼，或者 發布文件；

        :param request: Request instance for DeleteMedia.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteMediaRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMediaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePersonSample(self, request):
        """該介面用於根據人物 ID，删除人物樣本。

        :param request: Request instance for DeletePersonSample.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeletePersonSampleRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeletePersonSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePersonSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePersonSampleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteProcedureTemplate(self, request):
        """删除用戶自定義的任務流範本。

        :param request: Request instance for DeleteProcedureTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteProcedureTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProcedureTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProcedureTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSampleSnapshotTemplate(self, request):
        """删除用戶自定義采樣截圖範本。

        :param request: Request instance for DeleteSampleSnapshotTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteSampleSnapshotTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteSampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSampleSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSampleSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSnapshotByTimeOffsetTemplate(self, request):
        """删除用戶自定義指定時間點截圖範本。

        :param request: Request instance for DeleteSnapshotByTimeOffsetTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteSnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSnapshotByTimeOffsetTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSnapshotByTimeOffsetTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSuperPlayerConfig(self, request):
        """删除超級播放器配置。
        *注：系統預置播放器配置不允許删除。*

        :param request: Request instance for DeleteSuperPlayerConfig.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteSuperPlayerConfigRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteSuperPlayerConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSuperPlayerConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSuperPlayerConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTranscodeTemplate(self, request):
        """删除用戶自定義轉碼範本。

        :param request: Request instance for DeleteTranscodeTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteTranscodeTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWatermarkTemplate(self, request):
        """删除用戶自定義浮水印範本。

        :param request: Request instance for DeleteWatermarkTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteWatermarkTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWatermarkTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWatermarkTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWordSamples(self, request):
        """該介面用於批次删除關鍵詞樣本。

        :param request: Request instance for DeleteWordSamples.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DeleteWordSamplesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DeleteWordSamplesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWordSamples", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWordSamplesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAIAnalysisTemplates(self, request):
        """根據視訊内容分析範本唯一標識，獲取視訊内容分析範本詳情清單。返回結果包含符合條件的所有用戶自定義視訊内容分析範本及[系統預置視訊内容分析範本](https://cloud.taifucloud.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.88.86.E6.9E.90.E6.A8.A1.E6.9D.BF)。

        :param request: Request instance for DescribeAIAnalysisTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeAIAnalysisTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeAIAnalysisTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAIAnalysisTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAIAnalysisTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAIRecognitionTemplates(self, request):
        """根據視訊内容識别範本唯一標識，獲取視訊内容識别範本詳情清單。返回結果包含符合條件的所有用戶自定義視訊内容識别範本及[系統預置視訊内容識别範本](https://cloud.taifucloud.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E8.AF.86.E5.88.AB.E6.A8.A1.E6.9D.BF)。

        :param request: Request instance for DescribeAIRecognitionTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeAIRecognitionTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeAIRecognitionTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAIRecognitionTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAIRecognitionTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAdaptiveDynamicStreamingTemplates(self, request):
        """查詢轉自适應碼流範本，支援根據條件，分頁查詢。

        :param request: Request instance for DescribeAdaptiveDynamicStreamingTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeAdaptiveDynamicStreamingTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeAdaptiveDynamicStreamingTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAdaptiveDynamicStreamingTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAdaptiveDynamicStreamingTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAllClass(self, request):
        """* 獲得用戶的所有分類訊息。

        :param request: Request instance for DescribeAllClass.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeAllClassRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeAllClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAllClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAllClassResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAnimatedGraphicsTemplates(self, request):
        """查詢轉動圖範本清單，支援根據條件，分頁查詢。

        :param request: Request instance for DescribeAnimatedGraphicsTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeAnimatedGraphicsTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeAnimatedGraphicsTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAnimatedGraphicsTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAnimatedGraphicsTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCDNUsageData(self, request):
        """該介面用於查詢點播 CDN 的流量、頻寬等統計數據。
           1. 可以查詢最近365天内的 CDN 用量數據。
           2.  查詢時間跨度不超過90天。
           3. 可以指定用量數據的時間粒度，支援5分鍾、1小時、1天的時間粒度。
           4.  流量爲查詢時間粒度内的總流量，頻寬爲查詢時間粒度内的峰值頻寬。

        :param request: Request instance for DescribeCDNUsageData.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeCDNUsageDataRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeCDNUsageDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCDNUsageData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCDNUsageDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeContentReviewTemplates(self, request):
        """根據視訊内容審核範本唯一標識，獲取視訊内容審核範本詳情清單。返回結果包含符合條件的所有用戶自定義範本及[系統預置内容審核範本](https://cloud.taifucloud.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.A7.86.E9.A2.91.E5.86.85.E5.AE.B9.E5.AE.A1.E6.A0.B8.E6.A8.A1.E6.9D.BF)。

        :param request: Request instance for DescribeContentReviewTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeContentReviewTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeContentReviewTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContentReviewTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContentReviewTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageSpriteTemplates(self, request):
        """查詢雪碧圖範本，支援根據條件，分頁查詢。

        :param request: Request instance for DescribeImageSpriteTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeImageSpriteTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeImageSpriteTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageSpriteTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageSpriteTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMediaInfos(self, request):
        """1. 該介面可以獲取多個媒體文件的多種訊息，包括：
            1. 基礎訊息（basicInfo）：包括媒體名稱、分類、播放網址、封面圖片等。
            2. 元訊息（metaData）：包括大小、時長、視訊流訊息、音訊流訊息等。
            3. 轉碼結果訊息（transcodeInfo）：包括該媒體轉碼生成的各種規格的媒體網址、視訊流參數、音訊流參數等。
            4. 轉動圖結果訊息（animatedGraphicsInfo）：對視訊轉動圖（如 gif）後的動圖訊息。
            5. 采樣截圖訊息（sampleSnapshotInfo）：對視訊采樣截圖後的截圖訊息。
            6. 雪碧圖訊息（imageSpriteInfo）：對視訊截取雪碧圖後的雪碧圖訊息。
            7. 指定時間點截圖訊息（snapshotByTimeOffsetInfo）：對視訊依照指定時間點截圖後，的截圖訊息。
            8. 視訊打點訊息（keyFrameDescInfo）：對視訊設置的打點訊息。
            9. 轉自适應碼流訊息（adaptiveDynamicStreamingInfo）：包括規格、加密類型、打包格式等相關訊息。
        2. 可以指定回包只返回部分訊息。

        :param request: Request instance for DescribeMediaInfos.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeMediaInfosRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeMediaInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaInfosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMediaProcessUsageData(self, request):
        """該介面返回查詢時間範圍内每天使用的視訊處理用量訊息。
           1. 可以查詢最近365天内的視訊處理統計數據。
           2. 查詢時間跨度不超過90天。

        :param request: Request instance for DescribeMediaProcessUsageData.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeMediaProcessUsageDataRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeMediaProcessUsageDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaProcessUsageData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaProcessUsageDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePersonSamples(self, request):
        """該介面用於查詢人物樣本訊息，支援根據人物 ID、名稱、標簽，分頁查詢。

        :param request: Request instance for DescribePersonSamples.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribePersonSamplesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribePersonSamplesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonSamples", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonSamplesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProcedureTemplates(self, request):
        """根據任務流範本名字，獲取任務流範本詳情清單。

        :param request: Request instance for DescribeProcedureTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeProcedureTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeProcedureTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProcedureTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProcedureTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReviewDetails(self, request):
        """該介面返回查詢時間範圍内每天使用的視訊内容審核時長數據，單位： 秒。

        1. 可以查詢最近365天内的視訊内容審核時長統計數據。
        2. 查詢時間跨度不超過90天。

        :param request: Request instance for DescribeReviewDetails.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeReviewDetailsRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeReviewDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReviewDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReviewDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSampleSnapshotTemplates(self, request):
        """查詢采樣截圖範本，支援根據條件，分頁查詢。

        :param request: Request instance for DescribeSampleSnapshotTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeSampleSnapshotTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeSampleSnapshotTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSampleSnapshotTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSampleSnapshotTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSnapshotByTimeOffsetTemplates(self, request):
        """查詢指定時間點截圖範本，支援根據條件，分頁查詢。

        :param request: Request instance for DescribeSnapshotByTimeOffsetTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeSnapshotByTimeOffsetTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeSnapshotByTimeOffsetTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSnapshotByTimeOffsetTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSnapshotByTimeOffsetTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStorageData(self, request):
        """查詢儲存空間使用情況和文件數量。

        :param request: Request instance for DescribeStorageData.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeStorageDataRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeStorageDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStorageData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStorageDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStorageDetails(self, request):
        """該介面返回查詢時間範圍内使用的點播儲存空間，單位：位元。
           1. 可以查詢最近365天内的儲存空間數據；
           2. 查詢時間跨度不超過90天；
           3. 分鍾粒度查詢跨度不超過5天；
           4. 小時粒度查詢跨度不超過10天。

        :param request: Request instance for DescribeStorageDetails.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeStorageDetailsRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeStorageDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStorageDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStorageDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSubAppIds(self, request):
        """該介面用於獲取當前賬號有權限的子應用清單，包含主應用。若尚未開通子應用功能，介面将返回
         FailedOperation。

        :param request: Request instance for DescribeSubAppIds.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeSubAppIdsRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeSubAppIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubAppIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubAppIdsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSuperPlayerConfigs(self, request):
        """查詢超級播放器配置，支援根據條件，分頁查詢。

        :param request: Request instance for DescribeSuperPlayerConfigs.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeSuperPlayerConfigsRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeSuperPlayerConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSuperPlayerConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSuperPlayerConfigsResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """通過任務 ID 查詢任務的執行狀态和結果的詳細訊息（最多可以查詢3天之内提交的任務）。

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeTaskDetailRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeTaskDetailResponse`

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
        """* 該介面用於查詢任務清單；
        * 當清單數據比較多時，單次介面調用無法拉取整個清單，可通過 ScrollToken 參數，分批拉取；
        * 只能查詢到最近三天（72 小時）内的任務。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeTasksRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeTasksResponse`

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


    def DescribeTranscodeTemplates(self, request):
        """根據轉碼範本唯一標識，獲取轉碼範本詳情清單。返回結果包含符合條件的所有用戶自定義範本及[系統預置轉碼範本](https://cloud.taifucloud.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。

        :param request: Request instance for DescribeTranscodeTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeTranscodeTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTranscodeTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTranscodeTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWatermarkTemplates(self, request):
        """查詢用戶自定義浮水印範本，支援根據條件，分頁查詢。

        :param request: Request instance for DescribeWatermarkTemplates.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeWatermarkTemplatesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeWatermarkTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWatermarkTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWatermarkTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWordSamples(self, request):
        """該介面用於根據應用場景、關鍵詞、標簽，分頁查詢關鍵詞樣本訊息。

        :param request: Request instance for DescribeWordSamples.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.DescribeWordSamplesRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.DescribeWordSamplesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWordSamples", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWordSamplesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EditMedia(self, request):
        """對視訊進行編輯（剪輯、拼接等），生成一個新的點播視訊。編輯的功能包括：

        1. 對點播中的一個文件進行剪輯，生成一個新的視訊；
        2. 對點播中的多個文件進行拼接，生成一個新的視訊；
        3. 對點播中的多個文件進行剪輯，然後再拼接，生成一個新的視訊；
        4. 對點播中的一個流，直接生成一個新的視訊；
        5. 對點播中的一個流進行剪輯，生成一個新的視訊；
        6. 對點播中的多個流進行拼接，生成一個新的視訊；
        7. 對點播中的多個流進行剪輯，然後拼接，生成一個新的視訊。

        對於生成的新視訊，還可以指定生成後的視訊是否要執行任務流。

        >當對直播流做剪輯、拼接等操作時，請确保流結束後再操作。否則生成的視訊可能不完整。

        如使用事件通知，事件通知的類型爲 [視訊編輯完成](https://cloud.taifucloud.com/document/product/266/33794)。

        :param request: Request instance for EditMedia.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.EditMediaRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.EditMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EditMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EditMediaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExecuteFunction(self, request):
        """本介面僅用於定制開發的特殊場景，除非雲點播客服人員主動告知您需要使用本介面，其它情況請勿調用。

        :param request: Request instance for ExecuteFunction.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ExecuteFunctionRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ExecuteFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExecuteFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExecuteFunctionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ForbidMediaDistribution(self, request):
        """* 對媒體禁播後，除了點播控制台預覽，其他場景訪問視訊各種資源的 URL（原始文件、轉碼輸出文件、截圖等）均會返回 403。
          禁播/解禁操作全網生效時間約 5~10 分鍾。

        :param request: Request instance for ForbidMediaDistribution.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ForbidMediaDistributionRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ForbidMediaDistributionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ForbidMediaDistribution", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForbidMediaDistributionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def LiveRealTimeClip(self, request):
        """直播即時剪輯，是指在直播過程中（即直播尚未結束時），客戶可以在過往直播内容中選擇一段，實時生成一個新的視訊（HLS 格式），開發者可以将其立即分享出去，或者長久保存起來。

        Top Cloud 點播支援兩種即時剪輯模式：
        - 剪輯固化：将剪輯出來的視訊保存成獨立的視訊，擁有獨立 FileId；适用於将精彩片段**長久保存**的場景；
        - 剪輯不固化：剪輯得到的視訊附屬於直播錄制文件，沒有獨立 FileId；适用於将精彩片段**臨時分享**的場景。

        注意：
        - 使用直播即時剪輯功能的前提是：目標直播流開啓了[時移回看](https://cloud.taifucloud.com/document/product/267/32742)功能。
        - 直播即時剪輯是基於直播錄制生成的 m3u8 文件進行的，故而其最小剪輯精度爲一個 ts 切片，無法實現秒級或者更爲精确的剪輯精度。


        ### 剪輯固化
        所謂剪輯固化，是指将剪輯出來的視訊是保存成一個獨立的視訊（擁有獨立的 FileId）。其生命週期不受原始直播錄制視訊影響（即使原始錄制視訊被删除，剪輯結果也不會受到任何影響）；也可以對其進行轉碼、 發布等二次處理。

        舉例如下：一場完整的足球比賽，直播錄制出來的原始視訊可能長達 2 個小時，客戶出於節省成本的目的可以對這個視訊儲存 2 個月，但對於直播即時剪輯的「精彩時刻」視訊卻可以指定儲存更長時間，同時可以單獨對「精彩時刻」視訊進行轉碼、 發布等額外的點播操作，這時候可以選擇直播即時剪輯並且固化的方案。

        剪輯固化的優勢在於其生命週期與原始錄制視訊相互獨立，可以獨立管理、長久保存。

        ### 剪輯不固化
        所謂剪輯不固化，是指剪輯所得到的結果（m3u8 文件）與直播錄制視訊共享相同的 ts 分片，新生成的視訊不是一個獨立完整的視訊（沒有獨立 FileId，只有播放 URL），其有效期與直播錄制的完整視訊有效期是一緻的。一旦直播錄制出來的視訊被删除，也會導緻該片段無法播放。

        剪輯不固化，由於其剪輯結果不是一個獨立的視訊，因而也不會納入點播媒資視訊管理（例如控制台的視訊總數不會統計這一片段）中，也無法單獨針對這個片段做轉碼、 發布等任何視訊處理操作。

        剪輯不固化的優勢在於其剪輯操作十分“輕量化”，不會産生額外的儲存開銷。但其不足之處在於生命週期與原始錄制視訊相同，且無法進一步進行轉碼等視訊處理。

        :param request: Request instance for LiveRealTimeClip.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.LiveRealTimeClipRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.LiveRealTimeClipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LiveRealTimeClip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LiveRealTimeClipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAIAnalysisTemplate(self, request):
        """修改用戶自定義視訊内容分析範本。

        注意：範本 ID 10000 以下的爲系統預置範本，不允許修改。

        :param request: Request instance for ModifyAIAnalysisTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyAIAnalysisTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAIAnalysisTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAIAnalysisTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAIRecognitionTemplate(self, request):
        """修改用戶自定義視訊内容識别範本。

        :param request: Request instance for ModifyAIRecognitionTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyAIRecognitionTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAIRecognitionTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAIRecognitionTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAdaptiveDynamicStreamingTemplate(self, request):
        """修改轉自适應碼流範本

        :param request: Request instance for ModifyAdaptiveDynamicStreamingTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAdaptiveDynamicStreamingTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAdaptiveDynamicStreamingTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAnimatedGraphicsTemplate(self, request):
        """修改用戶自定義轉動圖範本。

        :param request: Request instance for ModifyAnimatedGraphicsTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyAnimatedGraphicsTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAnimatedGraphicsTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAnimatedGraphicsTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClass(self, request):
        """修改媒體分類屬性。

        :param request: Request instance for ModifyClass.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyClassRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyClassResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClass", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClassResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyContentReviewTemplate(self, request):
        """修改用戶自定義視訊内容審核範本。

        :param request: Request instance for ModifyContentReviewTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyContentReviewTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyContentReviewTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyContentReviewTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyImageSpriteTemplate(self, request):
        """修改用戶自定義雪碧圖範本。

        :param request: Request instance for ModifyImageSpriteTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyImageSpriteTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyImageSpriteTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImageSpriteTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMediaInfo(self, request):
        """修改媒體文件的屬性，包括分類、名稱、描述、標簽、過期時間、打點訊息、視訊封面等。

        :param request: Request instance for ModifyMediaInfo.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyMediaInfoRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyMediaInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMediaInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMediaInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPersonSample(self, request):
        """該介面用於根據人物 ID，修改人物樣本訊息，包括名稱、描述的修改，以及人臉、標簽的添加、删除、重置操作。人臉删除操作需保證至少剩餘 1 張圖片，否則，請使用重置操作。

        :param request: Request instance for ModifyPersonSample.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyPersonSampleRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyPersonSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonSampleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySampleSnapshotTemplate(self, request):
        """修改用戶自定義采樣截圖範本。

        :param request: Request instance for ModifySampleSnapshotTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifySampleSnapshotTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifySampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySampleSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySampleSnapshotTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySnapshotByTimeOffsetTemplate(self, request):
        """修改用戶自定義指定時間點截圖範本。

        :param request: Request instance for ModifySnapshotByTimeOffsetTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifySnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifySnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySnapshotByTimeOffsetTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySnapshotByTimeOffsetTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySubAppIdInfo(self, request):
        """該介面用於修改子應用訊息，但不允許修改主應用訊息。

        :param request: Request instance for ModifySubAppIdInfo.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifySubAppIdInfoRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifySubAppIdInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubAppIdInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubAppIdInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySubAppIdStatus(self, request):
        """該介面用於啓用、停用子應用。被停用的子應用将封停對應域名，並限制控制台訪問。

        :param request: Request instance for ModifySubAppIdStatus.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifySubAppIdStatusRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifySubAppIdStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubAppIdStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubAppIdStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySuperPlayerConfig(self, request):
        """修改超級播放器配置。

        :param request: Request instance for ModifySuperPlayerConfig.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifySuperPlayerConfigRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifySuperPlayerConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySuperPlayerConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySuperPlayerConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTranscodeTemplate(self, request):
        """修改用戶自定義轉碼範本訊息。

        :param request: Request instance for ModifyTranscodeTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyTranscodeTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTranscodeTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyWatermarkTemplate(self, request):
        """修改用戶自定義浮水印範本，水印類型不允許修改。

        :param request: Request instance for ModifyWatermarkTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyWatermarkTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyWatermarkTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWatermarkTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyWordSample(self, request):
        """該介面用於修改關鍵詞的應用場景、標簽，關鍵詞本身不可修改，如需修改，可删除重建。

        :param request: Request instance for ModifyWordSample.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ModifyWordSampleRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ModifyWordSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyWordSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWordSampleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ParseStreamingManifest(self, request):
        """上傳 HLS 視訊時，解析索引文件内容，返回待上傳的分片文件清單。分片文件路徑必須是當前目錄或子目錄的相對路徑，不能是 URL，不能是絕對路徑。

        :param request: Request instance for ParseStreamingManifest.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ParseStreamingManifestRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ParseStreamingManifestResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ParseStreamingManifest", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ParseStreamingManifestResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ProcessMedia(self, request):
        """對點播中的影音媒體發起處理任務，功能包括：
        1. 視訊轉碼（帶浮水印）；
        2. 視訊轉動圖；
        3. 對視訊按指定時間點截圖；
        4. 對視訊采樣截圖；
        5. 對視訊截圖雪碧圖；
        6. 對視訊截取一張圖做封面；
        7. 對視訊轉自适應碼流（並加密）；
        8. 智慧内容審核（ 、鑒恐、鑒政）；
        9. 智慧内容分析（標簽、分類、封面、按幀標簽）；
        10. 智慧内容識别（視訊片頭片尾、人臉、文本全文、文本關鍵詞、語音全文、語音關鍵詞、物體）。

        如使用事件通知，事件通知的類型爲 [任務流狀态變更](https://cloud.taifucloud.com/document/product/266/9636)。

        :param request: Request instance for ProcessMedia.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ProcessMediaRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ProcessMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ProcessMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ProcessMediaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ProcessMediaByProcedure(self, request):
        """使用任務流範本，對點播中的視訊發起處理任務。
        有兩種方式創建任務流範本：
        1. 在控制台上創建和修改任務流範本；
        2. 通過任務流範本介面創建任務流範本。

        如使用事件通知，事件通知的類型爲 [任務流狀态變更](https://cloud.taifucloud.com/document/product/266/9636)。

        :param request: Request instance for ProcessMediaByProcedure.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ProcessMediaByProcedureRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ProcessMediaByProcedureResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ProcessMediaByProcedure", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ProcessMediaByProcedureResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ProcessMediaByUrl(self, request):
        """對來源爲 URL 的影音媒體發起處理任務，功能包括：

        1. 智慧内容審核（ 、鑒恐、鑒政）；
        2. 智慧内容分析（標簽、分類、封面、按幀標簽）；
        3. 智慧内容識别（視訊片頭片尾、人臉、文本全文、文本關鍵詞、語音全文、語音關鍵詞、物體）。

        :param request: Request instance for ProcessMediaByUrl.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ProcessMediaByUrlRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ProcessMediaByUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ProcessMediaByUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ProcessMediaByUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PullEvents(self, request):
        """* 該介面用於業務服務器以 [可靠回調](https://cloud.taifucloud.com/document/product/266/33779#.E5.8F.AF.E9.9D.A0.E5.9B.9E.E8.B0.83) 的方式獲取事件通知；
        * 介面爲長輪詢模式，即：如果服務端存在未消費事件，則立即返回給請求方；如果服務端沒有未消費事件，則後台會将請求挂起，直到有新的事件産生爲止；
        * 請求最多挂起5秒，建議請求方将超時時間設置爲10秒；
        * 若該介面有事件返回，調用方必須在<font color="red">30秒</font>内調用 [确認事件通知](https://cloud.taifucloud.com/document/product/266/33434) 介面，确認事件通知已經處理，否則該事件通知在<font color="red">30秒</font>後會再次被拉取到。

        :param request: Request instance for PullEvents.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.PullEventsRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.PullEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PullEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PullEventsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PullUpload(self, request):
        """該介面用於将一個網絡上的視訊拉取到雲點播平台。

        :param request: Request instance for PullUpload.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.PullUploadRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.PullUploadResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PullUpload", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PullUploadResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PushUrlCache(self, request):
        """1. 預熱指定的 URL 清單。
        2. URL 的域名必須已在雲點播中注冊。
        3. 單次請求最多指定20個 URL。

        :param request: Request instance for PushUrlCache.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.PushUrlCacheRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.PushUrlCacheResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PushUrlCache", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PushUrlCacheResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetProcedureTemplate(self, request):
        """重新設置用戶自定義任務流範本的内容。

        :param request: Request instance for ResetProcedureTemplate.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.ResetProcedureTemplateRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.ResetProcedureTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetProcedureTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetProcedureTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchMedia(self, request):
        """搜索媒體訊息，支援多種條件篩選，以及支援對返回結果排序、過濾等功能，具體包括：
        - 根據媒體文件名或描述訊息進行模糊搜索。
        - 根據媒體分類、標簽進行檢索。
            - 指定分類集合 ClassIds（見輸入參數），返回滿足集合中任意分類的媒體。例如：媒體分類有電影、電視劇、綜藝，其中電影分類下又有子分類曆史片、動作片、言情片。如果 ClassIds 指定了電影、電視劇，那麽電影和電視劇下的所有子分類都會返回；而如果 ClassIds 指定的是曆史片、動作片，那麽只有這2個子分類下的媒體才會返回。
            - 指定標簽集合 Tags（見輸入參數），返回滿足集合中任意標簽的媒體。例如：媒體標簽有二次元、宮鬥、鬼畜，如果 Tags 指定了二次元、鬼畜2個標簽，那麽只要符合這2個標簽中任意一個的媒體都會被檢索出來。
        - 允許指定篩選某一來源 Source（見輸入參數）的媒體。
        - 允許根據直播推流碼、Vid（見輸入參數）篩選直播錄制的媒體。
        - 允許根據媒體的創建範圍篩選媒體。
        - 允許對上述條件進行任意組合，檢索同時滿足以上條件的媒體。例如：篩選創建時間在2018年12月1日到2018年12月8日之間、分類爲電影、帶有宮鬥標簽的媒體。
        - 允許對結果進行排序並分頁返回，通過 Offset 和 Limit （見輸入參數）來控制分頁。

        <div id="maxResultsDesc">介面返回結果數限制：</div>
        - <b><a href="#p_offset">Offset</a> 和 <a href="#p_limit">Limit</a> 兩個參數影響單次分頁查詢結果數。特别注意：當這2個值都缺省時，本介面最多只返回10條查詢結果。</b>
        - <b>最大支援返回5000條搜索結果，超出部分不再支援查詢。如果搜索結果量太大，建議使用更精細的篩選條件來減少搜索結果。</b>

        :param request: Request instance for SearchMedia.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.SearchMediaRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.SearchMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchMediaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SimpleHlsClip(self, request):
        """對 HLS 視訊進行按時間段裁剪。

        注意：裁剪出來的視訊與原始視訊共用 ts，僅生成新的 m3u8。原始視訊删除後，該裁剪視訊也會被删除。

        :param request: Request instance for SimpleHlsClip.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.SimpleHlsClipRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.SimpleHlsClipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SimpleHlsClip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SimpleHlsClipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def WeChatMiniProgramPublish(self, request):
        """将點播視訊發布到 小程式，供 小程式播放器播放。

        :param request: Request instance for WeChatMiniProgramPublish.
        :type request: :class:`taifucloudcloud.vod.v20180717.models.WeChatMiniProgramPublishRequest`
        :rtype: :class:`taifucloudcloud.vod.v20180717.models.WeChatMiniProgramPublishResponse`

        """
        try:
            params = request._serialize()
            body = self.call("WeChatMiniProgramPublish", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WeChatMiniProgramPublishResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)