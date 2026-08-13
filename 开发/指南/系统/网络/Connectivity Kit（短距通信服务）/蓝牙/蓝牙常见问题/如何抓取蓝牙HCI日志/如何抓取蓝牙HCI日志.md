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
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/zUKnYDBmS8yQ-7QoMT-i1w/zh-cn_image_0000002674632994.png?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=4C6FF71DE57392E7FE4C3C09C6606578559ABE8DE42ED646AF1267A745E07F05)

 
  

#### 步骤二：连接蓝牙设备进行调试

开启手机蓝牙，连接需要调试的蓝牙外设，进行设备连接调试或问题复现操作。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/8V2p46XNRLOmIcjhMHDOlA/zh-cn_image_0000002704272947.png?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=9A24BB4F2E32B45879403A18CEF4F869B531C79E4AA0717B1919F5DBDEFE1143)

 
  

#### 步骤三：一键采集HCI日志

连接调试操作完毕后，下拉通知栏，点击**开发者模式**卡片，卡片下方会显示**收集**按钮，点击即可一键采集HCI日志。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/qvmMd6S6RMOGdSMcA_l6Ug/zh-cn_image_0000002674473150.png?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=6A7EE201168A5BEA7B04E1CCC976C20FF07E8FE96EF27221E005CDAE07310773)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/LfM_22SFQa6BO95WveQe5w/zh-cn_image_0000002704393117.png?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=7DA20B4FF4E8213D989C3C541CF861F3AA5C7C56DB90568E60A2DC91BDE70415)

 
> [!NOTE]
> 点击"收集"后，系统开始采集HCI日志，采集过程约30秒，请耐心等待。 下拉通知栏的 开发者模式卡片 可以被移除，移除后将无法抓取HCI日志。若卡片已被移除，需在保证 开发者模式开启 的情况下， 重启手机 ，卡片才可重新生效。请勿随意移除开发者模式卡片。

 
  

#### 步骤四：查看与导出HCI日志

采集完成后，进入手机文件管理，选择**我的手机**，点击**Documents**目录，即可找到日志压缩包
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/dMvqs1mdTiSgEo_LpIpSeg/zh-cn_image_0000002674632996.png?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=20A611CB15CFB486ECDA33B45B7FF11BD8AA7903E868F136EC11C4AA4B85AE1A)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/Zno0S5ATQR-9T8mJ4VSkkg/zh-cn_image_0000002704272949.png?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=C767E033703DE5D6BB137BC8B6BF087042BE6E826106DAF4F09F627D6E251F50)

 
通过**华为分享**、**三方应用**等方式，将日志压缩包分享到PC侧。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/z4tqplx7QXevqR6eZs7aKw/zh-cn_image_0000002674473152.png?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=FE7CDBBC9AB901FBD9EC915AC37FEB93D49FB39211580032BEBF9F2AC798B44E)

 
> [!NOTE]
> 抓取的HCI日志仅保存在手机本地，不自动上传，日志文件完全由手机用户管理。

 
  

#### 步骤五：在PC侧分析HCI日志

将日志压缩包从手机导出至PC后，使用蓝牙HCI日志分析工具（如Ellisys Bluetooth Analyzer、Wireshark等）打开日志文件进行分析。
