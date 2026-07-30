# 开发态快速定位DMA泄漏

更新时间：2026-07-22 06:05:01

来源：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dma-leak-in-develop

#### 概述

 
在HarmonyOS中，DMA内存是指由DMA驱动分配的、支持多进程和多硬件之间共享访问的RAM内存（特别说明，DMA内存与ION内存是同一概念）。在HarmonyOS系统中，应用一般通过系统开放的ArkUI、图形和媒体的相关接口间接使用DMA内存。例如ArkUI中的XComponent、Image和Web组件，图形相关的ImageNative和NativeBuffer，AvCodec的编解码，图片的PixelMap接口等。当应用占用的DMA内存超过阈值时，即认为应用发生DMA内存泄漏。
 
本文将通过高频泄漏场景和DMA内存泄漏分析案例快速定位应用DMA泄漏的问题。
 

#### 常见泄漏场景

应用通常通过系统提供的ArkUI、图形和媒体接口间接使用DMA内存，常见场景包括：
 
 
- **Image控件泄漏或者缓存过多导致内存泄漏**应用程序中的Image控件未正确释放DMA内存，引发DMA内存泄漏，最终引发系统图像服务异常或应用崩溃。
- **ArkWeb控件泄漏导致内存泄漏**应用程序中的ArkWeb控件未正确管理ArkWeb控件的生命周期或缓存策略，引发DMA内存泄漏，最终引发系统异常或应用崩溃。
- **使用Surface的NDK接口分配内存未释放导致内存泄漏**应用程序中，Surface的NDK接口分配的DMA内存未释放，引发DMA内存泄漏，最终引发系统异常或应用崩溃。
- **XComponent组件泄漏或者缓存过多导致内存泄漏**应用程序中的XComponent组件未正确释放DMA内存，或组件缓存无限增长，引发DMA内存泄漏，最终引发系统异常或应用崩溃。
- **视频软硬编解码器API接口使用不当导致内存泄漏**应用程序中的视频软硬编解码器API接口使用不当导致视频解码/编码时分配的DMA内存未释放，引发DMA内存泄漏，最终引发系统异常或应用崩溃。

 

#### 标准化排查流程

 
1. 复现与日志获取：使用DevEco Profiler的Allocation模板开启统计模式录制泄漏场景，重复3-5次操作疑似泄漏场景以复现问题。
 
2. 识别泄漏点： 点击All Anonymous VM中的VM:ION子泳道，在下方详情Call Tree标签页中选择Created&Existing，查看内存占比较高的调用栈。
 
3. 分析调用栈：优先在调用栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。
 
4.** **代码审查：结合调用栈，梳理相关代码中的内存持有逻辑，定位泄漏根因。
 
- 业务逻辑未发现异常：[查看进程中DMA内存信息](#section53218913389)并结合DMA内存信息分析。
- 业务逻辑存在异常：修改相关代码。

 
5.** **修复与验证：修改代码后，重复步骤1，确认内存曲线回归平稳。
 
标准化排查流程整体流程如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/n6P6Nr_BTNiSaH_hsH8IJw/zh-cn_image_0000002675100563.jpg?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=37ABBCBB5E8813D7011BDF111AAC50C898FAC55DC53224D8E6BCFB203D028837)

 

#### DMA内存泄漏分析案例

 

#### 案例背景

**现象**：本案例中，通过反复操作复现问题场景，观察到应用Graph内存占用呈现“阶梯式持续增长”趋势。
 
**初步判断**：使用Allocation统计模式录制内存上涨过程，观察Memory泳道中的Graph曲线，呈现出典型的“阶梯式增长”，确认存在DMA内存泄漏。
 
- **Graph子泳道**：应用使用的DMA内存。

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/iZBNVRZWS6m28d09zLEwvA/zh-cn_image_0000002675020711.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=B0B38A05B221F9FAB49B83E22BB3B807AF10AD999AF1D07A3E57709318DDCD16)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Ys94zQPrRbGL28_Y6E_ypg/zh-cn_image_0000002645100760.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=94380E0945AD09EDE698D1214F7A44F7A997699CEA94D6855ADF6FCB4C4846C0)

 
 

#### 分析流程
1. **通过Allocation录制泄漏场景**

1. 基于DevEco Studio Profiler插件的Allocation模板分析堆内存分配、释放的信息以及调用栈信息。这些信息中包括已释放内存和未释放内存。操作步骤如下：启动应用进程，选择Profiler工具 → 选择设备与应用进程 → 选择Allocation模板 → 创建Session → 配置录制选项。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/MYNlNyjfT4GOPa8UFykTLw/zh-cn_image_0000002644940858.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=A45FBF155167A261E93A418F5A5928533631D8F6B080BE8F621B764263897FF8)


2. 开启统计模式，可以打开JS栈记录和异步栈记录开关。由于DMA内存的分配频率相比于NativeHeap的Malloc更低，因此可关闭Malloc采集，减少对DMA内存分析的影响。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/b6tsdqgATviHBIN-LbWwvg/zh-cn_image_0000002675100565.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=617CF65F85A6B2140E0C781B3403BDBEF6B84CAC9EAAEF9DD1029511FB1887BB)


3. 点击按钮启动录制并复现问题场景。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/eIqOf91jSCeuhFHUzbiiqg/zh-cn_image_0000002675020713.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=4DECAC5D2DF5EAFCFB19461DBB6DCA75D7E82A029A14CD583B7BD9DEA7ECA265)

2. **查看DMA内存调用栈**

1. 框选All Anonymous VM中的VM:ION子泳道。

  
VM:ION子泳道：用于显示DMA内存分配数据。
3. All Allocations：框选的时间段的所有分配内存信息。
4. Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
5. Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。
6. **分析DMA内存调用栈**

  优先在内存分配栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。可以看到业务代码中缓存了PixelMap，但未调用release()方法释放内存。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/51vAEKENQ7aRovfNqmJLDQ/zh-cn_image_0000002675100567.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=77F05E50486EA8B31081A436E4FE9939A044F3A217109035D6E228B4BFD415CF)

 
 

#### 优化修复
1. 修改代码，增加image.PixelMap的release()方法释放内存。
2. 重新运行应用，再次使用Allocation录制内存分配栈。
3. 重复3-5次操作泄漏场景。
4. 验证结果：
每次页面退出后，内存曲线回落至基线。
5. 泄漏问题已修复。
 
 

#### 附录：查看进程中DMA内存信息

1. 查找进程pid。启动应用进程，选择Profiler工具 → 选择设备与应用进程，即可看到进程pid。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/2LsaQRu9TBKVh5bdptj2ZA/zh-cn_image_0000002645100764.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=970B630CBB09ECB0E7166EB85638FF9921DBD3E7B22F5C6E39C6B183ABDE1A53)

 
2. 获取到pid后，在终端中执行hdc shell，然后执行命令hidumper --mem pid --show-dmabuf（[查询进程内存](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#查询进程内存)）对比出现DMA泄漏前和DMA泄漏后的DMA内存数据。根据buf_name和leak_type排查相关组件。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/XJNA-MRdS6WiOT-Xy3dUNw/zh-cn_image_0000002644940862.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=30813E45DD136A2D4D4816CA18949119B85958C29A844023E53C7C9D80F0BD72)

 
获取指定pid的DMA内存详细信息，开发者可以根据DMA内存信息中的buf_name、leak_type等列定位可疑泄漏组件。
