# Mac安装DevEco-Studio后启动报错“NSInternalInconsistencyException”如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-20

## Mac安装DevEco-Studio后启动报错“NSInternalInconsistencyException”如何解决
 


##### 问题现象

Mac环境下，安装DevEco Studio后启动报错：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/2HAhbImGTiGzB5M3lns8GA/zh-cn_image_0000002658924269.png?HW-CC-KV=V1&HW-CC-Date=20260701T025909Z&HW-CC-Expire=86400&HW-CC-Sign=B9DC01BBCD773D38DEE6EA495C5D975942104E5FD7A6DCDBC820BE419DA77730)

 
报错信息如下图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/fk4DniyJS3q2BBh2KoY_ug/zh-cn_image_0000002658804323.png?HW-CC-KV=V1&HW-CC-Date=20260701T025909Z&HW-CC-Expire=86400&HW-CC-Sign=FB257EB2865C6C04B0D49044AD170F12257A7C63A76A636ED7C86EFF79AAF759)

 
 

##### 背景知识

Mac环境下安装DevEco Studio[操作指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-software-install#section102166218352)。
 
 

##### 解决方案

对于启动报错可以按照如下步骤处理：
 
- 找到DevEco Studio安装目录，用命令行sh bin/inspect.sh启动DevEco Studio，分析终端打印的错误日志。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/GJ4Tm2PmTMuRuW0NkjxZXA/zh-cn_image_0000002628564966.png?HW-CC-KV=V1&HW-CC-Date=20260701T025909Z&HW-CC-Expire=86400&HW-CC-Sign=711164C71F4C4F792FD1F41B61525FAD3B4CCC5EB3E01E2153222865C85376FC)

- 根据报错内容DEVECOSTUDIO_VM_OPTIONS = /Users/{USER_NAME}/Downloads/jihuo.live/jihuo-tool/vmoptions/devecostudio.vmoptions，可以判断启动脚本被修改了。
- 删除启动脚本，启动脚本默认路径为“/Users/{USER_NAME}/Library/LaunchAgents/jetbrains.vmoptions.plist”，删除后重启Mac即可。

 
 

##### 总结

- 由于DevEco Studio和Jetbrains用的是相同的启动脚本，且脚本会一直沿用，如果脚本被修改，会导致不可知的问题。
- 如果运行过Jetbrains的破解软件，修改了Jetbrains启动脚本中的环境变量，会导致Java虚拟机无法启动，DevEco Studio无法打开。
