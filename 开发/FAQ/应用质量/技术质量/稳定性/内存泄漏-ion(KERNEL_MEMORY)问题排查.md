# 内存泄漏-ion(KERNEL_MEMORY)问题排查

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-74

## 内存泄漏-ion(KERNEL_MEMORY)问题排查
 


##### 问题现象

应用在使用过程中出现闪退，hilog日志中PROCESS_KILL的Reason为ResourceLeak:ION Leak，memory_leak中生成memleak-kernel-[process_name]-0-sample和memleak-kernel-[process_name]-0-[timestamp]的内存泄漏日志文件。
 
 

##### 背景知识

- ION泄漏的检测机制同ashmem泄漏相似，通过内核监控整机ION内存，当触发泄漏管控时，系统会对使用ION内存最多的应用进行终止。
- 应用被管控后，会在/data/log/memory_leak/目录生成两个故障日志文件以供分析：
memleak-native-[process_name]-[pid]-0-sample.txt：采样日志文件，用于观察内存增长趋势，确认泄漏情况。
- memleak-native-[process_name]-[pid]-0-[timestamp].txt：维测日志文件，记录了一些内存相关的统计信息，用于不同泄漏问题的维测。

 
 
- DevEco Profiler提供了基础的内存场景分析Allocation，可以使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化，参考文档[内存分析介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory)。

 
 

##### 问题定位

应用进程触发ION泄漏的管控后，系统会抓取泄漏相关的信息，在memory_leak目录生成两个故障日志文件以供分析。
 
**步骤一：分析采样日志memleak-native-[process_name]-[pid]-sample.txt。**
 
排查ION内存增长情况，是否超过了hardThreshold，或是超过softThreshold长时间未下降。
 
日志如下：
 
```text
memoryName:ion
softThreshold:3000(MB)	视频软硬编解码器API接口使用不当。
- XComponent组件泄漏或者缓存过多。
- 使用Surface的NDK接口分配内存，没有释放。
- ArkWeb控件泄漏。
- Image控件泄漏或者缓存过多。

 
 
 

##### 分析结论

应用存在ION泄漏，存在使用后的资源未释放。
 
 

##### 修改建议

程序需要正确管理分配的资源，使用完毕后需立刻释放。常见泄漏问题修复方法可见[资源泄漏类问题优化建议](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-leak-opt)和[资源泄漏类问题案例](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-scenario-stability-leak)。
