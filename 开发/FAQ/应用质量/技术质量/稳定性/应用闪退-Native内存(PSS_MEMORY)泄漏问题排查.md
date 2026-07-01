# 应用闪退-Native内存(PSS_MEMORY)泄漏问题排查

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-71

## 应用闪退-Native内存(PSS_MEMORY)泄漏问题排查
 


##### 问题现象

应用在使用过程中出现闪退，hilog日志中PROCESS_KILL的Reason为Pss Kill，memory_leak中生成memleak-native-[process_name]-[pid]的内存泄漏日志文件。
 
 

##### 背景知识

- 内存泄漏是指程序在申请分配内存后，由于疏忽或错误未能释放已经不再使用的内存空间，导致这部分内存无法被后续的程序使用。随着时间推移，未释放的内存会逐渐累积，最终可能导致系统性能下降甚至崩溃。
- native内存泄漏是一种资源泄漏类型，其检测机制为以应用进程平均动态峰值内存作为基线，当动态内存峰值超过基线值2倍时，判定泄漏，同时触发管控。
- 参考文档[日志获取](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-leak-guidelines#section166893320117)，native内存泄漏会生成三个故障日志文件以供分析：
memleak-native-[process_name]-[pid]-sample.txt：内存采样日志文件，用于观察内存增长趋势，确认泄漏情况。
- memleak-native-[process_name]-[pid]-smaps.txt：内存维测日志文件，记录了一些内存相关的统计信息，用于不同泄漏问题的维测。
- memleak-native-[process_name]-[pid]-[timestamp].txt：内存栈文件，检测到泄漏后抓取15min内的进程内存trace，用于分析内存分配时的调用栈。

 - [Smartperf_Host](https://gitcode.com/openharmony/developtools_smartperf_host/blob/master/smartperf_host/README_zh.md)：是一款深入挖掘数据、细粒度展示数据的性能功耗调优工具，可采集CPU调度、频点、进程线程时间片、堆内存、帧率等数据，采集的数据通过泳道图清晰地呈现给开发者，同时通过GUI以可视化的方式进行分析。工具当前为开发者提供了五个分析模板，分别是帧率分析、CPU/线程调度分析、应用启动分析、TaskPool分析、动效分析。

 
native泄漏问题速查表：
  
| 序号 | 泄漏类型 | 判断方法 | 解决方案 |
| --- | --- | --- | --- |
| 1 | 堆内存泄漏 | native_heap:jemalloc的PSS+SwapPSS > Summary的PSS*0.5 | 找到最大的内存块，解析调用栈，分析业务代码确认泄漏点 |
| 2 | ashmem泄漏 | dev/ashmem的PSS > Summary的PSS*0.5 | 找到最大Virtual_size的调用栈，分析业务代码确认泄漏点。 |
 
 
 

##### 问题定位

应用进程触发native泄漏的管控后，系统会抓取泄漏相关的信息，在memory_leak生成三个故障日志文件以供分析。
 
- **分析内存采样文件memleak-native-[process_name]-[pid]-sample.txt。**
日志规格如下：
 
```text
*************************************************************
*                    ***** READ ME *****                    *
*************************************************************
*    RSS: Resident Set Size                                 * // 两次jemalloc的申请情况（两次记录间隔5min），系统会根据两次NMD信息抓取内存栈。
// NMD：堆内存布局的快照
// Size：用户申请的内存经过对齐后的大小，jemalloc对齐size的分割是按照一个特定算法算的，8字节是最小单位，从第二个size开始，最小step是16，一个size到它的两倍size之间有4个分档。用户态传入的申请大小会向下对齐到离它最近的size中。
// Allocated：size申请的总内存。
******************************
LOGGER_MEMCHECK_SAMPLE_NMD_INFO 场景一：堆内存泄漏。
判定方法：native_heap:jemalloc的PSS+SwapPSS > Summary的PSS*0.5。
- 定位方法：
分析两次jemalloc的申请情况LOGGER_MEMCHECK_SAMPLE_NMD_INFO，观察allocated列和size列，找到申请总内存最大的size，可能存在泄漏点。
```text
LOGGER_MEMCHECK_SAMPLE_NMD_INFO
size       allocated         nmalloc         ndalloc
  8        79077136        10978034         1093392
// ...
128      1060568960         8563116          277421   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/phInqDe2QTS7lpE9fo2SjA/zh-cn_image_0000002628554906.png?HW-CC-KV=V1&HW-CC-Date=20260701T025511Z&HW-CC-Expire=86400&HW-CC-Sign=AC21569B8770D128112155CD076C3C25F7483C388F5FA40EBA819FA5D350AEEA)


 
 - 场景二：ashmem泄漏。
判定方法：dev/ashmem的PSS > Summary的PSS*0.5。
- 定位方法：
分析ashmem内存信息LOGGER_MEMCHECK_ASHMEM_INFO，筛选Process_name为泄漏应用的数据，排查Virtual_size列哪个内存块大小出现的次数最多，可能存在泄漏点。
```text
Process ashmem detail info: 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/PJaAQwJsSTOXILkVe44Dgw/zh-cn_image_0000002628395006.png?HW-CC-KV=V1&HW-CC-Date=20260701T025511Z&HW-CC-Expire=86400&HW-CC-Sign=8775B100405F76337E8280FE6F29995115FC95A250EE620CF43CD4F153A8196E)


 
 
 

- **结合业务代码分析泄漏点。**

排查方向：
堆内存泄漏：
基础对象泄漏：malloc/new等动态分配的内存，未释放。
- 循环引用：多个智能指针间相互持有，构成环状循环引用，导致智能指针计数未清零而泄漏。
- 生命周期管理不当：通过系统接口申请系统资源后未释放。
- 跨语言导致泄漏：ArkTS对象持有native对象导致native内存泄漏。
- 过量缓存：业务为了性能提升，通过缓存机制保留内存，但是由于缓存机制保护不合理导致泄漏。比如阈值设计不合理，出现代码流程错误导致超预期的数量和大小使用。
- 业务过载：业务请求方案需要申请内存发送请求，但是业务消费方由于代码流程错误，或负载等原因消费不及时，导致业务过载，内存超预期使用。

 - ashmeme内存泄漏：
如使用了Node-API在native层创建并使用decode()解码获取PixelMap，需排查申请未释放、把PixelMap缓存到应用生命周期的容器类中、引用计数多加等可能。
- 如使用了JS层的PixelMap，需排查JS对象泄漏或者缓存太多导致PixelMap大量占用，可使用DevEco Studio中的profiler工具抓取两次snapshot，分析对象的增量。
- pixmap使用的ashmem内存，应用可自定义绑定pixmap名字，当出现ashmem泄漏，快速根据ashmem块的名字锁定哪张图片存在问题，反推至对应的问题组件。JS层API：[setMemoryNameSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#setmemorynamesync13)，NATIVE层API：[OH_PixelmapNative_SetMemoryName()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_setmemoryname)。

 
 
 


 
 

##### 分析结论

- 堆内存泄漏：应用存在native内存泄漏，申请的堆内存不断增加，触发了系统管控导致闪退。
- ashmeme内存泄漏：应用存在ashmem泄漏，使用了PixelMap对象未释放。

 
 

##### 修改建议

程序需要正确管理分配的资源，使用完毕后需立刻释放。常见泄漏问题修复方法可见[资源泄漏类问题优化建议](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-leak-opt)和[资源泄漏类问题案例](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-scenario-stability-leak)。
