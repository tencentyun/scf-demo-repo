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
from taifucloudcloud.aai.v20180522 import models


class AaiClient(AbstractClient):
    _apiVersion = '2018-05-22'
    _endpoint = 'aai.taifucloudcloudapi.com'


    def Chat(self, request):
        """提供基于文本的基礎聊天能力，可以讓您的應用快速擁有具備深度語義理解的機器聊天功能。

        :param request: 調用Chat所需參數的結構體。
        :type request: :class:`taifucloudcloud.aai.v20180522.models.ChatRequest`
        :rtype: :class:`taifucloudcloud.aai.v20180522.models.ChatResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Chat", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ChatResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """識别60s内的短語音，當音訊放在請求body中傳輸時整個請求大小不能超過600KB，當音訊以url方式傳輸時，音訊時長不可超過60s。所有請求參數放在post的body中采用x-www-form-urlencoded（數據轉換成一個字串（name1=value1&name2=value2…）進行urlencode後）編碼傳輸。現暫只支援中文普通話識别，支援識别8k(16k)的16bit的mp3或者wav音訊。

        :param request: 調用SentenceRecognition所需參數的結構體。
        :type request: :class:`taifucloudcloud.aai.v20180522.models.SentenceRecognitionRequest`
        :rtype: :class:`taifucloudcloud.aai.v20180522.models.SentenceRecognitionResponse`

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


    def SimultaneousInterpreting(self, request):
        """該介面是實時流式識别，可同時返回語音識别文本及翻譯文本，當前僅支援中文和英文。該介面可配合同傳windows用戶端，提供會議現場同傳服務。

        :param request: 調用SimultaneousInterpreting所需參數的結構體。
        :type request: :class:`taifucloudcloud.aai.v20180522.models.SimultaneousInterpretingRequest`
        :rtype: :class:`taifucloudcloud.aai.v20180522.models.SimultaneousInterpretingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SimultaneousInterpreting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SimultaneousInterpretingResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextToVoice(self, request):
        """Top Cloud 語音合成技術（TTS）可以将任意文本轉化爲語音，實現讓機器和應用張口說話。
         TTS技術可以應用到很多場景，比如，行動APP語音播報新聞；智慧設備語音提醒；依靠網上現有節目或少量錄音，快速合成明星語音，降低邀約成本；支援車載導航語音合成的個性化語音播報。
        内測期間免費使用。

        :param request: 調用TextToVoice所需參數的結構體。
        :type request: :class:`taifucloudcloud.aai.v20180522.models.TextToVoiceRequest`
        :rtype: :class:`taifucloudcloud.aai.v20180522.models.TextToVoiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextToVoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextToVoiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)