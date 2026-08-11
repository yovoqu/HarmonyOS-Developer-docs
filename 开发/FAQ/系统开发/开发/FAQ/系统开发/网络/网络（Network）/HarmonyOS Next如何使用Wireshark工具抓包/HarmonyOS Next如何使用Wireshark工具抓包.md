# HarmonyOS Next如何使用Wireshark工具抓包

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-118

#### 问题现象

HarmonyOS Next手机上抓取tcpdump包（网络数据包）有可用的推荐工具吗？
 
 

#### 背景知识

Wireshark是全球主流的开源跨平台网络数据包分析工具，核心能力是实时捕获与深度解析网络流量，可透视网络通信细节，广泛用于排障、安全审计、协议调试与教学。遵循GPLv2协议，支持HarmonyOS/Windows/macOS/Linux等多系统。
 
局域网是将地理范围有限（几米～几千米）的多台计算机、终端设备（手机/平板/开发板/打印机等）通过有线/无线方式互联，形成的封闭型本地计算机网络，属于计算机网络的基础类型。电脑和手机组成局域网一般通过电脑开启热点，手机连接热点方式实现。
 
 

#### 解决方案
1. 下载并安装Wireshark软件；电脑开启热点，手机连接电脑热点，保证手机的请求转发到电脑；通过ipconfig命令查看对应的网络接口，示例中网络对应的本地连接10如下：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/9yCGuqpqSsOW9nJGoa0f1Q/zh-cn_image_0000002658850167.png?HW-CC-KV=V1&HW-CC-Date=20260811T005935Z&HW-CC-Expire=86400&HW-CC-Sign=1F42AFDC3C7B46D19E100C0E2C3419D6ED741CDDBB600C531647B6DEDB771064)

2. 根据当前手机连接的局域网设置捕获的网络接口；具体设置的路径为捕获-选项-勾选具体的网络接口，例如本次选择的是本地连接10。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/mjYeoHNnT-Kt0kqQxzdQ9A/zh-cn_image_0000002628610908.png?HW-CC-KV=V1&HW-CC-Date=20260811T005935Z&HW-CC-Expire=86400&HW-CC-Sign=4219A4E444C85830A67B5694963E6AF2C3B97B4758D5BE1BDFB7EB7EF726B056)

3. 点击开始捕获分组。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/U7yTb33hSMiTg5gSWBteYQ/zh-cn_image_0000002628770802.png?HW-CC-KV=V1&HW-CC-Date=20260811T005935Z&HW-CC-Expire=86400&HW-CC-Sign=5D9BC0D88108E1982458CF5CC65B7D7A066F234FB7782EF4AF03114DDC364B9F)

4. 操作App复现问题，可以查看Wireshark的包列表区和包内容细节区。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/yjfUDioQToSX9cy6UZAC1g/zh-cn_image_0000002658970125.png?HW-CC-KV=V1&HW-CC-Date=20260811T005935Z&HW-CC-Expire=86400&HW-CC-Sign=4C489E8E78818EFBEA7BFFB12E5A56A52BBE26A9DB36190E8DC70A429CF984EE)

5. 保存生成的tcpdump包文件；具体路径为文件-保存（另存为），即可生成后缀名为pcapng的文件。
