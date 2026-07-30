# 受限ACL权限申请

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application

调用Screen Time Guard Kit相关能力之前，需要检查是否已经获取"ohos.permission.MANAGE_SCREEN_TIME_GUARD"权限。该权限允许应用调用屏幕时间守护相关接口，进行屏幕使用限制、应用访问控制、管控使用时间等操作。该权限为受限ACL权限，需要特别配置和申请，具体操作步骤如下所示。
 1. 在 [申请调试Profile](https://developer.huawei.com/consumer/cn/doc/app/agc-help-debug-profile-0000002248181278)和[发布Profile文件](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-profile-0000002248341090)之前，需要[申请相应的ACL权限](https://developer.huawei.com/consumer/cn/doc/app/agc-help-apply-acl-0000002394212138)。
2. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/-GSCpS_vSLSGVCfH4WKxbw/zh-cn_image_0000002686087351.png?HW-CC-KV=V1&HW-CC-Date=20260730T072013Z&HW-CC-Expire=86400&HW-CC-Sign=A987D3DAEDE2581A71984D05B5A2FCD39DCE305350D486D04E2F9C55B22EF186)

3. 在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE_SCREEN_TIME_GUARD"，查找并勾选权限，提交申请。
4. 根据实际业务需求填写使用场景并提交，审批时间为3个工作日。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/o6NF_2RjSoaLxSPmaK0aTg/zh-cn_image_0000002685927523.png?HW-CC-KV=V1&HW-CC-Date=20260730T072013Z&HW-CC-Expire=86400&HW-CC-Sign=C028866E6BF5214BF3358A3D10217404B72749F360B83887FA7B5F7E6DF1031A)

5. 权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“查看”。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Hh_fz7y7RwWtDF1_Nhm7Cg/zh-cn_image_0000002656007844.png?HW-CC-KV=V1&HW-CC-Date=20260730T072013Z&HW-CC-Expire=86400&HW-CC-Sign=DBB3062640413E22F8EAAD8F83CB79C01BA170A00625A346E3F8204DD1D7BCDF)

6. 在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/eD-i4ltNSR6hiLw8qjjfxg/zh-cn_image_0000002655847924.png?HW-CC-KV=V1&HW-CC-Date=20260730T072013Z&HW-CC-Expire=86400&HW-CC-Sign=4C6DE4E5A31A229502A0E60ACD2422F3DDEBB5239B4884BBD764EA4D32E98CBC)

7. 选择权限后点击“添加”生成新的Profile文件，下载后按[手动配置签名信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)替换profile文件。
8. 在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE_SCREEN_TIME_GUARD"权限，如下所示：

  
```json
"requestPermissions": [{
  "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
}]
```
