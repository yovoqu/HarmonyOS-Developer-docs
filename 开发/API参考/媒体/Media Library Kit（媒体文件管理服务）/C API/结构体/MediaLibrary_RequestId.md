# MediaLibrary_RequestId

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-medialibrary-requestid
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct MediaLibrary_RequestId {...} MediaLibrary_RequestId
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

定义请求ID。
 
当请求媒体库资源时，会返回此类型。
 
请求ID可用于取消请求。
 
如果请求失败，值将全为零，如 "00000000-0000-0000-0000-000000000000"。
 
**起始版本：** 12
 
**相关模块：** [MediaAssetManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager)
 
**所在头文件：** [media_asset_base_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| char requestId[UUID_STR_MAX_LENGTH] | 请求ID。 |
