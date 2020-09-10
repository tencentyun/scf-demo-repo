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
from tencentcloud.mps.v20190612 import models


class MpsClient(AbstractClient):
    _apiVersion = '2019-06-12'
    _endpoint = 'mps.tencentcloudapi.com'


    def CreateAIAnalysisTemplate(self, request):
        """創建用戶自定義内容分析範本，數量上限：50。

        :param request: Request instance for CreateAIAnalysisTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAIAnalysisTemplateResponse`

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
        """創建用戶自定義内容識别範本，數量上限：50。

        :param request: Request instance for CreateAIRecognitionTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAIRecognitionTemplateResponse`

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


    def CreateAnimatedGraphicsTemplate(self, request):
        """創建用戶自定義轉動圖範本，數量上限：16。

        :param request: Request instance for CreateAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAnimatedGraphicsTemplateResponse`

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


    def CreateContentReviewTemplate(self, request):
        """創建用戶自定義内容審核範本，數量上限：50。

        :param request: Request instance for CreateContentReviewTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateContentReviewTemplateResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateImageSpriteTemplateResponse`

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
        """該介面用于創建人物樣本，用于通過人臉識别等技術，進行内容識别、内容審核等視訊處理。

        :param request: Request instance for CreatePersonSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreatePersonSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreatePersonSampleResponse`

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


    def CreateSampleSnapshotTemplate(self, request):
        """創建用戶自定義采樣截圖範本，數量上限：16。

        :param request: Request instance for CreateSampleSnapshotTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateSampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateSampleSnapshotTemplateResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateSnapshotByTimeOffsetTemplateResponse`

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


    def CreateTranscodeTemplate(self, request):
        """創建用戶自定義轉碼範本，數量上限：1000。

        :param request: Request instance for CreateTranscodeTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateTranscodeTemplateResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateWatermarkTemplateResponse`

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
        """該介面用于批次創建關鍵詞樣本，樣本用于通過OCR、ASR技術，進行内容審核、内容識别等視訊處理。

        :param request: Request instance for CreateWordSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateWordSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateWordSamplesResponse`

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


    def CreateWorkflow(self, request):
        """對 COS 中指定 Bucket 的目錄下上傳的媒體文件，設置處理規則，包括：
        1. 視訊轉碼（帶浮水印）；
        2. 視訊轉動圖；
        3. 對視訊按指定時間點截圖；
        4. 對視訊采樣截圖；
        5. 對視訊截圖雪碧圖；
        6. 對視訊轉自适應碼流；
        7. 智慧内容審核（鑒黃、鑒恐、鑒政）；
        8. 智慧内容分析（标簽、分類、封面、按幀标簽）；
        9. 智慧内容識别（人臉、文本全文、文本關鍵詞、語音全文、語音關鍵詞）。

        注意：創建工作流成功後是禁用狀态，需要手動啓用。

        :param request: Request instance for CreateWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateWorkflowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWorkflow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWorkflowResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """删除用戶自定義内容分析範本。

        注意：範本 ID 爲 10000 以下的爲系統預置範本，不允許删除。

        :param request: Request instance for DeleteAIAnalysisTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAIAnalysisTemplateResponse`

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
        """删除用戶自定義内容識别範本。

        :param request: Request instance for DeleteAIRecognitionTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAIRecognitionTemplateResponse`

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


    def DeleteAnimatedGraphicsTemplate(self, request):
        """删除用戶自定義轉動圖範本。

        :param request: Request instance for DeleteAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAnimatedGraphicsTemplateResponse`

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


    def DeleteContentReviewTemplate(self, request):
        """删除用戶自定義内容審核範本。

        :param request: Request instance for DeleteContentReviewTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteContentReviewTemplateResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteImageSpriteTemplateResponse`

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


    def DeletePersonSample(self, request):
        """該介面用于根據人物 ID，删除人物樣本。

        :param request: Request instance for DeletePersonSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeletePersonSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeletePersonSampleResponse`

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


    def DeleteSampleSnapshotTemplate(self, request):
        """删除用戶自定義采樣截圖範本。

        :param request: Request instance for DeleteSampleSnapshotTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteSampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteSampleSnapshotTemplateResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteSnapshotByTimeOffsetTemplateResponse`

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


    def DeleteTranscodeTemplate(self, request):
        """删除用戶自定義轉碼範本。

        :param request: Request instance for DeleteTranscodeTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteTranscodeTemplateResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteWatermarkTemplateResponse`

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
        """該介面用于批次删除關鍵詞樣本。

        :param request: Request instance for DeleteWordSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteWordSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteWordSamplesResponse`

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


    def DeleteWorkflow(self, request):
        """删除工作流。對于已啓用的工作流，需要禁用後才能删除。

        :param request: Request instance for DeleteWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteWorkflowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWorkflow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWorkflowResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """根據内容分析範本唯一标識，獲取内容分析範本詳情清單。返回結果包含符合條件的所有用戶自定義内容分析範本及系統預置視訊内容分析範本

        :param request: Request instance for DescribeAIAnalysisTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAIAnalysisTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAIAnalysisTemplatesResponse`

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
        """根據内容識别範本唯一标識，獲取内容識别範本詳情清單。返回結果包含符合條件的所有用戶自定義内容識别範本及系統預置視訊内容識别範本

        :param request: Request instance for DescribeAIRecognitionTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAIRecognitionTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAIRecognitionTemplatesResponse`

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


    def DescribeAnimatedGraphicsTemplates(self, request):
        """查詢轉動圖範本清單，支援根據條件，分頁查詢。

        :param request: Request instance for DescribeAnimatedGraphicsTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAnimatedGraphicsTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAnimatedGraphicsTemplatesResponse`

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


    def DescribeContentReviewTemplates(self, request):
        """根據内容審核範本唯一标識，獲取内容審核範本詳情清單。返回結果包含符合條件的所有用戶自定義範本及系統預置内容審核範本。

        :param request: Request instance for DescribeContentReviewTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeContentReviewTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeContentReviewTemplatesResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeImageSpriteTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeImageSpriteTemplatesResponse`

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


    def DescribeMediaMetaData(self, request):
        """獲取媒體的元訊息，包括視訊畫面寬、高、編碼格式、時長、幀率等。

        :param request: Request instance for DescribeMediaMetaData.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeMediaMetaDataRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeMediaMetaDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaMetaData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaMetaDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """該介面用于查詢人物樣本訊息，支援根據人物 ID、名稱、标簽，分頁查詢。

        :param request: Request instance for DescribePersonSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribePersonSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribePersonSamplesResponse`

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


    def DescribeSampleSnapshotTemplates(self, request):
        """查詢采樣截圖範本，支援根據條件，分頁查詢。

        :param request: Request instance for DescribeSampleSnapshotTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeSampleSnapshotTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeSampleSnapshotTemplatesResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeSnapshotByTimeOffsetTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeSnapshotByTimeOffsetTemplatesResponse`

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


    def DescribeTaskDetail(self, request):
        """通過任務 ID 查詢任務的執行狀态和結果的詳細訊息（最多可以查詢3天之内提交的任務）。

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeTaskDetailResponse`

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
        """* 該介面用于查詢任務清單；
        * 當清單數據比較多時，單次介面調用無法拉取整個清單，可通過 ScrollToken 參數，分批拉取；
        * 只能查詢到最近三天（72 小時）内的任務。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeTasksResponse`

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
        """根據轉碼範本唯一标識，獲取轉碼範本詳情清單。返回結果包含符合條件的所有用戶自定義範本及[系統預置轉碼範本](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。

        :param request: Request instance for DescribeTranscodeTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeTranscodeTemplatesResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeWatermarkTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeWatermarkTemplatesResponse`

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
        """該介面用于根據應用場景、關鍵詞、标簽，分頁查詢關鍵詞樣本訊息。

        :param request: Request instance for DescribeWordSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeWordSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeWordSamplesResponse`

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


    def DescribeWorkflows(self, request):
        """根據工作流 ID，獲取工作流詳情清單。

        :param request: Request instance for DescribeWorkflows.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeWorkflowsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeWorkflowsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWorkflows", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWorkflowsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableWorkflow(self, request):
        """禁用工作流。

        :param request: Request instance for DisableWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.DisableWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DisableWorkflowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableWorkflow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableWorkflowResponse()
                model._deserialize(response["Response"])
                return model
            else:
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

        1. 對一個文件進行剪輯，生成一個新的視訊；
        2. 對多個文件進行拼接，生成一個新的視訊；
        3. 對多個文件進行剪輯，然後再拼接，生成一個新的視訊。

        :param request: Request instance for EditMedia.
        :type request: :class:`tencentcloud.mps.v20190612.models.EditMediaRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.EditMediaResponse`

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


    def EnableWorkflow(self, request):
        """啓用工作流。

        :param request: Request instance for EnableWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.EnableWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.EnableWorkflowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableWorkflow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableWorkflowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ManageTask(self, request):
        """對已發起的任務進行管理。
        > 注意：目前僅支援終止執行中的直播流處理任務。

        :param request: Request instance for ManageTask.
        :type request: :class:`tencentcloud.mps.v20190612.models.ManageTaskRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ManageTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManageTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManageTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """修改用戶自定義内容分析範本。

        注意：範本 ID 10000 以下的爲系統預置範本，不允許修改。

        :param request: Request instance for ModifyAIAnalysisTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAIAnalysisTemplateResponse`

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
        """修改用戶自定義内容識别範本。

        :param request: Request instance for ModifyAIRecognitionTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAIRecognitionTemplateResponse`

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


    def ModifyAnimatedGraphicsTemplate(self, request):
        """修改用戶自定義轉動圖範本。

        :param request: Request instance for ModifyAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAnimatedGraphicsTemplateResponse`

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


    def ModifyContentReviewTemplate(self, request):
        """修改用戶自定義内容審核範本。

        :param request: Request instance for ModifyContentReviewTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyContentReviewTemplateResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyImageSpriteTemplateResponse`

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


    def ModifyPersonSample(self, request):
        """該介面用于根據人物 ID，修改人物樣本訊息，包括名稱、描述的修改，以及人臉、标簽的添加、删除、重置操作。人臉删除操作需保證至少剩餘 1 張圖片，否則，請使用重置操作。

        :param request: Request instance for ModifyPersonSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyPersonSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyPersonSampleResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifySampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifySampleSnapshotTemplateResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifySnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifySnapshotByTimeOffsetTemplateResponse`

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


    def ModifyTranscodeTemplate(self, request):
        """修改用戶自定義轉碼範本訊息。

        :param request: Request instance for ModifyTranscodeTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyTranscodeTemplateResponse`

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
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyWatermarkTemplateResponse`

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
        """該介面用于修改關鍵詞的應用場景、标簽，關鍵詞本身不可修改，如需修改，可删除重建。

        :param request: Request instance for ModifyWordSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyWordSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyWordSampleResponse`

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


    def ParseLiveStreamProcessNotification(self, request):
        """從 CMQ 獲取到訊息後，從訊息的 msgBody 欄位中解析出 MPS 直播流處理事件通知的内容。
        該介面不用于發起網絡調用，而是用來幫助生成各個語言平台的 SDK，您可以參考 SDK 的中解析函數的實現事件通知的解析。

        :param request: Request instance for ParseLiveStreamProcessNotification.
        :type request: :class:`tencentcloud.mps.v20190612.models.ParseLiveStreamProcessNotificationRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ParseLiveStreamProcessNotificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ParseLiveStreamProcessNotification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ParseLiveStreamProcessNotificationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ParseNotification(self, request):
        """從 CMQ 獲取到訊息後，從訊息的 msgBody 欄位中解析出 MPS 事件通知的内容。
        該介面不用于發起網絡調用，而是用來幫助生成各個語言平台的 SDK，您可以參考 SDK 的中解析函數的實現事件通知的解析。

        :param request: Request instance for ParseNotification.
        :type request: :class:`tencentcloud.mps.v20190612.models.ParseNotificationRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ParseNotificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ParseNotification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ParseNotificationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ProcessLiveStream(self, request):
        """對直播流媒體發起處理任務，功能包括：

        * 智慧内容審核（畫面鑒黃、鑒政、鑒暴、聲音鑒黃）。

        直播流處理事件通知實時寫入用戶指定的訊息隊列 CMQ 中，用戶需要從訊息隊列 CMQ 中獲取事件通知結果，同時處理過程中存在輸出文件的，會寫入用戶指定的輸出文件的目标儲存中。

        :param request: Request instance for ProcessLiveStream.
        :type request: :class:`tencentcloud.mps.v20190612.models.ProcessLiveStreamRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ProcessLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ProcessLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ProcessLiveStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """對 COS 中的媒體文件發起處理任務，功能包括：
        1. 視訊轉碼（帶浮水印）；
        2. 視訊轉動圖；
        3. 對視訊按指定時間點截圖；
        4. 對視訊采樣截圖；
        5. 對視訊截圖雪碧圖；
        6. 對視訊轉自适應碼流；
        7. 智慧内容審核（鑒黃、鑒恐、鑒政）；
        8. 智慧内容分析（标簽、分類、封面、按幀标簽）；
        9. 智慧内容識别（人臉、文本全文、文本關鍵詞、語音全文、語音關鍵詞）。

        :param request: Request instance for ProcessMedia.
        :type request: :class:`tencentcloud.mps.v20190612.models.ProcessMediaRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ProcessMediaResponse`

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


    def ResetWorkflow(self, request):
        """重新設置一個已經存在且處于禁用狀态的工作流。

        :param request: Request instance for ResetWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.ResetWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ResetWorkflowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetWorkflow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetWorkflowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)