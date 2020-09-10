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
from taifucloudcloud.iir.v20200417 import models


class IirClient(AbstractClient):
    _apiVersion = '2020-04-17'
    _endpoint = 'iir.taifucloudcloudapi.com'


    def RecognizeProduct(self, request):
        """商品識别，使用 掃一掃識物同款技術，基于人工智慧技術、海量訓練圖片、億級商品庫，可以實現全函蓋、細粒度、高準确率的商品識别和商品推薦功能。 本服務可以識别出圖片中的主體位置、主體商品類型，函蓋億級SKU，輸出具體商品的價格、型号等詳細訊息。 客戶無需自建商品庫，即可快速實現商品識别、拍照搜商品等功能。

        目前“商品識别”爲公測服務，需要申請、開通後方可使用。請在[服務開通申請表](https://cloud.taifucloud.com/apply/p/y1q2mnf0vdl) 中填寫詳細訊息和需求，如果通過審核，我們将會在2個工作日内與您聯系，并開通服務。 公測期間，本服務免費提供最高2QPS，收費模式和标準會在正式版上線前通過站内信、簡訊通知客戶。如果需要提升并發，請與我們聯系洽談。

        注意：本文件爲公測版本，僅适用于功能體驗和測試，正式業務接入請等待正式版。正式版的輸入、輸出可能會與公測版存在少量差異。

        :param request: Request instance for RecognizeProduct.
        :type request: :class:`taifucloudcloud.iir.v20200417.models.RecognizeProductRequest`
        :rtype: :class:`taifucloudcloud.iir.v20200417.models.RecognizeProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecognizeProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecognizeProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)