# Web页面点击响应慢

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-7

#### 问题现象

点击应用页面按钮或其他内容，等待一段时间后界面才有变化，响应慢。
 
 

#### 背景知识

- 点击响应时延：手指点击设备屏幕，到页面发生变化的时间。常见场景如点击应用页面按钮后显示弹窗或者加载动画等。
- [DevEco Profiler](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler)：提供实时监控（Realtime Monitor）能力和全方位的设备资源监测，支持系统事件、异常报告、CPU占用、内存占用、实时帧率、GPU使用率、能耗以及网络流量消耗等多个维度的数据分析。
- [DevTools](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-debugging-with-devtools)：Web前端开发调试工具，提供了电脑上调试移动设备前端页面的能力，利用DevTools工具可以分析Web组件加载页面的问题。

 
 

#### 问题定位
1. 使用DevEco Studio Profiler的ArkWeb分析模板抓取该网页加载过程的Trace。响应时延类问题需要确定响应起止点。起点是应用收到手指离开屏幕事件时，可以通过查看UserEvents泳道或者应用主线程Trace点DispatchTouchEvent xxx type=1来确定。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/0LXqpK1pQoC5DL-7KNBDig/zh-cn_image_0000002658914283.png?HW-CC-KV=V1&HW-CC-Date=20260723T012410Z&HW-CC-Expire=86400&HW-CC-Sign=BD30AAD2B1D9AABCB1AECC082ADCEFF80C92A2E81B32FF571D126B7CC0F07D95)


  点击响应时延的终点为应用界面开始变化的时候，由于非连续不稳定的vsync信号不一定导致界面上的渲染行为，取终点为渲染服务render_service连续稳定渲染的第一帧vsync信号，如下图所示，可看到响应时间为875.9ms左右。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Ox2fxRDxSF6H8JRggToVzQ/zh-cn_image_0000002658794329.png?HW-CC-KV=V1&HW-CC-Date=20260723T012410Z&HW-CC-Expire=86400&HW-CC-Sign=47F9FAA4F19E6006A6A6B0A3106805D7FA7EEEF8B7B1B8BCB3C3D993F1E2BAD5)


  查看应用主线程运行状态，应用大部分时间处于Sleeping状态，未有持续长时间Running的情况。同时在上图render_service连续稳定渲染的第一帧vsync信号之前仅发现几帧vsync信号，UI绘制过程并没有高负载情况。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/ZFiFlCCrQB260MTHOyhm0A/zh-cn_image_0000002628554964.png?HW-CC-KV=V1&HW-CC-Date=20260723T012410Z&HW-CC-Expire=86400&HW-CC-Sign=21E1B56CCDFF6BB488DF2B6FBD78A73670523F4C79C976854F3F04FFA579F94D)


  查看该过程CPU上运行的进程信息，发现运行时间较长的为lication:render、NetworkService、Chrome_IOThread，属于Web渲染、网络请求相关的线程，推测加载耗时主要在Web端。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/FjghR7zgSZSGnXM4gzvLEw/zh-cn_image_0000002628395064.png?HW-CC-KV=V1&HW-CC-Date=20260723T012410Z&HW-CC-Expire=86400&HW-CC-Sign=B4957C6C5139B2A6A4FBC4F8E64C08191F105E4703B3EFE4E039692519E78159)

2. 使用DevTools工具抓取、分析该加载过程的性能，起点为点击操作，终点为界面发生变化的第一帧，如下图中可以看到从点击到页面变化的时间间隔为813ms左右。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/2LGObYcWQrWFEBjdXHPddA/zh-cn_image_0000002658914285.png?HW-CC-KV=V1&HW-CC-Date=20260723T012410Z&HW-CC-Expire=86400&HW-CC-Sign=6CEBBC8CCD335DCD4ACAA9CB15BE02C61DE2676D2383E1084B91D9608A9803A1)


  该过程耗时可能包含以下情况：

  
- 网络请求、网络资源下载耗时长：如上图例中，点击操作后应用首先进行安全认证的网络请求，该部分主要耗时集中在发送请求到收到响应部分（106ms）。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/RdmZ-6mbSaeaM8uq6wJLQg/zh-cn_image_0000002658794333.png?HW-CC-KV=V1&HW-CC-Date=20260723T012410Z&HW-CC-Expire=86400&HW-CC-Sign=5C374FF03B90D4D3FDB88F80D4518C22C99D7C157CF2D4BDA4C24619569EF4C8)


  然后应用请求loginActivity页面，下载该页面的相关资源，该部分耗时380ms左右，主要耗时为与该页面的连接（134ms）、发送请求到收到响应（96ms），以及页面资源下载（147ms）。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/o9NOUeLQRTeVa-MGdgdJ0w/zh-cn_image_0000002628554966.png?HW-CC-KV=V1&HW-CC-Date=20260723T012410Z&HW-CC-Expire=86400&HW-CC-Sign=ECF4D041B5628242A0B8EE0C7453FC68D4F9E9E1644F491A3968DA53DD1BDA65)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/qfYd6ojPRVq6MYAQFXcMtg/zh-cn_image_0000002628395066.png?HW-CC-KV=V1&HW-CC-Date=20260723T012410Z&HW-CC-Expire=86400&HW-CC-Sign=1BDEEE020215700312AA6DA35FFCC0127B15231EC519F4AE18EED353BFC5DEAD)


  最后应用请求loading.gif加载中图标资源并显示，该部分耗时169ms。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/b6X-8lpeTm6m-lA_LK8xng/zh-cn_image_0000002658914287.png?HW-CC-KV=V1&HW-CC-Date=20260723T012410Z&HW-CC-Expire=86400&HW-CC-Sign=2745A27533C39276A7B3BB868480ECB39F6CD482BE9E00C3851C9D2012950F34)


3. JS代码运行耗时长：如下图中，网页处理点击事件时，JS代码get函数执行耗时较多（337.34ms），导致响应时间长。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/t1RySzoQSbuVm9ZVuk0RJw/zh-cn_image_0000002658794335.png?HW-CC-KV=V1&HW-CC-Date=20260723T012410Z&HW-CC-Expire=86400&HW-CC-Sign=D5FF6C98D7DFE3EFE07B41B1E0070B64615E6F9CF7E15A7CAC66F88AB605AB80)


  

  #### 分析结论

  导致Web页面点击响应慢的原因可能有：

  
网络请求、页面下载资源耗时较长。
- JS代码运行耗时长。

 
 

#### 修改建议

- [预下载优化](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-develop-optimization#section11708113212514)。
- 优化JS代码逻辑。
