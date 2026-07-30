# IDE编写C++代码时没有提示

更新时间：2026-07-30 01:18:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-31

#### 问题现象

IDE编写C++代码没有自动补全提示，点击变量名也无法快速定位或者跳转，且IDE右下角服务点为红色。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Ib52u4HFRomLqqAu8qsr9g/zh-cn_image_0000002658924309.png?HW-CC-KV=V1&HW-CC-Date=20260730T072709Z&HW-CC-Expire=86400&HW-CC-Sign=9B89A0428C5F5E72081E3A234DA0EE5D698631A2FCC70D96CD1CCAE475597B33)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/9e39VDdBQtWJ7ii0lIqsXw/zh-cn_image_0000002658804363.png?HW-CC-KV=V1&HW-CC-Date=20260730T072709Z&HW-CC-Expire=86400&HW-CC-Sign=3A46505B3158B39FD3A352D821EFF9540195C8BBBEDED257D3745DC03AF6B5B8)

 
 

#### 背景知识

[DevEco Studio](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment)是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助高效开发HarmonyOS应用及元服务。
 
 

#### 问题定位

进入IDE安装目录例如：“C:\Program Files\Huawei\DevEco Studio\tools\llvm\server\lsp\win”，点击clangd.exe文件，看下是否有报错vcruntime140.dll文件缺失。
 
 

#### 分析结论

由于vcruntime140.dll文件缺失导致IDE服务无法正常拉起，编写代码没有提示也无法快速定位或者跳转。
 
 

#### 修改建议

在网上下载vcruntime140.dll文件并放入：“C:\Windows\System32”下，重新运行clangd.exe成功后，再重启IDE后问题解决。
