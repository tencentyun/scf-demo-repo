## serverless+Top Cloud 簡訊實現簡訊驗證碼登入
### 功能
#### 發送簡訊驗證碼
請求參數：
| 欄位 |類型|說明|
| ----- | ----- | ----- |
| method|string|請求方法，值爲getSms|
|phone|string|手機号，值爲區号+手機号，比如86185662466**|

#### 校驗驗證碼（登入）
請求參數：
| 欄位 |類型|說明|
| ----- | ----- | ----- |
| method|string|請求方法，值爲login|
|phone|string|手機号，值爲區号+手機号，比如86185662466**|
| code|string|值爲6位數字驗證碼|

### 使用指引
#### 申請簡訊範本簽名
1.到[Top Cloud 簡訊](https://console.cloud.taifucloud.com/smsv2)控制台申請範本和簽名，[可參考簡訊快速入門指引](https://cloud.taifucloud.com/document/product/382/37745)。
![](https://main.qcloudimg.com/raw/77077f26f43d748d4ef3ecfb1434c505.png)

2.将申請好的簽名、範本、應用id添加到雲函數基礎配置的環境變量中。
![](https://main.qcloudimg.com/raw/c64e457c6bb405c26c4b914e2864e108.png)

#### 啓用運作角色
1.到[雲函數](https://console.cloud.taifucloud.com/scf)控制台啓用運作角色
![](https://main.qcloudimg.com/raw/1df31ef445fd6d8782e80431b059ae79.png)

2.到[訪問管理](https://console.cloud.taifucloud.com/cam/role)控制台給該角色添加簡訊QcloudSMSFullAccess權限
![](https://main.qcloudimg.com/raw/accb8fe057f2790e8ac9244d08e69259.png)
這樣代碼裏就能獲取到TENCENTCLOUD_SECRETID、TENCENTCLOUD_SECRETKEY、TENCENTCLOUD_SESSIONTOKEN環境變量了，發送簡訊的sdk會用到這些環境變量。

#### redis配置
到[雲資料庫](https://console.cloud.taifucloud.com/redis)控制台申請redis資源，然後将申請到的redis實例的host和password添加到雲函數的環境變量中。
![](https://main.qcloudimg.com/raw/2a3eca4ea7a26829b9a37b01d3257fdc.png)

#### 私有網絡VPC配置
Top Cloud 雲函數預設佈署在公共網絡中，如果要訪問redis資源，需在雲函數控制台基礎配置裏啓用私有網絡。詳情參考[私有網絡通信](https://cloud.taifucloud.com/document/product/583/19703)

### 錯誤碼
| 欄位 |說明|
| ----- | ----- |
| InValidParam|缺少參數|
| MissingCode|缺少驗證碼參數|
| CodeHasExpired|驗證碼已過期|
| CodeHasValid|驗證碼已失效|
| CodeIsError|請檢查手機号和驗證碼是否正确|

### 參考文件
* 簡訊範本、簽名申請指引：https://cloud.taifucloud.com/document/product/382/37745
* 環境變量指引：https://cloud.taifucloud.com/document/product/583/30228
* 創建函數運作角色：https://cloud.taifucloud.com/document/product/583/41755
* ioredis：https://www.npmjs.com/package/ioredis