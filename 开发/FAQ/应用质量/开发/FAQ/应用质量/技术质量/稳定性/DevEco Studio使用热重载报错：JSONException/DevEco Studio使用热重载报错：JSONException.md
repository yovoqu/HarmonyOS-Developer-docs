# DevEco Studio使用热重载报错：JSONException

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-54

#### 问题现象

DevEco Studio热重载启动应用报错：JSONException。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/j9t62p61Q8KmRuX3R1MwTA/zh-cn_image_0000002628554894.png?HW-CC-KV=V1&HW-CC-Date=20260811T005907Z&HW-CC-Expire=86400&HW-CC-Sign=4579A163A8B36CBD1457334DCFD7532355F0EDCA1F6E90CF1DE54719B70AC906)

 
 

#### 背景知识

DevEco Studio提供Hot Reload（热重载）能力，支持开发者在真机或模拟器上运行/调试应用时，修改代码并保存后无需重启应用，在真机或模拟器上即可使用最新的代码，帮助开发者更快速地进行调试。使用约束和操作步骤可以参考：[Hot Reload](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hot-reload#section995453874915)。
 
 

#### 问题定位

根据报错提示，是JSON序列化的问题，而使用热重载时会在模块下生成一个patch.json文件，记录着应用和模块信息，排查是否修改过这个文件，导致序列化异常。
 
 

#### 分析结论

patch.json文件被修改过，导致序列化异常。
 
 

#### 修改建议

删除patch.json文件，之后热重载时会重新生成。
