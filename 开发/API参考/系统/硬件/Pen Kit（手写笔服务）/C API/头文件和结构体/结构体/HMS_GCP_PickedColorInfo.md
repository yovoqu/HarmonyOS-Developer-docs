# HMS_GCP_PickedColorInfo

更新时间：2026-05-18 03:44:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-struct-colorinfo
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

定义取色颜色信息的结构体。
 
**系统能力：** SystemCapability.Stylus.ColorPicker
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [GlobalColorPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-c)
 
**所在头文件：** [native_gcp_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-headerfile-declare)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| HMS_GCP_Color color | 提取的颜色值。 |
| HMS_GCP_ColorSpace colorSpace | 颜色所属的颜色空间。 |
| int64_t timestamp | 提取颜色的时间戳。 |
 
 
  

##### 结构体成员变量说明

  

##### color

```text
HMS_GCP_Color HMS_GCP_PickedColorInfo::color
```
 
**描述**
 
提取的颜色值。
 
  

##### colorSpace

```text
HMS_GCP_ColorSpace HMS_GCP_PickedColorInfo::colorSpace
```
 
**描述**
 
颜色所属的颜色空间。
 
  

##### timestamp

```text
int64_t HMS_GCP_PickedColorInfo::timestamp
```
 
**描述**
 
提取颜色的时间戳，单位为ms。
