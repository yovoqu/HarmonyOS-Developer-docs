# JSVM_CreateVMOptions

更新时间：2026-06-13 03:51:30

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-createvmoptions
**支持设备：** Phone | PC/2in1 | Tablet | Wearable

```text
typedef struct {...} JSVM_CreateVMOptions
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

创建JavaScript虚拟机的选项。
 
**使用场景：** 需要自定义JavaScript虚拟机内存配置的应用，需要使用快照功能加速虚拟机启动的场景，对虚拟机内存使用有特殊要求的嵌入式或资源受限环境。
 
**系统能力：** SystemCapability.ArkCompiler.JSVM
 
**起始版本：** 11
 
**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)
 
**所在头文件：** [jsvm_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable
 
| 名称 | 描述 |
| --- | --- |
| size_t maxOldGenerationSize | 老年代内存大小上限。 |
| size_t maxYoungGenerationSize | 年轻代内存大小上限。 |
| size_t initialOldGenerationSize | 老年代内存大小初始值。 |
| size_t initialYoungGenerationSize | 年轻代内存大小初始值。 |
| const char* snapshotBlobData | 启动快照数据。 |
| size_t snapshotBlobSize | 启动快照数据的大小。 |
| bool isForSnapshotting | 虚拟机是否用于创建快照，为true，则虚拟机用于创建快照，为false，则虚拟机不用于创建快照。 |
