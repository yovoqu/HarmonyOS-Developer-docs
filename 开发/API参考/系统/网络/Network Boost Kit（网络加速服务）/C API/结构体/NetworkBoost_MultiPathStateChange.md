# NetworkBoost_MultiPathStateChange

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_statechange
**支持设备：** Phone / PC/2in1 / Tablet


## 概述
**支持设备：** Phone / PC/2in1 / Tablet

多网状态信息，用于注册多网状态变化事件回调后，系统多网状态发生变化的事件通知。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview)

**所在头文件：** [network_boost_handover.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-handover)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| [NetworkBoost_MultiPathState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_multipathstate) [multiPathState](#multipathstate) | 多网状态。 |
| [NetworkBoost_MultiPathChangeCause](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_multipathchangecause) [changeCause](#changecause) | 多网状态变化原因。 |
| [NetworkBoost_NetHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_nethandle) [netHandle](#nethandle) | 多网链路的netHandle。 |
| [NetworkBoost_PathState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_pathstate) [pathState](#pathstate) | 多网链路状态。 |
| [NetworkBoost_PathType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview#networkboost_pathtype) [pathType](#pathtype) | 多网链路类型。 |


## 结构体成员变量说明
**支持设备：** Phone / PC/2in1 / Tablet


## multiPathState
**支持设备：** Phone / PC/2in1 / Tablet


```text
NetworkBoost_MultiPathState NetworkBoost_MultiPathStateChange::multiPathState
```

**描述**

多网状态，可以通过该信息获取当前多网所处状态，包含空闲态、建立中、已建立和释放中四种状态。


## changeCause
**支持设备：** Phone / PC/2in1 / Tablet


```text
NetworkBoost_MultiPathChangeCause NetworkBoost_MultiPathStateChange::changeCause
```

**描述**

多网状态变化原因，在多网状态发生变化时，通过该信息可以获取发生多网状态发生变化的原因。


## netHandle
**支持设备：** Phone / PC/2in1 / Tablet


```text
NetworkBoost_NetHandle NetworkBoost_MultiPathStateChange::netHandle
```

**描述**

多网链路的netHandle。


## pathState
**支持设备：** Phone / PC/2in1 / Tablet


```text
NetworkBoost_PathState NetworkBoost_MultiPathStateChange::pathState
```

**描述**

多网链路状态。


## pathType
**支持设备：** Phone / PC/2in1 / Tablet


```text
NetworkBoost_PathType NetworkBoost_MultiPathStateChange::pathType
```

**描述**

多网链路类型。
