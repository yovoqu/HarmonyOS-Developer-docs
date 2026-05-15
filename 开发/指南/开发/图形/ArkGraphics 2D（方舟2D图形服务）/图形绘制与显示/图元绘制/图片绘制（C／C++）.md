# 图片绘制（C/C++）

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-drawing-c

位图是一种用于在内存中存储和表示图像的数据结构，它是一个未经过压缩的像素集合，而JPEG或PNG等图片是压缩格式的，两者并不相同。如果需要将JPEG或PNG绘制到屏幕上，需要先解码成位图格式，具体可参考[图片处理服务（Image Kit）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-overview)图片解码相关章节。

目前Drawing（C/C++）中位图绘制需要依赖PixelMap，它可以用于读取或写入图像数据以及获取图像信息。详细的API介绍请参考[drawing_pixel_map.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-pixel-map-h)。

有多个API接口可以创建PixelMap，下文以使用OH_Drawing_PixelMapGetFromOhPixelMapNative()为例。


## 示例代码

[图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
