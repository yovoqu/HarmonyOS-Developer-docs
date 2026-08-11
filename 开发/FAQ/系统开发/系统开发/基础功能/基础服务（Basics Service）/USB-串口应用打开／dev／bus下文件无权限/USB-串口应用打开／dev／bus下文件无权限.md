# USB-串口应用打开/dev/bus下文件无权限

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-61

#### 问题现象

NAPI开发USB-串口应用（CH340转换），打开/dev/bus下文件提示Error: Permission denied。
 
 

#### 解决方案

/dev下文件的读写权限不对外开放，如果需要对设备操作，可以用[usbManager.getFileDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-usbmanager#usbmanagergetfiledescriptor)接口。
