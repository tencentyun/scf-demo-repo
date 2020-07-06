## serverless+腾讯云短信实现短信验证码登录
### 发送短信验证码
请求参数：
| 字段 |类型|说明|
| ----- | ----- | ----- |
| method|string|请求方法，值为getSms|
|phone|string|手机号，值为区号+手机号，比如86185662466**|

### 校验验证码（登录）
请求参数：
| 字段 |类型|说明|
| ----- | ----- | ----- |
| method|string|请求方法，值为login|
|phone|string|手机号，值为区号+手机号，比如86185662466**|
| code|string|值为6位数字验证码|

### 错误码
| 字段 |说明|
| ----- | ----- |
| InValidParam|缺少参数|
| MissingCode|缺少验证码参数|
| CodeHasExpired|验证码已过期|
| CodeHasValid|验证码已失效|
| CodeIsError|请检查手机号和验证码是否正确|



