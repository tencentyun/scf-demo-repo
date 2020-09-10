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
from tencentcloud.tiia.v20190529 import models


class TiiaClient(AbstractClient):
    _apiVersion = '2019-05-29'
    _endpoint = 'tiia.tencentcloudapi.com'


    def AssessQuality(self, request):
        """評估輸入圖片在視覺上的質量，從多個方面評估，并同時給出綜合的、客觀的清晰度評分，和主觀的美觀度評分。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for AssessQuality.
        :type request: :class:`tencentcloud.tiia.v20190529.models.AssessQualityRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.AssessQualityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssessQuality", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssessQualityResponse()
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


    def CropImage(self, request):
        """根據輸入的裁剪比例，智慧判斷一張圖片的最佳裁剪區域，确保原圖的主體區域不受影響。

        可以自動裁剪圖片，适應不同平台、設備的展示要求，避免簡單拉伸帶來的變形。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for CropImage.
        :type request: :class:`tencentcloud.tiia.v20190529.models.CropImageRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.CropImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CropImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CropImageResponse()
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


    def DetectCelebrity(self, request):
        """傳入一張圖片，可以識别圖片中包含的人物是否爲公衆人物，如果是，輸出人物的姓名、基本訊息、臉部坐标。

        支援識别一張圖片中存在的多個人臉，針對每個人臉，會給出與之最相似的公衆人物。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for DetectCelebrity.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectCelebrityRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectCelebrityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectCelebrity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectCelebrityResponse()
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


    def DetectDisgust(self, request):
        """輸入一張圖片，返回AI針對一張圖片是否是惡心的一系列判斷值。

        通過惡心圖片識别, 可以判斷一張圖片是否令人惡心, 同時給出它屬于的潛在類别, 讓您能夠過濾掉使人不愉快的圖片。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for DetectDisgust.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectDisgustRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectDisgustResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectDisgust", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectDisgustResponse()
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


    def DetectLabel(self, request):
        """圖像标簽利用深度學習技術、海量訓練數據，可以對圖片進行智慧分類、物體識别等。

        目前支援8個大類、六十多個子類、數千個标簽。涵蓋各種日常場景、動植物、物品、美食、卡證等。具體分類請見[圖像分析常見問題功能與限制相關](https://cloud.tencent.com/document/product/865/39164)。

        圖像标簽提供三個版本供選擇：

        • 攝像頭版：針對搜索、手機攝像頭照片進行優化，涵蓋大量卡證、日常物品、二維碼條形碼。

        • 相冊版：針對手機相冊、網盤進行優化，去除相冊和網盤中不常見的标簽，針對相冊常見圖片類型（人像、日常活動、日常物品等）識别效果更好。

        • 網絡版：針對網絡圖片進行優化，涵蓋标簽更多，滿足長尾識别需求。

        每個産品的圖像類型都有獨特性，建議在接入初期，對三個版本進行對比評估後選擇合适的版本使用。

        爲了方便使用、減少圖片傳輸次數，圖像标簽包裝成多合一介面，實際上是多個服務。

        圖像标簽按照服務的實際使用數量進行收費。例如一張圖片同時調用相冊版、攝像頭版兩個服務，那麽此次調用按照兩次計費。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for DetectLabel.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectLabelRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectLabelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectLabel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectLabelResponse()
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


    def DetectMisbehavior(self, request):
        """可以識别輸入的圖片中是否包含不良行爲，例如打架鬥毆、賭博、抽煙等，可以應用于廣告圖、直播截圖、短視訊截圖等審核，減少不良行爲對平台内容質量的影響，維護健康向上的網際網路環境。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for DetectMisbehavior.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectMisbehaviorRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectMisbehaviorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectMisbehavior", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectMisbehaviorResponse()
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


    def DetectProduct(self, request):
        """本介面支援識别圖片中包含的商品，能夠輸出商品的品類名稱、類别，還可以輸出商品在圖片中的位置。支援一張圖片多個商品的識别。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for DetectProduct.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectProductRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectProductResponse()
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


    def DetectProductBeta(self, request):
        """商品識别-微信識物版，基于人工智慧技術、海量訓練圖片、億級商品庫，可以實現全函蓋、細粒度、高準确率的商品識别和商品推薦功能。
        本服務可以識别出圖片中的主體位置、主體商品類型，函蓋億級SKU，輸出具體商品的價格、型号等詳細訊息。
        客戶無需自建商品庫，即可快速實現商品識别、拍照搜商品等功能。

        目前“商品識别-微信識物版”爲内測服務，需要申請、開通後方可使用。請在[服務開通申請表](https://cloud.tencent.com/apply/p/y1q2mnf0vdl) 中填寫詳細訊息和需求，如果通過審核，我們将會在2個工作日内與您聯系，并開通服務。
        内測期間，本服務免費提供最高2QPS，收費模式和标準會在正式版上線前通過站内信、簡訊通知客戶。如果需要提升并發，請與我們聯系洽談。

        注意：本文件爲内測版本，僅适用于功能體驗和測試，正式業務接入請等待正式版。正式版的輸入、輸出可能會與内測版存在少量差異。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for DetectProductBeta.
        :type request: :class:`tencentcloud.tiia.v20190529.models.DetectProductBetaRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.DetectProductBetaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectProductBeta", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectProductBetaResponse()
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


    def EnhanceImage(self, request):
        """傳入一張圖片，輸出清晰度提升後的圖片。

        可以消除圖片有損壓縮導緻的噪聲，和使用濾鏡、拍攝失焦導緻的模糊。讓圖片的邊緣和細節更加清晰自然。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for EnhanceImage.
        :type request: :class:`tencentcloud.tiia.v20190529.models.EnhanceImageRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.EnhanceImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnhanceImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnhanceImageResponse()
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


    def RecognizeCar(self, request):
        """Top Cloud 車輛屬性識别可對汽車車身及車輛屬性進行檢測與識别，目前支援11種車身顔色、20多種車型、300多種品牌、4000多種車系+年款的識别，同時支援對車輛的位置進行檢測。如果圖片中存在多輛車，會分别輸出每輛車的車型和坐标。
        >
        - 公共參數中的簽名方式必須指定爲V3版本，即配置SignatureMethod參數爲TC3-HMAC-SHA256。

        :param request: Request instance for RecognizeCar.
        :type request: :class:`tencentcloud.tiia.v20190529.models.RecognizeCarRequest`
        :rtype: :class:`tencentcloud.tiia.v20190529.models.RecognizeCarResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecognizeCar", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecognizeCarResponse()
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