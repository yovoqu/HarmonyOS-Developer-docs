# UsbRequestPipe

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbrequestpipe
**支持设备：** PC/2in1


```text
typedef struct UsbRequestPipe {...} __attribute__((aligned(8))) UsbRequestPipe
```


## 概述
**支持设备：** PC/2in1

请求管道。

**起始版本：** 10

**相关模块：** [UsbDdk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk)

**所在头文件：** [usb_ddk_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usb-ddk-types-h)


## 汇总
**支持设备：** PC/2in1


### 成员变量
**支持设备：** PC/2in1


| 名称 | 描述 |
| --- | --- |
| uint64_t interfaceHandle | 接口操作句柄。 |
| uint8_t endpoint | 要通信的端点的地址。 |
| uint32_t timeout | 超时时间，单位是毫秒。 |
