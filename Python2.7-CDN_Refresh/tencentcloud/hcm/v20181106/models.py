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


class EvaluationRequest(AbstractModel):
    """Evaluation請求參數結構體

    """

    def __init__(self):
        """
        :param SessionId: 圖片唯一標識，一張圖片一個SessionId；
        :type SessionId: str
        :param Image: 圖片數據，需要使用base64對圖片的二進制數據進行編碼，與url參數二者填一即可；
        :type Image: str
        :param HcmAppid: 業務應用ID，與賬號應用APPID無關，是用來方便客戶管理服務的參數，新的 HcmAppid 可以在[控制台](https://console.cloud.taifucloud.com/hcm)【應用管理】下新建。
        :type HcmAppid: str
        :param Url: 圖片url，與Image參數二者填一即可；
        :type Url: str
        :param SupportHorizontalImage: 橫屏拍攝開關，若開啓則支援傳輸橫屏拍攝的圖片；
        :type SupportHorizontalImage: bool
        :param RejectNonArithmeticImage: 拒絕非速算圖（如風景圖、人物圖）開關，若開啓，則遇到非速算圖會快速返回拒絕的結果，但極端情況下可能會影響評估結果（比如算式截圖貼到風景畫裏可能被判爲非速算圖直接返回了）。
        :type RejectNonArithmeticImage: bool
        :param IsAsync: 異步模式標識，0：同步模式，1：異步模式。預設爲同步模式
        :type IsAsync: int
        """
        self.SessionId = None
        self.Image = None
        self.HcmAppid = None
        self.Url = None
        self.SupportHorizontalImage = None
        self.RejectNonArithmeticImage = None
        self.IsAsync = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Image = params.get("Image")
        self.HcmAppid = params.get("HcmAppid")
        self.Url = params.get("Url")
        self.SupportHorizontalImage = params.get("SupportHorizontalImage")
        self.RejectNonArithmeticImage = params.get("RejectNonArithmeticImage")
        self.IsAsync = params.get("IsAsync")


class EvaluationResponse(AbstractModel):
    """Evaluation返回參數結構體

    """

    def __init__(self):
        """
        :param SessionId: 圖片唯一標識，一張圖片一個SessionId；
        :type SessionId: str
        :param Items: 識别出的算式訊息；
注意：此欄位可能返回 null，表示取不到有效值。
        :type Items: list of Item
        :param TaskId: 任務 id，用於查詢介面
        :type TaskId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SessionId = None
        self.Items = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self.Items.append(obj)
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Item(AbstractModel):
    """識别出的算術式訊息及評估結果

    """

    def __init__(self):
        """
        :param Item: 識别的算式是否正确
        :type Item: str
        :param ItemString: 識别的算式
        :type ItemString: str
        :param ItemCoord: 識别的算式在圖片上的位置訊息
        :type ItemCoord: :class:`taifucloudcloud.hcm.v20181106.models.ItemCoord`
        :param Answer: 推薦的答案，暫不支援多個關系運算符、無關系運算符、單位換算錯題的推薦答案返回。
        :type Answer: str
        :param ExpressionType: 算式題型編號，如加減乘除四則題型，具體題型及編號如下：1 加減乘除四則 2 加減乘除已知結果求運算因子3 判斷大小 4 約等於估算 5 帶餘數除法 6 分數四則運算 7 單位換算 8 豎式加減法 9 豎式乘除法 10 脫式計算 11 解方程
注意：此欄位可能返回 null，表示取不到有效值。
        :type ExpressionType: str
        """
        self.Item = None
        self.ItemString = None
        self.ItemCoord = None
        self.Answer = None
        self.ExpressionType = None


    def _deserialize(self, params):
        self.Item = params.get("Item")
        self.ItemString = params.get("ItemString")
        if params.get("ItemCoord") is not None:
            self.ItemCoord = ItemCoord()
            self.ItemCoord._deserialize(params.get("ItemCoord"))
        self.Answer = params.get("Answer")
        self.ExpressionType = params.get("ExpressionType")


class ItemCoord(AbstractModel):
    """目標算式在圖片上的坐標訊息

    """

    def __init__(self):
        """
        :param Height: 算式高度
        :type Height: int
        :param Width: 算式寬度
        :type Width: int
        :param X: 算式圖的左上角橫坐標
        :type X: int
        :param Y: 算式圖的左上角縱坐標
        :type Y: int
        """
        self.Height = None
        self.Width = None
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.X = params.get("X")
        self.Y = params.get("Y")