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

from taifucloudcloud.common.abstract_model import AbstractModel


class Code(AbstractModel):
    """函數代碼

    """

    def __init__(self):
        """
        :param CosBucketName: 物件儲存桶名稱
        :type CosBucketName: str
        :param CosObjectName: 物件儲存對象路徑
        :type CosObjectName: str
        :param ZipFile: 包含函數代碼文件及其依賴項的 zip 格式文件，使用該介面時要求将 zip 文件的内容轉成 base64 編碼，最大支援20M
        :type ZipFile: str
        :param CosBucketRegion: 物件儲存的地域，地域爲 時需要傳入ap-beijing, 一區時需要傳遞ap-beijing-1，其他的地域不需要傳遞。
        :type CosBucketRegion: str
        :param DemoId: 如果是通過Demo創建的話，需要傳入DemoId
        :type DemoId: str
        :param TempCosObjectName: 如果是從TempCos創建的話，需要傳入TempCosObjectName
        :type TempCosObjectName: str
        """
        self.CosBucketName = None
        self.CosObjectName = None
        self.ZipFile = None
        self.CosBucketRegion = None
        self.DemoId = None
        self.TempCosObjectName = None


    def _deserialize(self, params):
        self.CosBucketName = params.get("CosBucketName")
        self.CosObjectName = params.get("CosObjectName")
        self.ZipFile = params.get("ZipFile")
        self.CosBucketRegion = params.get("CosBucketRegion")
        self.DemoId = params.get("DemoId")
        self.TempCosObjectName = params.get("TempCosObjectName")


class CopyFunctionRequest(AbstractModel):
    """CopyFunction請求參數結構體

    """

    def __init__(self):
        """
        :param FunctionName: 函數名
        :type FunctionName: str
        :param NewFunctionName: 新函數的名稱
        :type NewFunctionName: str
        :param Namespace: 命名空間，預設爲default
        :type Namespace: str
        :param TargetNamespace: 将函數複制到的命名空間，預設爲default
        :type TargetNamespace: str
        :param Description: 函數描述
        :type Description: str
        :param TargetRegion: 要将函數複制到的地域，不填則預設爲當前地域
        :type TargetRegion: str
        """
        self.FunctionName = None
        self.NewFunctionName = None
        self.Namespace = None
        self.TargetNamespace = None
        self.Description = None
        self.TargetRegion = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.NewFunctionName = params.get("NewFunctionName")
        self.Namespace = params.get("Namespace")
        self.TargetNamespace = params.get("TargetNamespace")
        self.Description = params.get("Description")
        self.TargetRegion = params.get("TargetRegion")


class CopyFunctionResponse(AbstractModel):
    """CopyFunction返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFunctionRequest(AbstractModel):
    """CreateFunction請求參數結構體

    """

    def __init__(self):
        """
        :param FunctionName: 創建的函數名稱，函數名稱支援26個英文字母大小寫、數字、連接符和下劃線，第一個字元只能以字母開頭，最後一個字元不能爲連接符或者下劃線，名稱長度2-60
        :type FunctionName: str
        :param Code: 函數的代碼. 注意：不能同時指定Cos與ZipFile
        :type Code: :class:`taifucloudcloud.scf.v20180416.models.Code`
        :param Handler: 函數處理方法名稱，名稱格式支援 "文件名稱.方法名稱" 形式，文件名稱和函數名稱之間以"."隔開，文件名稱和函數名稱要求以字母開始和結尾，中間允許插入字母、數字、下劃線和連接符，文件名稱和函數名字的長度要求是 2-60 個字元
        :type Handler: str
        :param Description: 函數描述,最大支援 1000 個英文字母、數字、空格、逗号、換行符和英文句号，支援中文
        :type Description: str
        :param MemorySize: 函數運作時内存大小，預設爲 128M，可選範圍 128MB-1536MB，并且以 128MB 爲階梯
        :type MemorySize: int
        :param Timeout: 函數最長執行時間，單位爲秒，可選值範圍 1-300 秒，預設爲 3 秒
        :type Timeout: int
        :param Environment: 函數的環境變量
        :type Environment: :class:`taifucloudcloud.scf.v20180416.models.Environment`
        :param Runtime: 函數運作環境，目前僅支援 Python2.7，Python3.6，Nodejs6.10， PHP5， PHP7，Golang1 和 Java8，預設Python2.7
        :type Runtime: str
        :param VpcConfig: 函數的私有網絡配置
        :type VpcConfig: :class:`taifucloudcloud.scf.v20180416.models.VpcConfig`
        :param ClsLogsetId: 函數日志投遞到的CLS LogsetID
        :type ClsLogsetId: str
        :param ClsTopicId: 函數日志投遞到的CLS TopicID
        :type ClsTopicId: str
        """
        self.FunctionName = None
        self.Code = None
        self.Handler = None
        self.Description = None
        self.MemorySize = None
        self.Timeout = None
        self.Environment = None
        self.Runtime = None
        self.VpcConfig = None
        self.ClsLogsetId = None
        self.ClsTopicId = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        if params.get("Code") is not None:
            self.Code = Code()
            self.Code._deserialize(params.get("Code"))
        self.Handler = params.get("Handler")
        self.Description = params.get("Description")
        self.MemorySize = params.get("MemorySize")
        self.Timeout = params.get("Timeout")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.Runtime = params.get("Runtime")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")


class CreateFunctionResponse(AbstractModel):
    """CreateFunction返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTriggerRequest(AbstractModel):
    """CreateTrigger請求參數結構體

    """

    def __init__(self):
        """
        :param FunctionName: 新建觸發器綁定的函數名稱
        :type FunctionName: str
        :param TriggerName: 新建觸發器名稱。如果是定時觸發器，名稱支援英文字母、數字、連接符和下劃線，最長100個字元；如果是其他觸發器，見具體觸發器綁定參數的說明
        :type TriggerName: str
        :param Type: 觸發器類型，目前支援 cos 、cmq、 timer、 ckafka類型
        :type Type: str
        :param TriggerDesc: 觸發器對應的參數，如果是 timer 類型的觸發器其内容是 Linux cron 表達式，如果是其他觸發器，見具體觸發器說明
        :type TriggerDesc: str
        :param Qualifier: 函數的版本
        :type Qualifier: str
        :param Enable: 觸發器的初始是能狀态 OPEN表示開啓 CLOSE表示關閉
        :type Enable: str
        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.Qualifier = None
        self.Enable = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Qualifier = params.get("Qualifier")
        self.Enable = params.get("Enable")


class CreateTriggerResponse(AbstractModel):
    """CreateTrigger返回參數結構體

    """

    def __init__(self):
        """
        :param TriggerInfo: 觸發器訊息
        :type TriggerInfo: :class:`taifucloudcloud.scf.v20180416.models.Trigger`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TriggerInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TriggerInfo") is not None:
            self.TriggerInfo = Trigger()
            self.TriggerInfo._deserialize(params.get("TriggerInfo"))
        self.RequestId = params.get("RequestId")


class DeleteFunctionRequest(AbstractModel):
    """DeleteFunction請求參數結構體

    """

    def __init__(self):
        """
        :param FunctionName: 要删除的函數名稱
        :type FunctionName: str
        """
        self.FunctionName = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")


class DeleteFunctionResponse(AbstractModel):
    """DeleteFunction返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTriggerRequest(AbstractModel):
    """DeleteTrigger請求參數結構體

    """

    def __init__(self):
        """
        :param FunctionName: 函數的名稱
        :type FunctionName: str
        :param TriggerName: 要删除的觸發器名稱
        :type TriggerName: str
        :param Type: 要删除的觸發器類型，目前支援 cos 、cmq、 timer、ckafka 類型
        :type Type: str
        :param TriggerDesc: 如果删除的觸發器類型爲 COS 觸發器，該欄位爲必填值，存放 JSON 格式的數據 {"event":"cos:ObjectCreated:*"}，數據内容和 SetTrigger 介面中該欄位的格式相同；如果删除的觸發器類型爲定時觸發器或 CMQ 觸發器，可以不指定該欄位
        :type TriggerDesc: str
        :param Qualifier: 函數的版本訊息
        :type Qualifier: str
        """
        self.FunctionName = None
        self.TriggerName = None
        self.Type = None
        self.TriggerDesc = None
        self.Qualifier = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.TriggerName = params.get("TriggerName")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.Qualifier = params.get("Qualifier")


class DeleteTriggerResponse(AbstractModel):
    """DeleteTrigger返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """函數的環境變量參數

    """

    def __init__(self):
        """
        :param Variables: 環境變量數組
        :type Variables: list of Variable
        """
        self.Variables = None


    def _deserialize(self, params):
        if params.get("Variables") is not None:
            self.Variables = []
            for item in params.get("Variables"):
                obj = Variable()
                obj._deserialize(item)
                self.Variables.append(obj)


class Filter(AbstractModel):
    """描述鍵值對過濾器，用于條件過濾查詢。例如過濾ID、名稱、狀态等
    若存在多個Filter時，Filter間的關系爲邏輯與（AND）關系。
    若同一個Filter存在多個Values，同一Filter下Values間的關系爲邏輯或（OR）關系。

    """

    def __init__(self):
        """
        :param Name: 需要過濾的欄位。
        :type Name: str
        :param Values: 欄位的過濾值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Function(AbstractModel):
    """函數清單

    """

    def __init__(self):
        """
        :param ModTime: 修改時間
        :type ModTime: str
        :param AddTime: 創建時間
        :type AddTime: str
        :param Runtime: 運作時
        :type Runtime: str
        :param FunctionName: 函數名稱
        :type FunctionName: str
        :param FunctionId: 函數ID
        :type FunctionId: str
        :param Namespace: 命名空間
        :type Namespace: str
        :param Status: 函數狀态
        :type Status: str
        :param StatusDesc: 函數狀态詳情
        :type StatusDesc: str
        :param Description: 函數描述
        :type Description: str
        :param Tags: 函數标簽
        :type Tags: list of Tag
        """
        self.ModTime = None
        self.AddTime = None
        self.Runtime = None
        self.FunctionName = None
        self.FunctionId = None
        self.Namespace = None
        self.Status = None
        self.StatusDesc = None
        self.Description = None
        self.Tags = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.AddTime = params.get("AddTime")
        self.Runtime = params.get("Runtime")
        self.FunctionName = params.get("FunctionName")
        self.FunctionId = params.get("FunctionId")
        self.Namespace = params.get("Namespace")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class FunctionLog(AbstractModel):
    """日志訊息

    """

    def __init__(self):
        """
        :param FunctionName: 函數的名稱
        :type FunctionName: str
        :param RetMsg: 函數執行完成後的返回值
        :type RetMsg: str
        :param RequestId: 執行該函數對應的requestId
        :type RequestId: str
        :param StartTime: 函數開始執行時的時間點
        :type StartTime: str
        :param RetCode: 函數執行結果，如果是 0 表示執行成功，其他值表示失敗
        :type RetCode: int
        :param InvokeFinished: 函數調用是否結束，如果是 1 表示執行結束，其他值表示調用異常
        :type InvokeFinished: int
        :param Duration: 函數執行耗時，單位爲 ms
        :type Duration: float
        :param BillDuration: 函數計費時間，根據 duration 向上取最近的 100ms，單位爲ms
        :type BillDuration: int
        :param MemUsage: 函數執行時消耗實際内存大小，單位爲 Byte
        :type MemUsage: int
        :param Log: 函數執行過程中的日志輸出
        :type Log: str
        """
        self.FunctionName = None
        self.RetMsg = None
        self.RequestId = None
        self.StartTime = None
        self.RetCode = None
        self.InvokeFinished = None
        self.Duration = None
        self.BillDuration = None
        self.MemUsage = None
        self.Log = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.RetMsg = params.get("RetMsg")
        self.RequestId = params.get("RequestId")
        self.StartTime = params.get("StartTime")
        self.RetCode = params.get("RetCode")
        self.InvokeFinished = params.get("InvokeFinished")
        self.Duration = params.get("Duration")
        self.BillDuration = params.get("BillDuration")
        self.MemUsage = params.get("MemUsage")
        self.Log = params.get("Log")


class GetFunctionLogsRequest(AbstractModel):
    """GetFunctionLogs請求參數結構體

    """

    def __init__(self):
        """
        :param FunctionName: 函數的名稱
        :type FunctionName: str
        :param Offset: 數據的偏移量，Offset+Limit不能大于10000
        :type Offset: int
        :param Limit: 返回數據的長度，Offset+Limit不能大于10000
        :type Limit: int
        :param Order: 以升序還是降序的方式對日志進行排序，可選值 desc和 asc
        :type Order: str
        :param OrderBy: 根據某個欄位排序日志,支援以下欄位：function_name, duration, mem_usage, start_time
        :type OrderBy: str
        :param Filter: 日志過濾條件。可用來區分正确和錯誤日志，filter.retCode=not0 表示只返回錯誤日志，filter.retCode=is0 表示只返回正确日志，不傳，則返回所有日志
        :type Filter: :class:`taifucloudcloud.scf.v20180416.models.LogFilter`
        :param Qualifier: 函數的版本
        :type Qualifier: str
        :param FunctionRequestId: 執行該函數對應的requestId
        :type FunctionRequestId: str
        :param StartTime: 查詢的具體日期，例如：2017-05-16 20:00:00，只能與endtime相差一天之内
        :type StartTime: str
        :param EndTime: 查詢的具體日期，例如：2017-05-16 20:59:59，只能與startTime相差一天之内
        :type EndTime: str
        """
        self.FunctionName = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderBy = None
        self.Filter = None
        self.Qualifier = None
        self.FunctionRequestId = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self.Filter = LogFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.Qualifier = params.get("Qualifier")
        self.FunctionRequestId = params.get("FunctionRequestId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class GetFunctionLogsResponse(AbstractModel):
    """GetFunctionLogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 函數日志的總數
        :type TotalCount: int
        :param Data: 函數日志訊息
        :type Data: list of FunctionLog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = FunctionLog()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class GetFunctionRequest(AbstractModel):
    """GetFunction請求參數結構體

    """

    def __init__(self):
        """
        :param FunctionName: 需要獲取詳情的函數名稱
        :type FunctionName: str
        :param Qualifier: 函數的版本号
        :type Qualifier: str
        :param ShowCode: 是否顯示代碼, TRUE表示顯示代碼，FALSE表示不顯示代碼,大于1M的入口文件不會顯示
        :type ShowCode: str
        """
        self.FunctionName = None
        self.Qualifier = None
        self.ShowCode = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Qualifier = params.get("Qualifier")
        self.ShowCode = params.get("ShowCode")


class GetFunctionResponse(AbstractModel):
    """GetFunction返回參數結構體

    """

    def __init__(self):
        """
        :param ModTime: 函數的最後修改時間
        :type ModTime: str
        :param CodeInfo: 函數的代碼
        :type CodeInfo: str
        :param Description: 函數的描述訊息
        :type Description: str
        :param Triggers: 函數的觸發器清單
        :type Triggers: list of Trigger
        :param Handler: 函數的入口
        :type Handler: str
        :param CodeSize: 函數代碼大小
        :type CodeSize: int
        :param Timeout: 函數的超時時間
        :type Timeout: int
        :param FunctionVersion: 函數的版本
        :type FunctionVersion: str
        :param MemorySize: 函數的最大可用内存
        :type MemorySize: int
        :param Runtime: 函數的運作環境
        :type Runtime: str
        :param FunctionName: 函數的名稱
        :type FunctionName: str
        :param VpcConfig: 函數的私有網絡
        :type VpcConfig: :class:`taifucloudcloud.scf.v20180416.models.VpcConfig`
        :param UseGpu: 是否使用GPU
        :type UseGpu: str
        :param Environment: 函數的環境變量
        :type Environment: :class:`taifucloudcloud.scf.v20180416.models.Environment`
        :param CodeResult: 代碼是否正确
        :type CodeResult: str
        :param CodeError: 代碼錯誤訊息
        :type CodeError: str
        :param ErrNo: 代碼錯誤碼
        :type ErrNo: int
        :param Namespace: 函數的命名空間
        :type Namespace: str
        :param Role: 函數綁定的角色
        :type Role: str
        :param InstallDependency: 是否自動安裝依賴
        :type InstallDependency: str
        :param Status: 函數狀态
        :type Status: str
        :param StatusDesc: 狀态描述
        :type StatusDesc: str
        :param ClsLogsetId: 日志投遞到的Cls日志集
        :type ClsLogsetId: str
        :param ClsTopicId: 日志投遞到的Cls Topic
        :type ClsTopicId: str
        :param FunctionId: 函數ID
        :type FunctionId: str
        :param Tags: 函數的标簽清單
        :type Tags: list of Tag
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ModTime = None
        self.CodeInfo = None
        self.Description = None
        self.Triggers = None
        self.Handler = None
        self.CodeSize = None
        self.Timeout = None
        self.FunctionVersion = None
        self.MemorySize = None
        self.Runtime = None
        self.FunctionName = None
        self.VpcConfig = None
        self.UseGpu = None
        self.Environment = None
        self.CodeResult = None
        self.CodeError = None
        self.ErrNo = None
        self.Namespace = None
        self.Role = None
        self.InstallDependency = None
        self.Status = None
        self.StatusDesc = None
        self.ClsLogsetId = None
        self.ClsTopicId = None
        self.FunctionId = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.CodeInfo = params.get("CodeInfo")
        self.Description = params.get("Description")
        if params.get("Triggers") is not None:
            self.Triggers = []
            for item in params.get("Triggers"):
                obj = Trigger()
                obj._deserialize(item)
                self.Triggers.append(obj)
        self.Handler = params.get("Handler")
        self.CodeSize = params.get("CodeSize")
        self.Timeout = params.get("Timeout")
        self.FunctionVersion = params.get("FunctionVersion")
        self.MemorySize = params.get("MemorySize")
        self.Runtime = params.get("Runtime")
        self.FunctionName = params.get("FunctionName")
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        self.UseGpu = params.get("UseGpu")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        self.CodeResult = params.get("CodeResult")
        self.CodeError = params.get("CodeError")
        self.ErrNo = params.get("ErrNo")
        self.Namespace = params.get("Namespace")
        self.Role = params.get("Role")
        self.InstallDependency = params.get("InstallDependency")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.ClsLogsetId = params.get("ClsLogsetId")
        self.ClsTopicId = params.get("ClsTopicId")
        self.FunctionId = params.get("FunctionId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class InvokeRequest(AbstractModel):
    """Invoke請求參數結構體

    """

    def __init__(self):
        """
        :param FunctionName: 函數名稱
        :type FunctionName: str
        :param InvocationType: RequestResponse(同步) 和 Event(異步)，預設爲同步
        :type InvocationType: str
        :param Qualifier: 觸發函數的版本号
        :type Qualifier: str
        :param ClientContext: 運作函數時的參數，以json格式傳入，最大支援的參數長度是 1M
        :type ClientContext: str
        :param LogType: 同步調用時指定該欄位，返回值會包含4K的日志，可選值爲None和Tail，預設值爲None。當該值爲Tail時，返回參數中的logMsg欄位會包含對應的函數執行日志
        :type LogType: str
        :param Namespace: 命名空間
        :type Namespace: str
        """
        self.FunctionName = None
        self.InvocationType = None
        self.Qualifier = None
        self.ClientContext = None
        self.LogType = None
        self.Namespace = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.InvocationType = params.get("InvocationType")
        self.Qualifier = params.get("Qualifier")
        self.ClientContext = params.get("ClientContext")
        self.LogType = params.get("LogType")
        self.Namespace = params.get("Namespace")


class InvokeResponse(AbstractModel):
    """Invoke返回參數結構體

    """

    def __init__(self):
        """
        :param Result: 函數執行結果
        :type Result: :class:`taifucloudcloud.scf.v20180416.models.Result`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Result()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ListFunctionsRequest(AbstractModel):
    """ListFunctions請求參數結構體

    """

    def __init__(self):
        """
        :param Order: 以升序還是降序的方式返回結果，可選值 ASC 和 DESC
        :type Order: str
        :param Orderby: 根據哪個欄位進行返回結果排序,支援以下欄位：AddTime, ModTime, FunctionName
        :type Orderby: str
        :param Offset: 數據偏移量，預設值爲 0
        :type Offset: int
        :param Limit: 返回數據長度，預設值爲 20
        :type Limit: int
        :param SearchKey: 支援FunctionName模糊比對
        :type SearchKey: str
        :param Description: 函數描述，支援模糊搜索
        :type Description: str
        :param Filters: 過濾條件。
- tag:tag-key - String - 是否必填：否 - （過濾條件）按照标簽鍵值對進行過濾。 tag-key使用具體的标簽鍵進行替換。

每次請求的Filters的上限爲10，Filter.Values的上限爲5。
        :type Filters: list of Filter
        """
        self.Order = None
        self.Orderby = None
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.Description = None
        self.Filters = None


    def _deserialize(self, params):
        self.Order = params.get("Order")
        self.Orderby = params.get("Orderby")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.Description = params.get("Description")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class ListFunctionsResponse(AbstractModel):
    """ListFunctions返回參數結構體

    """

    def __init__(self):
        """
        :param Functions: 函數清單
        :type Functions: list of Function
        :param TotalCount: 總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Functions = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Functions") is not None:
            self.Functions = []
            for item in params.get("Functions"):
                obj = Function()
                obj._deserialize(item)
                self.Functions.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class LogFilter(AbstractModel):
    """日志過濾條件，用于區分正确與錯誤日志

    """

    def __init__(self):
        """
        :param RetCode: filter.RetCode=not0 表示只返回錯誤日志，filter.RetCode=is0 表示只返回正确日志，無輸入則返回所有日志。
        :type RetCode: str
        """
        self.RetCode = None


    def _deserialize(self, params):
        self.RetCode = params.get("RetCode")


class Result(AbstractModel):
    """運作函數的返回

    """

    def __init__(self):
        """
        :param Log: 表示執行過程中的日志輸出，異步調用返回爲空
        :type Log: str
        :param RetMsg: 表示執行函數的返回，異步調用返回爲空
        :type RetMsg: str
        :param ErrMsg: 表示執行函數的錯誤返回訊息，異步調用返回爲空
        :type ErrMsg: str
        :param MemUsage: 執行函數時的内存大小，單位爲Byte，異步調用返回爲空
        :type MemUsage: int
        :param Duration: 表示執行函數的耗時，單位是毫秒，異步調用返回爲空
        :type Duration: float
        :param BillDuration: 表示函數的計費耗時，單位是毫秒，異步調用返回爲空
        :type BillDuration: int
        :param FunctionRequestId: 此次函數執行的Id
        :type FunctionRequestId: str
        :param InvokeResult: 0爲正确，異步調用返回爲空
        :type InvokeResult: int
        """
        self.Log = None
        self.RetMsg = None
        self.ErrMsg = None
        self.MemUsage = None
        self.Duration = None
        self.BillDuration = None
        self.FunctionRequestId = None
        self.InvokeResult = None


    def _deserialize(self, params):
        self.Log = params.get("Log")
        self.RetMsg = params.get("RetMsg")
        self.ErrMsg = params.get("ErrMsg")
        self.MemUsage = params.get("MemUsage")
        self.Duration = params.get("Duration")
        self.BillDuration = params.get("BillDuration")
        self.FunctionRequestId = params.get("FunctionRequestId")
        self.InvokeResult = params.get("InvokeResult")


class Tag(AbstractModel):
    """函數标簽

    """

    def __init__(self):
        """
        :param Key: 标簽的key
        :type Key: str
        :param Value: 标簽的value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class Trigger(AbstractModel):
    """觸發器類型

    """

    def __init__(self):
        """
        :param ModTime: 觸發器最後修改時間
        :type ModTime: str
        :param Type: 觸發器類型
        :type Type: str
        :param TriggerDesc: 觸發器詳細配置
        :type TriggerDesc: str
        :param TriggerName: 觸發器名稱
        :type TriggerName: str
        :param AddTime: 觸發器創建時間
        :type AddTime: str
        :param Enable: 使能開關
        :type Enable: int
        :param CustomArgument: 客戶自定義參數
        :type CustomArgument: str
        """
        self.ModTime = None
        self.Type = None
        self.TriggerDesc = None
        self.TriggerName = None
        self.AddTime = None
        self.Enable = None
        self.CustomArgument = None


    def _deserialize(self, params):
        self.ModTime = params.get("ModTime")
        self.Type = params.get("Type")
        self.TriggerDesc = params.get("TriggerDesc")
        self.TriggerName = params.get("TriggerName")
        self.AddTime = params.get("AddTime")
        self.Enable = params.get("Enable")
        self.CustomArgument = params.get("CustomArgument")


class UpdateFunctionCodeRequest(AbstractModel):
    """UpdateFunctionCode請求參數結構體

    """

    def __init__(self):
        """
        :param Handler: 函數處理方法名稱。名稱格式支援“文件名稱.函數名稱”形式，文件名稱和函數名稱之間以"."隔開，文件名稱和函數名稱要求以字母開始和結尾，中間允許插入字母、數字、下劃線和連接符，文件名稱和函數名字的長度要求 2-60 個字元
        :type Handler: str
        :param FunctionName: 要修改的函數名稱
        :type FunctionName: str
        :param CosBucketName: 物件儲存桶名稱
        :type CosBucketName: str
        :param CosObjectName: 物件儲存對象路徑
        :type CosObjectName: str
        :param ZipFile: 包含函數代碼文件及其依賴項的 zip 格式文件，使用該介面時要求将 zip 文件的内容轉成 base64 編碼，最大支援20M
        :type ZipFile: str
        :param CosBucketRegion: 物件儲存的地域，注： 分爲ap-beijing和ap-beijing-1
        :type CosBucketRegion: str
        """
        self.Handler = None
        self.FunctionName = None
        self.CosBucketName = None
        self.CosObjectName = None
        self.ZipFile = None
        self.CosBucketRegion = None


    def _deserialize(self, params):
        self.Handler = params.get("Handler")
        self.FunctionName = params.get("FunctionName")
        self.CosBucketName = params.get("CosBucketName")
        self.CosObjectName = params.get("CosObjectName")
        self.ZipFile = params.get("ZipFile")
        self.CosBucketRegion = params.get("CosBucketRegion")


class UpdateFunctionCodeResponse(AbstractModel):
    """UpdateFunctionCode返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateFunctionConfigurationRequest(AbstractModel):
    """UpdateFunctionConfiguration請求參數結構體

    """

    def __init__(self):
        """
        :param FunctionName: 要修改的函數名稱
        :type FunctionName: str
        :param Description: 函數描述。最大支援 1000 個英文字母、數字、空格、逗号和英文句号，支援中文
        :type Description: str
        :param MemorySize: 函數運作時内存大小，預設爲 128 M，可選範 128 M-1536 M
        :type MemorySize: int
        :param Timeout: 函數最長執行時間，單位爲秒，可選值範 1-300 秒，預設爲 3 秒
        :type Timeout: int
        :param Runtime: 函數運作環境，目前僅支援 Python2.7，Python3.6，Nodejs6.10，PHP5， PHP7，Golang1 和 Java8
        :type Runtime: str
        :param Environment: 函數的環境變量
        :type Environment: :class:`taifucloudcloud.scf.v20180416.models.Environment`
        :param VpcConfig: 函數的私有網絡配置
        :type VpcConfig: :class:`taifucloudcloud.scf.v20180416.models.VpcConfig`
        """
        self.FunctionName = None
        self.Description = None
        self.MemorySize = None
        self.Timeout = None
        self.Runtime = None
        self.Environment = None
        self.VpcConfig = None


    def _deserialize(self, params):
        self.FunctionName = params.get("FunctionName")
        self.Description = params.get("Description")
        self.MemorySize = params.get("MemorySize")
        self.Timeout = params.get("Timeout")
        self.Runtime = params.get("Runtime")
        if params.get("Environment") is not None:
            self.Environment = Environment()
            self.Environment._deserialize(params.get("Environment"))
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))


class UpdateFunctionConfigurationResponse(AbstractModel):
    """UpdateFunctionConfiguration返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Variable(AbstractModel):
    """變量參數

    """

    def __init__(self):
        """
        :param Key: 變量的名稱
        :type Key: str
        :param Value: 變量的值
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class VpcConfig(AbstractModel):
    """私有網絡參數配置

    """

    def __init__(self):
        """
        :param VpcId: 私有網絡 的 id
        :type VpcId: str
        :param SubnetId: 子網的 id
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")