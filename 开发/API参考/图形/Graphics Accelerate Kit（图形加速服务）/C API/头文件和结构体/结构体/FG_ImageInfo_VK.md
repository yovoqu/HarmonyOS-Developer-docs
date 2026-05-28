# FG_ImageInfo_VK

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_info___v_k
**支持设备：** Phone | Tablet | TV

#### 概述

**支持设备：** Phone | Tablet | TV

此结构体描述超帧输入输出图像信息。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)
 
**所在头文件：** [frame_generation_vk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__vk_8h)
 
  

#### 汇总

**支持设备：** Phone | Tablet | TV

  

#### 成员变量

**支持设备：** Phone | Tablet | TV
 
| 名称 | 描述 |
| --- | --- |
| FG_Image_VK* image | 超帧输入输出图像结构体FG_Image_VK对象的指针，该图像实例需要通过HMS_FG_CreateImage_VK进行创建，通过HMS_FG_DestroyImage_VK进行销毁。 |
| FG_ImageSync_VK initialSync | HMS_FG_Dispatch_VK执行前，该图像的同步状态。 |
| FG_ImageSync_VK finalSync | HMS_FG_Dispatch_VK执行后，该图像的同步状态。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | Tablet | TV

  

#### finalSync

**支持设备：** Phone | Tablet | TV

```text
FG_ImageSync_VK FG_ImageInfo_VK::finalSync
```
 
**描述**
 
[HMS_FG_Dispatch_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_dispatch_vk)执行后，该图像的同步状态。
 
  

#### image

**支持设备：** Phone | Tablet | TV

```text
FG_Image_VK* FG_ImageInfo_VK::image
```
 
**描述**
 
超帧输入输出图像结构体[FG_Image_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_image_vk)对象的指针，该图像实例需要通过[HMS_FG_CreateImage_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_createimage_vk)进行创建，通过[HMS_FG_DestroyImage_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_destroyimage_vk)进行销毁。
 
  

#### initialSync

**支持设备：** Phone | Tablet | TV

```text
FG_ImageSync_VK FG_ImageInfo_VK::initialSync
```
 
**描述**
 
[HMS_FG_Dispatch_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_dispatch_vk)执行前，该图像的同步状态。
