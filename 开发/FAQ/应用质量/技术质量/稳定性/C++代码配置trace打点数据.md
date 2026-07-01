# C++代码配置trace打点数据

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-58

## C++代码配置trace打点数据
 


##### 问题现象

在C++项目开发过程中，如何配置trace打点数据？
 
 

##### 背景知识

开发者可以在代码中调用HiTraceMeter接口进行trace打点，然后使用[hitrace命令行工具](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace)获取程序运行时产生的打点信息，从而了解程序运行的进程、线程、时间戳、cpu等信息。以帮助开发者进行问题分析和性能调优等活动。HiTraceMeter提供ArkTS和C/C++两种接口，按需选择。
 
- [使用HiTraceMeter跟踪性能（ArkTS）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-guidelines-arkts)
- [使用HiTraceMeter跟踪性能（C/C++）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-guidelines-ndk)

 
 

##### 解决方案

OH_HiTrace_StartTrace用于标记一个同步跟踪耗时任务的开始。同步跟踪打点接口OH_HiTrace_StartTrace和OH_HiTrace_FinishTrace必须配对使用。
 
OH_HiTrace_StartAsyncTrace标记一个异步跟踪耗时任务的开始。用于在异步操作前调用进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。必须和OH_HiTrace_FinishAsyncTrace配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。
 
- OH_HiTrace_StartTrace和OH_HiTrace_FinishTrace配套使用，要用cpu insight才能看到trace信息。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/Kg3Uqm3dRK24EOI0SB3BLA/zh-cn_image_0000002628394994.png?HW-CC-KV=V1&HW-CC-Date=20260701T025509Z&HW-CC-Expire=86400&HW-CC-Sign=62B268007AE89E1024687052434CC1C101424C7B003E7E25E60871FA30392CEB)

- OH_HiTrace_StartAsyncTrace和OH_HiTrace_FinishAsyncTrace配套使用，time insight和cpu insight都可以看到trace信息。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/xwa4YvhLTRyEtzbb6BWQZA/zh-cn_image_0000002658914213.png?HW-CC-KV=V1&HW-CC-Date=20260701T025509Z&HW-CC-Expire=86400&HW-CC-Sign=E099123960ECC95C72665D39D5E1AAC02B072E90BDF534A3A0AD1E1BAD84C5BB)

- 如果是配合ArkTS/Native排查函数耗时，用OH_HiTrace_StartAsyncTrace和OH_HiTrace_FinishAsyncTrace进行打点，然后使用Profiler的Time Insight模板就可以看到。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/T_ufZNn1RsSxmeL5i5YkUA/zh-cn_image_0000002658794261.png?HW-CC-KV=V1&HW-CC-Date=20260701T025509Z&HW-CC-Expire=86400&HW-CC-Sign=9E60488117CF486BA4FF58215A5DFD29FECFD00EB2ED58E1E637FC1E635C6058)

- 运行hitrace打点，要在这里添加libhitrace_ndk.z.so。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Zp0slcZoTACzQMaOpBfuHg/zh-cn_image_0000002628554902.png?HW-CC-KV=V1&HW-CC-Date=20260701T025509Z&HW-CC-Expire=86400&HW-CC-Sign=27EB618707A50EE7DA2942696A5DA89FB535E3D62BAFF1A9779F72ABE9A43DA8)


 
 

##### 总结

[HiTraceMeter](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-guidelines-ndk)提供系统性能打点接口。开发者通过在关键代码位置调用HiTraceMeter接口提供的API接口，能够有效跟踪进程轨迹、查看系统性能。
 
HiTraceMeter通过应用程序的打点操作收集数据，这些数据通过内核sysfs文件接口进入内核的ftrace数据缓冲区。随后，使用hitrace命令行工具可以读取这些数据，并将其输出到设备侧的文件中。
 
通过使用HiTraceMeter，开发者可以获得有价值的性能数据，从而帮助他们优化应用的性能和响应速度。
