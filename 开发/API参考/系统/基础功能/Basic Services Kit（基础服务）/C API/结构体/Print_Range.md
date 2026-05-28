# Print_Range

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-range
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct {...} Print_Range
```
  

##### 概述

表示打印范围结构体。
 
**起始版本：** 13
 
**相关模块：** [OH_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)
 
**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| uint32_t startPage | 打印起始页。 |
| uint32_t endPage | 打印结束页。 |
| uint32_t pagesArrayLen | 打印页数组长度。 |
| uint32_t* pagesArray | 打印页数组。 |
