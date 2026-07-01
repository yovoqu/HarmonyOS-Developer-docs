# Wearable和Lite Wearable穿戴设备真机调试和调测

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-76

## Wearable和Lite Wearable穿戴设备真机调试和调测
 


##### 问题现象

开发者在开发Wearable和Lite Wearable设备应用时需要进行调试和调测，具体怎么做？
 
 

##### 背景知识

- Wearable设备推荐使用[WiFi无线调试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device#section9315596477)。
- 在Lite Wearable中运行应用/服务，依赖HarmonyOS NEXT版本以前的华为手机上的运动健康和应用调测助手APP辅助进行。

 
 

##### 解决方案

- Wearable设备调试：
将Wearable设备和PC连接到同一WLAN网络。在设置>系统>开发者选项中，打开“无线调试”或“通过WLAN调试”（Wearable设备）开关，并获取设备端的IP地址和端口号。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/-2Y6MOlWTOaSLtlXe1LzGQ/zh-cn_image_0000002658928657.png?HW-CC-KV=V1&HW-CC-Date=20260701T025920Z&HW-CC-Expire=86400&HW-CC-Sign=FF24EF2366DA478A12057F788477E4F96DF4AB35E7E6BC444414B9B712125CBB)

- 连接设备，有两种方式。
在DevEco Studio菜单栏中，单击Tools > IP Connection，输入连接设备的IP地址和端口号，单击，连接正常后，设备状态为online。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/sA_uOXycT2yCeURFIuGjdQ/zh-cn_image_0000002628409434.png?HW-CC-KV=V1&HW-CC-Date=20260701T025920Z&HW-CC-Expire=86400&HW-CC-Sign=A3D8A3F4B631081F8F46347E91795D1B0BC8AE43CA3207EC87D77E182FF9884C)

- 执行hdc命令，关于hdc工具的使用指导请参考[hdc](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc)。hdc tconn设备IP地址:端口号。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/sIcSBUe0TuO4hMiqVbmYzg/zh-cn_image_0000002658808701.png?HW-CC-KV=V1&HW-CC-Date=20260701T025920Z&HW-CC-Expire=86400&HW-CC-Sign=A13E95426C9801489D35DC3EFEB7EB49825FA22EFF4B04BF6A627B56DEE21689)

 在菜单栏中，单击Run>Run'模块名称'，或使用默认快捷键Shift+F10（macOS为Control+R）运行应用/元服务。

 - DevEco Studio启动HAP的编译构建和安装。安装成功后，设备会自动运行安装的HarmonyOS应用/元服务。

 - Lite wearable设备调试：前提条件：
 
运动健康app升级最新版本。
- 从华为应用市场安装应用调测助手APP。
- 提前对应用/服务进行[签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing)。

 
具体步骤：
 
- 使用USB连接线将手机和电脑进行连接，确保连接状态是正常的。
- 手机与电脑使用USB连接时，在手机上选择传输文件连接方式。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/_7tOQOVnQAytsF2lRlyfkw/zh-cn_image_0000002628569340.png?HW-CC-KV=V1&HW-CC-Date=20260701T025920Z&HW-CC-Expire=86400&HW-CC-Sign=4E630B89C3D72DF0DE7647FCA3BC941E8AAC810946154738E4084BE2591B75EA)

- 在工程目录中的Build > outputs >hap中选择生成的HAP，通过手工拷贝的方式将HAP拷贝至手机中的“/sdcard/haps/”目录。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/UWRGHeBlSvO25TVs5zz03Q/zh-cn_image_0000002658928659.png?HW-CC-KV=V1&HW-CC-Date=20260701T025920Z&HW-CC-Expire=86400&HW-CC-Sign=149E5877CDA2E6F19411E6E8DAAA9A8C502ABD256AA810A436B246E7CD598265)

- 将Lite Wearable通过蓝牙与华为手机进行连接。
进入运动健康APP，在设备页签中，单击添加设备按钮。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/GRH3Gxv-Rtyq4WlEgze6Kw/zh-cn_image_0000002628409436.png?HW-CC-KV=V1&HW-CC-Date=20260701T025920Z&HW-CC-Expire=86400&HW-CC-Sign=C902CCC730D6BA8E86CE980B78F39AB14DCC8ED5BC66C028A59133E4912736DC)

- 进入手表列表中，选择对应的Lite Wearable型号。
- 单击开始配对，按照界面指引完成Lite Wearable与华为手机之间的连接。

 - 打开应用调测助手APP，界面会显示已经与华为手机连接的Lite Wearable。
- 单击应用调测助手APP界面中的应用管理按钮，选择需要安装的HarmonyOS安装包进行安装。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/lBepdVLGTcmt5dNRhNZpqw/zh-cn_image_0000002658808703.png?HW-CC-KV=V1&HW-CC-Date=20260701T025920Z&HW-CC-Expire=86400&HW-CC-Sign=AC4D60DCDC45E304963B2E74FF5020312F3A39934FD0BE59D0F6766CAF1E6AA8)

- 安装完成后，单击Lite Wearable中的应用图标，运行HarmonyOS应用。
