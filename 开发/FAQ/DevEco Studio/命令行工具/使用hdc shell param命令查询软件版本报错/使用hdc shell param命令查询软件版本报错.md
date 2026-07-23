# 使用hdc shell param命令查询软件版本报错

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-31

#### 问题现象

执行hdc shell param get const.product.software.version.name命令报错：Get parameter "xxx" fail! errNum is:106!
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/khGWtI3PSyipLQEYR2mnoA/zh-cn_image_0000002658808993.png?HW-CC-KV=V1&HW-CC-Date=20260723T014014Z&HW-CC-Expire=86400&HW-CC-Sign=7F07EE5412587EBDA2CE5319D644738857AE5C4487AF0ED2D8C7A60B450729D1)

 
 

#### 解决方案

原因：该命令是查询设备的软件版本，报错的原因是设备不支持该命令，不同的手机支持的查询命令不同。
 
解决方案：
 1. 执行hdc list targets保证设备连接正确。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/_olrIVnZSkS0cH3VvRZFNA/zh-cn_image_0000002628409728.png?HW-CC-KV=V1&HW-CC-Date=20260723T014014Z&HW-CC-Expire=86400&HW-CC-Sign=97FE5993C702B035B4AB63F665C2169C404B0BFDA949C6CA1A2C14E28D13079B)

2. 进入hdc shell模式，执行param get | grep "const.product.software"命令，查找该设备所支持的命令参数，然后基于返回的结果进行软件版本的查看。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/imvD8VAxQi-9Pv26DFj1ew/zh-cn_image_0000002628569630.png?HW-CC-KV=V1&HW-CC-Date=20260723T014014Z&HW-CC-Expire=86400&HW-CC-Sign=EF22FB2E7FD14BDC6BB8AED477E0864782A166660BB598C9AFDA82C93F2D580A)

 
 

#### 总结

hdc shell命令在不同的设备支持情况可能会有差异，使用hdc shell param get命令可以获取该设备的支持情况，比如使用const.product字段可以查询API版本、软件版本、硬件版本等信息。
