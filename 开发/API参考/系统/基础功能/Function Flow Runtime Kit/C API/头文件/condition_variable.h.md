# condition_variable.h

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-condition-variable-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

声明条件变量的C接口。
 
**引用文件：** <ffrt/condition_variable.h>
 
**库：** libffrt.z.so
 
**系统能力：** SystemCapability.Resourceschedule.Ffrt.Core
 
**起始版本：** 10
 
**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| FFRT_C_API int ffrt_cond_init(ffrt_cond_t* cond, const ffrt_condattr_t* attr) | 初始化条件变量。 |
| FFRT_C_API int ffrt_cond_signal(ffrt_cond_t* cond) | 唤醒阻塞在条件变量上的一个任务。 |
| FFRT_C_API int ffrt_cond_broadcast(ffrt_cond_t* cond) | 唤醒阻塞在条件变量上的所有任务。 |
| FFRT_C_API int ffrt_cond_wait(ffrt_cond_t* cond, ffrt_mutex_t* mutex) | 条件变量等待函数，条件变量不满足时阻塞当前任务。 |
| FFRT_C_API int ffrt_cond_timedwait(ffrt_cond_t* cond, ffrt_mutex_t* mutex, const struct timespec* time_point) | 条件变量超时等待函数，条件变量不满足时阻塞当前任务，超时等待返回。如果达到最大等待时间点时没有调用ffrt_cond_signal或ffrt_cond_broadcast函数解除线程阻塞，则线程会被自动解除阻塞。 |
| FFRT_C_API int ffrt_cond_destroy(ffrt_cond_t* cond) | 销毁条件变量。 |
 
 
  

##### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### ffrt_cond_init()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_cond_init(ffrt_cond_t* cond, const ffrt_condattr_t* attr)
```
 
**描述**
 
初始化条件变量。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_cond_t* cond | 条件变量指针。 |
| const ffrt_condattr_t* attr | 条件变量属性指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 初始化条件变量成功返回ffrt_success， 初始化条件变量失败返回ffrt_error_inval。 |
 
 
  

##### ffrt_cond_signal()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_cond_signal(ffrt_cond_t* cond)
```
 
**描述**
 
唤醒阻塞在条件变量上的一个任务。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_cond_t* cond | 条件变量指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 唤醒成功返回ffrt_success， 唤醒失败返回ffrt_error_inval。 |
 
 
  

##### ffrt_cond_broadcast()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_cond_broadcast(ffrt_cond_t* cond)
```
 
**描述**
 
唤醒阻塞在条件变量上的所有任务。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_cond_t* cond | 条件变量指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 唤醒成功返回ffrt_success， 唤醒失败返回ffrt_error_inval。 |
 
 
  

##### ffrt_cond_wait()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_cond_wait(ffrt_cond_t* cond, ffrt_mutex_t* mutex)
```
 
**描述**
 
条件变量等待函数，条件变量不满足时阻塞当前任务。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_cond_t* cond | 条件变量指针。 |
| ffrt_mutex_t* mutex | mutex指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 等待后被成功唤醒返回ffrt_success， 等待失败返回ffrt_error_inval。 |
 
 
  

##### ffrt_cond_timedwait()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_cond_timedwait(ffrt_cond_t* cond, ffrt_mutex_t* mutex, const struct timespec* time_point)
```
 
**描述**
 
条件变量超时等待函数，条件变量不满足时阻塞当前任务，超时等待返回。如果达到最大等待时间点时没有调用ffrt_cond_signal或ffrt_cond_broadcast函数解除线程阻塞，则线程会被自动解除阻塞。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_cond_t* cond | 条件变量指针。 |
| ffrt_mutex_t* mutex | mutex指针。 |
| const struct timespec* time_point | 最大等待到的时间点，超过这个时间点等待返回。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 等待后被成功唤醒返回ffrt_success， 等待超时返回ffrt_error_timedout， 等待失败ffrt_error_inval。 |
 
 
  

##### ffrt_cond_destroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
FFRT_C_API int ffrt_cond_destroy(ffrt_cond_t* cond)
```
 
**描述**
 
销毁条件变量。
 
**起始版本：** 10
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| ffrt_cond_t* cond | 条件变量指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| FFRT_C_API int | 销毁条件变量成功返回ffrt_success， 销毁条件变量失败返回ffrt_error_inval。 |
