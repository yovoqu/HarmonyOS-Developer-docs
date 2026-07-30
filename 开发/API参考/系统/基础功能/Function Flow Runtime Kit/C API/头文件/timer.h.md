# timer.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timer-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明定时器的C接口。提供基于QoS等级的定时器能力，支持在指定超时时间后执行回调函数，可用于延时任务调度等场景。
 
**引用文件：** <ffrt/timer.h>
 
**库：** libffrt.z.so
 
**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core
 
**起始版本：** 12
 
**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| FFRT_C_API ffrt_timer_t ffrt_timer_start(ffrt_qos_t qos, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat) | 在FFRT工作线程上启动定时器。避免在cb中调用exit或ffrt_timer_stop，以防止未定义行为或死锁。 |
| FFRT_C_API int ffrt_timer_stop(ffrt_qos_t qos, ffrt_timer_t handle) | 停止FFRT工作线程上的定时器。该接口为阻塞接口。请避免在回调函数内调用该接口，以防止死锁或同步问题。当handle对应的回调正在执行时，该函数会等待回调完成后再返回。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### ffrt_timer_start()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API ffrt_timer_t ffrt_timer_start(ffrt_qos_t qos, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat)
```
 
**描述**
 
在FFRT工作线程上启动定时器。避免在cb中调用exit或[ffrt_timer_stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timer-h#ffrt_timer_stop)，以防止未定义行为或死锁。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_qos_t qos | 运行定时器的工作线程的QoS等级。 |
| uint64_t timeout | 超时时间，单位是毫秒。 |
| void* data | 传递给cb的用户数据。 |
| ffrt_timer_cb cb | 超时后执行的用户回调函数。 |
| bool repeat | 是否重复执行该定时器。true表示重复，false表示只执行一次。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API ffrt_timer_t | 定时器句柄；若回调函数为空指针或QoS映射未注册则返回-1。 |
 
 
**参考：**
 
[ffrt_timer_stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timer-h#ffrt_timer_stop)
 
  

#### ffrt_timer_stop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_timer_stop(ffrt_qos_t qos, ffrt_timer_t handle)
```
 
**描述**
 
停止FFRT工作线程上的定时器。该接口为阻塞接口。请避免在回调函数内调用该接口，以防止死锁或同步问题。当handle对应的回调正在执行时，该函数会等待回调完成后再返回。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_qos_t qos | 运行定时器的工作线程的QoS等级。必须与ffrt_timer_start中使用的QoS等级一致。 |
| ffrt_timer_t handle | 目标定时器句柄，由ffrt_timer_start返回。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 操作成功时返回0； 否则返回-1。 |
 
 
**参考：**
 
[ffrt_timer_start](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timer-h#ffrt_timer_start)
