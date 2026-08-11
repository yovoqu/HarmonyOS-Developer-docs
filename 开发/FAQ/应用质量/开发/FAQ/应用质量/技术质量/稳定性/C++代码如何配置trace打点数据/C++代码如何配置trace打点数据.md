# C++代码如何配置trace打点数据

更新时间：2026-07-24 01:16:00

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-58

#### 问题现象

在C/C++项目开发过程中，如何配置trace打点数据？具体包括如何使用同步跟踪打点接口和异步跟踪打点接口标记耗时任务，以及如何通过hitrace命令行工具或Profiler工具查看打点信息。
 
 

#### 背景知识

开发者可以在代码中调用HiTraceMeter接口进行trace打点，然后使用[hitrace命令行工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace)获取程序运行时产生的打点信息，从而了解程序运行的进程、线程、时间戳、cpu等信息，以帮助开发者进行问题分析和性能调优等活动。
 
HiTraceMeter提供ArkTS和C/C++两种接口，开发者可根据实际开发语言选择合适的接口。
 
- [使用HiTraceMeter跟踪性能（ArkTS）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-guidelines-arkts)
- [使用HiTraceMeter跟踪性能（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-guidelines-ndk)

 
 

#### 解决方案

OH_HiTrace_StartTraceEx用于标记一个同步跟踪耗时任务的开始。同步跟踪打点接口OH_HiTrace_StartTraceEx和OH_HiTrace_FinishTraceEx必须配对使用。
 
OH_HiTrace_StartAsyncTraceEx标记一个异步跟踪耗时任务的开始。用于在异步操作前调用进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。必须和OH_HiTrace_FinishAsyncTraceEx配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。
 
- OH_HiTrace_StartTraceEx和OH_HiTrace_FinishTraceEx配套使用，要用cpu insight才能看到trace信息。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/NTx7vmLAT4iCwDFQ9EFq1A/zh-cn_image_0000002677871739.png?HW-CC-KV=V1&HW-CC-Date=20260811T005906Z&HW-CC-Expire=86400&HW-CC-Sign=624E251F193DBB53ED72305F28BFAAE2012F2A194FFA74FA43BA18AEFA9EB55C)

- OH_HiTrace_StartAsyncTraceEx和OH_HiTrace_FinishAsyncTraceEx配套使用，Time insight和cpu insight都可以看到trace信息。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/4bC_gXSwSuq5nNT77pHCIg/zh-cn_image_0000002677872197.png?HW-CC-KV=V1&HW-CC-Date=20260811T005906Z&HW-CC-Expire=86400&HW-CC-Sign=BC39EB8A1EEBB96B64D7C973630D4D32F7AABB159C9FF5DF12F8A4489F4B3BD5)

- 如果是配合ArkTS/HarmonyOS排查函数耗时，用OH_HiTrace_StartAsyncTraceEx和OH_HiTrace_FinishAsyncTraceEx进行打点，然后使用Profiler的Time insight模板就可以看到。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/BMotM155TVCld1vKGc_ZVw/zh-cn_image_0000002647792546.png?HW-CC-KV=V1&HW-CC-Date=20260811T005906Z&HW-CC-Expire=86400&HW-CC-Sign=E6900F67A538A92F2329E3B0E2BD999AD90DCC35EA1019F6325604A4E5ADAFBE)

- 运行hitrace打点，要在这里添加libhitrace_ndk.z.so。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/R-5SXBzlT2yFRA7HTPss_g/zh-cn_image_0000002647792624.png?HW-CC-KV=V1&HW-CC-Date=20260811T005906Z&HW-CC-Expire=86400&HW-CC-Sign=41F7DEDFE2651F8D716F4BDD89D2A8C07F94A6BCCD6E189F4A08CB954B3E58C0)


 
 

#### 常见FAQ

Q：通过OH_HiTrace_StartAsyncTraceEx、OH_HiTrace_FinishAsyncTraceEx等接口打点后，在Time Profile中看不到User trace信息怎么办？
 
A：建议通过IDE中抓取Time/CPU的Profiler trace信息来显示打点信息。若仍无法看到，请升级IDE版本到26.0.0 beta1版本后再尝试。
