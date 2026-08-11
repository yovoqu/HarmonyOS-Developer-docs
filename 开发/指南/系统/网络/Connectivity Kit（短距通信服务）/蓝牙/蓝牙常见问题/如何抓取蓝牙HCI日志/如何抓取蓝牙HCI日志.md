# 如何抓取蓝牙HCI日志

更新时间：2026-08-03 11:34:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bluetooth-hci-log-capture

#### 简介

蓝牙/全场景开发者，可以通过开发者模式，一键采集蓝牙连接HCI日志，高效完成APP连接性能调试。该功能具有以下特点：
 
- 一键采集：操作简单，下拉通知栏点击开发者模式卡片，点击收集按钮即可完成HCI日志采集。
- 本地管理：抓取的HCI日志保存在文件管理可访问路径下，日志文件由手机用户管理。

 
> [!NOTE]
> 蓝牙HCI日志抓取功能面向开发者提供便捷高效的蓝牙HCI日志抓取能力。 开发者抓取蓝牙HCI日志功能从API版本26.0.0开始支持，目前支持Phone、Tablet。

 
  

#### 操作步骤

  

#### 步骤一：开启开发者模式

在调测手机上进入开发者模式，开启方法请参考 **[开启开发者选项](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-developer-mode#section530763213432)**。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/fuJBixbJRH-c06hUAjBcOQ/zh-cn_image_0000002668301402.png?HW-CC-KV=V1&HW-CC-Date=20260811T010211Z&HW-CC-Expire=86400&HW-CC-Sign=C88E8F77922462A8ACB904F3B7C32124F76E33A15CD3C8883694B502258FF709)

 
  

#### 步骤二：连接蓝牙设备进行调试

开启手机蓝牙，连接需要调试的蓝牙外设，进行设备连接调试或问题复现操作。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/BBbzmo8FTuGFQegxyJAHYQ/zh-cn_image_0000002668461280.png?HW-CC-KV=V1&HW-CC-Date=20260811T010211Z&HW-CC-Expire=86400&HW-CC-Sign=4307D83374E7F5E43F86197DEC621DE389785EAF813CB2F3E90CF4917619AA50)

 
  

#### 步骤三：一键采集HCI日志

连接调试操作完毕后，下拉通知栏，点击**开发者模式**卡片，卡片下方会显示**收集**按钮，点击即可一键采集HCI日志。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/6xn_YUZSTfGx8kUsYLtm2g/zh-cn_image_0000002698221159.png?HW-CC-KV=V1&HW-CC-Date=20260811T010211Z&HW-CC-Expire=86400&HW-CC-Sign=D1B405E1E86EBD61555289A36663277B3571EC4D8AADA534A8472B6DBC6FDD47)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/bQUf2y_STwi2zzP_eClNQg/zh-cn_image_0000002698141067.png?HW-CC-KV=V1&HW-CC-Date=20260811T010211Z&HW-CC-Expire=86400&HW-CC-Sign=FB490BA9B744C2FFB36F6E3C07FDF83AA1B971E506A23EDD99A8F87407D3F383)

 
> [!NOTE]
> 点击"收集"后，系统开始采集HCI日志，采集过程约30秒，请耐心等待。 下拉通知栏的 开发者模式卡片 可以被移除，移除后将无法抓取HCI日志。若卡片已被移除，需在保证 开发者模式开启 的情况下， 重启手机 ，卡片才可重新生效。请勿随意移除开发者模式卡片。

 
  

#### 步骤四：查看与导出HCI日志

采集完成后，进入手机文件管理，选择**我的手机**，点击**Documents**目录，即可找到日志压缩包
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/ck1O0wOYRQO8aI28LyRTtw/zh-cn_image_0000002668301404.png?HW-CC-KV=V1&HW-CC-Date=20260811T010211Z&HW-CC-Expire=86400&HW-CC-Sign=6753992FCE466E41B6F8883997F238D3FCE8A7F9FB7A7C2E378ED0D54054308A)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/YpCX6Y1oSfWS9vRprq5_xA/zh-cn_image_0000002668461282.png?HW-CC-KV=V1&HW-CC-Date=20260811T010211Z&HW-CC-Expire=86400&HW-CC-Sign=F0AC8D54423368DF5CEF9E83B0EFE63B1FDE62D1FB65D815D8116C3392EA7FEC)

 
通过**华为分享**、**三方应用**等方式，将日志压缩包分享到PC侧。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/I0MOJv4zTG29fhOryKsl7A/zh-cn_image_0000002698221161.png?HW-CC-KV=V1&HW-CC-Date=20260811T010211Z&HW-CC-Expire=86400&HW-CC-Sign=C2D7E3286C62B39E9A9F2FE1741A5549FDA4EC9277CD3B756D79CB2C7441B59D)

 
> [!NOTE]
> 抓取的HCI日志仅保存在手机本地，不自动上传，日志文件完全由手机用户管理。

 
  

#### 步骤五：在PC侧分析HCI日志

将日志压缩包从手机导出至PC后，使用蓝牙HCI日志分析工具（如Ellisys Bluetooth Analyzer、Wireshark等）打开日志文件进行分析。
