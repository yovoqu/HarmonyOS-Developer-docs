# AREngine_ARSemanticDenseCubeData

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-arsemanticdensecubedata
**支持设备：** Phone / Tablet / TV


## 概述
**支持设备：** Phone / Tablet / TV

高精几何重建对象的立方体数据。

作为[HMS_AREngine_ARSemanticDense_AcquireCubeData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arsemanticdense_acquirecubedata)接口输入。

**起始版本：** 6.0.0(20)

**相关模块：** [AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)

**所在头文件：** [ar_engine_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-header-file)


## 汇总
**支持设备：** Phone / Tablet / TV


### 成员变量
**支持设备：** Phone / Tablet / TV


| 名称 | 描述 |
| --- | --- |
| int32_t [id](#id) | 当前立方体的ID。 |
| int32_t [vertexSize](#vertexsize) | 当前立方体的顶点大小。 |
| float* [vertexData](#vertexdata) | 当前立方体的顶点数据。 对应立方体的8个顶点。索引从立方体后表面开始，按逆时针方向排列。 |
| float [confidence](#confidence) | 当前立方体的置信度。 |
| AREngine_ARSemanticPlaneLabel [label](#label) | 当前立方体的语义标签。 参见[AREngine_ARSemanticPlaneLabel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#arengine_arsemanticplanelabel)。 |


## 结构体成员变量说明
**支持设备：** Phone / Tablet / TV


### id
**支持设备：** Phone / Tablet / TV


```cpp
int32_t AREngine_ARSemanticDenseCubeData::id
```

**描述**

当前立方体的ID。


### vertexSize
**支持设备：** Phone / Tablet / TV


```cpp
int32_t AREngine_ARSemanticDenseCubeData::vertexSize
```

**描述**

当前立方体的顶点大小。


### vertexData
**支持设备：** Phone / Tablet / TV


```cpp
float* AREngine_ARSemanticDenseCubeData::vertexData
```

**描述**

当前立方体的顶点数据。


### confidence
**支持设备：** Phone / Tablet / TV


```cpp
float AREngine_ARSemanticDenseCubeData::confidence
```

**描述**

当前立方体的置信度。


### label
**支持设备：** Phone / Tablet / TV


```cpp
AREngine_ARSemanticPlaneLabel AREngine_ARSemanticDenseCubeData::label
```

**描述**

当前立方体的语义标签。
