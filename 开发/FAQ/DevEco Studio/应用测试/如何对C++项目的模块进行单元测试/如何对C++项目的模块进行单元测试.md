# 如何对C++项目的模块进行单元测试

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-30

#### 问题现象

创建一个Native C++项目，新建一个HSP模块，如何对此模块进行单元测试呢？
 
 

#### 解决方案

从DevEco Studio 6.0.0 Beta5版本开始，支持[测试C++代码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-instrument-test#section1617524564017)，由于C++的测试so无法直接在设备上运行，需要通过[Node-API](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-introduction)的方式拉起，即通过ArkTS/JS语言拉起C/C++测试用例。
 
- [创建Native C++工程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-process#创建native-c工程)：在DevEco Studio中New > Create Project，选择Native C++模板，点击Next，选择API版本，设置好工程名称，点击Finish，创建得到新工程。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/vjUm1YGoTYG635DIsddN0A/zh-cn_image_0000002628569516.png?HW-CC-KV=V1&HW-CC-Date=20260730T072723Z&HW-CC-Expire=86400&HW-CC-Sign=4EEF4B6A140E2E5ED81E9ABAF4AE03119906A20F3CDA7C8ECFDAD8E948E0CA78)

- [创建](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/in-app-hsp#创建)HSP模块：鼠标移到工程目录顶部，单击鼠标右键，选择New > Module，选择Shared Library，并在“Configure New Module”页面中输入模块名，图中为library，启用“Enable native”选项。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/uMFDb4xeRxignMX5Fur3ig/zh-cn_image_0000002658928839.png?HW-CC-KV=V1&HW-CC-Date=20260730T072723Z&HW-CC-Expire=86400&HW-CC-Sign=A7DFF33DF24C3F8E0D01C8EB4A28FC284E949548719E586005098D34D239ECFE)

- 在HSP模块library中进行C++测试，参考测试C++代码，鼠标右键单击工程目录“\library\src\ohosTest”目录，选择New > C/C++ File(Napi)，在ohosTest下生成cpp测试目录，在工程目录“\library\src\ohosTest\ets\test”下实现单元测试代码。
