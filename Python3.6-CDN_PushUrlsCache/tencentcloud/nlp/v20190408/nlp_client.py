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
from tencentcloud.nlp.v20190408 import models


class NlpClient(AbstractClient):
    _apiVersion = '2019-04-08'
    _endpoint = 'nlp.tencentcloudapi.com'


    def AutoSummarization(self, request):
        """利用人工智慧算法，自動抽取文本中的關鍵訊息并生成指定長度的文本摘要。可用于新聞标題生成、科技文獻摘要生成和商品評論摘要等。

        :param request: Request instance for AutoSummarization.
        :type request: :class:`tencentcloud.nlp.v20190408.models.AutoSummarizationRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.AutoSummarizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AutoSummarization", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AutoSummarizationResponse()
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


    def ChatBot(self, request):
        """閑聊服務基于騰訊領先的NLP引擎能力、數據運算能力和千億級網際網路語料數據的支援，同時內建了廣泛的知識問答能力，可實現上百種自定義屬性配置，以及兒童語言風格及說話方式，從而讓聊天變得更睿智、簡單和有趣。


        :param request: Request instance for ChatBot.
        :type request: :class:`tencentcloud.nlp.v20190408.models.ChatBotRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.ChatBotResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ChatBot", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ChatBotResponse()
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


    def DependencyParsing(self, request):
        """句法依存分析介面能夠分析出句子中詞與詞之間的相互依存關系，并揭示其句法結構，包括主謂關系、動賓關系、核心關系等等，可用于提取句子主幹、提取句子核心詞等，在機器翻譯、自動問答、知識抽取等領域都有很好的應用。

        :param request: Request instance for DependencyParsing.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DependencyParsingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DependencyParsingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DependencyParsing", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DependencyParsingResponse()
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


    def DescribeEntity(self, request):
        """輸入實體名稱，返回實體相關的訊息如實體别名、實體英文名、實體詳細訊息、相關實體等。

        :param request: Request instance for DescribeEntity.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DescribeEntityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DescribeEntityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEntity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEntityResponse()
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


    def DescribeRelation(self, request):
        """輸入兩個實體，返回兩個實體間的關系，例如馬化騰與騰訊公司不僅是相關實體，二者還存在隸屬關系（馬化騰屬于騰訊公司）。

        :param request: Request instance for DescribeRelation.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DescribeRelationRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DescribeRelationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRelation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRelationResponse()
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


    def DescribeTriple(self, request):
        """三元組查詢，主要分爲兩類，SP查詢和PO查詢。SP查詢表示已知主語和謂語查詢賓語，PO查詢表示已知賓語和謂語查詢主語。每一個SP或PO查詢都是一個可獨立執行的查詢，TQL支援SP查詢的嵌套查詢，即主語可以是一個嵌套的子查詢。其他複雜的三元組查詢方法，請參考官網API文件範例。

        :param request: Request instance for DescribeTriple.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DescribeTripleRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DescribeTripleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTriple", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTripleResponse()
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


    def KeywordsExtraction(self, request):
        """基于關鍵詞提取平台，通過對文本内容進行深度分析，提取出文本内容中的關鍵訊息，爲用戶實現諸如新聞内容關鍵詞自動提取、評論關鍵詞提取等提供基礎服務。

        :param request: Request instance for KeywordsExtraction.
        :type request: :class:`tencentcloud.nlp.v20190408.models.KeywordsExtractionRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.KeywordsExtractionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("KeywordsExtraction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.KeywordsExtractionResponse()
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


    def LexicalAnalysis(self, request):
        """詞法分析介面提供以下三個功能：

        1、智慧分詞：将連續的自然語言文本，切分成具有語義合理性和完整性的詞匯序列；

        2、詞性标注：爲每一個詞附上對應的詞性，例如名詞、代詞、形容詞、動詞等；

        3、命名實體識别：快速識别文本中的實體，例如人名、地名、機構名等。

        所有的功能均基于千億級大規模網際網路語料進行持續叠代更新，以保證效果不斷提升，用戶無需擔心新詞發現、歧義消除、調用效能等問題。目前詞法分析已經在泛網際網路、金融、政務等不同垂直領域提供業務支援，并取得良好的效果。

        :param request: Request instance for LexicalAnalysis.
        :type request: :class:`tencentcloud.nlp.v20190408.models.LexicalAnalysisRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.LexicalAnalysisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LexicalAnalysis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LexicalAnalysisResponse()
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


    def SentenceEmbedding(self, request):
        """句向量介面能夠将輸入的句子映射成一個固定維度的向量，用來表示這個句子的語義特征，可用于文本聚類、文本相似度、文本分類等任務，能夠顯著提高它們的效果。

        該句向量服務由騰訊知文自然語言處理團隊聯合騰訊AI Lab共同打造，基于千億級大規模網際網路語料并采用AI Lab自研的DSG算法訓練而成，在騰訊内部諸多業務的NLP任務上實測效果顯著。

        :param request: Request instance for SentenceEmbedding.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentenceEmbeddingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentenceEmbeddingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SentenceEmbedding", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SentenceEmbeddingResponse()
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


    def SentenceSimilarity(self, request):
        """文本相似度介面能夠基于深度學習技術來計算兩個輸入文本的相似度，相似度數值越大的兩個文本在語義上越相似。目前僅支援短文本的相似度計算，長文本的相似度計算也即将推出。

        鑒于文本相似度是一個應用非常廣泛的功能，騰訊知文自然語言處理團隊在深度神經網絡模型的基礎上，專門針對文本相似任務進行了優化，并持續叠代更新。基于文本相似度，可以輕松實現諸如文本去重、相似推薦等功能。

        :param request: Request instance for SentenceSimilarity.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentenceSimilarityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentenceSimilarityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SentenceSimilarity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SentenceSimilarityResponse()
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


    def SentimentAnalysis(self, request):
        """情感分析介面能夠對帶有情感色彩的主觀性文本進行分析、處理、歸納和推理，識别出用戶的情感傾向，是積極還是消極，并且提供各自概率。

        該功能基于基于千億級大規模網際網路語料和LSTM、BERT等深度神經網絡模型進行訓練，并持續叠代更新，以保證效果不斷提升。

        :param request: Request instance for SentimentAnalysis.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentimentAnalysisRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentimentAnalysisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SentimentAnalysis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SentimentAnalysisResponse()
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


    def SimilarWords(self, request):
        """相似詞介面能夠基于同義詞庫及詞向量技術，檢索出與輸入詞語在語義上最相似的若幹個詞語，可廣泛用于檢索系統、問答系統、文件歸檔等場景。

        :param request: Request instance for SimilarWords.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SimilarWordsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SimilarWordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SimilarWords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SimilarWordsResponse()
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


    def TextClassification(self, request):
        """文本分類介面能夠對用戶輸入的文本進行自動分類，将其映射到具體的類目上，用戶只需要提供待分類的文本，而無需關注具體實現。

        該功能基于基于千億級大規模網際網路語料和LSTM、BERT等深度神經網絡模型進行訓練，并持續叠代更新，以保證效果不斷提升。

        目前已提供：

        - 通用領域分類體系，包括15個分類類目，分别是汽車、科技、健康、體育、旅行、教育、職業、文化、軍事、房産、娛樂、女性、奧運、财經以及其他，适用于通用的場景。

        - 新聞領域分類體系，包括37個一級分類類目，285個二級分類（詳細請見 [類目體系映射表](https://cloud.tencent.com/document/product/271/36459)），已應用于騰訊新聞的文章分類。

        更多垂直領域的分類體系即将推出，敬請期待。

        :param request: Request instance for TextClassification.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextClassificationRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextClassificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextClassification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextClassificationResponse()
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


    def TextCorrection(self, request):
        """提供對中文文本的自動糾錯功能，能夠識别輸入文本中的錯誤片段，定位錯誤并給出正确的文本結果；支援長度不超過2000字的長文本糾錯。

        此功能是基于千億級大規模網際網路語料和LSTM、BERT等深度神經網絡模型進行訓練，并持續叠代更新，以保證效果不斷提升，是搜索引擎、語音識别、内容審核等功能更好運作的基礎之一。

        :param request: Request instance for TextCorrection.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextCorrection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextCorrectionResponse()
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


    def WordEmbedding(self, request):
        """詞向量介面能夠将輸入的詞語映射成一個固定維度的詞向量，用來表示這個詞語的語義特征。詞向量是很多自然語言處理技術的基礎，能夠顯著提高它們的效果。

        該詞向量服務由騰訊知文自然語言處理團隊聯合騰訊AI Lab共同打造。使用的詞向量基于千億級大規模網際網路語料并采用AI Lab自研的DSG算法訓練而成，開源的詞向量包含800多萬中文詞匯，在函蓋率、新鮮度及準确性等三方面效能突出。

        騰訊AI Lab詞向量相關資料：

        https://ai.tencent.com/ailab/zh/news/detial?id=22

        https://ai.tencent.com/ailab/nlp/embedding.html

        :param request: Request instance for WordEmbedding.
        :type request: :class:`tencentcloud.nlp.v20190408.models.WordEmbeddingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.WordEmbeddingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("WordEmbedding", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WordEmbeddingResponse()
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


    def WordSimilarity(self, request):
        """詞相似度介面能夠基于詞向量技術來計算兩個輸入詞語的餘弦相似度，相似度數值越大的兩個詞語在語義上越相似。

        :param request: Request instance for WordSimilarity.
        :type request: :class:`tencentcloud.nlp.v20190408.models.WordSimilarityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.WordSimilarityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("WordSimilarity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WordSimilarityResponse()
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