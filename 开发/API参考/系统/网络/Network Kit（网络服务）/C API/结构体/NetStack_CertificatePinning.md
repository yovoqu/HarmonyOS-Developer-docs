# NetStack_CertificatePinning

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificatepinning
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```text
typedef struct NetStack_CertificatePinning {...} NetStack_CertificatePinning
```


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

定义证书锁定信息。

**起始版本：** 12

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net_ssl_c_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [NetStack_CertificatePinningKind](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h#netstack_certificatepinningkind) kind | 证书锁定类型。 |
| [NetStack_HashAlgorithm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h#netstack_hashalgorithm) hashAlgorithm | 哈希算法。 |
| char *publicKeyHash | 哈希值。 |
