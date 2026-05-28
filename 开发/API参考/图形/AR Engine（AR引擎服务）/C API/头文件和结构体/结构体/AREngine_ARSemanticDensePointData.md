# AREngine_ARSemanticDensePointData

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensepointdata
**支持设备：** Phone | Tablet | TV

##### 概述

**支持设备：** Phone | Tablet | TV

高精几何重建对象的稠密点云数据。
 
作为[HMS_AREngine_ARSemanticDense_AcquirePointData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsemanticdense_acquirepointdata)接口输入。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)
 
**所在头文件：** [ar_engine_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-header-file)
 
  

##### 汇总

**支持设备：** Phone | Tablet | TV

  

##### 成员变量

**支持设备：** Phone | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| int32_t id | 当前点的ID。 |
| float x | 当前点的X坐标。 |
| float y | 当前点的Y坐标。 |
| float z | 当前点的Z坐标。 |
| int32_t r | 当前点的颜色，RGBA表示，这里是R的值。 |
| int32_t g | 当前点的颜色，RGBA表示，这里是G的值。 |
| int32_t b | 当前点的颜色，RGBA表示，这里是B的值。 |
| int32_t a | 当前点的颜色，RGBA表示，这里是A的值。 |
| float confidence | 当前点的置信度。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** Phone | Tablet | TV

  

##### id

**支持设备：** Phone | Tablet | TV

```text
int32_t AREngine_ARSemanticDensePointData::id
```
 
**描述**
 
当前点的ID。
 
  

##### x

**支持设备：** Phone | Tablet | TV

```text
float AREngine_ARSemanticDensePointData::x
```
 
**描述**
 
当前点的X坐标。
 
  

##### y

**支持设备：** Phone | Tablet | TV

```text
float AREngine_ARSemanticDensePointData::y
```
 
**描述**
 
当前点的Y坐标。
 
  

##### z

**支持设备：** Phone | Tablet | TV

```text
float AREngine_ARSemanticDensePointData::z
```
 
**描述**
 
当前点的Z坐标。
 
  

##### r

**支持设备：** Phone | Tablet | TV

```text
int32_t AREngine_ARSemanticDensePointData::r
```
 
**描述**
 
当前点的颜色，RGBA表示，这里是R的值。
 
  

##### g

**支持设备：** Phone | Tablet | TV

```text
int32_t AREngine_ARSemanticDensePointData::g
```
 
**描述**
 
当前点的颜色，RGBA表示，这里是G的值。
 
  

##### b

**支持设备：** Phone | Tablet | TV

```text
int32_t AREngine_ARSemanticDensePointData::b
```
 
**描述**
 
当前点的颜色，RGBA表示，这里是B的值。
 
  

##### a

**支持设备：** Phone | Tablet | TV

```text
int32_t AREngine_ARSemanticDensePointData::a
```
 
**描述**
 
当前点的颜色，RGBA表示，这里是A的值。
 
  

##### confidence

**支持设备：** Phone | Tablet | TV

```text
float AREngine_ARSemanticDensePointData::confidence
```
 
**描述**
 
当前点的置信度。
