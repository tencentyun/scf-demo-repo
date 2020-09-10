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


class AttachCamRoleRequest(AbstractModel):
    """AttachCamRole請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 服務器ID
        :type InstanceId: str
        :param RoleName: 角色名稱。
        :type RoleName: str
        """
        self.InstanceId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RoleName = params.get("RoleName")


class AttachCamRoleResponse(AbstractModel):
    """AttachCamRole返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindPsaTagRequest(AbstractModel):
    """BindPsaTag請求參數結構體

    """

    def __init__(self):
        """
        :param PsaId: 預授權規則ID
        :type PsaId: str
        :param TagKey: 需要綁定的标簽key
        :type TagKey: str
        :param TagValue: 需要綁定的标簽value
        :type TagValue: str
        """
        self.PsaId = None
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class BindPsaTagResponse(AbstractModel):
    """BindPsaTag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BuyDevicesRequest(AbstractModel):
    """BuyDevices請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區ID。通過介面[查詢地域以及可用區(DescribeRegions)](https://cloud.taifucloud.com/document/api/386/33564)獲取可用區訊息
        :type Zone: str
        :param OsTypeId: 佈署服務器的作業系統ID。通過介面[查詢作業系統訊息(DescribeOsInfo)](https://cloud.taifucloud.com/document/product/386/32902)獲取作業系統訊息
        :type OsTypeId: int
        :param RaidId: RAID類型ID。通過介面[查詢機型RAID方式以及系統盤大小(DescribeDeviceClassPartition)](https://cloud.taifucloud.com/document/api/386/32910)獲取RAID訊息
        :type RaidId: int
        :param GoodsCount: 購買數量
        :type GoodsCount: int
        :param VpcId: 購買至私有網絡ID
        :type VpcId: str
        :param SubnetId: 購買至子網ID
        :type SubnetId: str
        :param DeviceClassCode: 購買的機型ID。通過介面[查詢設備型号(DescribeDeviceClass)](https://cloud.taifucloud.com/document/api/386/32911)獲取機型訊息
        :type DeviceClassCode: str
        :param TimeUnit: 購買時長單位，取值：M(月) D(天)
        :type TimeUnit: str
        :param TimeSpan: 購買時長
        :type TimeSpan: int
        :param NeedSecurityAgent: 是否安裝安全Agent，取值：1(安裝) 0(不安裝)，預設取值0
        :type NeedSecurityAgent: int
        :param NeedMonitorAgent: 是否安裝監控Agent，取值：1(安裝) 0(不安裝)，預設取值0
        :type NeedMonitorAgent: int
        :param NeedEMRAgent: 是否安裝EMR Agent，取值：1(安裝) 0(不安裝)，預設取值0
        :type NeedEMRAgent: int
        :param NeedEMRSoftware: 是否安裝EMR軟體包，取值：1(安裝) 0(不安裝)，預設取值0
        :type NeedEMRSoftware: int
        :param ApplyEip: 是否分配彈性公網IP，取值：1(分配) 0(不分配)，預設取值0
        :type ApplyEip: int
        :param EipPayMode: 彈性公網IP計費模式，取值：Flow(按流量計費) Bandwidth(按頻寬計費)，預設取值Flow
        :type EipPayMode: str
        :param EipBandwidth: 彈性公網IP頻寬限制，單位Mb
        :type EipBandwidth: int
        :param IsZoning: 數據盤是否格式化，取值：1(格式化) 0(不格式化)，預設取值爲1
        :type IsZoning: int
        :param CpmPayMode: 物理機計費模式，取值：1(預付費) 2(後付費)，預設取值爲1
        :type CpmPayMode: int
        :param ImageId: 自定義映像ID，取值生效時用自定義映像佈署物理機
        :type ImageId: str
        :param Password: 設置Linux root或Windows Administrator的密碼
        :type Password: str
        :param AutoRenewFlag: 自動續約标志位，取值：1(自動續約) 0(不自動續約)，預設取值0
        :type AutoRenewFlag: int
        :param SysRootSpace: 系統盤根分區大小，單位爲G，預設取值10G。通過介面[查詢機型RAID方式以及系統盤大小(DescribeDeviceClassPartition)](https://cloud.taifucloud.com/document/api/386/32910)獲取根分區訊息
        :type SysRootSpace: int
        :param SysSwaporuefiSpace: 系統盤swap分區或/boot/efi分區的大小，單位爲G。若是uefi啓動的機器，分區爲/boot/efi，且此值是預設是2G。 普通機器爲swap分區，可以不指定此分區。 機型是否是uefi啓動，參見介面[查詢設備型号(DescribeDeviceClass)](https://cloud.taifucloud.com/document/api/386/32911)
        :type SysSwaporuefiSpace: int
        :param SysUsrlocalSpace: /usr/local分區大小，單位爲G
        :type SysUsrlocalSpace: int
        :param SysDataSpace: /data分區大小，單位爲G。如果系統盤還有剩餘大小，會分配給/data分區。（特殊情況：如果剩餘空間不足10G，并且沒有指定/data分區，則剩餘空間會分配給Root分區）
        :type SysDataSpace: int
        :param HyperThreading: 是否開啓超線程，取值：1(開啓) 0(關閉)，預設取值1
        :type HyperThreading: int
        :param LanIps: 指定的内網IP清單，不指定時自動分配
        :type LanIps: list of str
        :param Aliases: 設備名稱清單
        :type Aliases: list of str
        :param CpuId: CPU型号ID，自定義機型需要傳入，取值：
<br/><li>1: E5-2620v3 (6核) &#42; 2</li><li>2: E5-2680v4 (14核) &#42; 2</li><li>3: E5-2670v3 (12核) &#42; 2</li><li>4: E5-2620v4 (8核) &#42; 2</li><li>5: 4110 (8核) &#42; 2</li><li>6: 6133 (20核) &#42; 2</li><br/>
        :type CpuId: int
        :param ContainRaidCard: 是否有RAID卡，取值：1(有) 0(無)，自定義機型需要傳入
        :type ContainRaidCard: int
        :param MemSize: 内存大小，單位爲G，自定義機型需要傳入。取值參考介面[查詢自定義機型部件訊息(DescribeHardwareSpecification)](https://cloud.taifucloud.com/document/api/386/33565)返回值
        :type MemSize: int
        :param SystemDiskTypeId: 系統盤ID，自定義機型需要傳入。取值參考介面[查詢自定義機型部件訊息(DescribeHardwareSpecification)](https://cloud.taifucloud.com/document/api/386/33565)返回值
        :type SystemDiskTypeId: int
        :param SystemDiskCount: 系統盤數量，自定義機型需要傳入。取值參考介面[查詢自定義機型部件訊息(DescribeHardwareSpecification)](https://cloud.taifucloud.com/document/api/386/33565)返回值
        :type SystemDiskCount: int
        :param DataDiskTypeId: 數據盤ID，自定義機型需要傳入。取值參考介面[查詢自定義機型部件訊息(DescribeHardwareSpecification)](https://cloud.taifucloud.com/document/api/386/33565)返回值
        :type DataDiskTypeId: int
        :param DataDiskCount: 數據盤數量，自定義機型需要傳入。取值參考介面[查詢自定義機型部件訊息(DescribeHardwareSpecification)](https://cloud.taifucloud.com/document/api/386/33565)返回值
        :type DataDiskCount: int
        :param Tags: 綁定的标簽清單
        :type Tags: list of Tag
        :param FileSystem: 指定數據盤的文件系統格式，當前支援 EXT4和XFS選項， 預設爲EXT4。 參數适用于數據盤和Linux， 且在IsZoning爲1時生效
        :type FileSystem: str
        :param BuySession: 此參數是爲了防止重複發貨。如果兩次調用傳入相同的BuySession，只會發貨一次。 不要以設備别名作爲BuySession，這樣只會第一次購買成功。參數長度爲128位，合法字元爲大小字母，數字，下劃線，橫線。
        :type BuySession: str
        :param SgId: 綁定已有的安全組ID。僅在NeedSecurityAgent爲1時生效
        :type SgId: str
        :param TemplateId: 安全組範本ID，由範本創建新安全組并綁定。TemplateId和SgId不能同時傳入
        :type TemplateId: str
        """
        self.Zone = None
        self.OsTypeId = None
        self.RaidId = None
        self.GoodsCount = None
        self.VpcId = None
        self.SubnetId = None
        self.DeviceClassCode = None
        self.TimeUnit = None
        self.TimeSpan = None
        self.NeedSecurityAgent = None
        self.NeedMonitorAgent = None
        self.NeedEMRAgent = None
        self.NeedEMRSoftware = None
        self.ApplyEip = None
        self.EipPayMode = None
        self.EipBandwidth = None
        self.IsZoning = None
        self.CpmPayMode = None
        self.ImageId = None
        self.Password = None
        self.AutoRenewFlag = None
        self.SysRootSpace = None
        self.SysSwaporuefiSpace = None
        self.SysUsrlocalSpace = None
        self.SysDataSpace = None
        self.HyperThreading = None
        self.LanIps = None
        self.Aliases = None
        self.CpuId = None
        self.ContainRaidCard = None
        self.MemSize = None
        self.SystemDiskTypeId = None
        self.SystemDiskCount = None
        self.DataDiskTypeId = None
        self.DataDiskCount = None
        self.Tags = None
        self.FileSystem = None
        self.BuySession = None
        self.SgId = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.OsTypeId = params.get("OsTypeId")
        self.RaidId = params.get("RaidId")
        self.GoodsCount = params.get("GoodsCount")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")
        self.NeedSecurityAgent = params.get("NeedSecurityAgent")
        self.NeedMonitorAgent = params.get("NeedMonitorAgent")
        self.NeedEMRAgent = params.get("NeedEMRAgent")
        self.NeedEMRSoftware = params.get("NeedEMRSoftware")
        self.ApplyEip = params.get("ApplyEip")
        self.EipPayMode = params.get("EipPayMode")
        self.EipBandwidth = params.get("EipBandwidth")
        self.IsZoning = params.get("IsZoning")
        self.CpmPayMode = params.get("CpmPayMode")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.SysRootSpace = params.get("SysRootSpace")
        self.SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self.SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self.SysDataSpace = params.get("SysDataSpace")
        self.HyperThreading = params.get("HyperThreading")
        self.LanIps = params.get("LanIps")
        self.Aliases = params.get("Aliases")
        self.CpuId = params.get("CpuId")
        self.ContainRaidCard = params.get("ContainRaidCard")
        self.MemSize = params.get("MemSize")
        self.SystemDiskTypeId = params.get("SystemDiskTypeId")
        self.SystemDiskCount = params.get("SystemDiskCount")
        self.DataDiskTypeId = params.get("DataDiskTypeId")
        self.DataDiskCount = params.get("DataDiskCount")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.FileSystem = params.get("FileSystem")
        self.BuySession = params.get("BuySession")
        self.SgId = params.get("SgId")
        self.TemplateId = params.get("TemplateId")


class BuyDevicesResponse(AbstractModel):
    """BuyDevices返回參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 購買的物理機實例ID清單
        :type InstanceIds: list of str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.InstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.RequestId = params.get("RequestId")


class CpuInfo(AbstractModel):
    """cpu訊息

    """

    def __init__(self):
        """
        :param CpuId: CPU的ID
        :type CpuId: int
        :param CpuDescription: CPU型号描述
        :type CpuDescription: str
        :param Series: 機型序列
        :type Series: int
        :param ContainRaidCard: 支援的RAID方式，0：有RAID卡，1：沒有RAID卡
        :type ContainRaidCard: list of int non-negative
        """
        self.CpuId = None
        self.CpuDescription = None
        self.Series = None
        self.ContainRaidCard = None


    def _deserialize(self, params):
        self.CpuId = params.get("CpuId")
        self.CpuDescription = params.get("CpuDescription")
        self.Series = params.get("Series")
        self.ContainRaidCard = params.get("ContainRaidCard")


class CreateCustomImageRequest(AbstractModel):
    """CreateCustomImage請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 用于制作映像的物理機ID
        :type InstanceId: str
        :param ImageName: 映像别名
        :type ImageName: str
        :param ImageDescription: 映像描述
        :type ImageDescription: str
        """
        self.InstanceId = None
        self.ImageName = None
        self.ImageDescription = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")


class CreateCustomImageResponse(AbstractModel):
    """CreateCustomImage返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 黑石異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreatePsaRegulationRequest(AbstractModel):
    """CreatePsaRegulation請求參數結構體

    """

    def __init__(self):
        """
        :param PsaName: 規則别名
        :type PsaName: str
        :param TaskTypeIds: 關聯的故障類型ID清單
        :type TaskTypeIds: list of int non-negative
        :param RepairLimit: 維修實例上限，預設爲5
        :type RepairLimit: int
        :param PsaDescription: 規則備注
        :type PsaDescription: str
        """
        self.PsaName = None
        self.TaskTypeIds = None
        self.RepairLimit = None
        self.PsaDescription = None


    def _deserialize(self, params):
        self.PsaName = params.get("PsaName")
        self.TaskTypeIds = params.get("TaskTypeIds")
        self.RepairLimit = params.get("RepairLimit")
        self.PsaDescription = params.get("PsaDescription")


class CreatePsaRegulationResponse(AbstractModel):
    """CreatePsaRegulation返回參數結構體

    """

    def __init__(self):
        """
        :param PsaId: 創建的預授權規則ID
        :type PsaId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.PsaId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.RequestId = params.get("RequestId")


class CreateSpotDeviceRequest(AbstractModel):
    """CreateSpotDevice請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區名稱。如ap-guangzhou-bls-1, 通過DescribeRegions獲取
        :type Zone: str
        :param ComputeType: 計算單元類型, 如v3.c2.medium，更詳細的ComputeType參考[競價實例産品文件](https://cloud.taifucloud.com/document/product/386/30256)
        :type ComputeType: str
        :param OsTypeId: 作業系統類型ID
        :type OsTypeId: int
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param GoodsNum: 購買的計算單元個數
        :type GoodsNum: int
        :param SpotStrategy: 出價策略。可取值爲SpotWithPriceLimit和SpotAsPriceGo。SpotWithPriceLimit，用戶設置價格上限，需要傳SpotPriceLimit參數， 如果市場價高于用戶的指定價格，則購買不成功;  SpotAsPriceGo 是随市場價的策略。
        :type SpotStrategy: str
        :param SpotPriceLimit: 用戶設置的價格。當爲SpotWithPriceLimit競價策略時有效
        :type SpotPriceLimit: float
        :param Passwd: 設置競價實例密碼。可選參數，沒有指定會生成随機密碼
        :type Passwd: str
        """
        self.Zone = None
        self.ComputeType = None
        self.OsTypeId = None
        self.VpcId = None
        self.SubnetId = None
        self.GoodsNum = None
        self.SpotStrategy = None
        self.SpotPriceLimit = None
        self.Passwd = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ComputeType = params.get("ComputeType")
        self.OsTypeId = params.get("OsTypeId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.GoodsNum = params.get("GoodsNum")
        self.SpotStrategy = params.get("SpotStrategy")
        self.SpotPriceLimit = params.get("SpotPriceLimit")
        self.Passwd = params.get("Passwd")


class CreateSpotDeviceResponse(AbstractModel):
    """CreateSpotDevice返回參數結構體

    """

    def __init__(self):
        """
        :param ResourceIds: 創建的服務器ID
        :type ResourceIds: list of str
        :param FlowId: 任務ID
        :type FlowId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.ResourceIds = None
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateUserCmdRequest(AbstractModel):
    """CreateUserCmd請求參數結構體

    """

    def __init__(self):
        """
        :param Alias: 用戶自定義腳本的名稱
        :type Alias: str
        :param OsType: 命令适用的作業系統類型，取值linux或xserver
        :type OsType: str
        :param Content: 腳本内容，必須經過base64編碼
        :type Content: str
        """
        self.Alias = None
        self.OsType = None
        self.Content = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.OsType = params.get("OsType")
        self.Content = params.get("Content")


class CreateUserCmdResponse(AbstractModel):
    """CreateUserCmd返回參數結構體

    """

    def __init__(self):
        """
        :param CmdId: 腳本ID
        :type CmdId: str
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CmdId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CmdId = params.get("CmdId")
        self.RequestId = params.get("RequestId")


class CustomImage(AbstractModel):
    """自定義映像訊息

    """

    def __init__(self):
        """
        :param ImageId: 映像ID
        :type ImageId: str
        :param ImageName: 映像别名
        :type ImageName: str
        :param ImageStatus: 映像狀态碼
        :type ImageStatus: int
        :param OsClass: 映像OS名
        :type OsClass: str
        :param OsVersion: 映像OS版本
        :type OsVersion: str
        :param OsBit: OS是64還是32位
        :type OsBit: int
        :param ImageSize: 映像大小(M)
        :type ImageSize: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param PartitionInfoSet: 分區訊息
        :type PartitionInfoSet: list of PartitionInfo
        :param DeviceClassCode: 适用機型
        :type DeviceClassCode: str
        :param ImageDescription: 備注
        :type ImageDescription: str
        :param OsTypeId: 原始映像id
        :type OsTypeId: int
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageStatus = None
        self.OsClass = None
        self.OsVersion = None
        self.OsBit = None
        self.ImageSize = None
        self.CreateTime = None
        self.PartitionInfoSet = None
        self.DeviceClassCode = None
        self.ImageDescription = None
        self.OsTypeId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageStatus = params.get("ImageStatus")
        self.OsClass = params.get("OsClass")
        self.OsVersion = params.get("OsVersion")
        self.OsBit = params.get("OsBit")
        self.ImageSize = params.get("ImageSize")
        self.CreateTime = params.get("CreateTime")
        if params.get("PartitionInfoSet") is not None:
            self.PartitionInfoSet = []
            for item in params.get("PartitionInfoSet"):
                obj = PartitionInfo()
                obj._deserialize(item)
                self.PartitionInfoSet.append(obj)
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.ImageDescription = params.get("ImageDescription")
        self.OsTypeId = params.get("OsTypeId")


class CustomImageProcess(AbstractModel):
    """映像制作進度清單

    """

    def __init__(self):
        """
        :param StepName: 步驟
        :type StepName: str
        :param StartTime: 此步驟開始時間
        :type StartTime: str
        :param StepType: 0: 已完成 1: 當前進行 2: 未開始
        :type StepType: int
        """
        self.StepName = None
        self.StartTime = None
        self.StepType = None


    def _deserialize(self, params):
        self.StepName = params.get("StepName")
        self.StartTime = params.get("StartTime")
        self.StepType = params.get("StepType")


class DeleteCustomImagesRequest(AbstractModel):
    """DeleteCustomImages請求參數結構體

    """

    def __init__(self):
        """
        :param ImageIds: 準備删除的映像ID清單
        :type ImageIds: list of str
        """
        self.ImageIds = None


    def _deserialize(self, params):
        self.ImageIds = params.get("ImageIds")


class DeleteCustomImagesResponse(AbstractModel):
    """DeleteCustomImages返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 黑石異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeletePsaRegulationRequest(AbstractModel):
    """DeletePsaRegulation請求參數結構體

    """

    def __init__(self):
        """
        :param PsaId: 預授權規則ID
        :type PsaId: str
        """
        self.PsaId = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")


class DeletePsaRegulationResponse(AbstractModel):
    """DeletePsaRegulation返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteUserCmdsRequest(AbstractModel):
    """DeleteUserCmds請求參數結構體

    """

    def __init__(self):
        """
        :param CmdIds: 需要删除的腳本ID
        :type CmdIds: list of str
        """
        self.CmdIds = None


    def _deserialize(self, params):
        self.CmdIds = params.get("CmdIds")


class DeleteUserCmdsResponse(AbstractModel):
    """DeleteUserCmds返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCustomImageProcessRequest(AbstractModel):
    """DescribeCustomImageProcess請求參數結構體

    """

    def __init__(self):
        """
        :param ImageId: 映像ID
        :type ImageId: str
        """
        self.ImageId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")


class DescribeCustomImageProcessResponse(AbstractModel):
    """DescribeCustomImageProcess返回參數結構體

    """

    def __init__(self):
        """
        :param CustomImageProcessSet: 映像制作進度
        :type CustomImageProcessSet: list of CustomImageProcess
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CustomImageProcessSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomImageProcessSet") is not None:
            self.CustomImageProcessSet = []
            for item in params.get("CustomImageProcessSet"):
                obj = CustomImageProcess()
                obj._deserialize(item)
                self.CustomImageProcessSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomImagesRequest(AbstractModel):
    """DescribeCustomImages請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 數量限制
        :type Limit: int
        :param OrderField: 排序欄位，僅支援CreateTime
        :type OrderField: str
        :param Order: 排序方式 0:遞增(預設) 1:遞減
        :type Order: int
        :param ImageId: 按ImageId查找指定映像訊息，ImageId欄位存在時其他欄位失效
        :type ImageId: str
        :param SearchKey: 模糊查詢過濾，可以查詢映像ID或映像名
        :type SearchKey: str
        :param ImageStatus: <ul>
映像狀态過濾清單，有效取值爲：
<li>1：制作中</li>
<li>2：制作失敗</li>
<li>3：正常</li>
<li>4：删除中</li>
</ul>
        :type ImageStatus: list of int non-negative
        """
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.ImageId = None
        self.SearchKey = None
        self.ImageStatus = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.ImageId = params.get("ImageId")
        self.SearchKey = params.get("SearchKey")
        self.ImageStatus = params.get("ImageStatus")


class DescribeCustomImagesResponse(AbstractModel):
    """DescribeCustomImages返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回映像數量
        :type TotalCount: int
        :param CustomImageSet: 映像訊息清單
        :type CustomImageSet: list of CustomImage
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CustomImageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CustomImageSet") is not None:
            self.CustomImageSet = []
            for item in params.get("CustomImageSet"):
                obj = CustomImage()
                obj._deserialize(item)
                self.CustomImageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceClassPartitionRequest(AbstractModel):
    """DescribeDeviceClassPartition請求參數結構體

    """

    def __init__(self):
        """
        :param DeviceClassCode: 設備類型代号。代号通過介面[查詢設備型号(DescribeDeviceClass)](https://cloud.taifucloud.com/document/api/386/32911)查詢。标準機型需要傳入此參數。雖是可選參數，但DeviceClassCode和InstanceId參數，必須要填寫一個。
        :type DeviceClassCode: str
        :param InstanceId: 需要查詢自定義機型RAID訊息時，傳入自定義機型實例ID。InstanceId存在時其餘參數失效。
        :type InstanceId: str
        :param CpuId: CPU型号ID，查詢自定義機型時需要傳入
        :type CpuId: int
        :param MemSize: 内存大小，單位爲G，查詢自定義機型時需要傳入
        :type MemSize: int
        :param ContainRaidCard: 是否有RAID卡，取值：1(有) 0(無)。查詢自定義機型時需要傳入
        :type ContainRaidCard: int
        :param SystemDiskTypeId: 系統盤類型ID，查詢自定義機型時需要傳入
        :type SystemDiskTypeId: int
        :param SystemDiskCount: 系統盤數量，查詢自定義機型時需要傳入
        :type SystemDiskCount: int
        :param DataDiskTypeId: 數據盤類型ID，查詢自定義機型時可傳入
        :type DataDiskTypeId: int
        :param DataDiskCount: 數據盤數量，查詢自定義機型時可傳入
        :type DataDiskCount: int
        """
        self.DeviceClassCode = None
        self.InstanceId = None
        self.CpuId = None
        self.MemSize = None
        self.ContainRaidCard = None
        self.SystemDiskTypeId = None
        self.SystemDiskCount = None
        self.DataDiskTypeId = None
        self.DataDiskCount = None


    def _deserialize(self, params):
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.InstanceId = params.get("InstanceId")
        self.CpuId = params.get("CpuId")
        self.MemSize = params.get("MemSize")
        self.ContainRaidCard = params.get("ContainRaidCard")
        self.SystemDiskTypeId = params.get("SystemDiskTypeId")
        self.SystemDiskCount = params.get("SystemDiskCount")
        self.DataDiskTypeId = params.get("DataDiskTypeId")
        self.DataDiskCount = params.get("DataDiskCount")


class DescribeDeviceClassPartitionResponse(AbstractModel):
    """DescribeDeviceClassPartition返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceClassPartitionInfoSet: 支援的RAID格式清單
        :type DeviceClassPartitionInfoSet: list of DeviceClassPartitionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceClassPartitionInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceClassPartitionInfoSet") is not None:
            self.DeviceClassPartitionInfoSet = []
            for item in params.get("DeviceClassPartitionInfoSet"):
                obj = DeviceClassPartitionInfo()
                obj._deserialize(item)
                self.DeviceClassPartitionInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceClassRequest(AbstractModel):
    """DescribeDeviceClass請求參數結構體

    """

    def __init__(self):
        """
        :param OnSale: 是否僅查詢在售标準機型配置訊息。取值0：查詢所有機型；1：查詢在售機型。預設爲1
        :type OnSale: int
        :param NeedPriceInfo: 是否返回價格訊息。取值0：不返回價格訊息，介面返回速度更快；1：返回價格訊息。預設爲1
        :type NeedPriceInfo: int
        """
        self.OnSale = None
        self.NeedPriceInfo = None


    def _deserialize(self, params):
        self.OnSale = params.get("OnSale")
        self.NeedPriceInfo = params.get("NeedPriceInfo")


class DescribeDeviceClassResponse(AbstractModel):
    """DescribeDeviceClass返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceClassSet: 物理機設備類型清單
        :type DeviceClassSet: list of DeviceClass
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceClassSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceClassSet") is not None:
            self.DeviceClassSet = []
            for item in params.get("DeviceClassSet"):
                obj = DeviceClass()
                obj._deserialize(item)
                self.DeviceClassSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceHardwareInfoRequest(AbstractModel):
    """DescribeDeviceHardwareInfo請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 設備 ID 清單
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class DescribeDeviceHardwareInfoResponse(AbstractModel):
    """DescribeDeviceHardwareInfo返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceHardwareInfoSet: 設備硬體配置訊息
        :type DeviceHardwareInfoSet: list of DeviceHardwareInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceHardwareInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceHardwareInfoSet") is not None:
            self.DeviceHardwareInfoSet = []
            for item in params.get("DeviceHardwareInfoSet"):
                obj = DeviceHardwareInfo()
                obj._deserialize(item)
                self.DeviceHardwareInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeviceInventoryRequest(AbstractModel):
    """DescribeDeviceInventory請求參數結構體

    """

    def __init__(self):
        """
        :param Zone: 可用區
        :type Zone: str
        :param DeviceClassCode: 設備型号
        :type DeviceClassCode: str
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param CpuId: CPU型号ID，查詢自定義機型時必填
        :type CpuId: int
        :param MemSize: 内存大小，單位爲G，查詢自定義機型時必填
        :type MemSize: int
        :param ContainRaidCard: 是否有RAID卡，取值：1(有) 0(無)，查詢自定義機型時必填
        :type ContainRaidCard: int
        :param SystemDiskTypeId: 系統盤類型ID，查詢自定義機型時必填
        :type SystemDiskTypeId: int
        :param SystemDiskCount: 系統盤數量，查詢自定義機型時必填
        :type SystemDiskCount: int
        :param DataDiskTypeId: 數據盤類型ID，查詢自定義機型時可填
        :type DataDiskTypeId: int
        :param DataDiskCount: 數據盤數量，查詢自定義機型時可填
        :type DataDiskCount: int
        """
        self.Zone = None
        self.DeviceClassCode = None
        self.VpcId = None
        self.SubnetId = None
        self.CpuId = None
        self.MemSize = None
        self.ContainRaidCard = None
        self.SystemDiskTypeId = None
        self.SystemDiskCount = None
        self.DataDiskTypeId = None
        self.DataDiskCount = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CpuId = params.get("CpuId")
        self.MemSize = params.get("MemSize")
        self.ContainRaidCard = params.get("ContainRaidCard")
        self.SystemDiskTypeId = params.get("SystemDiskTypeId")
        self.SystemDiskCount = params.get("SystemDiskCount")
        self.DataDiskTypeId = params.get("DataDiskTypeId")
        self.DataDiskCount = params.get("DataDiskCount")


class DescribeDeviceInventoryResponse(AbstractModel):
    """DescribeDeviceInventory返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceCount: 庫存設備數量
        :type DeviceCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeviceCount = params.get("DeviceCount")
        self.RequestId = params.get("RequestId")


class DescribeDeviceOperationLogRequest(AbstractModel):
    """DescribeDeviceOperationLog請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 設備實例ID
        :type InstanceId: str
        :param StartTime: 查詢開始日期
        :type StartTime: str
        :param EndTime: 查詢結束日期
        :type EndTime: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDeviceOperationLogResponse(AbstractModel):
    """DescribeDeviceOperationLog返回參數結構體

    """

    def __init__(self):
        """
        :param DeviceOperationLogSet: 操作日志清單
        :type DeviceOperationLogSet: list of DeviceOperationLog
        :param TotalCount: 返回數目
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DeviceOperationLogSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceOperationLogSet") is not None:
            self.DeviceOperationLogSet = []
            for item in params.get("DeviceOperationLogSet"):
                obj = DeviceOperationLog()
                obj._deserialize(item)
                self.DeviceOperationLogSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDevicePartitionRequest(AbstractModel):
    """DescribeDevicePartition請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 物理機ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDevicePartitionResponse(AbstractModel):
    """DescribeDevicePartition返回參數結構體

    """

    def __init__(self):
        """
        :param DevicePartition: 物理機分區格式
        :type DevicePartition: :class:`taifucloudcloud.bm.v20180423.models.DevicePartition`
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DevicePartition = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DevicePartition") is not None:
            self.DevicePartition = DevicePartition()
            self.DevicePartition._deserialize(params.get("DevicePartition"))
        self.RequestId = params.get("RequestId")


class DescribeDevicePositionRequest(AbstractModel):
    """DescribeDevicePosition請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 數量限制
        :type Limit: int
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param InstanceIds: 實例ID清單
        :type InstanceIds: list of str
        :param Alias: 實例别名
        :type Alias: str
        """
        self.Offset = None
        self.Limit = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceIds = None
        self.Alias = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceIds = params.get("InstanceIds")
        self.Alias = params.get("Alias")


class DescribeDevicePositionResponse(AbstractModel):
    """DescribeDevicePosition返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回數量
        :type TotalCount: int
        :param DevicePositionInfoSet: 設備所在機架訊息
        :type DevicePositionInfoSet: list of DevicePositionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DevicePositionInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DevicePositionInfoSet") is not None:
            self.DevicePositionInfoSet = []
            for item in params.get("DevicePositionInfoSet"):
                obj = DevicePositionInfo()
                obj._deserialize(item)
                self.DevicePositionInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDevicePriceInfoRequest(AbstractModel):
    """DescribeDevicePriceInfo請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 需要查詢的實例清單
        :type InstanceIds: list of str
        :param TimeUnit: 購買時長單位，當前只支援取值爲m
        :type TimeUnit: str
        :param TimeSpan: 購買時長
        :type TimeSpan: int
        """
        self.InstanceIds = None
        self.TimeUnit = None
        self.TimeSpan = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.TimeUnit = params.get("TimeUnit")
        self.TimeSpan = params.get("TimeSpan")


class DescribeDevicePriceInfoResponse(AbstractModel):
    """DescribeDevicePriceInfo返回參數結構體

    """

    def __init__(self):
        """
        :param DevicePriceInfoSet: 服務器價格訊息清單
        :type DevicePriceInfoSet: list of DevicePriceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.DevicePriceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DevicePriceInfoSet") is not None:
            self.DevicePriceInfoSet = []
            for item in params.get("DevicePriceInfoSet"):
                obj = DevicePriceInfo()
                obj._deserialize(item)
                self.DevicePriceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回數量
        :type Limit: int
        :param DeviceClassCode: 機型ID，通過介面[查詢設備型号(DescribeDeviceClass)](https://cloud.taifucloud.com/document/api/386/32911)查詢
        :type DeviceClassCode: str
        :param InstanceIds: 設備ID數組
        :type InstanceIds: list of str
        :param WanIps: 外網IP數組
        :type WanIps: list of str
        :param LanIps: 内網IP數組
        :type LanIps: list of str
        :param Alias: 設備名稱
        :type Alias: str
        :param VagueIp: 模糊IP查詢
        :type VagueIp: str
        :param DeadlineStartTime: 設備到期時間查詢的起始時間
        :type DeadlineStartTime: str
        :param DeadlineEndTime: 設備到期時間查詢的結束時間
        :type DeadlineEndTime: str
        :param AutoRenewFlag: 自動續約标志 0:不自動續約，1:自動續約
        :type AutoRenewFlag: int
        :param VpcId: 私有網絡唯一ID
        :type VpcId: str
        :param SubnetId: 子網唯一ID
        :type SubnetId: str
        :param Tags: 标簽清單
        :type Tags: list of Tag
        :param DeviceType: 設備類型，取值有: compute(計算型), standard(标準型), storage(儲存型) 等
        :type DeviceType: str
        :param IsLuckyDevice: 競價實例機器的過濾。如果未指定此參數，則不做過濾。0: 查詢非競價實例的機器; 1: 查詢競價實例的機器。
        :type IsLuckyDevice: int
        :param OrderField: 排序欄位
        :type OrderField: str
        :param Order: 排序方式，取值：0:增序(預設)，1:降序
        :type Order: int
        """
        self.Offset = None
        self.Limit = None
        self.DeviceClassCode = None
        self.InstanceIds = None
        self.WanIps = None
        self.LanIps = None
        self.Alias = None
        self.VagueIp = None
        self.DeadlineStartTime = None
        self.DeadlineEndTime = None
        self.AutoRenewFlag = None
        self.VpcId = None
        self.SubnetId = None
        self.Tags = None
        self.DeviceType = None
        self.IsLuckyDevice = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.InstanceIds = params.get("InstanceIds")
        self.WanIps = params.get("WanIps")
        self.LanIps = params.get("LanIps")
        self.Alias = params.get("Alias")
        self.VagueIp = params.get("VagueIp")
        self.DeadlineStartTime = params.get("DeadlineStartTime")
        self.DeadlineEndTime = params.get("DeadlineEndTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeviceType = params.get("DeviceType")
        self.IsLuckyDevice = params.get("IsLuckyDevice")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回數量
        :type TotalCount: int
        :param DeviceInfoSet: 物理機訊息清單
        :type DeviceInfoSet: list of DeviceInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeviceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeviceInfoSet") is not None:
            self.DeviceInfoSet = []
            for item in params.get("DeviceInfoSet"):
                obj = DeviceInfo()
                obj._deserialize(item)
                self.DeviceInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHardwareSpecificationRequest(AbstractModel):
    """DescribeHardwareSpecification請求參數結構體

    """


class DescribeHardwareSpecificationResponse(AbstractModel):
    """DescribeHardwareSpecification返回參數結構體

    """

    def __init__(self):
        """
        :param CpuInfoSet: CPU型号清單
        :type CpuInfoSet: list of CpuInfo
        :param MemSet: 内存的取值，單位爲G
        :type MemSet: list of int non-negative
        :param DiskInfoSet: 硬碟型号清單
        :type DiskInfoSet: list of DiskInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.CpuInfoSet = None
        self.MemSet = None
        self.DiskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CpuInfoSet") is not None:
            self.CpuInfoSet = []
            for item in params.get("CpuInfoSet"):
                obj = CpuInfo()
                obj._deserialize(item)
                self.CpuInfoSet.append(obj)
        self.MemSet = params.get("MemSet")
        if params.get("DiskInfoSet") is not None:
            self.DiskInfoSet = []
            for item in params.get("DiskInfoSet"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DiskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostedDeviceOutBandInfoRequest(AbstractModel):
    """DescribeHostedDeviceOutBandInfo請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 托管設備的唯一ID數組,數組個數不超過20
        :type InstanceIds: list of str
        :param Zone: 可用區ID
        :type Zone: str
        """
        self.InstanceIds = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Zone = params.get("Zone")


class DescribeHostedDeviceOutBandInfoResponse(AbstractModel):
    """DescribeHostedDeviceOutBandInfo返回參數結構體

    """

    def __init__(self):
        """
        :param HostedDeviceOutBandInfoSet: 托管設備帶外訊息
        :type HostedDeviceOutBandInfoSet: list of HostedDeviceOutBandInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.HostedDeviceOutBandInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HostedDeviceOutBandInfoSet") is not None:
            self.HostedDeviceOutBandInfoSet = []
            for item in params.get("HostedDeviceOutBandInfoSet"):
                obj = HostedDeviceOutBandInfo()
                obj._deserialize(item)
                self.HostedDeviceOutBandInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOperationResultRequest(AbstractModel):
    """DescribeOperationResult請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeOperationResultResponse(AbstractModel):
    """DescribeOperationResult返回參數結構體

    """

    def __init__(self):
        """
        :param TaskStatus: 任務的整體狀态，取值如下：<br>
1：成功<br>
2：失敗<br>
3：部分成功，部分失敗<br>
4：未完成<br>
5：部分成功，部分未完成<br>
6：部分未完成，部分失敗<br>
7：部分未完成，部分失敗，部分成功
        :type TaskStatus: int
        :param SubtaskStatusSet: 各實例對應任務的狀态ID
        :type SubtaskStatusSet: list of SubtaskStatus
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskStatus = None
        self.SubtaskStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskStatus = params.get("TaskStatus")
        if params.get("SubtaskStatusSet") is not None:
            self.SubtaskStatusSet = []
            for item in params.get("SubtaskStatusSet"):
                obj = SubtaskStatus()
                obj._deserialize(item)
                self.SubtaskStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOsInfoRequest(AbstractModel):
    """DescribeOsInfo請求參數結構體

    """

    def __init__(self):
        """
        :param DeviceClassCode: 設備類型代号。 可以從DescribeDeviceClass查詢設備類型清單
        :type DeviceClassCode: str
        """
        self.DeviceClassCode = None


    def _deserialize(self, params):
        self.DeviceClassCode = params.get("DeviceClassCode")


class DescribeOsInfoResponse(AbstractModel):
    """DescribeOsInfo返回參數結構體

    """

    def __init__(self):
        """
        :param OsInfoSet: 作業系統訊息清單
        :type OsInfoSet: list of OsInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.OsInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OsInfoSet") is not None:
            self.OsInfoSet = []
            for item in params.get("OsInfoSet"):
                obj = OsInfo()
                obj._deserialize(item)
                self.OsInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePsaRegulationsRequest(AbstractModel):
    """DescribePsaRegulations請求參數結構體

    """

    def __init__(self):
        """
        :param Limit: 數量限制
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param PsaIds: 規則ID過濾，支援模糊查詢
        :type PsaIds: list of str
        :param PsaNames: 規則别名過濾，支援模糊查詢
        :type PsaNames: list of str
        :param Tags: 标簽過濾
        :type Tags: list of Tag
        :param OrderField: 排序欄位，取值支援：CreateTime
        :type OrderField: str
        :param Order: 排序方式 0:遞增(預設) 1:遞減
        :type Order: int
        """
        self.Limit = None
        self.Offset = None
        self.PsaIds = None
        self.PsaNames = None
        self.Tags = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.PsaIds = params.get("PsaIds")
        self.PsaNames = params.get("PsaNames")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")


class DescribePsaRegulationsResponse(AbstractModel):
    """DescribePsaRegulations返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回規則數量
        :type TotalCount: int
        :param PsaRegulations: 返回規則清單
        :type PsaRegulations: list of PsaRegulation
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.PsaRegulations = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PsaRegulations") is not None:
            self.PsaRegulations = []
            for item in params.get("PsaRegulations"):
                obj = PsaRegulation()
                obj._deserialize(item)
                self.PsaRegulations.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions請求參數結構體

    """

    def __init__(self):
        """
        :param RegionId: 地域整型ID，目前黑石可用地域包括：8- ，4- ，1- ， 19- 
        :type RegionId: int
        """
        self.RegionId = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回參數結構體

    """

    def __init__(self):
        """
        :param RegionInfoSet: 地域訊息
        :type RegionInfoSet: list of RegionInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RegionInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionInfoSet") is not None:
            self.RegionInfoSet = []
            for item in params.get("RegionInfoSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.RegionInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRepairTaskConstantRequest(AbstractModel):
    """DescribeRepairTaskConstant請求參數結構體

    """


class DescribeRepairTaskConstantResponse(AbstractModel):
    """DescribeRepairTaskConstant返回參數結構體

    """

    def __init__(self):
        """
        :param TaskTypeSet: 故障類型ID與對應中文名清單
        :type TaskTypeSet: list of TaskType
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskTypeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskTypeSet") is not None:
            self.TaskTypeSet = []
            for item in params.get("TaskTypeSet"):
                obj = TaskType()
                obj._deserialize(item)
                self.TaskTypeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 開始位置
        :type Offset: int
        :param Limit: 數據條數
        :type Limit: int
        :param StartDate: 時間過濾下限
        :type StartDate: str
        :param EndDate: 時間過濾上限
        :type EndDate: str
        :param TaskStatus: 任務狀态ID過濾
        :type TaskStatus: list of int non-negative
        :param OrderField: 排序欄位，目前支援：CreateTime，AuthTime，EndTime
        :type OrderField: str
        :param Order: 排序方式 0:遞增(預設) 1:遞減
        :type Order: int
        :param TaskIds: 任務ID過濾
        :type TaskIds: list of str
        :param InstanceIds: 實例ID過濾
        :type InstanceIds: list of str
        :param Aliases: 實例别名過濾
        :type Aliases: list of str
        :param TaskTypeIds: 故障類型ID過濾
        :type TaskTypeIds: list of int non-negative
        """
        self.Offset = None
        self.Limit = None
        self.StartDate = None
        self.EndDate = None
        self.TaskStatus = None
        self.OrderField = None
        self.Order = None
        self.TaskIds = None
        self.InstanceIds = None
        self.Aliases = None
        self.TaskTypeIds = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.TaskStatus = params.get("TaskStatus")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.TaskIds = params.get("TaskIds")
        self.InstanceIds = params.get("InstanceIds")
        self.Aliases = params.get("Aliases")
        self.TaskTypeIds = params.get("TaskTypeIds")


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回任務總數量
        :type TotalCount: int
        :param TaskInfoSet: 任務訊息清單
        :type TaskInfoSet: list of TaskInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TaskInfoSet") is not None:
            self.TaskInfoSet = []
            for item in params.get("TaskInfoSet"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.TaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskOperationLogRequest(AbstractModel):
    """DescribeTaskOperationLog請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 維修任務ID
        :type TaskId: str
        :param OrderField: 排序欄位，目前支援：OperationTime
        :type OrderField: str
        :param Order: 排序方式 0:遞增(預設) 1:遞減
        :type Order: int
        """
        self.TaskId = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")


class DescribeTaskOperationLogResponse(AbstractModel):
    """DescribeTaskOperationLog返回參數結構體

    """

    def __init__(self):
        """
        :param TaskOperationLogSet: 操作日志
        :type TaskOperationLogSet: list of TaskOperationLog
        :param TotalCount: 日志條數
        :type TotalCount: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskOperationLogSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskOperationLogSet") is not None:
            self.TaskOperationLogSet = []
            for item in params.get("TaskOperationLogSet"):
                obj = TaskOperationLog()
                obj._deserialize(item)
                self.TaskOperationLogSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeUserCmdTaskInfoRequest(AbstractModel):
    """DescribeUserCmdTaskInfo請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 數量限制
        :type Limit: int
        :param OrderField: 排序欄位，支援： RunBeginTime,RunEndTime,Status
        :type OrderField: str
        :param Order: 排序方式，取值: 1倒序，0順序；預設倒序
        :type Order: int
        :param SearchKey: 關鍵字搜索，可搜索ID或别名，支援模糊搜索
        :type SearchKey: str
        """
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.SearchKey = params.get("SearchKey")


class DescribeUserCmdTaskInfoResponse(AbstractModel):
    """DescribeUserCmdTaskInfo返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回數量
        :type TotalCount: int
        :param UserCmdTaskInfoSet: 自定義腳本任務詳細訊息清單
        :type UserCmdTaskInfoSet: list of UserCmdTaskInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserCmdTaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserCmdTaskInfoSet") is not None:
            self.UserCmdTaskInfoSet = []
            for item in params.get("UserCmdTaskInfoSet"):
                obj = UserCmdTaskInfo()
                obj._deserialize(item)
                self.UserCmdTaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserCmdTasksRequest(AbstractModel):
    """DescribeUserCmdTasks請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 數量限制
        :type Limit: int
        :param OrderField: 排序欄位，支援： RunBeginTime,RunEndTime,InstanceCount,SuccessCount,FailureCount
        :type OrderField: str
        :param Order: 排序方式，取值: 1倒序，0順序；預設倒序
        :type Order: int
        """
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")


class DescribeUserCmdTasksResponse(AbstractModel):
    """DescribeUserCmdTasks返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 腳本任務訊息數量
        :type TotalCount: int
        :param UserCmdTasks: 腳本任務訊息清單
        :type UserCmdTasks: list of UserCmdTask
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserCmdTasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserCmdTasks") is not None:
            self.UserCmdTasks = []
            for item in params.get("UserCmdTasks"):
                obj = UserCmdTask()
                obj._deserialize(item)
                self.UserCmdTasks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUserCmdsRequest(AbstractModel):
    """DescribeUserCmds請求參數結構體

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 數量限制
        :type Limit: int
        :param OrderField: 排序欄位，支援： OsType,CreateTime,ModifyTime
        :type OrderField: str
        :param Order: 排序方式，取值: 1倒序，0順序；預設倒序
        :type Order: int
        :param SearchKey: 關鍵字搜索，可搜索ID或别名，支援模糊搜索
        :type SearchKey: str
        :param CmdId: 查詢的腳本ID
        :type CmdId: str
        """
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.Order = None
        self.SearchKey = None
        self.CmdId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.Order = params.get("Order")
        self.SearchKey = params.get("SearchKey")
        self.CmdId = params.get("CmdId")


class DescribeUserCmdsResponse(AbstractModel):
    """DescribeUserCmds返回參數結構體

    """

    def __init__(self):
        """
        :param TotalCount: 返回數量
        :type TotalCount: int
        :param UserCmds: 腳本訊息清單
        :type UserCmds: list of UserCmd
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.UserCmds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UserCmds") is not None:
            self.UserCmds = []
            for item in params.get("UserCmds"):
                obj = UserCmd()
                obj._deserialize(item)
                self.UserCmds.append(obj)
        self.RequestId = params.get("RequestId")


class DetachCamRoleRequest(AbstractModel):
    """DetachCamRole請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 服務器ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DetachCamRoleResponse(AbstractModel):
    """DetachCamRole返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeviceAlias(AbstractModel):
    """設備ID與别名

    """

    def __init__(self):
        """
        :param InstanceId: 設備ID
        :type InstanceId: str
        :param Alias: 設備别名
        :type Alias: str
        """
        self.InstanceId = None
        self.Alias = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")


class DeviceClass(AbstractModel):
    """物理機設備類型

    """

    def __init__(self):
        """
        :param DeviceClassCode: 機型ID
        :type DeviceClassCode: str
        :param CpuDescription: CPU描述
        :type CpuDescription: str
        :param MemDescription: 内存描述
        :type MemDescription: str
        :param DiskDescription: 硬碟描述
        :type DiskDescription: str
        :param HaveRaidCard: 是否支援RAID. 0:不支援; 1:支援
        :type HaveRaidCard: int
        :param NicDescription: 網卡描述
        :type NicDescription: str
        :param GpuDescription: GPU描述
        :type GpuDescription: str
        :param Discount: 單價折扣
注意：此欄位可能返回 null，表示取不到有效值。
        :type Discount: float
        :param UnitPrice: 用戶刊例價格
注意：此欄位可能返回 null，表示取不到有效值。
        :type UnitPrice: int
        :param RealPrice: 實際價格
注意：此欄位可能返回 null，表示取不到有效值。
        :type RealPrice: int
        :param NormalPrice: 官網刊例價格
注意：此欄位可能返回 null，表示取不到有效值。
        :type NormalPrice: int
        :param DeviceType: 設備使用場景類型
        :type DeviceType: str
        :param Series: 機型系列
        :type Series: int
        :param Cpu: cpu的核心數。僅是物理服務器未開啓超線程的核心數， 超線程的核心數爲Cpu*2
        :type Cpu: int
        :param Mem: 内存容量。單位G
        :type Mem: int
        """
        self.DeviceClassCode = None
        self.CpuDescription = None
        self.MemDescription = None
        self.DiskDescription = None
        self.HaveRaidCard = None
        self.NicDescription = None
        self.GpuDescription = None
        self.Discount = None
        self.UnitPrice = None
        self.RealPrice = None
        self.NormalPrice = None
        self.DeviceType = None
        self.Series = None
        self.Cpu = None
        self.Mem = None


    def _deserialize(self, params):
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.CpuDescription = params.get("CpuDescription")
        self.MemDescription = params.get("MemDescription")
        self.DiskDescription = params.get("DiskDescription")
        self.HaveRaidCard = params.get("HaveRaidCard")
        self.NicDescription = params.get("NicDescription")
        self.GpuDescription = params.get("GpuDescription")
        self.Discount = params.get("Discount")
        self.UnitPrice = params.get("UnitPrice")
        self.RealPrice = params.get("RealPrice")
        self.NormalPrice = params.get("NormalPrice")
        self.DeviceType = params.get("DeviceType")
        self.Series = params.get("Series")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")


class DeviceClassPartitionInfo(AbstractModel):
    """RAID和設備分區結構

    """

    def __init__(self):
        """
        :param RaidId: RAID類型ID
        :type RaidId: int
        :param Raid: RAID名稱
        :type Raid: str
        :param RaidDisplay: RAID名稱（前台展示用）
        :type RaidDisplay: str
        :param SystemDiskSize: 系統盤總大小（單位GiB）
        :type SystemDiskSize: int
        :param SysRootSpace: 系統盤/分區預設大小（單位GiB）
        :type SysRootSpace: int
        :param SysSwaporuefiSpace: 系統盤swap分區預設大小（單位GiB）
        :type SysSwaporuefiSpace: int
        :param SysUsrlocalSpace: 系統盤/usr/local分區預設大小（單位GiB）
        :type SysUsrlocalSpace: int
        :param SysDataSpace: 系統盤/data分區預設大小（單位GiB）
        :type SysDataSpace: int
        :param SysIsUefiType: 設備是否是uefi啓動方式。0:legacy啓動; 1:uefi啓動
        :type SysIsUefiType: int
        :param DataDiskSize: 數據盤總大小
        :type DataDiskSize: int
        :param DeviceDiskSizeInfoSet: 硬碟清單
        :type DeviceDiskSizeInfoSet: list of DeviceDiskSizeInfo
        """
        self.RaidId = None
        self.Raid = None
        self.RaidDisplay = None
        self.SystemDiskSize = None
        self.SysRootSpace = None
        self.SysSwaporuefiSpace = None
        self.SysUsrlocalSpace = None
        self.SysDataSpace = None
        self.SysIsUefiType = None
        self.DataDiskSize = None
        self.DeviceDiskSizeInfoSet = None


    def _deserialize(self, params):
        self.RaidId = params.get("RaidId")
        self.Raid = params.get("Raid")
        self.RaidDisplay = params.get("RaidDisplay")
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.SysRootSpace = params.get("SysRootSpace")
        self.SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self.SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self.SysDataSpace = params.get("SysDataSpace")
        self.SysIsUefiType = params.get("SysIsUefiType")
        self.DataDiskSize = params.get("DataDiskSize")
        if params.get("DeviceDiskSizeInfoSet") is not None:
            self.DeviceDiskSizeInfoSet = []
            for item in params.get("DeviceDiskSizeInfoSet"):
                obj = DeviceDiskSizeInfo()
                obj._deserialize(item)
                self.DeviceDiskSizeInfoSet.append(obj)


class DeviceDiskSizeInfo(AbstractModel):
    """硬碟大小的描述

    """

    def __init__(self):
        """
        :param DiskName: 硬碟名稱
        :type DiskName: str
        :param DiskSize: 硬碟大小（單位GiB）
        :type DiskSize: int
        """
        self.DiskName = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskName = params.get("DiskName")
        self.DiskSize = params.get("DiskSize")


class DeviceHardwareInfo(AbstractModel):
    """設備硬體配置訊息

    """

    def __init__(self):
        """
        :param InstanceId: 設備實例 ID
        :type InstanceId: str
        :param IsElastic: 是否自定義機型
        :type IsElastic: int
        :param CpmPayMode: 機型計費模式，1 爲預付費，2 爲後付費
        :type CpmPayMode: int
        :param CpuId: 自定義機型，CPU 型号 ID（非自定義機型返回0）
        :type CpuId: int
        :param Mem: 自定義機型，内存大小, 單位 GB（非自定義機型返回0）
        :type Mem: int
        :param ContainRaidCard: 是否有 RAID 卡，0：沒有 RAID 卡； 1：有 RAID 卡
        :type ContainRaidCard: int
        :param SystemDiskTypeId: 自定義機型系統盤類型ID（若沒有則返回0）
        :type SystemDiskTypeId: int
        :param SystemDiskCount: 自定義機型系統盤數量（若沒有則返回0）
        :type SystemDiskCount: int
        :param DataDiskTypeId: 自定義機型數據盤類型 ID（若沒有則返回0）
        :type DataDiskTypeId: int
        :param DataDiskCount: 自定義機型數據盤數量（若沒有則返回0）
        :type DataDiskCount: int
        :param CpuDescription: CPU 型号描述
        :type CpuDescription: str
        :param MemDescription: 内存描述
        :type MemDescription: str
        :param DiskDescription: 磁盤描述
        :type DiskDescription: str
        :param NicDescription: 網卡描述
        :type NicDescription: str
        :param RaidDescription: 是否支援 RAID 的描述
        :type RaidDescription: str
        :param Cpu: cpu的核心數。僅是物理服務器未開啓超線程的核心數， 超線程的核心數爲Cpu*2
        :type Cpu: int
        """
        self.InstanceId = None
        self.IsElastic = None
        self.CpmPayMode = None
        self.CpuId = None
        self.Mem = None
        self.ContainRaidCard = None
        self.SystemDiskTypeId = None
        self.SystemDiskCount = None
        self.DataDiskTypeId = None
        self.DataDiskCount = None
        self.CpuDescription = None
        self.MemDescription = None
        self.DiskDescription = None
        self.NicDescription = None
        self.RaidDescription = None
        self.Cpu = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IsElastic = params.get("IsElastic")
        self.CpmPayMode = params.get("CpmPayMode")
        self.CpuId = params.get("CpuId")
        self.Mem = params.get("Mem")
        self.ContainRaidCard = params.get("ContainRaidCard")
        self.SystemDiskTypeId = params.get("SystemDiskTypeId")
        self.SystemDiskCount = params.get("SystemDiskCount")
        self.DataDiskTypeId = params.get("DataDiskTypeId")
        self.DataDiskCount = params.get("DataDiskCount")
        self.CpuDescription = params.get("CpuDescription")
        self.MemDescription = params.get("MemDescription")
        self.DiskDescription = params.get("DiskDescription")
        self.NicDescription = params.get("NicDescription")
        self.RaidDescription = params.get("RaidDescription")
        self.Cpu = params.get("Cpu")


class DeviceInfo(AbstractModel):
    """物理機訊息

    """

    def __init__(self):
        """
        :param InstanceId: 設備唯一ID
        :type InstanceId: str
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param DeviceStatus: 設備狀态ID，取值：<li>1：申領設備中</li><li>2：初始化中</li><li>4：運營中</li><li>7：隔離中</li><li>8：已隔離</li><li>10：解隔離中</li><li>16：故障中</li>
        :type DeviceStatus: int
        :param OperateStatus: 設備操作狀态ID，取值：
<li>1：運作中</li><li>2：正在關機</li><li>3：已關機</li><li>5：正在開機</li><li>7：重啓中</li><li>9：重裝中</li><li>12：綁定EIP</li><li>13：解綁EIP</li><li>14：綁定LB</li><li>15：解綁LB</li><li>19：更換IP中</li><li>20：制作映像中</li><li>21：制作映像失敗</li>
        :type OperateStatus: int
        :param OsTypeId: 作業系統ID，參考介面[查詢作業系統訊息(DescribeOsInfo)](https://cloud.taifucloud.com/document/product/386/32902)
        :type OsTypeId: int
        :param RaidId: RAID類型ID，參考介面[查詢機型RAID方式以及系統盤大小(DescribeDeviceClassPartition)](https://cloud.taifucloud.com/document/product/386/32910)
        :type RaidId: int
        :param Alias: 設備别名
        :type Alias: str
        :param AppId: AppId
        :type AppId: int
        :param Zone: 可用區
        :type Zone: str
        :param WanIp: 外網IP
        :type WanIp: str
        :param LanIp: 内網IP
        :type LanIp: str
        :param DeliverTime: 設備交付時間
        :type DeliverTime: str
        :param Deadline: 設備到期時間
        :type Deadline: str
        :param AutoRenewFlag: 自動續約标識。0: 不自動續約; 1:自動續約
        :type AutoRenewFlag: int
        :param DeviceClassCode: 設備類型
        :type DeviceClassCode: str
        :param Tags: 标簽清單
        :type Tags: list of Tag
        :param CpmPayMode: 計費模式。1: 預付費; 2: 後付費; 3:預付費轉後付費中
        :type CpmPayMode: int
        :param DhcpIp: 帶外IP
        :type DhcpIp: str
        :param VpcName: 所在私有網絡别名
        :type VpcName: str
        :param SubnetName: 所在子網别名
        :type SubnetName: str
        :param VpcCidrBlock: 所在私有網絡CIDR
        :type VpcCidrBlock: str
        :param SubnetCidrBlock: 所在子網CIDR
        :type SubnetCidrBlock: str
        :param IsLuckyDevice: 标識是否是競價實例。0: 普通設備; 1: 競價實例設備
        :type IsLuckyDevice: int
        """
        self.InstanceId = None
        self.VpcId = None
        self.SubnetId = None
        self.DeviceStatus = None
        self.OperateStatus = None
        self.OsTypeId = None
        self.RaidId = None
        self.Alias = None
        self.AppId = None
        self.Zone = None
        self.WanIp = None
        self.LanIp = None
        self.DeliverTime = None
        self.Deadline = None
        self.AutoRenewFlag = None
        self.DeviceClassCode = None
        self.Tags = None
        self.CpmPayMode = None
        self.DhcpIp = None
        self.VpcName = None
        self.SubnetName = None
        self.VpcCidrBlock = None
        self.SubnetCidrBlock = None
        self.IsLuckyDevice = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DeviceStatus = params.get("DeviceStatus")
        self.OperateStatus = params.get("OperateStatus")
        self.OsTypeId = params.get("OsTypeId")
        self.RaidId = params.get("RaidId")
        self.Alias = params.get("Alias")
        self.AppId = params.get("AppId")
        self.Zone = params.get("Zone")
        self.WanIp = params.get("WanIp")
        self.LanIp = params.get("LanIp")
        self.DeliverTime = params.get("DeliverTime")
        self.Deadline = params.get("Deadline")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.DeviceClassCode = params.get("DeviceClassCode")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.CpmPayMode = params.get("CpmPayMode")
        self.DhcpIp = params.get("DhcpIp")
        self.VpcName = params.get("VpcName")
        self.SubnetName = params.get("SubnetName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.IsLuckyDevice = params.get("IsLuckyDevice")


class DeviceOperationLog(AbstractModel):
    """設備操作日志

    """

    def __init__(self):
        """
        :param Id: 日志的ID
        :type Id: int
        :param InstanceId: 設備ID
        :type InstanceId: str
        :param TaskId: 日志對應的操作任務ID
        :type TaskId: int
        :param TaskName: 操作任務名稱
        :type TaskName: str
        :param TaskDescription: 操作任務中文名稱
        :type TaskDescription: str
        :param StartTime: 操作開始時間
        :type StartTime: str
        :param EndTime: 操作結束時間
        :type EndTime: str
        :param Status: 操作狀态，0: 正在執行中；1：任務成功； 2: 任務失敗。
        :type Status: int
        :param OpUin: 操作者
        :type OpUin: str
        :param LogDescription: 操作描述
        :type LogDescription: str
        """
        self.Id = None
        self.InstanceId = None
        self.TaskId = None
        self.TaskName = None
        self.TaskDescription = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.OpUin = None
        self.LogDescription = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.InstanceId = params.get("InstanceId")
        self.TaskId = params.get("TaskId")
        self.TaskName = params.get("TaskName")
        self.TaskDescription = params.get("TaskDescription")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.OpUin = params.get("OpUin")
        self.LogDescription = params.get("LogDescription")


class DevicePartition(AbstractModel):
    """物理機分區格式

    """

    def __init__(self):
        """
        :param SystemDiskSize: 系統盤大小
        :type SystemDiskSize: int
        :param DataDiskSize: 數據盤大小
        :type DataDiskSize: int
        :param SysIsUefiType: 是否兼容Uefi
        :type SysIsUefiType: bool
        :param SysRootSpace: root分區大小
        :type SysRootSpace: int
        :param SysSwaporuefiSpace: Swaporuefi分區大小
        :type SysSwaporuefiSpace: int
        :param SysUsrlocalSpace: Usrlocal分區大小
        :type SysUsrlocalSpace: int
        :param SysDataSpace: data分區大小
        :type SysDataSpace: int
        :param DeviceDiskSizeInfoSet: 硬碟大小詳情
        :type DeviceDiskSizeInfoSet: list of DeviceDiskSizeInfo
        """
        self.SystemDiskSize = None
        self.DataDiskSize = None
        self.SysIsUefiType = None
        self.SysRootSpace = None
        self.SysSwaporuefiSpace = None
        self.SysUsrlocalSpace = None
        self.SysDataSpace = None
        self.DeviceDiskSizeInfoSet = None


    def _deserialize(self, params):
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.DataDiskSize = params.get("DataDiskSize")
        self.SysIsUefiType = params.get("SysIsUefiType")
        self.SysRootSpace = params.get("SysRootSpace")
        self.SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self.SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self.SysDataSpace = params.get("SysDataSpace")
        if params.get("DeviceDiskSizeInfoSet") is not None:
            self.DeviceDiskSizeInfoSet = []
            for item in params.get("DeviceDiskSizeInfoSet"):
                obj = DeviceDiskSizeInfo()
                obj._deserialize(item)
                self.DeviceDiskSizeInfoSet.append(obj)


class DevicePositionInfo(AbstractModel):
    """物理機機架訊息

    """

    def __init__(self):
        """
        :param InstanceId: 設備ID
        :type InstanceId: str
        :param Zone: 所在可用區
        :type Zone: str
        :param VpcId: 私有網絡ID
        :type VpcId: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param LanIp: 業務IP
        :type LanIp: str
        :param Alias: 實例别名
        :type Alias: str
        :param RckName: 機架名稱
        :type RckName: str
        :param PosCode: 機位
        :type PosCode: int
        :param SwitchName: 交換機名稱
        :type SwitchName: str
        :param DeliverTime: 設備交付時間
        :type DeliverTime: str
        :param Deadline: 過期時間
        :type Deadline: str
        """
        self.InstanceId = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.LanIp = None
        self.Alias = None
        self.RckName = None
        self.PosCode = None
        self.SwitchName = None
        self.DeliverTime = None
        self.Deadline = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.LanIp = params.get("LanIp")
        self.Alias = params.get("Alias")
        self.RckName = params.get("RckName")
        self.PosCode = params.get("PosCode")
        self.SwitchName = params.get("SwitchName")
        self.DeliverTime = params.get("DeliverTime")
        self.Deadline = params.get("Deadline")


class DevicePriceInfo(AbstractModel):
    """服務器價格訊息

    """

    def __init__(self):
        """
        :param InstanceId: 物理機ID
        :type InstanceId: str
        :param DeviceClassCode: 設備型号
        :type DeviceClassCode: str
        :param IsElastic: 是否是彈性機型，1：是，0：否
        :type IsElastic: int
        :param CpmPayMode: 付費模式ID, 1:預付費; 2:後付費; 3:預付費轉後付費中
        :type CpmPayMode: int
        :param CpuDescription: Cpu訊息描述
        :type CpuDescription: str
        :param MemDescription: 内存訊息描述
        :type MemDescription: str
        :param DiskDescription: 硬碟訊息描述
        :type DiskDescription: str
        :param NicDescription: 網卡訊息描述
        :type NicDescription: str
        :param GpuDescription: Gpu訊息描述
        :type GpuDescription: str
        :param RaidDescription: Raid訊息描述
        :type RaidDescription: str
        :param Price: 客戶的單價
        :type Price: int
        :param NormalPrice: 刊例單價
        :type NormalPrice: int
        :param TotalCost: 原價
        :type TotalCost: int
        :param RealTotalCost: 折扣價
        :type RealTotalCost: int
        :param TimeSpan: 計費時長
        :type TimeSpan: int
        :param TimeUnit: 計費時長單位, M:按月計費; D:按天計費
        :type TimeUnit: str
        :param GoodsCount: 商品數量
        :type GoodsCount: int
        """
        self.InstanceId = None
        self.DeviceClassCode = None
        self.IsElastic = None
        self.CpmPayMode = None
        self.CpuDescription = None
        self.MemDescription = None
        self.DiskDescription = None
        self.NicDescription = None
        self.GpuDescription = None
        self.RaidDescription = None
        self.Price = None
        self.NormalPrice = None
        self.TotalCost = None
        self.RealTotalCost = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.GoodsCount = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DeviceClassCode = params.get("DeviceClassCode")
        self.IsElastic = params.get("IsElastic")
        self.CpmPayMode = params.get("CpmPayMode")
        self.CpuDescription = params.get("CpuDescription")
        self.MemDescription = params.get("MemDescription")
        self.DiskDescription = params.get("DiskDescription")
        self.NicDescription = params.get("NicDescription")
        self.GpuDescription = params.get("GpuDescription")
        self.RaidDescription = params.get("RaidDescription")
        self.Price = params.get("Price")
        self.NormalPrice = params.get("NormalPrice")
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.GoodsCount = params.get("GoodsCount")


class DiskInfo(AbstractModel):
    """自定義機型磁盤的描述

    """

    def __init__(self):
        """
        :param DiskTypeId: 磁盤ID
        :type DiskTypeId: int
        :param Size: 磁盤的容量，單位爲G
        :type Size: int
        :param DiskDescription: 磁盤訊息描述
        :type DiskDescription: str
        """
        self.DiskTypeId = None
        self.Size = None
        self.DiskDescription = None


    def _deserialize(self, params):
        self.DiskTypeId = params.get("DiskTypeId")
        self.Size = params.get("Size")
        self.DiskDescription = params.get("DiskDescription")


class FailedTaskInfo(AbstractModel):
    """運作失敗的自定義腳本訊息

    """

    def __init__(self):
        """
        :param InstanceId: 運作腳本的設備ID
        :type InstanceId: str
        :param ErrorMsg: 失敗原因
        :type ErrorMsg: str
        """
        self.InstanceId = None
        self.ErrorMsg = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ErrorMsg = params.get("ErrorMsg")


class HostedDeviceOutBandInfo(AbstractModel):
    """托管設備帶外訊息

    """

    def __init__(self):
        """
        :param InstanceId: 物理機ID
        :type InstanceId: str
        :param OutBandIp: 帶外IP
        :type OutBandIp: str
        :param VpnIp: VPN的IP
        :type VpnIp: str
        :param VpnPort: VPN的端口
        :type VpnPort: int
        """
        self.InstanceId = None
        self.OutBandIp = None
        self.VpnIp = None
        self.VpnPort = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OutBandIp = params.get("OutBandIp")
        self.VpnIp = params.get("VpnIp")
        self.VpnPort = params.get("VpnPort")


class ModifyCustomImageAttributeRequest(AbstractModel):
    """ModifyCustomImageAttribute請求參數結構體

    """

    def __init__(self):
        """
        :param ImageId: 映像ID
        :type ImageId: str
        :param ImageName: 設置新的映像名
        :type ImageName: str
        :param ImageDescription: 設置新的映像描述
        :type ImageDescription: str
        """
        self.ImageId = None
        self.ImageName = None
        self.ImageDescription = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")


class ModifyCustomImageAttributeResponse(AbstractModel):
    """ModifyCustomImageAttribute返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDeviceAliasesRequest(AbstractModel):
    """ModifyDeviceAliases請求參數結構體

    """

    def __init__(self):
        """
        :param DeviceAliases: 需要改名的設備與别名清單
        :type DeviceAliases: list of DeviceAlias
        """
        self.DeviceAliases = None


    def _deserialize(self, params):
        if params.get("DeviceAliases") is not None:
            self.DeviceAliases = []
            for item in params.get("DeviceAliases"):
                obj = DeviceAlias()
                obj._deserialize(item)
                self.DeviceAliases.append(obj)


class ModifyDeviceAliasesResponse(AbstractModel):
    """ModifyDeviceAliases返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDeviceAutoRenewFlagRequest(AbstractModel):
    """ModifyDeviceAutoRenewFlag請求參數結構體

    """

    def __init__(self):
        """
        :param AutoRenewFlag: 自動續約标志位。0: 不自動續約; 1: 自動續約
        :type AutoRenewFlag: int
        :param InstanceIds: 需要修改的設備ID清單
        :type InstanceIds: list of str
        """
        self.AutoRenewFlag = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.InstanceIds = params.get("InstanceIds")


class ModifyDeviceAutoRenewFlagResponse(AbstractModel):
    """ModifyDeviceAutoRenewFlag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLanIpRequest(AbstractModel):
    """ModifyLanIp請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 物理機ID
        :type InstanceId: str
        :param VpcId: 指定新VPC
        :type VpcId: str
        :param SubnetId: 指定新子網
        :type SubnetId: str
        :param LanIp: 指定新内網IP
        :type LanIp: str
        :param RebootDevice: 是否需要重啓機器，取值 1(需要) 0(不需要)，預設取值0
        :type RebootDevice: int
        """
        self.InstanceId = None
        self.VpcId = None
        self.SubnetId = None
        self.LanIp = None
        self.RebootDevice = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.LanIp = params.get("LanIp")
        self.RebootDevice = params.get("RebootDevice")


class ModifyLanIpResponse(AbstractModel):
    """ModifyLanIp返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 黑石異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyPayModePre2PostRequest(AbstractModel):
    """ModifyPayModePre2Post請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 需要修改的設備ID清單
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class ModifyPayModePre2PostResponse(AbstractModel):
    """ModifyPayModePre2Post返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPsaRegulationRequest(AbstractModel):
    """ModifyPsaRegulation請求參數結構體

    """

    def __init__(self):
        """
        :param PsaId: 預授權規則ID
        :type PsaId: str
        :param PsaName: 預授權規則别名
        :type PsaName: str
        :param RepairLimit: 維修中的實例上限
        :type RepairLimit: int
        :param PsaDescription: 預授權規則備注
        :type PsaDescription: str
        :param TaskTypeIds: 預授權規則關聯故障類型ID清單
        :type TaskTypeIds: list of int non-negative
        """
        self.PsaId = None
        self.PsaName = None
        self.RepairLimit = None
        self.PsaDescription = None
        self.TaskTypeIds = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.PsaName = params.get("PsaName")
        self.RepairLimit = params.get("RepairLimit")
        self.PsaDescription = params.get("PsaDescription")
        self.TaskTypeIds = params.get("TaskTypeIds")


class ModifyPsaRegulationResponse(AbstractModel):
    """ModifyPsaRegulation返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUserCmdRequest(AbstractModel):
    """ModifyUserCmd請求參數結構體

    """

    def __init__(self):
        """
        :param CmdId: 待修改的腳本ID
        :type CmdId: str
        :param Alias: 待修改的腳本名稱
        :type Alias: str
        :param OsType: 腳本适用的作業系統類型
        :type OsType: str
        :param Content: 待修改的腳本内容，必須經過base64編碼
        :type Content: str
        """
        self.CmdId = None
        self.Alias = None
        self.OsType = None
        self.Content = None


    def _deserialize(self, params):
        self.CmdId = params.get("CmdId")
        self.Alias = params.get("Alias")
        self.OsType = params.get("OsType")
        self.Content = params.get("Content")


class ModifyUserCmdResponse(AbstractModel):
    """ModifyUserCmd返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OfflineDevicesRequest(AbstractModel):
    """OfflineDevices請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 需要退還的物理機ID清單
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class OfflineDevicesResponse(AbstractModel):
    """OfflineDevices返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 黑石異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class OsInfo(AbstractModel):
    """作業系統類型

    """

    def __init__(self):
        """
        :param OsTypeId: 作業系統ID
        :type OsTypeId: int
        :param OsName: 作業系統名稱
        :type OsName: str
        :param OsDescription: 作業系統名稱描述
        :type OsDescription: str
        :param OsEnglishDescription: 作業系統英文名稱
        :type OsEnglishDescription: str
        :param OsClass: 作業系統的分類，如CentOs Debian
        :type OsClass: str
        :param ImageTag: 标識映像分類。public:公共映像; private: 專屬映像
        :type ImageTag: str
        :param MaxPartitionSize: 作業系統，ext4文件下所支援的最大的磁盤大小。單位爲T
        :type MaxPartitionSize: int
        :param OsMinorVersion: 黑石版本号
注意：此欄位可能返回 null，表示取不到有效值。
        :type OsMinorVersion: str
        :param OsMinorClass: 黑石版本
注意：此欄位可能返回 null，表示取不到有效值。
        :type OsMinorClass: str
        """
        self.OsTypeId = None
        self.OsName = None
        self.OsDescription = None
        self.OsEnglishDescription = None
        self.OsClass = None
        self.ImageTag = None
        self.MaxPartitionSize = None
        self.OsMinorVersion = None
        self.OsMinorClass = None


    def _deserialize(self, params):
        self.OsTypeId = params.get("OsTypeId")
        self.OsName = params.get("OsName")
        self.OsDescription = params.get("OsDescription")
        self.OsEnglishDescription = params.get("OsEnglishDescription")
        self.OsClass = params.get("OsClass")
        self.ImageTag = params.get("ImageTag")
        self.MaxPartitionSize = params.get("MaxPartitionSize")
        self.OsMinorVersion = params.get("OsMinorVersion")
        self.OsMinorClass = params.get("OsMinorClass")


class PartitionInfo(AbstractModel):
    """描述設備分區訊息

    """

    def __init__(self):
        """
        :param Name: 分區名稱
        :type Name: str
        :param Size: 分區大小
        :type Size: int
        """
        self.Name = None
        self.Size = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Size = params.get("Size")


class PsaRegulation(AbstractModel):
    """一條預授權規則

    """

    def __init__(self):
        """
        :param PsaId: 規則ID
        :type PsaId: str
        :param PsaName: 規則别名
        :type PsaName: str
        :param TagCount: 關聯标簽數量
        :type TagCount: int
        :param InstanceCount: 關聯實例數量
        :type InstanceCount: int
        :param RepairCount: 故障實例數量
        :type RepairCount: int
        :param RepairLimit: 故障實例上限
        :type RepairLimit: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param PsaDescription: 規則備注
        :type PsaDescription: str
        :param Tags: 關聯标簽
        :type Tags: list of Tag
        :param TaskTypeIds: 關聯故障類型id
        :type TaskTypeIds: list of int non-negative
        """
        self.PsaId = None
        self.PsaName = None
        self.TagCount = None
        self.InstanceCount = None
        self.RepairCount = None
        self.RepairLimit = None
        self.CreateTime = None
        self.PsaDescription = None
        self.Tags = None
        self.TaskTypeIds = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.PsaName = params.get("PsaName")
        self.TagCount = params.get("TagCount")
        self.InstanceCount = params.get("InstanceCount")
        self.RepairCount = params.get("RepairCount")
        self.RepairLimit = params.get("RepairLimit")
        self.CreateTime = params.get("CreateTime")
        self.PsaDescription = params.get("PsaDescription")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.TaskTypeIds = params.get("TaskTypeIds")


class RebootDevicesRequest(AbstractModel):
    """RebootDevices請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 需要重啓的設備ID清單
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class RebootDevicesResponse(AbstractModel):
    """RebootDevices返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RecoverDevicesRequest(AbstractModel):
    """RecoverDevices請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 需要恢複的物理機ID清單
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class RecoverDevicesResponse(AbstractModel):
    """RecoverDevices返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 黑石異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域訊息

    """

    def __init__(self):
        """
        :param Region: 地域ID
        :type Region: str
        :param RegionId: 地域整型ID
        :type RegionId: int
        :param RegionDescription: 地域描述
        :type RegionDescription: str
        :param ZoneInfoSet: 該地域下的可用區訊息
        :type ZoneInfoSet: list of ZoneInfo
        """
        self.Region = None
        self.RegionId = None
        self.RegionDescription = None
        self.ZoneInfoSet = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.RegionDescription = params.get("RegionDescription")
        if params.get("ZoneInfoSet") is not None:
            self.ZoneInfoSet = []
            for item in params.get("ZoneInfoSet"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneInfoSet.append(obj)


class ReloadDeviceOsRequest(AbstractModel):
    """ReloadDeviceOs請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceId: 設備的唯一ID
        :type InstanceId: str
        :param Password: 密碼。 用戶設置的linux root或Windows Administrator密碼。密碼校驗規則: <li> Windows機器密碼需12到16位，至少包括三項 `[a-z]`,`[A-Z]`,`[0-9]`和`[()`'`~!@#$%^&*-+=_`|`{}[]:;'<>,.?/]`的特殊符号, 密碼不能包含Administrator(不區分大小寫); <li> Linux機器密碼需8到16位，至少包括兩項`[a-z,A-Z]`,`[0-9]`和`[()`'`~!@#$%^&*-+=_`|`{}[]:;'<>,.?/]`的特殊符号
        :type Password: str
        :param OsTypeId: 作業系統類型ID。通過介面[查詢作業系統訊息(DescribeOsInfo)](https://cloud.taifucloud.com/document/api/386/32902)獲取作業系統訊息
        :type OsTypeId: int
        :param RaidId: RAID類型ID。通過介面[查詢機型RAID方式以及系統盤大小(DescribeDeviceClassPartition)](https://cloud.taifucloud.com/document/api/386/32910)獲取RAID訊息
        :type RaidId: int
        :param IsZoning: 是否格式化數據盤。0: 不格式化（預設值）；1：格式化
        :type IsZoning: int
        :param SysRootSpace: 系統盤根分區大小，預設是10G。系統盤的大小參考介面[查詢機型RAID方式以及系統盤大小(DescribeDeviceClassPartition)](https://cloud.taifucloud.com/document/api/386/32910)
        :type SysRootSpace: int
        :param SysSwaporuefiSpace: 系統盤swap分區或/boot/efi分區的大小。若是uefi啓動的機器，分區爲/boot/efi ,且此值是預設是2G。普通機器爲swap分區，可以不指定此分區。機型是否是uefi啓動，參考介面[查詢設備型号(DescribeDeviceClass)](https://cloud.taifucloud.com/document/api/386/32911)
        :type SysSwaporuefiSpace: int
        :param SysUsrlocalSpace: /usr/local分區大小
        :type SysUsrlocalSpace: int
        :param VpcId: 重裝到新的私有網絡的ID。如果改變VPC子網，則要求與SubnetId同時傳參，否則可不填
        :type VpcId: str
        :param SubnetId: 重裝到新的子網的ID。如果改變VPC子網，則要求與VpcId同時傳參，否則可不填
        :type SubnetId: str
        :param LanIp: 重裝指定IP網址
        :type LanIp: str
        :param HyperThreading: 指定是否開啓超線程。 0：關閉超線程；1：開啓超線程（預設值）
        :type HyperThreading: int
        :param ImageId: 自定義映像ID。傳此欄位則用自定義映像重裝
        :type ImageId: str
        :param FileSystem: 指定數據盤的文件系統格式，當前支援 EXT4和XFS選項， 預設爲EXT4。 參數适用于數據盤和Linux， 且在IsZoning爲1時生效
        :type FileSystem: str
        :param NeedSecurityAgent: 是否安裝安全Agent，取值：1(安裝) 0(不安裝)，預設取值0
        :type NeedSecurityAgent: int
        :param NeedMonitorAgent: 是否安裝監控Agent，取值：1(安裝) 0(不安裝)，預設取值0
        :type NeedMonitorAgent: int
        :param NeedEMRAgent: 是否安裝EMR Agent，取值：1(安裝) 0(不安裝)，預設取值0
        :type NeedEMRAgent: int
        :param NeedEMRSoftware: 是否安裝EMR軟體包，取值：1(安裝) 0(不安裝)，預設取值0
        :type NeedEMRSoftware: int
        :param ReserveSgConfig: 是否保留安全組配置，取值：1(保留) 0(不保留)，預設取值0
        :type ReserveSgConfig: int
        :param SysDataSpace: /data分區大小，可不填。除root、swap、usr/local的剩餘空間會自動分配到data分區
        :type SysDataSpace: int
        """
        self.InstanceId = None
        self.Password = None
        self.OsTypeId = None
        self.RaidId = None
        self.IsZoning = None
        self.SysRootSpace = None
        self.SysSwaporuefiSpace = None
        self.SysUsrlocalSpace = None
        self.VpcId = None
        self.SubnetId = None
        self.LanIp = None
        self.HyperThreading = None
        self.ImageId = None
        self.FileSystem = None
        self.NeedSecurityAgent = None
        self.NeedMonitorAgent = None
        self.NeedEMRAgent = None
        self.NeedEMRSoftware = None
        self.ReserveSgConfig = None
        self.SysDataSpace = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")
        self.OsTypeId = params.get("OsTypeId")
        self.RaidId = params.get("RaidId")
        self.IsZoning = params.get("IsZoning")
        self.SysRootSpace = params.get("SysRootSpace")
        self.SysSwaporuefiSpace = params.get("SysSwaporuefiSpace")
        self.SysUsrlocalSpace = params.get("SysUsrlocalSpace")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.LanIp = params.get("LanIp")
        self.HyperThreading = params.get("HyperThreading")
        self.ImageId = params.get("ImageId")
        self.FileSystem = params.get("FileSystem")
        self.NeedSecurityAgent = params.get("NeedSecurityAgent")
        self.NeedMonitorAgent = params.get("NeedMonitorAgent")
        self.NeedEMRAgent = params.get("NeedEMRAgent")
        self.NeedEMRSoftware = params.get("NeedEMRSoftware")
        self.ReserveSgConfig = params.get("ReserveSgConfig")
        self.SysDataSpace = params.get("SysDataSpace")


class ReloadDeviceOsResponse(AbstractModel):
    """ReloadDeviceOs返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 黑石異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RepairTaskControlRequest(AbstractModel):
    """RepairTaskControl請求參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 維修任務ID
        :type TaskId: str
        :param Operate: 操作
        :type Operate: str
        """
        self.TaskId = None
        self.Operate = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Operate = params.get("Operate")


class RepairTaskControlResponse(AbstractModel):
    """RepairTaskControl返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 出參TaskId是黑石異步任務ID，不同于入參TaskId欄位。
此欄位可作爲DescriptionOperationResult查詢異步任務狀态介面的入參，查詢異步任務執行結果。
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ResetDevicePasswordRequest(AbstractModel):
    """ResetDevicePassword請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 需要重置密碼的服務器ID清單
        :type InstanceIds: list of str
        :param Password: 新密碼
        :type Password: str
        """
        self.InstanceIds = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Password = params.get("Password")


class ResetDevicePasswordResponse(AbstractModel):
    """ResetDevicePassword返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 黑石異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ReturnDevicesRequest(AbstractModel):
    """ReturnDevices請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 需要退還的物理機ID清單
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class ReturnDevicesResponse(AbstractModel):
    """ReturnDevices返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 黑石異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RunUserCmdRequest(AbstractModel):
    """RunUserCmd請求參數結構體

    """

    def __init__(self):
        """
        :param CmdId: 自定義腳本ID
        :type CmdId: str
        :param UserName: 執行腳本機器的用戶名
        :type UserName: str
        :param Password: 執行腳本機器的用戶名的密碼
        :type Password: str
        :param InstanceIds: 執行腳本的服務器實例
        :type InstanceIds: list of str
        :param CmdParam: 執行腳本的參數，必須經過base64編碼
        :type CmdParam: str
        """
        self.CmdId = None
        self.UserName = None
        self.Password = None
        self.InstanceIds = None
        self.CmdParam = None


    def _deserialize(self, params):
        self.CmdId = params.get("CmdId")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.InstanceIds = params.get("InstanceIds")
        self.CmdParam = params.get("CmdParam")


class RunUserCmdResponse(AbstractModel):
    """RunUserCmd返回參數結構體

    """

    def __init__(self):
        """
        :param SuccessTaskInfoSet: 運作成功的任務訊息清單
        :type SuccessTaskInfoSet: list of SuccessTaskInfo
        :param FailedTaskInfoSet: 運作失敗的任務訊息清單
        :type FailedTaskInfoSet: list of FailedTaskInfo
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.SuccessTaskInfoSet = None
        self.FailedTaskInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SuccessTaskInfoSet") is not None:
            self.SuccessTaskInfoSet = []
            for item in params.get("SuccessTaskInfoSet"):
                obj = SuccessTaskInfo()
                obj._deserialize(item)
                self.SuccessTaskInfoSet.append(obj)
        if params.get("FailedTaskInfoSet") is not None:
            self.FailedTaskInfoSet = []
            for item in params.get("FailedTaskInfoSet"):
                obj = FailedTaskInfo()
                obj._deserialize(item)
                self.FailedTaskInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class SetOutBandVpnAuthPasswordRequest(AbstractModel):
    """SetOutBandVpnAuthPassword請求參數結構體

    """

    def __init__(self):
        """
        :param Password: 設置的Vpn認證密碼
        :type Password: str
        :param Operate: 操作欄位，取值爲：Create（創建）或Update（修改）
        :type Operate: str
        """
        self.Password = None
        self.Operate = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.Operate = params.get("Operate")


class SetOutBandVpnAuthPasswordResponse(AbstractModel):
    """SetOutBandVpnAuthPassword返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ShutdownDevicesRequest(AbstractModel):
    """ShutdownDevices請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 需要關閉的設備ID清單
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class ShutdownDevicesResponse(AbstractModel):
    """ShutdownDevices返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class StartDevicesRequest(AbstractModel):
    """StartDevices請求參數結構體

    """

    def __init__(self):
        """
        :param InstanceIds: 需要開機的設備ID清單
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class StartDevicesResponse(AbstractModel):
    """StartDevices返回參數結構體

    """

    def __init__(self):
        """
        :param TaskId: 異步任務ID
        :type TaskId: int
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SubtaskStatus(AbstractModel):
    """各實例對應的異步任務執行結果

    """

    def __init__(self):
        """
        :param InstanceId: 實例ID
        :type InstanceId: str
        :param TaskStatus: 實例ID對應任務的狀态，取值如下：<br>
1：成功<br>
2：失敗<br>
3：部分成功，部分失敗<br>
4：未完成<br>
5：部分成功，部分未完成<br>
6：部分未完成，部分失敗<br>
7：部分未完成，部分失敗，部分成功
        :type TaskStatus: int
        """
        self.InstanceId = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TaskStatus = params.get("TaskStatus")


class SuccessTaskInfo(AbstractModel):
    """成功運作的自定義腳本訊息

    """

    def __init__(self):
        """
        :param InstanceId: 運作腳本的設備ID
        :type InstanceId: str
        :param TaskId: 黑石異步任務ID
        :type TaskId: int
        :param CmdTaskId: 黑石自定義腳本運作任務ID
        :type CmdTaskId: str
        """
        self.InstanceId = None
        self.TaskId = None
        self.CmdTaskId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TaskId = params.get("TaskId")
        self.CmdTaskId = params.get("CmdTaskId")


class Tag(AbstractModel):
    """标簽鍵與值

    """

    def __init__(self):
        """
        :param TagKey: 标簽鍵
        :type TagKey: str
        :param TagValues: 标簽鍵對應的值
        :type TagValues: list of str
        """
        self.TagKey = None
        self.TagValues = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValues = params.get("TagValues")


class TaskInfo(AbstractModel):
    """維護平台維修任務訊息

    """

    def __init__(self):
        """
        :param TaskId: 任務id
        :type TaskId: str
        :param InstanceId: 主機id
        :type InstanceId: str
        :param Alias: 主機别名
        :type Alias: str
        :param TaskTypeId: 故障類型id
        :type TaskTypeId: int
        :param TaskStatus: 任務狀态id
        :type TaskStatus: int
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param AuthTime: 授權時間
        :type AuthTime: str
        :param EndTime: 結束時間
        :type EndTime: str
        :param TaskDetail: 任務詳情
        :type TaskDetail: str
        :param DeviceStatus: 設備狀态
        :type DeviceStatus: int
        :param OperateStatus: 設備操作狀态
        :type OperateStatus: int
        :param Zone: 可用區
        :type Zone: str
        :param Region: 地域
        :type Region: str
        :param VpcId: 所屬網絡
        :type VpcId: str
        :param SubnetId: 所在子網
        :type SubnetId: str
        :param SubnetName: 子網名
        :type SubnetName: str
        :param VpcName: VPC名
        :type VpcName: str
        :param VpcCidrBlock: VpcCidrBlock
        :type VpcCidrBlock: str
        :param SubnetCidrBlock: SubnetCidrBlock
        :type SubnetCidrBlock: str
        :param WanIp: 公網ip
        :type WanIp: str
        :param LanIp: 内網IP
        :type LanIp: str
        :param MgtIp: 管理IP
        :type MgtIp: str
        :param TaskTypeName: 故障類中文名
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskTypeName: str
        :param TaskSubType: 故障類型，取值：unconfirmed (不明确故障)；redundancy (有備援故障)；nonredundancy (無備援故障)
注意：此欄位可能返回 null，表示取不到有效值。
        :type TaskSubType: str
        """
        self.TaskId = None
        self.InstanceId = None
        self.Alias = None
        self.TaskTypeId = None
        self.TaskStatus = None
        self.CreateTime = None
        self.AuthTime = None
        self.EndTime = None
        self.TaskDetail = None
        self.DeviceStatus = None
        self.OperateStatus = None
        self.Zone = None
        self.Region = None
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.SubnetCidrBlock = None
        self.WanIp = None
        self.LanIp = None
        self.MgtIp = None
        self.TaskTypeName = None
        self.TaskSubType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.InstanceId = params.get("InstanceId")
        self.Alias = params.get("Alias")
        self.TaskTypeId = params.get("TaskTypeId")
        self.TaskStatus = params.get("TaskStatus")
        self.CreateTime = params.get("CreateTime")
        self.AuthTime = params.get("AuthTime")
        self.EndTime = params.get("EndTime")
        self.TaskDetail = params.get("TaskDetail")
        self.DeviceStatus = params.get("DeviceStatus")
        self.OperateStatus = params.get("OperateStatus")
        self.Zone = params.get("Zone")
        self.Region = params.get("Region")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.WanIp = params.get("WanIp")
        self.LanIp = params.get("LanIp")
        self.MgtIp = params.get("MgtIp")
        self.TaskTypeName = params.get("TaskTypeName")
        self.TaskSubType = params.get("TaskSubType")


class TaskOperationLog(AbstractModel):
    """維修任務操作日志

    """

    def __init__(self):
        """
        :param TaskStep: 操作步驟
        :type TaskStep: str
        :param Operator: 操作人
        :type Operator: str
        :param OperationDetail: 操作描述
        :type OperationDetail: str
        :param OperationTime: 操作時間
        :type OperationTime: str
        """
        self.TaskStep = None
        self.Operator = None
        self.OperationDetail = None
        self.OperationTime = None


    def _deserialize(self, params):
        self.TaskStep = params.get("TaskStep")
        self.Operator = params.get("Operator")
        self.OperationDetail = params.get("OperationDetail")
        self.OperationTime = params.get("OperationTime")


class TaskType(AbstractModel):
    """故障id對應故障名清單

    """

    def __init__(self):
        """
        :param TypeId: 故障類ID
        :type TypeId: int
        :param TypeName: 故障類中文名
        :type TypeName: str
        :param TaskSubType: 故障類型父類
        :type TaskSubType: str
        """
        self.TypeId = None
        self.TypeName = None
        self.TaskSubType = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")
        self.TypeName = params.get("TypeName")
        self.TaskSubType = params.get("TaskSubType")


class UnbindPsaTagRequest(AbstractModel):
    """UnbindPsaTag請求參數結構體

    """

    def __init__(self):
        """
        :param PsaId: 預授權規則ID
        :type PsaId: str
        :param TagKey: 需要解綁的标簽key
        :type TagKey: str
        :param TagValue: 需要解綁的标簽value
        :type TagValue: str
        """
        self.PsaId = None
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.PsaId = params.get("PsaId")
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class UnbindPsaTagResponse(AbstractModel):
    """UnbindPsaTag返回參數結構體

    """

    def __init__(self):
        """
        :param RequestId: 唯一請求 ID，每次請求都會返回。定位問題時需要提供該次請求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserCmd(AbstractModel):
    """腳本訊息

    """

    def __init__(self):
        """
        :param Alias: 用戶自定義腳本名
        :type Alias: str
        :param AppId: AppId
        :type AppId: int
        :param AutoId: 腳本自增ID
        :type AutoId: int
        :param CmdId: 腳本ID
        :type CmdId: str
        :param Content: 腳本内容
        :type Content: str
        :param CreateTime: 創建時間
        :type CreateTime: str
        :param ModifyTime: 修改時間
        :type ModifyTime: str
        :param OsType: 命令适用的作業系統類型
        :type OsType: str
        """
        self.Alias = None
        self.AppId = None
        self.AutoId = None
        self.CmdId = None
        self.Content = None
        self.CreateTime = None
        self.ModifyTime = None
        self.OsType = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.AppId = params.get("AppId")
        self.AutoId = params.get("AutoId")
        self.CmdId = params.get("CmdId")
        self.Content = params.get("Content")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.OsType = params.get("OsType")


class UserCmdTask(AbstractModel):
    """自定義腳本任務訊息

    """

    def __init__(self):
        """
        :param TaskId: 任務ID
        :type TaskId: str
        :param Status: 任務狀态ID，取值: -1(進行中) 0(結束)
        :type Status: int
        :param Alias: 腳本名稱
        :type Alias: str
        :param CmdId: 腳本ID
        :type CmdId: str
        :param InstanceCount: 運作實例數量
        :type InstanceCount: int
        :param SuccessCount: 運作成功數量
        :type SuccessCount: int
        :param FailureCount: 運作失敗數量
        :type FailureCount: int
        :param RunBeginTime: 執行開始時間
        :type RunBeginTime: str
        :param RunEndTime: 執行結束時間
        :type RunEndTime: str
        """
        self.TaskId = None
        self.Status = None
        self.Alias = None
        self.CmdId = None
        self.InstanceCount = None
        self.SuccessCount = None
        self.FailureCount = None
        self.RunBeginTime = None
        self.RunEndTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Status = params.get("Status")
        self.Alias = params.get("Alias")
        self.CmdId = params.get("CmdId")
        self.InstanceCount = params.get("InstanceCount")
        self.SuccessCount = params.get("SuccessCount")
        self.FailureCount = params.get("FailureCount")
        self.RunBeginTime = params.get("RunBeginTime")
        self.RunEndTime = params.get("RunEndTime")


class UserCmdTaskInfo(AbstractModel):
    """自定義腳本任務詳細訊息

    """

    def __init__(self):
        """
        :param AutoId: 自動編号，可忽略
        :type AutoId: int
        :param TaskId: 任務ID
        :type TaskId: str
        :param RunBeginTime: 任務開始時間
        :type RunBeginTime: str
        :param RunEndTime: 任務結束時間
        :type RunEndTime: str
        :param Status: 任務狀态ID，取值爲 -1：進行中；0：成功；>0：失敗錯誤碼
        :type Status: int
        :param InstanceName: 設備别名
        :type InstanceName: str
        :param InstanceId: 設備ID
        :type InstanceId: str
        :param VpcName: 私有網絡名
        :type VpcName: str
        :param VpcId: 私有網絡整型ID
        :type VpcId: str
        :param VpcCidrBlock: 私有網絡Cidr
        :type VpcCidrBlock: str
        :param SubnetName: 子網名
        :type SubnetName: str
        :param SubnetId: 子網ID
        :type SubnetId: str
        :param SubnetCidrBlock: 子網Cidr
        :type SubnetCidrBlock: str
        :param LanIp: 内網IP
        :type LanIp: str
        :param CmdContent: 腳本内容，base64編碼後的值
        :type CmdContent: str
        :param CmdParam: 腳本參數，base64編碼後的值
        :type CmdParam: str
        :param CmdResult: 腳本執行結果，base64編碼後的值
        :type CmdResult: str
        :param AppId: 用戶AppId
        :type AppId: int
        :param LastShellExit: 用戶執行腳本結束登出的返回值，沒有返回值爲-1
        :type LastShellExit: int
        """
        self.AutoId = None
        self.TaskId = None
        self.RunBeginTime = None
        self.RunEndTime = None
        self.Status = None
        self.InstanceName = None
        self.InstanceId = None
        self.VpcName = None
        self.VpcId = None
        self.VpcCidrBlock = None
        self.SubnetName = None
        self.SubnetId = None
        self.SubnetCidrBlock = None
        self.LanIp = None
        self.CmdContent = None
        self.CmdParam = None
        self.CmdResult = None
        self.AppId = None
        self.LastShellExit = None


    def _deserialize(self, params):
        self.AutoId = params.get("AutoId")
        self.TaskId = params.get("TaskId")
        self.RunBeginTime = params.get("RunBeginTime")
        self.RunEndTime = params.get("RunEndTime")
        self.Status = params.get("Status")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetName = params.get("SubnetName")
        self.SubnetId = params.get("SubnetId")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.LanIp = params.get("LanIp")
        self.CmdContent = params.get("CmdContent")
        self.CmdParam = params.get("CmdParam")
        self.CmdResult = params.get("CmdResult")
        self.AppId = params.get("AppId")
        self.LastShellExit = params.get("LastShellExit")


class ZoneInfo(AbstractModel):
    """可用區訊息

    """

    def __init__(self):
        """
        :param Zone: 可用區ID
        :type Zone: str
        :param ZoneId: 可用區整型ID
        :type ZoneId: int
        :param ZoneDescription: 可用區描述
        :type ZoneDescription: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneDescription = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneDescription = params.get("ZoneDescription")