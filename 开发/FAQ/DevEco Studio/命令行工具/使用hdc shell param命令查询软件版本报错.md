# 使用hdc shell param命令查询软件版本报错

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-31

## 使用hdc shell param命令查询软件版本报错
 


##### 问题现象

执行hdc shell param get const.product.software.version.name命令报错：Get parameter "xxx" fail! errNum is:106!
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/khGWtI3PSyipLQEYR2mnoA/zh-cn_image_0000002658808993.png?HW-CC-KV=V1&HW-CC-Date=20260701T025925Z&HW-CC-Expire=86400&HW-CC-Sign=44B9E2BA6856EB1279D15827BD74CADA3793FB273872E0E1C9D9FC1B3E717BCD)

 
 

##### 解决方案

原因：该命令是查询设备的软件版本，报错的原因是设备不支持该命令，不同的手机支持的查询命令不同。
 
解决方案：
 
- 执行hdc list targets保证设备连接正确。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/_olrIVnZSkS0cH3VvRZFNA/zh-cn_image_0000002628409728.png?HW-CC-KV=V1&HW-CC-Date=20260701T025925Z&HW-CC-Expire=86400&HW-CC-Sign=9600892F33763CBE2DCABCDDCB4B5931A0E5DD8597AB1F183BA93830704F2B29)

- 进入hdc shell模式，执行param get | grep "const.product.software"命令，查找该设备所支持的命令参数，然后基于返回的结果进行软件版本的查看。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/imvD8VAxQi-9Pv26DFj1ew/zh-cn_image_0000002628569630.png?HW-CC-KV=V1&HW-CC-Date=20260701T025925Z&HW-CC-Expire=86400&HW-CC-Sign=D8F89734B461B8DC3C223DC7E4593A7D7D73E346128013178282144A5A018C5D)


 
 

##### 总结

hdc shell命令在不同的设备支持情况可能会有差异，使用hdc shell param get命令可以获取该设备的支持情况，比如使用const.product字段可以查询API版本、软件版本、硬件版本等信息。
