# Wearable和Lite Wearable穿戴设备真机调试和调测

更新时间：2026-08-05 01:58:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-76

#### 问题现象

开发者在开发Wearable和Lite Wearable设备应用时需要进行调试和调测，具体怎么做？
 
 

#### 背景知识

- Wearable设备推荐使用[WiFi无线调试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device#section9315596477)。
- 在Lite Wearable中运行应用/服务，依赖HarmonyOS NEXT版本以前的华为手机上的运动健康和应用调测助手APP辅助进行。

 
 

#### 解决方案

- Wearable设备调试：前提条件：需要登录华为开发者账号才有无线调试选项。

1. 将Wearable设备和PC连接到同一WLAN网络。在设置>系统>开发者选项中，打开"无线调试"或"通过WLAN调试"（Wearable设备）开关，并获取设备端的IP地址和端口号。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/zPwXAz10Tca4G6g7HqsTaA/zh-cn_image_0000002693109095.png?HW-CC-KV=V1&HW-CC-Date=20260811T005519Z&HW-CC-Expire=86400&HW-CC-Sign=F28589564F3B53191252542D01598434646A0941F240A05AB51197ED5F8E0844)


2. 连接设备，有两种方式。
在DevEco Studio菜单栏中，单击Tools > IP Connection，输入连接设备的IP地址和端口号，单击，连接正常后，设备状态为online。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/pHbo7iIwSDuAZQdJTqtZdA/zh-cn_image_0000002693109103.png?HW-CC-KV=V1&HW-CC-Date=20260811T005519Z&HW-CC-Expire=86400&HW-CC-Sign=A57CE7F5AFE6D26AEDE2354C37AE9D5099297187F68D3FD5017868D7FC7F9419)


3. 执行hdc命令，关于hdc工具的使用指导请参考[hdc](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc)。hdc tconn设备IP地址:端口号。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/td7hONZvQ6uYL0DnB6aZ5w/zh-cn_image_0000002663349102.png?HW-CC-KV=V1&HW-CC-Date=20260811T005519Z&HW-CC-Expire=86400&HW-CC-Sign=C62878FB381430BCB3258FAA1A927D5C3FA27C1369831180E7C47BE7C620B00C)


  在菜单栏中，单击Run>Run'模块名称'或使用默认快捷键Shift+F10（macOS为Control+R）运行应用/元服务。
- DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

 - Lite wearable设备调试：前提条件：

1. 运动健康app升级最新版本。

2. 从华为应用市场安装应用调测助手APP。

3. 提前对应用/服务进行[签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)。

  具体步骤：

1. 使用USB连接线将手机和电脑进行连接，确保连接状态是正常的。

2. 手机与电脑使用USB连接时，在手机上选择传输文件连接方式。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/m_ph-l51S6auaMLZXNVCYQ/zh-cn_image_0000002663189188.png?HW-CC-KV=V1&HW-CC-Date=20260811T005519Z&HW-CC-Expire=86400&HW-CC-Sign=CADF9DE3F75FD882639A1FA09A725CA1F8100D3D1CF843440D086B2297972084)


3. 在工程目录中的Build > outputs >hap中选择生成的HAP，通过手工拷贝的方式将HAP拷贝至手机中的"/sdcard/haps/"目录。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/gnk-BC34Tv2uv6nXgvGWFg/zh-cn_image_0000002663189190.png?HW-CC-KV=V1&HW-CC-Date=20260811T005519Z&HW-CC-Expire=86400&HW-CC-Sign=9C698662AF3E0C731B8C7841F8D6037062604B347061F29F553BB6462960B633)


4. 将Lite Wearable通过蓝牙与华为手机进行连接。
进入运动健康APP，在设备页签中，单击添加设备按钮。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/ht3AJlm7T6i7Ote7JEmJkw/zh-cn_image_0000002663349106.png?HW-CC-KV=V1&HW-CC-Date=20260811T005519Z&HW-CC-Expire=86400&HW-CC-Sign=6049F3C165F5FE0CCF4BE699321CC6E6F7E8ED1779C2FF88725E0D092FCF0E9C)


5. 进入手表列表中，选择对应的Lite Wearable型号。

6. 单击开始配对，按照界面指引完成Lite Wearable与华为手机之间的连接。
- 打开应用调测助手APP，界面会显示已经与华为手机连接的Lite Wearable。
- 单击应用调测助手APP界面中的应用管理按钮，选择需要安装的HarmonyOS安装包进行安装。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/CcvbTsR0TMGDjqO_MkYc6g/zh-cn_image_0000002663189192.png?HW-CC-KV=V1&HW-CC-Date=20260811T005519Z&HW-CC-Expire=86400&HW-CC-Sign=399BDFCF44EC2FAC258C090A4E79F1B561C0CB0872E46155C01BE04B407A195A)

- 安装完成后，单击Lite Wearable中的应用图标，运行HarmonyOS应用。

 
 
 

#### 常见FAQ

Q：HarmonyOS NEXT系统上能否开发Lite Wearable类型的手表应用？
 
A：Lite Wearable中运行应用/服务依赖HarmonyOS NEXT版本以前的手机上的运动健康和应用调测助手APP辅助进行，暂不支持在HarmonyOS NEXT系统上直接调试Lite Wearable设备。轻量级智能穿戴与智能穿戴在硬件能力和系统支持上不同，暂时无法仅开发一版实现通用。Wearable是当前更主流的方向，是HarmonyOS NEXT生态重点支持的穿戴设备类型。
 
Q：通过应用调测助手向Lite Wearable设备安装HAP时提示"安装失败：40.配置文件格式错误"怎么办？
 
A：该问题通常是由于工程级[build-profile.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app)中[compatibleSdkVersion](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app#section45865492619)配置格式不正确导致。compatibleSdkVersion必须写成5.0.0(12)格式，不能写成其他字符串格式。
