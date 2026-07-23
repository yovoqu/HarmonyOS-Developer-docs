# Wearable和Lite Wearable穿戴设备真机调试和调测

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-76

#### 问题现象

开发者在开发Wearable和Lite Wearable设备应用时需要进行调试和调测，具体怎么做？
 
 

#### 背景知识

- Wearable设备推荐使用[WiFi无线调试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device#section9315596477)。
- 在Lite Wearable中运行应用/服务，依赖HarmonyOS NEXT版本以前的华为手机上的运动健康和应用调测助手APP辅助进行。

 
 

#### 解决方案

- Wearable设备调试：1. 将Wearable设备和PC连接到同一WLAN网络。在设置>系统>开发者选项中，打开“无线调试”或“通过WLAN调试”（Wearable设备）开关，并获取设备端的IP地址和端口号。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/-2Y6MOlWTOaSLtlXe1LzGQ/zh-cn_image_0000002658928657.png?HW-CC-KV=V1&HW-CC-Date=20260723T013950Z&HW-CC-Expire=86400&HW-CC-Sign=D2DE3F0AC1FADD5C58BEE02F346C765F63AEB7BCAC9D010A7BC488170C69DDA8)


2. 连接设备，有两种方式。
在DevEco Studio菜单栏中，单击Tools > IP Connection，输入连接设备的IP地址和端口号，单击，连接正常后，设备状态为online。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/sA_uOXycT2yCeURFIuGjdQ/zh-cn_image_0000002628409434.png?HW-CC-KV=V1&HW-CC-Date=20260723T013950Z&HW-CC-Expire=86400&HW-CC-Sign=E4BAB2AE578091508F58762CF8ABBE79D24C16F7855EC5582C053434C4858412)


3. 执行hdc命令，关于hdc工具的使用指导请参考[hdc](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc)。hdc tconn设备IP地址:端口号。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/sIcSBUe0TuO4hMiqVbmYzg/zh-cn_image_0000002658808701.png?HW-CC-KV=V1&HW-CC-Date=20260723T013950Z&HW-CC-Expire=86400&HW-CC-Sign=CE62C328BEA2CFF88EDB1D0715B5573E9937B5B8F6B95E6427128EF4A2FE9D65)


  在菜单栏中，单击Run>Run'模块名称'，或使用默认快捷键Shift+F10（macOS为Control+R）运行应用/元服务。
- DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

 - Lite wearable设备调试：前提条件：

1. 运动健康app升级最新版本。

2. 从华为应用市场安装应用调测助手APP。

3. 提前对应用/服务进行[签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)。

  具体步骤：

1. 使用USB连接线将手机和电脑进行连接，确保连接状态是正常的。

2. 手机与电脑使用USB连接时，在手机上选择传输文件连接方式。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/_7tOQOVnQAytsF2lRlyfkw/zh-cn_image_0000002628569340.png?HW-CC-KV=V1&HW-CC-Date=20260723T013950Z&HW-CC-Expire=86400&HW-CC-Sign=FAB4CE87089EF61857DDCC71B5FE9AE49C40280FECD482DD795D84FB75D29E26)


3. 在工程目录中的Build > outputs >hap中选择生成的HAP，通过手工拷贝的方式将HAP拷贝至手机中的“/sdcard/haps/”目录。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/UWRGHeBlSvO25TVs5zz03Q/zh-cn_image_0000002658928659.png?HW-CC-KV=V1&HW-CC-Date=20260723T013950Z&HW-CC-Expire=86400&HW-CC-Sign=6F28F5C1D648E28234DF2E5B24F2F70A4FB6B53A9D044FB22DD766D8D890B2B2)


4. 将Lite Wearable通过蓝牙与华为手机进行连接。
进入运动健康APP，在设备页签中，单击添加设备按钮。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/GRH3Gxv-Rtyq4WlEgze6Kw/zh-cn_image_0000002628409436.png?HW-CC-KV=V1&HW-CC-Date=20260723T013950Z&HW-CC-Expire=86400&HW-CC-Sign=928F0D40468FCF647739777BD443709FB6DD70CF219ECE9B8ECD2EC01D40C848)


5. 进入手表列表中，选择对应的Lite Wearable型号。

6. 单击开始配对，按照界面指引完成Lite Wearable与华为手机之间的连接。
- 打开应用调测助手APP，界面会显示已经与华为手机连接的Lite Wearable。
- 单击应用调测助手APP界面中的应用管理按钮，选择需要安装的HarmonyOS安装包进行安装。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/lBepdVLGTcmt5dNRhNZpqw/zh-cn_image_0000002658808703.png?HW-CC-KV=V1&HW-CC-Date=20260723T013950Z&HW-CC-Expire=86400&HW-CC-Sign=95FB40A36D727EA043063A7C61F2E24242F43A58B079B69BCDB8F151EFF44D2F)

- 安装完成后，单击Lite Wearable中的应用图标，运行HarmonyOS应用。
