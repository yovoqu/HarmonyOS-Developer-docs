# 如何获取应用打印的hilog日志到本地查看

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-87

#### 问题现象

hilog日志如何导出到本地？
 
 

#### 解决方案

hilog日志导出到本地有2种方案：
 1. hdc shell hilog > 导出的文件地址。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/nspNT5myRb2ECJ5NydBkTQ/zh-cn_image_0000002628554934.png?HW-CC-KV=V1&HW-CC-Date=20260701T041409Z&HW-CC-Expire=86400&HW-CC-Sign=014FEC4CCEE3909FF028236B21876C285041108789AA2B4EFB536F4ED430ED68)

2. 通过hdc file recv /data/log/hilog获取。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/0zkPWsENSnW4lnMLtR2ykg/zh-cn_image_0000002628395034.png?HW-CC-KV=V1&HW-CC-Date=20260701T041409Z&HW-CC-Expire=86400&HW-CC-Sign=CA862314E7084EF901CC2A5E8FEBA481F11C97168FE5D351878105FC111B9004)
