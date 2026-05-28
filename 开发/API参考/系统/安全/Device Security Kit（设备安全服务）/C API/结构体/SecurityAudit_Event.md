# SecurityAudit_Event

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityaudit-event
**支持设备：** PC/2in1

##### 概述

**支持设备：** PC/2in1

定义审计事件信息。
 
**起始版本：** 6.0.0(20)
 
**相关模块：** [SecurityAudit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit)
 
**所在头文件：** [security_audit.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-security-audit-8h)
 
  

##### 汇总

**支持设备：** PC/2in1

  

##### 成员变量

**支持设备：** PC/2in1
 
| 名称 | 描述 |
| --- | --- |
| int64_t eventId | 审计事件ID。 |
| const char * metadata | 集成了事件版本号、事件接收时间、设备ID和用户ID的json字符串。 |
| const char * content | 事件内容。 |
 
 
  

##### 结构体成员变量说明

**支持设备：** PC/2in1

  

##### content

**支持设备：** PC/2in1

```text
const char* SecurityAudit_Event::content
```
 
**描述**
 
事件内容。
 
  

##### eventId

**支持设备：** PC/2in1

```text
int64_t SecurityAudit_Event::eventId
```
 
**描述**
 
审计事件ID。
 
  

##### metadata

**支持设备：** PC/2in1

```text
const char* SecurityAudit_Event::metadata
```
 
**描述**
 
集成了事件版本号、事件接收时间、设备ID和用户ID的json字符串。
