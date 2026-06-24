# drawing_point.h

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-point-h
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

文件中定义了与坐标点相关的功能函数。
 
**引用文件：** <native_drawing/drawing_point.h>
 
**库：** libnative_drawing.so
 
**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing
 
**起始版本：** 11
 
**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 函数

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| OH_Drawing_Point* OH_Drawing_PointCreate(float x, float y) | 用于创建一个坐标点对象。 |
| OH_Drawing_ErrorCode OH_Drawing_PointGetX(const OH_Drawing_Point* point, float* x) | 用于获取点的x轴坐标。 |
| OH_Drawing_ErrorCode OH_Drawing_PointGetY(const OH_Drawing_Point* point, float* y) | 用于获取点的y轴坐标。 |
| OH_Drawing_ErrorCode OH_Drawing_PointSet(OH_Drawing_Point* point, float x, float y) | 用于设置点的x轴和y轴坐标。 |
| OH_Drawing_ErrorCode OH_Drawing_PointNegate(OH_Drawing_Point* point) | 对点的坐标进行取反操作。 |
| OH_Drawing_ErrorCode OH_Drawing_PointOffset(OH_Drawing_Point* point, float dx, float dy) | 将指定坐标点沿着x轴和y轴方向偏移一定距离。 |
| void OH_Drawing_PointDestroy(OH_Drawing_Point* point) | 用于销毁坐标点对象并回收该对象占有的内存。 |
 
 
  

#### 函数说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### OH_Drawing_PointCreate()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Drawing_Point* OH_Drawing_PointCreate(float x, float y)
```
 
**描述**
 
用于创建一个坐标点对象。
 
**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| float x | X轴坐标。 |
| float y | Y轴坐标。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Point* | 函数会返回一个指针，指针指向创建的坐标点对象。 |
 
 
  

#### OH_Drawing_PointGetX()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Drawing_ErrorCode OH_Drawing_PointGetX(const OH_Drawing_Point* point, float* x)
```
 
**描述**
 
用于获取点的x轴坐标。
 
**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Point* point | 指向坐标点对象OH_Drawing_Point的指针。 |
| float* x | 表示点的x轴坐标。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数point或者x为空。 |
 
 
  

#### OH_Drawing_PointGetY()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Drawing_ErrorCode OH_Drawing_PointGetY(const OH_Drawing_Point* point, float* y)
```
 
**描述**
 
用于获取点的y轴坐标。
 
**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Point* point | 指向坐标点对象OH_Drawing_Point的指针。 |
| float* y | 表示点的y轴坐标。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数point或者y为空。 |
 
 
  

#### OH_Drawing_PointSet()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Drawing_ErrorCode OH_Drawing_PointSet(OH_Drawing_Point* point, float x, float y)
```
 
**描述**
 
用于设置点的x轴和y轴坐标。
 
**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing
 
**起始版本：** 12
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Point* point | 指向坐标点对象OH_Drawing_Point的指针。 |
| float x | 表示点的x轴坐标。 |
| float y | 表示点的y轴坐标。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数point为空。 |
 
 
  

#### OH_Drawing_PointNegate()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Drawing_ErrorCode OH_Drawing_PointNegate(OH_Drawing_Point* point)
```
 
**描述**
 
对点的坐标进行取反操作。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Point* point | 指向坐标点对象OH_Drawing_Point的指针。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数point为空。 |
 
 
  

#### OH_Drawing_PointOffset()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
OH_Drawing_ErrorCode OH_Drawing_PointOffset(OH_Drawing_Point* point, float dx, float dy)
```
 
**描述**
 
将指定坐标点沿着x轴和y轴方向偏移一定距离。
 
**起始版本：** 26.0.0
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Point* point | 指向坐标点对象OH_Drawing_Point的指针。 |
| float dx | 表示在x轴上的偏移量，单位为像素。正数表示往x轴正方向平移，负数表示往x轴负方向平移。 |
| float dy | 表示在y轴上的偏移量，单位为像素。正数表示往y轴正方向平移，负数表示往y轴负方向平移。 |
 
 
**返回：**
  
| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数point为空。 |
 
 
  

#### OH_Drawing_PointDestroy()

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
void OH_Drawing_PointDestroy(OH_Drawing_Point* point)
```
 
**描述**
 
用于销毁坐标点对象并回收该对象占有的内存。
 
**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing
 
**起始版本：** 11
 
**参数：**
  
| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Point* point | 指向坐标点对象的指针。 |
