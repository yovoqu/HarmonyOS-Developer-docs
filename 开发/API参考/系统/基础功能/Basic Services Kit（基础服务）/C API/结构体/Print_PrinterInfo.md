# Print_PrinterInfo

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printerinfo
**支持设备：** Phone / PC/2in1 / Tablet


```text
typedef struct {...} Print_PrinterInfo
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet

表示打印机信息。

**起始版本：** 12

**相关模块：** [OH_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)

**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet


| 名称 | 描述 |
| --- | --- |
| [Print_PrinterState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h#print_printerstate) printerState | 打印机状态。 |
| [Print_PrinterCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printercapability) capability | 打印机能力。 |
| [Print_DefaultValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-defaultvalue) defaultValue | 打印机当前属性。 |
| bool isDefaultPrinter | 默认打印机。 |
| char *printerId | 打印机 ID。 |
| char *printerName | 打印机名称。 |
| char *description | 打印机描述。 |
| char *location | 打印机位置。 |
| char *makeAndModel | 打印机品牌和型号信息。 |
| char *printerUri | 打印机 URI。 |
| char *detailInfo | JSON 格式的详细信息。 |
