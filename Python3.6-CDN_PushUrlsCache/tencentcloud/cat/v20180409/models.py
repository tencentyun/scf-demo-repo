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


class AgentGroup(AbstractModel):
    """撥測分組

    """

    def __init__(self):
        """
        :param GroupId: 撥測分組ID
        :type GroupId: int
        :param GroupName: 撥測分組名稱
        :type GroupName: str
        :param IsDefault: 是否預設撥測分組。1表示是，0表示否
        :type IsDefault: int
        :param TaskNum: 使用本撥測分組的任務數
        :type TaskNum: int
        :param GroupDetail: 撥測結點清單
        :type GroupDetail: list of CatAgent
        :param MaxGroupNum: 最大撥測分組數
        :type MaxGroupNum: int
        """
        self.GroupId = None
        self.GroupName = None
        self.IsDefault = None
        self.TaskNum = None
        self.GroupDetail = None
        self.MaxGroupNum = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.IsDefault = params.get("IsDefault")
        self.TaskNum = params.get("TaskNum")
        if params.get("GroupDetail") is not None:
            self.GroupDetail = []
            for item in params.get("GroupDetail"):
                obj = CatAgent()
                obj._deserialize(item)
                self.GroupDetail.append(obj)
        self.MaxGroupNum = params.get("MaxGroupNum")


class AlarmInfo(AbstractModel):
    """撥測告警訊息

    """

    def __init__(self):
        """
        :param ObjName: 告警對象的名稱
        :type ObjName: str
        :param FirstOccurTime: 告警發生的時間
        :type FirstOccurTime: str
        :param LastOccurTime: 告警結束的時間
        :type LastOccurTime: str
        :param Status: 告警狀态。1 表示已恢複，0 表示未恢複，2表示數據不足
        :type Status: int
        :param Content: 告警的内容
        :type Content: str
        :param TaskId: 撥測任務ID
        :type TaskId: int
        :param MetricName: 特征項名字
        :type MetricName: str
        :param MetricValue: 特征項數值
        :type MetricValue: str
        :param ObjId: 告警對象的ID
        :type ObjId: str
        """
        self.ObjName = None
        self.FirstOccurTime = None
        self.LastOccurTime = None
        self.Status = None
        self.Content = None
        self.TaskId = None
        self.MetricName = None
        self.MetricValue = None
        self.ObjId = None


    def _deserialize(self, params):
        self.ObjName = params.get("ObjName")
        self.FirstOccurTime = params.get("FirstOccurTime")
        self.LastOccurTime = params.get("LastOccurTime")
        self.Status = params.get("Status")
        self.Content = params.get("Content")
        self.TaskId = params.get("TaskId")
        self.MetricName = params.get("MetricName")
        self.MetricValue = params.get("MetricValue")
        self.ObjId = params.get("ObjId")


class AlarmTopic(AbstractModel):
    """告警主題

    """

    def __init__(self):
        """
        :param TopicId: 主題的ID
        :type TopicId: str
        :param TopicName: 主題的名稱
        :type TopicName: str
        """
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")


class BindAlarmPolicyRequest(AbstractModel):
    """BindAlarmPolicy請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 撥測任務Id
        :type TaskId: int
        :param PolicyGroupId: 告警策略組Id
        :type PolicyGroupId: int
        :param IfBind: 是否綁定操作。非0 爲綁定， 0 爲 解綁。缺省表示 綁定。
        :type IfBind: int
        :param TopicId: 告警主題Id
        :type TopicId: str
        """
        self.TaskId = None
        self.PolicyGroupId = None
        self.IfBind = None
        self.TopicId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.PolicyGroupId = params.get("PolicyGroupId")
        self.IfBind = params.get("IfBind")
        self.TopicId = params.get("TopicId")


class BindAlarmPolicyResponse(AbstractModel):
    """BindAlarmPolicy返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CatAgent(AbstractModel):
    """撥測Agent 所在 、運營商

    """

    def __init__(self):
        """
        :param Province: 撥測結點所在的 （拼音縮寫）
        :type Province: str
        :param Isp: 撥測結點所在的運營商（英文縮寫）
        :type Isp: str
        :param ProvinceName: 撥測結點所在的 （中文名稱）
注意：此欄位可能返回 null，表示取不到有效值。
        :type ProvinceName: str
        :param IspName: 撥測結點所在的運營商（中文名稱）
注意：此欄位可能返回 null，表示取不到有效值。
        :type IspName: str
        """
        self.Province = None
        self.Isp = None
        self.ProvinceName = None
        self.IspName = None


    def _deserialize(self, params):
        self.Province = params.get("Province")
        self.Isp = params.get("Isp")
        self.ProvinceName = params.get("ProvinceName")
        self.IspName = params.get("IspName")


class CatLog(AbstractModel):
    """撥測記錄

    """

    def __init__(self):
        """
        :param Time: 撥測時間點
        :type Time: str
        :param CatTypeName: 撥測類型
        :type CatTypeName: str
        :param TaskId: 任務ID
        :type TaskId: int
        :param City: 撥測點所在城市
        :type City: str
        :param Isp: 撥測點所在運營商
        :type Isp: str
        :param ServerIp: 被撥測Server的IP
        :type ServerIp: str
        :param DomainName: 被撥測Server的域名
        :type DomainName: str
        :param TotalTime: 執行耗時，單位毫秒
        :type TotalTime: int
        :param ResultType: 成功失敗(1 失敗，0 成功）
        :type ResultType: int
        :param ResultCode: 失敗錯誤碼
        :type ResultCode: int
        :param ReqPkgSize: 請求包大小
        :type ReqPkgSize: int
        :param RspPkgSize: 回應包大小
        :type RspPkgSize: int
        :param ReqMsg: 撥測請求
        :type ReqMsg: str
        :param RespMsg: 撥測回應
        :type RespMsg: str
        :param ClientIp: 用戶端IP
        :type ClientIp: str
        :param CityName: 撥測點所在城市名稱
        :type CityName: str
        :param IspName: 撥測點所在運營商名稱
        :type IspName: str
        :param ParseTime: 解析耗時，單位毫秒
        :type ParseTime: int
        :param ConnectTime: 連接耗時，單位毫秒
        :type ConnectTime: int
        :param SendTime: 數據發送耗時，單位毫秒
        :type SendTime: int
        :param WaitTime: 等待耗時，單位毫秒
        :type WaitTime: int
        :param ReceiveTime: 接收耗時，單位毫秒
        :type ReceiveTime: int
        """
        self.Time = None
        self.CatTypeName = None
        self.TaskId = None
        self.City = None
        self.Isp = None
        self.ServerIp = None
        self.DomainName = None
        self.TotalTime = None
        self.ResultType = None
        self.ResultCode = None
        self.ReqPkgSize = None
        self.RspPkgSize = None
        self.ReqMsg = None
        self.RespMsg = None
        self.ClientIp = None
        self.CityName = None
        self.IspName = None
        self.ParseTime = None
        self.ConnectTime = None
        self.SendTime = None
        self.WaitTime = None
        self.ReceiveTime = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.CatTypeName = params.get("CatTypeName")
        self.TaskId = params.get("TaskId")
        self.City = params.get("City")
        self.Isp = params.get("Isp")
        self.ServerIp = params.get("ServerIp")
        self.DomainName = params.get("DomainName")
        self.TotalTime = params.get("TotalTime")
        self.ResultType = params.get("ResultType")
        self.ResultCode = params.get("ResultCode")
        self.ReqPkgSize = params.get("ReqPkgSize")
        self.RspPkgSize = params.get("RspPkgSize")
        self.ReqMsg = params.get("ReqMsg")
        self.RespMsg = params.get("RespMsg")
        self.ClientIp = params.get("ClientIp")
        self.CityName = params.get("CityName")
        self.IspName = params.get("IspName")
        self.ParseTime = params.get("ParseTime")
        self.ConnectTime = params.get("ConnectTime")
        self.SendTime = params.get("SendTime")
        self.WaitTime = params.get("WaitTime")
        self.ReceiveTime = params.get("ReceiveTime")


class CatReturnDetail(AbstractModel):
    """撥測失敗詳情

    """

    def __init__(self):
        """
        :param IspName: 運營商名稱
        :type IspName: str
        :param Province:  全拼
        :type Province: str
        :param ProvinceName:  中文名稱
        :type ProvinceName: str
        :param MapKey: Map鍵值
        :type MapKey: str
        :param ServerIp: 撥測目标的IP
        :type ServerIp: str
        :param ResultCount: 撥測失敗個數
        :type ResultCount: int
        :param ResultCode: 撥測失敗返回碼
        :type ResultCode: int
        :param ErrorReason: 撥測失敗原因描述
        :type ErrorReason: str
        """
        self.IspName = None
        self.Province = None
        self.ProvinceName = None
        self.MapKey = None
        self.ServerIp = None
        self.ResultCount = None
        self.ResultCode = None
        self.ErrorReason = None


    def _deserialize(self, params):
        self.IspName = params.get("IspName")
        self.Province = params.get("Province")
        self.ProvinceName = params.get("ProvinceName")
        self.MapKey = params.get("MapKey")
        self.ServerIp = params.get("ServerIp")
        self.ResultCount = params.get("ResultCount")
        self.ResultCode = params.get("ResultCode")
        self.ErrorReason = params.get("ErrorReason")


class CatReturnSummary(AbstractModel):
    """撥測失敗返回情況匯總

    """

    def __init__(self):
        """
        :param ResultCount: 撥測失敗個數
        :type ResultCount: int
        :param ResultCode: 撥測失敗返回碼
        :type ResultCode: int
        :param ErrorReason: 撥測失敗原因描述
        :type ErrorReason: str
        """
        self.ResultCount = None
        self.ResultCode = None
        self.ErrorReason = None


    def _deserialize(self, params):
        self.ResultCount = params.get("ResultCount")
        self.ResultCode = params.get("ResultCode")
        self.ErrorReason = params.get("ErrorReason")


class CatTaskDetail(AbstractModel):
    """任務訊息和告警策略組

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param TaskName: 任務名稱
        :type TaskName: str
        :param Period: 任務週期，單位爲分鍾。目前支援1，5，15，30幾種取值
        :type Period: int
        :param CatTypeName: 撥測類型。http, https, ping, tcp 之一
        :type CatTypeName: str
        :param CgiUrl: 撥測任務的URL
        :type CgiUrl: str
        :param AgentGroupId: 撥測分組ID
        :type AgentGroupId: int
        :param PolicyGroupId: 告警策略組ID
        :type PolicyGroupId: int
        :param Status: 任務狀态。1表示暫停，2表示運作中，0爲初始态
        :type Status: int
        :param AddTime: 任務創建時間
        :type AddTime: str
        :param Type: 任務類型。0 站點監控，2 可用性監控
        :type Type: int
        :param TopicId: 綁定的統一告警主題ID
        :type TopicId: str
        :param AlarmStatus: 告警狀态。0 未啓用，1, 啓用
        :type AlarmStatus: int
        :param Host: 指定的域名
        :type Host: str
        :param Port: 撥測目标的端口号
        :type Port: int
        :param CheckStr: 要在結果中進行比對的字串
        :type CheckStr: str
        :param CheckType: 1 表示通過檢查結果是否包含CheckStr 進行校驗
        :type CheckType: int
        :param UserAgent: 用戶Agent訊息
        :type UserAgent: str
        :param Cookie: 設置的Cookie訊息
        :type Cookie: str
        :param PostData: POST 請求數據。空字串表示非POST請求
        :type PostData: str
        :param SslVer: SSL協議版本
        :type SslVer: str
        :param IsHeader: 是否爲Header請求。非0 Header 請求
        :type IsHeader: int
        :param DnsSvr: 目的DNS服務器
        :type DnsSvr: str
        :param DnsCheckIp: 需要檢驗是否在DNS IP清單的IP
        :type DnsCheckIp: str
        :param DnsQueryType: DNS查詢類型
        :type DnsQueryType: str
        :param UserName: 登入服務器的賬号
        :type UserName: str
        :param PassWord: 登入服務器的密碼
        :type PassWord: str
        :param UseSecConn: 是否使用安全連結SSL， 0 不使用，1 使用
        :type UseSecConn: int
        :param NeedAuth: FTP登入驗證方式  0 不驗證  1 匿名登入  2 需要身份驗證
        :type NeedAuth: int
        :param ReqDataType: 請求數據類型。0 表示請求爲字串類型。1表示爲二進制類型
        :type ReqDataType: int
        :param ReqData: 發起TCP, UDP請求的協議請求數據
        :type ReqData: str
        :param RespDataType: 響應數據類型。0 表示響應爲字串類型。1表示爲二進制類型
        :type RespDataType: int
        :param RespData: 預期的UDP請求的回應數據
        :type RespData: str
        :param RedirectFollowNum: 跟随跳轉次數
        :type RedirectFollowNum: int
        """
        self.TaskId = None
        self.TaskName = None
        self.Period = None
        self.CatTypeName = None
        self.CgiUrl = None
        self.AgentGroupId = None
        self.PolicyGroupId = None
        self.Status = None
        self.AddTime = None
        self.Type = None
        self.TopicId = None
        self.AlarmStatus = None
        self.Host = None
        self.Port = None
        self.CheckStr = None
        self.CheckType = None
        self.UserAgent = None
        self.Cookie = None
        self.PostData = None
        self.SslVer = None
        self.IsHeader = None
        self.DnsSvr = None
        self.DnsCheckIp = None
        self.DnsQueryType = None
        self.UserName = None
        self.PassWord = None
        self.UseSecConn = None
        self.NeedAuth = None
        self.ReqDataType = None
        self.ReqData = None
        self.RespDataType = None
        self.RespData = None
        self.RedirectFollowNum = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.Period = params.get("Period")
        self.CatTypeName = params.get("CatTypeName")
        self.CgiUrl = params.get("CgiUrl")
        self.AgentGroupId = params.get("AgentGroupId")
        self.PolicyGroupId = params.get("PolicyGroupId")
        self.Status = params.get("Status")
        self.AddTime = params.get("AddTime")
        self.Type = params.get("Type")
        self.TopicId = params.get("TopicId")
        self.AlarmStatus = params.get("AlarmStatus")
        self.Host = params.get("Host")
        self.Port = params.get("Port")
        self.CheckStr = params.get("CheckStr")
        self.CheckType = params.get("CheckType")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")
        self.PostData = params.get("PostData")
        self.SslVer = params.get("SslVer")
        self.IsHeader = params.get("IsHeader")
        self.DnsSvr = params.get("DnsSvr")
        self.DnsCheckIp = params.get("DnsCheckIp")
        self.DnsQueryType = params.get("DnsQueryType")
        self.UserName = params.get("UserName")
        self.PassWord = params.get("PassWord")
        self.UseSecConn = params.get("UseSecConn")
        self.NeedAuth = params.get("NeedAuth")
        self.ReqDataType = params.get("ReqDataType")
        self.ReqData = params.get("ReqData")
        self.RespDataType = params.get("RespDataType")
        self.RespData = params.get("RespData")
        self.RedirectFollowNum = params.get("RedirectFollowNum")


class CreateAgentGroupRequest(AbstractModel):
    """CreateAgentGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupName: 撥測分組名稱，不超過32個字元
        :type GroupName: str
        :param IsDefault: 是否爲預設分組，取值可爲 0 或 1。取 1 時表示設置爲預設分組
        :type IsDefault: int
        :param Agents: Province, Isp 需要成對地進行選擇。參數對的取值範圍。參見：DescribeAgents 的返回結果。
        :type Agents: list of CatAgent
        """
        self.GroupName = None
        self.IsDefault = None
        self.Agents = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.IsDefault = params.get("IsDefault")
        if params.get("Agents") is not None:
            self.Agents = []
            for item in params.get("Agents"):
                obj = CatAgent()
                obj._deserialize(item)
                self.Agents.append(obj)


class CreateAgentGroupResponse(AbstractModel):
    """CreateAgentGroup返回參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 撥測分組Id
        :type GroupId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateTaskExRequest(AbstractModel):
    """CreateTaskEx請求參數結構體

    """

    def __init__(self):
        """
        :param CatTypeName: http, https, ping, tcp, ftp, smtp, udp, dns 之一
        :type CatTypeName: str
        :param Url: 撥測的URL， 例如：www.qq.com (URL域名解析需要能解析出具體的IP)
        :type Url: str
        :param Period: 撥測週期。取值可爲1,5,15,30之一, 單位：分鍾。精度不能低于用戶等級規定的最小精度
        :type Period: int
        :param TaskName: 撥測任務名稱不能超過32個字元。同一個用戶創建的任務名不可重複
        :type TaskName: str
        :param AgentGroupId: 撥測分組ID，體現本撥測任務要采用哪些運營商作爲撥測源。一般可直接填寫本用戶的預設撥測分組。參見：DescribeAgentGroups 介面，本參數使用返回結果裏的GroupId的值。注意： Type爲0時，AgentGroupId爲必填
        :type AgentGroupId: int
        :param Host: 指定域名(如需要)
        :type Host: str
        :param IsHeader: 是否爲Header請求（非0 發起Header 請求。爲0，且PostData 非空，發起POST請求。爲0，PostData 爲空，發起GET請求）
        :type IsHeader: int
        :param SslVer: URL中含有"https"時有用。缺省爲SSLv23。需要爲 TLSv1_2, TLSv1_1, TLSv1, SSLv2, SSLv23, SSLv3 之一
        :type SslVer: str
        :param PostData: POST請求數據。空字串表示非POST請求
        :type PostData: str
        :param UserAgent: 用戶Agent訊息
        :type UserAgent: str
        :param CheckStr: 要在結果中進行比對的字串
        :type CheckStr: str
        :param CheckType: 1 表示通過檢查結果是否包含CheckStr 進行校驗
        :type CheckType: int
        :param Cookie: 需要設置的Cookie訊息
        :type Cookie: str
        :param TaskId: 任務ID，用于驗證且修改任務時傳入原任務ID
        :type TaskId: int
        :param UserName: 登入服務器的賬号。如果爲空字串，表示不用校驗用戶密碼。只做簡單連接服務器的撥測
        :type UserName: str
        :param PassWord: 登入服務器的密碼
        :type PassWord: str
        :param ReqDataType: 缺省爲0。0 表示請求爲字串類型。1表示爲二進制類型
        :type ReqDataType: int
        :param ReqData: 發起TCP, UDP請求的協議請求數據
        :type ReqData: str
        :param RespDataType: 缺省爲0。0 表示響應爲字串類型。1表示爲二進制類型
        :type RespDataType: int
        :param RespData: 預期的UDP請求的回應數據。字串型，只需要返回的結果裏包含本字串算校驗通過。二進制型，則需要嚴格等于才算通過
        :type RespData: str
        :param DnsSvr: 目的DNS服務器  可以爲空字串
        :type DnsSvr: str
        :param DnsCheckIp: 需要檢驗是否在DNS IP清單的IP。可以爲空字串，表示不校驗
        :type DnsCheckIp: str
        :param DnsQueryType: 需要爲下列值之一。缺省爲A。A, MX, NS, CNAME, TXT, ANY
        :type DnsQueryType: str
        :param UseSecConn: 是否使用安全連結SSL， 0 不使用，1 使用
        :type UseSecConn: int
        :param NeedAuth: FTP登入驗證方式， 0 不驗證 ， 1 匿名登入， 2 需要身份驗證
        :type NeedAuth: int
        :param Port: 撥測目标的端口号
        :type Port: int
        :param Type: Type=0 預設 （站點監控）Type=2 可用率監控
        :type Type: int
        :param IsVerify: IsVerify=0 非驗證任務 IsVerify=1 驗證任務，不傳則預設爲0
        :type IsVerify: int
        :param RedirectFollowNum: 跟随跳轉次數，取值範圍0-5，不傳則表示不跟随
        :type RedirectFollowNum: int
        """
        self.CatTypeName = None
        self.Url = None
        self.Period = None
        self.TaskName = None
        self.AgentGroupId = None
        self.Host = None
        self.IsHeader = None
        self.SslVer = None
        self.PostData = None
        self.UserAgent = None
        self.CheckStr = None
        self.CheckType = None
        self.Cookie = None
        self.TaskId = None
        self.UserName = None
        self.PassWord = None
        self.ReqDataType = None
        self.ReqData = None
        self.RespDataType = None
        self.RespData = None
        self.DnsSvr = None
        self.DnsCheckIp = None
        self.DnsQueryType = None
        self.UseSecConn = None
        self.NeedAuth = None
        self.Port = None
        self.Type = None
        self.IsVerify = None
        self.RedirectFollowNum = None


    def _deserialize(self, params):
        self.CatTypeName = params.get("CatTypeName")
        self.Url = params.get("Url")
        self.Period = params.get("Period")
        self.TaskName = params.get("TaskName")
        self.AgentGroupId = params.get("AgentGroupId")
        self.Host = params.get("Host")
        self.IsHeader = params.get("IsHeader")
        self.SslVer = params.get("SslVer")
        self.PostData = params.get("PostData")
        self.UserAgent = params.get("UserAgent")
        self.CheckStr = params.get("CheckStr")
        self.CheckType = params.get("CheckType")
        self.Cookie = params.get("Cookie")
        self.TaskId = params.get("TaskId")
        self.UserName = params.get("UserName")
        self.PassWord = params.get("PassWord")
        self.ReqDataType = params.get("ReqDataType")
        self.ReqData = params.get("ReqData")
        self.RespDataType = params.get("RespDataType")
        self.RespData = params.get("RespData")
        self.DnsSvr = params.get("DnsSvr")
        self.DnsCheckIp = params.get("DnsCheckIp")
        self.DnsQueryType = params.get("DnsQueryType")
        self.UseSecConn = params.get("UseSecConn")
        self.NeedAuth = params.get("NeedAuth")
        self.Port = params.get("Port")
        self.Type = params.get("Type")
        self.IsVerify = params.get("IsVerify")
        self.RedirectFollowNum = params.get("RedirectFollowNum")


class CreateTaskExResponse(AbstractModel):
    """CreateTaskEx返回參數結構體

    """

    def __init__(self):
        """
        :param ResultId: 撥測結果查詢ID。接下來可以使用查詢撥測是否能夠成功，驗證能否通過。
        :type ResultId: int
        :param TaskId: 撥測任務ID。驗證通過後，創建任務時使用，傳遞給CreateTask 介面。
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResultId = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResultId = params.get("ResultId")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DataPoint(AbstractModel):
    """延遲等數據，數據點

    """

    def __init__(self):
        """
        :param LogTime: 數據點的時間
        :type LogTime: str
        :param MetricValue: 數據值
        :type MetricValue: float
        """
        self.LogTime = None
        self.MetricValue = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.MetricValue = params.get("MetricValue")


class DataPointMetric(AbstractModel):
    """包含MetricName的DataPoint數據

    """

    def __init__(self):
        """
        :param MetricName: 數據項
        :type MetricName: str
        :param Points: 數據點的時間和值
        :type Points: list of DataPoint
        """
        self.MetricName = None
        self.Points = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        if params.get("Points") is not None:
            self.Points = []
            for item in params.get("Points"):
                obj = DataPoint()
                obj._deserialize(item)
                self.Points.append(obj)


class DeleteAgentGroupRequest(AbstractModel):
    """DeleteAgentGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 撥測分組id
        :type GroupId: int
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")


class DeleteAgentGroupResponse(AbstractModel):
    """DeleteAgentGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTasksRequest(AbstractModel):
    """DeleteTasks請求參數結構體

    """

    def __init__(self):
        """
        :param TaskIds: 撥測任務id
        :type TaskIds: list of int non-negative
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")


class DeleteTasksResponse(AbstractModel):
    """DeleteTasks返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAgentGroupsRequest(AbstractModel):
    """DescribeAgentGroups請求參數結構體

    """


class DescribeAgentGroupsResponse(AbstractModel):
    """DescribeAgentGroups返回參數結構體

    """

    def __init__(self):
        """
        :param SysDefaultGroup: 用戶所屬的系統預設撥測分組
        :type SysDefaultGroup: :class:`taifucloudcloud.cat.v20180409.models.AgentGroup`
        :param CustomGroups: 用戶創建的撥測分組清單
        :type CustomGroups: list of AgentGroup
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SysDefaultGroup = None
        self.CustomGroups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SysDefaultGroup") is not None:
            self.SysDefaultGroup = AgentGroup()
            self.SysDefaultGroup._deserialize(params.get("SysDefaultGroup"))
        if params.get("CustomGroups") is not None:
            self.CustomGroups = []
            for item in params.get("CustomGroups"):
                obj = AgentGroup()
                obj._deserialize(item)
                self.CustomGroups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAgentsRequest(AbstractModel):
    """DescribeAgents請求參數結構體

    """


class DescribeAgentsResponse(AbstractModel):
    """DescribeAgents返回參數結構體

    """

    def __init__(self):
        """
        :param Agents: 本用戶可選的撥測點清單
        :type Agents: list of CatAgent
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Agents = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Agents") is not None:
            self.Agents = []
            for item in params.get("Agents"):
                obj = CatAgent()
                obj._deserialize(item)
                self.Agents.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmTopicRequest(AbstractModel):
    """DescribeAlarmTopic請求參數結構體

    """

    def __init__(self):
        """
        :param NeedAdd: 如果不存在撥測相關的主題，是否自動創建一個。取值可爲0, 1，預設爲0
        :type NeedAdd: int
        """
        self.NeedAdd = None


    def _deserialize(self, params):
        self.NeedAdd = params.get("NeedAdd")


class DescribeAlarmTopicResponse(AbstractModel):
    """DescribeAlarmTopic返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 主題個數
        :type TotalCount: int
        :param Topics: 主題清單
        :type Topics: list of AlarmTopic
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Topics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = AlarmTopic()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAlarmsByTaskRequest(AbstractModel):
    """DescribeAlarmsByTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 撥測任務Id
        :type TaskId: int
        :param Offset: 從第Offset 條開始查詢。缺省值爲0
        :type Offset: int
        :param Limit: 本批次查詢Limit 條記錄。缺省值爲20
        :type Limit: int
        :param Status: 0 全部, 1 已恢複, 2 未恢複  預設爲0。其他值，視爲0 查全部狀态
        :type Status: int
        :param BeginTime: 格式如：2017-05-09 00:00:00  缺省爲7天前0點
        :type BeginTime: str
        :param EndTime: 格式如：2017-05-10 00:00:00  缺省爲明天0點
        :type EndTime: str
        :param SortBy: 排序欄位，可爲Time, ObjName, Duration, Status, Content 之一。缺省爲Time
        :type SortBy: str
        :param SortType: 升序或降序。可爲Desc, Asc之一。缺省爲Desc
        :type SortType: str
        :param ObjName: 告警對象的名稱
        :type ObjName: str
        """
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.BeginTime = None
        self.EndTime = None
        self.SortBy = None
        self.SortType = None
        self.ObjName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.SortBy = params.get("SortBy")
        self.SortType = params.get("SortType")
        self.ObjName = params.get("ObjName")


class DescribeAlarmsByTaskResponse(AbstractModel):
    """DescribeAlarmsByTask返回參數結構體

    """

    def __init__(self):
        """
        :param AlarmInfos: 告警訊息清單
        :type AlarmInfos: list of AlarmInfo
        :param FaultRatio: 故障率
        :type FaultRatio: float
        :param FaultTimeSpec: 故障總時長
        :type FaultTimeSpec: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AlarmInfos = None
        self.FaultRatio = None
        self.FaultTimeSpec = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlarmInfos") is not None:
            self.AlarmInfos = []
            for item in params.get("AlarmInfos"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self.AlarmInfos.append(obj)
        self.FaultRatio = params.get("FaultRatio")
        self.FaultTimeSpec = params.get("FaultTimeSpec")
        self.RequestId = params.get("RequestId")


class DescribeAlarmsRequest(AbstractModel):
    """DescribeAlarms請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 從第Offset 條開始查詢。缺省值爲0
        :type Offset: int
        :param Limit: 本批次查詢Limit 條記錄。缺省值爲20
        :type Limit: int
        :param Status: 0 全部, 1 已恢複, 2 未恢複  預設爲0。其他值，視爲0 查全部狀态。
        :type Status: int
        :param BeginTime: 格式如：2017-05-09 00:00:00  缺省爲7天前0點
        :type BeginTime: str
        :param EndTime: 格式如：2017-05-10 00:00:00  缺省爲明天0點
        :type EndTime: str
        :param ObjName: 告警任務名
        :type ObjName: str
        :param SortBy: 排序欄位，可爲Time, ObjName, Duration, Status, Content 之一。缺省爲Time。
        :type SortBy: str
        :param SortType: 升序或降序。可爲Desc, Asc之一。缺省爲Desc。
        :type SortType: str
        """
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.BeginTime = None
        self.EndTime = None
        self.ObjName = None
        self.SortBy = None
        self.SortType = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.ObjName = params.get("ObjName")
        self.SortBy = params.get("SortBy")
        self.SortType = params.get("SortType")


class DescribeAlarmsResponse(AbstractModel):
    """DescribeAlarms返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 告警總條數
        :type TotalCount: int
        :param AlarmInfos: 本批告警訊息清單
        :type AlarmInfos: list of AlarmInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AlarmInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AlarmInfos") is not None:
            self.AlarmInfos = []
            for item in params.get("AlarmInfos"):
                obj = AlarmInfo()
                obj._deserialize(item)
                self.AlarmInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCatLogsRequest(AbstractModel):
    """DescribeCatLogs請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 撥測任務Id
        :type TaskId: int
        :param Offset: 從第Offset 條開始查詢。缺省值爲0
        :type Offset: int
        :param Limit: 本批次查詢Limit 條記錄。缺省值爲20
        :type Limit: int
        :param BeginTime: 格式如：2017-05-09 00:00:00  缺省爲當天0點，最多拉取1天的數據
        :type BeginTime: str
        :param EndTime: 格式如：2017-05-10 00:00:00  缺省爲當前時間
        :type EndTime: str
        :param SortType: 按時間升序或降序。預設降序。可選值： Desc, Asc
        :type SortType: str
        """
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.BeginTime = None
        self.EndTime = None
        self.SortType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.SortType = params.get("SortType")


class DescribeCatLogsResponse(AbstractModel):
    """DescribeCatLogs返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的總記錄數
        :type TotalCount: int
        :param CatLogs: 撥測記錄清單
        :type CatLogs: list of CatLog
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CatLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CatLogs") is not None:
            self.CatLogs = []
            for item in params.get("CatLogs"):
                obj = CatLog()
                obj._deserialize(item)
                self.CatLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail請求參數結構體

    """

    def __init__(self):
        """
        :param TaskIds: 撥測任務id 數組
        :type TaskIds: list of int non-negative
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回參數結構體

    """

    def __init__(self):
        """
        :param Tasks: 撥測任務清單
        :type Tasks: list of CatTaskDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = CatTaskDetail()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTasksByTypeRequest(AbstractModel):
    """DescribeTasksByType請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 從第Offset 條開始查詢。缺省值爲0
        :type Offset: int
        :param Limit: 本批次查詢Limit 條記錄。缺省值爲20
        :type Limit: int
        :param Type: 撥測任務類型。0 站點監控，2 可用性監控。缺省值爲2
        :type Type: int
        """
        self.Offset = None
        self.Limit = None
        self.Type = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")


class DescribeTasksByTypeResponse(AbstractModel):
    """DescribeTasksByType返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 符合條件的總任務數
        :type TotalCount: int
        :param Tasks: 任務清單
        :type Tasks: list of TaskAlarm
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskAlarm()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserLimitRequest(AbstractModel):
    """DescribeUserLimit請求參數結構體

    """


class DescribeUserLimitResponse(AbstractModel):
    """DescribeUserLimit返回參數結構體

    """

    def __init__(self):
        """
        :param MaxTaskNum: 用戶可建立的最大任務數
        :type MaxTaskNum: int
        :param MaxAgentNum: 用戶可用的最大撥測結點數
        :type MaxAgentNum: int
        :param MaxGroupNum: 用戶可建立的最大撥測分組數
        :type MaxGroupNum: int
        :param MinPeriod: 用戶可用的最小撥測間隔
        :type MinPeriod: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.MaxTaskNum = None
        self.MaxAgentNum = None
        self.MaxGroupNum = None
        self.MinPeriod = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaxTaskNum = params.get("MaxTaskNum")
        self.MaxAgentNum = params.get("MaxAgentNum")
        self.MaxGroupNum = params.get("MaxGroupNum")
        self.MinPeriod = params.get("MinPeriod")
        self.RequestId = params.get("RequestId")


class DimensionsDetail(AbstractModel):
    """撥測點維度訊息

    """

    def __init__(self):
        """
        :param Isp: 運營商清單
        :type Isp: list of str
        :param Province:  清單
        :type Province: list of str
        """
        self.Isp = None
        self.Province = None


    def _deserialize(self, params):
        self.Isp = params.get("Isp")
        self.Province = params.get("Province")


class GetAvailRatioHistoryRequest(AbstractModel):
    """GetAvailRatioHistory請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 撥測任務Id
        :type TaskId: int
        :param TimeStamp: 具體時間點
        :type TimeStamp: str
        """
        self.TaskId = None
        self.TimeStamp = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TimeStamp = params.get("TimeStamp")


class GetAvailRatioHistoryResponse(AbstractModel):
    """GetAvailRatioHistory返回參數結構體

    """

    def __init__(self):
        """
        :param AvgAvailRatio: 整體平均可用率
        :type AvgAvailRatio: float
        :param LowestAvailRatio: 各 最低可用率
        :type LowestAvailRatio: float
        :param LowestProvince: 可用率最低的 
        :type LowestProvince: str
        :param LowestIsp: 可用率最低的運營商
        :type LowestIsp: str
        :param ProvinceData: 分 的可用率數據
        :type ProvinceData: list of ProvinceDetail
        :param AvgTime: 國内平均耗時，單位毫秒
        :type AvgTime: float
        :param AvgAvailRatio2: 國外平均可用率
        :type AvgAvailRatio2: float
        :param AvgTime2: 國外平均耗時，單位毫秒
        :type AvgTime2: float
        :param LowestAvailRatio2: 國外最低可用率
        :type LowestAvailRatio2: float
        :param LowestProvince2: 國外可用率最低的區域
        :type LowestProvince2: str
        :param LowestIsp2: 國外可用率最低的運營商
        :type LowestIsp2: str
        :param ProvinceData2: 國外分區域的可用率數據
        :type ProvinceData2: list of ProvinceDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AvgAvailRatio = None
        self.LowestAvailRatio = None
        self.LowestProvince = None
        self.LowestIsp = None
        self.ProvinceData = None
        self.AvgTime = None
        self.AvgAvailRatio2 = None
        self.AvgTime2 = None
        self.LowestAvailRatio2 = None
        self.LowestProvince2 = None
        self.LowestIsp2 = None
        self.ProvinceData2 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AvgAvailRatio = params.get("AvgAvailRatio")
        self.LowestAvailRatio = params.get("LowestAvailRatio")
        self.LowestProvince = params.get("LowestProvince")
        self.LowestIsp = params.get("LowestIsp")
        if params.get("ProvinceData") is not None:
            self.ProvinceData = []
            for item in params.get("ProvinceData"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData.append(obj)
        self.AvgTime = params.get("AvgTime")
        self.AvgAvailRatio2 = params.get("AvgAvailRatio2")
        self.AvgTime2 = params.get("AvgTime2")
        self.LowestAvailRatio2 = params.get("LowestAvailRatio2")
        self.LowestProvince2 = params.get("LowestProvince2")
        self.LowestIsp2 = params.get("LowestIsp2")
        if params.get("ProvinceData2") is not None:
            self.ProvinceData2 = []
            for item in params.get("ProvinceData2"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData2.append(obj)
        self.RequestId = params.get("RequestId")


class GetDailyAvailRatioRequest(AbstractModel):
    """GetDailyAvailRatio請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 撥測任務Id
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class GetDailyAvailRatioResponse(AbstractModel):
    """GetDailyAvailRatio返回參數結構體

    """

    def __init__(self):
        """
        :param AvgAvailRatio: 整體平均可用率
        :type AvgAvailRatio: float
        :param LowestAvailRatio: 各 最低可用率
        :type LowestAvailRatio: float
        :param LowestProvince: 可用率最低的 
        :type LowestProvince: str
        :param ProvinceData: 分 的可用率數據
        :type ProvinceData: list of ProvinceDetail
        :param AvgTime: 國内平均耗時，單位毫秒
        :type AvgTime: float
        :param AvgAvailRatio2: 國外平均可用率
        :type AvgAvailRatio2: float
        :param AvgTime2: 國外平均耗時，單位毫秒
        :type AvgTime2: float
        :param LowestAvailRatio2: 國外最低可用率
        :type LowestAvailRatio2: float
        :param LowestProvince2: 國外可用率最低的區域
        :type LowestProvince2: str
        :param ProvinceData2: 國外分區域的可用率數據
        :type ProvinceData2: list of ProvinceDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AvgAvailRatio = None
        self.LowestAvailRatio = None
        self.LowestProvince = None
        self.ProvinceData = None
        self.AvgTime = None
        self.AvgAvailRatio2 = None
        self.AvgTime2 = None
        self.LowestAvailRatio2 = None
        self.LowestProvince2 = None
        self.ProvinceData2 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AvgAvailRatio = params.get("AvgAvailRatio")
        self.LowestAvailRatio = params.get("LowestAvailRatio")
        self.LowestProvince = params.get("LowestProvince")
        if params.get("ProvinceData") is not None:
            self.ProvinceData = []
            for item in params.get("ProvinceData"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData.append(obj)
        self.AvgTime = params.get("AvgTime")
        self.AvgAvailRatio2 = params.get("AvgAvailRatio2")
        self.AvgTime2 = params.get("AvgTime2")
        self.LowestAvailRatio2 = params.get("LowestAvailRatio2")
        self.LowestProvince2 = params.get("LowestProvince2")
        if params.get("ProvinceData2") is not None:
            self.ProvinceData2 = []
            for item in params.get("ProvinceData2"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData2.append(obj)
        self.RequestId = params.get("RequestId")


class GetRealAvailRatioRequest(AbstractModel):
    """GetRealAvailRatio請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 撥測任務Id
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class GetRealAvailRatioResponse(AbstractModel):
    """GetRealAvailRatio返回參數結構體

    """

    def __init__(self):
        """
        :param AvgAvailRatio: 國内平均可用率
        :type AvgAvailRatio: float
        :param LowestAvailRatio: 各 最低可用率
        :type LowestAvailRatio: float
        :param LowestProvince: 可用率最低的 
        :type LowestProvince: str
        :param LowestIsp: 可用率最低的運營商
        :type LowestIsp: str
        :param ProvinceData: 分 的可用率數據
        :type ProvinceData: list of ProvinceDetail
        :param AvgTime: 國内平均耗時，單位毫秒
        :type AvgTime: float
        :param AvgAvailRatio2: 國外平均可用率
        :type AvgAvailRatio2: float
        :param AvgTime2: 國外平均耗時，單位毫秒
        :type AvgTime2: float
        :param LowestAvailRatio2: 國外最低可用率
        :type LowestAvailRatio2: float
        :param LowestProvince2: 國外可用率最低的區域
        :type LowestProvince2: str
        :param LowestIsp2: 國外可用率最低的運營商
        :type LowestIsp2: str
        :param ProvinceData2: 國外分區域的可用率數據
        :type ProvinceData2: list of ProvinceDetail
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.AvgAvailRatio = None
        self.LowestAvailRatio = None
        self.LowestProvince = None
        self.LowestIsp = None
        self.ProvinceData = None
        self.AvgTime = None
        self.AvgAvailRatio2 = None
        self.AvgTime2 = None
        self.LowestAvailRatio2 = None
        self.LowestProvince2 = None
        self.LowestIsp2 = None
        self.ProvinceData2 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AvgAvailRatio = params.get("AvgAvailRatio")
        self.LowestAvailRatio = params.get("LowestAvailRatio")
        self.LowestProvince = params.get("LowestProvince")
        self.LowestIsp = params.get("LowestIsp")
        if params.get("ProvinceData") is not None:
            self.ProvinceData = []
            for item in params.get("ProvinceData"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData.append(obj)
        self.AvgTime = params.get("AvgTime")
        self.AvgAvailRatio2 = params.get("AvgAvailRatio2")
        self.AvgTime2 = params.get("AvgTime2")
        self.LowestAvailRatio2 = params.get("LowestAvailRatio2")
        self.LowestProvince2 = params.get("LowestProvince2")
        self.LowestIsp2 = params.get("LowestIsp2")
        if params.get("ProvinceData2") is not None:
            self.ProvinceData2 = []
            for item in params.get("ProvinceData2"):
                obj = ProvinceDetail()
                obj._deserialize(item)
                self.ProvinceData2.append(obj)
        self.RequestId = params.get("RequestId")


class GetRespTimeTrendExRequest(AbstractModel):
    """GetRespTimeTrendEx請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 驗證成功的撥測任務id
        :type TaskId: int
        :param Date: 統計數據的發生日期。格式如：2017-05-09
        :type Date: str
        :param Period: 數據的采集週期，單位分鍾。取值可爲 1, 5, 15, 30
        :type Period: int
        :param Dimensions: 可爲 Isp, Province
        :type Dimensions: :class:`taifucloudcloud.cat.v20180409.models.DimensionsDetail`
        :param MetricName: 可爲  totalTime, parseTime, connectTime, sendTime, waitTime, receiveTime, availRatio。缺省值爲 totalTime
        :type MetricName: str
        """
        self.TaskId = None
        self.Date = None
        self.Period = None
        self.Dimensions = None
        self.MetricName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Date = params.get("Date")
        self.Period = params.get("Period")
        if params.get("Dimensions") is not None:
            self.Dimensions = DimensionsDetail()
            self.Dimensions._deserialize(params.get("Dimensions"))
        self.MetricName = params.get("MetricName")


class GetRespTimeTrendExResponse(AbstractModel):
    """GetRespTimeTrendEx返回參數結構體

    """

    def __init__(self):
        """
        :param DataPoints: 數據點集合，延遲等走勢數據
        :type DataPoints: list of DataPointMetric
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DataPoints = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataPoints") is not None:
            self.DataPoints = []
            for item in params.get("DataPoints"):
                obj = DataPointMetric()
                obj._deserialize(item)
                self.DataPoints.append(obj)
        self.RequestId = params.get("RequestId")


class GetResultSummaryRequest(AbstractModel):
    """GetResultSummary請求參數結構體

    """

    def __init__(self):
        """
        :param TaskIds: 任務Id清單
        :type TaskIds: list of int non-negative
        """
        self.TaskIds = None


    def _deserialize(self, params):
        self.TaskIds = params.get("TaskIds")


class GetResultSummaryResponse(AbstractModel):
    """GetResultSummary返回參數結構體

    """

    def __init__(self):
        """
        :param RealData: 實時統計數據
        :type RealData: list of ResultSummary
        :param DayData: 按天的統計數據
        :type DayData: list of ResultSummary
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RealData = None
        self.DayData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RealData") is not None:
            self.RealData = []
            for item in params.get("RealData"):
                obj = ResultSummary()
                obj._deserialize(item)
                self.RealData.append(obj)
        if params.get("DayData") is not None:
            self.DayData = []
            for item in params.get("DayData"):
                obj = ResultSummary()
                obj._deserialize(item)
                self.DayData.append(obj)
        self.RequestId = params.get("RequestId")


class GetReturnCodeHistoryRequest(AbstractModel):
    """GetReturnCodeHistory請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 正整數。驗證成功的撥測任務id
        :type TaskId: int
        :param BeginTime: 開始時間點。格式如：2017-05-09 10:20:00。注意，BeginTime 和 EndTime 需要在同一天
        :type BeginTime: str
        :param EndTime: 結束時間點。格式如：2017-05-09 10:25:00。注意，BeginTime 和 EndTime 需要在同一天
        :type EndTime: str
        :param Province:  名稱的全拼
        :type Province: str
        """
        self.TaskId = None
        self.BeginTime = None
        self.EndTime = None
        self.Province = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Province = params.get("Province")


class GetReturnCodeHistoryResponse(AbstractModel):
    """GetReturnCodeHistory返回參數結構體

    """

    def __init__(self):
        """
        :param Details: 撥測失敗詳情清單
        :type Details: list of CatReturnDetail
        :param Summary: 撥測失敗匯總清單
        :type Summary: list of CatReturnSummary
        :param BeginTime: 開始時間
        :type BeginTime: str
        :param EndTime: 截至時間
        :type EndTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Details = None
        self.Summary = None
        self.BeginTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = CatReturnDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        if params.get("Summary") is not None:
            self.Summary = []
            for item in params.get("Summary"):
                obj = CatReturnSummary()
                obj._deserialize(item)
                self.Summary.append(obj)
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class GetReturnCodeInfoRequest(AbstractModel):
    """GetReturnCodeInfo請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 正整數。驗證成功的撥測任務id
        :type TaskId: int
        :param BeginTime: 開始時間點。格式如：2017-05-09 10:20:00，最多拉群兩天的數據
        :type BeginTime: str
        :param EndTime: 結束時間點。格式如：2017-05-09 10:25:00，最多拉群兩天的數據
        :type EndTime: str
        :param Province:  名稱的全拼
        :type Province: str
        """
        self.TaskId = None
        self.BeginTime = None
        self.EndTime = None
        self.Province = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Province = params.get("Province")


class GetReturnCodeInfoResponse(AbstractModel):
    """GetReturnCodeInfo返回參數結構體

    """

    def __init__(self):
        """
        :param Details: 撥測失敗詳情清單
        :type Details: list of CatReturnDetail
        :param Summary: 撥測失敗匯總清單
        :type Summary: list of CatReturnSummary
        :param BeginTime: 開始時間
        :type BeginTime: str
        :param EndTime: 截至時間
        :type EndTime: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.Details = None
        self.Summary = None
        self.BeginTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = CatReturnDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        if params.get("Summary") is not None:
            self.Summary = []
            for item in params.get("Summary"):
                obj = CatReturnSummary()
                obj._deserialize(item)
                self.Summary.append(obj)
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class GetTaskTotalNumberRequest(AbstractModel):
    """GetTaskTotalNumber請求參數結構體

    """


class GetTaskTotalNumberResponse(AbstractModel):
    """GetTaskTotalNumber返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 撥測任務總數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class IspDetail(AbstractModel):
    """運營商可用率

    """

    def __init__(self):
        """
        :param IspName: 運營商名稱
        :type IspName: str
        :param AvailRatio: 可用率
        :type AvailRatio: float
        :param AvgTime: 平均耗時
注意：此欄位可能返回 null，表示取不到有效值。
        :type AvgTime: float
        """
        self.IspName = None
        self.AvailRatio = None
        self.AvgTime = None


    def _deserialize(self, params):
        self.IspName = params.get("IspName")
        self.AvailRatio = params.get("AvailRatio")
        self.AvgTime = params.get("AvgTime")


class ModifyAgentGroupRequest(AbstractModel):
    """ModifyAgentGroup請求參數結構體

    """

    def __init__(self):
        """
        :param GroupId: 撥測分組ID
        :type GroupId: int
        :param GroupName: 撥測分組名稱
        :type GroupName: str
        :param IsDefault: 是否爲預設分組。取值可爲0，1。取 1 時表示設置爲預設分組
        :type IsDefault: int
        :param Agents: Province, Isp 需要成對地進行選擇。參數對的取值範圍。參見：DescribeAgents 的返回結果。
        :type Agents: list of CatAgent
        """
        self.GroupId = None
        self.GroupName = None
        self.IsDefault = None
        self.Agents = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.IsDefault = params.get("IsDefault")
        if params.get("Agents") is not None:
            self.Agents = []
            for item in params.get("Agents"):
                obj = CatAgent()
                obj._deserialize(item)
                self.Agents.append(obj)


class ModifyAgentGroupResponse(AbstractModel):
    """ModifyAgentGroup返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTaskExRequest(AbstractModel):
    """ModifyTaskEx請求參數結構體

    """

    def __init__(self):
        """
        :param CatTypeName: http, https, ping, tcp, ftp, smtp, udp, dns 之一
        :type CatTypeName: str
        :param Url: 撥測的URL，例如：www.qq.com (URL域名解析需要能解析出具體的IP)
        :type Url: str
        :param Period: 撥測週期。取值可爲1,5,15,30之一, 單位：分鍾。精度不能低于用戶等級規定的最小精度
        :type Period: int
        :param TaskName: 撥測任務名稱不能超過32個字元。同一個用戶創建的任務名不可重複
        :type TaskName: str
        :param TaskId: 驗證成功的撥測任務ID
        :type TaskId: int
        :param AgentGroupId: 撥測分組ID，體現本撥測任務要采用哪些運營商作爲撥測源。一般可直接填寫本用戶的預設撥測分組。參見：DescribeAgentGroupList 介面，本參數使用返回結果裏的GroupId的值。注意，Type爲0時，AgentGroupId爲必填
        :type AgentGroupId: int
        :param Host: 指定域名(如需要)
        :type Host: str
        :param Port: 撥測目标的端口号
        :type Port: int
        :param IsHeader: 是否爲Header請求（非0 發起Header 請求。爲0，且PostData非空，發起POST請求。爲0，PostData爲空，發起GET請求）
        :type IsHeader: int
        :param SslVer: URL中含有"https"時有用。缺省爲SSLv23。需要爲 TLSv1_2, TLSv1_1, TLSv1, SSLv2, SSLv23, SSLv3 之一
        :type SslVer: str
        :param PostData: POST 請求數據，空字串表示非POST請求
        :type PostData: str
        :param UserAgent: 用戶Agent訊息
        :type UserAgent: str
        :param CheckStr: 要在結果中進行比對的字串
        :type CheckStr: str
        :param CheckType: 1 表示通過檢查結果是否包含CheckStr 進行校驗
        :type CheckType: int
        :param Cookie: 需要設置的Cookie訊息
        :type Cookie: str
        :param UserName: 登入服務器的賬号。如果爲空字串，表示不用校驗用戶密碼。只做簡單連接服務器的撥測
        :type UserName: str
        :param PassWord: 登入服務器的密碼
        :type PassWord: str
        :param ReqDataType: 缺省爲0，0 表示請求爲字串類型, 1表示爲二進制類型
        :type ReqDataType: int
        :param ReqData: 發起TCP, UDP請求的協議請求數據
        :type ReqData: str
        :param RespDataType: 缺省爲0。0 表示請求爲字串類型。1表示爲二進制類型
        :type RespDataType: str
        :param RespData: 預期的UDP請求的回應數據。字串型，只需要返回的結果裏包含本字串算校驗通過。二進制型，則需要嚴格等于才算通過
        :type RespData: str
        :param DnsSvr: 目的DNS服務器，可以爲空字串
        :type DnsSvr: str
        :param DnsCheckIp: 需要檢驗是否在DNS IP清單的IP。可以爲空字串，表示不校驗
        :type DnsCheckIp: str
        :param DnsQueryType: 需要爲下列值之一。缺省爲A。A, MX, NS, CNAME, TXT, ANY
        :type DnsQueryType: str
        :param UseSecConn: 是否使用安全連結SSL， 0 不使用，1 使用
        :type UseSecConn: int
        :param NeedAuth: FTP登入驗證方式，  0 不驗證  1 匿名登入  2 需要身份驗證
        :type NeedAuth: int
        :param Type: Type=0 預設 （站點監控） Type=2 可用率監控
        :type Type: int
        :param RedirectFollowNum: 跟随跳轉次數，取值範圍0-5，不傳則表示不跟随
        :type RedirectFollowNum: int
        """
        self.CatTypeName = None
        self.Url = None
        self.Period = None
        self.TaskName = None
        self.TaskId = None
        self.AgentGroupId = None
        self.Host = None
        self.Port = None
        self.IsHeader = None
        self.SslVer = None
        self.PostData = None
        self.UserAgent = None
        self.CheckStr = None
        self.CheckType = None
        self.Cookie = None
        self.UserName = None
        self.PassWord = None
        self.ReqDataType = None
        self.ReqData = None
        self.RespDataType = None
        self.RespData = None
        self.DnsSvr = None
        self.DnsCheckIp = None
        self.DnsQueryType = None
        self.UseSecConn = None
        self.NeedAuth = None
        self.Type = None
        self.RedirectFollowNum = None


    def _deserialize(self, params):
        self.CatTypeName = params.get("CatTypeName")
        self.Url = params.get("Url")
        self.Period = params.get("Period")
        self.TaskName = params.get("TaskName")
        self.TaskId = params.get("TaskId")
        self.AgentGroupId = params.get("AgentGroupId")
        self.Host = params.get("Host")
        self.Port = params.get("Port")
        self.IsHeader = params.get("IsHeader")
        self.SslVer = params.get("SslVer")
        self.PostData = params.get("PostData")
        self.UserAgent = params.get("UserAgent")
        self.CheckStr = params.get("CheckStr")
        self.CheckType = params.get("CheckType")
        self.Cookie = params.get("Cookie")
        self.UserName = params.get("UserName")
        self.PassWord = params.get("PassWord")
        self.ReqDataType = params.get("ReqDataType")
        self.ReqData = params.get("ReqData")
        self.RespDataType = params.get("RespDataType")
        self.RespData = params.get("RespData")
        self.DnsSvr = params.get("DnsSvr")
        self.DnsCheckIp = params.get("DnsCheckIp")
        self.DnsQueryType = params.get("DnsQueryType")
        self.UseSecConn = params.get("UseSecConn")
        self.NeedAuth = params.get("NeedAuth")
        self.Type = params.get("Type")
        self.RedirectFollowNum = params.get("RedirectFollowNum")


class ModifyTaskExResponse(AbstractModel):
    """ModifyTaskEx返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 撥測任務ID。驗證通過後，創建任務時使用，傳遞給CreateTask 介面。
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PauseTaskRequest(AbstractModel):
    """PauseTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 撥測任務id
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class PauseTaskResponse(AbstractModel):
    """PauseTask返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ProvinceDetail(AbstractModel):
    """ 可用率

    """

    def __init__(self):
        """
        :param AvgAvailRatio: 可用率
        :type AvgAvailRatio: float
        :param ProvinceName:  名稱
        :type ProvinceName: str
        :param Mapkey:  英文名稱
        :type Mapkey: str
        :param TimeStamp: 統計時間點
        :type TimeStamp: str
        :param IspDetail: 分運營商可用率
        :type IspDetail: list of IspDetail
        :param AvgTime: 平均耗時，單位毫秒
        :type AvgTime: float
        :param Province:  
        :type Province: str
        """
        self.AvgAvailRatio = None
        self.ProvinceName = None
        self.Mapkey = None
        self.TimeStamp = None
        self.IspDetail = None
        self.AvgTime = None
        self.Province = None


    def _deserialize(self, params):
        self.AvgAvailRatio = params.get("AvgAvailRatio")
        self.ProvinceName = params.get("ProvinceName")
        self.Mapkey = params.get("Mapkey")
        self.TimeStamp = params.get("TimeStamp")
        if params.get("IspDetail") is not None:
            self.IspDetail = []
            for item in params.get("IspDetail"):
                obj = IspDetail()
                obj._deserialize(item)
                self.IspDetail.append(obj)
        self.AvgTime = params.get("AvgTime")
        self.Province = params.get("Province")


class ResultSummary(AbstractModel):
    """實時統計數據

    """

    def __init__(self):
        """
        :param LogTime: 統計時間
        :type LogTime: str
        :param TaskId: 任務ID
        :type TaskId: int
        :param AvailRatio: 實時可用率
        :type AvailRatio: float
        :param ReponseTime: 實時響應時間
        :type ReponseTime: float
        """
        self.LogTime = None
        self.TaskId = None
        self.AvailRatio = None
        self.ReponseTime = None


    def _deserialize(self, params):
        self.LogTime = params.get("LogTime")
        self.TaskId = params.get("TaskId")
        self.AvailRatio = params.get("AvailRatio")
        self.ReponseTime = params.get("ReponseTime")


class RunTaskRequest(AbstractModel):
    """RunTask請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務Id
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class RunTaskResponse(AbstractModel):
    """RunTask返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TaskAlarm(AbstractModel):
    """可用性監控任務狀态及告警訊息

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: int
        :param TaskName: 任務名稱
        :type TaskName: str
        :param Period: 任務週期，單位爲分鍾。目前支援1，5，15，30幾種取值
        :type Period: int
        :param CatTypeName: 撥測類型。http, https, ping, tcp, udp, smtp, pop3, dns 之一
        :type CatTypeName: str
        :param Status: 任務狀态。1表示暫停，2表示運作中，0爲初始态
        :type Status: int
        :param CgiUrl: 撥測任務的URL
        :type CgiUrl: str
        :param AddTime: 任務創建時間
        :type AddTime: str
        :param AlarmStatus: 告警狀态。1 故障，0 正常
        :type AlarmStatus: int
        :param StatusInfo: 告警狀态描述，統計訊息
        :type StatusInfo: str
        :param UpdateTime: 任務更新時間
        :type UpdateTime: str
        """
        self.TaskId = None
        self.TaskName = None
        self.Period = None
        self.CatTypeName = None
        self.Status = None
        self.CgiUrl = None
        self.AddTime = None
        self.AlarmStatus = None
        self.StatusInfo = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.Period = params.get("Period")
        self.CatTypeName = params.get("CatTypeName")
        self.Status = params.get("Status")
        self.CgiUrl = params.get("CgiUrl")
        self.AddTime = params.get("AddTime")
        self.AlarmStatus = params.get("AlarmStatus")
        self.StatusInfo = params.get("StatusInfo")
        self.UpdateTime = params.get("UpdateTime")


class VerifyResultRequest(AbstractModel):
    """VerifyResult請求參數結構體

    """

    def __init__(self):
        """
        :param ResultId: 要查詢的撥測任務的結果id
        :type ResultId: int
        """
        self.ResultId = None


    def _deserialize(self, params):
        self.ResultId = params.get("ResultId")


class VerifyResultResponse(AbstractModel):
    """VerifyResult返回參數結構體

    """

    def __init__(self):
        """
        :param ErrorReason: 錯誤的原因
        :type ErrorReason: str
        :param ResultCode: 錯誤号
        :type ResultCode: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ErrorReason = None
        self.ResultCode = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorReason = params.get("ErrorReason")
        self.ResultCode = params.get("ResultCode")
        self.RequestId = params.get("RequestId")