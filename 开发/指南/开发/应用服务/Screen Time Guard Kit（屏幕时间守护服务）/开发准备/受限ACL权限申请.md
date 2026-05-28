# 受限ACL权限申请

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application

1. 在 [申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)和[发布Profile文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)之前，需要[申请相应的ACL权限](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apply-acl-0000002394212138)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/C_rPlBKJQqm4jQYnTo3H8Q/zh-cn_image_0000002581435258.png?HW-CC-KV=V1&HW-CC-Date=20260528T030057Z&HW-CC-Expire=86400&HW-CC-Sign=645C9EAF5B6A7CCA7DB88B013969CF5BEFC6F4C49FA374877002D312DDB0CFDF)

3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE_SCREEN_TIME_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写申请原因并提交，提交后将在1个工作日回复。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/kYxaIDztSMyNReJSGgnrcQ/zh-cn_image_0000002611835089.png?HW-CC-KV=V1&HW-CC-Date=20260528T030057Z&HW-CC-Expire=86400&HW-CC-Sign=9973DF7D9ACFFB03B1CA28828863FAE096DE103BA3A2C3FFAAECF7DE6955BCF0)

5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“选择”。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/ZMiP_CLuT_-fpj0BCSX0gg/zh-cn_image_0000002581275342.png?HW-CC-KV=V1&HW-CC-Date=20260528T030057Z&HW-CC-Expire=86400&HW-CC-Sign=351F07F8AD1AA2FB8BE1EC9DA40AD9740D94F9938B882D9FC829D233916C43C4)

6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/hsXTCUfcSO-iASOTQ8FPYw/zh-cn_image_0000002611755197.png?HW-CC-KV=V1&HW-CC-Date=20260528T030057Z&HW-CC-Expire=86400&HW-CC-Sign=4F91302F5A21E66D6AD4898ABAC86CFF41DC1FDAF4FA7D37144B08E08CE4313B)

7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE_SCREEN_TIME_GUARD"权限，如下所示：

  
```text
"requestPermissions": [{
   "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
}]
```
