# Rcp_Timeout

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___timeout
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

请求的超时配置。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| uint32_t connectMs | 连接超时时间。默认值为60000毫秒。 |
| uint32_t transferMs | 传输超时时间。默认值为60000毫秒。 |
 
 
  

##### 结构体成员变量说明

  

##### connectMs

```text
uint32_t Rcp_Timeout::connectMs
```
 
**描述**
 
连接超时时间。默认值为60000毫秒。
 
  

##### transferMs

```text
uint32_t Rcp_Timeout::transferMs
```
 
**描述**
 
传输超时时间。默认值为60000毫秒。
