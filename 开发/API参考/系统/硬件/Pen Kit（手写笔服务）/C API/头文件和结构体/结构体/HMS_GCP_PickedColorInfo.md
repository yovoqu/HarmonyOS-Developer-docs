# HMS_GCP_PickedColorInfo

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-struct-colorinfo
**支持设备：** Phone / PC/2in1 / Tablet


## 概述
**支持设备：** Phone / PC/2in1 / Tablet

定义取色颜色信息的结构体。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 5.0.0(12)

**相关模块：** [GlobalColorPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-c)

**所在头文件：** [native_gcp_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-headerfile-declare)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| [HMS_GCP_Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-struct-color) color | 提取的颜色值。 |
| [HMS_GCP_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-c#hms_gcp_colorspace) colorSpace | 颜色所属的颜色空间。 |
| int64_t [timestamp](#timestamp) | 提取颜色的时间戳。 |


## 结构体成员变量说明
**支持设备：** Phone / PC/2in1 / Tablet


### color
**支持设备：** Phone / PC/2in1 / Tablet


```text
HMS_GCP_Color HMS_GCP_PickedColorInfo::color
```

**描述**

提取的颜色值。


### colorSpace
**支持设备：** Phone / PC/2in1 / Tablet


```text
HMS_GCP_ColorSpace HMS_GCP_PickedColorInfo::colorSpace
```

**描述**

颜色所属的颜色空间。


### timestamp
**支持设备：** Phone / PC/2in1 / Tablet


```text
int64_t HMS_GCP_PickedColorInfo::timestamp
```

**描述**

提取颜色的时间戳。
