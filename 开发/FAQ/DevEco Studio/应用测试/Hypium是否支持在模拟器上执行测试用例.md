# Hypium是否支持在模拟器上执行测试用例

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-23

## Hypium是否支持在模拟器上执行测试用例
 


##### 问题现象

Hypium自动化的测试用例是否支持在模拟器上运行以及如何操作。
 
 

##### 背景知识

- [DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)提供[使用模拟器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-use?ha_source=sousuo&ha_sourceId=89000251)（Emulator），为开发者提供了运行和调试HarmonyOS应用/元服务的便捷方式。模拟器还原了真实设备的基本功能，如屏幕旋转、音量调节、模拟的硬件传感器和指定设备的位置等。这使得您无需拥有不同类型的物理设备，就可以在各种虚拟环境中轻松测试您的应用程序。
- [DevEco Testing Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)以下简称（Hypium）是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本。

 
 

##### 解决方案

Hypium自动化测试用例支持在模拟器中运行。步骤如下：
 
- 步骤一：DevEco Studio启动模拟器。
点击菜单栏的Tools > Device Manager > Run如图：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/H3U674QDQmaHMqfFsPjrJw/zh-cn_image_0000002658808819.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=A38D991023244927B0353D338236DECB805274ED3AAA3019E6A2C97F31E9FC2A)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/G0vMvEWFRsynmHRmeRjsaw/zh-cn_image_0000002628409552.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=B322DD18CE059EFED207FD76F226FE1873B57F2EEE73A4F7B0279171E9C98BB6)

- 步骤二：PyCharm运行用例。
模拟器启动后PyCharm可以查看本地模拟器已连接。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/_Gedla88RxqnqNwoEToV5g/zh-cn_image_0000002628569450.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=0FE197B8817A5DD17B59CDBFD400F5A259C1AEBA1D5560FE81307EBD58D0B1BE)

 单台设备直接执行用例正常运行成功，同时模拟器正常展示用例运行过程。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/eZ_4dTMEQ5SO7z4UUo1-Rw/zh-cn_image_0000002658928767.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=5F161D1D06DABC2168D56056BD1C9B8194871F4270A72449E526CF6C99A6944C)

 多台设备需在user_config.xml指定运行设备的sn，若指定运行设备是模拟器配置如下：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/8YIU5okYSNisy3tqDFYwAg/zh-cn_image_0000002658808821.png?HW-CC-KV=V1&HW-CC-Date=20260701T025922Z&HW-CC-Expire=86400&HW-CC-Sign=C299A37FF726B20F5DF0D108BD5E47E702277E3C269FA9D3B407C948399C4360)
