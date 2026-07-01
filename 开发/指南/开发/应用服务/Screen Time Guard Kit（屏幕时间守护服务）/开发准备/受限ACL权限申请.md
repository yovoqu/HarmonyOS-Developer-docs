# 受限ACL权限申请

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application

调用Screen Time Guard Kit相关能力之前，需要检查是否已经获取"ohos.permission.MANAGE_SCREEN_TIME_GUARD"权限。该权限允许应用调用屏幕时间守护相关接口，进行屏幕使用限制、应用访问控制、管控使用时间等操作。该权限为受限ACL权限，需要特别配置和申请，具体操作步骤如下所示。
 1. 在 [申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)和[发布Profile文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)之前，需要[申请相应的ACL权限](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apply-acl-0000002394212138)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/H_sLDgqtSfOcTtbsjLvMkA/zh-cn_image_0000002659221151.png?HW-CC-KV=V1&HW-CC-Date=20260701T015300Z&HW-CC-Expire=86400&HW-CC-Sign=6C587DD07609BA7D50AED8F01A94F26805C2DC09BFA5B6090D8C8487FC5FFC65)

3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE_SCREEN_TIME_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写申请原因并提交，提交后将在1个工作日回复。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/EHfKkPeiRZelyiZklyrM1A/zh-cn_image_0000002628701962.png?HW-CC-KV=V1&HW-CC-Date=20260701T015300Z&HW-CC-Expire=86400&HW-CC-Sign=2622CD47A6D7651FAA6F01773377A0FC1115E0F48CF441E932C08DDA13422B8A)

5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“选择”。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/E2RUZSjORrSQkSBYxEiTUw/zh-cn_image_0000002659101191.png?HW-CC-KV=V1&HW-CC-Date=20260701T015300Z&HW-CC-Expire=86400&HW-CC-Sign=F0309F9B239A2B374CED94323ABEC42C42E190D644F546CB595733C93E47E390)

6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/GiiitP-mSHaPOUDECywptQ/zh-cn_image_0000002628861840.png?HW-CC-KV=V1&HW-CC-Date=20260701T015300Z&HW-CC-Expire=86400&HW-CC-Sign=CC013254BC6781472D2C0397D2588FFB8F8F4934C1310770281978BA08B5DE53)

7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE_SCREEN_TIME_GUARD"权限，如下所示：

  
```json
"requestPermissions": [{
  "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
}]
```
