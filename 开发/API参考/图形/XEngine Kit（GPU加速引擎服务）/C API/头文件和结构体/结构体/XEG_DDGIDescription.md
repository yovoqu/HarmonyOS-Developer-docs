# XEG_DDGIDescription

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgidescription
**支持设备：** Phone | PC/2in1 | Tablet | TV

##### 概述

此结构体描述更新DDGI探针辐照度及渲染输出GI图像所需的信息。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)
 
**所在头文件：** [xeg_vulkan_rtgi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rtgi-8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| XEG_StructureType sType | 识别此结构的XEG_StructureType值，必须是XEG_STRUCTURE_TYPE_DDGI_DESCRIPTION。 |
| const void * pNext | 指向扩展结构的指针。 |
| float viewMatrix [16] | 相机观察矩阵，必须是4*4列主序矩阵。 |
| float projectionMatrix [16] | 相机投影矩阵，必须是4*4列主序矩阵。 |
| VkImageView inputNormalImage | 输入Gbuffer法向量图像，其宽高必须和XEG_DDGICreateInfo中viewSize的宽高保持一致。 |
| VkImageView inputDepthImage | 输入Gbuffer深度图像，其宽高必须和XEG_DDGICreateInfo中viewSize的宽高保持一致。 |
| VkImageView inputBasecolorMetallicImage | 输入Gbuffer基础颜色和金属度图像，其宽高必须和XEG_DDGICreateInfo中viewSize的宽高保持一致。 |
| VkImageView inputDirectionImage | 输入探针发射光线方向图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkImageView inputRayRadianceDistanceImage | 输入探针发射光线交点的辐射率及距离图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkImageView inputRayHitNormalAndMetallicImage | 输入探针发射光线交点的法向量及金属度图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkBuffer inputVolumeIndexAndProbeIndex | 输入探针的索引信息，对应于探针发射光线的信息，每个数据为两个uint值（探针索引/体积索引）。 |
| uint32_t inputProbeCount | 输入探针数量，对应于inputVolumeIndexAndProbeIndex中的有效数据个数。 |
| VkBuffer outputVolumeIndexAndProbeIndex | 输出探针的索引信息，指示用户下一帧如何发射光线，每个数据为两个uint值（探针索引/体积索引）。 |
| VkBuffer outputProbeCount | 输出探针数量，对应于outputVolumeIndexAndProbeIndex中的有效数据个数。 |
| VkImageView outputGIImage | 输出GI 2D图像，其宽高必须和XEG_DDGICreateInfo中viewSize的宽高保持一致，VkFormat为VK_FORMAT_R8G8B8A8_UNORM。 |
| uint32_t enableVolumeNumber | 使用的体积数量，必须不大于XEG_DDGICreateInfo中的numberVolume值。 |
| const struct XEG_DDGIVolumeEntryParameters * pVolumeEntryParameters | 输入体积参数信息，对应于XEG_DDGIVolumeEntryParameters。该结构体数组的大小必须等于enableVolumeNumber的值。 |
 
 
  

##### 结构体成员变量说明

  

##### enableVolumeNumber

```text
uint32_t XEG_DDGIDescription::enableVolumeNumber
```
 
**描述**
 
使用的体积数量，必须不大于[XEG_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中的numberVolume值。
 
  

##### inputBasecolorMetallicImage

```text
VkImageView XEG_DDGIDescription::inputBasecolorMetallicImage
```
 
**描述**
 
输入Gbuffer基础颜色和金属度图像，其宽高必须和[XEG_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致。
 
  

##### inputDepthImage

```text
VkImageView XEG_DDGIDescription::inputDepthImage
```
 
**描述**
 
输入Gbuffer深度图像，其宽高必须和[XEG_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致。
 
  

##### inputDirectionImage

```text
VkImageView XEG_DDGIDescription::inputDirectionImage
```
 
**描述**
 
输入探针发射光线方向图像，其宽高分别为：探针发射光线数量，输入探针数量。
 
  

##### inputNormalImage

```text
VkImageView XEG_DDGIDescription::inputNormalImage
```
 
**描述**
 
输入Gbuffer法向量图像，其宽高必须和[XEG_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致。
 
  

##### inputProbeCount

```text
uint32_t XEG_DDGIDescription::inputProbeCount
```
 
**描述**
 
输入探针数量，对应于inputVolumeIndexAndProbeIndex中的有效数据个数。
 
  

##### inputRayHitNormalAndMetallicImage

```text
VkImageView XEG_DDGIDescription::inputRayHitNormalAndMetallicImage
```
 
**描述**
 
输入探针发射光线交点的法向量及金属度图像，其宽高分别为：探针发射光线数量，输入探针数量。
 
  

##### inputRayRadianceDistanceImage

```text
VkImageView XEG_DDGIDescription::inputRayRadianceDistanceImage
```
 
**描述**
 
输入探针发射光线交点的辐射率及距离图像，其宽高分别为：探针发射光线数量，输入探针数量。
 
  

##### inputVolumeIndexAndProbeIndex

```text
VkBuffer XEG_DDGIDescription::inputVolumeIndexAndProbeIndex
```
 
**描述**
 
输入探针的索引信息，对应于探针发射光线的信息，每个数据为两个uint值（探针索引/体积索引）。
 
  

##### outputGIImage

```text
VkImageView XEG_DDGIDescription::outputGIImage
```
 
**描述**
 
输出GI 2D图像，其宽高必须和[XEG_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致，VkFormat为VK_FORMAT_R8G8B8A8_UNORM。
 
  

##### outputProbeCount

```text
VkBuffer XEG_DDGIDescription::outputProbeCount
```
 
**描述**
 
输出探针数量，对应于outputVolumeIndexAndProbeIndex中的有效数据个数。
 
  

##### outputVolumeIndexAndProbeIndex

```text
VkBuffer XEG_DDGIDescription::outputVolumeIndexAndProbeIndex
```
 
**描述**
 
输出探针的索引信息，指示用户下一帧如何发射光线，每个数据为两个uint值（探针索引/体积索引）。
 
  

##### pNext

```text
const void* XEG_DDGIDescription::pNext
```
 
**描述**
 
指向扩展结构的指针。
 
  

##### projectionMatrix

```text
float XEG_DDGIDescription::projectionMatrix[16]
```
 
**描述**
 
相机投影矩阵，必须是4*4列主序矩阵。
 
  

##### pVolumeEntryParameters

```text
const struct XEG_DDGIVolumeEntryParameters* XEG_DDGIDescription::pVolumeEntryParameters
```
 
**描述**
 
输入体积参数信息，对应于[XEG_DDGIVolumeEntryParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgivolumeentryparameters)。该结构体数组的大小必须等于enableVolumeNumber的值。
 
  

##### sType

```text
XEG_StructureType XEG_DDGIDescription::sType
```
 
**描述**
 
识别此结构的[XEG_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG_STRUCTURE_TYPE_DDGI_DESCRIPTION。
 
  

##### viewMatrix

```text
float XEG_DDGIDescription::viewMatrix[16]
```
 
**描述**
 
相机观察矩阵，必须是4*4列主序矩阵。
