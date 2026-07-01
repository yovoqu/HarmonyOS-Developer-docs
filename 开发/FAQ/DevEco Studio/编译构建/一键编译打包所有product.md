# 一键编译打包所有product

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-211

## 一键编译打包所有product
 


##### 问题现象

当项目包含多个product时，如何实现一键批量编译打包？目前只能逐个product进行编译打包，效率较低。
 
 

##### 背景知识

[hvigorw](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-commandline#section16300629103)作为Hvigor的wrapper包装工具，支持自动安装Hvigor构建工具和相关插件依赖，以及执行Hvigor构建命令。
 
编译构建参数详情见[编译构建](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-commandline#section9580122622012)。
 
 

##### 解决方案

通过hvigorw命令实现一键编译打包所有product。对应的命令行如下（这里的default、default1、default2替换为对应的product，如有更多product，可按相同格式追加命令）：
 
```text
hvigorw -p product=default -p buildMode=release assembleApp; hvigorw -p product=default1 -p buildMode=release assembleApp; hvigorw -p product=default2 -p buildMode=release assembleApp;
```
 
DevEco Studio配置的详细步骤如下：
 
- 编辑配置。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/XTD2U-AmQMSWazui9V4-Tw/zh-cn_image_0000002658928501.png?HW-CC-KV=V1&HW-CC-Date=20260701T025915Z&HW-CC-Expire=86400&HW-CC-Sign=A1E72F4097E649686A911C0943843FFF70E112BBC22497D192056C05AF2FD757)

- 点击加号创建Shell Script。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/cRUx22M9RM-F44feRQ918w/zh-cn_image_0000002628409282.png?HW-CC-KV=V1&HW-CC-Date=20260701T025915Z&HW-CC-Expire=86400&HW-CC-Sign=8D36A489CF4387B3A6A8B93E750B65F59490B41B8EE1A7457B32B0AE70BC1259)

- 选择Script text，将命令写入，多个命令用分号隔开。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/_KEspRFpSZCJpw8TwHOenw/zh-cn_image_0000002658808553.png?HW-CC-KV=V1&HW-CC-Date=20260701T025915Z&HW-CC-Expire=86400&HW-CC-Sign=67FDAFBE5F5E4534BF2C331998CD1612E9F84CB2D208440B7EDAE2DF0A35F62B)

- 切换创建的脚本，执行。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/gZQ8thPHSGSdkIaXMky7VQ/zh-cn_image_0000002628569178.png?HW-CC-KV=V1&HW-CC-Date=20260701T025915Z&HW-CC-Expire=86400&HW-CC-Sign=A5E031631BD0E5D8B19B572626D329C13E5573B631C70FD425C9FD65DCD070C1)
