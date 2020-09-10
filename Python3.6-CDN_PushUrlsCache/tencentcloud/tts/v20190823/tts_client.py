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
from taifucloudcloud.tts.v20190823 import models


class TtsClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'tts.taifucloudcloudapi.com'


    def TextToVoice(self, request):
        """Top Cloud 語音合成技術（TTS）可以将任意文本轉化爲語音，實現讓機器和應用張口說話。
         TTS技術可以應用到很多場景，比如，行動APP語音播報新聞；智慧設備語音提醒；依靠網上現有節目或少量錄音，快速合成明星語音，降低邀約成本；支援車載導航語音合成的個性化語音播報。
        内測期間免費使用。

        :param request: Request instance for TextToVoice.
        :type request: :class:`taifucloudcloud.tts.v20190823.models.TextToVoiceRequest`
        :rtype: :class:`taifucloudcloud.tts.v20190823.models.TextToVoiceResponse`

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