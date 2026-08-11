# 如何获取应用打印的hilog日志到本地查看

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-87

#### 问题现象

hilog日志如何导出到本地？
 
 

#### 解决方案

hilog日志导出到本地有2种方案：
 1. hdc shell hilog > 导出的文件地址。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/nspNT5myRb2ECJ5NydBkTQ/zh-cn_image_0000002628554934.png?HW-CC-KV=V1&HW-CC-Date=20260811T005909Z&HW-CC-Expire=86400&HW-CC-Sign=21AAC10CDA3DF948773DB7F7B2E461071F638184A023718775741F8C51755A57)

2. 通过hdc file recv /data/log/hilog获取。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/0zkPWsENSnW4lnMLtR2ykg/zh-cn_image_0000002628395034.png?HW-CC-KV=V1&HW-CC-Date=20260811T005909Z&HW-CC-Expire=86400&HW-CC-Sign=76A66CE14EE179C6A43DE39F1E58734B8AF082E9861D7DEC9CC4C350E625562A)
