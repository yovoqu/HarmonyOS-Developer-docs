# JSVM_PropertyHandler

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandler
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


```text
typedef struct {...} JSVM_PropertyHandler
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable

包含将class作为函数进行调用时所触发的回调函数的函数指针，以及访问实例对象属性时触发的回调函数的函数指针集。

**起始版本：** 18

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable


| 名称 | 描述 |
| --- | --- |
| [JSVM_PropertyHandlerCfg](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-jsvm-jsvm-propertyhandlerconfigurationstruct8h) propertyHandlerCfg | 访问实例对象属性触发相应的回调函数。 |
| [JSVM_Callback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackstruct8h) callAsFunctionCallback | 实例对象作为函数调用将触发此回调。 |
