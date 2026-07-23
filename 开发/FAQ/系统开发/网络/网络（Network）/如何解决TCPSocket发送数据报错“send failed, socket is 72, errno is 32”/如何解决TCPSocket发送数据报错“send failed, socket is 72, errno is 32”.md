# 如何解决TCPSocket发送数据报错“send failed, socket is 72, errno is 32”

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-119

#### 问题现象

使用TCPSocket给打印机循环发送文件数据时中途报错：[socket_exec.cpp:2654] send failed, socket is 72, errno is 32，但是使用Debug方式一步一步的执行可以发送成功，如何解决？
 
 

#### 背景知识

应用使用TCP协议进行Socket通信需要了解以下流程：
 
1. import需要的Socket模块。
2. 创建一个TCPSocket连接，返回一个TCPSocket对象。
3. 订阅TCPSocket相关的订阅事件。
4. 绑定IP地址和端口，端口可以指定或由系统随机分配。
5. 连接到指定的IP地址和端口。
6. 发送数据。
7. Socket连接使用完毕后，主动关闭。
 

#### 问题定位

- 通过TCPDump日志分析是否对端主动关闭连接。
- 检查是否循环发送数据量过大导致服务端处理不过来。

 
 

#### 分析结论

通过抓取TCPDump日志进行分析，关键日志如下：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/cY7XY_H8SMK9GemTUvMQVA/zh-cn_image_0000002658850169.png?HW-CC-KV=V1&HW-CC-Date=20260723T013435Z&HW-CC-Expire=86400&HW-CC-Sign=911EB26873D079E09B28D60EA70A91C70B574091F41CACA8CBF559E61F749372)

 
结论如下：
 
- 在非Debug方式下，打印机主动发了一个RST，服务端主动关闭连接。
- 客户端已经发了大量的包，打印机还在应答前面的包，服务端处理不过来了。

 
 

#### 修改建议

- 减小每次发送的数据大小。
- 在每次发送完添加Sleep延时50毫秒避免数据堆积。
