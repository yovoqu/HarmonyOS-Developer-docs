# 如何获取和查看DevEco Testing稳定性测试日志

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-stability-basic-quality-test-6

## 如何获取和查看DevEco Testing稳定性测试日志
 


##### 问题现象

使用DevEco Testing进行稳定性测试，执行完成后如何获取和查看稳定性测试日志？
 
 

##### 解决方案

[稳定性基础质量测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/specialized-testing#section9290138152218)日志存在于hilog和faultlog日志中，其中faultlog为Crash时的堆栈日志，hilog是这一个运行过程中的全量日志。
 
- 稳定性测试获取日志途径：
稳定性测试报告中检测异常项，详细日志点击查看，如图所示：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/uWuGQWSLT4e63nRxOlurFw/zh-cn_image_0000002658802747.png?HW-CC-KV=V1&HW-CC-Date=20260701T025927Z&HW-CC-Expire=86400&HW-CC-Sign=6E64221A30F2E927BC2BBAE97F77ED636172BC5B4FF39EF29565CEC0EE69F802)

- 日志详情-定位日志，点击查看，跳转到对应日志，如图所示：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/PT1L35xkSQeZXUB3r80o4Q/zh-cn_image_0000002628563374.png?HW-CC-KV=V1&HW-CC-Date=20260701T025927Z&HW-CC-Expire=86400&HW-CC-Sign=3F0C671157D747AB370D9C1E58C791A78E57C3E4681BD0356D62AD36875E9AB1)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/hV60qLZGSnihjdF1RVbwnA/zh-cn_image_0000002658922685.png?HW-CC-KV=V1&HW-CC-Date=20260701T025927Z&HW-CC-Expire=86400&HW-CC-Sign=C89FC269AD739A70467FE71B6DA2FD4C302EBBAE3C48FA6D4D99D27D731F6D2E)

- DevEco Testing稳定性测试，发生内存泄漏，如需获取profiler日志，需要执行测试前在“开发者选项”中打开“系统资源泄漏日志”开关（打开或关闭开关均需重启设备），参考[订阅资源泄漏事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events-arkts#步骤二订阅资源泄漏事件)。

 - 稳定性日志分析：稳定性分析将稳定性划分为地址越界、资源泄漏、应用冻屏（AppFreeze）和应用崩溃四大类。分析方法可参考文档[稳定性分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-analysis)。
