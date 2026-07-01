# 使用hdc shell param命令查询软件版本报错

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-31

#### 问题现象

执行hdc shell param get const.product.software.version.name命令报错：Get parameter "xxx" fail! errNum is:106!
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/khGWtI3PSyipLQEYR2mnoA/zh-cn_image_0000002658808993.png?HW-CC-KV=V1&HW-CC-Date=20260701T041007Z&HW-CC-Expire=86400&HW-CC-Sign=8EC2501923DC549969C804F2EEEAAE2CD1722DF44653AC93B4CD19AE05DF2785)

 
 

#### 解决方案

原因：该命令是查询设备的软件版本，报错的原因是设备不支持该命令，不同的手机支持的查询命令不同。
 
解决方案：
 1. 执行hdc list targets保证设备连接正确。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/_olrIVnZSkS0cH3VvRZFNA/zh-cn_image_0000002628409728.png?HW-CC-KV=V1&HW-CC-Date=20260701T041007Z&HW-CC-Expire=86400&HW-CC-Sign=87C1265A6B150AC9D35C4A45472E325F27FCA5647277F989151241A47888D215)

2. 进入hdc shell模式，执行param get | grep "const.product.software"命令，查找该设备所支持的命令参数，然后基于返回的结果进行软件版本的查看。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/imvD8VAxQi-9Pv26DFj1ew/zh-cn_image_0000002628569630.png?HW-CC-KV=V1&HW-CC-Date=20260701T041007Z&HW-CC-Expire=86400&HW-CC-Sign=7D91EC1A0F2210719150093A6111F534E4045F91059A737F3E0CAF5A74A45D6E)

 
 

#### 总结

hdc shell命令在不同的设备支持情况可能会有差异，使用hdc shell param get命令可以获取该设备的支持情况，比如使用const.product字段可以查询API版本、软件版本、硬件版本等信息。
