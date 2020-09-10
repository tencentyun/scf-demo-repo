<?php

namespace Qcloud\Cos;

// http://guzzle3.readthedocs.io/webservice-client/guzzle-service-descriptions.html
class Service {
    public static function getService() {
        return array(
            'name' => 'Cos Service',
            'apiVersion' => 'V5',
            'description' => 'Cos V5 API Service',

            'operations' => array(
                /**
                舍棄一個分塊上傳且删除已上傳的分片塊的方法.

                COS 支援舍棄一個分塊上傳且删除已上傳的分片塊. 注意，已上傳但是未終止的分片塊會占用儲存空間進 而産生儲存費用.因此，建議及時完成分塊上傳 或者舍棄分塊上傳.

                關于分塊上傳的具體描述，請檢視 https://cloud.tencent.com/document/product/436/14112.

                關于舍棄一個分塊上傳且删除已上傳的分片塊介面的描述，請檢視 https://cloud.tencent.com/document/product/436/7740.

                cos php SDK 中舍棄一個分塊上傳且删除已上傳的分片塊請求的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 AbortMultipfartUpload 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則操作成功。
                 */
                'AbortMultipartUpload' => array(
                    'httpMethod' => 'DELETE',
                    'uri' => '/{Bucket}{/Key*}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'AbortMultipartUploadOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri'),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1),
                        'UploadId' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'uploadId')),
                    'errorResponses' => array(
                        array(
                            'reason' => 'The specified multipart upload does not exist.',
                            'class' => 'NoSuchUploadException'))),
                /**
                創建儲存桶（Bucket）的方法.

                在開始使用 COS 時，需要在指定的賬号下先創建一個 Bucket 以便于對象的使用和管理. 并指定 Bucket 所屬的地域.創建 Bucket 的用戶預設成爲 Bucket 的持有者.若創建 Bucket 時沒有指定訪問權限，則預設 爲私有讀寫（private）權限.

                可用地域，可以檢視https://cloud.tencent.com/document/product/436/6224.

                關于創建 Bucket 描述，請檢視 https://cloud.tencent.com/document/product/436/14106.

                關于創建儲存桶（Bucket）介面的具體 描述，請檢視 https://cloud.tencent.com/document/product/436/7738.

                cos php SDK 中創建 Bucket的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 CreateBucket 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則創建成功。

                範例：
                $result = $cosClient->createBucket(array('Bucket' => 'testbucket-1252448703'));
                 */
                'CreateBucket' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'CreateBucketOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'CreateBucketConfiguration')),
                    'parameters' => array(
                        'ACL' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-acl'),
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri')),
                    'errorResponses' => array(
                        array(
                            'reason' => 'The requested bucket name is not available. The bucket namespace is shared by all users of the system. Please select a different name and try again.',
                            'class' => 'BucketAlreadyExistsException'))),
                /**
                完成整個分塊上傳的方法.

                當使用分塊上傳（uploadPart(UploadPartRequest)）完對象的所有塊以後，必須調用該 completeMultiUpload(CompleteMultiUploadRequest) 或者 completeMultiUploadAsync(CompleteMultiUploadRequest, CosXmlResultListener) 來完成整個文件的分塊上傳.且在該請求的 Body 中需要給出每一個塊的 PartNumber 和 ETag，用來校驗塊的準 确性.

                分塊上傳适合于在弱網絡或高頻寬環境下上傳較大的對象.SDK 支援自行切分對象并分别調用uploadPart(UploadPartRequest)上傳各 個分塊.

                關于分塊上傳的描述，請檢視 https://cloud.tencent.com/document/product/436/14112.

                關于完成整個分片上傳介面的描述，請檢視 https://cloud.tencent.com/document/product/436/7742.

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 CompleteMultipartUpload 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則操作成功。

                 */
                'CompleteMultipartUpload' => array(
                    'httpMethod' => 'POST',
                    'uri' => '/{Bucket}{/Key*}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'CompleteMultipartUploadOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'CompleteMultipartUpload')),
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri'),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1),
                        'Parts' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'data' => array(
                                'xmlFlattened' => true),
                            'items' => array(
                                'name' => 'CompletedPart',
                                'type' => 'object',
                                'sentAs' => 'Part',
                                'properties' => array(
                                    'ETag' => array(
                                        'type' => 'string'),
                                    'PartNumber' => array(
                                        'type' => 'numeric')))),
                        'UploadId' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'uploadId'),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml'))),
                'CreateMultipartUpload' => array(
                    'httpMethod' => 'POST',
                    'uri' => '/{Bucket}{/Key*}?uploads',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'CreateMultipartUploadOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'CreateMultipartUploadRequest')),
                    'parameters' => array(
                        'ACL' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-acl',
                        ),
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'CacheControl' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Cache-Control',
                        ),
                        'ContentDisposition' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Disposition',
                        ),
                        'ContentEncoding' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Encoding',
                        ),
                        'ContentLanguage' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Language',
                        ),
                        'ContentType' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Type',
                        ),
                        'Expires' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer',
                            ),
                            'format' => 'date-time-http',
                            'location' => 'header',
                        ),
                        'GrantFullControl' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-full-control',
                        ),
                        'GrantRead' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-read',
                        ),
                        'GrantReadACP' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-read-acp',
                        ),
                        'GrantWriteACP' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-write-acp',
                        ),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1,
                        ),
                        'Metadata' => array(
                            'type' => 'object',
                            'location' => 'header',
                            'sentAs' => 'x-cos-meta-',
                            'additionalProperties' => array(
                                'type' => 'string',
                            ),
                        ),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'StorageClass' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-storage-class',
                        ),
                        'WebsiteRedirectLocation' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-website-redirect-location',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKey' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'SSEKMSKeyId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-aws-kms-key-id',
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ),
                        'ACP' => array(
                            'type' => 'object',
                            'additionalProperties' => true,
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ))),
                'CopyObject' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}{/Key*}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'CopyObjectOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'CopyObjectRequest',
                        ),
                    ),
                    'parameters' => array(
                        'ACL' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-acl',
                        ),
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'CacheControl' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Cache-Control',
                        ),
                        'ContentDisposition' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Disposition',
                        ),
                        'ContentEncoding' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Encoding',
                        ),
                        'ContentLanguage' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Language',
                        ),
                        'ContentType' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Type',
                        ),
                        'CopySource' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source',
                        ),
                        'CopySourceIfMatch' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-if-match',
                        ),
                        'CopySourceIfModifiedSince' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer',
                            ),
                            'format' => 'date-time-http',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-if-modified-since',
                        ),
                        'CopySourceIfNoneMatch' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-if-none-match',
                        ),
                        'CopySourceIfUnmodifiedSince' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer',
                            ),
                            'format' => 'date-time-http',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-if-unmodified-since',
                        ),
                        'Expires' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer',
                            ),
                            'format' => 'date-time-http',
                            'location' => 'header',
                        ),
                        'GrantFullControl' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-full-control',
                        ),
                        'GrantRead' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-read',
                        ),
                        'GrantReadACP' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-read-acp',
                        ),
                        'GrantWriteACP' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-write-acp',
                        ),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1,
                        ),
                        'Metadata' => array(
                            'type' => 'object',
                            'location' => 'header',
                            'sentAs' => 'x-cos-meta-',
                            'additionalProperties' => array(
                                'type' => 'string',
                            ),
                        ),
                        'MetadataDirective' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-metadata-directive',
                        ),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'StorageClass' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-storage-class',
                        ),
                        'WebsiteRedirectLocation' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-website-redirect-location',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKey' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key',
                        ),
                        'CopySourceSSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-server-side-encryption-customer-algorithm',
                        ),
                        'CopySourceSSECustomerKey' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-server-side-encryption-customer-key',
                        ),
                        'CopySourceSSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-server-side-encryption-customer-key-MD5',
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ),
                        'ACP' => array(
                            'type' => 'object',
                            'additionalProperties' => true,
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                    'errorResponses' => array(
                        array(
                            'reason' => 'The source object of the COPY operation is not in the active tier.',
                            'class' => 'ObjectNotInActiveTierErrorException',
                        ),
                    ),
                ),
                /**
                删除儲存桶 (Bucket)的方法.

                COS 目前僅支援删除已經清空的 Bucket，如果 Bucket 中仍有對象，将會删除失敗. 因此，在執行删除 Bucket 前，需确保 Bucket 内已經沒有對象. 删除 Bucket 時，還需要确保操作的身份已被授權該操作，并确認 傳入了正确的儲存桶名稱和地域參數, 請參閱 putBucket(PutBucketRequest).

                關于删除 Bucket 的描述,請檢視 https://cloud.tencent.com/document/product/436/14105.

                關于删除 Bucket 介面的具體描述，請檢視https://cloud.tencent.com/document/product/436/7732.

                cos php SDK 中删除 Bucket 的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 DeleteBucket 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，删除成功。

                範例：
                $result = $cosClient->deleteBucket(array(
                'Bucket' => 'testbucket-1252448703'));
                print_r($result);
                 */
                'DeleteBucket' => array(
                    'httpMethod' => 'DELETE',
                    'uri' => '/{Bucket}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'DeleteBucketOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri'))),
                /**
                删除跨域訪問配置訊息的方法.

                若是 Bucket 不需要支援跨域訪問配置，可以調用此介面删除已配置的跨域訪問訊息. 跨域訪問配置可以通過 putBucketCORS(PutBucketCORSRequest) 或者 putBucketCORSAsync(PutBucketCORSRequest, CosXmlResultListener) 方法來開啓 Bucket 的跨域訪問 支援.

                關于删除跨域訪問配置訊息介面的具體描述，請檢視https://cloud.tencent.com/document/product/436/8283.

                cos php SDK 中删除跨域訪問配置訊息的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 DeleteBucketCORS 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，删除成功。

                範例：
                $result = $cosClient->deleteBucketCors(array(
                // Bucket is required
                'Bucket' => 'testbucket-1252448703',
                ));
                 */
                'DeleteBucketCors' => array(
                    'httpMethod' => 'DELETE',
                    'uri' => '/{Bucket}?cors',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'DeleteBucketCorsOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                    ),
                ),
                /**
                删除 COS 上單個對象的方法.

                COS 支援直接删除一個或多個對象，當僅需要删除一個對象時,只需要提供對象的名稱（即對象鍵)即可.

                關于删除 COS 上單個對象的具體描述，請檢視 https://cloud.tencent.com/document/product/436/14119.

                關于删除 COS 上單個對象介面的具體描述，請檢視 https://cloud.tencent.com/document/product/436/7743.

                cos php SDK 中删除 COS 上單個對象請求的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 DeleteObject 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則删除成功。

                範例：
                $result = $cosClient->deleteObject(array(
                'Bucket' => 'testbucket-1252448703',
                'Key' => '111.txt',
                'VersionId' => 'string'));
                 */
                'DeleteObject' => array(
                    'httpMethod' => 'DELETE',
                    'uri' => '/{Bucket}{/Key*}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'DeleteObjectOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri'),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1),
                        'MFA' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-mfa',
                        ),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'versionId',
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ),)),
                /**
                批次删除 COS 對象的方法.

                COS 支援批次删除指定 Bucket 中 對象，單次請求最大支援批次删除 1000 個 對象. 請求中删除一個不存在的對象，仍然認爲是成功的. 對于響應結果，COS提供 Verbose 和 Quiet 兩種模式：Verbose 模式将返回每個對象的删除結果;Quiet 模式只返回删除報錯的對象訊息. 請求必須攜帶 Content-MD5 用來校驗請求Body 的完整性.

                關于批次删除 COS 對象介面的描述，請檢視https://cloud.tencent.com/document/product/436/8289.

                cos php SDK 中批次删除 COS 對象的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 DeleteObjects 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則删除成功。

                範例：
                $result = $cosClient->deleteObjects(array(
                // Bucket is required
                'Bucket' => 'testbucket-1252448703',
                // Objects is required
                'Objects' => array(
                array(
                // Key is required
                'Key' => 'string',
                'VersionId' => 'string',
                ),
                // ... repeated
                ),
                ));
                 */
                'DeleteObjects' => array(
                    'httpMethod' => 'POST',
                    'uri' => '/{Bucket}?delete',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'DeleteObjectsOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'Delete',
                        ),
                        'contentMd5' => true,
                    ),
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'Objects' => array(
                            'required' => true,
                            'type' => 'array',
                            'location' => 'xml',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'ObjectIdentifier',
                                'type' => 'object',
                                'sentAs' => 'Object',
                                'properties' => array(
                                    'Key' => array(
                                        'required' => true,
                                        'type' => 'string',
                                        'minLength' => 1,
                                    ),
                                    'VersionId' => array(
                                        'type' => 'string',
                                    ),
                                ),
                            ),
                        ),
                        'Quiet' => array(
                            'type' => 'boolean',
                            'format' => 'boolean-string',
                            'location' => 'xml',
                        ),
                        'MFA' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-mfa',
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                ),
                /**
                删除儲存桶（Bucket） 的生命周期配置的方法.

                COS 支援删除已配置的 Bucket 的生命週期清單. COS 支援以生命週期配置的方式來管理 Bucket 中 對象的生命週期，生命週期配置包含一個或多個将 應用于一組對象規則的規則集 (其中每個規則爲 COS 定義一個操作)，請參閱 putBucketLifecycle(PutBucketLifecycleRequest).

                關于删除 Bucket 的生命週期配置介面的具體描述，請檢視https://cloud.tencent.com/document/product/436/8284.

                cos php SDK 中删除 Bucket 的生命週期配置的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 DeleteBucketLifeCycle 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，删除成功。

                範例：
                $result = $cosClient->deleteBucketLifecycle(array(
                // Bucket is required
                'Bucket' =>'testbucket-1252448703',
                ));
                 */
                'DeleteBucketLifecycle' => array(
                    'httpMethod' => 'DELETE',
                    'uri' => '/{Bucket}?lifecycle',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'DeleteBucketLifecycleOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                    ),
                ),
                /**
                删除跨區域複制配置的方法.

                當不需要進行跨區域複制時，可以删除 Bucket 的跨區域複制配置. 跨區域複制，可以查閱putBucketReplication(PutBucketReplicationRequest)

                cos php SDK 中删除跨區域複制配置的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 DeleteBucketReplication 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，獲取成功。

                 */
                'DeleteBucketReplication' => array(
                    'httpMethod' => 'DELETE',
                    'uri' => '/{Bucket}?replication',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'DeleteBucketReplicationOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                    ),
                ),
                'GetObject' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}{/Key*}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'GetObjectOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri'),
                        'IfMatch' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'If-Match'),
                        'IfModifiedSince' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer'),
                            'format' => 'date-time-http',
                            'location' => 'header',
                            'sentAs' => 'If-Modified-Since'),
                        'IfNoneMatch' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'If-None-Match'),
                        'IfUnmodifiedSince' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer'),
                            'format' => 'date-time-http',
                            'location' => 'header',
                            'sentAs' => 'If-Unmodified-Since'),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1),
                        'Range' => array(
                            'type' => 'string',
                            'location' => 'header'),
                        'ResponseCacheControl' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'response-cache-control'),
                        'ResponseContentDisposition' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'response-content-disposition'),
                        'ResponseContentEncoding' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'response-content-encoding'),
                        'ResponseContentLanguage' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'response-content-language'),
                        'ResponseContentType' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'response-content-type'),
                        'ResponseExpires' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer'),
                            'format' => 'date-time-http',
                            'location' => 'query',
                            'sentAs' => 'response-expires'),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'versionId',
                        ),
                        'SaveAs' => array(
                            'location' => 'response_body')),
                    'errorResponses' => array(
                        array(
                            'reason' => 'The specified key does not exist.',
                            'class' => 'NoSuchKeyException'))),
                /**
                獲取 COS 對象的訪問權限訊息（Access Control List, ACL）的方法.

                Bucket 的持有者可獲取該 Bucket 下的某個對象的 ACL 訊息，如被授權者以及被授權的訊息. ACL 權限包括讀、寫、讀寫權限.

                關于獲取 COS 對象的 ACL 介面的具體描述，請檢視https://cloud.tencent.com/document/product/436/7744.

                cos php SDK 中獲取 COS 對象的 ACL 的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 GetObjectAcl 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則獲取成功。

                範例：
                $result = $cosClient->getObjectAcl(array(
                'Bucket' => 'testbucket-1252448703',
                'Key' => '11'));
                 */
                'GetObjectAcl' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}{/Key*}?acl',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'GetObjectAclOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1,
                        ),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'versionId',
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                    'errorResponses' => array(
                        array(
                            'reason' => 'The specified key does not exist.',
                            'class' => 'NoSuchKeyException',
                        ),
                    ),
                ),
                /**
                獲取儲存桶（Bucket) 的訪問權限訊息（Access Control List, ACL）的方法.

                ACL 權限包括讀、寫、讀寫權限. COS 中 Bucket 是有訪問權限控制的.可以通過獲取 Bucket 的 ACL 表(putBucketACL(PutBucketACLRequest))，來檢視那些用戶擁有 Bucket 訪 問權限.

                關于獲取 Bucket 的 ACL 介面的具體描述，請檢視 https://cloud.tencent.com/document/product/436/7733.

                cos php SDK 中獲取 Bucket 的 ACL 的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 GetBucketACL 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則獲取成功。


                範例：
                $result = $cosClient->GetBucketAcl(array(
                'Bucket' => 'testbucket-1252448703',));
                 */
                'GetBucketAcl' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}?acl',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'GetBucketAclOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri'),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml'))),
                /**
                查詢儲存桶（Bucket) 跨域訪問配置訊息的方法.

                COS 支援查詢當前 Bucket 跨域訪問配置訊息，以确定是否配置跨域訊息.當跨域訪問配置不存在時，請求 返回403 Forbidden. 跨域訪問配置可以通過 putBucketCORS(PutBucketCORSRequest) 或者 putBucketCORSAsync(PutBucketCORSRequest, CosXmlResultListener) 方法來開啓 Bucket 的跨域訪問 支援.

                關于查詢 Bucket 跨域訪問配置訊息介面的具體描述， 請檢視 https://cloud.tencent.com/document/product/436/8274.

                cos php SDK 中查詢 Bucket 跨域訪問配置訊息的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 GetBucketCORS 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則獲取成功。


                範例：
                $result = $cosClient->getBucketCors(array(
                // Bucket is required
                'Bucket' => 'testbucket-1252448703',
                ));
                 */
                'GetBucketCors' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}?cors',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'GetBucketCorsOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                ),
                /**
                查詢儲存桶（Bucket) 的生命週期配置的方法.

                COS 支援以生命週期配置的方式來管理 Bucket 中對象的生命週期，生命週期配置包含一個或多個将 應用于一組對象規則的規則集 (其中每個規則爲 COS 定義一個操作)，請參閱 putBucketLifecycle(PutBucketLifecycleRequest).

                關于查詢 Bucket 的生命週期配置介面的具體描述，請檢視https://cloud.tencent.com/document/product/436/8278.

                cos php SDK 中查詢 Bucket 的生命週期配置的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 GetBucketLifecycle 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則獲取成功。


                範例：
                $result = $cosClient->getBucketLifecycle(array(
                'Bucket' => 'testbucket-1252448703',
                ));
                 */
                'GetBucketLifecycle' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}?lifecycle',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'GetBucketLifecycleOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                ),
                /**
                獲取儲存桶（Bucket）版本控制訊息的方法.

                通過查詢版本控制訊息，可以得知該 Bucket 的版本控制功能是處于禁用狀态還是啓用狀态（Enabled 或者 Suspended）, 開啓版本控制功能，可參考putBucketVersioning(PutBucketVersioningRequest).

                cos php SDK 中獲取 Bucket 版本控制訊息的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 GetBucketVersioning 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，獲取成功。

                範例：
                $result = $cosClient->getBucketVersioning(
                array('Bucket' => 'lewzylu02-1252448703'));
                 */
                'GetBucketVersioning' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}?versioning',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'GetBucketVersioningOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                ),
                /**
                獲取跨區域複制配置訊息的方法.

                跨區域複制是支援不同區域 Bucket 自動複制對象, 請查閱putBucketReplication(PutBucketReplicationRequest).

                cos php SDK 中獲取跨區域複制配置訊息的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 GetBucketReplication 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，設置成功。

                 */
                'GetBucketReplication' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}?replication',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'GetBucketReplicationOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                ),
                /**
                獲取儲存桶（Bucket) 所在的地域訊息的方法.

                在創建 Bucket 時，需要指定所屬該 Bucket 所屬地域訊息.

                COS 支援的地域訊息，可檢視https://cloud.tencent.com/document/product/436/6224.

                關于獲取 Bucket 所在的地域訊息介面的具體描述，請檢視https://cloud.tencent.com/document/product/436/8275.

                cos php SDK 中獲取 Bucket 所在的地域訊息的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 GetBucketLocation 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則獲取成功。


                範例：
                $result = $cosClient->getBucketLocation(array(
                'Bucket' => 'testbucket-1252448703',
                ));
                 */
                'GetBucketLocation' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}?location',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'GetBucketLocationOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                    ),
                ),
                'UploadPart' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}{/Key*}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'UploadPartOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'UploadPartRequest')),
                    'parameters' => array(
                        'Body' => array(
                            'type' => array(
                                'string',
                                'object'),
                            'location' => 'body'),
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri'),
                        'ContentLength' => array(
                            'type' => 'numeric',
                            'location' => 'header',
                            'sentAs' => 'Content-Length'),
                        'ContentMD5' => array(
                            'type' => array(
                                'string',
                                'boolean'),
                            'location' => 'header',
                            'sentAs' => 'Content-MD5'),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1),
                        'PartNumber' => array(
                            'required' => true,
                            'type' => 'numeric',
                            'location' => 'query',
                            'sentAs' => 'partNumber'),
                        'UploadId' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'uploadId'),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKey' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ))),
                'PutObject' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}{/Key*}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'PutObjectOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'PutObjectRequest')),
                    'parameters' => array(
                        'ACL' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-acl'),
                        'Body' => array(
                            'type' => array(
                                'string',
                                'object'),
                            'location' => 'body'),
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri'),
                        'CacheControl' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Cache-Control'),
                        'ContentDisposition' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Disposition'),
                        'ContentEncoding' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Encoding'),
                        'ContentLanguage' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Language'),
                        'ContentLength' => array(
                            'type' => 'numeric',
                            'location' => 'header',
                            'sentAs' => 'Content-Length'),
                        'ContentMD5' => array(
                            'type' => array(
                                'string',
                                'boolean'),
                            'location' => 'header',
                            'sentAs' => 'Content-MD5'),
                        'ContentType' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Type'),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1),
                        'Metadata' => array(
                            'type' => 'object',
                            'location' => 'header',
                            'sentAs' => 'x-cos-meta-',
                            'additionalProperties' => array(
                                'type' => 'string')
                        ),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'StorageClass' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-storage-class',
                        ),
                        'WebsiteRedirectLocation' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-website-redirect-location',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKey' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'SSEKMSKeyId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-aws-kms-key-id',
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ),
                        'ACP' => array(
                            'type' => 'object',
                            'additionalProperties' => true,
                        ))),
                /**
                設置 COS 對象的訪問權限訊息（Access Control List, ACL）的方法.

                ACL權限包括讀、寫、讀寫權限. COS 對象的 ACL 可以通過 header頭部："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-write"， "x-cos-grant-full-control" 傳入 ACL 訊息，或者通過 Body 以 XML 格式傳入 ACL 訊息.這兩種方式只 能選擇其中一種，否則引起沖突. 傳入新的 ACL 将函蓋原有 ACL訊息.ACL策略數上限1000，建議用戶不要每個上傳文件都設置 ACL.

                關于設置 COS 對象的ACL介面的具體描述，請檢視https://cloud.tencent.com/document/product/436/7748.

                cos PHP SDK 中設置 COS 對象的 ACL 的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 PutObjectAcl 對象中的方法發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則設置成功。

                範例：
                $cosClient->PutObjectAcl(array(
                'Bucket' => $this->bucket,
                'Key' => '11',
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
                'DisplayName' => 'qcs::cam::uin/2779643970:uin/2779643970',
                'ID' => 'qcs::cam::uin/2779643970:uin/2779643970',
                )));
                 */
                'PutObjectAcl' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}{/Key*}?acl',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'PutObjectAclOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'AccessControlPolicy',
                        ),
                    ),
                    'parameters' => array(
                        'ACL' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-acl',
                        ),
                        'Grants' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'AccessControlList',
                            'items' => array(
                                'name' => 'Grant',
                                'type' => 'object',
                                'properties' => array(
                                    'Grantee' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'DisplayName' => array(
                                                'type' => 'string'),
                                            'ID' => array(
                                                'type' => 'string'),
                                            'Type' => array(
                                                'type' => 'string',
                                                'sentAs' => 'xsi:type',
                                                'data' => array(
                                                    'xmlAttribute' => true,
                                                    'xmlNamespace' => 'http://www.w3.org/2001/XMLSchema-instance')),
                                            'URI' => array(
                                                'type' => 'string') )),
                                    'Permission' => array(
                                        'type' => 'string',
                                    ),
                                ),
                            ),
                        ),
                        'Owner' => array(
                            'type' => 'object',
                            'location' => 'xml',
                            'properties' => array(
                                'DisplayName' => array(
                                    'type' => 'string',
                                ),
                                'ID' => array(
                                    'type' => 'string',
                                ),
                            ),
                        ),
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'GrantFullControl' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-full-control',
                        ),
                        'GrantRead' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-read',
                        ),
                        'GrantReadACP' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-read-acp',
                        ),
                        'GrantWrite' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-write',
                        ),
                        'GrantWriteACP' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-write-acp',
                        ),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1,
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ),
                        'ACP' => array(
                            'type' => 'object',
                            'additionalProperties' => true,
                        ),
                    ),
                    'errorResponses' => array(
                        array(
                            'reason' => 'The specified key does not exist.',
                            'class' => 'NoSuchKeyException',
                        ),
                    ),
                ),
                /**
                設置儲存桶（Bucket） 的訪問權限（Access Control List, ACL)的方法.

                ACL 權限包括讀、寫、讀寫權限. 寫入 Bucket 的 ACL 可以通過 header頭部："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-write"， "x-cos-grant-full-control" 傳入 ACL 訊息，或者通過 Body 以 XML 格式傳入 ACL 訊息.這兩種方式只 能選擇其中一種，否則引起沖突. 傳入新的 ACL 将函蓋原有 ACL訊息. 私有 Bucket 可以下可以給某個文件夾設置成公有，那麽該文件夾下的文件都是公有；但是把文件夾設置成私有後，在該文件夾下的文件設置 的公有屬性，不會生效.

                關于設置 Bucket 的ACL介面的具體描述，請檢視 https://cloud.tencent.com/document/product/436/7737.

                cos php SDK 中設置 Bucket 的ACL的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 PutObjectAcl 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，設置成功。


                範例：
                $result = $cosClient->PutObjectAcl(array(
                'Bucket' => 'testbucket-1252448703',
                'Key' => '111',
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
                ),));
                 */
                'PutBucketAcl' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}?acl',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'PutBucketAclOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'AccessControlPolicy',
                        ),
                    ),
                    'parameters' => array(
                        'ACL' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-acl',
                        ),
                        'Grants' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'AccessControlList',
                            'items' => array(
                                'name' => 'Grant',
                                'type' => 'object',
                                'properties' => array(
                                    'Grantee' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'DisplayName' => array(
                                                'type' => 'string',
                                            ),
                                            'EmailAddress' => array(
                                                'type' => 'string',
                                            ),
                                            'ID' => array(
                                                'type' => 'string',
                                            ),
                                            'Type' => array(
                                                'required' => true,
                                                'type' => 'string',
                                                'sentAs' => 'xsi:type',
                                                'data' => array(
                                                    'xmlAttribute' => true,
                                                    'xmlNamespace' => 'http://www.w3.org/2001/XMLSchema-instance',
                                                ),
                                            ),
                                            'URI' => array(
                                                'type' => 'string',
                                            ),
                                        ),
                                    ),
                                    'Permission' => array(
                                        'type' => 'string',
                                    ),
                                ),
                            ),
                        ),
                        'Owner' => array(
                            'type' => 'object',
                            'location' => 'xml',
                            'properties' => array(
                                'DisplayName' => array(
                                    'type' => 'string',
                                ),
                                'ID' => array(
                                    'type' => 'string',
                                ),
                            ),
                        ),
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'GrantFullControl' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-full-control',
                        ),
                        'GrantRead' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-read',
                        ),
                        'GrantReadACP' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-read-acp',
                        ),
                        'GrantWrite' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-write',
                        ),
                        'GrantWriteACP' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-grant-write-acp',
                        ),
                        'ACP' => array(
                            'type' => 'object',
                            'additionalProperties' => true,
                        ),
                    ),
                ),
                /**
                設置儲存桶（Bucket） 的跨域配置訊息的方法.

                跨域訪問配置的預請求是指在發送跨域請求之前會發送一個 OPTIONS 請求并帶上特定的來源域，HTTP 方 法和 header 訊息等給 COS，以決定是否可以發送真正的跨域請求. 當跨域訪問配置不存在時，請求返回403 Forbidden.

                預設情況下，Bucket的持有者可以直接配置 Bucket的跨域訊息 ，Bucket 持有者也可以将配置權限授予其他用戶.新的配置是函蓋當前的所有配置信 息，而不是新增一條配置.可以通過傳入 XML 格式的配置文件來實現配置，文件大小限制爲64 KB.

                關于設置 Bucket 的跨域配置訊息介面的具體描述，請檢視 https://cloud.tencent.com/document/product/436/8279.

                cos php SDK 中設置 Bucket 的跨域配置訊息的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 PutBucketCORS 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，設置成功。

                範例：
                $result = $cosClient->putBucketCors(array(
                // Bucket is required
                'Bucket' => 'testbucket-1252448703',
                // CORSRules is required
                'CORSRules' => array(
                array(
                'ID' => '1234',
                'AllowedHeaders' => array('*'),
                // AllowedMethods is required
                'AllowedMethods' => array('PUT'),
                // AllowedOrigins is required
                'AllowedOrigins' => array('http://www.qq.com', ),
                ),
                // ... repeated
                ),
                ));
                 */
                'PutBucketCors' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}?cors',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'PutBucketCorsOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'CORSConfiguration',
                        ),
                        'contentMd5' => true,
                    ),
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'CORSRules' => array(
                            'required' => true,
                            'type' => 'array',
                            'location' => 'xml',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'CORSRule',
                                'type' => 'object',
                                'sentAs' => 'CORSRule',
                                'properties' => array(
                                    'ID' => array(
                                        'type' => 'string',
                                    ),
                                    'AllowedHeaders' => array(
                                        'type' => 'array',
                                        'data' => array(
                                            'xmlFlattened' => true,
                                        ),
                                        'items' => array(
                                            'name' => 'AllowedHeader',
                                            'type' => 'string',
                                            'sentAs' => 'AllowedHeader',
                                        ),
                                    ),
                                    'AllowedMethods' => array(
                                        'required' => true,
                                        'type' => 'array',
                                        'data' => array(
                                            'xmlFlattened' => true,
                                        ),
                                        'items' => array(
                                            'name' => 'AllowedMethod',
                                            'type' => 'string',
                                            'sentAs' => 'AllowedMethod',
                                        ),
                                    ),
                                    'AllowedOrigins' => array(
                                        'required' => true,
                                        'type' => 'array',
                                        'data' => array(
                                            'xmlFlattened' => true,
                                        ),
                                        'items' => array(
                                            'name' => 'AllowedOrigin',
                                            'type' => 'string',
                                            'sentAs' => 'AllowedOrigin',
                                        ),
                                    ),
                                    'ExposeHeaders' => array(
                                        'type' => 'array',
                                        'data' => array(
                                            'xmlFlattened' => true,
                                        ),
                                        'items' => array(
                                            'name' => 'ExposeHeader',
                                            'type' => 'string',
                                            'sentAs' => 'ExposeHeader',
                                        ),
                                    ),
                                    'MaxAgeSeconds' => array(
                                        'type' => 'numeric',
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                /**
                設置儲存桶（Bucket) 生命週期配置的方法.

                COS 支援以生命週期配置的方式來管理 Bucket 中對象的生命週期. 如果該 Bucket 已配置生命週期，新的配置的同時則會函蓋原有的配置. 生命週期配置包含一個或多個将應用于一組對象規則的規則集 (其中每個規則爲 COS 定義一個操作)。這些操作分爲以下兩種：轉換操作，過期操作.

                轉換操作,定義對象轉換爲另一個儲存類的時間(例如，您可以選擇在對象創建 30 天後将其轉換爲低頻儲存類别，同 時也支援将數據沉降到歸檔儲存類别.

                過期操作，指定 Object 的過期時間，COS 将會自動爲用戶删除過期的 Object.

                關于Bucket 生命週期配置介面的具體描述，請檢視 https://cloud.tencent.com/document/product/436/8280

                cos php SDK 中Bucket 生命週期配置的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 PutBucketLifecycle 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，設置成功。

                範例：
                $result = $cosClient->putBucketLifecycle(array(
                // Bucket is required
                'Bucket' => 'lewzylu06-1252448703',
                // Rules is required
                'Rules' => array(
                array(
                'Expiration' => array(
                'Days' => 1000,
                ),
                'ID' => 'id1',
                'Filter' => array(
                'Prefix' => 'documents/'
                ),
                // Status is required
                'Status' => 'Enabled',
                'Transitions' => array(
                array(
                'Days' => 200,
                'StorageClass' => 'NEARLINE'),
                ),
                // ... repeated
                ),
                )));
                 */
                'PutBucketLifecycle' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}?lifecycle',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'PutBucketLifecycleOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'LifecycleConfiguration',
                        ),
                        'contentMd5' => true,
                    ),
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'Rules' => array(
                            'required' => true,
                            'type' => 'array',
                            'location' => 'xml',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'Rule',
                                'type' => 'object',
                                'sentAs' => 'Rule',
                                'properties' => array(
                                    'Expiration' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'Date' => array(
                                                'type' => array(
                                                    'object',
                                                    'string',
                                                    'integer',
                                                ),
                                                'format' => 'date-time',
                                            ),
                                            'Days' => array(
                                                'type' => 'numeric',
                                            ),
                                        ),
                                    ),
                                    'ID' => array(
                                        'type' => 'string',
                                    ),
                                    'Filter' => array(
                                        'type' => 'object',
                                        'require' => true,
                                        'properties' => array(
                                            'Prefix' => array(
                                                'type' => 'string',
                                                'require' => true,
                                            ),
                                            'Tag' => array(
                                                'type' => 'object',
                                                'require' => true,
                                                'properties' => array(
                                                    'Key' => array(
                                                        'type' => 'string'
                                                    ),
                                                    'Value' => array(
                                                        'type' => 'string'
                                                    ),
                                                )
                                            )
                                        ),
                                    ),
                                    'Status' => array(
                                        'required' => true,
                                        'type' => 'string',
                                    ),
                                    'Transitions' => array(
                                        'required' => true,
                                        'type' => 'array',
                                        'location' => 'xml',
                                        'data' => array(
                                            'xmlFlattened' => true,
                                        ),
                                        'items' => array(
                                            'name' => 'Transition',
                                            'type' => 'object',
                                            'sentAs' => 'Transition',
                                            'properties' => array(
                                                'Date' => array(
                                                    'type' => array(
                                                        'object',
                                                        'string',
                                                        'integer',
                                                    ),
                                                    'format' => 'date-time',
                                                ),
                                                'Days' => array(
                                                    'type' => 'numeric',
                                                ),
                                                'StorageClass' => array(
                                                    'type' => 'string',
                                                )))),
                                    'NoncurrentVersionTransition' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'NoncurrentDays' => array(
                                                'type' => 'numeric',
                                            ),
                                            'StorageClass' => array(
                                                'type' => 'string',
                                            ),
                                        ),
                                    ),
                                    'NoncurrentVersionExpiration' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'NoncurrentDays' => array(
                                                'type' => 'numeric',
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                /**
                儲存桶（Bucket）版本控制的方法.

                版本管理功能一經打開，只能暫停，不能關閉. 通過版本控制，可以在一個 Bucket 中保留一個對象的多個版本. 版本控制可以防止意外函蓋和删除對象，以便檢索早期版本的對象. 預設情況下，版本控制功能處于禁用狀态，需要主動去啓用或者暫停（Enabled 或者 Suspended）.

                cos php SDK 中 Bucket 版本控制啓用或者暫停的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 PutBucketVersioning 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，設置成功。

                範例：
                $result = $cosClient->putBucketVersioning(
                array('Bucket' => 'testbucket-1252448703',
                'Status' => 'Enabled'));
                 */
                'PutBucketVersioning' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}?versioning',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'PutBucketVersioningOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'VersioningConfiguration',
                        ),
                    ),
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'MFA' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-mfa',
                        ),
                        'MFADelete' => array(
                            'type' => 'string',
                            'location' => 'xml',
                            'sentAs' => 'MfaDelete',
                        ),
                        'Status' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                    ),
                ),
                /**
                配置跨區域複制的方法.

                跨區域複制是支援不同區域 Bucket 自動異步複制對象.注意，不能是同區域的 Bucket, 且源 Bucket 和目 标 Bucket 必須已啓用版本控制putBucketVersioning(PutBucketVersioningRequest).

                cos php SDK 中配置跨區域複制的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 PutBucketRelication 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，設置成功。

                範例：

                 */
                'PutBucketReplication' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}?replication',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'PutBucketReplicationOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'ReplicationConfiguration',
                        ),
                        'contentMd5' => true,
                    ),
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'Role' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Rules' => array(
                            'required' => true,
                            'type' => 'array',
                            'location' => 'xml',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'ReplicationRule',
                                'type' => 'object',
                                'sentAs' => 'Rule',
                                'properties' => array(
                                    'ID' => array(
                                        'type' => 'string',
                                    ),
                                    'Prefix' => array(
                                        'required' => true,
                                        'type' => 'string',
                                    ),
                                    'Status' => array(
                                        'required' => true,
                                        'type' => 'string',
                                    ),
                                    'Destination' => array(
                                        'required' => true,
                                        'type' => 'object',
                                        'properties' => array(
                                            'Bucket' => array(
                                                'required' => true,
                                                'type' => 'string',
                                            ),
                                            'StorageClass' => array(
                                                'type' => 'string',
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                'RestoreObject' => array(
                    'httpMethod' => 'POST',
                    'uri' => '/{Bucket}{/Key*}?restore',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'RestoreObjectOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'RestoreRequest',
                        ),
                    ),
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1,
                        ),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'versionId',
                        ),
                        'Days' => array(
                            'required' => true,
                            'type' => 'numeric',
                            'location' => 'xml',
                        ),
                        'CASJobParameters' => array(
                            'type' => 'object',
                            'location' => 'xml',
                            'properties' => array(
                                'Tier' => array(
                                    'type' => 'string',
                                    'required' => true,
                                ),
                            ),
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ),
                    ),
                    'errorResponses' => array(
                        array(
                            'reason' => 'This operation is not allowed against this storage tier',
                            'class' => 'ObjectAlreadyInActiveTierErrorException',
                        ),
                    ),
                ),
                /**
                查詢儲存桶（Bucket）中正在進行中的分塊上傳對象的方法.

                COS 支援查詢 Bucket 中有哪些正在進行中的分塊上傳對象，單次請求操作最多列出 1000 個正在進行中的 分塊上傳對象.

                關于查詢 Bucket 中正在進行中的分塊上傳對象介面的具體描述，請檢視 https://cloud.tencent.com/document/product/436/7736.

                cos php SDK 中查詢 Bucket 中正在進行中的分塊上傳對象的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 ListParts 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，獲取成功。

                 */
                'ListParts' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}{/Key*}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'ListPartsOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri'),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1),
                        'MaxParts' => array(
                            'type' => 'numeric',
                            'location' => 'query',
                            'sentAs' => 'max-parts'),
                        'PartNumberMarker' => array(
                            'type' => 'numeric',
                            'location' => 'query',
                            'sentAs' => 'part-number-marker'),
                        'UploadId' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'uploadId'),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml'))),
                /**
                查詢儲存桶（Bucket) 下的部分或者全部對象的方法.

                COS 支援列出指定 Bucket 下的部分或者全部對象.

                每次預設返回的最大條目數爲 1000 條.

                如果無法一次返回所有的對象，則返回結果中的 IsTruncated 爲 true，同時會附加一個 NextMarker 欄位，提示下 一個條目的起點.

                若一次請求，已經返回了全部對象，則不會有 NextMarker 這個欄位，同時 IsTruncated 爲 false.

                若把 prefix 設置爲某個文件夾的全路徑名，則可以列出以此 prefix 爲開頭的文件，即該文件 夾下遞歸的所有文件和子文件夾.

                如果再設置 delimiter 定界符爲 “/”，則只列出該文件夾下的文件，子文件夾下遞歸的文件和文件夾名 将不被列出.而子文件夾名将會以 CommonPrefix 的形式給出.

                關于查詢Bucket 下的部分或者全部對象介面的具體描述，請檢視https://cloud.tencent.com/document/product/436/7734.

                cos php SDK 中查詢 Bucket 下的部分或者全部對象的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 ListObjects 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，則list成功。

                範例：
                $result = $cosClient->ListObjects(array(
                'Bucket' =>  'testbucket-1252448703'));
                 */
                'ListObjects' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'ListObjectsOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri'),
                        'Delimiter' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'delimiter'),
                        'EncodingType' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'encoding-type'),
                        'Marker' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'marker'),
                        'MaxKeys' => array(
                            'type' => 'numeric',
                            'location' => 'query',
                            'sentAs' => 'max-keys'),
                        'Prefix' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'prefix'),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml')),
                    'errorResponses' => array(
                        array(
                            'reason' => 'The specified bucket does not exist.',
                            'class' => 'NoSuchBucketException'))),
                /**
                獲取所屬帳戶的所有儲存空間清單的方法.

                通過使用帯 Authorization 簽名認證的請求，可以獲取簽名中 APPID 所屬帳戶的所有儲存空間清單 (Bucket list).

                關于獲取所有儲存空間清單介面的具體描述，請檢視https://cloud.tencent.com/document/product/436/8291.

                cos php SDK 中獲取所屬帳戶的所有儲存空間清單的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 ListBuckets 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，獲取成功。

                範例：
                $result = $cosClient->listBuckets();
                print_r($result);
                 */
                'ListBuckets' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'ListBucketsOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                ),
                'ListObjectVersions' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}?versions',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'ListObjectVersionsOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'Delimiter' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'delimiter',
                        ),
                        'EncodingType' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'encoding-type',
                        ),
                        'KeyMarker' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'key-marker',
                        ),
                        'MaxKeys' => array(
                            'type' => 'numeric',
                            'location' => 'query',
                            'sentAs' => 'max-keys',
                        ),
                        'Prefix' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'prefix',
                        ),
                        'VersionIdMarker' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'version-id-marker',
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                ),
                'ListMultipartUploads' => array(
                    'httpMethod' => 'GET',
                    'uri' => '/{Bucket}?uploads',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'ListMultipartUploadsOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'Delimiter' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'delimiter',
                        ),
                        'EncodingType' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'encoding-type',
                        ),
                        'KeyMarker' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'key-marker',
                        ),
                        'MaxUploads' => array(
                            'type' => 'numeric',
                            'location' => 'query',
                            'sentAs' => 'max-uploads',
                        ),
                        'Prefix' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'prefix',
                        ),
                        'UploadIdMarker' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'upload-id-marker',
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                ),
                'HeadObject' => array(
                    'httpMethod' => 'HEAD',
                    'uri' => '/{Bucket}{/Key*}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'HeadObjectOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'IfMatch' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'If-Match',
                        ),
                        'IfModifiedSince' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer',
                            ),
                            'format' => 'date-time-http',
                            'location' => 'header',
                            'sentAs' => 'If-Modified-Since',
                        ),
                        'IfNoneMatch' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'If-None-Match',
                        ),
                        'IfUnmodifiedSince' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer',
                            ),
                            'format' => 'date-time-http',
                            'location' => 'header',
                            'sentAs' => 'If-Unmodified-Since',
                        ),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1,
                        ),
                        'Range' => array(
                            'type' => 'string',
                            'location' => 'header',
                        ),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'versionId',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKey' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ),
                    ),
                    'errorResponses' => array(
                        array(
                            'reason' => 'The specified key does not exist.',
                            'class' => 'NoSuchKeyException',
                        ),
                    ),
                ),
                /**
                儲存桶（Bucket） 是否存在的方法.

                在開始使用 COS 時，需要确認該 Bucket 是否存在，是否有權限訪問.若不存在，則可以調用putBucket(PutBucketRequest) 創建.

                關于确認該 Bucket 是否存在，是否有權限訪問介面的具體描述，請檢視https://cloud.tencent.com/document/product/436/7735.

                cos php SDK 中Bucket 是否存在的方法具體步驟如下：

                1. 初始化用戶端cosClient，填入儲存桶名，和一些額外需要的參數，如授權的具體訊息等。

                2. 調用 HeadBucket 介面發出請求。

                3. 接收該介面的返回數據，若沒有抛出異常，獲取成功。

                範例：
                $result = $cosClient->headObject(array(
                'Bucket' => 'testbucket-1252448703',
                'Key' => '11',
                'VersionId' =>'111',
                'ServerSideEncryption' => 'AES256'));
                 */
                'HeadBucket' => array(
                    'httpMethod' => 'HEAD',
                    'uri' => '/{Bucket}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'HeadBucketOutput',
                    'responseType' => 'model',
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                    ),
                    'errorResponses' => array(
                        array(
                            'reason' => 'The specified bucket does not exist.',
                            'class' => 'NoSuchBucketException',
                        ),
                    ),
                ),
                'UploadPartCopy' => array(
                    'httpMethod' => 'PUT',
                    'uri' => '/{Bucket}{/Key*}',
                    'class' => 'Qcloud\\Cos\\Command',
                    'responseClass' => 'UploadPartCopyOutput',
                    'responseType' => 'model',
                    'data' => array(
                        'xmlRoot' => array(
                            'name' => 'UploadPartCopyRequest',
                        ),
                    ),
                    'parameters' => array(
                        'Bucket' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                        ),
                        'CopySource' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source',
                        ),
                        'CopySourceIfMatch' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-if-match',
                        ),
                        'CopySourceIfModifiedSince' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer',
                            ),
                            'format' => 'date-time-http',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-if-modified-since',
                        ),
                        'CopySourceIfNoneMatch' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-if-none-match',
                        ),
                        'CopySourceIfUnmodifiedSince' => array(
                            'type' => array(
                                'object',
                                'string',
                                'integer',
                            ),
                            'format' => 'date-time-http',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-if-unmodified-since',
                        ),
                        'CopySourceRange' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-range',
                        ),
                        'Key' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'uri',
                            'minLength' => 1,
                        ),
                        'PartNumber' => array(
                            'required' => true,
                            'type' => 'numeric',
                            'location' => 'query',
                            'sentAs' => 'partNumber',
                        ),
                        'UploadId' => array(
                            'required' => true,
                            'type' => 'string',
                            'location' => 'query',
                            'sentAs' => 'uploadId',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKey' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'CopySourceSSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-server-side-encryption-customer-algorithm',
                        ),
                        'CopySourceSSECustomerKey' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-server-side-encryption-customer-key',
                        ),
                        'CopySourceSSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-server-side-encryption-customer-key-MD5',
                        ),
                        'RequestPayer' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-payer',
                        ),
                        'command.expects' => array(
                            'static' => true,
                            'default' => 'application/xml',
                        ),
                    ),
                ),),
            'models' => array(
                'AbortMultipartUploadOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id'))),
                'CreateBucketOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Location' => array(
                            'type' => 'string',
                            'location' => 'header'),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id'))),
                'CompleteMultipartUploadOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Location' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Bucket' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Key' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Expiration' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-expiration',
                        ),
                        'ETag' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-version-id',
                        ),
                        'SSEKMSKeyId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-aws-kms-key-id',
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'CreateMultipartUploadOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Bucket' => array(
                            'type' => 'string',
                            'location' => 'xml',
                            'sentAs' => 'Bucket'),
                        'Key' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'UploadId' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'SSEKMSKeyId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-aws-kms-key-id',
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ))),
                'CopyObjectOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'ETag' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'LastModified' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Expiration' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-expiration',
                        ),
                        'CopySourceVersionId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-version-id',
                        ),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-version-id',
                        ),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'DeleteBucketOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id'))),
                'DeleteBucketCorsOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'DeleteObjectOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'DeleteMarker' => array(
                            'type' => 'boolean',
                            'location' => 'header',
                            'sentAs' => 'x-cos-delete-marker',
                        ),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-version-id',
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'DeleteObjectsOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Deleted' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'DeletedObject',
                                'type' => 'object',
                                'properties' => array(
                                    'Key' => array(
                                        'type' => 'string',
                                    ),
                                    'VersionId' => array(
                                        'type' => 'string',
                                    ),
                                    'DeleteMarker' => array(
                                        'type' => 'boolean',
                                    ),
                                    'DeleteMarkerVersionId' => array(
                                        'type' => 'string',
                                    ),
                                ),
                            ),
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'Errors' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'Error',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'Error',
                                'type' => 'object',
                                'sentAs' => 'Error',
                                'properties' => array(
                                    'Key' => array(
                                        'type' => 'string',
                                    ),
                                    'VersionId' => array(
                                        'type' => 'string',
                                    ),
                                    'Code' => array(
                                        'type' => 'string',
                                    ),
                                    'Message' => array(
                                        'type' => 'string',
                                    ),
                                ),
                            ),
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'DeleteBucketLifecycleOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'DeleteBucketReplicationOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'GetObjectOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Body' => array(
                            'type' => 'string',
                            'instanceOf' => 'Guzzle\\Http\\EntityBody',
                            'location' => 'body',
                        ),
                        'DeleteMarker' => array(
                            'type' => 'boolean',
                            'location' => 'header',
                            'sentAs' => 'x-cos-delete-marker',
                        ),
                        'AcceptRanges' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'accept-ranges',
                        ),
                        'Expiration' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-expiration',
                        ),
                        'Restore' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-restore',
                        ),
                        'LastModified' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Last-Modified',
                        ),
                        'ContentLength' => array(
                            'type' => 'numeric',
                            'location' => 'header',
                            'sentAs' => 'Content-Length',
                        ),
                        'ETag' => array(
                            'type' => 'string',
                            'location' => 'header',
                        ),
                        'MissingMeta' => array(
                            'type' => 'numeric',
                            'location' => 'header',
                            'sentAs' => 'x-cos-missing-meta',
                        ),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-version-id',
                        ),
                        'CacheControl' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Cache-Control',
                        ),
                        'ContentDisposition' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Disposition',
                        ),
                        'ContentEncoding' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Encoding',
                        ),
                        'ContentLanguage' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Language',
                        ),
                        'ContentRange' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Range',
                        ),
                        'ContentType' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Type',
                        ),
                        'Expires' => array(
                            'type' => 'string',
                            'location' => 'header',
                        ),
                        'WebsiteRedirectLocation' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-website-redirect-location',
                        ),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'Metadata' => array(
                            'type' => 'object',
                            'location' => 'header',
                            'sentAs' => 'x-cos-meta-',
                            'additionalProperties' => array(
                                'type' => 'string',
                            ),
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'SSEKMSKeyId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-aws-kms-key-id',
                        ),
                        'StorageClass' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-storage-class',
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'ReplicationStatus' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-replication-status',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'GetObjectAclOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Owner' => array(
                            'type' => 'object',
                            'location' => 'xml',
                            'properties' => array(
                                'DisplayName' => array(
                                    'type' => 'string',
                                ),
                                'ID' => array(
                                    'type' => 'string',
                                ),
                            ),
                        ),
                        'Grants' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'AccessControlList',
                            'items' => array(
                                'name' => 'Grant',
                                'type' => 'object',
                                'sentAs' => 'Grant',
                                'properties' => array(
                                    'Grantee' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'DisplayName' => array(
                                                'type' => 'string'),
                                            /*
                                                'EmailAddress' => array(
                                                    'type' => 'string'),
                                                */
                                            'ID' => array(
                                                'type' => 'string'),
                                            /*
                                                'Type' => array(
                                                    'type' => 'string',
                                                    'sentAs' => 'xsi:type',
                                                    'data' => array(
                                                        'xmlAttribute' => true,
                                                        'xmlNamespace' => 'http://www.w3.org/2001/XMLSchema-instance')),
                                                */
                                            /*'URI' => array(
                                                    'type' => 'string') */)),
                                    'Permission' => array(
                                        'type' => 'string',
                                    ),
                                ),
                            ),
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'GetBucketAclOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Owner' => array(
                            'type' => 'object',
                            'location' => 'xml',
                            'properties' => array(
                                'DisplayName' => array(
                                    'type' => 'string'),
                                'ID' => array(
                                    'type' => 'string'))),
                        'Grants' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'AccessControlList',
                            'items' => array(
                                'name' => 'Grant',
                                'type' => 'object',
                                'sentAs' => 'Grant',
                                'properties' => array(
                                    'Grantee' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'DisplayName' => array(
                                                'type' => 'string'),
                                            /*
                                                'EmailAddress' => array(
                                                    'type' => 'string'),
                                                */
                                            'ID' => array(
                                                'type' => 'string'),
                                            /*
                                                'Type' => array(
                                                    'type' => 'string',
                                                    'sentAs' => 'xsi:type',
                                                    'data' => array(
                                                        'xmlAttribute' => true,
                                                        'xmlNamespace' => 'http://www.w3.org/2001/XMLSchema-instance')),
                                                */
                                            /*'URI' => array(
                                                    'type' => 'string') */)),
                                    'Permission' => array(
                                        'type' => 'string')))),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id'))),
                'GetBucketCorsOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'CORSRules' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'CORSRule',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'CORSRule',
                                'type' => 'object',
                                'sentAs' => 'CORSRule',
                                'properties' => array(
                                    'ID' => array(
                                        'type' => 'string'),
                                    'AllowedHeaders' => array(
                                        'type' => 'array',
                                        'sentAs' => 'AllowedHeader',
                                        'data' => array(
                                            'xmlFlattened' => true,
                                        ),
                                        'items' => array(
                                            'name' => 'AllowedHeader',
                                            'type' => 'string',
                                            'sentAs' => 'AllowedHeader',
                                        ),
                                    ),
                                    'AllowedMethods' => array(
                                        'type' => 'array',
                                        'sentAs' => 'AllowedMethod',
                                        'data' => array(
                                            'xmlFlattened' => true,
                                        ),
                                        'items' => array(
                                            'name' => 'AllowedMethod',
                                            'type' => 'string',
                                            'sentAs' => 'AllowedMethod',
                                        ),
                                    ),
                                    'AllowedOrigins' => array(
                                        'type' => 'array',
                                        'sentAs' => 'AllowedOrigin',
                                        'data' => array(
                                            'xmlFlattened' => true,
                                        ),
                                        'items' => array(
                                            'name' => 'AllowedOrigin',
                                            'type' => 'string',
                                            'sentAs' => 'AllowedOrigin',
                                        ),
                                    ),
                                    'ExposeHeaders' => array(
                                        'type' => 'array',
                                        'sentAs' => 'ExposeHeader',
                                        'data' => array(
                                            'xmlFlattened' => true,
                                        ),
                                        'items' => array(
                                            'name' => 'ExposeHeader',
                                            'type' => 'string',
                                            'sentAs' => 'ExposeHeader',
                                        ),
                                    ),
                                    'MaxAgeSeconds' => array(
                                        'type' => 'numeric',
                                    ),
                                ),
                            ),
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'GetBucketLifecycleOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Rules' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'Rule',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'Rule',
                                'type' => 'object',
                                'sentAs' => 'Rule',
                                'properties' => array(
                                    'Expiration' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'Date' => array(
                                                'type' => 'string',
                                            ),
                                            'Days' => array(
                                                'type' => 'numeric',
                                            ),
                                        ),
                                    ),
                                    'ID' => array(
                                        'type' => 'string',
                                    ),
                                    'Filter' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'Prefix' => array(
                                                'type' => 'string',
                                            ),
                                            'Tag' => array(
                                                'type' => 'object',
                                                'properties' => array(
                                                    'Key' => array(
                                                        'type' => 'string'
                                                    ),
                                                    'Value' => array(
                                                        'type' => 'string'
                                                    ),
                                                )
                                            )
                                        ),
                                    ),
                                    'Status' => array(
                                        'type' => 'string',
                                    ),
                                    'Transition' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'Date' => array(
                                                'type' => 'string',
                                            ),
                                            'Days' => array(
                                                'type' => 'numeric',
                                            ),
                                            'StorageClass' => array(
                                                'type' => 'string',
                                            ),
                                        ),
                                    ),
                                    'NoncurrentVersionTransition' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'NoncurrentDays' => array(
                                                'type' => 'numeric',
                                            ),
                                            'StorageClass' => array(
                                                'type' => 'string',
                                            ),
                                        ),
                                    ),
                                    'NoncurrentVersionExpiration' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'NoncurrentDays' => array(
                                                'type' => 'numeric',
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'GetBucketVersioningOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Status' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'MFADelete' => array(
                            'type' => 'string',
                            'location' => 'xml',
                            'sentAs' => 'MfaDelete',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'GetBucketReplicationOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Role' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Rules' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'Rule',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'ReplicationRule',
                                'type' => 'object',
                                'sentAs' => 'Rule',
                                'properties' => array(
                                    'ID' => array(
                                        'type' => 'string',
                                    ),
                                    'Prefix' => array(
                                        'type' => 'string',
                                    ),
                                    'Status' => array(
                                        'type' => 'string',
                                    ),
                                    'Destination' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'Bucket' => array(
                                                'type' => 'string',
                                            ),
                                            'StorageClass' => array(
                                                'type' => 'string',
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'GetBucketLocationOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Location' => array(
                            'type' => 'string',
                            'location' => 'body',
                            'filters' => array(
                                'strval',
                                'strip_tags',
                                'trim',
                            ),
                        ),
                    ),
                ),
                'UploadPartOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'ETag' => array(
                            'type' => 'string',
                            'location' => 'header',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'SSEKMSKeyId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-aws-kms-key-id',
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'UploadPartCopyOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'CopySourceVersionId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-copy-source-version-id',
                        ),
                        'ETag' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'LastModified' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'SSEKMSKeyId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-aws-kms-key-id',
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'PutBucketAclOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id'))),
                'PutObjectOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Expiration' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-expiration',
                        ),
                        'ETag' => array(
                            'type' => 'string',
                            'location' => 'header',
                        ),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-version-id',
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'SSEKMSKeyId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-aws-kms-key-id',
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'PutObjectAclOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'PutBucketCorsOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'PutBucketLifecycleOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'PutBucketVersioningOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'PutBucketReplicationOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'RestoreObjectOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'ListPartsOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Bucket' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'Key' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'UploadId' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'PartNumberMarker' => array(
                            'type' => 'numeric',
                            'location' => 'xml'),
                        'NextPartNumberMarker' => array(
                            'type' => 'numeric',
                            'location' => 'xml'),
                        'MaxParts' => array(
                            'type' => 'numeric',
                            'location' => 'xml'),
                        'IsTruncated' => array(
                            'type' => 'boolean',
                            'location' => 'xml'),
                        'Parts' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'Part',
                            'data' => array(
                                'xmlFlattened' => true),
                            'items' => array(
                                'name' => 'Part',
                                'type' => 'object',
                                'sentAs' => 'Part',
                                'properties' => array(
                                    'PartNumber' => array(
                                        'type' => 'numeric'),
                                    'LastModified' => array(
                                        'type' => 'string'),
                                    'ETag' => array(
                                        'type' => 'string'),
                                    'Size' => array(
                                        'type' => 'numeric')))),
                        'Initiator' => array(
                            'type' => 'object',
                            'location' => 'xml',
                            'properties' => array(
                                'ID' => array(
                                    'type' => 'string'),
                                'DisplayName' => array(
                                    'type' => 'string'))),
                        'Owner' => array(
                            'type' => 'object',
                            'location' => 'xml',
                            'properties' => array(
                                'DisplayName' => array(
                                    'type' => 'string'),
                                'ID' => array(
                                    'type' => 'string'))),
                        'StorageClass' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id'))),
                'ListObjectsOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'IsTruncated' => array(
                            'type' => 'boolean',
                            'location' => 'xml'),
                        'Marker' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'NextMarker' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'Contents' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'data' => array(
                                'xmlFlattened' => true),
                            'items' => array(
                                'name' => 'Object',
                                'type' => 'object',
                                'properties' => array(
                                    'Key' => array(
                                        'type' => 'string'),
                                    'LastModified' => array(
                                        'type' => 'string'),
                                    'ETag' => array(
                                        'type' => 'string'),
                                    'Size' => array(
                                        'type' => 'numeric'),
                                    'StorageClass' => array(
                                        'type' => 'string'),
                                    'Owner' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'DisplayName' => array(
                                                'type' => 'string'),
                                            'ID' => array(
                                                'type' => 'string')))))),
                        'Name' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'Prefix' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'Delimiter' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'MaxKeys' => array(
                            'type' => 'numeric',
                            'location' => 'xml'),
                        'CommonPrefixes' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'data' => array(
                                'xmlFlattened' => true),
                            'items' => array(
                                'name' => 'CommonPrefix',
                                'type' => 'object',
                                'properties' => array(
                                    'Prefix' => array(
                                        'type' => 'string')))),
                        'EncodingType' => array(
                            'type' => 'string',
                            'location' => 'xml'),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id'))),
                'ListBucketsOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Buckets' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'items' => array(
                                'name' => 'Bucket',
                                'type' => 'object',
                                'sentAs' => 'Bucket',
                                'properties' => array(
                                    'Name' => array(
                                        'type' => 'string',
                                    ),
                                    'CreationDate' => array(
                                        'type' => 'string',
                                    ),
                                ),
                            ),
                        ),
                        'Owner' => array(
                            'type' => 'object',
                            'location' => 'xml',
                            'properties' => array(
                                'DisplayName' => array(
                                    'type' => 'string',
                                ),
                                'ID' => array(
                                    'type' => 'string',
                                ),
                            ),
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'ListObjectVersionsOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'IsTruncated' => array(
                            'type' => 'boolean',
                            'location' => 'xml',
                        ),
                        'KeyMarker' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'VersionIdMarker' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'NextKeyMarker' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'NextVersionIdMarker' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Versions' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'Version',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'ObjectVersion',
                                'type' => 'object',
                                'sentAs' => 'Version',
                                'properties' => array(
                                    'ETag' => array(
                                        'type' => 'string',
                                    ),
                                    'Size' => array(
                                        'type' => 'numeric',
                                    ),
                                    'StorageClass' => array(
                                        'type' => 'string',
                                    ),
                                    'Key' => array(
                                        'type' => 'string',
                                    ),
                                    'VersionId' => array(
                                        'type' => 'string',
                                    ),
                                    'IsLatest' => array(
                                        'type' => 'boolean',
                                    ),
                                    'LastModified' => array(
                                        'type' => 'string',
                                    ),
                                    'Owner' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'DisplayName' => array(
                                                'type' => 'string',
                                            ),
                                            'ID' => array(
                                                'type' => 'string',
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        'DeleteMarkers' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'DeleteMarker',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'DeleteMarkerEntry',
                                'type' => 'object',
                                'sentAs' => 'DeleteMarker',
                                'properties' => array(
                                    'Owner' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'DisplayName' => array(
                                                'type' => 'string',
                                            ),
                                            'ID' => array(
                                                'type' => 'string',
                                            ),
                                        ),
                                    ),
                                    'Key' => array(
                                        'type' => 'string',
                                    ),
                                    'VersionId' => array(
                                        'type' => 'string',
                                    ),
                                    'IsLatest' => array(
                                        'type' => 'boolean',
                                    ),
                                    'LastModified' => array(
                                        'type' => 'string',
                                    ),
                                ),
                            ),
                        ),
                        'Name' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Prefix' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Delimiter' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'MaxKeys' => array(
                            'type' => 'numeric',
                            'location' => 'xml',
                        ),
                        'CommonPrefixes' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'CommonPrefix',
                                'type' => 'object',
                                'properties' => array(
                                    'Prefix' => array(
                                        'type' => 'string',
                                    ),
                                ),
                            ),
                        ),
                        'EncodingType' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'ListMultipartUploadsOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'Bucket' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'KeyMarker' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'UploadIdMarker' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'NextKeyMarker' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Prefix' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'Delimiter' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'NextUploadIdMarker' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'MaxUploads' => array(
                            'type' => 'numeric',
                            'location' => 'xml',
                        ),
                        'IsTruncated' => array(
                            'type' => 'boolean',
                            'location' => 'xml',
                        ),
                        'Uploads' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'sentAs' => 'Upload',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'MultipartUpload',
                                'type' => 'object',
                                'sentAs' => 'Upload',
                                'properties' => array(
                                    'UploadId' => array(
                                        'type' => 'string',
                                    ),
                                    'Key' => array(
                                        'type' => 'string',
                                    ),
                                    'Initiated' => array(
                                        'type' => 'string',
                                    ),
                                    'StorageClass' => array(
                                        'type' => 'string',
                                    ),
                                    'Owner' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'DisplayName' => array(
                                                'type' => 'string',
                                            ),
                                            'ID' => array(
                                                'type' => 'string',
                                            ),
                                        ),
                                    ),
                                    'Initiator' => array(
                                        'type' => 'object',
                                        'properties' => array(
                                            'ID' => array(
                                                'type' => 'string',
                                            ),
                                            'DisplayName' => array(
                                                'type' => 'string',
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        'CommonPrefixes' => array(
                            'type' => 'array',
                            'location' => 'xml',
                            'data' => array(
                                'xmlFlattened' => true,
                            ),
                            'items' => array(
                                'name' => 'CommonPrefix',
                                'type' => 'object',
                                'properties' => array(
                                    'Prefix' => array(
                                        'type' => 'string',
                                    ),
                                ),
                            ),
                        ),
                        'EncodingType' => array(
                            'type' => 'string',
                            'location' => 'xml',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),
                'HeadObjectOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'DeleteMarker' => array(
                            'type' => 'boolean',
                            'location' => 'header',
                            'sentAs' => 'x-cos-delete-marker',
                        ),
                        'AcceptRanges' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'accept-ranges',
                        ),
                        'Expiration' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-expiration',
                        ),
                        'Restore' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-restore',
                        ),
                        'LastModified' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Last-Modified',
                        ),
                        'ContentLength' => array(
                            'type' => 'numeric',
                            'location' => 'header',
                            'sentAs' => 'Content-Length',
                        ),
                        'ETag' => array(
                            'type' => 'string',
                            'location' => 'header',
                        ),
                        'MissingMeta' => array(
                            'type' => 'numeric',
                            'location' => 'header',
                            'sentAs' => 'x-cos-missing-meta',
                        ),
                        'VersionId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-version-id',
                        ),
                        'CacheControl' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Cache-Control',
                        ),
                        'ContentDisposition' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Disposition',
                        ),
                        'ContentEncoding' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Encoding',
                        ),
                        'ContentLanguage' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Language',
                        ),
                        'ContentType' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'Content-Type',
                        ),
                        'Expires' => array(
                            'type' => 'string',
                            'location' => 'header',
                        ),
                        'WebsiteRedirectLocation' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-website-redirect-location',
                        ),
                        'ServerSideEncryption' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption',
                        ),
                        'Metadata' => array(
                            'type' => 'object',
                            'location' => 'header',
                            'sentAs' => 'x-cos-meta-',
                            'additionalProperties' => array(
                                'type' => 'string',
                            ),
                        ),
                        'SSECustomerAlgorithm' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-algorithm',
                        ),
                        'SSECustomerKeyMD5' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-customer-key-MD5',
                        ),
                        'SSEKMSKeyId' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-server-side-encryption-aws-kms-key-id',
                        ),
                        'StorageClass' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-storage-class',
                        ),
                        'RequestCharged' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-charged',
                        ),
                        'ReplicationStatus' => array(
                            'type' => 'string',
                            'location' => 'header',
                            'sentAs' => 'x-cos-replication-status',
                        ),
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ))),
                'HeadBucketOutput' => array(
                    'type' => 'object',
                    'additionalProperties' => true,
                    'properties' => array(
                        'RequestId' => array(
                            'location' => 'header',
                            'sentAs' => 'x-cos-request-id',
                        ),
                    ),
                ),));
    }
}