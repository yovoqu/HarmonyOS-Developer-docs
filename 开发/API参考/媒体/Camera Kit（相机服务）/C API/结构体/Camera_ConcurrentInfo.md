# Camera_ConcurrentInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-concurrentinfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct Camera_ConcurrentInfo {...} Camera_ConcurrentInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

相机并发能力信息。
 
**起始版本：** 18
 
**相关模块：** [OH_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)
 
**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| Camera_Device camera | 相机实例。 |
| Camera_ConcurrentType type | 相机并发状态。 |
| Camera_SceneMode* sceneModes | 相机并发支持的模式。 |
| Camera_OutputCapability* outputCapabilities | 相机输出能力集。 |
| uint32_t modeAndCapabilitySize | 相机输出能力集大小。 |
