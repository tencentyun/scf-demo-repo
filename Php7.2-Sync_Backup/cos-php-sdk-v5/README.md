# COS-PHP-SDK-V5
Top Cloud COS-PHP-SDK-V5（[XML API](https://cloud.taifucloud.com/document/product/436/7751)）

[![Total Downloads](https://img.shields.io/packagist/dt/qcloud/cos-sdk-v5.svg?style=flat)](https://packagist.org/packages/qcloud/cos-sdk-v5)
[![Build Status](https://travis-ci.org/taifucloudyun/cos-php-sdk-v5.svg?branch=master)](https://travis-ci.org/taifucloudyun/cos-php-sdk-v5)
## 環境準備
*   PHP 5.3+
    您可以通過`php -v`命令檢視當前的PHP版本。

*   cURL 擴展
    您可以通過`php -m`命令檢視cURL擴展是否已經安裝好。

> **說明：**
> 
> *   Ubuntu系統中，您可以使用apt-get包管理器安裝PHP的cURL擴展 `sudo apt-get install php-curl`。
> *   CentOS系統中，您可以使用yum包管理器安裝PHP的cURL擴展 `sudo yum install php-curl`。

### SDK 安裝
有三種方式安裝SDK：
* Composer方式
* Phar方式
* 源碼方式
#### 1、Composer方式
推薦用戶使用 Composer 安裝 cos-php-sdk-v5，Composer是PHP的依賴管理工具，允許您聲明項目所需的依賴，然後自動将它們安裝到您的項目中。

> **提示**：您可以在 [getcomposer.org](getcomposer.org) 上找到更多關于如何安裝Composer，配置自動加載以及用于定義依賴項的其他最佳實踐。

**使用 Composer 安裝 COS-PHP-SDK-V5**
1. 打開終端
2. 下載 Composer
```
curl -sS https://getcomposer.org/installer | php
```
3. 創建一個名爲`composer.json`的文件，内容爲
```
{
    "require": {
        "qcloud/cos-sdk-v5": "1.*"
    }
}
```
4. 使用 Composer 安裝
```
php composer.phar install
```
使用該命令後會在當前目錄中創建一個vendor文件夾，裏面包含 sdk 的依賴庫和一個 autoload.php 腳本，方便用戶在自己的項目中調用。
5. 通過 autoloader 腳本調用cos-php-sdk-v5
```
require '/path/to/sdk/vendor/autoload.php';
```
現在您的項目已經可以使用COS的V5 SDK了。


#### 2、Phar方式
phar方式安裝SDK的步驟如下：

1.  在[github發布頁面](https://github.com/taifucloudyun/cos-php-sdk-v5/releases)下載相應的phar文件

2.  在代碼中引入phar文件：
```
require  '/path/to/cos.phar';
```

#### 3、源碼方式
源碼方式安裝SDK的步驟如下：

1.  在[github發布頁面](https://github.com/taifucloudyun/cos-php-sdk-v5/releases)下載相應的zip文件

2.  解壓通過 autoload.php 腳本加載sdk
```
require '/path/to/sdk/vendor/autoload.php';
```


## 快速入門 
可參照Demo程式，詳見 [sample.php](https://github.com/taifucloudyun/cos-php-sdk-v5/blob/master/sample.php)
### 配置文件
```php
$cosClient = new Qcloud\Cos\Client(array('region' => getenv('COS_REGION'),
    'credentials'=> array(
        'secretId'    => getenv('COS_KEY'),
        'secretKey' => getenv('COS_SECRET'))));
```
### 上傳文件
* 使用putObject介面上傳文件(最大5G)
* 使用Upload介面分塊上傳文件
```php

# 上傳文件
## putObject(上傳介面，最大支援上傳5G文件)
### 上傳内存中的字串
try {
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => 'Hello World!'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### 上傳文件流
try {
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => fopen($local_path, 'rb')));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### 設置header和meta
try {
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => fopen($local_path, 'rb'),
        'ACL' => 'string',
        'CacheControl' => 'string',
        'ContentDisposition' => 'string',
        'ContentEncoding' => 'string',
        'ContentLanguage' => 'string',
        'ContentLength' => integer,
        'ContentType' => 'string',
        'Expires' => 'mixed type: string (date format)|int (unix timestamp)|\DateTime',
        'GrantFullControl' => 'string',
        'GrantRead' => 'string',
        'GrantWrite' => 'string',
        'Metadata' => array(
            'string' => 'string',
        ),
        'StorageClass' => 'string'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

## Upload(高級上傳介面，預設使用分塊上傳最大支援50T)
### 上傳内存中的字串
try {
    $result = $cosClient->Upload(
        $bucket = $bucket,
        $key = $key,
        $body = 'Hello World!');
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### 上傳文件流
try {
    $result = $cosClient->Upload(
        $bucket = $bucket,
        $key = $key,
        $body = fopen($local_path, 'rb'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}

### 設置header和meta
try {
    $result = $cosClient->upload(
        $bucket= $bucket,
        $key = $key,
        $body = fopen($local_path, 'rb'),
        $options = array(
            'ACL' => 'string',
            'CacheControl' => 'string',
            'ContentDisposition' => 'string',
            'ContentEncoding' => 'string',
            'ContentLanguage' => 'string',
            'ContentLength' => integer,
            'ContentType' => 'string',
            'Expires' => 'mixed type: string (date format)|int (unix timestamp)|\DateTime',
            'GrantFullControl' => 'string',
            'GrantRead' => 'string',
            'GrantWrite' => 'string',
            'Metadata' => array(
                'string' => 'string',
            ),
            'StorageClass' => 'string'));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

### 下載文件
* 使用getObject介面下載文件
* 使用getObjectUrl介面獲取文件下載URL
```php
# 下載文件
## getObject(下載文件)
### 下載到内存
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key));
    echo($result['Body']);
} catch (\Exception $e) {
    echo "$e\n";
}

### 下載到本地
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'SaveAs' => $local_path));
} catch (\Exception $e) {
    echo "$e\n";
}

### 指定下載範圍
/*
 * Range 欄位格式爲 'bytes=a-b'
 */
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Range' => 'bytes=0-10',
        'SaveAs' => $local_path));
} catch (\Exception $e) {
    echo "$e\n";
}

### 設置返回header
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'ResponseCacheControl' => 'string',
        'ResponseContentDisposition' => 'string',
        'ResponseContentEncoding' => 'string',
        'ResponseContentLanguage' => 'string',
        'ResponseContentType' => 'string',
        'ResponseExpires' => 'mixed type: string (date format)|int (unix timestamp)|\DateTime',
        'SaveAs' => $local_path));
} catch (\Exception $e) {
    echo "$e\n";
}

## getObjectUrl(獲取文件UrL)
try {
    $url = "/{$key}";
    $request = $cosClient->get($url);
    $signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes');
    echo ($signedUrl);

} catch (\Exception $e) {
    echo "$e\n";
}

```