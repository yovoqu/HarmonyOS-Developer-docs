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
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/GxmcvM6QRlqLI-2S9WaUCw/zh-cn_image_0000002628569540.png?HW-CC-KV=V1&HW-CC-Date=20260730T072724Z&HW-CC-Expire=86400&HW-CC-Sign=41E6B357281FEACB42A89D2C36A3A7834BF644030EC04208924112E5948E4B24)


2. 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Instrument Test”；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/WhnSAIpnTRyvQoJjJwltvw/zh-cn_image_0000002658928865.png?HW-CC-KV=V1&HW-CC-Date=20260730T072724Z&HW-CC-Expire=86400&HW-CC-Sign=F6E3F94154F4FCF35CACD7845E567F5DCF557B188693E500A3B8BEEA1BF6FEB9)

- 如果创建的是Local Test用例：1. 排查是否存在[代码测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-test)中Local Test的相关约束与限制；

2. 排查工程中是否存在“src/test”路径；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/RbMARSoKRvaN0SWRPUu8Jg/zh-cn_image_0000002628409650.png?HW-CC-KV=V1&HW-CC-Date=20260730T072724Z&HW-CC-Expire=86400&HW-CC-Sign=BAE1630FC59CC376FDF832E7FFFFDF07D48DA055B12DDC276FB5FF24C52620D7)


3. 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Local Test”；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/a0WpWk1JQt6kiFNc8o0YrA/zh-cn_image_0000002658808911.png?HW-CC-KV=V1&HW-CC-Date=20260730T072724Z&HW-CC-Expire=86400&HW-CC-Sign=37AE8123E84849D22197A68ACC103FA4CDFA4C3CDADA1D9BB039D5B09EF03725)


 
 

#### 分析结论

IDE中未设置允许创建“Create Instrument Test”或“Create Local Test”。
 
 

#### 修改建议

打开IDE，点击Settings->Editor->Intentions->JavaScript，勾选“Create Instrument Test”和“Create Local Test”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MGnnPmMaRXC96D6_WTaGLw/zh-cn_image_0000002628569542.png?HW-CC-KV=V1&HW-CC-Date=20260730T072724Z&HW-CC-Expire=86400&HW-CC-Sign=85A286B2420C9EBC7B37C7254937280D7509E1D3F906BAE0E0DC7680B2FF5D33)

 
 

#### 总结

在创建Local Test用例时需要关注约束与限制；IDE中需要设置允许创建“Create Instrument Test”或“Create Local Test”。
