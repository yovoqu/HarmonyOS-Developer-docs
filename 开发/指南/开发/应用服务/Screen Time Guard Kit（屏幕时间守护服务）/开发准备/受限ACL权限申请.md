# 受限ACL权限申请

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application

调用Screen Time Guard Kit相关能力之前，需要检查是否已经获取"ohos.permission.MANAGE_SCREEN_TIME_GUARD"权限。该权限允许应用调用屏幕时间守护相关接口，进行屏幕使用限制、应用访问控制、管控使用时间等操作。如未获取授权，则需申请相应的权限。
 1. 在 [申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)和[发布Profile文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)之前，需要[申请相应的ACL权限](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apply-acl-0000002394212138)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/mFLo0pRxQxKgi5O56BRkPw/zh-cn_image_0000002626229792.png?HW-CC-KV=V1&HW-CC-Date=20260624T020939Z&HW-CC-Expire=86400&HW-CC-Sign=A98D2A30DF55F5F2E9F69131E169CF1A6B4275D2A85BE68AEB7C9643E38C17F0)

3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE_SCREEN_TIME_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写申请原因并提交，提交后将在1个工作日回复。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/avvs8qdCRROknjPnp-Ud0w/zh-cn_image_0000002626069882.png?HW-CC-KV=V1&HW-CC-Date=20260624T020939Z&HW-CC-Expire=86400&HW-CC-Sign=3AE43B8296672818560E53083053D893CF735BAA2A5D49383AE8A41733BAE2BD)

5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“选择”。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/0pFc5Z6dTpqXffl4aa0pfg/zh-cn_image_0000002656469159.png?HW-CC-KV=V1&HW-CC-Date=20260624T020939Z&HW-CC-Expire=86400&HW-CC-Sign=C8D4F44B4FB0468468C6B753744C21BC7780F878D1D6A23F7A147E61983C60E3)

6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/TBhSmtkGQLCE7_cIsVSj5A/zh-cn_image_0000002656349207.png?HW-CC-KV=V1&HW-CC-Date=20260624T020939Z&HW-CC-Expire=86400&HW-CC-Sign=B7C63B71E9FAC902A3130FEF3C501226CBDF233BE206C54C2504D31A912D65B8)

7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE_SCREEN_TIME_GUARD"权限，如下所示：

  
```json
"requestPermissions": [{
  "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
}]
```
