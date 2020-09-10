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
from tencentcloud.tiw.v20190919 import models


class TiwClient(AbstractClient):
    _apiVersion = '2019-09-19'
    _endpoint = 'tiw.tencentcloudapi.com'


    def CreateTranscode(self, request):
        """創建一個文件轉碼任務

        :param request: Request instance for CreateTranscode.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateTranscodeRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateTranscodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTranscode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTranscodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOnlineRecord(self, request):
        """查詢實時錄制任務狀态與結果

        :param request: Request instance for DescribeOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOnlineRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOnlineRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOnlineRecordCallback(self, request):
        """查詢實時錄制回調網址

        :param request: Request instance for DescribeOnlineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOnlineRecordCallback", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOnlineRecordCallbackResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTranscode(self, request):
        """查詢文件轉碼任務的執行進度與轉碼結果

        :param request: Request instance for DescribeTranscode.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTranscode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTranscodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTranscodeCallback(self, request):
        """查詢文件轉碼回調網址

        :param request: Request instance for DescribeTranscodeCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeCallbackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTranscodeCallback", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTranscodeCallbackResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PauseOnlineRecord(self, request):
        """暫停實時錄制

        :param request: Request instance for PauseOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.PauseOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.PauseOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PauseOnlineRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PauseOnlineRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeOnlineRecord(self, request):
        """恢複實時錄制

        :param request: Request instance for ResumeOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ResumeOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ResumeOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResumeOnlineRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeOnlineRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetOnlineRecordCallback(self, request):
        """設置實時錄制回調網址

        :param request: Request instance for SetOnlineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetOnlineRecordCallback", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetOnlineRecordCallbackResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetTranscodeCallback(self, request):
        """設置文件轉碼回調網址

        :param request: Request instance for SetTranscodeCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetTranscodeCallback", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetTranscodeCallbackResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartOnlineRecord(self, request):
        """發起一個實時錄制任務

        :param request: Request instance for StartOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StartOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StartOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartOnlineRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartOnlineRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopOnlineRecord(self, request):
        """停止實時錄制

        :param request: Request instance for StopOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StopOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StopOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopOnlineRecord", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopOnlineRecordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)