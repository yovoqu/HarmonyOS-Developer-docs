# 如何解决DevEco Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-71

> [!NOTE]
> 注：此方法为临时规避方案，后续将修复该问题，建议仅在阻塞时使用。

 
用于减少编译HSP和闭源HAR包时生成声明文件的耗时。
 
修改 ets_checker.js 文件（文件路径：SDK路径\default\base\ets\build-tools\ets-loader\lib\ets_checker.js），编辑 processBuildHap 函数。
 1. 生成 sourceFile，在遍历文件时生成声明文件。
![](assets/如何解决DevEco%20Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题/file-20260515130126834-1.png)

2. 修改 getEmitOutput 函数，将其改为 getFileEmitOutput 函数，以获取声明文件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/moagKbMETG2aUvbjaMHacg/zh-cn_image_0000002194318168.png?HW-CC-KV=V1&HW-CC-Date=20260528T013219Z&HW-CC-Expire=86400&HW-CC-Sign=CD9388BC88B33BC9ADAF1AB67E78751CCCA7E4F2B9C646BB2B480FF561B3686F)
