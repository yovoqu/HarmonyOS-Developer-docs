# OHIPCRemoteProxy

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcparcel-ohipcremoteproxy
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OHIPCRemoteProxy OHIPCRemoteProxy
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

IPC（进程间通信）远端代理对象，用于在客户端代理远端服务的能力，实现跨进程通信。该对象封装了远端服务的引用，支持向远端服务发送请求和接收响应。适用于需要跨进程调用服务能力的场景，例如跨进程服务调用、系统服务访问、跨应用数据共享等典型应用。使用该对象可以简化跨进程通信的实现，提高开发效率。
 
**起始版本：** 12
 
**相关模块：**[OHIPCParcel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcparcel)
 
**所在头文件：** [ipc_cparcel.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cparcel-h)
