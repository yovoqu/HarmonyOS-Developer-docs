# JSVM_VMInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-vminfo
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```text
typedef struct {...} JSVM_VMInfo
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

JavaScript虚拟机信息。

**起始版本：** 11

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


| 名称 | 描述 |
| --- | --- |
| uint32_t apiVersion | 此虚拟机支持的最高API版本。 |
| const char* engine | 实现虚拟机的引擎名称。 |
| const char* version | 虚拟机的版本。 |
| uint32_t cachedDataVersionTag | 缓存数据版本标签。 |
