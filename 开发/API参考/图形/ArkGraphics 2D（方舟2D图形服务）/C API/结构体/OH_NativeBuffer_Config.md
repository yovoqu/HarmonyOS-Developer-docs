# OH_NativeBuffer_Config

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-config
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct {...} OH_NativeBuffer_Config
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

OH_NativeBuffer的属性配置，用于申请新的OH_NativeBuffer实例或查询现有实例的相关属性。
 
**起始版本：** 9
 
**相关模块：** [OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer)
 
**所在头文件：** [native_buffer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-buffer-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t width | 宽度（像素）。 |
| int32_t height | 高度（像素）。 |
| int32_t format | 像素格式，具体可参见OH_NativeBuffer_Format枚举。 |
| int32_t usage | buffer的用途说明，具体可参见OH_NativeBuffer_Usage枚举。 |
| int32_t stride | 输出参数。本地窗口缓冲区步幅，单位为Byte。 起始版本： 10 |
