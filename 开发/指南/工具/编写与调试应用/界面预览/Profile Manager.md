# Profile Manager

更新时间：2026-03-17 02:59:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-profile-manager

由于真机设备型号众多，不同设备型号的屏幕分辨率可能各不相同。因此，在HarmonyOS应用/元服务开发过程中，为了适配多种设备型号，可能需要查看不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以通过定义不同的预览设备Profile，查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。
 
定义设备后，可以在Previewer右上角，单击
![](assets/Profile%20Manager/file-20260514132934956-0.png)
按钮，打开Profile管理器，切换预览设备。
 

![](assets/Profile%20Manager/file-20260514132934956-1.png)

 
同时，Profile Manager还支持多设备预览功能，具体请参考[查看多端设备预览效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-multi-profile)。
 
下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。
 1. 在预览器界面，打开Profile Manager界面。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/eohZDrIKTlacB0yAS2JnNQ/zh-cn_image_0000002571386802.png?HW-CC-KV=V1&HW-CC-Date=20260528T014957Z&HW-CC-Expire=86400&HW-CC-Sign=46807123C96A4907BFA2F25A44F4339C8B705A0BC73994E6570C4F0EEDBB71FF)

2. 在Profile Manager界面，单击**+ New Profile**按钮，添加设备。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/Q2JvkHATSImxhKx5SN8amg/zh-cn_image_0000002602065917.png?HW-CC-KV=V1&HW-CC-Date=20260528T014957Z&HW-CC-Expire=86400&HW-CC-Sign=D94EDCFF80F2E51E5B204D95427CA3255E624682D4B70C015CB2B6B746673DCD)

3. 在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Nf7Ems1BTRGq0etGwIPRCg/zh-cn_image_0000002571386800.png?HW-CC-KV=V1&HW-CC-Date=20260528T014957Z&HW-CC-Expire=86400&HW-CC-Sign=90271D7C3E9B6C9189706380EE9271EA42F501B995D185536450EE68872CC9D7)

4. 设备信息填写完成后，单击**OK**完成创建。
