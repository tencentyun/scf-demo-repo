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
from tencentcloud.soe.v20180724 import models


class SoeClient(AbstractClient):
    _apiVersion = '2018-07-24'
    _endpoint = 'soe.tencentcloudapi.com'


    def InitOralProcess(self, request):
        """初始化發音評估過程，每一輪評估前進行調用。語音輸入模式分爲流式模式和非流式模式，流式模式支援數據分片傳輸，可以加快評估響應速度。評估模式分爲詞模式和句子模式，詞模式會标注每個音節的詳細訊息；句子模式會有完整度和流利度的評估。

        :param request: 調用InitOralProcess所需參數的結構體。
        :type request: :class:`tencentcloud.soe.v20180724.models.InitOralProcessRequest`
        :rtype: :class:`tencentcloud.soe.v20180724.models.InitOralProcessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitOralProcess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitOralProcessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransmitOralProcess(self, request):
        """傳輸音訊數據，必須在完成發音評估初始化介面之後調用，且SessonId要與初始化介面保持一緻。分片傳輸時，盡量保證SeqId順序傳輸。音訊源目前僅支援16k采樣率16bit單聲道編碼方式，如有不一緻可能導緻評估不準确或失敗。

        :param request: 調用TransmitOralProcess所需參數的結構體。
        :type request: :class:`tencentcloud.soe.v20180724.models.TransmitOralProcessRequest`
        :rtype: :class:`tencentcloud.soe.v20180724.models.TransmitOralProcessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransmitOralProcess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransmitOralProcessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransmitOralProcessWithInit(self, request):
        """初始化并傳輸音訊數據，分片傳輸時，盡量保證SeqId順序傳輸。音訊源目前僅支援16k采樣率16bit單聲道編碼方式，如有不一緻可能導緻評估不準确或失敗。

        :param request: 調用TransmitOralProcessWithInit所需參數的結構體。
        :type request: :class:`tencentcloud.soe.v20180724.models.TransmitOralProcessWithInitRequest`
        :rtype: :class:`tencentcloud.soe.v20180724.models.TransmitOralProcessWithInitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransmitOralProcessWithInit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransmitOralProcessWithInitResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)