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
from taifucloudcloud.tmt.v20180321 import models


class TmtClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'tmt.taifucloudcloudapi.com'


    def ImageTranslate(self, request):
        """提供中文到英文、英文到中文兩種語言的圖片翻譯服務，可自動識别圖片中的文本内容并翻譯成目标語言，識别後的文本按行翻譯，後續會提供可按段落翻譯的版本。<br />
        提示：對于一般開發者，我們建議優先使用SDK接入簡化開發。SDK使用介紹請直接檢視 5. 開發者資源 部分。

        :param request: Request instance for ImageTranslate.
        :type request: :class:`taifucloudcloud.tmt.v20180321.models.ImageTranslateRequest`
        :rtype: :class:`taifucloudcloud.tmt.v20180321.models.ImageTranslateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageTranslate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageTranslateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def LanguageDetect(self, request):
        """可自動識别文本内容的語言種類，輕量高效，無需額外實現判斷方式，使面向客戶的服務體驗更佳。 <br />
        提示：對于一般開發者，我們建議優先使用SDK接入簡化開發。SDK使用介紹請直接檢視 5. 開發者資源 部分。

        :param request: Request instance for LanguageDetect.
        :type request: :class:`taifucloudcloud.tmt.v20180321.models.LanguageDetectRequest`
        :rtype: :class:`taifucloudcloud.tmt.v20180321.models.LanguageDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LanguageDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LanguageDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SpeechTranslate(self, request):
        """本介面提供上傳音訊，将音訊進行語音識别并翻譯成文本的服務，目前開放中英互譯的語音翻譯服務。
        待識别和翻譯的音訊文件可以是 pcm、mp3和speex 格式，pcm采樣率要求16kHz、位深16bit、單聲道，音訊内語音清晰。<br/>
        如果采用流式傳輸的方式，要求每個分片時長200ms~500ms；如果采用非流式的傳輸方式，要求音訊時長不超過8s。注意最後一個分片的IsEnd參數設置爲1。<br />
        提示：對于一般開發者，我們建議優先使用SDK接入簡化開發。SDK使用介紹請直接檢視 5. 開發者資源部分。

        :param request: Request instance for SpeechTranslate.
        :type request: :class:`taifucloudcloud.tmt.v20180321.models.SpeechTranslateRequest`
        :rtype: :class:`taifucloudcloud.tmt.v20180321.models.SpeechTranslateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SpeechTranslate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SpeechTranslateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextTranslate(self, request):
        """提供中文到英文、英文到中文的等多種語言的文本内容翻譯服務， 經過大數據語料庫、多種解碼算法、翻譯引擎深度優化，在新聞文章、生活口語等不同語言場景中都有深厚積累，翻譯結果專業評價處于行業領先水平。<br />
        提示：對于一般開發者，我們建議優先使用SDK接入簡化開發。SDK使用介紹請直接檢視 5. 開發者資源 部分。

        :param request: Request instance for TextTranslate.
        :type request: :class:`taifucloudcloud.tmt.v20180321.models.TextTranslateRequest`
        :rtype: :class:`taifucloudcloud.tmt.v20180321.models.TextTranslateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextTranslate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextTranslateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextTranslateBatch(self, request):
        """文本翻譯的批次介面

        :param request: Request instance for TextTranslateBatch.
        :type request: :class:`taifucloudcloud.tmt.v20180321.models.TextTranslateBatchRequest`
        :rtype: :class:`taifucloudcloud.tmt.v20180321.models.TextTranslateBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextTranslateBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextTranslateBatchResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)