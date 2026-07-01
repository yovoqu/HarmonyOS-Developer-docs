# Web页面点击响应慢

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-7

## Web页面点击响应慢
 


##### 问题现象

点击应用页面按钮或其他内容，等待一段时间后界面才有变化，响应慢。
 
 

##### 背景知识

- 点击响应时延：手指点击设备屏幕，到页面发生变化的时间。常见场景如点击应用页面按钮后显示弹窗或者加载动画等。
- [DevEco Profiler](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler)：提供实时监控（Realtime Monitor）能力和全方位的设备资源监测，支持系统事件、异常报告、CPU占用、内存占用、实时帧率、GPU使用率、能耗以及网络流量消耗等多个维度的数据分析。
- [DevTools](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-debugging-with-devtools)：Web前端开发调试工具，提供了电脑上调试移动设备前端页面的能力，利用DevTools工具可以分析Web组件加载页面的问题。

 
 

##### 问题定位

- 使用DevEco Studio Profiler的ArkWeb分析模板抓取该网页加载过程的Trace。响应时延类问题需要确定响应起止点。起点是应用收到手指离开屏幕事件时，可以通过查看UserEvents泳道或者应用主线程Trace点DispatchTouchEvent xxx type=1来确定。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/0LXqpK1pQoC5DL-7KNBDig/zh-cn_image_0000002658914283.png?HW-CC-KV=V1&HW-CC-Date=20260701T025513Z&HW-CC-Expire=86400&HW-CC-Sign=DA9AAC84330434F22536D59BBCBCE5F1F5463E83AA1FFE3657255C18A479072D)

 点击响应时延的终点为应用界面开始变化的时候，由于非连续不稳定的vsync信号不一定导致界面上的渲染行为，取终点为渲染服务render_service连续稳定渲染的第一帧vsync信号，如下图所示，可看到响应时间为875.9ms左右。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Ox2fxRDxSF6H8JRggToVzQ/zh-cn_image_0000002658794329.png?HW-CC-KV=V1&HW-CC-Date=20260701T025513Z&HW-CC-Expire=86400&HW-CC-Sign=07CA32714BEBF7FFF1A44CFAE29C9B4E1F319C877B9C4F212053F469898064EE)

 查看应用主线程运行状态，应用大部分时间处于Sleeping状态，未有持续长时间Running的情况。同时在上图render_service连续稳定渲染的第一帧vsync信号之前仅发现几帧vsync信号，UI绘制过程并没有高负载情况。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/ZFiFlCCrQB260MTHOyhm0A/zh-cn_image_0000002628554964.png?HW-CC-KV=V1&HW-CC-Date=20260701T025513Z&HW-CC-Expire=86400&HW-CC-Sign=738CD77D27456CD5E9909CD892E945030EE359FA544A5A2F3A1193CB0973AEC8)

 查看该过程CPU上运行的进程信息，发现运行时间较长的为lication:render、NetworkService、Chrome_IOThread，属于Web渲染、网络请求相关的线程，推测加载耗时主要在Web端。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/FjghR7zgSZSGnXM4gzvLEw/zh-cn_image_0000002628395064.png?HW-CC-KV=V1&HW-CC-Date=20260701T025513Z&HW-CC-Expire=86400&HW-CC-Sign=5EDB75075220F7684C372888F0B7E58CCA249DB3564D083A57E5311A1A0870A2)

- 使用DevTools工具抓取、分析该加载过程的性能，起点为点击操作，终点为界面发生变化的第一帧，如下图中可以看到从点击到页面变化的时间间隔为813ms左右。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/2LGObYcWQrWFEBjdXHPddA/zh-cn_image_0000002658914285.png?HW-CC-KV=V1&HW-CC-Date=20260701T025513Z&HW-CC-Expire=86400&HW-CC-Sign=9064666AB72F194244C72A36E305F913EF53FBDB0FE1DD2E93B9BADAFDFEED23)

 该过程耗时可能包含以下情况：
 
网络请求、网络资源下载耗时长：如上图例中，点击操作后应用首先进行安全认证的网络请求，该部分主要耗时集中在发送请求到收到响应部分（106ms）。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/RdmZ-6mbSaeaM8uq6wJLQg/zh-cn_image_0000002658794333.png?HW-CC-KV=V1&HW-CC-Date=20260701T025513Z&HW-CC-Expire=86400&HW-CC-Sign=1FD873C38C5EA6F5D323BA02E4F86343F4D359B5DDBE7506DCAF11518622E4E9)

 然后应用请求loginActivity页面，下载该页面的相关资源，该部分耗时380ms左右，主要耗时为与该页面的连接（134ms）、发送请求到收到响应（96ms），以及页面资源下载（147ms）。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/o9NOUeLQRTeVa-MGdgdJ0w/zh-cn_image_0000002628554966.png?HW-CC-KV=V1&HW-CC-Date=20260701T025513Z&HW-CC-Expire=86400&HW-CC-Sign=4B89A054FE75183FB4FED768CBF8D466E3461C005E066B6997EEFC758979B377)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/qfYd6ojPRVq6MYAQFXcMtg/zh-cn_image_0000002628395066.png?HW-CC-KV=V1&HW-CC-Date=20260701T025513Z&HW-CC-Expire=86400&HW-CC-Sign=0024EF5BA7FD0F7A85DD3EAC1D993058ABA207E68130E269983E311D7867BC53)

 最后应用请求loading.gif加载中图标资源并显示，该部分耗时169ms。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/b6X-8lpeTm6m-lA_LK8xng/zh-cn_image_0000002658914287.png?HW-CC-KV=V1&HW-CC-Date=20260701T025513Z&HW-CC-Expire=86400&HW-CC-Sign=7838D82E4717D1C0A3729BE1F1FEF03DD2E99651A0555EF4DED90A3D0A7567E2)

- JS代码运行耗时长：如下图中，网页处理点击事件时，JS代码get函数执行耗时较多（337.34ms），导致响应时间长。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/t1RySzoQSbuVm9ZVuk0RJw/zh-cn_image_0000002658794335.png?HW-CC-KV=V1&HW-CC-Date=20260701T025513Z&HW-CC-Expire=86400&HW-CC-Sign=FE13C241C38828D5302AF4DAE7DE4A8AB01E19BF378DEED0AC3500798F960E68)


 
 
 

##### 分析结论

导致Web页面点击响应慢的原因可能有：
 
- 网络请求、页面下载资源耗时较长。
- JS代码运行耗时长。

 
 

##### 修改建议

- [预下载优化](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-develop-optimization#section11708113212514)。
- 优化JS代码逻辑。
