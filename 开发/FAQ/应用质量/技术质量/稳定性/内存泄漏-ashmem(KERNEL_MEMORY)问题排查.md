# 内存泄漏-ashmem(KERNEL_MEMORY)问题排查

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-73

## 内存泄漏-ashmem(KERNEL_MEMORY)问题排查
 


##### 问题现象

应用在使用过程中出现闪退，hilog日志中PROCESS_KILL的Reason为ResourceLeak:Ashmem Leak，memory_leak中生成memleak-kernel-[process_name]-0-sample和memleak-kernel-[process_name]-0-[timestamp]的内存泄漏日志文件。
 
 

##### 背景知识

- ashmem（匿名共享内存）泄漏是指调用了申请ashmem内存接口后，由于疏忽或错误未能及时释放，导致ashmem内存持续累积，对整机运行造成影响。
- ashmem泄漏的检测机制是通过内核监控整机ashmem内存是否超过阈值，当触发泄漏管控时，系统会对使用ashmem内存最多的应用进行终止。
- 应用被管控后，会在/data/log/memory_leak/目录生成两个故障日志文件以供分析：
memleak-native-[process_name]-[pid]-0-sample.txt：采样日志文件，用于观察内存增长趋势，确认泄漏情况。
- memleak-native-[process_name]-[pid]-0-[timestamp].txt：维测日志文件，记录了一些内存相关的统计信息，用于不同泄漏问题的维测。

 
 
- DevEco Profiler提供了基础的内存场景分析Allocation，可以使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化，参考文档[内存分析介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory)。

 
 

##### 问题定位

应用进程触发ashmem泄漏的管控后，系统会抓取泄漏相关的信息，在memory_leak目录生成两个故障日志文件以供分析。
 
**步骤一：分析采样日志memleak-native-[process_name]-[pid]-sample.txt。**
 
排查ashmem内存增长情况，是否超过了hardThreshold，或是超过softThreshold长时间未下降。
 
日志如下：
 
```text
memoryName:ashmem
softThreshold:2048(MB)	
##### 分析结论

应用存在ashmem泄漏，使用了PixelMap对象未释放。
 
 

##### 修改建议

程序需要正确管理分配的资源，使用完毕后需立刻释放。常见泄漏问题修复方法可见[资源泄漏类问题优化建议](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-leak-opt)和[资源泄漏类问题案例](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-scenario-stability-leak)。
