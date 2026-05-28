# 受限ACL权限申请

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application

1. 在 [申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)和[发布Profile文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)之前，需要[申请相应的ACL权限](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apply-acl-0000002394212138)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/C_rPlBKJQqm4jQYnTo3H8Q/zh-cn_image_0000002581435258.png?HW-CC-KV=V1&HW-CC-Date=20260528T014428Z&HW-CC-Expire=86400&HW-CC-Sign=24FDAD64CB05F4FA5CEE34BA8025B1A94DD7A40B87A100CC4C9FD975F19C2E57)

3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE_SCREEN_TIME_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写申请原因并提交，提交后将在1个工作日回复。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/kYxaIDztSMyNReJSGgnrcQ/zh-cn_image_0000002611835089.png?HW-CC-KV=V1&HW-CC-Date=20260528T014428Z&HW-CC-Expire=86400&HW-CC-Sign=3CBF56A3001A2D37DEE71E86EB23BD0430A76EB3F6845B7A7A996EC79856CD31)

5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“选择”。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/ZMiP_CLuT_-fpj0BCSX0gg/zh-cn_image_0000002581275342.png?HW-CC-KV=V1&HW-CC-Date=20260528T014428Z&HW-CC-Expire=86400&HW-CC-Sign=EF4FDA0C500840850FD65A5F5F2DFE841560652C1DB9DFF4ACE1589095584D96)

6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/hsXTCUfcSO-iASOTQ8FPYw/zh-cn_image_0000002611755197.png?HW-CC-KV=V1&HW-CC-Date=20260528T014428Z&HW-CC-Expire=86400&HW-CC-Sign=5804A80FD4FAD4ED09598BAF6A13375B7AE6E7A855AAACD4F03B4BD1C4652398)

7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE_SCREEN_TIME_GUARD"权限，如下所示：

  
```text
"requestPermissions": [{
   "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
}]
```
