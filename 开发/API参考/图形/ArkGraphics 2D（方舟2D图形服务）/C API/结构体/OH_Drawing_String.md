# OH_Drawing_String

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-string
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} OH_Drawing_String
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

采用UTF-16编码的字符串信息结构体。
 
**起始版本：** 14
 
**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)
 
**所在头文件：** [drawing_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-types-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint8_t* strData | 指向包含UTF-16编码的字节数组的指针。 |
| uint32_t strLen | strData指向的字符串的实际长度，单位为字节。 |
