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

from tencentcloud.common.abstract_model import AbstractModel


class ApplyBlackListRequest(AbstractModel):
    """ApplyBlackList請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組
        :type Module: str
        :param Operation: 操作
        :type Operation: str
        :param BlackList: 黑名單清單
        :type BlackList: list of SingleBlackApply
        :param InstId: 實例ID，不傳預設爲系統分配的初始實例
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.BlackList = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        if params.get("BlackList") is not None:
            self.BlackList = []
            for item in params.get("BlackList"):
                obj = SingleBlackApply()
                obj._deserialize(item)
                self.BlackList.append(obj)
        self.InstId = params.get("InstId")


class ApplyBlackListResponse(AbstractModel):
    """ApplyBlackList返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ApplyCreditAuditRequest(AbstractModel):
    """ApplyCreditAudit請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組
        :type Module: str
        :param Operation: 操作
        :type Operation: str
        :param InstId: 實例ID
        :type InstId: str
        :param ProductId: 産品ID，形如P******。
        :type ProductId: str
        :param CaseId: 信審任務ID，同一天内，同一InstId下，同一CaseId只能調用一次。
        :type CaseId: str
        :param CallbackUrl: 回調網址
        :type CallbackUrl: str
        :param Data: JSON格式的業務欄位。
        :type Data: str
        """
        self.Module = None
        self.Operation = None
        self.InstId = None
        self.ProductId = None
        self.CaseId = None
        self.CallbackUrl = None
        self.Data = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.InstId = params.get("InstId")
        self.ProductId = params.get("ProductId")
        self.CaseId = params.get("CaseId")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Data = params.get("Data")


class ApplyCreditAuditResponse(AbstractModel):
    """ApplyCreditAudit返回參數結構體

    """

    def __init__(self):
        """
        :param RequestDate: 請求日期
        :type RequestDate: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestDate = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestDate = params.get("RequestDate")
        self.RequestId = params.get("RequestId")


class DescribeCreditResultRequest(AbstractModel):
    """DescribeCreditResult請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組
        :type Module: str
        :param Operation: 操作
        :type Operation: str
        :param InstId: 實例ID
        :type InstId: str
        :param ProductId: 産品ID，形如P******。
        :type ProductId: str
        :param CaseId: 信審任務ID
        :type CaseId: str
        :param RequestDate: 請求日期
        :type RequestDate: str
        """
        self.Module = None
        self.Operation = None
        self.InstId = None
        self.ProductId = None
        self.CaseId = None
        self.RequestDate = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.InstId = params.get("InstId")
        self.ProductId = params.get("ProductId")
        self.CaseId = params.get("CaseId")
        self.RequestDate = params.get("RequestDate")


class DescribeCreditResultResponse(AbstractModel):
    """DescribeCreditResult返回參數結構體

    """

    def __init__(self):
        """
        :param ResultCode: <p>呼叫結果，取值範圍：</p><ul style="margin-bottom:0px;"><li>NON：接通</li><li>DBU：号碼忙</li><li>DRF：不在服務區</li><li>ANA：欠費未接聽</li><li>REJ：拒接</li><li>SHU：關機</li><li>NAN：空号</li><li>HAL：停機</li><li>DAD：未接聽</li><li>EXE：其他異常</li></ul>
        :type ResultCode: str
        :param ClientCode: 客戶标識代碼，多個标識碼以英文逗号分隔，ResultCode爲NON時才有。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClientCode: str
        :param RingStartTime: 開始振鈴時間，ResultCode爲NON或DAD時才有此欄位。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RingStartTime: str
        :param RingDuration: 振鈴時長
        :type RingDuration: int
        :param AnswerDuration: 接通時長
        :type AnswerDuration: int
        :param ContextValue: JSON格式的擴展訊息欄位，ResultCode爲NON時才有。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ContextValue: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultCode = None
        self.ClientCode = None
        self.RingStartTime = None
        self.RingDuration = None
        self.AnswerDuration = None
        self.ContextValue = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultCode = params.get("ResultCode")
        self.ClientCode = params.get("ClientCode")
        self.RingStartTime = params.get("RingStartTime")
        self.RingDuration = params.get("RingDuration")
        self.AnswerDuration = params.get("AnswerDuration")
        self.ContextValue = params.get("ContextValue")
        self.RequestId = params.get("RequestId")


class DescribeRecordsRequest(AbstractModel):
    """DescribeRecords請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組
        :type Module: str
        :param Operation: 操作
        :type Operation: str
        :param ProductId: 産品ID
        :type ProductId: str
        :param AccountNum: 案件編号
        :type AccountNum: str
        :param CalledPhone: 被叫号碼
        :type CalledPhone: str
        :param StartBizDate: 查詢起始日期
        :type StartBizDate: str
        :param EndBizDate: 查詢結束日期
        :type EndBizDate: str
        :param Offset: 分頁參數，索引，從0開始
        :type Offset: str
        :param Limit: 分頁參數，頁長
        :type Limit: str
        :param InstId: 實例ID，不傳預設爲系統分配的初始實例
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.ProductId = None
        self.AccountNum = None
        self.CalledPhone = None
        self.StartBizDate = None
        self.EndBizDate = None
        self.Offset = None
        self.Limit = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ProductId = params.get("ProductId")
        self.AccountNum = params.get("AccountNum")
        self.CalledPhone = params.get("CalledPhone")
        self.StartBizDate = params.get("StartBizDate")
        self.EndBizDate = params.get("EndBizDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstId = params.get("InstId")


class DescribeRecordsResponse(AbstractModel):
    """DescribeRecords返回參數結構體

    """

    def __init__(self):
        """
        :param RecordList: 錄音清單。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RecordList: list of SingleRecord
        :param TotalCount: 錄音總量。
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RecordList") is not None:
            self.RecordList = []
            for item in params.get("RecordList"):
                obj = SingleRecord()
                obj._deserialize(item)
                self.RecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param TaskId: 任務ID，形如abc-a0b1c2xyz
        :type TaskId: str
        """
        self.Module = None
        self.Operation = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.TaskId = params.get("TaskId")


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回參數結構體

    """

    def __init__(self):
        """
        :param TaskResult: 任務結果，例如上傳成功時返回“File Uploading Task Success.”
        :type TaskResult: str
        :param TaskType: <p>任務類型：</p><ul style="margin-bottom:0px;"><li>報告下載：001</li><li>催收數據上傳：002</li><li>還款數據上傳：003</li><li>回訪數據上傳：004</li><li>停撥數據上傳：005</li></ul>
        :type TaskType: str
        :param TaskFileUrl: 過濾文件下載連結，有過濾數據時才存在。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskFileUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.TaskType = None
        self.TaskFileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskResult = params.get("TaskResult")
        self.TaskType = params.get("TaskType")
        self.TaskFileUrl = params.get("TaskFileUrl")
        self.RequestId = params.get("RequestId")


class DownloadReportRequest(AbstractModel):
    """DownloadReport請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param ReportDate: 報告日期
        :type ReportDate: str
        :param InstId: 實例ID，不傳預設爲系統分配的初始實例。
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.ReportDate = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.ReportDate = params.get("ReportDate")
        self.InstId = params.get("InstId")


class DownloadReportResponse(AbstractModel):
    """DownloadReport返回參數結構體

    """

    def __init__(self):
        """
        :param DailyReportUrl: 催收日報下載網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type DailyReportUrl: str
        :param ResultReportUrl: 催收結果下載網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type ResultReportUrl: str
        :param DetailReportUrl: 催收明細下載網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type DetailReportUrl: str
        :param CallbackDailyReportUrl: 回訪日報下載網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type CallbackDailyReportUrl: str
        :param CallbackResultReportUrl: 回訪結果下載網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type CallbackResultReportUrl: str
        :param CallbackDetailReportUrl: 回訪明細下載網址
注意：此欄位可能返回 null，表示取不到有效值。
        :type CallbackDetailReportUrl: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DailyReportUrl = None
        self.ResultReportUrl = None
        self.DetailReportUrl = None
        self.CallbackDailyReportUrl = None
        self.CallbackResultReportUrl = None
        self.CallbackDetailReportUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DailyReportUrl = params.get("DailyReportUrl")
        self.ResultReportUrl = params.get("ResultReportUrl")
        self.DetailReportUrl = params.get("DetailReportUrl")
        self.CallbackDailyReportUrl = params.get("CallbackDailyReportUrl")
        self.CallbackResultReportUrl = params.get("CallbackResultReportUrl")
        self.CallbackDetailReportUrl = params.get("CallbackDetailReportUrl")
        self.RequestId = params.get("RequestId")


class SingleBlackApply(AbstractModel):
    """黑名單申請訊息

    """

    def __init__(self):
        """
        :param BlackType: 黑名單類型，01代表手機号碼。
        :type BlackType: str
        :param OperationType: 操作類型，A爲新增，D爲删除。
        :type OperationType: str
        :param BlackValue: 黑名單值，BlackType爲01時，填寫11位手機号碼。
        :type BlackValue: str
        :param BlackDescription: 備注。
        :type BlackDescription: str
        :param BlackValidDate: 黑名單生效截止日期，格式爲YYYY-MM-DD，不填預設爲永久。
        :type BlackValidDate: str
        """
        self.BlackType = None
        self.OperationType = None
        self.BlackValue = None
        self.BlackDescription = None
        self.BlackValidDate = None


    def _deserialize(self, params):
        self.BlackType = params.get("BlackType")
        self.OperationType = params.get("OperationType")
        self.BlackValue = params.get("BlackValue")
        self.BlackDescription = params.get("BlackDescription")
        self.BlackValidDate = params.get("BlackValidDate")


class SingleRecord(AbstractModel):
    """錄音訊息

    """

    def __init__(self):
        """
        :param AccountNum: 案件編号。
        :type AccountNum: str
        :param BizDate: 外呼日期。
        :type BizDate: str
        :param CallStartTime: 開始呼叫時間。
        :type CallStartTime: str
        :param CallerPhone: 主叫号碼。
        :type CallerPhone: str
        :param Direction: 呼叫方向，O爲呼出，I爲呼入。
        :type Direction: str
        :param Duration: 通話時長。
        :type Duration: int
        :param ProductId: 産品ID。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProductId: str
        :param RecordCosUrl: 錄音下載連結。
注意：此欄位可能返回 null，表示取不到有效值。
        :type RecordCosUrl: str
        """
        self.AccountNum = None
        self.BizDate = None
        self.CallStartTime = None
        self.CallerPhone = None
        self.Direction = None
        self.Duration = None
        self.ProductId = None
        self.RecordCosUrl = None


    def _deserialize(self, params):
        self.AccountNum = params.get("AccountNum")
        self.BizDate = params.get("BizDate")
        self.CallStartTime = params.get("CallStartTime")
        self.CallerPhone = params.get("CallerPhone")
        self.Direction = params.get("Direction")
        self.Duration = params.get("Duration")
        self.ProductId = params.get("ProductId")
        self.RecordCosUrl = params.get("RecordCosUrl")


class UploadDataFileRequest(AbstractModel):
    """UploadDataFile請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param FileName: 文件名
        :type FileName: str
        :param UploadModel: <p>上傳類型，不填預設催收文件，取值範圍：</p><ul style="margin-bottom:0px;"><li>data：催收文件</li><li>repay：還款文件</li><li>callback：回訪文件</li></ul>
        :type UploadModel: str
        :param File: 文件，文件與文件網址上傳只可選用一種，必須使用multipart/form-data協議來上傳二進制流文件，建議使用xlsx格式，大小不超過5MB。
        :type File: binary
        :param FileUrl: 文件上傳網址，文件與文件網址上傳只可選用一種，大小不超過50MB。
        :type FileUrl: str
        :param InstId: 實例ID，不傳預設爲系統分配的初始實例。
        :type InstId: str
        """
        self.Module = None
        self.Operation = None
        self.FileName = None
        self.UploadModel = None
        self.File = None
        self.FileUrl = None
        self.InstId = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.FileName = params.get("FileName")
        self.UploadModel = params.get("UploadModel")
        self.File = params.get("File")
        self.FileUrl = params.get("FileUrl")
        self.InstId = params.get("InstId")


class UploadDataFileResponse(AbstractModel):
    """UploadDataFile返回參數結構體

    """

    def __init__(self):
        """
        :param DataResId: 數據ID
        :type DataResId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataResId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataResId = params.get("DataResId")
        self.RequestId = params.get("RequestId")


class UploadFileRequest(AbstractModel):
    """UploadFile請求參數結構體

    """

    def __init__(self):
        """
        :param Module: 模組名
        :type Module: str
        :param Operation: 操作名
        :type Operation: str
        :param FileUrl: 文件上傳網址，要求網址協議爲HTTPS，且URL端口必須爲443
        :type FileUrl: str
        :param FileName: 文件名
        :type FileName: str
        :param FileDate: 文件日期
        :type FileDate: str
        """
        self.Module = None
        self.Operation = None
        self.FileUrl = None
        self.FileName = None
        self.FileDate = None


    def _deserialize(self, params):
        self.Module = params.get("Module")
        self.Operation = params.get("Operation")
        self.FileUrl = params.get("FileUrl")
        self.FileName = params.get("FileName")
        self.FileDate = params.get("FileDate")


class UploadFileResponse(AbstractModel):
    """UploadFile返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")