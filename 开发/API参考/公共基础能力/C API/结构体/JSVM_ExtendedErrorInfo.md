# JSVM_ExtendedErrorInfo

更新时间：2026-03-17 02:21:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-extendederrorinfo
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```text
typedef struct {...} JSVM_ExtendedErrorInfo
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

扩展的异常信息。

**起始版本：** 11

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


| 名称 | 描述 |
| --- | --- |
| const char* errorMessage | UTF-8编码的字符串，包含异常信息。 |
| void* engineReserved | 特定于VM的详细异常信息。目前尚未为任何VM实现此功能。 |
| uint32_t engineErrorCode | 特定于VM的异常代码。目前尚未为任何VM实现此功能。 |
| JSVM_Status errorCode | 源自最后一个异常的JSVM-API状态码。 |
