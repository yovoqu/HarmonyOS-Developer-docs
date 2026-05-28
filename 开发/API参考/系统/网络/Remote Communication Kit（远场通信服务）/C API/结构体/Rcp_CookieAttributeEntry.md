# Rcp_CookieAttributeEntry

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

##### 概述

响应Cookie属性条目。
 
**起始版本：** 5.0.0(12)
 
**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)
 
**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)
 
  

##### 汇总

  

##### 成员变量
 
| 名称 | 描述 |
| --- | --- |
| const char * key | 键。 |
| const char * value | 值。 |
| struct Rcp_CookieAttributeEntry * next | 链式存储。指向下一个Rcp_CookieAttributeEntry的指针。 |
 
 
  

##### 结构体成员变量说明

  

##### key

```text
const char* Rcp_CookieAttributeEntry::key
```
 
**描述**
 
键。
 
  

##### next

```text
struct Rcp_CookieAttributeEntry* Rcp_CookieAttributeEntry::next
```
 
**描述**
 
链式存储。指向下一个[Rcp_CookieAttributeEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry)的指针。
 
  

##### value

```text
const char* Rcp_CookieAttributeEntry::value
```
 
**描述**
 
值。
