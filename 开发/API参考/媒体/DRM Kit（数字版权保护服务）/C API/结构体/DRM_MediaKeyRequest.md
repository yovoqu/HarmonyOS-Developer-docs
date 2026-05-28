# DRM_MediaKeyRequest

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequest
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct DRM_MediaKeyRequest {...} DRM_MediaKeyRequest
```
  

##### 概述

媒体密钥请求。
 
**起始版本：** 11
 
**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)
 
**所在头文件：** [native_drm_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| DRM_MediaKeyRequestType type | 媒体密钥请求类型。 |
| int32_t dataLen | 媒体密钥请求数据长度。 |
| uint8_t data[MAX_MEDIA_KEY_REQUEST_DATA_LEN] | 发送到媒体密钥服务器的媒体密钥请求数据。 |
| char defaultUrl[MAX_DEFAULT_URL_LEN] | 媒体密钥服务器URL。 |
