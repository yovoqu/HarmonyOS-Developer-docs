# HarmonyOS PC应用接入状态栏如何实现鼠标悬停弹出气泡提示？

更新时间：2026-07-30 01:55:38

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-desktop-extension-1

#### 问题现象


![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/WdFzQTbwR9evjM5HZmYzEQ/zh-cn_image_0000002628615110.png?HW-CC-KV=V1&HW-CC-Date=20260730T072607Z&HW-CC-Expire=86400&HW-CC-Sign=633E48192FC34BF860C06143897AC162D71B850A7E4D7BADC38D3BE9392F18C7)

 
HarmonyOS PC应用接入状态栏后应该如何配置才能实现在鼠标悬停时弹出气泡提示？
 
 

#### 背景知识

- [Desktop Extension Kit（桌面拓展服务）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/status-bar-extension-api)：提供系统级统一的操作入口，支持应用快捷功能接入桌面，注意该模块提供的接口能力只支持中国境内（不包含中国香港、中国澳门、中国台湾），仅在PC/2in1设备上生效。
- [statusBarManager.QuickOperation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager#statusbarmanageraddtostatusbar)：用于构建左键业务弹窗信息。

 
 

#### 解决方案
1. 参考应用接入状态栏[开发步骤](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/statusbar-extension-guide#开发步骤)，先调用[statusBarManager.QuickOperation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager#statusbarmanageraddtostatusbar)构建左键业务弹窗信息，以下为关键代码：
```text
<em>// 构建点击状态栏图标时弹出的快捷操作窗口</em>
let operation: statusBarManager.QuickOperation = {
  abilityName: 'MyStatusBarViewAbility',
  title: 'Test Demo',
  height: 300,
  moduleName: 'entry'
};
```
 完整接入示例可参考官方教程：[接入状态栏开发](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_StatusBarExtensionKit)。
2. 将上述[statusBarManager.QuickOperation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager#statusbarmanageraddtostatusbar)的moduleName参数设置为所在模块对应module.json5中module-name字段。要实现鼠标悬停于状态栏时弹出气泡提示，则当前moduleName不可缺省，若未配置moduleName参数，该参数默认为''，则鼠标悬停时不会显示气泡提示，如下图：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/hQ55kTxaS8GOycRlumQsyw/zh-cn_image_0000002628775006.png?HW-CC-KV=V1&HW-CC-Date=20260730T072607Z&HW-CC-Expire=86400&HW-CC-Sign=A9567A160C36AB30195C7B8E86A0DBCB3EB450DC86477810A9C15410E861103A)

3. 设置状态栏悬停气泡展示内容：需在接入状态栏提供的模块名对应/moduleName/src/main目录下的module.json5文件中，找到对应的abilities-label字段，修改该关键字对应的value值。注意：状态栏label和应用窗口对应的名称是相同字段
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/oiF5JVgBRa2LR8oPfIm3gw/zh-cn_image_0000002658974319.png?HW-CC-KV=V1&HW-CC-Date=20260730T072607Z&HW-CC-Expire=86400&HW-CC-Sign=24C6128C96462C1AB5D1FD52CE48A21D32199346251687470600A53707A17E05)

 
 

#### 常见FAQ

Q：PC端应用的系统托盘图标，是否支持根据鼠标左键或右键点击，分别弹出不同的快捷菜单？
 
A：系统托盘图标能够识别左键操作：[statusBarManager.QuickOperation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager#statusbarmanageraddtostatusbar)，但暂不支持快捷菜单的控制。支持右键操作：[statusBarManager.StatusBarGroupMenu](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-manager#statusbarmanageraddtostatusbar)，弹出快捷菜单。
