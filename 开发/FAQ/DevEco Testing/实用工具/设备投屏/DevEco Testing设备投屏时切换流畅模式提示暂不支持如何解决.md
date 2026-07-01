# DevEco Testing设备投屏时切换流畅模式提示暂不支持如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-cast-3

## DevEco Testing设备投屏时切换流畅模式提示暂不支持如何解决
 


##### 问题现象

使用DevEco Testing的流畅模式进行设备投屏时提示“当前版本不支持流畅模式，请切换标准模式”。
 
 

##### 背景知识

DevEco Testing的[实用工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/tool)支持将设备界面实时投放到PC上，并支持在PC上对设备进行操作，如按键操作、查看设备/应用信息，文件管理、自定义指令等常用操作。
 
 

##### 问题定位

- 连接设备，执行“hdc shell param set persist.ace.testmode.enabled 1”命令是否success。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/ksWboBweRD2ocg7sVT6JGw/zh-cn_image_0000002658803453.png?HW-CC-KV=V1&HW-CC-Date=20260701T025928Z&HW-CC-Expire=86400&HW-CC-Sign=22ADF3403185BADF7565F9F91E9512D8B6D56FEFB6426F62C7AECD14F33FC611)

- 执行“hdc shell pidof uitest”命令，查看是否存在被占用的线程。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/kR4SHKMmTF2NzLvJXQVlWg/zh-cn_image_0000002628404190.png?HW-CC-KV=V1&HW-CC-Date=20260701T025928Z&HW-CC-Expire=86400&HW-CC-Sign=B3AB91CA1E35B366DE1716D51F43488588D82774B08472E3C422CCBEFEF9E3B1)

- 执行“hdc shell uitest start-daemon singleness”命令，检查是否有信息打印。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/ZSgjLzTVS--QS_KODHKQvQ/zh-cn_image_0000002628564092.png?HW-CC-KV=V1&HW-CC-Date=20260701T025928Z&HW-CC-Expire=86400&HW-CC-Sign=9D46C8176686C400F4BEC4E9ADEB5E7A413A3004E92A4BA86534F82C5602EC71)


 
 

##### 分析结论

投屏通道被占用，需要清理被占用的通道。
 
 

##### 修改建议

- 执行“hdc shell kill -9 41894”清理被占用的通道，其中41984是被占用的线程号。
- 重启DevEco Testing客户端，选择流畅模式重新进行投屏。
