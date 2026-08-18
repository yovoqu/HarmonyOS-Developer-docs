# Push Kit推送服务接入常见错误码和解决方案

更新时间：2026-08-12 10:47:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-push-10

#### 问题现象

消息推送时产生10009000xx、80xxxxxx等错误码，如何排查？
 
 

#### 解决方案

在消息推送对接过程中，用于定位的错误码（状态码）主要来自以下三种：
 1. [REST API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-rest-api)云侧接口[业务响应码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-response#业务响应码)。
2. Push Kit端侧[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-error-code)与[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。
3. 消息[回执状态码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-msg-receipt#回执状态码)。
 
进行问题排查时首先排查云侧REST API接口是否正常下发。然后再排查端侧响应是否正常，是否产生ArkTS API错误码。以下按场景列举几个常见错误码及解决方式：
 
**场景一**：REST API业务响应码错误。
 
- [80200001 认证错误](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-response#section80200001-认证错误)，常见于请求头中Authorization参数鉴权失败，建议排查方向：1. 确认用于申请JWT Token的[服务账号密钥](https://developer.huawei.com/consumer/cn/doc/start/api-0000001062522591#section3554194116341)凭证中project_id、[推送请求接口URL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-request-struct)中projectId与应用所属项目ID三者一致。

2. 请确认生成JWT Token的正确性后再推送消息，详情参见[基于服务账号生成鉴权令牌](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-jwt-token)。

3. HarmonyOS 5及以上系统版本使用V3版本的REST API下发消息，鉴权方式只支持JWT Token令牌；不支持Access Token的鉴权方式。
- [80300002 当前应用无权限下发推送消息](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-response#section80300002-当前应用无权限下发推送消息)。请确保当前应用所属的项目已开通了推送服务，并基于该项目重新生成鉴权令牌，并重新尝试推送消息。建议排查方向：1. 是否已开通推送服务。

2. 推送请求URL中的projectId与当前应用所属的项目是否一致。
- [80300007 所有Token都是无效的](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-response#section80300007-所有token都是无效的)，请根据响应消息中的提示，按关键词排查问题。例如，下面日志中的关键词为noPushTypeRight，表示没有发送对应push-type场景的权益，需要申请对应场景的权益。其他问题情况可参考[80300007](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-response#section80300007-所有token都是无效的)相关详细解析。
```text
code=80300007,
msg={"failure":1,"illegalTokens":{"noPushTypeRight":["MAM0Ku.........jixTSG"]}},
requestId=17xxxxxxxxxxxx001,
```

- 更多参考[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-error-code)与[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)说明。

 
 
**场景二**：Push Kit端侧ArkTS API错误码：
 
- [1000900010 APP身份验证失败](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-error-code#section1000900010-app身份验证失败)，常见于[pushService.getToken](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-pushservice#pushservicegettoken)失败的场景：1. 确认当前HarmonyOS应用已经开启推送服务，生成Profile证书打包，且应用签名正确，详情参见[开通推送服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-config-setting#section13206419341)步骤5、步骤6。

2. 如果生成Profile证书后，再开通推送服务。需要重新更新Profile文件，在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)的“项目设置->API管理”中启用“推送服务”开启后重新申请Profile文件。同时应用需要重新签名，

3. 保证设备网络环境通畅。

4. 建议使用真机进行调试，不要使用云真机调试。
- [1000900009 推送服务内部错误](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-error-code#section1000900009-推送服务内部错误)：1. 保证设备网络环境通畅。

2. 建议使用真机进行调试。

3. 重启设备。
- 更多参考[REST API](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-rest-api)云侧接口[业务响应码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-scenariozed-api-response#业务响应码)。
