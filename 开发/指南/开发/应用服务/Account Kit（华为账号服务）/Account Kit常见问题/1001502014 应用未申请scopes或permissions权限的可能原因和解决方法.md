# 1001502014 应用未申请scopes或permissions权限的可能原因和解决方法

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-2

**问题现象**
 
调用接口报错1001502014 应用未申请scopes或permissions权限。
 
**可能原因**
 1. 没有申请对应的账号权限。
2. 权限申请成功后，最迟会在25小时后生效。
3. 使用[获取风险等级](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel-introduction)能力，但未申请获取风险等级权限。
 
**解决措施**
 1. 申请对应权限，请见[申请账号权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-config-permissions)章节。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/ZnApPS30RlC1pL89DHB1Ig/zh-cn_image_0000002611754773.png?HW-CC-KV=V1&HW-CC-Date=20260528T030139Z&HW-CC-Expire=86400&HW-CC-Sign=59EE8AFB72ED467205608655D046BE55817B67EE5D54F9C1FD20E39A206F9058)

2. 权限申请通过后，您可通过修改应用工程 > app.json5中的versionCode触发权限生效。

  **图1** 修改前

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/cBJDilzST4mHSKt5IHLDhg/zh-cn_image_0000002611834667.png?HW-CC-KV=V1&HW-CC-Date=20260528T030139Z&HW-CC-Expire=86400&HW-CC-Sign=48AE7F8F11151EBCD9BAE1EFD4C7F1EB6095CD15637B519B5452AAB85FDB62C5)


  **图2** 修改后

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/oEtl39W6SzOILdDzOHmPJQ/zh-cn_image_0000002581274920.png?HW-CC-KV=V1&HW-CC-Date=20260528T030139Z&HW-CC-Expire=86400&HW-CC-Sign=F0A5E1BAC6B6E775BAD14905625761A0235A36295100193D03773A0FDA6C173F)

3. 确认是否需要使用获取风险等级能力，如需使用，请参考[获取风险等级](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel-introduction)申请对应权限。
