# 如何通过DevEco Testing将故障截图/录屏导出到电脑上

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-cast-5

## 如何通过DevEco Testing将故障截图/录屏导出到电脑上
 


##### 问题现象

如何通过DevEco Testing将故障截图/录屏导出到电脑上，便于后续问题提单、分析等操作。
 
 

##### 解决方案

- 下载[DevEco Testing](https://developer.huawei.com/consumer/cn/download/deveco-testing)工具并完成安装。
- 测试机打开开发者选项开关及USB调试开关：系统设置-关于本机，连续快速7次点击软件版本出现弹框，根据弹框提示确认重启并开启开发者模式，重启测试机后进入系统设置-系统，打开开发者选项开关和USB调试开关。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/ccqm-LruSzyzalkLGjfO_g/zh-cn_image_0000002658923405.png?HW-CC-KV=V1&HW-CC-Date=20260701T025928Z&HW-CC-Expire=86400&HW-CC-Sign=28A7A5D8D58D4642BEEC36436E40D5E20392175270ADD16E80A7B2C7333CBAF7)

- 通过数据线连接PC和测试机，打开DevEco Testing工具，点击页面左侧实用工具，选择设备投屏，点击开始投屏按钮（如果未检测到测试机，请检查步骤2中是否成功打开开发者选项开关和USB调试开关）。点击快捷工具中截屏按钮则直接截取当前测试机页面；点击屏幕录制按钮则进入录屏模式，可进行问题复现操作并在操作结束后点击结束录屏。截图/录屏保存路径见执行日志。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/2JQLIH1ySUCCkFQIukb4bw/zh-cn_image_0000002658803457.png?HW-CC-KV=V1&HW-CC-Date=20260701T025928Z&HW-CC-Expire=86400&HW-CC-Sign=3E6F42108675F58F7D774DB2EFC97D95DEC3208FAC9E71A5AB3DBA008C4B394C)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/b1u-IGFpSlCu9Jur2rXZvQ/zh-cn_image_0000002628404194.png?HW-CC-KV=V1&HW-CC-Date=20260701T025928Z&HW-CC-Expire=86400&HW-CC-Sign=20750DAF603C02B5AAD4908BBADBD8A9965F68F88F816E0377FD12D3C546956F)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/49g1HwYXQsGZSzt1Dnle2A/zh-cn_image_0000002628564098.png?HW-CC-KV=V1&HW-CC-Date=20260701T025928Z&HW-CC-Expire=86400&HW-CC-Sign=4ACF2227E8261A4B7E084CA87CD6EA9943A74A11BAC15F73D68CB3F56C1D1EC9)
