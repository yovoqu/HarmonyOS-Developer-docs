# Print_PrinterInfo

更新时间：2026-06-09 02:58:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printerinfo
**支持设备：** Phone | PC/2in1 | Tablet

```text
typedef struct {...} Print_PrinterInfo
```
  

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet

表示打印机信息。
 
**起始版本：** 12
 
**相关模块：** [OH_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)
 
**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet
 
| 名称 | 描述 |
| --- | --- |
| Print_PrinterState printerState | 打印机状态。 |
| Print_PrinterCapability capability | 打印机能力。 |
| Print_DefaultValue defaultValue | 打印机当前属性。 |
| bool isDefaultPrinter | 默认打印机。 |
| char *printerId | 打印机 ID。 |
| char *printerName | 打印机名称。 |
| char *description | 打印机描述。 |
| char *location | 打印机位置。 |
| char *makeAndModel | 打印机品牌和型号信息。 |
| char *printerUri | 打印机 URI。 |
| char *detailInfo | JSON 格式的详细信息。 支持的键包括： - printerAlias：string类型，表示打印机别名，起始版本： 24。 - vendorId：int类型，表示USB打印机的VID，起始版本： 12。 - productId：int类型，表示USB打印机的PID，起始版本： 12。 - protocol：string数组，表示探测到的打印机支持的协议列表，起始版本： 24。 - ipp：string类型，表示探测到的IPP协议对应的打印机URI，起始版本： 24。 - ipps：string类型，表示探测到的IPPS协议对应的打印机URI，起始版本： 24。 - lpd：string类型，表示探测到的LPD协议对应的打印机URI，起始版本： 24。 - socket：string类型，表示探测到的Socket协议对应的打印机URI，起始版本： 24。 |
