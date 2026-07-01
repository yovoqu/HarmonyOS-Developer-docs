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

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/H3U674QDQmaHMqfFsPjrJw/zh-cn_image_0000002658808819.png?HW-CC-KV=V1&HW-CC-Date=20260701T041010Z&HW-CC-Expire=86400&HW-CC-Sign=A6958D4D265BAE415289FCDF30C9DC8C49A2660E39FF03A893C077E7F5EA1DF2)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/G0vMvEWFRsynmHRmeRjsaw/zh-cn_image_0000002628409552.png?HW-CC-KV=V1&HW-CC-Date=20260701T041010Z&HW-CC-Expire=86400&HW-CC-Sign=35029B3011F7557AA13306313ABBB47F6B6B6288AD27CFA9C4F914CC07929FD2)

2. 步骤二：PyCharm运行用例。

  模拟器启动后PyCharm可以查看本地模拟器已连接。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/_Gedla88RxqnqNwoEToV5g/zh-cn_image_0000002628569450.png?HW-CC-KV=V1&HW-CC-Date=20260701T041010Z&HW-CC-Expire=86400&HW-CC-Sign=74028FF4F93BF774691B749582C9EE6B9D9A01C08526F6D57DD07C837619A048)


  单台设备直接执行用例正常运行成功，同时模拟器正常展示用例运行过程。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/eZ_4dTMEQ5SO7z4UUo1-Rw/zh-cn_image_0000002658928767.png?HW-CC-KV=V1&HW-CC-Date=20260701T041010Z&HW-CC-Expire=86400&HW-CC-Sign=2AAEA3FA2AD5D44F76822555E0285B354D51BED98283F8FD9BD503D6B2D6E737)


  多台设备需在user_config.xml指定运行设备的sn，若指定运行设备是模拟器配置如下：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/8YIU5okYSNisy3tqDFYwAg/zh-cn_image_0000002658808821.png?HW-CC-KV=V1&HW-CC-Date=20260701T041010Z&HW-CC-Expire=86400&HW-CC-Sign=BA375A01E00F0F8C9F99FAA8E40571DD00F77E3409A7FAA381EA6109AAA1F8AF)
