# Native调试启动加速

更新时间：2026-06-12 06:54:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-lldb-client-alive

在大型工程中，Native调试的启动耗时较长。为提升开发调试效率，从26.0.0 Beta1版本开始，新增Native调试启动加速功能。开启该功能后，首次调试完成时，调试服务器会保持活跃状态，后续再次启动调试时，可以大幅减少调试连接的耗时。
 

#### 使用约束

- 该配置是工程级配置，每个工程需要单独开启。
- 同一个工程中，同时创建多个Native调试会话，该加速功能只对第一个调试会话有效。

 
 

#### 操作步骤

在**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Debugger > C++ Debugger**中，勾选**Keep LLDB client alive**开启Native调试启动加速功能。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/7Ls9ogOMSo2Q5chFW6vUOg/zh-cn_image_0000002625074119.png?HW-CC-KV=V1&HW-CC-Date=20260701T041508Z&HW-CC-Expire=86400&HW-CC-Sign=C481105D7503EBE9612901DF42ABB71C4C2CCB1A8C6EC952C802E4BCB694749A)

 
也可以通过调试窗口控制台的超链接跳转到设置中开启。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/CQncBwkLQ5uMzGDCIV7x-Q/zh-cn_image_0000002594634538.png?HW-CC-KV=V1&HW-CC-Date=20260701T041508Z&HW-CC-Expire=86400&HW-CC-Sign=6985E4212F9443B2F39C6343C92BBA9F30AFC549DCD304DBF0F1A63221939F25)

 
开启开关并启动调试后，DevEco Studio底部会有调试服务器图标，调试过程中不能关闭服务器。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/ABJ1aZxrQCi6r0rirPnu8g/zh-cn_image_0000002624993977.png?HW-CC-KV=V1&HW-CC-Date=20260701T041508Z&HW-CC-Expire=86400&HW-CC-Sign=2F321E96FFA4D29BC03C49680621D907ABAF806473B642D854BBB5B579BDF49D)

 
同时，开启开关后会占用内存和磁盘空间，在不调试时，可手动释放资源。
 
- 释放内存：点击DevEco Studio底部的调试服务器图标，关闭调试服务器释放内存。
- 释放磁盘空间：点击**File >**** Invalidate Caches**，勾选**Clear LLDB caches**，点击**Invalidate and Restart**重启DevEco Studio以清理缓存数据。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/APfNxWuGR4y6DJ9-gP_5VA/zh-cn_image_0000002594474616.png?HW-CC-KV=V1&HW-CC-Date=20260701T041508Z&HW-CC-Expire=86400&HW-CC-Sign=F1C9528CA1D032DF5884E5EA2CC244B155E75AF1509C9B0EF0C9EA9872E71F8D)
