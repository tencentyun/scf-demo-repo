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
from taifucloudcloud.asr.v20190614 import models


class AsrClient(AbstractClient):
    _apiVersion = '2019-06-14'
    _endpoint = 'asr.taifucloudcloudapi.com'


    def CreateAsrVocab(self, request):
        """用戶通過本介面進行熱詞表的創建。
        <br>•   預設最多可創建30個熱詞表。
        <br>•   每個熱詞表最多可添加128個詞，每個詞最長10個字，不能超出限制。
        <br>•   熱詞表可以通過數組或者本地文件形式上傳。
        <br>•   本地文件必須爲UTF-8編碼格式，每行僅添加一個熱詞且不能包含标點和特殊字元。
        <br>•   熱詞權重取值範圍爲[1,10]之間的整數，權重越大代表該詞被識别出來的概率越大。

        :param request: Request instance for CreateAsrVocab.
        :type request: :class:`taifucloudcloud.asr.v20190614.models.CreateAsrVocabRequest`
        :rtype: :class:`taifucloudcloud.asr.v20190614.models.CreateAsrVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAsrVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAsrVocabResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRecTask(self, request):
        """本介面服務對錄音時長1小時以内的錄音文件進行識别，異步返回識别全部結果。
        <br>• 介面是 HTTP RESTful 形式
        <br>• 介面支援wav、mp3、silk、amr、m4a等主流音訊格式
        <br>• 支援語音 URL 和本地語音文件兩種請求方式
        <br>• 本地語音文件上傳的文件不能大于5MB，語音 URL的音訊時長不能長于1小時
        <br>• 支援中文普通話、英語和粵語。
        <br>• 支援回調或輪詢的方式獲取結果，結果獲取請參考[ 錄音文件識别結果查詢](https://cloud.taifucloud.com/document/product/1093/37822)。

        :param request: Request instance for CreateRecTask.
        :type request: :class:`taifucloudcloud.asr.v20190614.models.CreateRecTaskRequest`
        :rtype: :class:`taifucloudcloud.asr.v20190614.models.CreateRecTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRecTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRecTaskResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAsrVocab(self, request):
        """用戶通過本介面進行熱詞表的删除。

        :param request: Request instance for DeleteAsrVocab.
        :type request: :class:`taifucloudcloud.asr.v20190614.models.DeleteAsrVocabRequest`
        :rtype: :class:`taifucloudcloud.asr.v20190614.models.DeleteAsrVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAsrVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAsrVocabResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskStatus(self, request):
        """在調用錄音文件識别請求介面後，有回調和輪詢兩種方式獲取識别結果。
        <br>• 當采用回調方式時，識别完成後會将結果通過 POST 請求的形式通知到用戶在請求時填寫的回調 URL，具體請參見[ 錄音識别結果回調 ](https://cloud.taifucloud.com/document/product/1093/37139#callback)。
        <br>• 當采用輪詢方式時，需要主動提交任務ID來輪詢識别結果，共有任務成功、等待、執行中和失敗四種結果，具體訊息請參見下文說明。

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`taifucloudcloud.asr.v20190614.models.DescribeTaskStatusRequest`
        :rtype: :class:`taifucloudcloud.asr.v20190614.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadAsrVocab(self, request):
        """用戶通過本介面進行熱詞表的下載，獲得詞表權重文件形式的 base64 值，文件形式爲通過 “|” 分割的詞和權重，即 word|weight 的形式。

        :param request: Request instance for DownloadAsrVocab.
        :type request: :class:`taifucloudcloud.asr.v20190614.models.DownloadAsrVocabRequest`
        :rtype: :class:`taifucloudcloud.asr.v20190614.models.DownloadAsrVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadAsrVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadAsrVocabResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetAsrVocab(self, request):
        """用戶根據詞表的ID可以獲取對應的熱詞表訊息

        :param request: Request instance for GetAsrVocab.
        :type request: :class:`taifucloudcloud.asr.v20190614.models.GetAsrVocabRequest`
        :rtype: :class:`taifucloudcloud.asr.v20190614.models.GetAsrVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetAsrVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAsrVocabResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetAsrVocabList(self, request):
        """用戶通過該介面，可獲得所有的熱詞表及其訊息。

        :param request: Request instance for GetAsrVocabList.
        :type request: :class:`taifucloudcloud.asr.v20190614.models.GetAsrVocabListRequest`
        :rtype: :class:`taifucloudcloud.asr.v20190614.models.GetAsrVocabListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetAsrVocabList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetAsrVocabListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SentenceRecognition(self, request):
        """本介面用于對60秒之内的短音訊文件進行識别。
        <br>•   支援中文普通話、英語、粵語。
        <br>•   支援本地語音文件上傳和語音URL上傳兩種請求方式。
        <br>•   音訊格式支援wav、mp3；采樣率支援8000Hz或者16000Hz；采樣精度支援16bits；聲道支援單聲道。
        <br>•   當音訊文件通過請求中body内容上傳時，請求大小不能超過600KB；當音訊以URL方式傳輸時，音訊時長不可超過60s。
        <br>•   所有請求參數放在POST請求的body中，編碼類型采用x-www-form-urlencoded，參數進行urlencode編碼後傳輸。

        :param request: Request instance for SentenceRecognition.
        :type request: :class:`taifucloudcloud.asr.v20190614.models.SentenceRecognitionRequest`
        :rtype: :class:`taifucloudcloud.asr.v20190614.models.SentenceRecognitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SentenceRecognition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SentenceRecognitionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetVocabState(self, request):
        """用戶通過該介面可以設置熱詞表的預設狀态。初始狀态爲0，用戶可設置狀态爲1，即爲預設狀态。預設狀态表示用戶在請求識别時，如不設置熱詞表ID，則預設使用狀态爲1的熱詞表。

        :param request: Request instance for SetVocabState.
        :type request: :class:`taifucloudcloud.asr.v20190614.models.SetVocabStateRequest`
        :rtype: :class:`taifucloudcloud.asr.v20190614.models.SetVocabStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetVocabState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetVocabStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateAsrVocab(self, request):
        """用戶通過本介面進行對應的詞表訊息更新。

        :param request: Request instance for UpdateAsrVocab.
        :type request: :class:`taifucloudcloud.asr.v20190614.models.UpdateAsrVocabRequest`
        :rtype: :class:`taifucloudcloud.asr.v20190614.models.UpdateAsrVocabResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAsrVocab", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAsrVocabResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)