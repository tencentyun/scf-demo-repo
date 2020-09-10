# scf-demo-repo

SCF 雲函數 Demo 代碼庫

# Demo說明

## 文件組織結構

golang

```
|-- Go1-helloworld     文件夾名稱，也作爲demo名稱，最好和serverless-cloud-function-application::application::name一緻。
|   |-- config.json    配置文件可以爲config.json或者config.yaml 必選
|   |-- main           對應的入口文件 必選
|   |-- readme.md      readme 非必選
|   `-- license.txt    license文件 非必選
```

python


```
|-- apigw-py2          文件夾名稱，也作爲demo名稱，最好和serverless-cloud-function-application::application::name一緻。
|   |-- config.json    配置文件可以爲config.json或者config.yaml 必選
|   |-- index.py       對應的入口文件 必選
|   |-- readme.md      readme 非必選
|   `-- license.txt    license文件 非必選
```


注：對于java語言來說入口文件是jar包，對于golang語言來說入口文件必須是可執行文件。

## 配置文件說明

```sh
{
    "serverless-cloud-function-application": {
        "application": {
            "Chinese"{  # "Chinese"對應中文版本
        "name": "API閘道觸發器基礎應用",
    # 應用名稱,Chinese對應中文，如果是java demo的話，必須和jar文件的名稱一緻，其他語言不做限制。前台需要展示，請認真填寫，名稱要具有一定的意義，不支援中文，名稱裏統一剝離掉runtime
        "description": "此範例使用 API 閘道作爲觸發器，實現 http 介面，并返回 html 格式頁面。",
    # 應用描述，主要是介紹該應用的用途、用法、涉及到的關鍵技術等，用戶可以通過該關鍵字搜索。前台需要展示，請認真填寫，支援中文。
        "attention": "該雲函數使用了API閘道觸發器，并使用了內建響應功能，返回值需要構造爲Json格式" ,   #demo使用的注意事項，在範本詳情裏展示
        "readme": {  # readme 說明，非必選，file 或 content 二選一即可
            "file": "readme.md",  # readme文件内容
            "content": "此範例使用 API 閘道作爲觸發器，實現 http 介面"  # readme内容
        },
        "license": {  # license 說明，非必選，file 或 content 二選一即可
            "file": "license.txt",  # license文件内容
            "content": "公開"  # license内容
        },
        "author": {
            "name": "Top Cloud 無服務器雲函數團隊"  # 作者
        },
    },
    "English"{   # "English" is for English version
        "name": "apigw-response-proxy",
    # This is the name of demo.If it is java demo. Please keep the same name with jar package. Non-jave demos have no limit.Please note the demo name doesn't include runtime.
        "description": "This demo is for API GW trigger. You can all function by http interface and you will get html page",
    # The description of demo. You can describe the detail function.
        "attention": "This demo has used api gw and integrated response function. So the return value should be json format based on the requirement",   #the description of precautions
        "readme": {  # "readme" is not necessary.You can only fill in the "file" or "content".
            "file": "readme.md",  # readme file
            "content": "This demo is for API GW trigger."  # content of readme
        },
        "license": {  # "license" is not necessary.You can only fill in the "file" or "content".
            "file": "license.txt",  # license file
            "content": "license info"  # content of license
        },
        "author": {
            "name": "taifucloud cloud serverless team"  # author
        },
    },
    "input_parameters":{
    },    #the description of input parameters.
    "output_parameters":{        #the description of output_parameters.
        {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type":"text/html"},
            "body": "<html><body><h1>Heading</h1><p>Paragraph.</p></body></html>"
        }
    },
    "download_address":"demo的git下載連結",  #demo的git下載連結
    "tags":[
            "apigw", "Python2.7", "api"  # 标簽統一爲英文，可編寫多個，建議使用runtime、觸發器、場景等關鍵字，用戶可以通過該關鍵字搜索。前台需要展示，請認真填寫，不支援中文
    ],
    "version": "1.0.1",  # 版本号，通過版本号标識 demo 升級情況，未修改版本号會導緻 demo 不更新至頁面
},
"functions": {
    "name": "test-function",  # 函數名稱，只支援英文
    "description": "此範例使用 API 閘道作爲觸發器，實現 http 介面，并返回 html 格式頁面。" # 和"application"保持一緻，可爲英文或中文，前台不展示
    "handler":"index.main_hanlder",
# 函數入口 不支援中文，如果是一段式的話，必須和對應的二進制文件名稱一緻，第一段不能使用readme、license、config；如果二段式的，第一段必須是對應的入口文件名，第一段不能使用readme、license、config；三段式的話，必須是對應的handler
    "memorySize": 128,  # 運作配置内存
    "timeout": 3,  # 運作超時時間
    "runtime": "Python2.7",# 運作環境，用戶可以通過該關鍵字搜索["Python2.7", "Python3.6", "Nodejs6.10", "Java8", "LuaCDN", "NodejsCDN", "Php5", "Php7", "Nodejs8.9", "Go1"] 前台需要展示，請認真填寫
    "Environment":{
            "DB_NAME": "mydb" # 可選，函數環境變量
    },
    "Events":{
    },      # 可選，用于定義觸發此函數的事件源
    "VpcConfig":{
    },     # 可選， 用于配置雲函數訪問 VPC 私有網絡。
    "codeObject": {
        "codeFile": [  # 代碼文件
            "index.py"
        ]
        "CodeUri":[     # 代碼下載網址，和download_address保持一緻
            ""
        ]
    }
}
}
}
```

函數入口 handler 寫法：
* 一段式：golang，預制内容："main"
* 二段式：python，nodejs，PHP，預制内容："index.main_handler"
* 三段式：java，預制内容："example.Hello::mainHandler"

# Demo 開發注意事項

1. 需要注意代碼提交時不要帶有 SecretID，SecretKey 等訊息。
2. 關鍵訊息可修改爲通過環境變量讀取，并定義好所需配置的環境變量。
3. Demo 描述盡量使用中文，簡潔扼要的描述 Demo 的實現功能，可适用的場景，使用的方式。
4. 每個Demo的英文名稱必填且唯一,不同開發語言可以一樣。


## 上傳到Demo庫

請參照：https://blog.csdn.net/qq_33429968/article/details/62219783