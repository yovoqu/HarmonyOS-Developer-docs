# NativeChildProcess_Args

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-args
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} NativeChildProcess_Args
```
  

##### 概述

传递给子进程的参数。
 
**起始版本：** 13
 
**相关模块：** [ChildProcess](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess)
 
**所在头文件：** [native_child_process.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char* entryParams | 入口参数，大小不能超过150KB。 |
| struct NativeChildProcess_FdList fdList | 传递给子进程的文件描述符信息列表。 |
