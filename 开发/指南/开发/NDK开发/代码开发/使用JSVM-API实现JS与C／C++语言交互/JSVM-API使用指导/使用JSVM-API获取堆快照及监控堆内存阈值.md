# 使用JSVM-API获取堆快照及监控堆内存阈值

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-threshold-callback

## 使用JSVM-API获取堆快照及监控堆内存阈值
 
 

##### 简介

从API版本26.0.0开始，JSVM-API提供了堆内存管理相关的核心能力，包含**获取原始堆快照**和**监控堆内存阈值**两类关键接口：
 
- OH_JSVM_TakeRawHeapSnapshot：获取当前JS虚拟机（VM）的原始堆快照（二进制格式）并输出到指定流，可用于堆内存分析、内存泄漏定位、调试等场景。
- OH_JSVM_SetHeapThresholdCallback：为VM注册堆内存阈值回调函数，当堆内存使用量达到指定阈值时自动触发回调。
- OH_JSVM_ClearHeapThresholdCallback：移除已注册的堆内存阈值回调函数，释放相关资源。

 
开发者可通过这些接口实现堆内存的全生命周期监控、快照采集与分析，辅助优化内存使用效率、排查内存相关问题。
 
  

##### 基本概念

  

##### [h2]原始堆快照（Raw Heap Snapshot）

JSVM-API提供了OH_JSVM_TakeRawHeapSnapshot接口，来获取VM的原始堆快照。原始堆快照以JSVM专属的二进制格式存储堆内存的完整状态，其格式是与具体VM实现绑定的，数据布局在不同版本之间不保证稳定。获取堆快照的操作可能短暂地暂停应用运行，频繁调用会生成大量快照文件，需开发者合理管控磁盘占用。
 
此外，快照数据通过自定义的流回调获取时，会在VM运行的线程上**同步调用**，因此回调函数需避免长时间阻塞操作；若回调返回false，输出流将会被中止，快照生成流程也会立即终止。
 
  

##### [h2]堆内存阈值回调

JSVM-API提供了OH_JSVM_SetHeapThresholdCallback接口，为指定的VM注册一个堆内存阈值回调函数。一个VM同一时间仅能注册**一个**堆内存阈值回调，回调通过“阈值（字节数）+回调函数+用户自定义数据”的组合唯一标识，当不再需要该回调时，必须调用OH_JSVM_ClearHeapThresholdCallback进行注销。
 
该类接口不保证线程安全，必须在VM运行的线程上调用。当堆内存使用量达到指定阈值时，回调函数会被触发，并在同一线程上被同步调用，且回调执行期间会跳过堆阈值检查。
 
  

##### [h2]接口说明
 
| 接口 | 功能说明 |
| --- | --- |
| OH_JSVM_TakeRawHeapSnapshot | 获取VM的原始堆快照，并通过流回调输出二进制数据。 |
| OH_JSVM_SetHeapThresholdCallback | 为VM注册堆内存阈值回调，达到阈值时触发自定义逻辑。 |
| OH_JSVM_ClearHeapThresholdCallback | 移除VM中已注册的堆内存阈值回调函数。 |
 
 
  

##### 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-process)，本文仅对接口对应C++相关代码进行展示。
 
  

##### [h2]具体函数使用示例代码

包括OH_JSVM_TakeRawHeapSnapshot、OH_JSVM_SetHeapThresholdCallback、OH_JSVM_ClearHeapThresholdCallback三个函数的使用示例，涵盖堆快照采集、堆阈值回调注册/移除、边界场景（重复注册/移除、无效参数）等核心场景。
 
**cpp部分代码**
 
```text
#include 
#include 
#include 
#include 
#include 
#include 
#include "napi/native_api.h"
#include "hilog/log.h"
#include "ark_runtime/jsvm.h"

#define LOG_DOMAIN 0x3200
#define LOG_TAG "APP"

static int g_aa = 0;

static bool g_heapThresholdCalled = false;
static uint64_t g_triggeredThreshold = 0;
static void* g_callbackUserData = nullptr;
static bool g_snapshotGenerated = false;

static constexpr int SLEEP_TIME_MS = 100;
static constexpr uint64_t THRESHOLD_SIZE = 1024 * 1024;
static constexpr int TEST_DATA_VALUE = 0x12345678;

bool SnapshotStreamCallback(const char* data, int size, void* streamData)
{
    std::FILE* file = reinterpret_cast(streamData);
    if (file) {
        size_t written = std::fwrite(data, 1, size, file);
        return written == static_cast(size);
    }
    return true;
}

void OnHeapThresholdReached(JSVM_VM vm, uint64_t threshold, void* data)
{
    OH_LOG_INFO(LOG_APP, "== Heap threshold reached ==");
    OH_LOG_INFO(LOG_APP, "Threshold: %{public}lu bytes", threshold);
    OH_LOG_INFO(LOG_APP, "User data: %{public}d", *static_cast(data));

    g_heapThresholdCalled = true;
    g_triggeredThreshold = threshold;
    g_callbackUserData = data;

    if (!g_snapshotGenerated) {
        g_snapshotGenerated = true;
        pid_t pid = fork();
        if (pid 
##### 注意事项

- OH_JSVM_TakeRawHeapSnapshot
vm/stream参数为NULL时，返回JSVM_INVALID_ARG；其他场景均返回JSVM_OK；
- 快照流回调需避免长时间阻塞，否则会阻塞VM线程；
- 频繁调用会产生大量二进制文件，建议按需采集并及时清理。

 - OH_JSVM_SetHeapThresholdCallback
阈值需满足：0 < threshold ≤ heapSizeLimit（heapSizeLimit来自JSVM_HeapStatistics），否则返回JSVM_INVALID_ARG；
- vm或callback参数为NULL时，返回JSVM_INVALID_ARG；
- VM已注册回调时重复注册，返回JSVM_INVALID_ARG；
- 接口非线程安全，**必须**在VM运行的线程调用；
- 阈值检查在GC期间进行，回调在同一线程同步调用；回调执行期间会跳过阈值检查，避免递归触发；回调返回后若堆使用量仍≥阈值，下次GC会再次触发，无需重新注册。

 - OH_JSVM_ClearHeapThresholdCallback
vm/callback参数为NULL时，或（阈值+回调+用户数据）与已注册信息不匹配时，返回JSVM_INVALID_ARG；
- 接口非线程安全，**必须**在VM运行的线程调用；
- 回调执行期间可移除自身，并重新注册新的阈值回调（需保证参数合法）。
