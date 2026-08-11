# 如何获取和查看DevEco Testing稳定性测试日志

更新时间：2026-07-07 09:58:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-stability-basic-quality-test-6

#### 问题现象

使用DevEco Testing进行稳定性测试，执行完成后如何获取和查看稳定性测试日志？
 
 

#### 解决方案

[稳定性基础质量测试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stability-testing#section1661194962815)日志存在于hilog和faultlog日志中，其中faultlog为Crash时的堆栈日志，hilog是这整个运行过程中的全量日志。
 1. 稳定性测试获取日志途径：
稳定性测试报告中检测异常项，详细日志点击查看，如图所示：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/D4juf8WUTZO0HOO5ZlqgcA/zh-cn_image_0000002632552628.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=C3F10F6A27597588B9307916662C5AB3AE691A8115FDE8E62DA68713210A5416)

2. 日志详情-定位日志，点击查看，跳转到对应日志，如图所示：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/O-s1dyryTOywaWongtliMQ/zh-cn_image_0000002663031767.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=1D8D4BC70E715334AB464B48339470D720AA38CF093F87465D2D66544D2FEF49)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/1LPhD7OeQnCKnHmCWHebtQ/zh-cn_image_0000002662871817.png?HW-CC-KV=V1&HW-CC-Date=20260811T005529Z&HW-CC-Expire=86400&HW-CC-Sign=D689F819D2CDDF58204C92CB383FA1C6785FFF4BAFC577D5C3D9889A6EF3DC25)

3. DevEco Testing稳定性测试，发生内存泄漏，如需获取profiler日志，需要执行测试前在“开发者选项”中打开“系统资源泄漏日志”开关（打开或关闭开关均需重启设备），参考[订阅资源泄漏事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events-arkts#步骤二订阅资源泄漏事件)。
4. 稳定性日志分析：稳定性分析将稳定性划分为地址越界、资源泄漏、应用冻屏（AppFreeze）和应用崩溃四大类。分析方法可参考文档[稳定性分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-analysis)。
