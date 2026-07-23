# 单元测试如何创建ArkTS测试用例

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-39

#### 问题现象

在代码内部使用Show Context Actions创建单元测试用例时，提示No context actions available at this location。
 
 

#### 背景知识

- [Instrument Test](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-instrument-test)的测试用例存放在ohosTest测试目录下，需要运行在设备或模拟器上。
- [Local Test](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-local-test)的测试用例存放在test测试目录下，不需要运行在设备或模拟器上。

 
 

#### 问题定位

- 如果创建的是Instrument Test用例：1. 排查工程中是否存在“src/ohosTest”路径；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/GxmcvM6QRlqLI-2S9WaUCw/zh-cn_image_0000002628569540.png?HW-CC-KV=V1&HW-CC-Date=20260723T014007Z&HW-CC-Expire=86400&HW-CC-Sign=9B4F4452BACF43798B629BAA84E89B955109E1BF633BD40654BA7D24CC1D89E0)


2. 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Instrument Test”；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/WhnSAIpnTRyvQoJjJwltvw/zh-cn_image_0000002658928865.png?HW-CC-KV=V1&HW-CC-Date=20260723T014007Z&HW-CC-Expire=86400&HW-CC-Sign=04E71430CFDD7886676DFA800CAB3B87A319B17CC0D07A1667988727ED0FA0AC)

- 如果创建的是Local Test用例：1. 排查是否存在[代码测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-test)中Local Test的相关约束与限制；

2. 排查工程中是否存在“src/test”路径；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/RbMARSoKRvaN0SWRPUu8Jg/zh-cn_image_0000002628409650.png?HW-CC-KV=V1&HW-CC-Date=20260723T014007Z&HW-CC-Expire=86400&HW-CC-Sign=873B8334A0BB3398B87DD53547F931064390A260B2845BD27C06C70A0E227024)


3. 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Local Test”；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/a0WpWk1JQt6kiFNc8o0YrA/zh-cn_image_0000002658808911.png?HW-CC-KV=V1&HW-CC-Date=20260723T014007Z&HW-CC-Expire=86400&HW-CC-Sign=C1FBE0C9CEF7C8672BDFC4FF2F6A6FC039C4C568C58AD9E8DDB0F11D087A7E41)


 
 

#### 分析结论

IDE中未设置允许创建“Create Instrument Test”或“Create Local Test”。
 
 

#### 修改建议

打开IDE，点击Settings->Editor->Intentions->JavaScript，勾选“Create Instrument Test”和“Create Local Test”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MGnnPmMaRXC96D6_WTaGLw/zh-cn_image_0000002628569542.png?HW-CC-KV=V1&HW-CC-Date=20260723T014007Z&HW-CC-Expire=86400&HW-CC-Sign=C97F67B1576A9013B4E1326D83DBFB39B2839378973BE09C81154DB342CCB760)

 
 

#### 总结

在创建Local Test用例时需要关注约束与限制；IDE中需要设置允许创建“Create Instrument Test”或“Create Local Test”。
