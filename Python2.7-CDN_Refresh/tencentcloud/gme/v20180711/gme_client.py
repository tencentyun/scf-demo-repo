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
from tencentcloud.gme.v20180711 import models


class GmeClient(AbstractClient):
    _apiVersion = '2018-07-11'
    _endpoint = 'gme.tencentcloudapi.com'


    def CreateApp(self, request):
        """本介面(CreateApp)用于創建一個GME應用。

        :param request: Request instance for CreateApp.
        :type request: :class:`tencentcloud.gme.v20180711.models.CreateAppRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.CreateAppResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAppResponse()
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


    def DescribeAppStatistics(self, request):
        """本介面(DescribeAppStatistics)用于獲取某個GME應用的用量數據。包括實時語音，語音訊息及轉文本，語音分析等。最長查詢週期爲最近30天。

        :param request: Request instance for DescribeAppStatistics.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAppStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAppStatisticsResponse()
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


    def DescribeFilterResult(self, request):
        """根據應用ID和文件ID查詢識别結果

        :param request: Request instance for DescribeFilterResult.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeFilterResultRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeFilterResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFilterResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFilterResultResponse()
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


    def DescribeFilterResultList(self, request):
        """根據日期查詢識别結果清單

        :param request: Request instance for DescribeFilterResultList.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeFilterResultListRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeFilterResultListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFilterResultList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFilterResultListResponse()
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


    def DescribeScanResultList(self, request):
        """本介面(DescribeScanResultList)用于查詢語音檢測結果，查詢任務清單最多支援100個。
        <p style="color:red">如果在提交語音檢測任務時未設置 Callback 欄位，則需要通過本介面獲取檢測結果</p>

        :param request: Request instance for DescribeScanResultList.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeScanResultListRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeScanResultListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScanResultList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScanResultListResponse()
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


    def ModifyAppStatus(self, request):
        """本介面(ModifyAppStatus)用于修改應用總開關狀态。

        :param request: Request instance for ModifyAppStatus.
        :type request: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAppStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAppStatusResponse()
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


    def ScanVoice(self, request):
        """本介面(ScanVoice)用于提交語音檢測任務，檢測任務清單最多支援100個。使用前請您登入[控制台 - 服務配置](https://console.cloud.tencent.com/gamegme/conf)開啓語音分析服務。
        </br></br>

        <h4><b>功能試用說明：</b></h4>
        <li>打開前往<a href="https://console.cloud.tencent.com/gamegme/tryout">控制台 - 産品試用</a>免費試用語音分析服務。</li>
        </br>

        <h4><b>介面功能說明：</b></h4>
        <li>支援對語音流或語音文件進行檢測，判斷其中是否包含違規内容。</li>
        <li>支援設置回調網址 Callback 獲取檢測結果，同時支援通過介面(查詢語音檢測結果)主動輪詢獲取檢測結果。</li>
        <li>支援場景輸入，包括：謾罵、色情、涉政等場景</li>
        <li>支援批次提交檢測任務。檢測任務清單最多支援100個。</li>
        </br>
        <h4><b>音訊文件限制說明：</b></h4>
        <li>音訊文件大小限制：100 M</li>
        <li>音訊文件時長限制：30分鍾</li>
        <li>音訊文件格式支援的類型：.wav、.m4a、.amr、.mp3、.aac、.wma、.ogg</li>
        </br>
        <h4><b>語音流限制說明：</b></h4>
        <li>語音流格式支援的類型：.m3u8、.flv</li>
        <li>語音流支援的傳輸協議：RTMP、HTTP、HTTPS</li>
        <li>語音流時長限制：4小時</li>
        <li>支援影音流分離并對音訊流進行分析</li>
        </br>
        <h4 id="Label_Value"><b>Scenes 與 Label 參數說明：</b></h4>
        <p>提交語音檢測任務時，需要指定 Scenes 場景參數，<font color="red">目前要求您設置 Scenes 參數值爲：["default"]</font>；而在檢測結果中，則包含請求時指定的場景，以及對應類型的檢測結果。</p>
        <table>
        <thread>
        <tr>
        <th>場景</th>
        <th>描述</th>
        <th>Label</th>
        </tr>
        </thread>
        <tbody>
        <tr>
        <td>語音檢測</td>
        <td>語音檢測的檢測類型</td>
        <td>
        <p>normal:正常文本</p>
        <p>porn:色情</p>
        <p>politics:涉政</p>
        <p>abuse:謾罵</p>
        <p>ad :廣告</p>
        <p>terrorism:暴恐</p>
        <p>contraband :違禁</p>
        <p>customized:自定義詞庫。目前白名單開放，如有需要請<a href="https://cloud.tencent.com/apply/p/8809fjcik56">聯系我們</a>。</p>
        </td>
        </tr>
        </tbody>
        </table>
        </br>
        <h4 id="Callback_Declare"><b>回調相關說明：</b></h4>
        <li>如果在請求參數中指定了回調網址參數 Callback，即一個 HTTP(S) 協議介面的 URL，則需要支援 POST 方法，傳輸數據編碼采用 UTF-8。</li>
        <li>在推送回調數據後，接收到的 HTTP 狀态碼爲 200 時，表示推送成功。</li>
        <li>HTTP 頭參數說明：</li>
        <table>
        <thread>
        <tr>
        <th>名稱</th>
        <th>類型</th>
        <th>是否必需</th>
        <th>描述</th>
        </tr>
        </thread>
        <tbody>
        <tr>
        <td>Signatue</td>
        <td>string</td>
        <td>是</td>
        <td>簽名，具體見<a href="#Callback_Signatue">簽名生成說明</a></td>
        </tr>
        </tbody>
        </table>
        <ul  id="Callback_Signatue">
        	<li>簽名生成說明：</li>
        	<ul>
        		<li>使用 HMAC-SH1 算法, 最終結果做 BASE64 編碼;</li>
        		<li>簽名原文串爲 POST+body 的整個json内容(長度以 Content-Length 爲準);</li>
        		<li>簽名key爲應用的 SecretKey，可以通過控制台檢視。</li>
        	</ul>
        </ul>

        <li>回調範例如下<font color="red">（詳細欄位說明見結構：
        <a href="https://cloud.tencent.com/document/api/607/35375#DescribeScanResult" target="_blank">DescribeScanResult</a>）</font>：</li>
        <pre><code>{
        	"Code": 0,
        	"DataId": "1400000000_test_data_id",
        	"ScanFinishTime": 1566720906,
        	"HitFlag": true,
        	"Live": false,
        	"Msg": "",
        	"ScanPiece": [{
        		"DumpUrl": "",
        		"HitFlag": true,
        		"MainType": "abuse",
        		"RoomId": "123",
        		"OpenId": "xxx",
        		"Info":"",
        		"Offset": 0,
        		"Duration": 3400,
        		"PieceStartTime":1574684231,
        		"ScanDetail": [{
        			"EndTime": 1110,
        			"KeyWord": "xxx",
        			"Label": "abuse",
        			"Rate": "90.00",
        			"StartTime": 1110
        		}, {
        			"EndTime": 1380,
        			"KeyWord": "xxx",
        			"Label": "abuse",
        			"Rate": "90.00",
        			"StartTime": 930
        		}, {
        			"EndTime": 1560,
        			"KeyWord": "xxx",
        			"Label": "abuse",
        			"Rate": "90.00",
        			"StartTime": 930
        		}, {
        			"EndTime": 2820,
        			"KeyWord": "xxx",
        			"Label": "abuse",
        			"Rate": "90.00",
        			"StartTime": 2490
        		}]
        	}],
        	"ScanStartTime": 1566720905,
        	"Scenes": [
        		"default"
        	],
        	"Status": "Success",
        	"TaskId": "xxx",
        	"Url": "https://xxx/xxx.m4a"
        }
        </code></pre>

        :param request: Request instance for ScanVoice.
        :type request: :class:`tencentcloud.gme.v20180711.models.ScanVoiceRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ScanVoiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScanVoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScanVoiceResponse()
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


    def VoiceFilter(self, request):
        """本介面用于識别涉黃、涉政等違規音訊，成功會回調配置在應用的回調網址。回調範例如下：
        {"BizId":0,"FileId":"test_file_id","FileName":"test_file_name","FileUrl":"test_file_url","OpenId":"test_open_id","TimeStamp":"0000-00-00 00:00:00","Data":[{"Type":1,"Word":"xx"}]}
        Type表示過濾類型，1：政治，2：色情，3：謾罵

        :param request: Request instance for VoiceFilter.
        :type request: :class:`tencentcloud.gme.v20180711.models.VoiceFilterRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.VoiceFilterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VoiceFilter", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VoiceFilterResponse()
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