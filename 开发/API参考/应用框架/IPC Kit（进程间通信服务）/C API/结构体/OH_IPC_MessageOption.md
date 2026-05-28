# OH_IPC_MessageOption

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject-oh-ipc-messageoption
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} OH_IPC_MessageOption
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

IPC消息选项定义。
 
**起始版本：** 12
 
**相关模块：** [OHIPCRemoteObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohipcremoteobject)
 
**所在头文件：** [ipc_cremote_object.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-cremote-object-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_IPC_RequestMode mode | 消息请求模式。 |
| uint32_t timeout | RPC预留参数，该参数对IPC无效。 |
| void* reserved | 保留参数，必须为空 |
