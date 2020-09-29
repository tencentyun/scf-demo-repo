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


class CallbackInfo(AbstractModel):
    """任務結果回調網址訊息

    """

    def __init__(self):
        """
        :param Url: 回調URL。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")


class ClassificationEditingInfo(AbstractModel):
    """視訊分類識别任務參數訊息

    """

    def __init__(self):
        """
        :param Switch: 是否開啓視訊分類識别。0爲關閉，1爲開啓。其他非0非1值預設爲0。
        :type Switch: int
        :param CustomInfo: 額外定制化服務參數。參數爲序列化的Json字串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class ClassificationTaskResult(AbstractModel):
    """視訊分類識别結果訊息

    """

    def __init__(self):
        """
        :param Status: 編輯任務狀态。 
1：執行中；2：成功；3：失敗。
        :type Status: int
        :param ErrCode: 編輯任務失敗錯誤碼。 
0：成功；其他值：失敗。
        :type ErrCode: int
        :param ErrMsg: 編輯任務失敗錯誤描述。
        :type ErrMsg: str
        :param ItemSet: 視訊分類識别結果集。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ItemSet: list of ClassificationTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = ClassificationTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)


class ClassificationTaskResultItem(AbstractModel):
    """視訊分類識别結果項

    """

    def __init__(self):
        """
        :param Classification: 分類名稱。
        :type Classification: str
        :param Confidence: 置信度，取值範圍是 0 到 100。
        :type Confidence: float
        """
        self.Classification = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Classification = params.get("Classification")
        self.Confidence = params.get("Confidence")


class CosAuthMode(AbstractModel):
    """任務視訊cos授權訊息

    """

    def __init__(self):
        """
        :param Type: 授權類型，可選值： 
0：bucket授權，需要将對應bucket授權給本服務帳號（3020447271），否則會讀寫cos失敗； 
1：key托管，把cos的賬號id和key托管於本服務，本服務會提供一個托管id； 
3：臨時key授權。
注意：目前智慧編輯還不支援臨時key授權。
        :type Type: int
        :param HostedId: cos賬號托管id，Type等於1時必選。
        :type HostedId: str
        :param SecretId: cos身份識别id，Type等於3時必選。
        :type SecretId: str
        :param SecretKey: cos身份秘鑰，Type等於3時必選。
        :type SecretKey: str
        :param Token: 臨時授權 token，Type等於3時必選。
        :type Token: str
        """
        self.Type = None
        self.HostedId = None
        self.SecretId = None
        self.SecretKey = None
        self.Token = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.HostedId = params.get("HostedId")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")
        self.Token = params.get("Token")


class CosInfo(AbstractModel):
    """任務視訊cos訊息

    """

    def __init__(self):
        """
        :param Region: cos 區域值。例如：ap-beijing。
        :type Region: str
        :param Bucket: cos 儲存桶，格式爲BuketName-AppId。例如：test-123456。
        :type Bucket: str
        :param Path: cos 路徑。 
對於寫表示目錄，例如：/test； 
對於讀表示文件路徑，例如：/test/test.mp4。
        :type Path: str
        :param CosAuthMode: cos 授權訊息，不填預設爲公有權限。
        :type CosAuthMode: :class:`taifucloudcloud.ie.v20200304.models.CosAuthMode`
        """
        self.Region = None
        self.Bucket = None
        self.Path = None
        self.CosAuthMode = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.Bucket = params.get("Bucket")
        self.Path = params.get("Path")
        if params.get("CosAuthMode") is not None:
            self.CosAuthMode = CosAuthMode()
            self.CosAuthMode._deserialize(params.get("CosAuthMode"))


class CoverEditingInfo(AbstractModel):
    """智慧封面任務參數訊息

    """

    def __init__(self):
        """
        :param Switch: 是否開啓智慧封面。0爲關閉，1爲開啓。其他非0非1值預設爲0。
        :type Switch: int
        :param CustomInfo: 額外定制化服務參數。參數爲序列化的Json字串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class CoverTaskResult(AbstractModel):
    """智慧封面結果訊息

    """

    def __init__(self):
        """
        :param Status: 編輯任務狀态。 
1：執行中；2：成功；3：失敗。
        :type Status: int
        :param ErrCode: 編輯任務失敗錯誤碼。 
0：成功；其他值：失敗。
        :type ErrCode: int
        :param ErrMsg: 編輯任務失敗錯誤描述。
        :type ErrMsg: str
        :param ItemSet: 智慧封面結果集。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ItemSet: list of CoverTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = CoverTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)


class CoverTaskResultItem(AbstractModel):
    """智慧封面結果項

    """

    def __init__(self):
        """
        :param CoverUrl: 智慧封面網址。
        :type CoverUrl: str
        :param Confidence: 置信度，取值範圍是 0 到 100。
        :type Confidence: float
        """
        self.CoverUrl = None
        self.Confidence = None


    def _deserialize(self, params):
        self.CoverUrl = params.get("CoverUrl")
        self.Confidence = params.get("Confidence")


class CreateEditingTaskRequest(AbstractModel):
    """CreateEditingTask請求參數結構體

    """

    def __init__(self):
        """
        :param EditingInfo: 智慧編輯任務參數。
        :type EditingInfo: :class:`taifucloudcloud.ie.v20200304.models.EditingInfo`
        :param DownInfo: 視訊源訊息。
        :type DownInfo: :class:`taifucloudcloud.ie.v20200304.models.DownInfo`
        :param SaveInfo: 結果儲存訊息。對於包含智慧拆條、智慧集錦或者智慧封面的任務必選。
        :type SaveInfo: :class:`taifucloudcloud.ie.v20200304.models.SaveInfo`
        :param CallbackInfo: 任務結果回調網址訊息。
        :type CallbackInfo: :class:`taifucloudcloud.ie.v20200304.models.CallbackInfo`
        """
        self.EditingInfo = None
        self.DownInfo = None
        self.SaveInfo = None
        self.CallbackInfo = None


    def _deserialize(self, params):
        if params.get("EditingInfo") is not None:
            self.EditingInfo = EditingInfo()
            self.EditingInfo._deserialize(params.get("EditingInfo"))
        if params.get("DownInfo") is not None:
            self.DownInfo = DownInfo()
            self.DownInfo._deserialize(params.get("DownInfo"))
        if params.get("SaveInfo") is not None:
            self.SaveInfo = SaveInfo()
            self.SaveInfo._deserialize(params.get("SaveInfo"))
        if params.get("CallbackInfo") is not None:
            self.CallbackInfo = CallbackInfo()
            self.CallbackInfo._deserialize(params.get("CallbackInfo"))


class CreateEditingTaskResponse(AbstractModel):
    """CreateEditingTask返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 編輯任務 ID，可以通過該 ID 查詢任務狀态。
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeEditingTaskResultRequest(AbstractModel):
    """DescribeEditingTaskResult請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 編輯任務 ID。
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeEditingTaskResultResponse(AbstractModel):
    """DescribeEditingTaskResult返回參數結構體

    """

    def __init__(self):
        """
        :param TaskResult: 編輯任務結果訊息。
        :type TaskResult: :class:`taifucloudcloud.ie.v20200304.models.EditingTaskResult`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskResult") is not None:
            self.TaskResult = EditingTaskResult()
            self.TaskResult._deserialize(params.get("TaskResult"))
        self.RequestId = params.get("RequestId")


class DownInfo(AbstractModel):
    """視訊源訊息

    """

    def __init__(self):
        """
        :param Type: 下載類型，可選值： 
0：UrlInfo； 
1：CosInfo。
        :type Type: int
        :param UrlInfo: Url形式下載訊息，當Type等於0時必選。
        :type UrlInfo: :class:`taifucloudcloud.ie.v20200304.models.UrlInfo`
        :param CosInfo: Cos形式下載訊息，當Type等於1時必選。
        :type CosInfo: :class:`taifucloudcloud.ie.v20200304.models.CosInfo`
        """
        self.Type = None
        self.UrlInfo = None
        self.CosInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("UrlInfo") is not None:
            self.UrlInfo = UrlInfo()
            self.UrlInfo._deserialize(params.get("UrlInfo"))
        if params.get("CosInfo") is not None:
            self.CosInfo = CosInfo()
            self.CosInfo._deserialize(params.get("CosInfo"))


class EditingInfo(AbstractModel):
    """智慧編輯任務參數訊息

    """

    def __init__(self):
        """
        :param TagEditingInfo: 視訊標簽識别任務參數，不填則不開啓。
        :type TagEditingInfo: :class:`taifucloudcloud.ie.v20200304.models.TagEditingInfo`
        :param ClassificationEditingInfo: 視訊分類識别任務參數，不填則不開啓。
        :type ClassificationEditingInfo: :class:`taifucloudcloud.ie.v20200304.models.ClassificationEditingInfo`
        :param StripEditingInfo: 智慧拆條任務參數，不填則不開啓。
        :type StripEditingInfo: :class:`taifucloudcloud.ie.v20200304.models.StripEditingInfo`
        :param HighlightsEditingInfo: 智慧集錦任務參數，不填則不開啓。
        :type HighlightsEditingInfo: :class:`taifucloudcloud.ie.v20200304.models.HighlightsEditingInfo`
        :param CoverEditingInfo: 智慧封面任務參數，不填則不開啓。
        :type CoverEditingInfo: :class:`taifucloudcloud.ie.v20200304.models.CoverEditingInfo`
        :param OpeningEndingEditingInfo: 片頭片尾識别任務參數，不填則不開啓。
        :type OpeningEndingEditingInfo: :class:`taifucloudcloud.ie.v20200304.models.OpeningEndingEditingInfo`
        """
        self.TagEditingInfo = None
        self.ClassificationEditingInfo = None
        self.StripEditingInfo = None
        self.HighlightsEditingInfo = None
        self.CoverEditingInfo = None
        self.OpeningEndingEditingInfo = None


    def _deserialize(self, params):
        if params.get("TagEditingInfo") is not None:
            self.TagEditingInfo = TagEditingInfo()
            self.TagEditingInfo._deserialize(params.get("TagEditingInfo"))
        if params.get("ClassificationEditingInfo") is not None:
            self.ClassificationEditingInfo = ClassificationEditingInfo()
            self.ClassificationEditingInfo._deserialize(params.get("ClassificationEditingInfo"))
        if params.get("StripEditingInfo") is not None:
            self.StripEditingInfo = StripEditingInfo()
            self.StripEditingInfo._deserialize(params.get("StripEditingInfo"))
        if params.get("HighlightsEditingInfo") is not None:
            self.HighlightsEditingInfo = HighlightsEditingInfo()
            self.HighlightsEditingInfo._deserialize(params.get("HighlightsEditingInfo"))
        if params.get("CoverEditingInfo") is not None:
            self.CoverEditingInfo = CoverEditingInfo()
            self.CoverEditingInfo._deserialize(params.get("CoverEditingInfo"))
        if params.get("OpeningEndingEditingInfo") is not None:
            self.OpeningEndingEditingInfo = OpeningEndingEditingInfo()
            self.OpeningEndingEditingInfo._deserialize(params.get("OpeningEndingEditingInfo"))


class EditingTaskResult(AbstractModel):
    """智慧識别任務結果訊息

    """

    def __init__(self):
        """
        :param TaskId: 編輯任務 ID。
        :type TaskId: str
        :param Status: 編輯任務狀态。 
1：執行中；2：已完成。
        :type Status: int
        :param TagTaskResult: 視訊標簽識别結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type TagTaskResult: :class:`taifucloudcloud.ie.v20200304.models.TagTaskResult`
        :param ClassificationTaskResult: 視訊分類識别結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ClassificationTaskResult: :class:`taifucloudcloud.ie.v20200304.models.ClassificationTaskResult`
        :param StripTaskResult: 智慧拆條結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type StripTaskResult: :class:`taifucloudcloud.ie.v20200304.models.StripTaskResult`
        :param HighlightsTaskResult: 智慧集錦結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type HighlightsTaskResult: :class:`taifucloudcloud.ie.v20200304.models.HighlightsTaskResult`
        :param CoverTaskResult: 智慧封面結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type CoverTaskResult: :class:`taifucloudcloud.ie.v20200304.models.CoverTaskResult`
        :param OpeningEndingTaskResult: 片頭片尾識别結果。
注意：此欄位可能返回 null，表示取不到有效值。
        :type OpeningEndingTaskResult: :class:`taifucloudcloud.ie.v20200304.models.OpeningEndingTaskResult`
        """
        self.TaskId = None
        self.Status = None
        self.TagTaskResult = None
        self.ClassificationTaskResult = None
        self.StripTaskResult = None
        self.HighlightsTaskResult = None
        self.CoverTaskResult = None
        self.OpeningEndingTaskResult = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        if params.get("TagTaskResult") is not None:
            self.TagTaskResult = TagTaskResult()
            self.TagTaskResult._deserialize(params.get("TagTaskResult"))
        if params.get("ClassificationTaskResult") is not None:
            self.ClassificationTaskResult = ClassificationTaskResult()
            self.ClassificationTaskResult._deserialize(params.get("ClassificationTaskResult"))
        if params.get("StripTaskResult") is not None:
            self.StripTaskResult = StripTaskResult()
            self.StripTaskResult._deserialize(params.get("StripTaskResult"))
        if params.get("HighlightsTaskResult") is not None:
            self.HighlightsTaskResult = HighlightsTaskResult()
            self.HighlightsTaskResult._deserialize(params.get("HighlightsTaskResult"))
        if params.get("CoverTaskResult") is not None:
            self.CoverTaskResult = CoverTaskResult()
            self.CoverTaskResult._deserialize(params.get("CoverTaskResult"))
        if params.get("OpeningEndingTaskResult") is not None:
            self.OpeningEndingTaskResult = OpeningEndingTaskResult()
            self.OpeningEndingTaskResult._deserialize(params.get("OpeningEndingTaskResult"))


class HighlightsEditingInfo(AbstractModel):
    """智慧集錦任務參數訊息

    """

    def __init__(self):
        """
        :param Switch: 是否開啓智慧集錦。0爲關閉，1爲開啓。其他非0非1值預設爲0。
        :type Switch: int
        :param CustomInfo: 額外定制化服務參數。參數爲序列化的Json字串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class HighlightsTaskResult(AbstractModel):
    """智慧集錦結果訊息

    """

    def __init__(self):
        """
        :param Status: 編輯任務狀态。 
1：執行中；2：成功；3：失敗。
        :type Status: int
        :param ErrCode: 編輯任務失敗錯誤碼。 
0：成功；其他值：失敗。
        :type ErrCode: int
        :param ErrMsg: 編輯任務失敗錯誤描述。
        :type ErrMsg: str
        :param ItemSet: 智慧集錦結果集。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ItemSet: list of HighlightsTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = HighlightsTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)


class HighlightsTaskResultItem(AbstractModel):
    """智慧集錦結果項

    """

    def __init__(self):
        """
        :param HighlightUrl: 智慧集錦網址。
        :type HighlightUrl: str
        :param CovImgUrl: 智慧集錦封面網址。
        :type CovImgUrl: str
        :param Confidence: 置信度，取值範圍是 0 到 100。
        :type Confidence: float
        :param Duration: 智慧集錦持續時間，單位：秒。
        :type Duration: float
        :param SegmentSet: 智慧集錦子片段結果集，集錦片段由這些子片段拼接生成。
        :type SegmentSet: list of HighlightsTaskResultItemSegment
        """
        self.HighlightUrl = None
        self.CovImgUrl = None
        self.Confidence = None
        self.Duration = None
        self.SegmentSet = None


    def _deserialize(self, params):
        self.HighlightUrl = params.get("HighlightUrl")
        self.CovImgUrl = params.get("CovImgUrl")
        self.Confidence = params.get("Confidence")
        self.Duration = params.get("Duration")
        if params.get("SegmentSet") is not None:
            self.SegmentSet = []
            for item in params.get("SegmentSet"):
                obj = HighlightsTaskResultItemSegment()
                obj._deserialize(item)
                self.SegmentSet.append(obj)


class HighlightsTaskResultItemSegment(AbstractModel):
    """智慧集錦結果片段

    """

    def __init__(self):
        """
        :param Confidence: 置信度，取值範圍是 0 到 100。
        :type Confidence: float
        :param StartTimeOffset: 集錦片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 集錦片段終止的偏移時間，單位：秒。
        :type EndTimeOffset: float
        """
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class OpeningEndingEditingInfo(AbstractModel):
    """片頭片尾識别任務參數訊息

    """

    def __init__(self):
        """
        :param Switch: 是否開啓片頭片尾識别。0爲關閉，1爲開啓。其他非0非1值預設爲0。
        :type Switch: int
        :param CustomInfo: 額外定制化服務參數。參數爲序列化的Json字串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class OpeningEndingTaskResult(AbstractModel):
    """片頭片尾識别結果訊息

    """

    def __init__(self):
        """
        :param Status: 編輯任務狀态。 
1：執行中；2：成功；3：失敗。
        :type Status: int
        :param ErrCode: 編輯任務失敗錯誤碼。 
0：成功；其他值：失敗。
        :type ErrCode: int
        :param ErrMsg: 編輯任務失敗錯誤描述。
        :type ErrMsg: str
        :param Item: 片頭片尾識别結果項。
注意：此欄位可能返回 null，表示取不到有效值。
        :type Item: :class:`taifucloudcloud.ie.v20200304.models.OpeningEndingTaskResultItem`
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.Item = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("Item") is not None:
            self.Item = OpeningEndingTaskResultItem()
            self.Item._deserialize(params.get("Item"))


class OpeningEndingTaskResultItem(AbstractModel):
    """片頭片尾識别結果項

    """

    def __init__(self):
        """
        :param OpeningTimeOffset: 視訊片頭的結束時間點，單位：秒。
        :type OpeningTimeOffset: float
        :param OpeningConfidence: 片頭識别置信度，取值範圍是 0 到 100。
        :type OpeningConfidence: float
        :param EndingTimeOffset: 視訊片尾的開始時間點，單位：秒。
        :type EndingTimeOffset: float
        :param EndingConfidence: 片尾識别置信度，取值範圍是 0 到 100。
        :type EndingConfidence: float
        """
        self.OpeningTimeOffset = None
        self.OpeningConfidence = None
        self.EndingTimeOffset = None
        self.EndingConfidence = None


    def _deserialize(self, params):
        self.OpeningTimeOffset = params.get("OpeningTimeOffset")
        self.OpeningConfidence = params.get("OpeningConfidence")
        self.EndingTimeOffset = params.get("EndingTimeOffset")
        self.EndingConfidence = params.get("EndingConfidence")


class SaveInfo(AbstractModel):
    """任務儲存訊息

    """

    def __init__(self):
        """
        :param Type: 儲存類型，可選值： 
1：CosInfo。
        :type Type: int
        :param CosInfo: Cos形式儲存訊息，當Type等於1時必選。
        :type CosInfo: :class:`taifucloudcloud.ie.v20200304.models.CosInfo`
        """
        self.Type = None
        self.CosInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("CosInfo") is not None:
            self.CosInfo = CosInfo()
            self.CosInfo._deserialize(params.get("CosInfo"))


class StripEditingInfo(AbstractModel):
    """智慧拆條任務參數訊息

    """

    def __init__(self):
        """
        :param Switch: 是否開啓智慧拆條。0爲關閉，1爲開啓。其他非0非1值預設爲0。
        :type Switch: int
        :param CustomInfo: 額外定制化服務參數。參數爲序列化的Json字串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class StripTaskResult(AbstractModel):
    """智慧拆條結果訊息

    """

    def __init__(self):
        """
        :param Status: 編輯任務狀态。 
1：執行中；2：成功；3：失敗。
        :type Status: int
        :param ErrCode: 編輯任務失敗錯誤碼。 
0：成功；其他值：失敗。
        :type ErrCode: int
        :param ErrMsg: 編輯任務失敗錯誤描述。
        :type ErrMsg: str
        :param ItemSet: 智慧拆條結果集。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ItemSet: list of StripTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = StripTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)


class StripTaskResultItem(AbstractModel):
    """智慧拆條結果項

    """

    def __init__(self):
        """
        :param SegmentUrl: 視訊拆條片段網址。
        :type SegmentUrl: str
        :param CovImgUrl: 拆條封面圖片網址。
        :type CovImgUrl: str
        :param Confidence: 置信度，取值範圍是 0 到 100。
        :type Confidence: float
        :param StartTimeOffset: 拆條片段起始的偏移時間，單位：秒。
        :type StartTimeOffset: float
        :param EndTimeOffset: 拆條片段終止的偏移時間，單位：秒。
        :type EndTimeOffset: float
        """
        self.SegmentUrl = None
        self.CovImgUrl = None
        self.Confidence = None
        self.StartTimeOffset = None
        self.EndTimeOffset = None


    def _deserialize(self, params):
        self.SegmentUrl = params.get("SegmentUrl")
        self.CovImgUrl = params.get("CovImgUrl")
        self.Confidence = params.get("Confidence")
        self.StartTimeOffset = params.get("StartTimeOffset")
        self.EndTimeOffset = params.get("EndTimeOffset")


class TagEditingInfo(AbstractModel):
    """視訊標簽識别任務參數訊息

    """

    def __init__(self):
        """
        :param Switch: 是否開啓視訊標簽識别。0爲關閉，1爲開啓。其他非0非1值預設爲0。
        :type Switch: int
        :param CustomInfo: 額外定制化服務參數。參數爲序列化的Json字串，例如：{"k1":"v1"}。
        :type CustomInfo: str
        """
        self.Switch = None
        self.CustomInfo = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CustomInfo = params.get("CustomInfo")


class TagTaskResult(AbstractModel):
    """視訊標簽識别結果訊息

    """

    def __init__(self):
        """
        :param Status: 編輯任務狀态。 
1：執行中；2：成功；3：失敗。
        :type Status: int
        :param ErrCode: 編輯任務失敗錯誤碼。 
0：成功；其他值：失敗。
        :type ErrCode: int
        :param ErrMsg: 編輯任務失敗錯誤描述。
        :type ErrMsg: str
        :param ItemSet: 視訊標簽識别結果集。
注意：此欄位可能返回 null，表示取不到有效值。
        :type ItemSet: list of TagTaskResultItem
        """
        self.Status = None
        self.ErrCode = None
        self.ErrMsg = None
        self.ItemSet = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrCode = params.get("ErrCode")
        self.ErrMsg = params.get("ErrMsg")
        if params.get("ItemSet") is not None:
            self.ItemSet = []
            for item in params.get("ItemSet"):
                obj = TagTaskResultItem()
                obj._deserialize(item)
                self.ItemSet.append(obj)


class TagTaskResultItem(AbstractModel):
    """視訊標簽識别結果項

    """

    def __init__(self):
        """
        :param Tag: 標簽名稱。
        :type Tag: str
        :param Confidence: 置信度，取值範圍是 0 到 100。
        :type Confidence: float
        """
        self.Tag = None
        self.Confidence = None


    def _deserialize(self, params):
        self.Tag = params.get("Tag")
        self.Confidence = params.get("Confidence")


class UrlInfo(AbstractModel):
    """任務視訊Url形式下載訊息。

    """

    def __init__(self):
        """
        :param Url: 視訊 URL。影音支援mp4、ts等格式；直播流支援flv、rtmp格式。
注意：目前智慧編輯還不支援直播流場景。
        :type Url: str
        :param Format: 視訊網址格式，可選值： 
0：影音 ;
1：直播流。 
預設爲0。其他非0非1值預設爲0。
        :type Format: int
        :param Host: 指定請求資源時，HTTP頭部host的值。
        :type Host: str
        """
        self.Url = None
        self.Format = None
        self.Host = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Format = params.get("Format")
        self.Host = params.get("Host")