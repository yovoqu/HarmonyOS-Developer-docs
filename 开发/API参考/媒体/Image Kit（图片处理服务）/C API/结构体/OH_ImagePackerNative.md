# OH_ImagePackerNative

更新时间：2026-06-27 10:02:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagepackernative
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
typedef struct OH_ImagePackerNative OH_ImagePackerNative
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

OH_ImagePackerNative用于将ImageSource、PixelMap、Picture或PixelMap序列编码为图片数据或文件。
 
使用[OH_ImagePackerNative_Create](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_create)函数创建OH_ImagePackerNative对象。
 
使用[OH_ImagePackerNative_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_release)函数释放OH_ImagePackerNative对象。
 
资源管理：OH_ImagePackerNative使用完成后，应调用[OH_ImagePackerNative_Release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_release)释放。释放OH_ImagePackerNative对象不会释放OH_PackingOptions、OH_PackingOptionsForSequence、OH_ImageSourceNative、OH_PixelmapNative或OH_PictureNative对象。
 
OH_ImagePackerNative支持的编码方式如下：
  
| 输入对象 | 输出位置 | 编码函数 | 描述 |
| --- | --- | --- | --- |
| OH_ImageSourceNative | 数据缓冲区 | OH_ImagePackerNative_PackToDataFromImageSource | 将ImageSource编码为指定格式的数据。 |
| OH_PixelmapNative | 数据缓冲区 | OH_ImagePackerNative_PackToDataFromPixelmap | 将PixelMap编码为指定格式的数据。 |
| OH_PictureNative | 数据缓冲区 | OH_ImagePackerNative_PackToDataFromPicture | 将Picture编码为指定格式的数据，仅支持JPEG和HEIF。 |
| OH_PixelmapNative数组 | 数据缓冲区 | OH_ImagePackerNative_PackToDataFromPixelmapSequence | 将PixelMap序列编码为GIF格式数据。 |
| OH_ImageSourceNative | 文件描述符 | OH_ImagePackerNative_PackToFileFromImageSource | 将ImageSource编码到文件中。 |
| OH_PixelmapNative | 文件描述符 | OH_ImagePackerNative_PackToFileFromPixelmap | 将PixelMap编码到文件中。 |
| OH_PictureNative | 文件描述符 | OH_ImagePackerNative_PackToFileFromPicture | 将Picture编码到文件中，仅支持JPEG和HEIF。 |
| OH_PixelmapNative数组 | 文件描述符 | OH_ImagePackerNative_PackToFileFromPixelmapSequence | 将PixelMap序列编码为GIF格式并写入文件。 |
 
 
获取支持编码的图片格式使用[OH_ImagePackerNative_GetSupportedFormats](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h#oh_imagepackernative_getsupportedformats)函数。
 
**起始版本：** 12
 
**相关模块：** [Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)
 
**所在头文件：** [image_packer_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-packer-native-h)
