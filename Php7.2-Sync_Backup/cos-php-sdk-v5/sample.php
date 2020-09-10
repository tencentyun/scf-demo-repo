<?php

require 'vendor/autoload.php';

$cosClient = new Qcloud\Cos\Client(array(
    'region' => getenv('COS_REGION'),
    'credentials' => array(
        'appId' => getenv('COS_APPID'),
        'secretId' => getenv('COS_KEY'),
        'secretKey' => getenv('COS_SECRET'),
    ),
));

// 若初始化 Client 時未填寫 appId，則 bucket 的命名規則爲{name}-{appid} ，此處填寫的儲存桶名稱必須爲此格式
$bucket = 'lewzyLU02-1252448703';
$key = 'a.txt';
$local_path = "E:/a.txt";

# 上傳文件
## putObject(上傳介面，最大支援上傳5G文件)
### 上傳内存中的字串
try {
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => 'Hello World!'
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

### 上傳文件流
try {
    $result = $cosClient->putObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => fopen($local_path, 'rb')
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
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
        'cONTENTType' => 'string',
        'Expires' => 'mixed type: string (date format)|int (unix timestamp)|\DateTime',
        'GrantFullControl' => 'string',
        'GrantRead' => 'string',
        'GrantWrite' => 'string',
        'Metadata' => array(
            'string' => 'string',
        ),
        'StorageClass' => 'string'
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## Upload(高級上傳介面，預設使用分塊上傳最大支援50T)
### 上傳内存中的字串
try {
    $result = $cosClient->Upload(
        $bucket = $bucket,
        $key = $key,
        $body = 'Hello World!'
    );
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

### 上傳文件流
try {
    $result = $cosClient->Upload(
        $bucket = $bucket,
        $key = $key,
        $body = fopen($local_path, 'rb')
    );
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

### 設置header和meta
try {
    $result = $cosClient->upload(
        $bucket = $bucket,
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
            'StorageClass' => 'string'
        )
    );
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## 預簽名上傳createPresignedUrl
## 獲取帶有簽名的url
### 簡單上傳預簽名
try {
    #此處可以替換爲其他上傳介面
    $command = $cosClient->getCommand('putObject', array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Body' => '', //Body可以任意
    ));
    $signedUrl = $command->createPresignedUrl('+10 minutes');
    echo ($signedUrl);
} catch (\Exception $e) {
    print_r($e);
}

### 分塊上傳預簽名
try {
    #此處可以替換爲其他上傳介面
    $command = $cosClient->getCommand('uploadPart', array(
        'Bucket' => $bucket,
        'Key' => $key,
        'UploadId' => $uploadId,
        'PartNumber' => '1',
        'Body' => '', //Body可以任意
    ));
    $signedUrl = $command->createPresignedUrl('+10 minutes');
    echo ($signedUrl);
} catch (\Exception $e) {
    print_r($e);
}

# 下載文件
## getObject(下載文件)
### 下載到内存
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key
    ));
    echo $result['Body'];
} catch (\Exception $e) {
    print_r($e);
}

### 下載到本地
try {
    $result = $cosClient->getObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'SaveAs' => $local_path
    ));
} catch (\Exception $e) {
    print_r($e);
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
        'SaveAs' => $local_path
    ));
} catch (\Exception $e) {
    print_r($e);
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
        'SaveAs' => $local_path
    ));
} catch (\Exception $e) {
    print_r($e);
}

## getObjectUrl(獲取文件UrL)
try {
    $signedUrl = $cosClient->getObjectUrl($bucket, $key, '+10 minutes');
    echo $signedUrl;
} catch (\Exception $e) {
    print_r($e);
}

# 删除object
## deleteObject
try {
    $result = $cosClient->deleteObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'VersionId' => 'string'
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 删除多個object
## deleteObjects
try {
    $result = $cosClient->deleteObjects(array(
        'Bucket' => 'string',
        'Objects' => array(
            array(
                'Key' => $key,
                'VersionId' => 'string',
            ),
            // ... repeated
        ),
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 獲取object訊息
## headObject
/*
 * 可代替isObjectExist介面，查詢object是否存在
 */
try {
    $result = $cosClient->headObject(array(
        'Bucket' => $bucket,
        'Key' => '11',
        'VersionId' => '111',
        'ServerSideEncryption' => 'AES256'
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 獲取bucket清單
## listBuckets
try {
    $result = $cosClient->listBuckets();
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 創建bucket
## createBucket
try {
    $result = $cosClient->createBucket(array('Bucket' => $bucket));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 删除bucket
## deleteBucket
try {
    $result = $cosClient->deleteBucket(array(
        'Bucket' => $bucket
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 獲取bucket訊息
## headBucket
/*
 * 可代替isBucketExist介面，查詢bucket是否存在
 */
try {
    $result = $cosClient->headBucket(array(
        'Bucket' => $bucket
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 列出bucket下的object
## listObjects
### 列出所有object
/*
 * 該介面一次最多列出1000個，需要列出所有請參考其他服務中的清空并删除bucket介面
 */
try {
    $result = $cosClient->listObjects(array(
        'Bucket' => $bucket
    ));
    foreach ($result['Contents'] as $rt) {
        print_r($rt);
    }
} catch (\Exception $e) {
    print_r($e);
}

### 列出帶有前綴的object
try {
    $result = $cosClient->listObjects(array(
        'Bucket' => $bucket,
        'Prefix' => 'string'
    ));
    foreach ($result['Contents'] as $rt) {
        print_r($rt);
    }
} catch (\Exception $e) {
    print_r($e);
}

# 獲取bucket地域
## getBucketLocation
try {
    $result = $cosClient->getBucketLocation(array(
        'Bucket' => 'lewzylu02',
    ));
} catch (\Exception $e) {
    print_r($e);
};

# 多版本相關
## putBucketVersioning(開啓關閉某個bucket的多版本)
try {
    $result = $cosClient->putBucketVersioning(array(
        'Bucket' => $bucket,
        'Status' => 'Enabled'
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## ListObjectVersions(列出多版本object)
/*
 * 同名文件會出現多個版本
 */
try {
    $result = $cosClient->ListObjectVersions(array(
        'Bucket' => $bucket,
        'Prefix' => 'string'
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## getBucketVersioning(獲取某個bucket多版本屬性)
try {
    $result = $cosClient->getBucketVersioning(
        array('Bucket' => $bucket));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# ACL相關
## putBucketACL(設置bucketACL)
try {
    $result = $cosClient->PutBucketAcl(array(
        'Bucket' => $bucket,
        'Grants' => array(
            array(
                'Grantee' => array(
                    'DisplayName' => 'qcs::cam::uin/327874225:uin/327874225',
                    'ID' => 'qcs::cam::uin/327874225:uin/327874225',
                    'Type' => 'CanonicalUser',
                ),
                'Permission' => 'FULL_CONTROL',
            ),
            // ... repeated
        ),
        'Owner' => array(
            'DisplayName' => 'qcs::cam::uin/3210232098:uin/3210232098',
            'ID' => 'qcs::cam::uin/3210232098:uin/3210232098',
        )));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## getBucketACL(獲取bucketACL)
try {
    $result = $cosClient->GetBucketAcl(array(
        'Bucket' => $bucket));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## putObjectACL(設置objectACL)
try {
    $result = $cosClient->putObjectACL(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Grants' => array(
            array(
                'Grantee' => array(
                    'DisplayName' => 'qcs::cam::uin/327874225:uin/327874225',
                    'ID' => 'qcs::cam::uin/327874225:uin/327874225',
                    'Type' => 'CanonicalUser',
                ),
                'Permission' => 'FULL_CONTROL',
            ),
            // ... repeated
        ),
        'Owner' => array(
            'DisplayName' => 'qcs::cam::uin/3210232098:uin/3210232098',
            'ID' => 'qcs::cam::uin/3210232098:uin/3210232098',
        )));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## getObjectACL(獲取objectACL)
try {
    $result = $cosClient->GetObjectAcl(array(
        'Bucket' => $bucket,
        'Key' => $key));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 生命週期相關
## putBucketLifecycle(設置bucket生命週期)
try {
    $result = $cosClient->putBucketLifecycle(array(
        'Bucket' => $bucket,
        'Rules' => array(
            array(
                'Expiration' => array(
                    'Days' => 1000,
                ),
                'ID' => 'id1',
                'Filter' => array(
                    'Prefix' => 'documents/',
                ),
                'Status' => 'Enabled',
                'Transitions' => array(
                    array(
                        'Days' => 200,
                        'StorageClass' => 'NEARLINE'),
                ),
            ),
        )));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## getBucketLifecycle(獲取bucket生命週期)
try {
    $result = $cosClient->getBucketLifecycle(array(
        'Bucket' => $bucket,
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## deleteBucketLifecycle(删除bucket生命周期)
try {
    $result = $cosClient->deleteBucketLifecycle(array(
        'Bucket' => $bucket,
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 跨域相關
## putBucketCors(設置bucket跨域)
try {
    $result = $cosClient->putBucketCors(array(
        'Bucket' => $bucket,
        'CORSRules' => array(
            array(
                'ID' => '1234',
                'AllowedHeaders' => array('*'),
                'AllowedMethods' => array('PUT'),
                'AllowedOrigins' => array('http://www.qq.com'),
            ),
        ),
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## getBucketCors(獲取bucket跨域訊息)
try {
    $result = $cosClient->getBucketCors(array());
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## deleteBucketCors(删除bucket跨域)
try {
    $result = $cosClient->deleteBucketCors(array(
        // Bucket is required
        'Bucket' => $bucket,
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 複制
## copyobject(簡單複制)
/*
 * 将{bucket},{region},{cos_path},{versionId}替換成複制源的真實訊息
 */
try {
    $result = $cosClient->copyObject(array(
        'Bucket' => $bucket,
        'CopySource' => '{bucket}.cos.{region}.myqcloud.com/{cos_path}?versionId={versionId}',
        'Key' => 'string',
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## Copy(分塊并發複制)
/*
 * 将{bucket},{region},{cos_path},{versionId}替換成複制源的真實訊息
 */
try {
    $result = $cosClient->Copy(
        $bucket = $bucket,
        $key = $key,
        $copysource = '{bucket}.cos.{region}.myqcloud.com/{cos_path}',
        $options = array('VersionId' => '{versionId}'
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 恢複歸檔文件
## restoreObject
try {
    $result = $cosClient->restoreObject(array(
        'Bucket' => $bucket,
        'Key' => $key,
        'Days' => 7,
        'CASJobParameters' => array(
            'Tier' => 'Bulk',
        ),
    ));
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

# 其他服務
## 列出某bucket下所有的object
try {
    $prefix = '';
    $marker = '';
    while (true) {
        $result = $cosClient->ListObjects(array(
            'Bucket' => $bucket,
            'Marker' => $marker,
            'MaxKeys' => 1000
        ));
        foreach ($result['Contents'] as $rt) {
            print_r($rt['Key'] . " ");
            /*
             * 使用下面的代碼可以删除全部object
             */
            // try {
            //     $result = $cosClient->deleteobjects(array(
            //         'Bucket' => $bucket,
            //         'Key' => $rt['Key']));
            //     print_r($result);
            // } catch (\Exception $e) {
            //     print_r($e);
            // }
        }
        $marker = $result['NextMarker'];
        if (!$result['IsTruncated']) {
            break;
        }
    }
} catch (\Exception $e) {
    print_r($e);
}

## 删除所有因上傳失敗而産生的分塊
/*
 * 可以清理掉因分塊上傳失敗
 */
try {
    while (true) {
        $result = $cosClient->ListMultipartUploads(
            array('Bucket' => $bucket,
                'Prefix' => ''));
        if (count($result['Uploads']) == 0) {
            break;
        }
        foreach ($result['Uploads'] as $upload) {
            try {
                $rt = $cosClient->AbortMultipartUpload(array(
                    'Bucket' => $bucket,
                    'Key' => $upload['Key'],
                    'UploadId' => $upload['UploadId']
                ));
                print_r($rt);
            } catch (\Exception $e) {
                print_r($e);
            }
        }
    }
} catch (\Exception $e) {
    print_r($e);
}

## 分塊上傳斷點重傳
/*
 * 僅适用于分塊上傳失敗的情況
 * 需要填寫上傳失敗的uploadId
 */
try {
    $result = $cosClient->resumeUpload(
        $bucket = $bucket,
        $key = $key,
        $body = fopen("E:/test.txt", 'rb'),
        $uploadId = '152448808231afdf221eb558ab15d1e455d2afd025c5663936142fdf5614ebf6d1668e2eda'
    );
    print_r($result);
} catch (\Exception $e) {
    print_r($e);
}

## 删除某些前綴的空bucket
function startsWith($haystack, $needle)
{
    $length = strlen($needle);
    return (substr($haystack, 0, $length) === $needle);
}

try {
    $result = $cosClient->listBuckets();
    foreach ($result['Buckets'] as $bucket) {
        $region = $bucket['Location'];
        $name = $bucket['Name'];
        if (startsWith($name, 'lewzylu')) {
            try {
                $cosClient2 = new Qcloud\Cos\Client(array(
                    'region' => $region,
                    'credentials' => array(
                        'secretId' => getenv('COS_KEY'),
                        'secretKey' => getenv('COS_SECRET'))
                ));
                $rt = $cosClient2->deleteBucket(array('Bucket' => $name));
                print_r($rt);
            } catch (\Exception $e) {
            }
        }
    }
} catch (\Exception $e) {
    print_r($e);
}