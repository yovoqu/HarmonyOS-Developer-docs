# 如何通过DevEco Testing将故障截图/录屏导出到电脑上

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-cast-5

#### 问题现象

如何通过DevEco Testing将故障截图/录屏导出到电脑上，便于后续问题提单、分析等操作。
 
 

#### 解决方案
1. 下载[DevEco Testing](https://developer.huawei.com/consumer/cn/download/deveco-testing)工具并完成安装。
2. 测试机打开开发者选项开关及USB调试开关：系统设置-关于本机，连续快速7次点击软件版本出现弹框，根据弹框提示确认重启并开启开发者模式，重启测试机后进入系统设置-系统，打开开发者选项开关和USB调试开关。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ccqm-LruSzyzalkLGjfO_g/zh-cn_image_0000002658923405.png?HW-CC-KV=V1&HW-CC-Date=20260723T014027Z&HW-CC-Expire=86400&HW-CC-Sign=CB16A21A9D05F817D59ED261A199F1B10856104689865FF0C9B2330D5F1322CA)

3. 通过数据线连接PC和测试机，打开DevEco Testing工具，点击页面左侧实用工具，选择设备投屏，点击开始投屏按钮（如果未检测到测试机，请检查步骤2中是否成功打开开发者选项开关和USB调试开关）。点击快捷工具中截屏按钮则直接截取当前测试机页面；点击屏幕录制按钮则进入录屏模式，可进行问题复现操作并在操作结束后点击结束录屏。截图/录屏保存路径见执行日志。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/2JQLIH1ySUCCkFQIukb4bw/zh-cn_image_0000002658803457.png?HW-CC-KV=V1&HW-CC-Date=20260723T014027Z&HW-CC-Expire=86400&HW-CC-Sign=820249C96649664524931FCE5E3AB75554FD65495BEF83D8AD55C496787E879F)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/b1u-IGFpSlCu9Jur2rXZvQ/zh-cn_image_0000002628404194.png?HW-CC-KV=V1&HW-CC-Date=20260723T014027Z&HW-CC-Expire=86400&HW-CC-Sign=2DA512C05B634E2558A68CA2756B299AE70D5C1603F16B236793F52C5DEE05D7)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/49g1HwYXQsGZSzt1Dnle2A/zh-cn_image_0000002628564098.png?HW-CC-KV=V1&HW-CC-Date=20260723T014027Z&HW-CC-Expire=86400&HW-CC-Sign=868525C01DECBA1D60681458336F52E0B63DCC4B56A7827316E1F873B272B285)
