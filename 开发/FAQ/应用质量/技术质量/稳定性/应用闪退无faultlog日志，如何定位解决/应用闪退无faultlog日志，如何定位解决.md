# 应用闪退无faultlog日志，如何定位解决

更新时间：2026-07-24 01:16:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-77

#### 问题现象

应用在使用过程中出现闪退现象，但faultlogger中无应用故障日志，如何定位解决。
 
 

#### 解决方案
1. 使用hdc file recv /data/log/hilog获取hilog和hilog_kmsg日志，hilog日志无法直接解压查看，需要使用hilogtool解析，可以参考[常用解析命令示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog-tool#常用解析命令示例)，hilog_kmsg日志可以直接解压查看。
2. 在hilog日志中以正则表达式搜索Kill Reason|exit with，查看是否有相关日志。
 
- 存在processName=com.hx.example ... Kill Reason:日志，表示应用进程被系统终止，Kill Reason表示终止原因，可能的情况如下表所示。

| 日志 | 含义 | 解决方法 |
| --- | --- | --- |
| Kill Reason:ILLEGAL_AUDIO_RENDERER_BY_SUSPEND | 未申请音频播放后台长时任务，但是在后台时有大量音频播放 | 方法一：申请长时任务 。 方法二：应用退到后台时，停止音频播放，参考音频资源合理使用。 |
| Kill Reason:ILLEGAL_AUDIO_CAPTURER_BY_SUSPEND | 未申请合理的后台任务，但是在后台时有录音 | 方法一：申请长时任务 。 方法二：应用退到后台时，停止录音，参考音频资源合理使用。 |
| Kill Reason:ResourceLeak:Gpu_rs Leak | 应用在Render Service进程内的GPU内存占用超标 | 排查是否使用高分辨率图片，是否使用autoResize对Image组件进行降采样减少内存占用，使用createPixelMap或createPixelMapUsingAllocator接口时是否在DecodingOptions（解码参数）中设置desiredSize进行下采样解码。 |
| Kill Reason:ResourceLeak:Thread Leak | 应用进程的总线程数超标 | 参考线程泄漏问题定位。 |
| Kill Reason:ResourceLeak:Fd Leak | 应用进程fd句柄总数超标 | 参考句柄泄漏分析方法。 |
| Kill Reason:ResourceLeak:Ion Leak | 应用占用的ION内存超标 | 参考ION泄漏。 |
- 存在com.hx.example with pid xxx exit with signal:9日志，表示系统向应用发送SIGKILL信号来终止应用进程。在该情况下可以在hilog_kmsg日志搜索rss_threshold monitor|cpa prepare memory。

| 日志 | 含义 | 定位方法 |
| --- | --- | --- |
| rss_threshold monitor Kill Pid 应用进程号 [包名] adj 0 totalRss ZZZ K out of range YYY K, rss AAA K, swapRss BBB K | 应用Rss内存超过阈值（YYY KB），被系统终止 | 方法一：参考ArkTS内存泄漏分析或Native内存泄漏分析。 方法二：查看/data/log/reliability/resource_leak/目录下是否有应用资源泄漏故障日志，日志规格可以参考[Resource Leak（资源泄漏）检测]，问题分析可以参考资源泄漏类问题分析方法。 |
| cpa prepare memory, start to kill process（pid: 进程Pid） | DRM(Digital Right Management)业务申请内存但是内存不足时，会按照一定策略终止进程以回收内存 | 尝试降低应用自身的内存占用，以减少被整机终止进程策略选中的概率。 如果被终止的进程为ArkWeb渲染，可以参考应用如何避免Web组件渲染子进程异常退出导致的页面卡死问题修复。 |
