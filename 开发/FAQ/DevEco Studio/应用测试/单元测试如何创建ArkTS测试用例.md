# 单元测试如何创建ArkTS测试用例

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-39

## 单元测试如何创建ArkTS测试用例
 


##### 问题现象

在代码内部使用Show Context Actions创建单元测试用例时，提示No context actions available at this location。
 
 

##### 背景知识

- [Instrument Test](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-instrument-test)的测试用例存放在ohosTest测试目录下，需要运行在设备或模拟器上。
- [Local Test](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-local-test)的测试用例存放在test测试目录下，不需要运行在设备或模拟器上。

 
 

##### 问题定位

- 如果创建的是Instrument Test用例：
排查工程中是否存在“src/ohosTest”路径；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/GxmcvM6QRlqLI-2S9WaUCw/zh-cn_image_0000002628569540.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=F8F39F69512F7B5E8E5C49F5C2E7F549698848FAA7D9D99F18151DA6D2327FAD)

- 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Instrument Test”；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/WhnSAIpnTRyvQoJjJwltvw/zh-cn_image_0000002658928865.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=318694FB3555889CC84C72F1D1E39F074AB248766534DCEB28C34336E19995C4)


 - 如果创建的是Local Test用例：
排查是否存在[代码测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-test)中Local Test的相关约束与限制；
- 排查工程中是否存在“src/test”路径；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/RbMARSoKRvaN0SWRPUu8Jg/zh-cn_image_0000002628409650.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=73B62EC8AFFED18F4E615A018E82D735ED9F6A70BDDF03F667AE71A78BECB966)

- 点击Settings->Editor->Intentions->JavaScript，查看是否勾选“Create Local Test”；
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/a0WpWk1JQt6kiFNc8o0YrA/zh-cn_image_0000002658808911.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=734E9C46305F38BB8C5771FDF42CBB619AD677E5B7717683A4525B78AC3112C2)


 
 
 

##### 分析结论

IDE中未设置允许创建“Create Instrument Test”或“Create Local Test”。
 
 

##### 修改建议

打开IDE，点击Settings->Editor->Intentions->JavaScript，勾选“Create Instrument Test”和“Create Local Test”。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MGnnPmMaRXC96D6_WTaGLw/zh-cn_image_0000002628569542.png?HW-CC-KV=V1&HW-CC-Date=20260701T025923Z&HW-CC-Expire=86400&HW-CC-Sign=7111B98359CFDF754679D40804D28292CAB5EE24E6496D02481B8AE06F363073)

 
 

##### 总结

在创建Local Test用例时需要关注约束与限制；IDE中需要设置允许创建“Create Instrument Test”或“Create Local Test”。
