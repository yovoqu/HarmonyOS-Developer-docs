# DRM_MediaKeySystemInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeysysteminfo
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct DRM_MediaKeySystemInfo {...} DRM_MediaKeySystemInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

加密媒体内容的DRM信息。
 
**起始版本：** 11
 
**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)
 
**所在头文件：** [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t psshCount | PSSH计数。 |
| DRM_PsshInfo psshInfo[MAX_PSSH_INFO_COUNT] | PSSH信息。 |
