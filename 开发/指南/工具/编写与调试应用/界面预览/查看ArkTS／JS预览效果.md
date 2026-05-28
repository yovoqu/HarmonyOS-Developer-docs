# 查看ArkTS/JS预览效果

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-arkts-js

预览器支持ArkTS/JS应用/元服务“实时预览”和“动态预览”。
 
> [!WARNING]
> 预览支持Phone、Tablet、2in1、Car、Wearable、TV设备的ArkTS工程，支持LiteWearable和Wearable设备的JS工程。 预览器功能依赖于电脑显卡的OpenGL版本，OpenGL版本要求为3.2及以上。 预览时将不会运行Ability生命周期。 从DevEco Studio 6.0.0 Beta3版本开始，HAP/HSP引用HSP时支持预览，HAR模块引用HSP不支持预览，请直接在HSP内预览或为该HSP 设置Mock实现 。 预览场景下，不支持通过相对路径及绝对路径的方式访问resources目录下的文件。 预览不支持组件拖拽。 部分API不支持预览，如Ability、App、MultiMedia等模块。 Richtext、Web、Video、 XComponent 组件不支持预览。 不支持调用C++库的预览。 HAR在被应用/元服务使用时真机效果有区别，真机上实际效果应用不显示menubar，元服务显示menubar，但预览器都以不显示menubar为准。若开发HAR模块，请注意被元服务使用时预览器效果与真机效果的不同。

 
- **实时预览**：在开发界面UI代码过程中，如果添加或删除了UI组件，您只需**Ctrl+S**进行保存，然后预览器就会立即刷新预览结果。如果修改了组件的属性，则预览器会实时（亚秒级）刷新预览结果，达到极速预览的效果（当前版本极速预览仅支持ArkTS组件。支持部分数据绑定场景，如@State装饰的变量）。实时预览默认开启，如果不需要实时预览，请单击预览器右上角
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/EO3VDRQZTO64B_Wmzbd1Iw/zh-cn_image_0000002571546628.png?HW-CC-KV=V1&HW-CC-Date=20260528T014957Z&HW-CC-Expire=86400&HW-CC-Sign=CB86FF9F5A8A894CEE6310A2A5D067C590653EC64FFABEC7BFCACF1CDE01DE4F)
按钮，关闭实时预览功能。
> [!NOTE]
> 开发者修改resources/base/profile目录下的配置文件（如main_pages.json/form_config.json），不支持触发实时预览，开发者需要点击重新加载 。


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/of_gk2p6SkGDyzfKby47Gg/zh-cn_image_0000002571386988.gif?HW-CC-KV=V1&HW-CC-Date=20260528T014957Z&HW-CC-Expire=86400&HW-CC-Sign=90A9BC9A84F455E1553382C5DCD5916C3216538801A8B6F39BC589D0D9B07733)

- **动态预览**：在预览器界面，可以在预览器中操作应用/元服务的界面交互动作，如单击、跳转、滑动等，与应用/元服务运行在真机设备上的界面交互体验一致。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/i_wpf_NlSYK9DX0X506_jw/zh-cn_image_0000002571546630.gif?HW-CC-KV=V1&HW-CC-Date=20260528T014957Z&HW-CC-Expire=86400&HW-CC-Sign=E2F9C8B38C08E17A5F4705A3F4912E16CCFE61B5FCE0AFD3B808646409279C93)


 
以ArkTS为例，使用预览器的方法如下：
 1. 创建或打开一个ArkTS应用/元服务工程。本示例以打开一个本地ArkTS Demo工程为例。
2. 在工程目录下，打开任意一个.ets文件（JS工程请打开.hml/.css/.js页面）。
3. 可以通过如下任意一种方式打开预览器，启动预览。

  
通过菜单栏，单击**View > Tool Windows > Previewer**打开预览器。
4. 在编辑窗口右上角的侧边工具栏，单击**Previewer**，打开预览器。
5. 点击按钮
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/K9KAB_FNSqmKmNCSiFDo3A/zh-cn_image_0000002602066109.png?HW-CC-KV=V1&HW-CC-Date=20260528T014957Z&HW-CC-Expire=86400&HW-CC-Sign=24758E26C06F7F64B1D325F8E4DCEDFC5A7D9530152F849D06135B09B2238067)
，停止预览。
