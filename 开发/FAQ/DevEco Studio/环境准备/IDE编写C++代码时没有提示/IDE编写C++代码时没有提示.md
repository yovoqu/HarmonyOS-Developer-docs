# IDE编写C++代码时没有提示

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-31

#### 问题现象

IDE编写C++代码没有自动补全提示，点击变量名也无法快速定位或者跳转，且IDE右下角服务点为红色。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/4QHDpMsNR1-KV1dgnnVqCA/zh-cn_image_0000002658924309.png?HW-CC-KV=V1&HW-CC-Date=20260723T013905Z&HW-CC-Expire=86400&HW-CC-Sign=BD5B33244E55125A6A7BADA2121089F3DCB9305A98C6AE1322F744CCA592FB8C)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/uWQmGu_sT92TAJq-G6FrbA/zh-cn_image_0000002658804363.png?HW-CC-KV=V1&HW-CC-Date=20260723T013905Z&HW-CC-Expire=86400&HW-CC-Sign=28C2C661A6699340AB37864CD275C566B104AD3D3B76B6776CA371BB1FAE0837)

 
 

#### 背景知识

[DevEco Studio](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-deveco-studio)是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助高效开发HarmonyOS应用及元服务。
 
 

#### 问题定位

进入IDE安装目录例如：“C:\Program Files\Huawei\DevEco Studio\tools\llvm\server\lsp\win”，点击clangd.exe文件，看下是否有报错vcruntime140.dll文件缺失。
 
 

#### 分析结论

由于vcruntime140.dll文件缺失导致IDE服务无法正常拉起，编写代码没有提示也无法快速定位或者跳转。
 
 

#### 修改建议

在网上下载vcruntime140.dll文件并放入：“C:\Windows\System32”下，重新运行clangd.exe成功后，再重启IDE后问题解决。
