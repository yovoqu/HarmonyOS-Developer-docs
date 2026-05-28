# HiDebug_MallocDispatch

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-mallocdispatch
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct HiDebug_MallocDispatch {...} HiDebug_MallocDispatch
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

应用程序进程可替换/恢复的HiDebug_MallocDispatch表结构类型定义。
 
**起始版本：** 20
 
**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)
 
**所在头文件：** [hidebug_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| void* (*malloc)(size_t) | 开发者自定义malloc函数指针。 |
| void* (*calloc)(size_t, size_t) | 开发者自定义calloc函数指针。 |
| void* (*realloc)(void*, size_t) | 开发者自定义realloc函数指针。 |
| void (*free)(void*) | 开发者自定义free函数指针。 |
| void* (*mmap)(void*, size_t, int, int, int, off_t) | 开发者自定义mmap函数指针。 |
| int (*munmap)(void*, size_t) | 开发者自定义munmap函数指针。 |
 
 
  

##### 成员函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### malloc()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void* (*malloc)(size_t)
```
 
**描述**
 
开发者自定义malloc函数指针。
 
  

##### calloc()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void* (*calloc)(size_t, size_t)
```
 
**描述**
 
开发者自定义calloc函数指针。
 
  

##### realloc()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void* (*realloc)(void*, size_t)
```
 
**描述**
 
开发者自定义realloc函数指针。
 
  

##### free()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void (*free)(void*)
```
 
**描述**
 
开发者自定义free函数指针。
 
  

##### mmap()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void* (*mmap)(void*, size_t, int, int, int, off_t)
```
 
**描述**
 
开发者自定义mmap函数指针。
 
  

##### munmap()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
int (*munmap)(void*, size_t)
```
 
**描述**
 
开发者自定义munmap函数指针。
