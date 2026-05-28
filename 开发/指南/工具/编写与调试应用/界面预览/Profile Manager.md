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

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/RBEafB9nQgiZfzyC382sTw/zh-cn_image_0000002571386802.png?HW-CC-KV=V1&HW-CC-Date=20260528T030627Z&HW-CC-Expire=86400&HW-CC-Sign=09A16D6E85044FB571BD5BB60B208F662BD09C3F778211A1FDC20E992021A4CB)

2. 在Profile Manager界面，单击**+ New Profile**按钮，添加设备。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/6ZyxGuZbQSWHkNwHjQ_CGw/zh-cn_image_0000002602065917.png?HW-CC-KV=V1&HW-CC-Date=20260528T030627Z&HW-CC-Expire=86400&HW-CC-Sign=8251523AC57C999DC17ED027B9D2BABE3F8AAACD73106C012BB6D9F54F5DF1A3)

3. 在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/pML_MqwNQBClMu4R8S7_yA/zh-cn_image_0000002571386800.png?HW-CC-KV=V1&HW-CC-Date=20260528T030627Z&HW-CC-Expire=86400&HW-CC-Sign=1BB2DBA99ABA5B12A97E92FB5F000F77DF57BCCC13CFFC4212306F40DCE0135F)

4. 设备信息填写完成后，单击**OK**完成创建。
