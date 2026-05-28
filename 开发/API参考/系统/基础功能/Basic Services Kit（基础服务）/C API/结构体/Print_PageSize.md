# Print_PageSize

更新时间：2026-04-03 09:39:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-pagesize
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct {...} Print_PageSize
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet

表示纸张尺寸信息。
 
**起始版本：** 12
 
**相关模块：** [OH_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)
 
**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| char *id | 纸张 ID。 |
| char *name | 纸张名称。 |
| uint32_t width | 纸张宽度，单位：毫米。 |
| uint32_t height | 纸张高度，单位：毫米。 |
