# 应用如何上架分发到多端（手机、PC、平板）

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-27

#### 问题现象

同一个应用如何上架分发到手机、PC、平板多端设备，工程代码和AppGallery Connect侧如何配置？
 
 

#### 背景知识

一个应用需要在多个设备上提供同样的内容，则需要适配不同的屏幕尺寸和硬件，开发成本较高。HarmonyOS系统面向多终端提供了“[一次开发，多端部署](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-overview)”（简称为“一多”）的能力，让开发者可以基于一套设计，高效构建多端可运行的应用。
 
 

#### 解决方案

应用上架时，需根据软件包中声明的设备（即module.json5配置文件中“[deviceTypes](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#devicetypes标签)”标签的枚举值）勾选对应的支持设备，确保软件包中声明的设备范围大于等于AppGallery Connect上勾选的支持设备范围。提交审核时会进行校验，如果AppGallery Connect上勾选的支持设备范围大于软件包内声明时，会提示上传的软件包与声明支持设备不一致，将无法提交审核。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/gFiJPu_LT_Kh9KKF0XON0Q/zh-cn_image_0000002658913803.png?HW-CC-KV=V1&HW-CC-Date=20260730T072658Z&HW-CC-Expire=86400&HW-CC-Sign=5F3DF83661AEE9347EC2682881151C1FE388C879A809D975B6F32B4A05A6319E)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/3TGHVg_3Tc2sVz9QUrS0pg/zh-cn_image_0000002658793861.png?HW-CC-KV=V1&HW-CC-Date=20260730T072658Z&HW-CC-Expire=86400&HW-CC-Sign=3E60B4C8F6AA9D76C8A3DC4F80BE63211318878D32D6C0138E8479178950BB4B)

 

 
 

#### 常见FAQ

Q：AppGallery Connect应用信息中的支持设备勾选分发的规则有哪些需要注意？
 
A：
 
1、当设备类型包含手机时，即便包里未声明平板，应用也会默认以兼容的方式分发到HarmonyOS NEXT平板。
 
2、当设备类型未勾选PC/2in1时，但手机和平板应用经过测试后会默认发布到PC/2in1。
 
更多详情参考[配置支持设备](https://developer.huawei.com/consumer/cn/doc/app/agc-help-release-app-devicetype-0000002271592112)。
 
Q：应用在手机端已上架，PC端和平板与手机端功能有所不同，如何只针对PC端和平板上架？
 
A：需要重新创建项目单独上架PC端和平板，包名和手机端区分开。
