# drawing_color_space.h

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-color-space-h
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

文件中定义了与颜色空间相关的功能函数。

**引用文件：** <native_drawing/drawing_color_space.h>

**库：** libnative_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 函数
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [OH_Drawing_ColorSpace* OH_Drawing_ColorSpaceCreateSrgb(void)](#oh_drawing_colorspacecreatesrgb) | 创建一个标准颜色空间。 |
| [OH_Drawing_ColorSpace* OH_Drawing_ColorSpaceCreateSrgbLinear(void)](#oh_drawing_colorspacecreatesrgblinear) | 创建一个Gamma 1.0空间上的颜色空间。 |
| [void OH_Drawing_ColorSpaceDestroy(OH_Drawing_ColorSpace* colorSpace)](#oh_drawing_colorspacedestroy) | 销毁颜色空间对象，并回收该对象占用内存。 |


## 函数说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### OH_Drawing_ColorSpaceCreateSrgb()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
OH_Drawing_ColorSpace* OH_Drawing_ColorSpaceCreateSrgb(void)
```

**描述**

创建一个标准颜色空间。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**


| 类型 | 说明 |
| --- | --- |
| [OH_Drawing_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)* | 函数返回一个指针，指针指向创建的颜色空间对象[OH_Drawing_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)。 |


### OH_Drawing_ColorSpaceCreateSrgbLinear()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
OH_Drawing_ColorSpace* OH_Drawing_ColorSpaceCreateSrgbLinear(void)
```

**描述**

创建一个Gamma 1.0空间上的颜色空间。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**


| 类型 | 说明 |
| --- | --- |
| [OH_Drawing_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)* | 函数返回一个指针，指针指向创建的颜色空间对象[OH_Drawing_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)。 |


### OH_Drawing_ColorSpaceDestroy()
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
void OH_Drawing_ColorSpaceDestroy(OH_Drawing_ColorSpace* colorSpace)
```

**描述**

销毁颜色空间对象，并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**


| 参数项 | 描述 |
| --- | --- |
| [OH_Drawing_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)* colorSpace | 指向颜色空间对象[OH_Drawing_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-colorspace)的指针。 |
