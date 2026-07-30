# 如何通过DevEco Testing将故障截图/录屏导出到电脑上

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-cast-5

#### 问题现象

如何通过DevEco Testing将故障截图/录屏导出到电脑上，便于后续问题提单、分析等操作。
 
 

#### 解决方案
1. 下载[DevEco Testing](https://developer.huawei.com/consumer/cn/download/deveco-testing)工具并完成安装。
2. 测试机打开开发者选项开关及USB调试开关：系统设置-关于本机，连续快速7次点击软件版本出现弹框，根据弹框提示确认重启并开启开发者模式，重启测试机后进入系统设置-系统，打开开发者选项开关和USB调试开关。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ccqm-LruSzyzalkLGjfO_g/zh-cn_image_0000002658923405.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=75BDAD352A3E814EC49AE261FCF63807059BA1D208E3A6BB59C305EA96F84277)

3. 通过数据线连接PC和测试机，打开DevEco Testing工具，点击页面左侧实用工具，选择设备投屏，点击开始投屏按钮（如果未检测到测试机，请检查步骤2中是否成功打开开发者选项开关和USB调试开关）。点击快捷工具中截屏按钮则直接截取当前测试机页面；点击屏幕录制按钮则进入录屏模式，可进行问题复现操作并在操作结束后点击结束录屏。截图/录屏保存路径见执行日志。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/2JQLIH1ySUCCkFQIukb4bw/zh-cn_image_0000002658803457.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=2E0DB8A23AFE034AD45E433E1F1E88A5F020FDA09CABACD8C14D9E0223449B96)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/b1u-IGFpSlCu9Jur2rXZvQ/zh-cn_image_0000002628404194.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=71879FB0AC5804F901DFF87F35830FA3B330D8586FAB5A0BF8F38FBE40D730D8)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/49g1HwYXQsGZSzt1Dnle2A/zh-cn_image_0000002628564098.png?HW-CC-KV=V1&HW-CC-Date=20260730T072728Z&HW-CC-Expire=86400&HW-CC-Sign=795CF4591F4FD78151FB8449151AEAC0E127700FD59FF2229EBDF1C7148BA6C6)
