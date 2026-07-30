# OHAudio播放音频出现卡顿问题

更新时间：2026-07-09 10:22:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-68

#### 问题现象

OHAudio播放音频出现卡顿，如何定位？
 
 

#### 背景知识

- [OHAudio](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ohaudio-for-playback)是系统在API version 10中引入的一套C API，此API在设计上实现归一，同时支持普通音频通路和低时延通路。仅支持PCM格式，适用于依赖Native层实现音频输出功能的场景。
- [HiProfiler](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiprofiler)调优组件旨在为开发者提供一系列调优能力，可以用来帮助分析内存、性能等问题。

 
 

#### 问题定位

此类问题可通过抓取trace数据，分析问题出现时音频数据回调是否正常。
 1. 抓取trace数据。
先执行hdc shell进入命令行。
2. 粘贴如下Bash脚本执行，并同时复现问题，开始抓30秒trace数据。也可以参考[命令行说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiprofiler#命令行说明)，或使用[DevEco Studio](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-software-install)和[Smartperf](https://gitcode.com/openharmony/developtools_smartperf_host/releases)网页抓取。
3. 执行命令将trace文件保存到本地hdc file recv /data/local/tmp/hiprofiler_data.htrace ./hiprofiler_data.htrace。
4. 使用[DevEco Profiler调优工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler)或[Smartperf](https://gitcode.com/openharmony/developtools_smartperf_host/releases)网页中打开trace文件分析。
查看应用进程下的音频输出回调线程OS_AudioWriteCB，其中RendererInClientInner::OnWriteData是应用送数据给系统的回调处理函数，trace中发现此回调函数处理耗时都小于1ms，没有明显堵塞问题，运行正常。
5. 查看RendererInClientInClient线程，会打印应用送给系统的数据大小，发现有几次为0的数据，这不是正常现象。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/1WIAqJmeTtaKgPHaQvoWug/zh-cn_image_0000002664157965.png?HW-CC-KV=V1&HW-CC-Date=20260730T072626Z&HW-CC-Expire=86400&HW-CC-Sign=2C0BB55CF76076B92D3B1B64E7B7807AA7AAADEE2D60975F3E4BD3F0AD0685E5)

 
 

#### 分析结论

应用送给系统的音频数据中，有为0的静音数据，播放后会有卡顿现象。
 
 

#### 修改建议

应用侧需要排查[OH_AudioRenderer_OnWriteDataCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiorenderer_onwritedatacallback)回调函数中写入静音数据的问题。在无法填满回调所需长度数据的情况下，建议返回AUDIO_DATA_CALLBACK_RESULT_INVALID，系统不会处理该段音频数据。
