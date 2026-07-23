# 如何获取应用打印的hilog日志到本地查看

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-87

#### 问题现象

hilog日志如何导出到本地？
 
 

#### 解决方案

hilog日志导出到本地有2种方案：
 1. hdc shell hilog > 导出的文件地址。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/nspNT5myRb2ECJ5NydBkTQ/zh-cn_image_0000002628554934.png?HW-CC-KV=V1&HW-CC-Date=20260723T012409Z&HW-CC-Expire=86400&HW-CC-Sign=3B647F235DC3A30594EE9B9917BB28C6D0F9D0783F242B3E0C9CD0EF51689059)

2. 通过hdc file recv /data/log/hilog获取。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/0zkPWsENSnW4lnMLtR2ykg/zh-cn_image_0000002628395034.png?HW-CC-KV=V1&HW-CC-Date=20260723T012409Z&HW-CC-Expire=86400&HW-CC-Sign=B3D33C87C9018C50B69718F6EBD4B9F960C11B86CA3AE15DAC5A57E75BE9C17E)
