# Frame分析

更新时间：2026-06-12 06:54:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-frame

#### 功能介绍

开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据并进行分析，从而识别出导致卡顿丢帧的原因。

Frame模板支持的泳道包括：Anomaly、User Events、Frame、ArkUI Component、ArkUI State、User Trace、ArkTS Callstack、Callstack、Network Traffic、Network Request、Energy、CPU Core、Process。本文介绍Anomaly、User Events、Frame泳道，其他泳道的详细信息请参考对应模板内容。

 - ArkUI Component、ArkUI State泳道的介绍请参考[ArkUI分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-analysis)。
 - User Trace、ArkTS Callstack、Callstack泳道的介绍请参考[基础耗时：Time分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-time)。
 - Network Traffic、Network Request泳道的介绍请参考[网络诊断：Network分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-network)。
 - Energy泳道的介绍请参考[能耗诊断：Energy分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-energy)。
 - CPU Core、Process泳道的介绍请参考[CPU活动分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu)。


> [!NOTE]
> 卡顿丢帧分析前，需创建Frame分析任务并录制相关数据，操作方法可参考 性能问题定位：深度录制 ，或在 会话区 选择 Open File ，导入历史数据。




#### 查看GPU使用情况

**Frame**泳道显示当前设备的GPU的使用率，将其展开，子泳道显示渲染服务（Render Service）侧帧数据和App侧帧数据。

在带有**RS Frame**和**App Frame**标签的子泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。

> [!NOTE]
> 一帧的绘制，一般需要由App侧提交渲染到Render Service侧，然后Render Service侧再提交给硬件进行合成渲染，因此App侧的帧和Render Service侧的帧存在关联的情况。并且可能多个APP侧的帧/同一APP侧的多个帧提交到同一个Render Service侧帧上，出现帧之间的一对多的关联情况。 一帧绘制的期望耗时，与fps的大小有关，一般情况下fps为60，对应的Vsync周期为16.6ms，即App侧/Render Service侧的帧耗时，一般需要在16.6ms以内。App侧帧/Render Service侧帧判断卡顿的标准为帧的实际结束时间晚于帧的期望结束时间。



![](assets/Frame分析/file-20260514133135535-10.png)




#### 查看指定时间段内所有进程的Frame数据统计信息
1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 框选**Frame**主泳道。窗口下方的**Statistics**区域以进程维度展示了选定时间段内的Frame相关信息，包括卡顿率、卡顿次数、最大连续卡顿次数、最大卡顿耗时、平均卡顿耗时以及平均正常耗时等。

  
![](assets/Frame分析/file-20260514133135535-11.png)

3. 点击**Statistics**列表中任一进程的跳转按钮会跳转至**Frame List**，该区域展现该进程各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

  
![](assets/Frame分析/file-20260514133135535-12.png)

4. 点击Frame List中任意一帧，在右侧的**More**区域会中显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击
![](assets/Frame分析/file-20260514133135535-13.png)
跳转至关联的切片。



#### 查看指定时间段内指定进程的Frame数据统计信息
1. 在时间轴上拖拽鼠标选定要查看的时间段。
2. 展开**Frame**主泳道，选择要观察的带**App Frame**或带**RS Frame**标签的子泳道。

  窗口下方的**Details**区域中会显示选定时间段内的RS帧统计信息列表，体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

  
![](assets/Frame分析/file-20260514133135535-14.png)

3. 单击列表中任意一帧，右侧的**More**区域中会显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击
![](assets/Frame分析/file-20260514133135535-15.png)
跳转至关联的切片。



#### 查看指定Frame信息

展开**Frame**主泳道，选择带**App Frame**或带**RS Fram****e**标签的子泳道，该[泳道图区域](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-data)上方是耗时最长的非UI函数，下方是UI主线程泳道。将鼠标悬浮在任意帧上，会冒泡显示该帧的Jank信息。


![](assets/Frame分析/file-20260514133135535-16.png)


窗口下方的**Frame**区域中会显示选定帧的关键信息，如VSync编号、开始时间、App应用侧持续时间、App应用侧业务逻辑耗时、Render Service侧持续时间、GPU持续时间、总持续时间、卡顿丢帧类型以及可能出现卡顿的原因等。在带**App Frame**标签的子泳道中，**Non UI**区域中会显示非UI耗时最大的函数，如开始时间、结束时间、持续时间，函数名等。      
> [!NOTE]
> 在选定观察对象后，DevEco Profiler会自动关联与其相关的切片，用箭头连接。 如果该帧是由于超出期望结束时间引起的，则显示两条线，对应期望开始时间（Expected Start）和期望结束时间（Expected End），用于关联分析同一时刻Trace或者函数采样信息。 卡顿丢帧类型（Jank Type）：No Jank（不卡顿）、AppDeadlineMissed（App侧的卡顿）、RenderDeadlineMissed（Render Service侧的卡顿）。




![](assets/Frame分析/file-20260514133135535-18.png)




#### 查看指定Frame页面布局信息

从DevEco Studio 5.1.0 Release版本开始，支持查看最新录制的Session中指定的Frame页面布局信息。

从DevEco Studio 6.1.0 Beta1版本开始，
![](assets/Frame分析/file-20260514133135535-19.png)
按钮中新增Frame Layout开关，开发者可自行设置开关状态。开关关闭时，不支持查看最新录制的Session中指定的Frame页面布局信息，默认关闭。

暂不支持在Wearable设备上查看指定Frame页面布局信息。

1. 展开**Frame**主泳道，单击带**App Frame**或带**RS Frame**标签的子泳道中任意一帧，**Details**区域会展示该帧具体信息。点击**Open Layout**按钮，将在ArkUI Inspector中直接打开相应arkli文件；点击**Download Layout**将arkli文件下载到指定目录，之后可手动导入[ArkUI Inspector](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector)查看页面布局信息。

  
> [!NOTE]
> 单击Download Layout或 Open Layout前，应用进程需置于前台，才能正确回放全量渲染数据，获取arkli文件。


  
![](assets/Frame分析/file-20260514133135535-20.png)

2. 在ArkUI Inspector中可查看组件树和组件属性信息，当前支持BackgroundFilter、nodeGroup、nodeGroupReuseCache组件。

  
 - BackgroundFilter：背景滤波器。

3. nodeGroup：节点组类型，0表示非节点组节点，1表示被动画标记的节点组，2表示被UI标记的节点组，4表示被用户标记的节点组，8表示被前景滤波器标记的节点组。

4. nodeGroupReuseCache： 0表示在生成缓存或无需缓存，1表示在重用缓存。

  

  #### 查看帧率统计信息

1. 展开**Frame**泳道，框选一段数据。

2. 带**App Frame**和**RS Frame**标签的子泳道会出现FPS标记，展示当前框选范围内的帧率统计信息。

  
![](assets/Frame分析/file-20260514133135535-22.png)


3. 在带**RS Frame**标签的子泳道中打开Only ArkWeb data开关，筛选过滤出包含ArkWeb帧的数据。

  
![](assets/Frame分析/file-20260514133135535-23.png)


  

  #### 查看动效详细信息

  开发者在开发应用时，会使用到动效，动效的卡顿影响到用户的使用体验。DevEco Profiler提供动效场景的调优，能帮助开发者优化动效场景。

  展开**Frame**主泳道，查看**Animation**子泳道，将鼠标放置在某个动效上，泳道会显示该动效的详细信息，包括响应时延、动效持续时间、完成时延、期望帧率、FPS。

  
响应时延：<=85ms 绿色，85ms~150ms 浅绿色，150ms ~250ms 浅红色，>250ms深红色。
 - 动效持续时间：根据帧率展示颜色，FPS大于达标帧率即为绿色，小于则为深红色。智能刷新率模式下，帧率可变，颜色为灰色。达标帧率与期望帧率的大小有关，一般情况下期望帧率为60HZ，则达标帧率= 60HZ * 91.7%。
 - 完成时延：响应时延和动效持续时间只要有一个为深红色，完成时延为深红色。
 - 期望帧率：当前系统运行满帧帧率，如60HZ、90HZ、120HZ。智能刷新率模式下，不展示期望帧率。


> [!NOTE]
> 在 Launch模板 中，点击Frame泳道， Details 区展示启动动效的详情信息， More 区域展示动效帧的Animation Data List信息。



![](assets/Frame分析/file-20260514133135535-25.png)




#### 查看组件动画信息

从DevEco Studio 6.0.0.828版本开始，Frame泳道下新增Component Animation子泳道，用于从组件的角度展示应用中包含的各种动画类型，包括属性动画 (animation)、显式动画 (animateTo)、关键帧动画 (keyframeAnimateTo)以及页面间转场 (pageTransition)。

在**Details**区域，可以查看每个动画的详细信息，包括起止时间、帧率、动画曲线类型以及影响的组件属性等。单击列表中任意一动画，右侧的**More**区域中会显示该动画所影响的组件属性的具体变化过程。


![](assets/Frame分析/file-20260514133135535-3.png)




#### 查看屏幕帧率动态变化场景下丢帧和卡顿信息

Frame泳道下新增Lost Frames和Hitch Time两个子泳道，用于识别和优化卡顿和丢帧问题。

 - Lost Frames子泳道：展示当前时间段内丢帧数。Lost Frames计算出的结果，六舍七入统计取整。
 - Hitch Time子泳道：展示当前时间段内卡顿时长。计算方式为渲染前后两帧的间隔减去单帧耗时，若计算结果大于单帧耗时*70%，则视为出现卡顿现象。

1. 创建Frame模板并录制会话，如存在卡顿和丢帧现象，会在**Lost Frames**和**Hitch Time**子泳道对应时间显示矩形图。

  
![](assets/Frame分析/file-20260514133135535-4.png)

2. 鼠标悬浮到泳道图区域某一时间点，提示信息会显示该点所属时间段内的丢帧数以及卡顿时间。

  
![](assets/Frame分析/file-20260514133135535-5.png)




#### 查看组件帧率信息

Frame泳道下新增两个子泳道，分别为Display Vsync与DisplaySync_cb(tid)，用于对可变帧率的检测调优。      
 - Display Vsync子泳道：该泳道显示对应时间段的屏幕刷新率，支持对框选的时间段内的vsync进行分布统计。区分“<=30HZ”、“30~60HZ”、“60~90HZ”、“>90HZ”。统计值包括框选时间段内各区间的分布比率、最小/最大/平均时长以及平均HZ。如果某场景满足了帧率改变的要求，当底层系统根据机制进行变帧，相应的情况会展现在对应的泳道，帮助开发者了解vsync的变化情况是否符合预期。该泳道仅支持在配备硬件屏幕的设备上进行数据采集。
 - DisplaySync_cb(tid)子泳道：该泳道显示对应组件的帧率，如DisplaySync、XComponent两类接口组件动画对应的帧率。调测时，不同场景下由于帧率可变，系统实际表现是否符合预期，需要有实际的检测手段。尤其是由于DisplaySync的渲染均在UI主线程执行，当存在多个需要渲染的组件需要同时执行时，只能在UI主线程排队，此时任何一个组件的延迟都会对其他组件的渲染产生影响，导致UI卡顿。        如下图所示，vsync2和vsync4中，vsync周期内的组件由于渲染耗时长，导致以下两个vsync周期挤掉下一个vsync周期的渲染时间，导致掉帧的情况产生。

  
![](assets/Frame分析/file-20260514133135535-6.png)



1. 选择**Display Vsync**子泳道，在时间轴上拖拽鼠标选定要查看的时间段。
2. 详情区显示当前时间段的屏幕刷新率，当前帧最大持续时间、最小持续时间、平均持续时间以及该时间段内平均帧数。

  
![](assets/Frame分析/file-20260514133135535-7.png)

3. 选择**Display Vsync**子泳道，可以查看当前帧的耗时和帧率。

  
![](assets/Frame分析/file-20260514133135535-8.png)

4. 框选**DisplaySync_cb**子泳道，可以查看应用侧对应组件的帧率，渲染时间等信息。

  
![](assets/Frame分析/file-20260514133135535-9.png)

5. 同时如果组件有可能的掉帧情况，**DisplaySync_cb**子泳道显示对应的掉帧情况并标红展示。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/8MByu013TFuJ0sb6V7eKwQ/zh-cn_image_0000002624993891.png?HW-CC-KV=V1&HW-CC-Date=20260624T020720Z&HW-CC-Expire=86400&HW-CC-Sign=71046E16E0E975C265CB0F440FF01A1717B43B587F295156199DC483FB4A3CE3)




#### 查看解码过度耗时和超过阈值的序列化、反序列化操作

如果工程中存在图片资源，并感知到解码绘制/渲染过程存在卡顿，可以通过Anomaly泳道查看主线程解码过程中是否存在解码过度耗时告警，并确认发生告警的时段。

如果应用中使用了worker、Taskpool工作线程等场景，通常会触发跨线程对象传递，并触发序列化和反序列化的操作。对于耗时超过阈值的序列化、反序列化操作，Anomaly泳道也会给出对应的耗时告警，并给出发送这个操作的开始时间和耗时时间。
1. 在时间轴上拖拽鼠标选定出现告警的时间段。当耗时超过VSync周期的50%时，将在**Anomaly**泳道中出现红色告警，提示“Image decoding has exceeded 50% of the VSync time”。
2. 详情区给出录制时段内解码过度耗时的统计情况，包括类型，图片名，计数，总耗时，最小耗时、平均耗时、最大耗时，耗时标准差、 图源尺寸大小，目标尺寸大小等。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/N0rCEARrTCC4zBMS47Kafg/zh-cn_image_0000002625074043.png?HW-CC-KV=V1&HW-CC-Date=20260624T020720Z&HW-CC-Expire=86400&HW-CC-Sign=DBDAC89729351D865F18EA589B09CEDB20D3317D5D184FAA5894F63F5E898C91)

3. 对于耗时超过阈值的序列化、反序列化操作，**Anomaly**泳道也会给出对应的耗时告警。其中可以通过泳道启动配置按钮配置检测阈值，默认配置阈值为8ms。
4. 详情区给出录制时段内序列化、反序列化耗时情况统计信息，包括类型、计数、总耗时、最小耗时、平均耗时、最大耗时、耗时标准差等。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/Au3IFC7DSMe95YwhNHWdHA/zh-cn_image_0000002594474520.png?HW-CC-KV=V1&HW-CC-Date=20260624T020720Z&HW-CC-Expire=86400&HW-CC-Sign=AD0A04BB14707C4C8C7A676A1454338BECB4BA29D3876CF891AA575F58637E31)


  
> [!NOTE]
> 已上架应用市场的应用不支持录制Anomaly泳道。




#### 查看用户事件耗时

开发者在卡顿丢帧场景可通过User Event泳道查看用户事件，可查看用户事件开始时间、应用开始处理时间以及应用处理耗时等情况。
1. 选择**User Event**泳道，在时间轴上拖拽鼠标选定要查看的时间段。
2. 详情区列表给出录制时间段内用户事件详情，包括用户事件ID、事件开始时间Input Time、应用开始处理时间Processing Start、应用处理耗时Duration和事件类型User Event Type。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/_9zK_UWmRIGRpnBepgTcVg/zh-cn_image_0000002594634450.png?HW-CC-KV=V1&HW-CC-Date=20260624T020720Z&HW-CC-Expire=86400&HW-CC-Sign=5F89EA17AFC9170BDE34835693E72CE34CE34D79DBEC7BBBB147A09DCEF36C66)

3. 点选User Event泳道中的条块，**Slice Detail**区域展示该事件的详情信息。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/AZVWvZHTTmixyOSVvAQTsw/zh-cn_image_0000002594634470.png?HW-CC-KV=V1&HW-CC-Date=20260624T020720Z&HW-CC-Expire=86400&HW-CC-Sign=31E6CFFA739940C6CD4F5360BF6E03030D4ACE16F88D10485BE234EA7E696B7C)


更多性能调优最佳实践，请参考[点击响应时延分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-click-response-optimization)、[点击完成时延分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-complete-delay-analysis)、[帧率问题分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-zhenlv)、[Web点击响应时延分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-click-response-delay-analysis)、[Web加载完成时延分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-completion-delay-analysis)。
