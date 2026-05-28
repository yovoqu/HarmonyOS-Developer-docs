# Rcp_Urls

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___urls
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

#### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

URLs，用于确定主机是否正在使用代理。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

#### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| const char * url | 匹配的URL。 |
| struct Rcp_Urls * next | 链式存储。指向下一个Rcp_Urls的指针。 |
 
 
  

#### 结构体成员变量说明

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

#### next

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct Rcp_Urls* Rcp_Urls::next
```
 
**描述**
 
链式存储。指向下一个[Rcp_Urls](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___urls)的指针。
 
  

#### url

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
const char* Rcp_Urls::url
```
 
**描述**
 
匹配的URL。
