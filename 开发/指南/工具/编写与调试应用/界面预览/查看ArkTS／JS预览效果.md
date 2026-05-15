# 查看ArkTS/JS预览效果

更新时间：2026-04-20 06:32:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-arkts-js

预览器支持ArkTS/JS应用/元服务“实时预览”和“动态预览”。


> [!NOTE]
> 预览支持Phone、Tablet、2in1、Car、Wearable、TV设备的ArkTS工程，支持LiteWearable和Wearable设备的JS工程。预览器功能依赖于电脑显卡的OpenGL版本，OpenGL版本要求为3.2及以上。预览时将不会运行Ability生命周期。从DevEco Studio 6.0.0 Beta3版本开始，HAP/HSP引用HSP时支持预览，HAR模块引用HSP不支持预览，请直接在HSP内预览或为该HSP设置Mock实现。预览场景下，不支持通过相对路径及绝对路径的方式访问resources目录下的文件。预览不支持组件拖拽。部分API不支持预览，如Ability、App、MultiMedia等模块。Richtext、Web、Video、XComponent组件不支持预览。不支持调用C++库的预览。HAR在被应用/元服务使用时真机效果有区别，真机上实际效果应用不显示menubar，元服务显示menubar，但预览器都以不显示menubar为准。若开发HAR模块，请注意被元服务使用时预览器效果与真机效果的不同。


 以ArkTS为例，使用预览器的方法如下：


1. 创建或打开一个ArkTS应用/元服务工程。本示例以打开一个本地ArkTS Demo工程为例。
2. 在工程目录下，打开任意一个.ets文件（JS工程请打开.hml/.css/.js页面）。
3. 点击按钮
![](assets/查看ArkTS／JS预览效果/file-20260514132934068-0.png)
，停止预览。
