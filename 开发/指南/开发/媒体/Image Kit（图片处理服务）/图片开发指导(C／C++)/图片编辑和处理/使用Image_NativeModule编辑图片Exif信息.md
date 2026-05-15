# 使用Image_NativeModule编辑图片Exif信息

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-tool-c

Image Kit提供图片Exif信息的读取与编辑能力。

Exif（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。当前支持JPEG、PNG、HEIF、WEBP23+、DNG23+格式，且需要图片包含Exif信息。

在图库等应用中，需要查看或修改数码照片的Exif信息。当摄像机的手动镜头参数无法自动写入到Exif信息中，或者相机断电等原因会导致拍摄时间出错时，可手动修改错误的Exif数据。

系统目前仅支持对部分Exif信息的查看和修改，具体支持的范围请参见：[变量](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h#变量)里的OHOS_IMAGE_PROPERTY_XXX类型。需要注意的是，DNG格式图片仅支持读取Exif信息，不支持修改。


## 开发步骤


## 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target_link_libraries依赖中添加libimage_source.so 以及日志依赖libhilog_ndk.z.so。
```text
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so)
```


## Native接口调用

Exif信息的读取与编辑相关C API接口的详细介绍请参见[OH_ImageSourceNative_GetImageProperty()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_getimageproperty)和[OH_ImageSourceNative_ModifyImageProperty()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_modifyimageproperty)。 在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下： **读取和编辑图片Exif信息接口使用示例**
> [!NOTE]
> 部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

导入相关头文件。
```text
#include
#include
#include
#include "napi/native_api.h"
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

在成功创建ImageSource对象后，读取、编辑Exif信息。
> [!NOTE]
> 创建ImageSource对象可参考图片解码。


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
