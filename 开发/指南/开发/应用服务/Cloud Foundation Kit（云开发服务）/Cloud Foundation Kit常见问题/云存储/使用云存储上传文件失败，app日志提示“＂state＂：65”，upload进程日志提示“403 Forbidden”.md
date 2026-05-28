# 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-2

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

 - app日志提示“"state":65”

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/t-p7cwgJTGaYeMtu5OVWxg/zh-cn_image_0000002581275058.png?HW-CC-KV=V1&HW-CC-Date=20260528T014421Z&HW-CC-Expire=86400&HW-CC-Sign=D418C57061FB584D28AEF2AA43BB21FB15CCCF57D25648983DC4E915ADD326BA)

 - upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/tz1dHfnTQX28gMRJ2Oj6aQ/zh-cn_image_0000002611754913.png?HW-CC-KV=V1&HW-CC-Date=20260528T014421Z&HW-CC-Expire=86400&HW-CC-Sign=E6BE439A71FEAF26EE6A220B16467349A3A5F324474CF997D4F47FEAED718627)



**解决措施**

出现此问题，可按照如下步骤排查和解决：
1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section20943184413328)和[手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)两种方式。
2. 请确认已通过[AuthProvider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-cloudcommon#authprovider)获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。
