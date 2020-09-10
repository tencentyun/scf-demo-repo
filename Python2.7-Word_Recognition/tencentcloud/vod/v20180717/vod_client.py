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
        """* 該介面用于申請媒體文件（和封面文件）的上傳，獲取文件上傳到Top Cloud 點播的元訊息（包括上傳路徑、上傳簽名等），用于後續上傳介面。
        * 上傳流程請參考[服務端上傳綜述](https://cloud.taifucloud.com/document/product/266/9759)。

        :param request: 調用ApplyUpload所需參數的結構體。
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
        """該介面用于确認媒體文件（和封面文件）上傳到Top Cloud 點播的結果，并儲存媒體訊息，返回文件的播放網址和文件 ID。

        :param request: 調用CommitUpload所需參數的結構體。
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


    def ConfirmEvents(self, request):
        """* 開發者調用拉取事件通知，獲取到事件後，必須調用該介面來确認訊息已經收到；
        * 開發者獲取到事件句柄後，等待确認的有效時間爲 30 秒，超出 30 秒會報參數錯誤（4000）；
        * 更多參考[服務端事件通知](https://cloud.taifucloud.com/document/product/266/7829)。

        :param request: 調用ConfirmEvents所需參數的結構體。
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

        :param request: 調用CreateAIAnalysisTemplate所需參數的結構體。
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

        :param request: 調用CreateAIRecognitionTemplate所需參數的結構體。
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


    def CreateClass(self, request):
        """* 用于對媒體進行分類管理；
        * 該介面不影響既有媒體的分類，如需修改媒體分類，請調用[修改媒體文件屬性](/document/product/266/31762)介面。
        * 分類層次不可超過 4 層。
        * 每個分類的子類數量不可超過 500 個。

        :param request: 調用CreateClass所需參數的結構體。
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

        :param request: 調用CreateContentReviewTemplate所需參數的結構體。
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


    def CreatePersonSample(self, request):
        """該介面用于創建人物樣本，用于通過人臉識别等技術，進行内容識别、内容審核等視訊處理。

        :param request: 調用CreatePersonSample所需參數的結構體。
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

        :param request: 調用CreateProcedureTemplate所需參數的結構體。
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


    def CreateTranscodeTemplate(self, request):
        """創建用戶自定義轉碼範本，數量上限：1000。

        :param request: 調用CreateTranscodeTemplate所需參數的結構體。
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

        :param request: 調用CreateWatermarkTemplate所需參數的結構體。
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
        """該介面用于批次創建關鍵詞樣本，樣本用于通過OCR、ASR技術，進行内容審核、内容識别等視訊處理。

        :param request: 調用CreateWordSamples所需參數的結構體。
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

        :param request: 調用DeleteAIAnalysisTemplate所需參數的結構體。
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

        :param request: 調用DeleteAIRecognitionTemplate所需參數的結構體。
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


    def DeleteClass(self, request):
        """* 僅當待删分類無子分類且無媒體關聯情況下，可删除分類；
        * 否則，請先執行[删除媒體](/document/product/266/31764)及子分類，再删除該分類；

        :param request: 調用DeleteClass所需參數的結構體。
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

        :param request: 調用DeleteContentReviewTemplate所需參數的結構體。
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


    def DeleteMedia(self, request):
        """* 删除媒體及其對應的視訊處理文件（如轉碼視訊、雪碧圖、截圖、 發布視訊等）；
        * 可單獨删除指定 ID 的視訊文件下的轉碼，或者 發布文件；

        :param request: 調用DeleteMedia所需參數的結構體。
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
        """該介面用于根據人物 ID，删除人物樣本。

        :param request: 調用DeletePersonSample所需參數的結構體。
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
        """删除指定名字的任務流範本

        :param request: 調用DeleteProcedureTemplate所需參數的結構體。
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


    def DeleteTranscodeTemplate(self, request):
        """删除用戶自定義轉碼範本。

        :param request: 調用DeleteTranscodeTemplate所需參數的結構體。
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

        :param request: 調用DeleteWatermarkTemplate所需參數的結構體。
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
        """該介面用于批次删除關鍵詞樣本。

        :param request: 調用DeleteWordSamples所需參數的結構體。
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
        """根據視訊内容分析範本唯一标識，獲取視訊内容分析範本詳情清單。返回結果包含符合條件的所有用戶自定義視訊内容分析範本及[系統預置視訊内容分析範本]

        :param request: 調用DescribeAIAnalysisTemplates所需參數的結構體。
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
        """根據視訊内容識别範本唯一标識，獲取視訊内容識别範本詳情清單。返回結果包含符合條件的所有用戶自定義視訊内容識别範本及[系統預置視訊内容識别範本]

        :param request: 調用DescribeAIRecognitionTemplates所需參數的結構體。
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


    def DescribeAllClass(self, request):
        """* 獲得用戶的所有分類訊息。

        :param request: 調用DescribeAllClass所需參數的結構體。
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


    def DescribeContentReviewTemplates(self, request):
        """根據視訊内容審核範本唯一标識，獲取視訊内容審核範本詳情清單。返回結果包含符合條件的所有用戶自定義範本及[系統預置内容審核範本]。

        :param request: 調用DescribeContentReviewTemplates所需參數的結構體。
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


    def DescribeMediaInfos(self, request):
        """1. 該介面可以獲取多個視訊的多種訊息，包括：
            1. 基礎訊息（basicInfo）：包括視訊名稱、大小、時長、封面圖片等。
            2. 元訊息（metaData）：包括視訊流訊息、音訊流訊息等。
            3. 轉碼結果訊息（transcodeInfo）：包括該視訊轉碼生成的各種碼率的視訊的網址、規格、碼率、分辨率等。
            4. 轉動圖結果訊息（animatedGraphicsInfo）：對視訊轉動圖（如 gif）後，動圖相關訊息。
            5. 采樣截圖訊息（sampleSnapshotInfo）：對視訊采樣截圖後，相關截圖訊息。
            6. 雪碧圖訊息（imageSpriteInfo）：對視訊截取雪碧圖之後，雪碧圖的相關訊息。
            7. 指定時間點截圖訊息（snapshotByTimeOffsetInfo）：對視訊依照指定時間點截圖後，各個截圖的訊息。
            8. 視訊打點訊息（keyFrameDescInfo）：對視訊設置的各個打點訊息。
            9. 轉自适應碼流訊息（adaptiveDynamicStreamingInfo）：包括規格、加密類型、打包格式等相關訊息。
        2. 可以指定回包只返回部分訊息。

        :param request: 調用DescribeMediaInfos所需參數的結構體。
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


    def DescribePersonSamples(self, request):
        """該介面用于查詢人物樣本訊息，支援根據人物 ID、名稱、标簽，分頁查詢。

        :param request: 調用DescribePersonSamples所需參數的結構體。
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

        :param request: 調用DescribeProcedureTemplates所需參數的結構體。
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


    def DescribeTaskDetail(self, request):
        """通過任務 ID 查詢任務的執行狀态和結果的詳細訊息（最多可以查詢3天之内提交的任務）。

        :param request: 調用DescribeTaskDetail所需參數的結構體。
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
        """* 該介面用于查詢任務清單；
        * 當清單數據比較多時，單次介面調用無法拉取整個清單，可通過 ScrollToken 參數，分批拉取；
        * 只能查詢到最近三天（72 小時）内的任務。

        :param request: 調用DescribeTasks所需參數的結構體。
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
        """根據轉碼範本唯一标識，獲取轉碼範本詳情清單。返回結果包含符合條件的所有用戶自定義範本及[系統預置轉碼範本](https://cloud.taifucloud.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。

        :param request: 調用DescribeTranscodeTemplates所需參數的結構體。
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

        :param request: 調用DescribeWatermarkTemplates所需參數的結構體。
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
        """該介面用于根據應用場景、關鍵詞、标簽，分頁查詢關鍵詞樣本訊息。

        :param request: 調用DescribeWordSamples所需參數的結構體。
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

        對于生成的新視訊，還可以指定生成後的視訊是否要執行任務流。

        :param request: 調用EditMedia所需參數的結構體。
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


    def LiveRealTimeClip(self, request):
        """直播即時剪輯，是指在直播過程中（即直播尚未結束時），客戶可以在過往直播内容中選擇一段，實時生成一個新的視訊（HLS 格式），開發者可以将其立即分享出去，或者長久保存起來。

        Top Cloud 點播支援兩種即時剪輯模式：
        - 剪輯固化：将剪輯出來的視訊保存成獨立的視訊，擁有獨立 FileId；适用于将精彩片段**長久保存**的場景；
        - 剪輯不固化：剪輯得到的視訊附屬于直播錄制文件，沒有獨立 FileId；适用于将精彩片段**臨時分享**的場景。

        注意：
        - 使用直播即時剪輯功能的前提是：目标直播流開啓了[時移回看](https://cloud.taifucloud.com/document/product/267/32742)功能。
        - 直播即時剪輯是基于直播錄制生成的 m3u8 文件進行的，故而其最小剪輯精度爲一個 ts 切片，無法實現秒級或者更爲精确的剪輯精度。


        ### 剪輯固化
        所謂剪輯固化，是指将剪輯出來的視訊是保存成一個獨立的視訊（擁有獨立的 FileId）。其生命週期不受原始直播錄制視訊影響（即使原始錄制視訊被删除，剪輯結果也不會受到任何影響）；也可以對其進行轉碼、 發布等二次處理。

        舉例如下：一場完整的足球比賽，直播錄制出來的原始視訊可能長達 2 個小時，客戶出于節省成本的目的可以對這個視訊儲存 2 個月，但對于直播即時剪輯的「精彩時刻」視訊卻可以指定儲存更長時間，同時可以單獨對「精彩時刻」視訊進行轉碼、 發布等額外的點播操作，這時候可以選擇直播即時剪輯并且固化的方案。

        剪輯固化的優勢在于其生命週期與原始錄制視訊相互獨立，可以獨立管理、長久保存。

        ### 剪輯不固化
        所謂剪輯不固化，是指剪輯所得到的結果（m3u8 文件）與直播錄制視訊共享相同的 ts 分片，新生成的視訊不是一個獨立完整的視訊（沒有獨立 FileId，只有播放 URL），其有效期與直播錄制的完整視訊有效期是一緻的。一旦直播錄制出來的視訊被删除，也會導緻該片段無法播放。

        剪輯不固化，由于其剪輯結果不是一個獨立的視訊，因而也不會納入點播媒資視訊管理（比如控制台的視訊總數不會統計這一片段）中，也無法單獨針對這個片段做轉碼、 發布等任何視訊處理操作。

        剪輯不固化的優勢在于其剪輯操作十分“輕量化”，不會産生額外的儲存開銷。但其不足之處在于生命週期與原始錄制視訊相同，且無法進一步進行轉碼等視訊處理。

        :param request: 調用LiveRealTimeClip所需參數的結構體。
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

        :param request: 調用ModifyAIAnalysisTemplate所需參數的結構體。
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

        :param request: 調用ModifyAIRecognitionTemplate所需參數的結構體。
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


    def ModifyClass(self, request):
        """修改媒體分類屬性。

        :param request: 調用ModifyClass所需參數的結構體。
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

        :param request: 調用ModifyContentReviewTemplate所需參數的結構體。
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


    def ModifyMediaInfo(self, request):
        """修改媒體文件的屬性，包括分類、名稱、描述、标簽、過期時間、打點訊息、視訊封面等。

        :param request: 調用ModifyMediaInfo所需參數的結構體。
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
        """該介面用于根據人物 ID，修改人物樣本訊息，包括名稱、描述的修改，以及人臉、标簽的添加、删除、重置操作。人臉删除操作需保證至少剩餘 1 張圖片，否則，請使用重置操作。

        :param request: 調用ModifyPersonSample所需參數的結構體。
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


    def ModifyTranscodeTemplate(self, request):
        """修改用戶自定義轉碼範本訊息。

        :param request: 調用ModifyTranscodeTemplate所需參數的結構體。
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

        :param request: 調用ModifyWatermarkTemplate所需參數的結構體。
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
        """該介面用于修改關鍵詞的應用場景、标簽，關鍵詞本身不可修改，如需修改，可删除重建。

        :param request: 調用ModifyWordSample所需參數的結構體。
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


    def ProcessMedia(self, request):
        """對點播中的影音媒體發起處理任務，功能包括：
        1. 視訊轉碼（帶浮水印）；
        2. 視訊轉動圖；
        3. 對視訊按指定時間點截圖；
        4. 對視訊采樣截圖；
        5. 對視訊截圖雪碧圖；
        6. 對視訊截取一張圖做封面；
        7. 對視訊轉自适應碼流（并加密）；
        8. 智慧内容審核（ 、鑒恐、鑒政）；
        9. 智慧内容分析（标簽、分類、封面、按幀标簽）；
        10. 智慧内容識别（視訊片頭片尾、人臉、文本全文、文本關鍵詞、語音全文、語音關鍵詞、物體）。

        :param request: 調用ProcessMedia所需參數的結構體。
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

        :param request: 調用ProcessMediaByProcedure所需參數的結構體。
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
        2. 智慧内容分析（标簽、分類、封面、按幀标簽）；
        3. 智慧内容識别（視訊片頭片尾、人臉、文本全文、文本關鍵詞、語音全文、語音關鍵詞、物體）。

        :param request: 調用ProcessMediaByUrl所需參數的結構體。
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
        """* 該介面用于從點播服務端獲取事件通知，詳見[服務端事件通知](https://cloud.taifucloud.com/document/product/266/7829)；
        * 介面爲長輪詢模式，即：如果服務端存在未消費事件，則立即返回給請求方；如果服務端沒有未消費事件，則後台會将請求挂起，直到有新的事件産生爲止；
        * 請求最多挂起 5 秒，建議請求方将超時時間設置爲 10 秒；
        * 若該介面有事件返回，調用方必須再調用[确認事件通知](https://cloud.taifucloud.com/document/product/266/33434)介面，确認事件通知已經處理，否則該事件通知後續會再次被拉取到。

        :param request: 調用PullEvents所需參數的結構體。
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


    def ResetProcedureTemplate(self, request):
        """重新設置已存在的任務流範本的任務内容

        :param request: 調用ResetProcedureTemplate所需參數的結構體。
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
        """搜索媒體訊息，支援各種條件篩選，以及對返回結果進行排序、過濾等功能，具體包括：
        - 根據媒體文件名或描述訊息進行文本模糊搜索。
        - 根據媒體分類、标簽進行檢索。
            - 指定分類集合 ClassIds（見輸入參數），返回滿足集合中任意分類的媒體。例如：假設媒體分類有電影、電視劇、綜藝，其中電影又有子分類曆史片、動作片、言情片。如果 ClassIds 指定了電影、電視劇，那麽電影和電視劇下的所有子分類
            都會返回；而如果 ClassIds 指定的是曆史片、動作片，那麽只有這 2 個子分類下的媒體才會返回。
            - 指定标簽集合 Tags（見輸入參數），返回滿足集合中任意标簽的媒體。例如：假設媒體标簽有二次元、宮鬥、鬼畜，如果 Tags 指定了二次元、鬼畜 2 個标簽，那麽只要符合這 2 個标簽中任意一個的媒體都會被檢索出來。
        - 允許指定篩選某一來源 Source（見輸入參數）的媒體。
        - 允許根據直播推流碼、Vid（見輸入參數）篩選直播錄制的媒體。
        - 允許根據媒體的創建範圍篩選媒體。
        - 允許對上述條件進行任意組合，檢索同時滿足以上條件的媒體。例如可以篩選從 2018 年 12 月 1 日到 2018 年 12 月 8 日創建的電影、電視劇分類下帶有宮鬥、鬼畜标簽的媒體。
        - 允許對結果進行排序，允許通過 Offset 和 Limit 實現只返回部分結果。

        介面搜索限制：
        - 搜索結果超過 5000條，不再支援分頁查詢超過 5000 部分的數據。

        :param request: 調用SearchMedia所需參數的結構體。
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

        :param request: 調用SimpleHlsClip所需參數的結構體。
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