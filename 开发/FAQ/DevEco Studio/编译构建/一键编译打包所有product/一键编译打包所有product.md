# 一键编译打包所有product

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-211

#### 问题现象

当项目包含多个product时，如何实现一键批量编译打包？目前只能逐个product进行编译打包，效率较低。
 
 

#### 背景知识

[hvigorw](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-commandline#section16300629103)作为Hvigor的wrapper包装工具，支持自动安装Hvigor构建工具和相关插件依赖，以及执行Hvigor构建命令。
 
编译构建参数详情见[编译构建](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-commandline#section9580122622012)。
 
 

#### 解决方案

通过hvigorw命令实现一键编译打包所有product。对应的命令行如下（这里的default、default1、default2替换为对应的product，如有更多product，可按相同格式追加命令）：
 
```text
hvigorw -p product=default -p buildMode=release assembleApp; hvigorw -p product=default1 -p buildMode=release assembleApp; hvigorw -p product=default2 -p buildMode=release assembleApp;
```
 
DevEco Studio配置的详细步骤如下：
 1. 编辑配置。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/XTD2U-AmQMSWazui9V4-Tw/zh-cn_image_0000002658928501.png?HW-CC-KV=V1&HW-CC-Date=20260730T072714Z&HW-CC-Expire=86400&HW-CC-Sign=7378CC2DF96DF463B8CAF0CEF5A4DC1B583987D61C75449B789E639FA1DFFEE2)

2. 点击加号创建Shell Script。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/cRUx22M9RM-F44feRQ918w/zh-cn_image_0000002628409282.png?HW-CC-KV=V1&HW-CC-Date=20260730T072714Z&HW-CC-Expire=86400&HW-CC-Sign=A666F21AAD618B3404E87A4EF032700B17EB518E61E7DF126984F35723C50C7C)

3. 选择Script text，将命令写入，多个命令用分号隔开。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/_KEspRFpSZCJpw8TwHOenw/zh-cn_image_0000002658808553.png?HW-CC-KV=V1&HW-CC-Date=20260730T072714Z&HW-CC-Expire=86400&HW-CC-Sign=1022EABC9833958F857ADABF4F54A90DF8653609310114C8B59076E12D91475A)

4. 切换创建的脚本，执行。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/gZQ8thPHSGSdkIaXMky7VQ/zh-cn_image_0000002628569178.png?HW-CC-KV=V1&HW-CC-Date=20260730T072714Z&HW-CC-Expire=86400&HW-CC-Sign=592C3DFEAE6DFB10F84E2429603157D54AD82CFE1C261A46C6A454728E1F8284)
