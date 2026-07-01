# flutter页面滑动卡顿

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-1

## flutter页面滑动卡顿
 


##### 问题现象

用户滑动应用页面查看当前不可见的内容时，出现页面滑动卡顿的现象。
 
 

##### 背景知识

- 屏幕刷新率：显示设备每秒钟更新屏幕内容的次数，这决定了Vsync信号周期，120Hz对应8.33ms，90Hz对应11.11ms，60Hz对应16.67ms。
- Vsync信号：垂直同步信号，设备的屏幕通过固定频率发送Vsync信号来控制每一帧绘制操作的时机。
- Flutter页面是使用Flutter框架开发的应用程序中的一个独立显示区域或屏幕，可包含各种用户界面元素如按钮、文本框、列表等。Flutter页面绘制大致如下：
 
多模输入模块收到点击、滑动事件，上报传递给应用。
- 应用收到触摸事件，将事件发送给ui线程。
- ui线程收到触摸事件后，比较事件相关的坐标值，滑动距离超过预设阈值时触发滑动动效，申请新一帧绘制，在新一帧绘制中计算页面元素坐标、位置生成图层树，发送给raster线程。
- raster线程收到图层树，将其转换成平台可执行的GPU指令提交给GPU渲染。

  
| 关键线程名 | 说明 |
| --- | --- |
| ui线程 | 负责执行Dart代码中的UI相关操作，其会根据UI界面的描述生成UI界面的绘制指令（图层树），并将图层树发送到raster线程以在设备上渲染。 |
| raster线程 | 从ui线程获取图层树，将其转换成平台可执行的GPU指令并提交给GPU。 |
| io线程 | 负责处理与I/O相关的任务，如图片编解码、读写文件等。 |
 
 - DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，更多内容可看[使用Profiler进行性能调优](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-introduction)。使用DevEco Profiler提供的[Frame](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-frame)场景分析能力可分析卡顿丢帧问题。Flutter页面滑动卡顿相关Trace点：
  
| 流程 | 所在线程/泳道 | Trace关键字 |
| --- | --- | --- |
| 多模输入模块收到点击、滑动事件上报 | mmi_service | H:originEventHandle code: |
| 应用收到点击、滑动事件 | 应用主线程 | H:DispatchTouchEvent |
| 应用收到屏幕触摸事件 | H:touchEventDispatch | H:touchEventDispatch |
| 应用将触摸事件发送给Flutter ui线程 | 应用主线程 | H:flutter::Shell::OnPlatformViewDispatchPointerDataPacket |
| Flutter ui线程收到触摸事件 | ui | H:flutter::Engine::DispatchPointerDataPacket |
| 请求新一帧绘制 | ui | H:flutter::Animator::RequestFrame |
| 开始一帧绘制，生成图层树 | ui | H:flutter::Animator::BeginFrame frame_number: |
| 将图层树转换成平台可执行的GPU指令，提交给GPU | raster | H:flutter::GPURasterizer::Draw |
| 获取Flutter渲染帧数据，合成渲染树上各节点图层 | render_service | H:RSMainThread::DoComposition |
| GPU执行绘制 | RSUniRenderThre | H:RenderFrame |
| GPU渲染完成，提交渲染结果到显示硬件 | RSHardwareThrea | H:RSHardwareThread::CommitAndReleaseLayers |

 
 

##### 问题定位

- **场景一**：以某应用Flutter页面滑动卡顿为例，定位过程如下：
 
使用Profiler Frame分析能力抓取该过程的Trace信息，根据H:touchEventDispatch泳道的Trace点找到页面滑动的过程，并点击Frame泳道下的子泳道Display Vsync可看到该过程的屏幕刷新率为119，Flutter页面各线程的单帧处理时间需控制在8.3ms以内，否则会出现滑动卡顿的问题。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/hrGu9pQqS6qkqeKJ2PWwow/zh-cn_image_0000002658914251.png?HW-CC-KV=V1&HW-CC-Date=20260701T025512Z&HW-CC-Expire=86400&HW-CC-Sign=16E6B71AFC2E8405780104C76AD781430D2D3F60D60C01700124593A75A3AB6A)

- 查看页面滑动附近ui线程的Trace信息，发现ui线程在进行绘制时耗时较长，平均一帧绘制耗时达到39ms左右，远远超出了8.3ms。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/uTm1J9jOSh-EBDKBmF9DoA/zh-cn_image_0000002658794299.png?HW-CC-KV=V1&HW-CC-Date=20260701T025512Z&HW-CC-Expire=86400&HW-CC-Sign=B093C1E9357788BBC94161762A1161D3F23A9148880D5DF7CAD07DE1020D050E)

- 在Callstack泳道的ui[65405]子泳道中查看ui线程单帧绘制时的调用栈，发现耗时主要集中在libapp.so文件，该文件是由应用Dart业务代码打包生成的，因此此处耗时与应用业务逻辑有关。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/OKOi5wrBQM2QMs_LXMzvsg/zh-cn_image_0000002628554936.png?HW-CC-KV=V1&HW-CC-Date=20260701T025512Z&HW-CC-Expire=86400&HW-CC-Sign=38644C3B17B5E5A62D1CF62A13B3CAD44484C80D3F67B29544E85EBEA20AAA19)


 - **场景二**：以某应用Flutter页面滑动丢帧为例，定位过程如下：
 
使用Profiler Frame分析能力抓取该过程的Trace信息，根据H:oh_flutter_1Surface和VSyncGenerator泳道找到页面滑动丢帧的具体位置。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/L6x65b8bQBykEnng8N3ROA/zh-cn_image_0000002628395036.png?HW-CC-KV=V1&HW-CC-Date=20260701T025512Z&HW-CC-Expire=86400&HW-CC-Sign=0219EB9E2D137B134EA896A05D19B124FE574791CC032D21FD0CD649A48F200E)

- 在应用包名泳道中找到ui、raster线程，在render_service泳道中找到render_service、RSUniRenderThre子泳道。依次排列后可以看到信号传递过程，发现中间存在丢帧现象。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/lwwzWZiBTkS3rHPCFE36rg/zh-cn_image_0000002658914253.png?HW-CC-KV=V1&HW-CC-Date=20260701T025512Z&HW-CC-Expire=86400&HW-CC-Sign=6796C06BC68F6F3682AFD59A9CC044D9BFB600284999E1AAA71FCCD09326D824)

- 向下继续找到ui、raster对应的泳道，可以看到由位置1到位置2，ui线程和raster线程总计耗时超过10ms，120Hz情况下两帧间隔8.33ms，因此导致在位置2处没有发送信号。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/7a4snbehQIqpJaOY8igurA/zh-cn_image_0000002658794301.png?HW-CC-KV=V1&HW-CC-Date=20260701T025512Z&HW-CC-Expire=86400&HW-CC-Sign=A8FB5F5B6B4762D91763CD2DB8EB9DD2D6DEFAA975C96C29EC538BE6493B1056)

- 在Callstack泳道的ui[47556]以及raster[47557]子泳道中查看ui和raster线程单帧绘制时的调用栈，发现耗时主要集中在libflutter.so文件中。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/u2DliD4LRM2OMDQse0iUSg/zh-cn_image_0000002628554938.png?HW-CC-KV=V1&HW-CC-Date=20260701T025512Z&HW-CC-Expire=86400&HW-CC-Sign=DBB9BDE69B7F5F8E8CA20C06DDA06C36E19736DD6F87E0B114416E8D7EE55EE6)


 
 
 

##### 分析结论

- 应用Dart业务代码执行耗时多，导致Flutter ui线程一帧绘制耗时长，出现滑动卡顿的问题。
- ui和raster线程单帧绘制耗时集中在libflutter.so文件中，超出120Hz情况下两帧间隔8.33ms，导致出现丢帧问题。

 
 

##### 修改建议

- 优化应用Dart业务代码，减少执行耗时。
- 优化应用libflutter.so库调用，减少执行耗时。
