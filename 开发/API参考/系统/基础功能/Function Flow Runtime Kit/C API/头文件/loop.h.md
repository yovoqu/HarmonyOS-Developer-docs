# loop.h

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-loop-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明事件循环的C接口。
 
**引用文件：** <ffrt/loop.h>
 
**库：** libffrt.z.so
 
**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core
 
**起始版本：** 12
 
**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 结构体

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| ffrt_loop_t | loop句柄，用于标识不同的loop。 |
 
 
  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| FFRT_C_API ffrt_loop_t ffrt_loop_create(ffrt_queue_t queue) | 在指定的队列上创建loop，用于运行事件循环。 |
| FFRT_C_API int ffrt_loop_destroy(ffrt_loop_t loop) | 销毁loop。调用该接口可释放与loop关联的资源。 |
| FFRT_C_API int ffrt_loop_run(ffrt_loop_t loop) | 启动一次loop循环。该函数会独占调用线程，在当前调用线程中同步运行事件循环，直到调用ffrt_loop_stop后才会返回。 |
| FFRT_C_API void ffrt_loop_stop(ffrt_loop_t loop) | 停止loop循环。调用后，正在执行ffrt_loop_run的线程将停止循环并返回。 |
| FFRT_C_API int ffrt_loop_epoll_ctl(ffrt_loop_t loop, int op, int fd, uint32_t events, void *data, ffrt_poller_cb cb) | 在ffrt loop上控制epoll文件描述符。在目标文件描述符上添加、修改或删除监听的事件。 |
| FFRT_C_API ffrt_timer_t ffrt_loop_timer_start(ffrt_loop_t loop, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat) | 在ffrt loop上启动定时器。超时后调用回调函数；若repeat为true，则周期性重复触发。 |
| FFRT_C_API int ffrt_loop_timer_stop(ffrt_loop_t loop, ffrt_timer_t handle) | 在ffrt loop上停止定时器。调用后，该定时器不再触发。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### ffrt_loop_create()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API ffrt_loop_t ffrt_loop_create(ffrt_queue_t queue)
```
 
**描述**
 
在指定的队列上创建loop，用于运行事件循环。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_queue_t queue | 队列。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API ffrt_loop_t | loop创建成功时返回非空的loop句柄； 否则返回空指针。 |
 
 
  

#### ffrt_loop_destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_loop_destroy(ffrt_loop_t loop)
```
 
**描述**
 
销毁loop。调用该接口可释放与loop关联的资源。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_loop_t loop | loop句柄。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | loop销毁成功时返回0； 否则返回-1。 |
 
 
  

#### ffrt_loop_run()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_loop_run(ffrt_loop_t loop)
```
 
**描述**
 
启动一次loop循环。该函数会独占调用线程，在当前调用线程中同步运行事件循环，直到调用[ffrt_loop_stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-loop-h#ffrt_loop_stop)后才会返回。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_loop_t loop | loop句柄。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | loop运行成功时返回0； 否则返回-1。 |
 
 
**参考：**
 
[ffrt_loop_stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-loop-h#ffrt_loop_stop)
 
  

#### ffrt_loop_stop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API void ffrt_loop_stop(ffrt_loop_t loop)
```
 
**描述**
 
停止loop循环。调用后，正在执行[ffrt_loop_run](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-loop-h#ffrt_loop_run)的线程将停止循环并返回。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_loop_t loop | loop句柄。 |
 
 
**参考：**
 
[ffrt_loop_run](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-loop-h#ffrt_loop_run)
 
  

#### ffrt_loop_epoll_ctl()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_loop_epoll_ctl(ffrt_loop_t loop, int op, int fd, uint32_t events, void *data, ffrt_poller_cb cb)
```
 
**描述**
 
在ffrt loop上控制epoll文件描述符。在目标文件描述符上添加、修改或删除监听的事件。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_loop_t loop | loop句柄。 |
| int op | 在目标文件描述符上执行的操作类型，如添加、修改或删除。 |
| int fd | 执行操作的目标文件描述符。 |
| uint32_t events | 监听的事件类型（如可读、可写等），支持按位或组合。 |
| void *data | 传递给cb的用户数据。 |
| ffrt_poller_cb cb | 当目标fd被轮询到时执行的用户回调函数。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 操作成功时返回0； 否则返回-1。 |
 
 
  

#### ffrt_loop_timer_start()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API ffrt_timer_t ffrt_loop_timer_start(ffrt_loop_t loop, uint64_t timeout, void* data, ffrt_timer_cb cb, bool repeat)
```
 
**描述**
 
在ffrt loop上启动定时器。超时后调用回调函数；若repeat为true，则周期性重复触发。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_loop_t loop | loop句柄。 |
| uint64_t timeout | 超时时间，单位是毫秒，取值范围为[0, +∞)。 |
| void* data | 传递给cb的用户数据。 |
| ffrt_timer_cb cb | 超时后执行的用户回调函数。 |
| bool repeat | 是否重复执行该定时器。true表示重复，false表示只执行一次。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API ffrt_timer_t | 定时器句柄；若loop或cb为空则返回-1。 |
 
 
**参考：**
 
[ffrt_loop_timer_stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-loop-h#ffrt_loop_timer_stop)
 
  

#### ffrt_loop_timer_stop()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_loop_timer_stop(ffrt_loop_t loop, ffrt_timer_t handle)
```
 
**描述**
 
在ffrt loop上停止定时器。调用后，该定时器不再触发。
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_loop_t loop | loop句柄。 |
| ffrt_timer_t handle | 定时器句柄，由ffrt_loop_timer_start返回。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 操作成功时返回0； 否则返回-1。 |
 
 
**参考：**
 
[ffrt_loop_timer_start](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-loop-h#ffrt_loop_timer_start)
