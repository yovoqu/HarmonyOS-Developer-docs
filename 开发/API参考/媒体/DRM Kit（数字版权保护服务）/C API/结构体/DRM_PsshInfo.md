# DRM_PsshInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-psshinfo
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct DRM_PsshInfo {...} DRM_PsshInfo
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

DRM内容保护系统专用头（Protection System Specific Header）信息。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| uint8_t uuid[DRM_UUID_LEN] | UUID的PSSH信息。 |
| int32_t dataLen | PSSH数据长度。 |
| uint8_t data[MAX_PSSH_DATA_LEN] | PSSH数据。 |
