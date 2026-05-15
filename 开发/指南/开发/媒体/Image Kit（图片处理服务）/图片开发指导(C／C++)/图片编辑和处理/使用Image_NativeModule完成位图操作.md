# 使用Image_NativeModule完成位图操作

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-c

创建位图，获取位图的宽、高、pixelFormat、alphaType、rowStride信息、对位图进行操作以及释放位图实例。


## 开发步骤


## 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target_link_libraries依赖中添加libpixelmap.so以及日志依赖libhilog_ndk.z.so。
```text
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libpixelmap.so)
```


## Native接口调用

具体接口说明请参考[Image_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)。 在DevEco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下： **位图接口使用示例** 在初始化参数后创建Pixelmap实例，进行图片像素数据的读写，对图片进行缩放、位置变换、反转、旋转、裁剪等操作。
```text
#include
#include

#undef LOG_DOMAIN
#undef LOG_TAG
#define LOG_DOMAIN 0x3200
#define LOG_TAG "MY_TAG"

Image_ErrorCode PixelmapTest()
{
    uint8_t data[96];
    size_t dataSize = 96;
    for (int i = 0; i **提取图片平均颜色示例**     通过将图片缩放到较小尺寸，遍历所有像素计算RGB平均值来获取图片的主色调。
```text
#include
#include
#include
// 颜色结构体。
struct AverageColor {
uint8_t r;
uint8_t g;
uint8_t b;
};

// 提取图片平均颜色。
// 基本思路：
// 1. 将原始PixelMap缩放到较小尺寸（如32像素×32像素），减少像素数量以提高计算效率。
// 2. 读取缩放后的像素数据。
// 3. 遍历所有像素，累加R、G、B通道的值。
// 4. 计算各通道的平均值作为最终颜色。
Image_ErrorCode ExtractAverageColor(OH_PixelmapNative* pixelmap, AverageColor& avgColor)
{
if (pixelmap == nullptr) {
OH_LOG_ERROR(LOG_APP, "ExtractAverageColor: pixelmap is nullptr");
return IMAGE_BAD_PARAMETER;
}

// 获取原始图片信息，判断是否需要缩放。
OH_Pixelmap_ImageInfo* imageInfo;
OH_PixelmapImageInfo_Create(&imageInfo);
Image_ErrorCode errCode = OH_PixelmapNative_GetImageInfo(pixelmap, imageInfo);
if (errCode != IMAGE_SUCCESS) {
OH_LOG_ERROR(LOG_APP, "ExtractAverageColor: GetImageInfo failed, errCode: %{public}d", errCode);
OH_PixelmapImageInfo_Release(imageInfo);
return errCode;
}

uint32_t width, height;
OH_PixelmapImageInfo_GetWidth(imageInfo, &width);
OH_PixelmapImageInfo_GetHeight(imageInfo, &height);
OH_PixelmapImageInfo_Release(imageInfo);

// 定义缩小后的目标尺寸（32像素×32像素是经验值，平衡性能和准确度）。
const uint32_t SAMPLE_SIZE = 32;

// 如果图片较大，先进行缩放处理。
if (width > SAMPLE_SIZE || height > SAMPLE_SIZE) {
// 计算缩放比例。
double scaleX = (double)SAMPLE_SIZE / width;
double scaleY = (double)SAMPLE_SIZE / height;

// 对图片进行缩放。
errCode = OH_PixelmapNative_Scale(pixelmap, scaleX, scaleY);
if (errCode != IMAGE_SUCCESS) {
OH_LOG_ERROR(LOG_APP, "ExtractAverageColor: Scale failed, errCode: %{public}d", errCode);
OH_PixelmapNative_Release(pixelmap);
return errCode;
}
} else {
// 图片较小，直接使用原图。
pixelmap = pixelmap;
}

// 重新获取缩放后的图片信息。
OH_PixelmapImageInfo_Create(&imageInfo);
errCode = OH_PixelmapNative_GetImageInfo(pixelmap, imageInfo);
if (errCode != IMAGE_SUCCESS) {
OH_LOG_ERROR(LOG_APP, "ExtractAverageColor: GetImageInfo after scale failed, errCode: %{public}d", errCode);
OH_PixelmapImageInfo_Release(imageInfo);
return errCode;
}

uint32_t scaledWidth, scaledHeight, rowStride;
int32_t pixelFormat, alphaType;
OH_PixelmapImageInfo_GetWidth(imageInfo, &scaledWidth);
OH_PixelmapImageInfo_GetHeight(imageInfo, &scaledHeight);
OH_PixelmapImageInfo_GetRowStride(imageInfo, &rowStride);
OH_PixelmapImageInfo_GetPixelFormat(imageInfo, &pixelFormat);
OH_PixelmapImageInfo_GetAlphaType(imageInfo, &alphaType);
OH_PixelmapImageInfo_Release(imageInfo);
if (pixelFormat != PIXEL_FORMAT_RGBA_8888) {
// 此案例中只处理RGBA格式。
return IMAGE_BAD_SOURCE;
}

// 读取像素数据。
size_t bufferSize = rowStride * scaledHeight;
uint8_t* pixelData = new uint8_t[bufferSize];
errCode = OH_PixelmapNative_ReadPixels(pixelmap, pixelData, &bufferSize);
if (errCode != IMAGE_SUCCESS) {
OH_LOG_ERROR(LOG_APP, "ExtractAverageColor: ReadPixels failed, errCode: %{public}d", errCode);
delete[] pixelData;
return errCode;
}

// 根据像素格式确定每像素字节数。
constexpr int bytesPerPixel = 4; // 默认RGBA_8888

// 累加RGB值。
uint64_t totalR = 0, totalG = 0, totalB = 0;
uint32_t pixelCount = 0;

for (uint32_t y = 0; y  0) {
avgColor.r = (uint8_t)(totalR / pixelCount);
avgColor.g = (uint8_t)(totalG / pixelCount);
avgColor.b = (uint8_t)(totalB / pixelCount);
} else {
avgColor.r = 0;
avgColor.g = 0;
avgColor.b = 0;
}

OH_LOG_INFO(LOG_APP,
"ExtractAverageColor success, avgColor: R=%{public}d, G=%{public}d, B=%{public}d, pixelCount=%{public}d",
avgColor.r, avgColor.g, avgColor.b, pixelCount);

return IMAGE_SUCCESS;
}
```
