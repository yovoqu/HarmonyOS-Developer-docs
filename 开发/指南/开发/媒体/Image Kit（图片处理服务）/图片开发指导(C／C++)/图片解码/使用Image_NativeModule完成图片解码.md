# 使用Image_NativeModule完成图片解码

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-c

创建ImageSource，获取位图的宽、高信息，以及释放ImageSource实例。

从API version 22开始支持对部分专业相机格式图片的预览图解码，具体格式包括：CR2、CR3、ARW、NEF、RAF、NRW、ORF、RW2、PEF、SRW。


## 开发步骤


## 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target_link_libraries依赖中添加libimage_source.so、libpixelmap.so以及日志功能依赖的libhilog_ndk.z.so。
```text
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libpixelmap.so)
```


## Native接口调用

具体接口说明请参考[Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)。 在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下： **解码接口使用示例**
> [!NOTE]
> 部分接口（如：OH_ImageSourceNative_GetSupportedFormats）在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

导入相关头文件。
```text
#include
#include
#include
#include "napi/native_api.h"
#include
#include
```

日志宏定义可参考下述代码按实际需求自行修改。
```text
#undef LOG_DOMAIN
#undef LOG_TAG
#define LOG_DOMAIN 0x3200
#define LOG_TAG "IMAGE_SAMPLE"
```

定义ImageSourceNative类。
```text
class ImageSourceNative {
public:
    OH_ImageSource_Info *imageInfo;
    OH_ImageSourceNative *source = nullptr;
    OH_PixelmapNative *resPixMap = nullptr;
    OH_Pixelmap_ImageInfo *pixelmapImageInfo = nullptr;
    uint32_t frameCnt = 0;
    ImageSourceNative() {}
    ~ImageSourceNative() {}
};
```

创建ImageSourceNative的一个实例。
```text
static ImageSourceNative *g_thisImageSource = new ImageSourceNative();
```

创建GetJsResult函数处理napi返回值。
```text
// 处理napi返回值。
napi_value GetJsResult(napi_env env, int result)
{
    napi_value resultNapi = nullptr;
    napi_create_int32(env, result, &resultNapi);
    return resultNapi;
}
```

常量定义。
```text
const int MAX_STRING_LENGTH = 1024;
```

创建ImageSource实例。
```text
// 返回ErrorCode。
napi_value ReturnErrorCode(napi_env env, Image_ErrorCode errCode, std::string funcName)
{
    if (errCode != IMAGE_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "%{public}s failed, errCode: %{public}d.", funcName.c_str(), errCode);
        return GetJsResult(env, errCode);
    }
    return GetJsResult(env, errCode);
}

// 获取解码能力范围。
napi_value GetSupportedFormats(napi_env env, napi_callback_info info)
{
    Image_MimeType* mimeType = nullptr;
    size_t length = 10;
    Image_ErrorCode errCode = OH_ImageSourceNative_GetSupportedFormats(&mimeType, &length);
    if (errCode != IMAGE_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_GetSupportedFormats failed, "
                     "errCode: %{public}d.", errCode);
        return GetJsResult(env, errCode);
    }
    for (size_t count = 0; count source);
    return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_CreateFromUri");
}
```

在创建ImageSource实例后，进行指定属性值的获取和修改、通过解码参数创建PixelMap对象、获取图像帧数等操作。 创建PixelMap对象。
```text
// 通过图片解码参数创建PixelMap对象。
napi_value CreatePixelMap(napi_env env, napi_callback_info info)
{
    // ops参数支持传入nullptr, 当不需要设置解码参数时，不用创建。
    OH_DecodingOptions *ops = nullptr;
    OH_DecodingOptions_Create(&ops);
    // 设置为AUTO会根据图片资源格式和设备支持情况进行解码，如果图片资源为HDR资源且设备支持HDR解码则会解码为HDR的pixelmap。
    OH_DecodingOptions_SetDesiredDynamicRange(ops, IMAGE_DYNAMIC_RANGE_AUTO);

    OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
    g_thisImageSource->resPixMap = nullptr;

    Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmap(g_thisImageSource->source,
                                                                  ops, &g_thisImageSource->resPixMap);
    OH_DecodingOptions_Release(ops);
    ops = nullptr;
    if (errCode != IMAGE_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_CreatePixelmap failed, errCode: %{public}d.", errCode);
        return GetJsResult(env, errCode);
    }

    // 判断pixelmap是否为HDR内容。
    OH_PixelmapImageInfo_Create(&g_thisImageSource->pixelmapImageInfo);
    OH_PixelmapNative_GetImageInfo(g_thisImageSource->resPixMap, g_thisImageSource->pixelmapImageInfo);
    bool pixelmapIsHdr;
    OH_PixelmapImageInfo_GetDynamicRange(g_thisImageSource->pixelmapImageInfo, &pixelmapIsHdr);
    if (pixelmapIsHdr) {
        OH_LOG_INFO(LOG_APP, "The pixelMap's dynamicRange is HDR.");
    }
    OH_PixelmapImageInfo_Release(g_thisImageSource->pixelmapImageInfo);
    g_thisImageSource->pixelmapImageInfo = nullptr;
    return GetJsResult(env, errCode);
}
```

创建定义图片信息的结构体对象，并获取图片信息。
```text
// 创建定义图片信息的结构体对象，并获取图片信息。
napi_value GetImageInfo(napi_env env, napi_callback_info info)
{
    OH_ImageSourceInfo_Create(&g_thisImageSource->imageInfo);
    Image_ErrorCode errCode = OH_ImageSourceNative_GetImageInfo(g_thisImageSource->source,
                                                                0, g_thisImageSource->imageInfo);
    if (errCode != IMAGE_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "OH_ImageSourceInfo_Create failed, errCode: %{public}d.", errCode);
        return GetJsResult(env, errCode);
    }

    uint32_t width;
    uint32_t height;
    OH_ImageSourceInfo_GetWidth(g_thisImageSource->imageInfo, &width);
    OH_ImageSourceInfo_GetHeight(g_thisImageSource->imageInfo, &height);
    OH_LOG_INFO(LOG_APP, "OH_ImageSourceNative_GetImageInfo success,"
               "width: %{public}d, height: %{public}d.", width, height);
    OH_ImageSourceInfo_Release(g_thisImageSource->imageInfo);
    g_thisImageSource->imageInfo = nullptr;
    return GetJsResult(env, width); // 返回获取到info信息的width。
}
```

读取、编辑Exif信息。
```text
// 获取指定property的value值。
napi_value GetImageProperty(napi_env env, napi_callback_info info)
{
    napi_value argValue[1] = {nullptr};
    size_t argCount = 1;
    if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount source,
                                                                            &getKey, &getValue);
    if (errCode != IMAGE_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_GetImageProperty failed, errCode: %{public}d.", errCode);
        return GetJsResult(env, errCode);
    }
    napi_value resultNapi = nullptr;
    napi_create_string_utf8(env, getValue.data, getValue.size, &resultNapi);
    free(getValue.data);
    getValue.data = nullptr;
    return resultNapi;
}

// 修改指定property的value值。
napi_value ModifyImageProperty(napi_env env, napi_callback_info info)
{
    napi_value argValue[2] = {nullptr};
    size_t argCount = 2;
    const size_t minCount = 2;
    if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount source, &setKey, &setValue);
    return GetJsResult(env, errCode);
}
```

获取图像帧数。
```text
// 获取图像帧数。
napi_value GetFrameCount(napi_env env, napi_callback_info info)
{
    Image_ErrorCode errCode = OH_ImageSourceNative_GetFrameCount(g_thisImageSource->source,
                                                                 &g_thisImageSource->frameCnt);
    if (errCode != IMAGE_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_GetFrameCount failed, errCode: %{public}d.", errCode);
        return GetJsResult(env, errCode);
    }
    return GetJsResult(env, g_thisImageSource->frameCnt); // 返回获取到的图像帧数。
}
```

通过图片解码参数创建Pixelmap列表。
```text
// 通过图片解码参数创建Pixelmap列表。
napi_value CreatePixelmapList(napi_env env, napi_callback_info info)
{
    OH_DecodingOptions *opts = nullptr;
    OH_DecodingOptions_Create(&opts);
    OH_PixelmapNative** resVecPixMap = new OH_PixelmapNative* [g_thisImageSource->frameCnt];
    size_t outSize = g_thisImageSource->frameCnt;
    Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmapList(g_thisImageSource->source,
                                                                      opts, resVecPixMap, outSize);
    OH_DecodingOptions_Release(opts);
    opts = nullptr;
    delete[] resVecPixMap;
    return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_CreatePixelmapList");
}
```

获取图像延迟时间列表。
```text
// 获取图像延迟时间列表。
napi_value GetDelayTimeList(napi_env env, napi_callback_info info)
{
    int32_t *delayTimeList = new int32_t[g_thisImageSource->frameCnt];
    size_t size = g_thisImageSource->frameCnt;
    OH_LOG_INFO(LOG_APP, "GetDelayTimeList size: %{public}zu.", size);
    Image_ErrorCode errCode = OH_ImageSourceNative_GetDelayTimeList(g_thisImageSource->source, delayTimeList, size);
    delete[] delayTimeList;
    return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_GetDelayTimeList");
}
```

释放ImageSource。
```text
// 释放资源。
napi_value ReleaseImageSource(napi_env env, napi_callback_info info)
{
    Image_ErrorCode errCode = OH_ImageSourceNative_Release(g_thisImageSource->source);
    g_thisImageSource->source = nullptr;
    OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
    g_thisImageSource->resPixMap = nullptr;
    return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_Release");
}
```
