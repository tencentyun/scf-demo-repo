# scf-demo-repo

SCF 无服务器云函数 Demo 代码库

# Demo说明

## 文件组织结构

```sh
|-- Go1-helloworld     文件夹名称，也作为demo名称，最好和serverless-cloud-function-application::application::name一致。
|   |-- config.json    配置文件可以为config.json或者config.yaml 必选
|   |-- main           对应的入口文件 必选
|   |-- readme.md      readme 非必选
|   `-- license.txt    license文件 非必选
```

注：对于java语言来说入口文件是jar包，对于golang语言来说入口文件必须是可执行文件。

## 配置文件说明

```sh
{
    "serverless-cloud-function-application": {
        "application": {
            "name": "Go1-helloworld",                                   应用名称,如果是java demo的话，必须和jar文件的名称一致，其他语言不做限制。前台需要展示，请认真填写，名称要具有一定的意义
            "description": "this is a golang demo balabala",            应用描述，主要是介绍该应用的用途、涉及到的关键技术等，用户可以通过该关键字搜索  前台需要展示，请认真填写
            "readme": {
                "file": "readme.md",                                    readme文件
                "content": "this is a golang demo balabala"             readme内容
            },
            "license": {
                "file": "license.txt",                                  license文件名
                "content": "this is this application license info"      license信息
            },
            "author": {
                "name": "tencent cloud serverless team"                 作者
            },
            "tags": [
                "Go1"                                                   标签，如CMQ、timer、kafka、http等，用户可以通过该关键字搜索  前台需要展示，请认真填写
            ],
            "version": "1.0.0"                                          版本号
        },
        "functions": {
            "name": "test-function",                                    函数名称
            "description": "first test function",                       函数描述
            "handler": "main",                                          hander 如果是一段式的话，必须和对应的二进制文件名称一致，第一段不能使用readme、license、config；如果二段式的，第一段必须是对应的入口文件名，第一段不能使用readme、license、config；三段式的话，必须是对应的handler
                                                                        一段式：golang，预制内容："main"
                                                                        二段式：python，nodejs，PHP，预制内容："index.main_handler"
                                                                        三段式：java，预制内容："example.Hello::mainHandler"
            "memorySize": 128,                                          运行所需内存
            "timeout": 3,                                               运行所需时间
            "runtime": "Go1",                                           运行环境，用户可以通过该关键字搜索["Python2.7", "Python3.6", "Nodejs6.10", "Java8", "LuaCDN", "NodejsCDN", "Php5", "Php7", "Nodejs8.9", "Go1"] 前台需要展示，请认真填写
            "codeObject": {
                "codeFile": [                                           代码文件
                    "main"
                ]
            }
        }
    }
}
```

## 上传到Demo库

请参照：https://blog.csdn.net/qq_33429968/article/details/62219783
