# XEG_ExtensionProperties

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-extensionproperties
**支持设备：** Phone | PC/2in1 | Tablet | TV

##### 概述

此结构体描述通过[HMS_XEG_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)
 
**所在头文件：** [xeg_vulkan_extension.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-extension-8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| char extensionName [XEG_MAX_EXTENSION_NAME_SIZE] | XEngine支持的扩展特性名称。 |
| uint32_t version | XEngine支持的扩展特性版本号。 |
 
 
  

##### 结构体成员变量说明

  

##### extensionName

```text
char XEG_ExtensionProperties::extensionName[XEG_MAX_EXTENSION_NAME_SIZE]
```
 
**描述**
 
XEngine支持的扩展特性名称。
 
  

##### version

```text
uint32_t XEG_ExtensionProperties::version
```
 
**描述**
 
XEngine支持的扩展特性版本号。
