# Scan_PictureScanProgress

更新时间：2026-04-03 09:39:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-picturescanprogress
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct {...} Scan_PictureScanProgress
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

表示扫描仪扫描图片的进度
 
**起始版本：** 12
 
**相关模块：** [OH_Scan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan)
 
**所在头文件：** [ohscan.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohscan-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| int32_t progress | 图片的扫描进度，从0到100，单位：百分比。 |
| int32_t fd | 扫描仪文件句柄 |
| bool isFinal | 指示该图像是否为最后扫描的图像。true表示该图像是最后扫描的图像，false表示该图像不是最后扫描的图像。 |
