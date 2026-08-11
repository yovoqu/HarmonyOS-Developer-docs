# Hypium是否支持在模拟器上执行测试用例

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-23

#### 问题现象

Hypium自动化的测试用例是否支持在模拟器上运行以及如何操作。
 
 

#### 背景知识

- [DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/)提供[使用模拟器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-use?ha_source=sousuo&ha_sourceId=89000251)（Emulator），为开发者提供了运行和调试HarmonyOS应用/元服务的便捷方式。模拟器还原了真实设备的基本功能，如屏幕旋转、音量调节、模拟的硬件传感器和指定设备的位置等。这使得您无需拥有不同类型的物理设备，就可以在各种虚拟环境中轻松测试您的应用程序。
- [DevEco Testing Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)以下简称（Hypium）是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本。

 
 

#### 解决方案

Hypium自动化测试用例支持在模拟器中运行。步骤如下：
 1. 步骤一：DevEco Studio启动模拟器。

  点击菜单栏的Tools > Device Manager > Run如图：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/H3U674QDQmaHMqfFsPjrJw/zh-cn_image_0000002658808819.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=64CDEEE0B75143FFA15824A6E13702C64C34081F45B8E6A496E9B6A906980459)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/G0vMvEWFRsynmHRmeRjsaw/zh-cn_image_0000002628409552.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=02F8F7A091E25758EEE8BAAC91EBF146BA303D7B0F8479E0532980B329726C9C)

2. 步骤二：PyCharm运行用例。

  模拟器启动后PyCharm可以查看本地模拟器已连接。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/_Gedla88RxqnqNwoEToV5g/zh-cn_image_0000002628569450.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=C296FF6FF788DAB040C03DE4BD0675196F5A1B371136BE4BC4DF8333B2193499)


  单台设备直接执行用例正常运行成功，同时模拟器正常展示用例运行过程。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/eZ_4dTMEQ5SO7z4UUo1-Rw/zh-cn_image_0000002658928767.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=9AA7F97F906AC3137D80A6508F4D9B7ED61ED1D19163B068934B4F1ABC62DDDD)


  多台设备需在user_config.xml指定运行设备的sn，若指定运行设备是模拟器配置如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/8YIU5okYSNisy3tqDFYwAg/zh-cn_image_0000002658808821.png?HW-CC-KV=V1&HW-CC-Date=20260811T005517Z&HW-CC-Expire=86400&HW-CC-Sign=65A8161E03994B27327A4F2805C0BBDC64326303D3ED33300A6A428B67326395)
