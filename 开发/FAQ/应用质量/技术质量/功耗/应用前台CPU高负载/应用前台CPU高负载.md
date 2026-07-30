# 应用前台CPU高负载

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-power-footage-1

#### 问题现象

一些应用程序会在前台长时间工作运行，比如视频直播类应用长时间播放视频，金融理财类应用不断更新显示的数据，会使设备CPU持续在高频下工作，存在CPU高负载问题。
 
 

#### 背景知识

- DevEco Profiler目前是集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，目前版本提供六大特性解决快速定界、效率提升、内存分析、内核分析和卡顿分析相关问题，帮助应用开发者定位到问题代码，更多详细介绍可查看[使用Profiler进行性能调优](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-introduction)。DevEco Profiler提供[实时监控](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/realtime-monitor)（Realtime Monitor）能力，该能力提供全方位的设备资源监测，覆盖系统事件、异常报告、CPU占用、内存占用、实时帧率、GPU使用率、温度、电流、能耗以及网络流量消耗等多个维度的数据，可以帮助识别性能瓶颈，定界问题所在。
- Trace文件是一种用于追踪应用程序在运行时的性能和行为的文件，它是通过调用系统提供的Trace类的方法来记录应用程序的操作。通过Trace文件能够分析应用程序运行时各阶段的耗时情况，查看Trace文件可使用[Smartperf](https://gitcode.com/openharmony/developtools_smartperf_host/blob/master/smartperf_host/README_zh.md)。
- 火焰图是一种用于可视化程序性能分析的工具，其以直观的图形界面，将复杂的函数调用关系和执行时间分布清晰地展示出来。在分析功耗问题中常常借助火焰图来找到应用运行中比重较大的部分，确定问题分析的方向。Smartperf的[Hiperf](https://gitcode.com/openharmony/developtools_smartperf_host/blob/master/smartperf_host/ide/src/doc/md/quickstart_hiperf.md)工具包含了火焰图功能。

 
 

#### 问题定位
1. 使用DevEco Profiler实时检测工具(Realtime Monitor)查看运行应用一段时间后的在CPU上的运行占比以及设备温度，如果手机温度在持续上升达到发热、应用进程运行在CPU运行占比较高，如下图所示，则存在功耗问题。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/xPo877t2QbOHVUSNooTg9w/zh-cn_image_0000002628316224.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=5F6E8FFB4937B050DBFF266CBB3688497609A1D0ED36ED35C843500BC368726E)

2. 使用Smartperf的Hiperf工具抓取该过程的火焰图数据，通过Hiperf的火焰图功能查看运行占比较高的线程是应用子线程还是渲染相关的线程，展开Hiperf泳道，框选前面两个泳道，下方会以运行频率从高到低来显示各个进程的情况。
如果运行占比较高的线程为应用的子线程，则会看到如下图所示的情况，在运行占比最高的应用进程7139中，子线程7394运行占比最多。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/9Cy_czRwTsmwmZRO8xEbZw/zh-cn_image_0000002658675461.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=34A9B2F33A7532700E70D8C63DBFAB5308852B1944CA87383BC441EA879426C8)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/xK47jesWRfSG1QqkZ7cKfA/zh-cn_image_0000002658555519.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=20DA8880DFD9C38B6F79E04D9C1F7AB3B4E374AFA4ECE40D95BC9FB3E6B0713D)


  a.在应用线程中该子线程的泳道，框选运行状态，查看该线程主要运行在什么CPU上，如果在CPU10和CPU11（大核）上，则确定是由于该线程长时间运行导致功耗问题。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/qzR-nMQ9QHKKtBNGbf_kmw/zh-cn_image_0000002628476140.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=861CBFD11273F575D19E1BDD8F45C6EE6D0EB2DAC1DC30D41241D904C51432BA)


  b.通过Perf Profile来查看该线程的调用栈，耗时集中在执行什么函数上。从下图中可以看到uv_run运行时间最长，堆栈中涉及到了libuv.so库，该库基于事件驱动来实现异步I/O，适用于网络编程和文件系统操作。应用通常使用该库访问云侧查询数据，因此需要排查应用侧业务处理逻辑是否合理，是否存在死循环，任务是否过多。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/V6mYDRvjR2SIbC6Yj4_dXg/zh-cn_image_0000002628316228.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=0BFF3E2E17F6D3FEC53E08B64B9A3D2C40F5A61C066314AE43A0BC06D03D6C0D)

3. 如果运行占比较高的线程为绘制、渲染相关的线程，如下图所示，渲染服务进程render_service和应用进程29187运行占比最高。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/6rcDG8L9SdO12MdSdWj8GQ/zh-cn_image_0000002658675465.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=EEBD06B26418EFA5CF8D54034854E279A06AB333C6534573EFAA5CFF1691496F)


  a.点击/system/bin/render_service(1466)查看render_service的子线程运行占比，可看到RSUniRenderThread线程和主线程占比最高。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/7aDX2hT6SaK6vz1mRd0izw/zh-cn_image_0000002658555523.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=529C562AF469698ED82634AB9794150CCBABF7F8EE19B3D580A3A3873CBCCFBB)


  b.点击应用进程29187查看应用的子线程运行占比，可看到主线程运行占比最高。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Id4gWkhzR5SiNBhTwzFsJA/zh-cn_image_0000002628476142.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=829D87544D564BFCD4C9AD8E8E3587A881F1CCDED17823295B8AE914849402CC)


  c.在Trace中框选应用主线程泳道，在下方搜索框输入anima、FrameNode来确认是否有动画、组件绘制的情况，如果存在动画、组件多次绘制的情况，使用ArkUI Inspector工具查看执行动画、进行多次绘制的组件是什么，是否显示在屏幕上，如果不存在屏幕上则存在动画空跑、冗余绘制的情况，会导致功耗问题。

  如在下图中可以看到应用主线程有执行动画，同时组件Canvas（id为1441）、Image（id为338、284、516）有多次绘制。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/RdNlRpCNTQ22e-HBI02x8A/zh-cn_image_0000002628316230.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=A858FB482B0999794801A833B99F764F52294B596B7D4E38351C44F6A8DFB069)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Qx9E_lCDTyK8tQq4LFCc-Q/zh-cn_image_0000002658675467.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=1E6AD9DEC4AFFA7EE70CFE26608DDE78D63092863E819BBC21F599E0E5088D1E)


  d.使用ArkUI Inspector工具来查看绘制的组件，可以看到组件Canvas未显示在屏幕上，而Image组件显示在屏幕上。Image显示组件在屏幕上，有执行动画，属于正常的业务流程，而Canvas组件未显示在屏幕上，存在冗余绘制的问题。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/6g71uCh4TTSnSAFVMe_LXA/zh-cn_image_0000002658555525.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=22F18580F80E036C53B2B834E4E7057286816E992EA87C65AFE890B68AB17A0A)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/41dSuf7pSLSrl5YudiS_ZQ/zh-cn_image_0000002628476144.png?HW-CC-KV=V1&HW-CC-Date=20260730T072246Z&HW-CC-Expire=86400&HW-CC-Sign=59FC595B01115503B420F9219A9A57F0E8CCC8B813F87866DE49C7D49E254089)

 
 

#### 分析结论
1. 应用子线程处理任务较多，长时间在大核CPU上运行，导致功耗问题。
2. 应用组件冗余绘制、动画空跑，使主线程长时间在大核CPU上运行，导致功耗问题。
 
 

#### 修改建议
1. 优化应用子线程处理逻辑，减少处理任务。
2. 应用组件存在冗余绘制问题时，可优化成不显示时停止绘制，避免冗余绘制。
