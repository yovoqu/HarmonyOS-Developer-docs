# 小艺开放平台意图注册审核“APP名称”与应用名称不一致如何解决

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-intents-kit-2

#### 问题现象

开发者在小艺开放平台进行意图注册配置并提交审核，被告知意图注册审核后台识别的“APP名称”与该应用的实际名称不一致，如何修改？
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/sVcFcy81TSmUm7U12ayDRA/zh-cn_image_0000002658914055.png?HW-CC-KV=V1&HW-CC-Date=20260730T072732Z&HW-CC-Expire=86400&HW-CC-Sign=D4A0F41423E525EAFEDD259E867D6B8259EF9171DDE057A8713D0B172D39815D)

 
 

#### 背景知识

- Intents Kit（意图框架服务）是HarmonyOS级的意图标准体系，意图连接了应用/元服务内的业务功能。
- 开发者完成开发者测试后需在小艺开放平台进行意图注册配置并提交审核，审核通过后完成意图的正式上线。意图注册配置之前，APP需要先在AppGallery Connect（以下简称AGC）完成应用上架。

 
 

#### 问题定位
1. 检查代码工程：检查代码工程“AppScope/app.json5”文件中“app”内“label”字段对应的值（默认引用的为“AppScope/Resources/base/element/string.json”中name为“app_name”的value值），是否与应用名称一致，见下图字段。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/nD0aeG8aSvKZbTzdRt6tyg/zh-cn_image_0000002658794103.png?HW-CC-KV=V1&HW-CC-Date=20260730T072732Z&HW-CC-Expire=86400&HW-CC-Sign=3B32C43B54F5B43E558A20C47F4C00FF4B91A132D04125E9C8D54E7A6D820A4B)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/1QslmqjVTxuL40FIS6OZ3w/zh-cn_image_0000002628394840.png?HW-CC-KV=V1&HW-CC-Date=20260730T072732Z&HW-CC-Expire=86400&HW-CC-Sign=9DAE41DFB04FDAED73B8913A48FF16CC262AD79E4AA6E2AD84FC9FAB3CAECCC3)


  若不一致，则参考修改建议的步骤一和步骤二进行修改；若一致，执行下一步检查。
2. 检查意图注册提交时间：在小艺开放平台查看意图注册的提交时间，在应用市场查看包含正确“app_name”应用的上架完成时间。

  若意图注册提交时间早于应用上架时间，参考修改建议的步骤二进行修改。
 
 

#### 分析结论

在小艺开放平台提交意图注册后，会从已上架的应用中获取“APP名称”信息，审核时会核对该字段与应用名称是否一致，若不一致则需要提交人修改。
 
 

#### 修改建议
1. 修改“AppScope/app.json5”文件中“app”内“label”字段对应的值（默认引用的为“AppScope/Resources/base/element/string.json”中name为“app_name”的value值）为应用名称，重新打包应用上架。
2. 应用上架完成后，在小艺开放平台编辑已提交过的意图注册，参见[意图框架上架配置指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-configuration)，编辑保存后重新提交意图注册审核。
> [!NOTE]
> 必须是应用重新上架完成后，再重新提交意图注册审核。
