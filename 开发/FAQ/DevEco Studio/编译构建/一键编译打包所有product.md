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
<span style="color: rgb(0,0,255);">hvigorw </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">p product</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(0,0,255);">default </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">p buildMode</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(0,0,255);">release assembleApp</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">hvigorw </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">p product</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(0,0,255);">default1 </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">p buildMode</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(0,0,255);">release assembleApp</span><span style="color: rgb(181,106,1);">; </span><span style="color: rgb(0,0,255);">hvigorw </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">p product</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(0,0,255);">default2 </span><span style="color: rgb(181,106,1);">-</span><span style="color: rgb(0,0,255);">p buildMode</span><span style="color: rgb(181,106,1);">=</span><span style="color: rgb(0,0,255);">release assembleApp</span><span style="color: rgb(181,106,1);">;</span>
```
 
DevEco Studio配置的详细步骤如下：
 1. 编辑配置。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/XTD2U-AmQMSWazui9V4-Tw/zh-cn_image_0000002658928501.png?HW-CC-KV=V1&HW-CC-Date=20260701T041020Z&HW-CC-Expire=86400&HW-CC-Sign=95AA3508FAE0B539B7D89D63C5777AF391C7CBA9D6432E9ED886AD85C59F3E53)

2. 点击加号创建Shell Script。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/cRUx22M9RM-F44feRQ918w/zh-cn_image_0000002628409282.png?HW-CC-KV=V1&HW-CC-Date=20260701T041020Z&HW-CC-Expire=86400&HW-CC-Sign=1730587B0DB6E991FB6DA0A7430B9F511E2B526911E2F8CF2A14CB9D99002639)

3. 选择Script text，将命令写入，多个命令用分号隔开。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/_KEspRFpSZCJpw8TwHOenw/zh-cn_image_0000002658808553.png?HW-CC-KV=V1&HW-CC-Date=20260701T041020Z&HW-CC-Expire=86400&HW-CC-Sign=6AC10D8FF91A364F3F305877FAE05F2DB4D3E76D4924687C15603FA17409EF3E)

4. 切换创建的脚本，执行。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/gZQ8thPHSGSdkIaXMky7VQ/zh-cn_image_0000002628569178.png?HW-CC-KV=V1&HW-CC-Date=20260701T041020Z&HW-CC-Expire=86400&HW-CC-Sign=0EE8905AC27069A9DB49A24C4CAD6A8B01658E4AE202A5EE8C558E0626C9E43B)
