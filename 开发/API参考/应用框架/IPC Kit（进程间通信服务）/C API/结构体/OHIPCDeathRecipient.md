# OHIPCDeathRecipient

更新时间：2026-07-28 11:23:46

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject-ohipcdeathrecipient
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OHIPCDeathRecipient OHIPCDeathRecipient
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

IPC死亡通知对象，用于监听IPC远程对象的死亡事件。创建OHIPCDeathRecipient对象后，必须注册到OHIPCRemoteObject对象才能生效。当远程进程意外终止或主动销毁时，注册了死亡监听的本地进程将收到死亡通知回调，从而及时释放相关资源或进行错误处理。
 
**起始版本：** 12
 
**相关模块：** [OHIPCRemoteObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject)
 
**所在头文件：** [ipc_cremote_object.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cremote-object-h)
