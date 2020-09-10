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
from taifucloudcloud.cr.v20180321 import models


class CrClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'cr.taifucloudcloudapi.com'


    def ApplyBlackList(self, request):
        """提交黑名單後，黑名單中有效期内的号碼将停止撥打，适用于到期/逾期提醒、回訪場景。

        :param request: Request instance for ApplyBlackList.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.ApplyBlackListRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.ApplyBlackListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyBlackList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyBlackListResponse()
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


    def ApplyCreditAudit(self, request):
        """提交信審外呼申請，返回當次請求日期。

        :param request: Request instance for ApplyCreditAudit.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.ApplyCreditAuditRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.ApplyCreditAuditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyCreditAudit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyCreditAuditResponse()
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


    def DescribeCreditResult(self, request):
        """根據信審任務ID和請求日期，獲取相關信審結果。

        :param request: Request instance for DescribeCreditResult.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.DescribeCreditResultRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.DescribeCreditResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCreditResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCreditResultResponse()
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


    def DescribeRecords(self, request):
        """用于獲取指定案件的錄音網址，次日早上8:00後可查詢前日錄音。

        :param request: Request instance for DescribeRecords.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.DescribeRecordsRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.DescribeRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordsResponse()
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
        """根據上傳文件介面的輸出參數DataResId，獲取相關上傳結果。

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.DescribeTaskStatusRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.DescribeTaskStatusResponse`

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


    def DownloadDialogueText(self, request):
        """用于獲取指定案件的對話文本内容，次日早上8:00後可查詢前日對話文本内容。

        :param request: Request instance for DownloadDialogueText.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.DownloadDialogueTextRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.DownloadDialogueTextResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadDialogueText", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadDialogueTextResponse()
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


    def DownloadRecordList(self, request):
        """<p>用于獲取錄音下載連結清單，次日早上8:00後可查詢前日錄音清單。</p>
        <p>注意：錄音清單中的錄音下載連結僅次日20:00之前有效，請及時下載。</p>

        :param request: Request instance for DownloadRecordList.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.DownloadRecordListRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.DownloadRecordListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadRecordList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadRecordListResponse()
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


    def DownloadReport(self, request):
        """用于下載結果報表。當日23:00後，可獲取當日到期/逾期提醒結果，次日00:30後，可獲取昨日回訪結果。

        :param request: Request instance for DownloadReport.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.DownloadReportRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.DownloadReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadReportResponse()
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


    def QueryInstantData(self, request):
        """實時數據查詢

        :param request: Request instance for QueryInstantData.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.QueryInstantDataRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.QueryInstantDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryInstantData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryInstantDataResponse()
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


    def UploadDataFile(self, request):
        """上傳文件，介面返回數據任務ID，支援xlsx、xls、csv、zip格式。

        :param request: Request instance for UploadDataFile.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.UploadDataFileRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.UploadDataFileResponse`

        """
        try:
            params = request._serialize()
            options = {'IsMultipart': True, 'BinaryParams': [u'File']}
            body = self.call("UploadDataFile", params, options=options)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadDataFileResponse()
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


    def UploadDataJson(self, request):
        """上傳Json格式數據，介面返回數據任務ID

        :param request: Request instance for UploadDataJson.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.UploadDataJsonRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.UploadDataJsonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadDataJson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadDataJsonResponse()
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


    def UploadFile(self, request):
        """客戶通過調用該介面上傳需催收文件，格式需爲excel格式。介面返回任務ID。

        :param request: Request instance for UploadFile.
        :type request: :class:`taifucloudcloud.cr.v20180321.models.UploadFileRequest`
        :rtype: :class:`taifucloudcloud.cr.v20180321.models.UploadFileResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadFile", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadFileResponse()
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