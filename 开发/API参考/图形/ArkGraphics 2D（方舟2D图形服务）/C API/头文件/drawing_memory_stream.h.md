# drawing_memory_stream.h

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-memory-stream-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

文件中定义了与内存流相关的功能函数。
 
**引用文件：** <native_drawing/drawing_memory_stream.h>
 
**库：** libnative_drawing.so
 
**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing
 
**起始版本：** 12
 
**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_Drawing_MemoryStream* OH_Drawing_MemoryStreamCreate(const void* data, size_t length, bool copyData) | 创建一个内存流对象。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 data为NULL或者length等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_MemoryStreamDestroy(OH_Drawing_MemoryStream* memoryStream) | 销毁内存流对象并回收该对象占用内存。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_Drawing_MemoryStreamCreate()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Drawing_MemoryStream* OH_Drawing_MemoryStreamCreate(const void* data, size_t length, bool copyData)
```
 
**描述**
 
创建一个内存流对象。
 
本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h#oh_drawing_errorcodeget)查看错误码的取值。
 
data为NULL或者length等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER。
 
**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const void* data | 数据段。 |
| size_t length | 数据段长度。 |
| bool copyData | 是否拷贝数据。true表示内存流对象会拷贝一份数据段数据，false表示内存流对象直接使用数据段数据，不拷贝。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Drawing_MemoryStream* | 函数会返回一个指针，指针指向创建的内存流对象OH_Drawing_MemoryStream。 |
 
 
  

#### OH_Drawing_MemoryStreamDestroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_Drawing_MemoryStreamDestroy(OH_Drawing_MemoryStream* memoryStream)
```
 
**描述**
 
销毁内存流对象并回收该对象占用的内存。
 
**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_MemoryStream* memoryStream | 指向内存流对象OH_Drawing_MemoryStream的指针。 |
