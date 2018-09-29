# scf-demo-repo

SCF 无服务器云函数 Demo 代码库

# Demo说明

## 文件组织结构

golang

```
|-- Go1-helloworld     文件夹名称，也作为demo名称，最好和serverless-cloud-function-application::application::name一致。
|   |-- config.json    配置文件可以为config.json或者config.yaml 必选
|   |-- main           对应的入口文件 必选
|   |-- readme.md      readme 非必选
|   `-- license.txt    license文件 非必选
```

python


```
|-- apigw-py2          文件夹名称，也作为demo名称，最好和serverless-cloud-function-application::application::name一致。
|   |-- config.json    配置文件可以为config.json或者config.yaml 必选
|   |-- index.py       对应的入口文件 必选
|   |-- readme.md      readme 非必选
|   `-- license.txt    license文件 非必选
```


注：对于java语言来说入口文件是jar包，对于golang语言来说入口文件必须是可执行文件。

## 配置文件说明

```sh
{
    "serverless-cloud-function-application": {
        "application": {
            "name": "apigw-response-proxy-py2.7",        #应用名称,如果是java demo的话，必须和jar文件的名称一致，其他语言不做限制。前台需要展示，请认真填写，名称要具有一定的意义，不支持中文。
            "description": "此示例使用 API 网关作为触发器，实现 http 接口，并返回 html 格式页面。",            #应用描述，主要是介绍该应用的用途、用法、涉及到的关键技术等，用户可以通过该关键字搜索。前台需要展示，请认真填写，支持中文。
            "readme": {                     # readme 说明，非必选，file 或 content 二选一即可
                "file": "readme.md",                                    #readme文件内容
                "content": "此示例使用 API 网关作为触发器，实现 http 接口"             #readme内容
            },
            "license": {                    # license 说明，非必选，file 或 content 二选一即可
                "file": "license.txt",                                  #license文件内容
                "content": "license info"      #license内容
            },
            "author": {
                "name": "tencent cloud serverless team"      #作者
            },
            "tags": [
                "apigw","python2.7","api"                #标签，可编写多个，可包含包括runtime、触发器、场景等关键字，用户可以通过该关键字搜索。前台需要展示，请认真填写，不支持中文
            ],
            "version": "1.0.0"                           #版本号，通过版本号标识 demo 升级情况，未修改版本号会导致 demo 不更新至页面
        },
        "functions": {
            "name": "test-function",                                    #函数名称
            "description": "first test function",                       #函数描述，支持中文
            "handler": "index.main_hanlder",                            #函数入口 不支持中文，如果是一段式的话，必须和对应的二进制文件名称一致，第一段不能使用readme、license、config；如果二段式的，第一段必须是对应的入口文件名，第一段不能使用readme、license、config；三段式的话，必须是对应的handler
                                                                       
            "memorySize": 128,                                          #运行配置内存
            "timeout": 3,                                               #运行超时时间
            "runtime": "Python2.7",                                           #运行环境，用户可以通过该关键字搜索["Python2.7", "Python3.6", "Nodejs6.10", "Java8", "LuaCDN", "NodejsCDN", "Php5", "Php7", "Nodejs8.9", "Go1"] 前台需要展示，请认真填写
            "codeObject": {
                "codeFile": [                                           #代码文件
                    "index.py"
                ]
            }
        }
    }
}
```

函数入口 handler 写法：
* 一段式：golang，预制内容："main"
* 二段式：python，nodejs，PHP，预制内容："index.main_handler"
* 三段式：java，预制内容："example.Hello::mainHandler"

# Demo 开发注意事项

1. 需要注意代码提交时不要带有 SecretID，SecretKey 等信息。
2. 关键信息可修改为通过环境变量读取，并定义好所需配置的环境变量。
3. Demo 描述尽量使用中文，简洁扼要的描述 Demo 的实现功能，可适用的场景，使用的方式。


## 上传到Demo库

请参照：https://blog.csdn.net/qq_33429968/article/details/62219783
