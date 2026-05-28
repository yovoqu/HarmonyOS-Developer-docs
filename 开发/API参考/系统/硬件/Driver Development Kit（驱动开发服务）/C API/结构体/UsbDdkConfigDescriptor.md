# UsbDdkConfigDescriptor

更新时间：2026-04-28 03:31:56

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbddkconfigdescriptor
**支持设备：** PC/2in1

```text
typedef struct UsbDdkConfigDescriptor {...} UsbDdkConfigDescriptor
```
  

##### 概述

**支持设备：** PC/2in1

配置描述符。
 
**起始版本：** 10
 
**相关模块：** [UsbDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk)
 
**所在头文件：** [usb_ddk_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-ddk-types-h)
 
  

##### 汇总

**支持设备：** PC/2in1

  

##### 成员变量

**支持设备：** PC/2in1
 
| 名称 | 描述 |
| --- | --- |
| struct UsbConfigDescriptor configDescriptor | 标准配置描述符。 |
| struct UsbDdkInterface* interface | 该配置所包含的接口。 |
| const uint8_t* extra | 未做解析的描述符，包含特定于类或供应商的描述符。 |
| uint32_t extraLength | 未做解析的描述符长度。 |
