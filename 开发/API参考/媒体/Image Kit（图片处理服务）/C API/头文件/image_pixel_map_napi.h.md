# image_pixel_map_napi.h

更新时间：2026-03-19 08:47:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-pixel-map-napi-h
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

声明可以锁定并访问pixelmap数据的方法，声明解锁的方法。

**库：** libpixelmap_ndk.z.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**引用文件：** <multimedia/image_framework/image_pixel_map_napi.h>

**起始版本：** 8

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 结构体
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OhosPixelMapInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapinfo) | - | 用于定义PixelMap的相关信息。 |


### 枚举
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [方法返回的错误码](#方法返回的错误码) | 函数方法返回值的错误码的枚举。 |
| [像素格式](#像素格式) | 像素格式的枚举。 |
| [anonymous enum](#pixelmap缩放类型) | PixelMap缩放类型的枚举。 |


### 函数
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [int32_t OH_GetImageInfo(napi_env env, napi_value value, OhosPixelMapInfo *info)](#oh_getimageinfo) | 获取PixelMap的信息，并记录信息到[OhosPixelMapInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapinfo)结构体中。 |
| [int32_t OH_AccessPixels(napi_env env, napi_value value, void** addrPtr)](#oh_accesspixels) | 获取PixelMap对象数据的内存地址，并锁定该内存。 函数执行成功后，*addrPtr就是获取的待访问的内存地址。访问操作完成后，必须要使用[OH_UnAccessPixels](#oh_unaccesspixels)来释放锁，否则的话资源无法被释放。待解锁后，内存地址就不可以再被访问和操作。 |
| [int32_t OH_UnAccessPixels(napi_env env, napi_value value)](#oh_unaccesspixels) | 释放PixelMap对象数据的内存锁，用于匹配方法[OH_AccessPixels](#oh_accesspixels)。 |


## 枚举类型说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 方法返回的错误码
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
enum anonymous enum
```

**描述**

函数方法返回值的错误码的枚举。

**起始版本：** 8

**废弃版本：** 10


| 枚举项 | 描述 |
| --- | --- |
| OHOS_IMAGE_RESULT_SUCCESS = 0 | 成功的结果。 |
| OHOS_IMAGE_RESULT_BAD_PARAMETER = -1 | 无效值。 |


### 像素格式
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
enum anonymous enum
```

**描述**

像素格式的枚举。

**起始版本：** 8

**废弃版本：** 10


| 枚举项 | 描述 |
| --- | --- |
| OHOS_PIXEL_MAP_FORMAT_NONE = 0 | 未知的格式。 |
| OHOS_PIXEL_MAP_FORMAT_RGBA_8888 = 3 | RGBA_8888格式。 |
| OHOS_PIXEL_MAP_FORMAT_RGB_565 = 2 | RGB_565格式。 |


### PixelMap缩放类型
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
enum anonymous enum
```

**描述**

PixelMap缩放类型的枚举。

**起始版本：** 10


| 枚举项 | 描述 |
| --- | --- |
| OHOS_PIXEL_MAP_SCALE_MODE_FIT_TARGET_SIZE = 0 | 适应目标图片大小的格式。 |
| OHOS_PIXEL_MAP_SCALE_MODE_CENTER_CROP = 1 | 以中心进行缩放的格式。 |


## 函数说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### OH_GetImageInfo()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
int32_t OH_GetImageInfo(napi_env env, napi_value value, OhosPixelMapInfo *info)
```

**描述**

获取PixelMap的信息，并记录信息到[OhosPixelMapInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapinfo)结构体中。

**起始版本：** 8

**废弃版本：** 10

**参数：**


| 参数项 | 描述 |
| --- | --- |
| napi_env env | napi的环境指针。 |
| napi_value value | 应用层的PixelMap对象。 |
| [OhosPixelMapInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapinfo) *info | 用于保存信息的指针对象。 |


**返回：**


| 类型 | 说明 |
| --- | --- |
| int32_t | [错误码](#方法返回的错误码)： OHOS_IMAGE_RESULT_SUCCESS：操作成功。 OHOS_IMAGE_RESULT_BAD_PARAMETER：操作失败。 |


### OH_AccessPixels()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
int32_t OH_AccessPixels(napi_env env, napi_value value, void** addrPtr)
```

**描述**

获取PixelMap对象数据的内存地址，并锁定该内存。

函数执行成功后，*addrPtr就是获取的待访问的内存地址。访问操作完成后，必须要使用[OH_UnAccessPixels](#oh_unaccesspixels)来释放锁，否则的话资源无法被释放。待解锁后，内存地址就不可以再被访问和操作。

**起始版本：** 8

**废弃版本：** 10

**参数：**


| 参数项 | 描述 |
| --- | --- |
| napi_env env | napi的环境指针。 |
| napi_value value | 应用层的PixelMap对象。 |
| void** addrPtr | 用于指向的内存地址的双指针对象。 |


**返回：**


| 类型 | 说明 |
| --- | --- |
| int32_t | [错误码](#方法返回的错误码)： OHOS_IMAGE_RESULT_SUCCESS：操作成功。 OHOS_IMAGE_RESULT_BAD_PARAMETER：操作失败。 |


### OH_UnAccessPixels()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
int32_t OH_UnAccessPixels(napi_env env, napi_value value)
```

**描述**

释放PixelMap对象数据的内存锁，用于匹配方法[OH_AccessPixels](#oh_accesspixels)。

**起始版本：** 8

**废弃版本：** 10

**参数：**


| 参数项 | 描述 |
| --- | --- |
| napi_env env | napi的环境指针。 |
| napi_value value | 应用层的PixelMap对象。 |


**返回：**


| 类型 | 说明 |
| --- | --- |
| int32_t | [错误码](#方法返回的错误码)： OHOS_IMAGE_RESULT_SUCCESS：操作成功。 OHOS_IMAGE_RESULT_BAD_PARAMETER：操作失败。 |
