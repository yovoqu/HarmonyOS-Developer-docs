# NativeChildProcess_FdList

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fdlist
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct NativeChildProcess_FdList {...} NativeChildProcess_FdList
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

传递给子进程的文件描述符信息列表，文件描述符记录个数不能超过16个。
 
**起始版本：** 13
 
**相关模块：** [ChildProcess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess)
 
**所在头文件：** [native_child_process.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| struct NativeChildProcess_Fd* head | 子进程文件描述符记录链表中的第一个记录。 |
