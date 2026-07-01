# HarmonyOS指定设备发布描述文件签名sign字段如何生成

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-9

## HarmonyOS指定设备发布描述文件签名sign字段如何生成
 


##### 问题现象

使用[指定设备发布](https://developer.huawei.com/consumer/cn/doc/app/agc-help-internal-test-0000002270709477)发布应用，在使用[构建Deeplink实现下载应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-internal-test-release-app-0000002260691994)生成应用描述文件（例如：manifest.json5，文件名可自定义）时，需要获取描述文件签名（即sign字段），应该如何获取sign的值呢？
 
 

##### 背景知识

- 需要根据提供的[验签工具](https://gitee.com/arkin-internal-testing/internal-testing)来生成sign字段。
- 生成签名所需要manifest-sign-tool-1.0.0.jar也需要通过[验签工具](https://gitee.com/arkin-internal-testing/internal-testing)获取。

 
 

##### 解决方案

- 描述文件不是由项目生成，但可以通过应用的module.json5和app.json5文件生成，具体字段可以参考[构建Deeplink实现下载应用](https://developer.huawei.com/consumer/cn/doc/app/agc-help-internal-test-release-app-0000002260691994)说明，并根据实际情况手动填写对应的参数，保存到本地即可。
- 描述文件生成后保存本地，参照如下命令生成描述文件签名sign：
```text
java -jar manifest-sign-tool-1.0.0.jar -operation sign -mode localjks -inputFile D:\old_manifest.json5 -outputFile D:\new_manifest.json5 -keystore D:\internaltest.p12 -keystorepasswd Abc123456 -keyaliaspasswd Abc123456 -privatekey internaltest
```
 其中：
 
operation为操作类型，生成签名时为sign，验证签名时为verify。
- mode为获取签名的模式，本地为localjks，远端为remote，参考示例选择localjks。
- inputFile为需要生成签名描述文件路径，参考示例为D:\old_manifest.json5。
- outputFile为输出的带sign的描述文件路径，参考示例为D:\new_manifest.json5。
- keystore为p12密钥文件路径，对应[生成密钥和证书请求文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-publish-app#section1079214271414)中的keystore Name(*.p12)，参考示例为D:\internaltest.p12。
- keystorepasswd为密钥文件密码，对应[生成密钥和证书请求文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-publish-app#section1079214271414)的Key store Password，参考示例为Abc123456。
- keyaliaspasswd为私钥的密码，对应[生成密钥和证书请求文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-publish-app#section1079214271414)的Key password，参考示例为Abc123456。
- privatekey为私钥的别名，对应[生成密钥和证书请求文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-publish-app#section1079214271414)的Alias，参考示例为internaltest。

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/qXMDFsCBS42k6uKdsG_R5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025857Z&HW-CC-Expire=86400&HW-CC-Sign=88263EFCB76484D93DB75F77615CB7EFE7D16AF4ACC3F9DE35A0B0DA5BB3CAEB)
 

执行operation指令时，其中old_manifest.json5的sign字段无需填写，生成的new_manifest.json5会自动补充，以下为执行前后示例：
 
```text
old_manifest.json5：
"sign": "描述文件签名"
new_manifest.json5：
"sign": "MEUCIEl****4AVZyWFc="
```
 
低版本的JDK会限制加密强度并产生报错，需要升级JDK到1.8.0.3*或更高版本（不包括java11的版本）。
