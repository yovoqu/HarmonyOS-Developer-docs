# DRM_OfflineMediakeyIdArray

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-offlinemediakeyidarray
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct DRM_OfflineMediakeyIdArray {...} DRM_OfflineMediakeyIdArray
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

离线媒体密钥ID数组。
 
**起始版本：** 11
 
**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)
 
**所在头文件：** [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| uint32_t idsCount | ID计数。 |
| int32_t idsLen[MAX_OFFLINE_MEDIA_KEY_ID_COUNT] | ID长度集合。 |
| uint8_t ids[MAX_OFFLINE_MEDIA_KEY_ID_COUNT][MAX_OFFLINE_MEDIA_KEY_ID_LEN] | ID数据集合。 |
