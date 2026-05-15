# Rcp_IpAndPort

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_and_port
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

该接口用在[Rcp_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)中，表示一个DNS服务器的地址和端口。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)


## 汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### 成员变量
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| char [ip](#ip) [[RCP_IP_MAX_LEN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_ip_max_len)] | IPv4或IPv6地址。 |
| uint16_t [port](#port) | 表示端口。取值范围：[0, 65535]。 |


## 结构体成员变量说明
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


### ip
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
char Rcp_IpAndPort::ip[RCP_IP_MAX_LEN]
```

**描述**

IPv4或IPv6地址。


### port
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


```cpp
uint16_t Rcp_IpAndPort::port
```

**描述**

表示端口。取值范围：[0, 65535]。
