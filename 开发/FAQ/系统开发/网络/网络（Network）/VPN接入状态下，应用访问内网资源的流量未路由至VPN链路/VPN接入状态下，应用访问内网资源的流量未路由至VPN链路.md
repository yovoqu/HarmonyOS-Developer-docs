# VPN接入状态下，应用访问内网资源的流量未路由至VPN链路

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-135

#### 问题现象

应用请求为外网服务时，请求走VPN网络；应用请求为内网时，请求不走VPN网络。
 
 

#### 背景知识

- 路由的概念：路由起到请求转发的作用，将应用的请求转发至VPN虚拟网卡转发或者物理网卡。路由在VPN中的位置：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/0j8p-cHIRli76piWNlcZDg/zh-cn_image_0000002628611264.png?HW-CC-KV=V1&HW-CC-Date=20260730T072552Z&HW-CC-Expire=86400&HW-CC-Sign=5535DC02E69F0053C2113BFD178B9A6802A3BCA963623099D8FC9610E13131B7)

- 默认路由: 所有未匹配到其它路由流量的兜底出口；在VPN网络未配置路由时，所有的流程都会走VPN隧道。IPv4默认路由为0.0.0.0/0；IPv6默认路由为::/0。
- VPN路由的分类：全隧道模式和分流路由。1. 全隧道模式：客户端默认路由（0.0.0.0/0）指向VPN网关，所有流量（包括上网、访问内网）都走VPN。

2. 分流路由：仅让特定目标流量走VPN，其余流量走本地默认路由。

 
 

#### 问题定位

1. 网络的主要配置信息如下：

| 名称 | IP地址 |

| --- | --- |

| 本地设备IP | 192.xxx.x.9 |

| 默认网关 | 192.xxx.x.1 |

| 路由1 | 192.xxx.x.10 |

| 路由2 | 182.xx.xxx.108 |

| 虚拟网卡地址 | 10.x.x.5 |
2. WireShark条件搜索ip.src == 182.xx.xxx.108 && ip.dst == 10.x.x.5，表示搜索从182.xx.xxx.108路由到10.x.x.5网卡的流量，说明应用的外网请求通过VPN网络转发。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/KsHJPdhLTfqciBBxEBRmxQ/zh-cn_image_0000002658850527.png?HW-CC-KV=V1&HW-CC-Date=20260730T072552Z&HW-CC-Expire=86400&HW-CC-Sign=BCF8E518E5BB5708F160E8C6F69876889D7517F2916671A8BD644E0F065D060D)

3. WireShark条件搜索ip.src == 192.xxx.x.10 && ip.dst == 10.x.x.5，表示搜索从192.xxx.x.10路由到10.x.x.5网卡的流量，说明应用的内网请求不通过VPN网络转发，直接走内网的路由规则。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/GbmWDC6UQMOFv8CvQXjc3g/zh-cn_image_0000002628771156.png?HW-CC-KV=V1&HW-CC-Date=20260730T072552Z&HW-CC-Expire=86400&HW-CC-Sign=42483DC53094CFFF6B77E8DD59C11DF6F87F64D288AD302D092381915C2E1480)

 

#### 分析结论

内网路由优先级默认高于VPN路由导致内网流量不走VPN网络。
 
 

#### 修改建议

方案1：避免网段重叠，内网和VPN网段尽量不重叠，比如内网用192.xxx.x.0/24网段，VPN用10.x.x.0/24网段。
 
方案2：最长前缀匹配，通过设置某个网段的掩码越长路由优先级越高，比如VPN网段为192.xxx.x.10/32的掩码长度32比内网网段192.xxx.x.0/23的掩码长度23大，能够保证前者的路由优先级比后者大。
 
 

#### 常见FAQ

Q：HarmonyOS系统如何查看设备路由规则？
 
A：连接设备后，执行hdc shell netstat -r；其中Destination表示下一跳路由。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/gU4Xm-fKRX-n3fqpoSkpTw/zh-cn_image_0000002658970479.png?HW-CC-KV=V1&HW-CC-Date=20260730T072552Z&HW-CC-Expire=86400&HW-CC-Sign=FB7AA7CE84395D1CEA327F35C5CABFB324E211404DFF32C0C42FC05CA3CC7153)

 
 

#### 总结

VPN网络访问问题通常需要使用网络包工具分析TcpDump包进行定位定界；根据数据包日志可以定位网络请求是否经过VPN网络，达到网络问题定位定界能力。
