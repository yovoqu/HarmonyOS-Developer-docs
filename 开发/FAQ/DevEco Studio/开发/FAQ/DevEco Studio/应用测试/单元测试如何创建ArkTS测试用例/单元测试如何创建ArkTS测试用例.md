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
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/GxmcvM6QRlqLI-2S9WaUCw/zh-cn_image_0000002628569540.png?HW-CC-KV=V1&HW-CC-Date=20260811T005518Z&HW-CC-Expire=86400&HW-CC-Sign=D7E6FF2246FEDB45F07400DEE1E0EB6853C4F9C8C8B84D9BA6130C2CC77ADB12)


2. 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Instrument Test”；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/WhnSAIpnTRyvQoJjJwltvw/zh-cn_image_0000002658928865.png?HW-CC-KV=V1&HW-CC-Date=20260811T005518Z&HW-CC-Expire=86400&HW-CC-Sign=6C50BD80FBA5BBD32D301C01A3A79057768EE15BFF6B394B008D0B588BE84704)

- 如果创建的是Local Test用例：1. 排查是否存在[代码测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-test)中Local Test的相关约束与限制；

2. 排查工程中是否存在“src/test”路径；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/RbMARSoKRvaN0SWRPUu8Jg/zh-cn_image_0000002628409650.png?HW-CC-KV=V1&HW-CC-Date=20260811T005518Z&HW-CC-Expire=86400&HW-CC-Sign=907DDD3A8D87186750D897D9E81711311F9AD40E35770BD43068586FE7110D2A)


3. 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Local Test”；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/a0WpWk1JQt6kiFNc8o0YrA/zh-cn_image_0000002658808911.png?HW-CC-KV=V1&HW-CC-Date=20260811T005518Z&HW-CC-Expire=86400&HW-CC-Sign=466EC810EF100C3D3A738017DC3272A79C3A47E2AE1D80AA9171E40BE650AB47)


 
 

#### 分析结论

IDE中未设置允许创建“Create Instrument Test”或“Create Local Test”。
 
 

#### 修改建议

打开IDE，点击Settings->Editor->Intentions->JavaScript，勾选“Create Instrument Test”和“Create Local Test”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MGnnPmMaRXC96D6_WTaGLw/zh-cn_image_0000002628569542.png?HW-CC-KV=V1&HW-CC-Date=20260811T005518Z&HW-CC-Expire=86400&HW-CC-Sign=C21B74E86647490BFED80A5F6D33451387788D843563C5986A47388AA63B93A9)

 
 

#### 总结

在创建Local Test用例时需要关注约束与限制；IDE中需要设置允许创建“Create Instrument Test”或“Create Local Test”。
