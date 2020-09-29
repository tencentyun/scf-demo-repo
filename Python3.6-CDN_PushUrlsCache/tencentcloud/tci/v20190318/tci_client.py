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
from taifucloudcloud.tci.v20190318 import models


class TciClient(AbstractClient):
    _apiVersion = '2019-03-18'
    _endpoint = 'tci.taifucloudcloudapi.com'


    def AIAssistant(self, request):
        """提供 AI 助教基礎版本功能介面

        :param request: Request instance for AIAssistant.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.AIAssistantRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.AIAssistantResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AIAssistant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AIAssistantResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelTask(self, request):
        """用於取消已經提交的任務，目前只支援圖像任務。

        :param request: Request instance for CancelTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.CancelTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckFacePhoto(self, request):
        """檢查人臉圖片是否合法

        :param request: Request instance for CheckFacePhoto.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.CheckFacePhotoRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.CheckFacePhotoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckFacePhoto", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckFacePhotoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFace(self, request):
        """創建人臉

        :param request: Request instance for CreateFace.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.CreateFaceRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.CreateFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLibrary(self, request):
        """創建人員庫

        :param request: Request instance for CreateLibrary.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.CreateLibraryRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.CreateLibraryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLibrary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLibraryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePerson(self, request):
        """創建人員

        :param request: Request instance for CreatePerson.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.CreatePersonRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.CreatePersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePersonResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVocab(self, request):
        """創建詞匯

        :param request: Request instance for CreateVocab.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.CreateVocabRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.CreateVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVocabResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVocabLib(self, request):
        """建立詞匯庫

        :param request: Request instance for CreateVocabLib.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.CreateVocabLibRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.CreateVocabLibResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVocabLib", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVocabLibResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteFace(self, request):
        """删除人臉

        :param request: Request instance for DeleteFace.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DeleteFaceRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DeleteFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLibrary(self, request):
        """删除人員庫

        :param request: Request instance for DeleteLibrary.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DeleteLibraryRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DeleteLibraryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLibrary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLibraryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePerson(self, request):
        """删除人員

        :param request: Request instance for DeletePerson.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DeletePersonRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DeletePersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePersonResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVocab(self, request):
        """删除詞匯

        :param request: Request instance for DeleteVocab.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DeleteVocabRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DeleteVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVocabResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVocabLib(self, request):
        """删除詞匯庫

        :param request: Request instance for DeleteVocabLib.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DeleteVocabLibRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DeleteVocabLibResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVocabLib", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVocabLibResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAITaskResult(self, request):
        """獲取標準化介面任務結果

        :param request: Request instance for DescribeAITaskResult.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribeAITaskResultRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribeAITaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAITaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAITaskResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAttendanceResult(self, request):
        """人臉考勤查詢結果

        :param request: Request instance for DescribeAttendanceResult.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribeAttendanceResultRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribeAttendanceResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAttendanceResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAttendanceResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAudioTask(self, request):
        """音訊評估任務訊息查詢介面，異步查詢客戶提交的請求的結果。

        :param request: Request instance for DescribeAudioTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribeAudioTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribeAudioTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAudioTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAudioTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConversationTask(self, request):
        """音訊對話任務評估任務訊息查詢介面，異步查詢客戶提交的請求的結果。

        :param request: Request instance for DescribeConversationTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribeConversationTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribeConversationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConversationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConversationTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHighlightResult(self, request):
        """視訊精彩集錦結果查詢介面，異步查詢客戶提交的請求的結果。

        :param request: Request instance for DescribeHighlightResult.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribeHighlightResultRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribeHighlightResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHighlightResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHighlightResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageTask(self, request):
        """拉取任務詳情

        :param request: Request instance for DescribeImageTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribeImageTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribeImageTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageTaskStatistic(self, request):
        """獲取圖像任務統計訊息

        :param request: Request instance for DescribeImageTaskStatistic.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribeImageTaskStatisticRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribeImageTaskStatisticResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageTaskStatistic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageTaskStatisticResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLibraries(self, request):
        """獲取人員庫清單

        :param request: Request instance for DescribeLibraries.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribeLibrariesRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribeLibrariesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLibraries", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLibrariesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePerson(self, request):
        """獲取人員詳情

        :param request: Request instance for DescribePerson.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribePersonRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribePersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePersons(self, request):
        """拉取人員清單

        :param request: Request instance for DescribePersons.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribePersonsRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribePersonsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersons", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVocab(self, request):
        """查詢詞匯

        :param request: Request instance for DescribeVocab.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribeVocabRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribeVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVocabResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVocabLib(self, request):
        """查詢詞匯庫

        :param request: Request instance for DescribeVocabLib.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.DescribeVocabLibRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.DescribeVocabLibResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVocabLib", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVocabLibResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLibrary(self, request):
        """修改人員庫訊息

        :param request: Request instance for ModifyLibrary.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.ModifyLibraryRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.ModifyLibraryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLibrary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLibraryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPerson(self, request):
        """修改人員訊息

        :param request: Request instance for ModifyPerson.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.ModifyPersonRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.ModifyPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitAudioTask(self, request):
        """音訊任務提交介面

        :param request: Request instance for SubmitAudioTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitAudioTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitAudioTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitAudioTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitAudioTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitCheckAttendanceTask(self, request):
        """提交人員考勤任務，支援包括點播和直播資源；支援通過DescribeAttendanceResult查詢結果，也支援通過NoticeUrl設置考勤回調結果，回調結果結構如下：
        ##### 回調事件結構
         | 參數名稱 | 類型 | 描述 |
         | ----  | ---  | ------  |
         | jobid | Integer | 任務ID |
         | person_info | array of PersonInfo | 識别到的人員清單 |
        #####子結構PersonInfo
         | 參數名稱 | 類型 | 描述 |
         | ----  | ---  | ------  |
         | traceid | String | 可用於區分同一路視訊流下的不同陌生人 |
         | personid | String | 識别到的人員ID，如果是陌生人則返回空串 |
         | libid | String | 識别到的人員所在的庫ID，如果是陌生人則返回空串 |
         | timestamp | uint64 | 識别到人臉的絕對時間戳，單位ms |
         | image_url | string | 識别到人臉的事件抓圖的下載網址，不長期保存，需要請及時下載 |

        :param request: Request instance for SubmitCheckAttendanceTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitCheckAttendanceTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitCheckAttendanceTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitCheckAttendanceTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitCheckAttendanceTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitCheckAttendanceTaskPlus(self, request):
        """支援多路視訊流，提交高級人員考勤任務

        :param request: Request instance for SubmitCheckAttendanceTaskPlus.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitCheckAttendanceTaskPlusRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitCheckAttendanceTaskPlusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitCheckAttendanceTaskPlus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitCheckAttendanceTaskPlusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitConversationTask(self, request):
        """對話任務分析介面

        :param request: Request instance for SubmitConversationTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitConversationTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitConversationTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitConversationTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitConversationTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitDoubleVideoHighlights(self, request):
        """發起雙路視訊生成精彩集錦介面。該介面可以通過客戶傳入的學生影音及老師視訊兩路Url，自動生成一堂課程的精彩集錦。需要通過DescribeHighlightResult
        介面獲取生成結果。

        :param request: Request instance for SubmitDoubleVideoHighlights.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitDoubleVideoHighlightsRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitDoubleVideoHighlightsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitDoubleVideoHighlights", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitDoubleVideoHighlightsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitFullBodyClassTask(self, request):
        """**傳統課堂授課任務**：在此場景中，老師爲站立授課，有白板或投影供老師展示課程内容，攝像頭可以拍攝到老師的半身或者全身。拍攝視訊爲一路全局畫面，且背景不動，要求畫面穩定清晰。通過此介面可分析老師授課的行爲及語音，以支援AI評教。

        **提供的功能介面有：**老師人臉識别、老師表情識别、老師肢體動作識别、語音識别。  可分析的指標維度包括：身份識别、正臉、側臉、人臉坐標、人臉尺寸、高興、中性、高興、中性、驚訝、厭惡、恐懼、憤怒、蔑視、悲傷、正面講解、寫板書、指黑板、語音轉文字、發音時長、非發音時長、音量、語速、指定關鍵詞的使用等

        **對場景的要求爲：**真實場景老師1人出現在畫面中，全局畫面且背景不動；人臉上下角度在20度以内，左右角度在15度以内，歪頭角度在15度以内；光照均勻，無遮擋，人臉清晰可見；像素最好在 100X100 像素以上，但是圖像整體質量不能超過1080p。

        **結果查詢方式：**圖像任務直接返回結果，點播及直播任務通過DescribeAITaskResult查詢結果。

        :param request: Request instance for SubmitFullBodyClassTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitFullBodyClassTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitFullBodyClassTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitFullBodyClassTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitFullBodyClassTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitHighlights(self, request):
        """發起視訊生成精彩集錦介面。該介面可以通過客戶傳入的課程音訊數據及相關策略（如微笑抽取，專注抽取等），自動生成一堂課程的精彩集錦。需要通過QueryHighlightResult介面獲取生成結果。

        :param request: Request instance for SubmitHighlights.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitHighlightsRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitHighlightsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitHighlights", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitHighlightsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitImageTask(self, request):
        """提交圖像分析任務

        :param request: Request instance for SubmitImageTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitImageTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitImageTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitImageTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitImageTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitImageTaskPlus(self, request):
        """高級圖像分析任務，開放了圖像任務裏的所有開關，可以根據場景深度定制圖像分析任務。支援的圖像類别有，圖片連結、圖片二進制數據、點播連結和直播連結。

        :param request: Request instance for SubmitImageTaskPlus.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitImageTaskPlusRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitImageTaskPlusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitImageTaskPlus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitImageTaskPlusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitOneByOneClassTask(self, request):
        """**提交在線1對1課堂任務**
        對於在線1對1課堂，老師通過視訊向學生授課，並且學生人數爲1人。通過上傳學生端的圖像訊息，可以獲取學生的聽課情況分析。 具體指一路全局畫面且背景不動，有1位學生的頭像或上半身的畫面，要求畫面穩定清晰。

        **提供的功能介面有：**學生人臉識别、學生表情識别、語音識别。可分析的指標維度包括：學生身份識别、正臉、側臉、擡頭、低頭、人臉坐標、人臉尺寸、高興、中性、高興、中性、驚訝、厭惡、恐懼、憤怒、蔑視、悲傷、語音轉文字、發音時長、非發音時長、音量、語速等。

        **對場景的要求爲：**真實常規1v1授課場景，學生2人以下，全局畫面且背景不動；人臉上下角度在20度以内，左右角度在15度以内，歪頭角度在15度以内；光照均勻，無遮擋，人臉清晰可見；像素最好在 100X100 像素以上，但是圖像整體質量不能超過1080p。

        **結果查詢方式：**圖像任務直接返回結果，點播及直播任務通過DescribeAITaskResult查詢結果。

        :param request: Request instance for SubmitOneByOneClassTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitOneByOneClassTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitOneByOneClassTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitOneByOneClassTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitOneByOneClassTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitOpenClassTask(self, request):
        """**提交線下小班（無課桌）課任務**
        線下小班課是指有學生無課桌的課堂，滿座15人以下，全局畫面且背景不動，能清晰看到。

        **提供的功能介面有：**學生人臉識别、學生表情識别、學生肢體動作識别。  可分析的指標維度包括：身份識别、正臉、側臉、擡頭、低頭、高興、中性、高興、中性、驚訝、厭惡、恐懼、憤怒、蔑視、悲傷、站立、舉手、坐着等。

        **對場景的要求爲：**真實常規教室，滿座15人以下，全局畫面且背景不動；人臉上下角度在20度以内，左右角度在15度以内，歪頭角度在15度以内；光照均勻，無遮擋，人臉清晰可見；像素最好在 100X100 像素以上但是圖像整體質量不能超過1080p。

        **結果查詢方式：**圖像任務直接返回結果，點播及直播任務通過DescribeAITaskResult查詢結果。

        :param request: Request instance for SubmitOpenClassTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitOpenClassTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitOpenClassTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitOpenClassTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitOpenClassTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitPartialBodyClassTask(self, request):
        """**在線小班課任務**：此場景是在線授課場景，老師一般爲坐着授課，攝像頭可以拍攝到老師的頭部及上半身。拍攝視訊爲一路全局畫面，且背景不動，要求畫面穩定清晰。通過此介面可分析老師授課的行爲及語音，以支援AI評教。

        **提供的功能介面有：**老師人臉識别、老師表情識别、老師手勢識别、光線識别、語音識别。 可分析的指標維度包括：身份識别、正臉、側臉、人臉坐標、人臉尺寸、高興、中性、高興、中性、驚訝、厭惡、恐懼、憤怒、蔑視、悲傷、點贊手勢、聽你說手勢、聽我說手勢、拿教具行爲、語音轉文字、發音時長、非發音時長、音量、語速、指定關鍵詞的使用等

        **對場景的要求爲：**在線常規授課場景，全局畫面且背景不動；人臉上下角度在20度以内，左右角度在15度以内，歪頭角度在15度以内；光照均勻，無遮擋，人臉清晰可見；像素最好在 100X100 像素以上，但是圖像整體質量不能超過1080p。

        **結果查詢方式：**圖像任務直接返回結果，點播及直播任務通過DescribeAITaskResult查詢結果。

        :param request: Request instance for SubmitPartialBodyClassTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitPartialBodyClassTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitPartialBodyClassTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitPartialBodyClassTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitPartialBodyClassTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitTraditionalClassTask(self, request):
        """**提交線下傳統面授大班課（含課桌）任務。**
        傳統教室課堂是指有學生課堂有課桌的課堂，滿座20-50人，全局畫面且背景不動。

        **提供的功能介面有：**學生人臉識别、學生表情識别、學生肢體動作識别。可分析的指標維度包括：學生身份識别、正臉、側臉、擡頭、低頭、高興、中性、高興、中性、驚訝、厭惡、恐懼、憤怒、蔑視、悲傷、舉手、站立、坐着、趴桌子、玩手機等

        **對場景的要求爲：**傳統的學生上課教室，滿座20-50人，全局畫面且背景不動；人臉上下角度在20度以内，左右角度在15度以内，歪頭角度在15度以内；光照均勻，無遮擋，人臉清晰可見；像素最好在 100X100 像素以上，但是圖像整體質量不能超過1080p。

        **結果查詢方式：**圖像任務直接返回結果，點播及直播任務通過DescribeAITaskResult查詢結果。


        :param request: Request instance for SubmitTraditionalClassTask.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.SubmitTraditionalClassTaskRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.SubmitTraditionalClassTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitTraditionalClassTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitTraditionalClassTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransmitAudioStream(self, request):
        """分析音訊訊息

        :param request: Request instance for TransmitAudioStream.
        :type request: :class:`taifucloudcloud.tci.v20190318.models.TransmitAudioStreamRequest`
        :rtype: :class:`taifucloudcloud.tci.v20190318.models.TransmitAudioStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransmitAudioStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransmitAudioStreamResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)