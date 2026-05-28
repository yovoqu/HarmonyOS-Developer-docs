# NetStack_CertBlob

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certblob
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
struct NetStack_CertBlob {...}
```
  

##### 概述

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

证书数据结构体。
 
**起始版本：** 11
 
**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)
 
**所在头文件：** [net_ssl_c_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h)
 
  

##### 汇总

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

  

##### 成员变量

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV
 
| 名称 | 描述 |
| --- | --- |
| enum NetStack_CertType type | 证书类型。 |
| uint32_t size | 证书内容长度。 |
| uint8_t *data | 证书内容。 |
