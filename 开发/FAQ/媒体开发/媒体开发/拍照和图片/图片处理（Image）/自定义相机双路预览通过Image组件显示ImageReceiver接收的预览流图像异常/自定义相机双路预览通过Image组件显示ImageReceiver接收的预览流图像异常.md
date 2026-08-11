# 自定义相机双路预览通过Image组件显示ImageReceiver接收的预览流图像异常

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-52

#### 问题现象

自定义相机双路预览，将ImageReceiver接收到的预览图像流通过Image组件显示，Image组件的objectFit属性设置为ImageFit.Contain，但是Image组件不能完整显示预览图像流，显示的画面不完整。用于显示预览图像数据的Image组件的UI描述如下：
 
```text
<span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
  <em>// this.imagePixelMap</em><em><span style="color: rgb(128,128,128);">为</span><span style="color: rgb(128,128,128);">ImageReceiver</span><span style="color: rgb(128,128,128);">接收的预览流数据</span></em>
  <span style="color: rgb(0,0,255);">Image</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">imagePixelMap</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">rotate</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">angle</span><span style="color: rgb(181,106,1);">: -</span><span style="color: rgb(255,0,0);">90 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">)     </span><em>  </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">组件逆时针旋转</span><span style="color: rgb(128,128,128);">90</span><span style="color: rgb(128,128,128);">度，用于适应相机预览流的旋转角度</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">objectFit</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">ImageFit</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Contain</span><span style="color: rgb(0,0,255);">)  </span><em>// </em><em><span style="color: rgb(128,128,128);">设置图片的填充，使得预览流画面在</span><span style="color: rgb(128,128,128);">Image</span><span style="color: rgb(128,128,128);">组件中完整显示</span></em>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">backgroundColor</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">Color</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">Black</span><span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">clip</span><span style="color: rgb(0,0,255);">(</span>true<span style="color: rgb(0,0,255);">)</span>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">floatWindowWidth</span><span style="color: rgb(0,0,255);">)    </span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">组件宽</span></em>
<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">floatWindowHeight</span><span style="color: rgb(0,0,255);">)  </span><em> </em><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">组件高</span></em>
```
 
 

#### 背景知识

- [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image)为图片组件，用于在应用中显示图片，支持加载PixelMap类型的图片数据。[objectFit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#objectfit)用于设置图片的填充效果，设置为[ImageFit.Contain](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#imagefit)后，将保持宽高比进行缩小或者放大，使得图片或视频完全显示在显示边界内。
- 双路预览即应用可同时使用两路预览流，一路通过XComponent的surface获取预览流数据，一路通过ImageReceiver的surface获取拍照流的数据，具体可参考：[双路预览](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-dual-channel-preview)。
- [clip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping#clip12)属性表示是否对子组件超出当前组件范围外的区域进行裁剪。[rotate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation#rotate)属性用于设置组件旋转。

 
 

#### 问题定位

为了适应相机预览流图像的旋转角度，将Image组件逆时针旋转了90度，若组件宽高不一致时，旋转后会导致Image组件的一部分超出父容器组件的范围，同时因为父容器Column组件设置了clip属性为true，这将导致Image组件旋转后超出Column组件的部分将被裁剪，若被裁剪的部分包含图像，则会导致图像显示不完整。
 
 

#### 分析结论

Image组件旋转后超出了父容器Column组件的范围，同时Column组件设置了clip属性为true，将Image组件超出Column组件的部分裁剪，被裁剪的部分包括了显示的相机预览流画面，导致相机预览流图像不能完整显示。
 
 

#### 修改建议

不通过旋转Image组件来适应相机预览流图像的旋转。调用[PreviewOutput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-previewoutput)的[getPreviewRotation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-previewoutput#getpreviewrotation12)接口，获取预览流的旋转角度。在[ImageReceiver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver)的[imageArrival](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver#on9)回调中接收到预览流图像后，通过获取的预览流旋转角度调用[PixelMap.rotate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#rotate9)来旋转预览流图像将图像调正。
