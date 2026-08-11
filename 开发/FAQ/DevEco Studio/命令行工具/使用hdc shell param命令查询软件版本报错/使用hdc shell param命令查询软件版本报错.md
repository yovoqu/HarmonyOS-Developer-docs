# 使用hdc shell param命令查询软件版本报错

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-31

#### 问题现象

执行hdc shell param get const.product.software.version.name命令报错：Get parameter "xxx" fail! errNum is:106!
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/khGWtI3PSyipLQEYR2mnoA/zh-cn_image_0000002658808993.png?HW-CC-KV=V1&HW-CC-Date=20260811T005514Z&HW-CC-Expire=86400&HW-CC-Sign=4988111AAA92AB290D80FB1CC0EB2687649DD7EE6708EF16B7C268D5B964711E)

 
 

#### 解决方案

原因：该命令是查询设备的软件版本，报错的原因是设备不支持该命令，不同的手机支持的查询命令不同。
 
解决方案：
 1. 执行hdc list targets保证设备连接正确。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/_olrIVnZSkS0cH3VvRZFNA/zh-cn_image_0000002628409728.png?HW-CC-KV=V1&HW-CC-Date=20260811T005514Z&HW-CC-Expire=86400&HW-CC-Sign=96AE7B0A6008BBEE579BE7855BD8BE7785E0C0864F46F10B1FF3E3A80BD4E465)

2. 进入hdc shell模式，执行param get | grep "const.product.software"命令，查找该设备所支持的命令参数，然后基于返回的结果进行软件版本的查看。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/imvD8VAxQi-9Pv26DFj1ew/zh-cn_image_0000002628569630.png?HW-CC-KV=V1&HW-CC-Date=20260811T005514Z&HW-CC-Expire=86400&HW-CC-Sign=34E19587021C17A738F9BD535A349418A75876F877B8718FA27D117CEDF6DFB9)

 
 

#### 总结

hdc shell命令在不同的设备支持情况可能会有差异，使用hdc shell param get命令可以获取该设备的支持情况，比如使用const.product字段可以查询API版本、软件版本、硬件版本等信息。
