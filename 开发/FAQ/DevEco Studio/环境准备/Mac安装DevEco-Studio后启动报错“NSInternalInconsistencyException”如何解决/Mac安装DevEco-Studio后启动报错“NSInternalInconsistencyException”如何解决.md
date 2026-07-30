# Mac安装DevEco-Studio后启动报错“NSInternalInconsistencyException”如何解决

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-20

#### 问题现象

Mac环境下，安装DevEco Studio后启动报错：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/2HAhbImGTiGzB5M3lns8GA/zh-cn_image_0000002658924269.png?HW-CC-KV=V1&HW-CC-Date=20260730T072708Z&HW-CC-Expire=86400&HW-CC-Sign=F50532470BDB364864E8B8828177AB4878B4CEA05BF03FE4A8A65FBF29767FD0)

 
报错信息如下图：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/fk4DniyJS3q2BBh2KoY_ug/zh-cn_image_0000002658804323.png?HW-CC-KV=V1&HW-CC-Date=20260730T072708Z&HW-CC-Expire=86400&HW-CC-Sign=E7783253F42930B78C4F192295203072B6D84B079EA47F5DF1EB632086FE6DA7)

 
 

#### 背景知识

Mac环境下安装DevEco Studio[操作指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-software-install#section102166218352)。
 
 

#### 解决方案

对于启动报错可以按照如下步骤处理：
 1. 找到DevEco Studio安装目录，用命令行sh bin/inspect.sh启动DevEco Studio，分析终端打印的错误日志。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/GJ4Tm2PmTMuRuW0NkjxZXA/zh-cn_image_0000002628564966.png?HW-CC-KV=V1&HW-CC-Date=20260730T072708Z&HW-CC-Expire=86400&HW-CC-Sign=98E0E815F4A1DED1C7ABE370CCFA2CC3B9A44D809F291B166C076415E15D6835)

2. 根据报错内容DEVECOSTUDIO_VM_OPTIONS = /Users/{USER_NAME}/Downloads/jihuo.live/jihuo-tool/vmoptions/devecostudio.vmoptions，可以判断启动脚本被修改了。
3. 删除启动脚本，启动脚本默认路径为“/Users/{USER_NAME}/Library/LaunchAgents/jetbrains.vmoptions.plist”，删除后重启Mac即可。
 
 

#### 总结

- 由于DevEco Studio和Jetbrains用的是相同的启动脚本，且脚本会一直沿用，如果脚本被修改，会导致不可知的问题。
- 如果运行过Jetbrains的破解软件，修改了Jetbrains启动脚本中的环境变量，会导致Java虚拟机无法启动，DevEco Studio无法打开。
