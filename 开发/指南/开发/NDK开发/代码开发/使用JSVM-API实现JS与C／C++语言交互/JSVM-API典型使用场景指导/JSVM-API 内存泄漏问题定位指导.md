# JSVM-API 内存泄漏问题定位指导

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-locate-memory-leak

JSVM的内存占用包括Native内存占用(C/C++侧的内存占用)和底层的JS引擎的堆内存占用，JS引擎会维护一个堆来管理其生成的JS对象，其生命周期由JS引擎维护，除此之外的内存我们归为Native内存。用户在使用JSVM时，可能碰到这两种内存异常增长的情况。

 本文先介绍如何定性分析，然后分两个部分介绍如何定位Native内存泄漏和JS引擎堆内存泄漏。


## 定性分析

可以通过hdc连接设备，执行如下命令行的方式对目标应用的内存进行采样，比较一段时间内的内存变化情况，从而定性分析是Native内存泄漏还是JS内存。下图中Pss Total列，native heap对应Native内存占用，AnonPage other对应js堆内存占用。
```text
hidumper --mem $(pidof dest_app)
```

 ![](assets/JSVM-API%20内存泄漏问题定位指导/file-20260514132730715-0.png)

## Native内存泄漏定位


## 典型场景

OH_JSVM_CreateReference 和 OH_JSVM_DeleteReference 接口没有成对调用，导致Reference没有被释放。
```text
JSVM_Value obj = nullptr;
OH_JSVM_CreateObject(env, &obj);
// 创建引用
JSVM_Ref reference;
OH_JSVM_CreateReference(env, obj, 1, &reference);

// 使用引用
JSVM_Value result;
OH_JSVM_GetReferenceValue(env, reference, &result);

// 未释放引用
// OH_JSVM_DeleteReference(env, reference);
```


## 定位步骤

为了分析Native内存泄漏，可以借助DevEco Studio的内存分析模块，具体参考文档：[内存分析及优化](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory)。 使用Profiler的Allocation模块记录一段时间内的Native内存信息。
![](assets/JSVM-API%20内存泄漏问题定位指导/file-20260514132730715-1.png)
比较这段时间内"Created & Existing"的内存变化情况，如果存在占比较大且Count较大的未释放内存，则怀疑存在内存泄漏，展开进一步查看调用栈。
![](assets/JSVM-API%20内存泄漏问题定位指导/file-20260514132730715-2.png)

## JS引擎堆内存泄漏定位


## 典型场景

全局变量滥用，导致DOM元素未释放。
```text
const elements = [];
function createElements() {
  for (let i = 0; i

## 定位步骤

JSVM目前提供了OH_JSVM_OpenInspector开启inspector，参考[使用OH_JSVM_OpenInspector](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-debugger-cpuprofiler-heapsnapshot#使用-oh_jsvm_openinspector),在此基础上可以[使用 Chrome inspect 页面进行调试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-debugger-cpuprofiler-heapsnapshot#使用-chrome-inspect-页面进行调试)。 通过使用DevTools工具，对目标场景内的堆内存进行快照（快照前先点击上方的垃圾回收按钮进行垃圾回收），利用快照对比功能，找到未释放的JS对象和其所在源码中的位置，进一步指导定位堆内存未释放的原因。 ![](assets/JSVM-API%20内存泄漏问题定位指导/file-20260514132730715-3.png)
