# DRM_MediaKeyStatus

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeystatus
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct DRM_MediaKeyStatus {...} DRM_MediaKeyStatus
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

媒体密钥状态。
 
**起始版本：** 11
 
**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)
 
**所在头文件：** [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t statusCount | 状态计数。 |
| char statusName[MAX_MEDIA_KEY_STATUS_COUNT][MAX_MEDIA_KEY_STATUS_NAME_LEN] | 状态名数组。 |
| char statusValue[MAX_MEDIA_KEY_STATUS_COUNT][MAX_MEDIA_KEY_STATUS_VALUE_LEN] | 状态值数组。 |
