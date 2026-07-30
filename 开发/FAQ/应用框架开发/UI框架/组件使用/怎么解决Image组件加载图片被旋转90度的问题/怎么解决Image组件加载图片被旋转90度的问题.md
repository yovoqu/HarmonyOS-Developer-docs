# 怎么解决Image组件加载图片被旋转90度的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-720

#### 问题现象

使用Image组件加载图片时，图片自动被旋转了90度，如何使图片显示方向正确。问题代码如下：
 
```text
@Entry
@Component
struct ImageRotationProblem {
  build() {
    Column() {
     <em> // 运行时请按需替换图片资源</em>
      Image($r('app.media.startIcon'));
    };
  }
}
```
 
左图为正常显示效果，右图为Image加载显示效果：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/HFwkJPWuRnao_cmaS8xMYA/zh-cn_image_0000002658794579.png?HW-CC-KV=V1&HW-CC-Date=20260730T072326Z&HW-CC-Expire=86400&HW-CC-Sign=B2A7609985CAE5FFE0E40E01A00871694E0426F5B20C61C32579EB3077B19E1E)

 
 

#### 背景知识

- [Image组件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)为图片组件，常用于在应用中显示图片。
- [rotate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#rotate)属性能够设置组件旋转。可使组件在以组件左上角为坐标原点的坐标系中进行旋转。
- [orientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#orientation14)属性能够设置图像内容的显示方向。该属性对alt占位图不生效，不支持gif和svg类型的图片。如果需要显示携带旋转角度信息或翻转信息的图片，建议使用ImageRotateOrientation.AUTO进行设置。
- [ImageSource类](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagesource)，用于获取图片相关信息。在调用ImageSource的方法前，需要先通过createImageSource构建一个ImageSource实例。
- [EXIF（Exchangeable image file format）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-tool)是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。当前支持JPEG、PNG、HEIF格式，且需要图片包含EXIF信息。
- [图片旋转角度](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-rotate-faq#图片旋转角度介绍)在数码摄影中，拍摄设备（如手机、相机）会将图片的旋转角度（方向）信息保存在图片的Exif（Exchangeable image file format）数据的Orientation字段。

 
 

#### 问题定位
1. 使用Image组件加载其他图片，检查是否为组件问题。由于“新闻”图片正常显示，确认非组件问题。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/U_kXHGeWTlur-_aGlTThAg/zh-cn_image_0000002628555212.png?HW-CC-KV=V1&HW-CC-Date=20260730T072326Z&HW-CC-Expire=86400&HW-CC-Sign=D5C5D333B191C6777C98A7A567F672224C554910EF8D2111D31A83C5508159FD)

2. 检查原图片Exif信息，定位其orientation属性。通过在线网站查看图片信息得知该图片的拍摄方向为逆时针旋转90度。由此，定位到图片被旋转的原因。

| 属性 | 说明 | 值 |

| --- | --- | --- |

| ImageWidth | 像素宽度 | 4032 |

| XResolution | X分辨率 | 72 |

| YResolution | Y分辨率 | 72 |

| Resolution | 分辨率单位 | 英寸 |

| Orientation | 拍摄方向 | 6（逆时针旋转90°） |
 
 

#### 分析结论

图片旋转是因为图像的拍摄方向属性固定为旋转90度导致的，需要旋转归位或者对图像进行其他处理。
 
 

#### 修改建议

- **方案一：通过组件旋转属性，使图片显示方向正常：**直接给Image组件加上对应的旋转属性，使图片正常显示。因为图片的方向是逆时针90度，将Image组件顺时针旋转90度后，图片会正常显示。通过以下属性旋转：

  
```text
@Entry
@Component
struct ImageRotationOne {
  build() {
    Column() {
    <em>  // 运行时请按需替换图片资源</em>
      Image($r('app.media.startIcon'))
        .rotate({ angle: 90 });
    };
  }
}
```
 
> [!NOTE]
> 这种方案只有在确定图片的方向信息时才能使用，如果是从网络加载的、不能确定方向的图片列表，该方案则不适用。

- **方案二：通过orientation属性，设置图片的显示方向：**

  利用orientation属性，[设置图像内容的显示方向](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#示例21设置图像内容的显示方向)。如果需要显示携带旋转角度信息或翻转信息的图片建议使用ImageRotateOrientation.AUTO进行设置。
```text
<em>// 运行时请按需替换图片资源</em>
@Entry
@Component
struct ImageRotationTwo {
  build() {
    Column() {
     <em> // 运行时请按需替换图片资源</em>
      Image($r('app.media.startIcon'))
        .orientation(ImageRotateOrientation.AUTO);
    };
  }
}
```


  
> [!NOTE]
> 这种方案不支持gif和svg类型的图片。

- **方案三：将图片转成ImageSource对象后读取旋转信息：****思路**：读取每张图片的方向orientation信息，根据其方向，设置图片的显示方向。

1. 使用Image Kit的createImageSource接口，将图片转换成image.ImageSource对象。

2. 使用ImageSource的getImageProperty接口获取图片的image.PropertyKey.ORIENTATION旋转信息。

3. 根据图片的EXIF方向信息设置orientation属性值进行旋转，使图片正常显示。

  详细代码可以参考：[获取图片的Exif信息并设置图像内容的显示方向](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#示例22获取图片的exif信息并设置图像内容的显示方向)。
