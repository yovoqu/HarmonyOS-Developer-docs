# Rcp_TransferRange

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| int64_t [from](#from) | 传输起始位置。 |
| bool [hasZeroFrom](#haszerofrom) | 是否从零开始。 |
| int64_t [to](#to) | 传输结束位置。 |
| bool [hasZeroTo](#haszeroto) | 是否以零结束。 |
| struct [Rcp_TransferRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range) * [next](#next) | 链式存储。指向下一个[Rcp_TransferRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range)。 |


## 结构体成员变量说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### from
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
int64_t Rcp_TransferRange::from
```

**描述**

传输起始位置。


### hasZeroFrom
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
bool Rcp_TransferRange::hasZeroFrom
```

**描述**

请求范围是否从零开始。


### hasZeroTo
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
bool Rcp_TransferRange::hasZeroTo
```

**描述**

是否以零结束。


### next
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
struct Rcp_TransferRange* Rcp_TransferRange::next
```

**描述**

链式存储。指向下一个[Rcp_TransferRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range)。


### to
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
int64_t Rcp_TransferRange::to
```

**描述**

传输结束位置。
