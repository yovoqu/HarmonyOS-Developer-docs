# XEG_RTShadowAODescription

更新时间：2026-05-14 10:06:22

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtshadowaodescription
**支持设备：** Phone | PC/2in1 | Tablet | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | TV

此结构体描述光线追踪阴影和环境光遮蔽算法渲染命令的输入信息。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)
 
**所在头文件：** [xeg_vulkan_rt_visible_mask.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rt-visible-mask-8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| XEG_StructureType sType | 识别此结构的XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_RT_SHADOWAO_DESCRIPTION。 |
| const void * pNext | 指向扩展结构的指针。 |
| VkImageView inputDepthImage | 深度图像，不能为空。 |
| VkImageView inputNormalImage | 法线图像，不能为空。需要是无符号浮点格式并包含3个以上通道，如VK_FORMAT_R8G8B8_UNORM。XEngine将按照Normal=textureLod(inputNormalImage).xyz*2.0–1.0的方式解析法线。 |
| VkImageView inputMotionVectorImage | 运动矢量图像，可以为空。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去其上一帧的NDC坐标的XY值。图像格式需要是VK_FORMAT_R16G16_SFLOAT或更高精度。保留字段，暂不支持。 |
| VkImageView outputShadowAOImage | 输出的阴影和环境光遮蔽图像，不能为空，格式必须为VK_FORMAT_R8G8_UNORM。阴影值将写入R通道，环境光遮蔽值将写入G通道。 |
| VkAccelerationStructureKHR accelerationStructure | 场景的光线追踪加速结构。 |
| bool isAsInTranslatedSpace | 光线追踪加速结构是否在Translated世界空间构建。true表示在Translated世界空间构建，false表示在绝对世界空间构建。默认值为false。 |
| float translatedViewMatrix | 相机Translated观察矩阵，必须是4*4列主序矩阵。当isAsInTranslatedSpace值为false时可以不赋值。 |
| float viewMatrix [16] | 相机观察矩阵，必须是4*4列主序矩阵。 |
| float projectionMatrix [16] | 相机投影矩阵，必须是4*4列主序矩阵。 |
| float worldCameraOrigin [3] | 相机在世界空间中的位置坐标。 |
| bool ndcFlipY | 标识NDC空间与世界空间是否存在Y轴翻转关系。true表示翻转，false表示不翻转。默认值为false。 |
| const XEG_RTShadowParameters * pRtShadowParameters | 光线追踪阴影算法参数，当XEG_RTShadowAOCreateInfo::enableRTShadow=true时不能为空。 |
| const XEG_RTAOParameters * pRtAOParameters | 光线追踪环境光算法参数，当XEG_RTShadowAOCreateInfo::enableRTAO=true时不能为空。 |
| const XEG_RTShadowAODenoiserParameters * pRtShadowAODenoiserParameters | 去噪参数，不能为空。光线追踪阴影和环境光遮蔽使用相同的去噪参数。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | TV

  

#### accelerationStructure

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkAccelerationStructureKHR XEG_RTShadowAODescription::accelerationStructure
```
 
**描述**
 
场景的光线追踪加速结构。
 
  

#### inputDepthImage

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkImageView XEG_RTShadowAODescription::inputDepthImage
```
 
**描述**
 
深度图像，不能为空。
 
  

#### inputMotionVectorImage

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkImageView XEG_RTShadowAODescription::inputMotionVectorImage
```
 
**描述**
 
运动矢量图像，可以为空。运动矢量的计算方式为当前渲染像素的NDC坐标的XY值减去其上一帧的NDC坐标的XY值。图像格式需要是VK_FORMAT_R16G16_SFLOAT或更高精度。保留字段，暂不支持。
 
  

#### inputNormalImage

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkImageView XEG_RTShadowAODescription::inputNormalImage
```
 
**描述**
 
法线图像，不能为空。需要是无符号浮点格式并包含3个以上通道，如VK_FORMAT_R8G8B8_UNORM。XEngine将按照Normal=textureLod(inputNormalImage).xyz*2.0–1.0的方式解析法线。
 
  

#### outputShadowAOImage

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
VkImageView XEG_RTShadowAODescription::outputShadowAOImage
```
 
**描述**
 
输出的阴影和环境光遮蔽图像，不能为空，格式必须为VK_FORMAT_R8G8_UNORM。阴影值将写入R通道，环境光遮蔽值将写入G通道。
 
  

#### pNext

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
const void* XEG_RTShadowAODescription::pNext
```
 
**描述**
 
指向扩展结构的指针。
 
  

#### projectionMatrix

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
float XEG_RTShadowAODescription::projectionMatrix[16]
```
 
**描述**
 
相机投影矩阵，必须是4*4列主序矩阵。
 
  

#### pRtAOParameters

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
const XEG_RTAOParameters* XEG_RTShadowAODescription::pRtAOParameters
```
 
**描述**
 
光线追踪环境光算法参数，当XEG_RTShadowAOCreateInfo::enableRTAO=true时不能为空。
 
  

#### pRtShadowAODenoiserParameters

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
const XEG_RTShadowAODenoiserParameters* XEG_RTShadowAODescription::pRtShadowAODenoiserParameters
```
 
**描述**
 
去噪参数，不能为空。光线追踪阴影和环境光遮蔽使用相同的去噪参数。
 
  

#### pRtShadowParameters

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
const XEG_RTShadowParameters* XEG_RTShadowAODescription::pRtShadowParameters
```
 
**描述**
 
光线追踪阴影算法参数，当XEG_RTShadowAOCreateInfo::enableRTShadow=true时不能为空。
 
  

#### sType

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
XEG_StructureType XEG_RTShadowAODescription::sType
```
 
**描述**
 
识别此结构的[XEG_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_RT_SHADOWAO_DESCRIPTION。
 
  

#### viewMatrix

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
float XEG_RTShadowAODescription::viewMatrix[16]
```
 
**描述**
 
相机观察矩阵，必须是4*4列主序矩阵。
 
  

#### worldCameraOrigin

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
float XEG_RTShadowAODescription::worldCameraOrigin[3]
```
 
**描述**
 
相机在世界空间中的位置坐标。
 
  

#### isAsInTranslatedSpace

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
bool XEG_RTShadowAODescription::isAsInTranslatedSpace = false;
```
 
**描述**
 
光线追踪加速结构是否在Translated世界空间构建。true表示在Translated世界空间构建，false表示在绝对世界空间构建。默认值为false。
 
  

#### translatedViewMatrix

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
float XEG_RTShadowAODescription::translatedViewMatrix[16];
```
 
**描述**
 
相机Translated观察矩阵，必须是4*4列主序矩阵。当isAsInTranslatedSpace值为false时可以不赋值。
 
  

#### ndcFlipY

**支持设备：** Phone | PC/2in1 | Tablet | TV

```text
bool XEG_RTShadowAODescription::ndcFlipY  = false;
```
 
**描述**
 
标识NDC空间与世界空间是否存在Y轴翻转关系。true表示翻转，false表示不翻转。默认值为false。
