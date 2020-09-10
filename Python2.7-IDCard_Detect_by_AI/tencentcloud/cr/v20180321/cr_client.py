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
        """加入黑名單的客戶，将停止撥打。用于：
        将客戶進行黑名單的增加和移除，用于對某些客戶階段性停催。

        :param request: 調用ApplyBlackList所需參數的結構體。
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

        :param request: 調用ApplyCreditAudit所需參數的結構體。
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

        :param request: 調用DescribeCreditResult所需參數的結構體。
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

        :param request: 調用DescribeRecords所需參數的結構體。
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

        :param request: 調用DescribeTaskStatus所需參數的結構體。
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


    def DownloadReport(self, request):
        """用于下載當日催收和回訪結果報表。當日23:00後，可獲取當日催收結果，次日00:30後，可獲取昨日回訪結果。

        :param request: 調用DownloadReport所需參數的結構體。
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


    def UploadDataFile(self, request):
        """<p>該介面包含上傳下列文件：</p>
        <ol style="margin-bottom:10px;">
          <li>入催文件：用于每天入催文件的上傳</li>
          <li>回訪文件：用于每天貸中回訪文件的上傳</li>
          <li>還款文件：實時上傳當前已還款客戶，用于還款客戶的實時停催</li>
        </ol>
        介面返回數據任務ID，支援xlsx、xls、csv、zip格式，文件大小不超過50MB。

        :param request: 調用UploadDataFile所需參數的結構體。
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


    def UploadFile(self, request):
        """客戶通過調用該介面上傳需催收文件，格式需爲excel格式。介面返回任務ID。

        :param request: 調用UploadFile所需參數的結構體。
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