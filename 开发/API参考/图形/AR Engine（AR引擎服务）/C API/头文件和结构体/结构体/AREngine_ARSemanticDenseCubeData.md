# AREngine_ARSemanticDenseCubeData

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensecubedata
**支持设备：** Phone | Tablet | TV

##### 概述

高精几何重建对象的立方体数据。
 
作为[HMS_AREngine_ARSemanticDense_AcquireCubeData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsemanticdense_acquirecubedata)接口输入。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)
 
**所在头文件：** [ar_engine_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-header-file)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| int32_t id | 当前立方体的ID。 |
| int32_t vertexSize | 当前立方体的顶点大小。 |
| float* vertexData | 当前立方体的顶点数据。 对应立方体的8个顶点。索引从立方体后表面开始，按逆时针方向排列。 |
| float confidence | 当前立方体的置信度。 |
| AREngine_ARSemanticPlaneLabel label | 当前立方体的语义标签。 参见AREngine_ARSemanticPlaneLabel。 |
 
 
  

##### 结构体成员变量说明

  

##### id

```text
int32_t AREngine_ARSemanticDenseCubeData::id
```
 
**描述**
 
当前立方体的ID。
 
  

##### vertexSize

```text
int32_t AREngine_ARSemanticDenseCubeData::vertexSize
```
 
**描述**
 
当前立方体的顶点大小。
 
  

##### vertexData

```text
float* AREngine_ARSemanticDenseCubeData::vertexData
```
 
**描述**
 
当前立方体的顶点数据。
 
  

##### confidence

```text
float AREngine_ARSemanticDenseCubeData::confidence
```
 
**描述**
 
当前立方体的置信度。
 
  

##### label

```text
AREngine_ARSemanticPlaneLabel AREngine_ARSemanticDenseCubeData::label
```
 
**描述**
 
当前立方体的语义标签。
