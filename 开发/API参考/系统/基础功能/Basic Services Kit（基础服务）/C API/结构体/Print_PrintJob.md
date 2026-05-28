# Print_PrintJob

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printjob
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct {...} Print_PrintJob
```
  

##### 概述

表示打印任务结构体。
 
**起始版本：** 12
 
**相关模块：** [OH_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)
 
**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char *jobName | 任务名称。 |
| uint32_t *fdList | 待打印的文件描述符数组。 |
| uint32_t fdListCount | 待打印的文件描述符数量。 |
| char *printerId | 打印机 ID。 |
| uint32_t copyNumber | 打印份数。 |
| char *paperSource | 纸张来源。 |
| char *mediaType | 介质类型。 |
| char *pageSizeId | 纸张尺寸 ID。 |
| Print_ColorMode colorMode | 色彩模式。 |
| Print_DuplexMode duplexMode | 双面模式。 |
| Print_Resolution resolution | 以 dpi 为单位的打印分辨率。 |
| Print_Margin printMargin | 打印边距。 |
| bool borderless | 无边距。 |
| Print_OrientationMode orientationMode | 方向模式。 |
| Print_Quality printQuality | 打印质量。 |
| Print_DocumentFormat documentFormat | 文档格式。 |
| char *advancedOptions | JSON 格式的高级选项。 支持的键包括： - isReverse：布尔类型，表示是否逆序打印。 - isCollate：布尔类型，表示是否逐份打印。 |
