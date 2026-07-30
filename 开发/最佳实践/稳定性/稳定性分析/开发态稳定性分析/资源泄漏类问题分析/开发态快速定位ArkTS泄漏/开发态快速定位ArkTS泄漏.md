# 开发态快速定位ArkTS泄漏

更新时间：2026-07-22 06:05:01

来源：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-leak-in-develop

#### 概述

在ArkTS中，开发者无需手动管理内存。但如果代码中存在不合理的引用，则会导致内存无法被正确回收，从而引发内存泄漏。本文将通过常见泄漏场景和ArkTS内存泄漏分析案例，帮助开发者快速定位应用中的内存泄漏问题。
 
 

#### ArkTS泄漏根因

ArkTS运行时采用[HPP GC](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gc-introduction#hpp-gc)（即高性能部分垃圾回收），将对象按生命周期划分为新生代和老年代。使用标记-清除（mark-and-sweep）算法回收内存，所有可达对象被标记为存活，不可达对象则被回收。每次GC都是从根节点开始遍历，因此根节点被称为[GC Root](#table17319174010236)。该树的快照如下图所示。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/jJaothozQniL1Q3Z-CxxDA/zh-cn_image_0000002675100549.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=0D08C703F6D19C1AC67C832EA2F12E81DE9AE55AE1085940ED930BCE3DEC76BE)

 
理解垃圾回收（GC）机制的核心，在于把握一个根本原则：GC仅回收那些从GC Root不可达的对象。换言之，只要一个对象仍处于引用树的路径之上，即便它已被程序逻辑遗忘、不再被实际需要，GC也无力将其回收。内存泄漏的本质不是GC失效，而是开发者留下了不该留的引用链。因此排查内存泄漏的关键，就是找到那条从GC Root出发、让无用对象“存活”的引用路径，并在适当位置将其切断。
 
 

#### 常见泄漏场景

 

#### JS对象被VMRoot类型持有导致内存泄漏

常见构成[VMRoot](#table17319174010236)引用的来源包括：
 
- 模块导出对象：export出的对象被底层的SourceTextModule系统对象持有，而模块本身在应用生命周期内不被卸载。
- 全局对象属性：通过globalThis.xxx = ... 挂载的对象，globalThis是贯穿应用始终的根对象。
- 内置原型链扩展：修改Array.prototype、Object.prototype等内置对象原型，导致意外全局持有。

 
一旦业务对象挂载到上述根节点上，即使页面销毁、组件卸载，该对象依然被VMRoot强引用，GC无法回收。
 
 

#### JS对象被Local Handle/Global Handle引用导致内存泄漏

 
在鸿蒙的JS-Native交互中，JS对象可以通过NAPI Native代码访问或持有。Native代码为了引用这些JS对象，会使用两种主要的句柄类型：napi_value、napi_ref。其中，napi_ref是一种引用计数的句柄，用于保持对JS对象的引用，防止其在Native代码持有引用期间被垃圾回收器回收。
 
- Local Handle (napi_value): 通常指在Native代码执行上下文中创建的、作用域较短的引用。当Native代码执行环境切换时，这些[Local Handle](#table17319174010236)通常会被自动清理。Local Handle受Handle Scope管理，大部分场景下（如同步调用、napi框架异步调用等）系统会为创建的Local Handle添加Handle Scope，但仍有部分场景（如libuv异步调用等）系统不会主动添加Handle Scope，需要应用自行添加Handle Scope，否则就会导致JS对象无法回收。
- Global Handle (napi_ref): 这是一种作用域为整个应用生命周期的引用。一旦创建，除非显式删除，否则它会一直保持对JS对象的引用。通常用于需要跨模块、跨上下文甚至跨JS线程访问的JS对象。由于其持久性，如果不加注意，很容易成为JS对象泄漏的根源。

 
当Native代码持有（无论是local还是global）一个JS对象时，它实际上建立了一种强引用关系。在JS引擎的垃圾回收机制中，如果一个JS对象的所有可达性引用（包括JS代码内部的引用、DOM树等）都被清除，该对象就可以被回收。然而，如果存在一个Native句柄指向它，那么这个句柄就构成了一个阻止根，使得该JS对象在Native代码持有该句柄期间，从垃圾回收器的角度看，它是“可达”的。这就阻止了JS对象被回收，从而可能导致内存泄漏。
 

#### JS对象被FrameRoot类型持有导致内存泄漏

正常情况下，函数执行完毕退栈后，栈帧销毁，这些临时引用自动失效，内存随之释放。
 
然而，若函数长期不退栈，局部变量/参数所引用的对象将持续被[FrameRoot](#table17319174010236)锚定，即便业务逻辑已不再需要它们，GC也无法回收。常见导致栈帧滞留的情形包括：
 
- 死循环或无限递归，函数永不返回。
- 在函数内启动了一个长期运行的同步阻塞操作（如同步网络请求、大文件同步读写）。
- 函数内部创建了闭包并被外部长期持有，且闭包捕获了该函数栈帧中的变量（导致整个栈帧无法释放）。
- 使用了生成器（Generator）或async/await但未正确消费，导致协程挂起，栈帧保留。

 
 

#### 标准化排查流程
1. 复现与观察：使用DevEco Profiler的Realtime Monitor(Memory泳道)，重复多次进出目标页面，观察内存曲线是否呈阶梯状上升。
2. 识别泄漏点：在操作前后各采集一次堆快照，使用Snapshot对比功能，关注新增对象数量和Shallow Size，从而识别泄漏点。
3. 查看对象引用链：在Snapshot快照的对象引用链中找到异常存活对象（如本该销毁的Component实例），通过“Shortest Paths”分析引用链情况。
4. 是否VMRoot持有：若引用链顶端为[VMRoot](#table17319174010236)/SourceTextModule，多为模块导出单例或全局变量未清理。
5. 是否Local/Global Handle持有：若泄漏对象的Distance为1，则多为Native侧持有未释放导致。可分为2种场景：
- [Local Handle](#table17319174010236)：napi_value未使用napi_open_handle_scope 或未成对使用（即使用napi_open_handle_scope但是未使用napi_close_handle_scope 释放）。

6. [Global Handle](#table17319174010236)：napi_ref 未调用 napi_delete_reference 释放或未成对使用（即使用napi_create_reference但是未使用napi_delete_reference 释放）在这2种情况下，无法基于引用链分析，需要通过Allocation模板，开启Local Handle及Global Handle录制选项来进一步分析。

7. 是否 FrameRoot 持有：若非VMRoot和Local Handle/Global Handle持有，则多为函数不退栈或闭包捕获对象被外部持有。

8. 代码审查：根据引用链中的关键节点（如 EventHub、Timer、全局变量、napi_ref、闭包上下文）定位代码中的持有关系。

9. 修复与验证：修改代码后重复步骤 1~2，确认内存曲线回归平稳。

  标准化排查流程整体流程如下图所示：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/sgLCRtl-Rt2roYqzsAyJlg/zh-cn_image_0000002675020693.jpg?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=57CBD674016FFE360CBBAD4F8DF5277B92A6326A07422632CE79A7698B60E88C)


  

  #### ArkTS内存泄漏分析案例

  

  #### 案例背景

  **现象**：本案例中，通过复现“首页至消息页”的反复进出操作，观察到应用内存占用呈现“阶梯式持续增长”趋势。在循环操作10次后，应用出现显著卡顿现象。

  **初步判断**：典型的“阶梯式内存增长”，高度疑似内存泄漏。

  

  #### 分析流程

1. **Memory泳道确认泄漏**

  
打开 DevEco Studio，连接真机，点击Profiler工具Realtime Monitor（也可使用snapshot模板的Memory录制观察，以下是使用Realtime Monitor观察）。

2. 启动应用，选择设备与应用进程。

3. 点击录制按钮，在设备上重复操作：进入消息页面 → 停留2秒 → 返回首页，重复多次。

4. 观察内存曲线：
**正常预期**：每次退出后内存回落至基线附近，整体呈锯齿状。

5. **实际现象**：曲线呈阶梯状上升，多次操作后内存增长至314.1MB且无明显回落，存在内存泄漏。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/qJ4XSnxpQTaTRoCHdJ7UAA/zh-cn_image_0000002645100746.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=AFEBEDB097F48CCA96446B3D15EBFC2068B91E73B7F51D8AA461E923CCEA06CD)

- **堆快照对比定位异常对象**

  在 Profiler 中切换到Snapshot模板，请参考[Snapshot模板基本操作](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-snapshot-basic-operations)：选择Profiler工具 → 选择设备与应用进程 → 选择Snapshot模板 → 创建Session → 启动录制。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/4pFKbsygQ6OhpCJe91mx4Q/zh-cn_image_0000002644940842.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=49E3B00B1DC5468E0FC901B862DA9BD632999A23B3B659FA85CF8A3C51C96EE3)


  抓取快照1：首次在进入消息页前，点击“Take Heap Snapshot”。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/7h6JTuIwR32Yr3mLlz5dhg/zh-cn_image_0000002675100551.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=3CB9706B6573CE88BF7F5261F294D068165DCA990DF97A9DD9908BA8B55F4329)


  抓取快照2：重复进出消息页面7次后，回到首页，点击“Take Heap Snapshot”，再抓取第二次快照，并停止录制。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/kHv_I08_R_6QN-9frCCHGg/zh-cn_image_0000002675020695.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=CDE16AD4633C98BF8E6CEE2D437210E0350B0B6B307C5321E13CCB1A5D299994)


  在快照对比视图Comparison中，选择CompareTo Snapshot1。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/JsiYRNTBSTaZIybjBwjwiQ/zh-cn_image_0000002645100748.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=B322112B3AB62B7C8A5E27D44FF34A811CD260DCCDC5ED640D8247B97D75FD84)


  查看对象新增销毁情况，优先关注：

  操作次数的整数倍或整数倍+1（export 出的对象本身也有一条引用链），

  业务对象，即Constructor的结构为包名/模块名/文件路径#泄漏对象。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Bu-H9MAvRue2rSyBol7p6A/zh-cn_image_0000002644940844.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=001580E3AABA8E534E4B20A366E0A1FE5DE24B8C6CF20842853FFF75619FCFA6)


  关键发现：

  
对比结果中，Test对象实例数量从0个增加到8个，Test对象实例泄漏。
- 正常情况下，页面退出后组件实例应被回收，快照2中应只有1个Test 对象（被export持有）。

 

- **追踪引用链**

  在快照对比视图中，展开并选中一个Test对象实例，优先选Distance数量较多的，此处我们选“6”的，并打开右侧详细信息面板。

  注：选择Distance数量较多的对象实例，主要是因为这些实例频繁地被创建且未能得到及时释放。这表明存在潜在的内存泄漏问题，需要进一步调查以确定具体的泄漏源。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/5uh0a3NpSY2MeQRdYeq5Eg/zh-cn_image_0000002675100553.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=A462C8004A467F156A599DC87EA7CCE290A4A44F188F8498C9D9FDB5E70D8412)


  点击“Shortest Paths”获得如下Test对象实例的最短引用链：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/25w1yBBhTSCs_CNNs0m0dA/zh-cn_image_0000002675020697.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=088A78FBCB847DE9C335DA4C883C3473BC326E27AB54D209EDB22254C52FA6A5)

- **分析****VMRoot类型持有导致泄漏问题**

1. 根据步骤3得到的Test对象实例的最短引用链分析，该引用链的GC Root为SourceTextModule符合被export模块导出对象持有，[VMRoot](#table17319174010236)泄漏类型场景。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/4qNL1xk8RtW9KrRFefIEOw/zh-cn_image_0000002645100750.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=11FA08B88BA8D889A7CFF35881FE6BCAC1862D76701E45277471FBF496282DA1)


2. 从GC Root向上排查引用链，找到第一个业务对象，即CacheTest.ts文件中的CacheTest对象的cache属性持有了Test对象未释放。点击后面跳转图标，打开CacheTest对象实例详细面板。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/Npw7iZdvRWSlr66NY7EWYg/zh-cn_image_0000002644940846.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=5BA4ABC743CDAC36EE13FDBCAF56039746C0E46214FEFEF81EB5EC7D3A2F10B7)


3. CacheTest对象实例面板中，点击对象名后跳转按钮，跳转对应代码行。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/qkWiFCYsSLaCOJzU5gyjNQ/zh-cn_image_0000002675100555.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=A59864F296876F9B41827EF297783963952CCCF812CA1F2679C9603262B614C3)


4. 跳转代码后分析，CacheTest对象存在静态属性cache，该静态属性中保存了Test对象。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/O44j23clQ32DT5XCplWpqA/zh-cn_image_0000002675020701.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=17F4029FE55C1902C7A8E6847D307DC7E2366EF41FBEF7573DD416F37DE1F684)


5. 结合业务代码分析，MessageCenterPage组件创建时会保存一个Test对象到CacheTest中，但组件销毁时未清理该缓存导致内存泄漏。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/OhCi53A4Qb-iMOFd7I1Xqw/zh-cn_image_0000002645100752.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=AC91B3AC1874B43954253F841A175F609F3AE5DD137F552DAB14BAF6402E3813)


6. 修改代码，在页面销毁时清除缓存。修改后重新复现操作**7次**，并抓快照验证，Test对象创建数量正常。但分析发现Proxy对象数量异常，创建70个未销毁。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/4zLS8W_dT0Swl2Xfj8hSpQ/zh-cn_image_0000002644940848.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=2BFAD6F4EB9D17A1D2B316542948838312B1EAA9621FB2FB7D1DAFCD6F93FFE9)


7. 参考“步骤3：追踪引用链”，找到最短引用链，发现该Proxy对象的Distance为1。说明其为GC Root直接持有的对象，被Native侧直接持有未释放，即JS对象被Local Handle/Global Handle引用导致内存泄漏。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/V4ebuY3_QNC2DzUMaiOslQ/zh-cn_image_0000002675100557.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=96F0544392F303D9B01288AE2C09EDE872DB7BCF28EE722A585766533FABE7E6)


8. 通过Proxy对象的Distance为1的References，确认内存泄漏是由JS对象被Global Handle引用导致。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/6FXzl55iRh60RXyQjFWUzQ/zh-cn_image_0000002675020703.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=6086C97E04A029BB34C56C366B033347C65604B14B9B7AC968B2A1A231FD34E9)

- 分析Local Handle/Global Handle类型持有导致泄漏问题

  基于步骤4分析得到Proxy对象实例可能被[Local Handle](#table17319174010236)/[Global Handle](#table17319174010236)引用导致内存泄漏，我们可以通过以下步骤继续分析定位：

  **1. 配置Allocation录制模板并捕获数据**

  
打开DevEco Studio：确保你的工程已加载，并连接了目标设备或模拟器。
- 进入Profiler模块：在主界面下方菜单栏，找到并点击Profiler选项卡。
- 选择应用进程：运行应用，并在“区域2”选择目标设备和应用进程。
- 创建Allocation录制模板：选择“Allocation”并点击Create Session创建录制模板。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/M8mHGRvUSziH8Xu8UCUw2w/zh-cn_image_0000002645100754.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=48F762271BB68F6A9D605315BD7D26D5DA6D704BCA13CCDCACA98A1718DFE707)

- 配置录制参数
配置模式：选择详情模式（即关闭Statistics Mode）。当前仅详情模式支持进行ArkTS和Native的关联分析。
- 配置开关：勾选“Local Handle”和“Global Handle”，这是关键配置。这将使Allocation专门捕获与JS-NAPI句柄相关的内存分配事件。如果底层镜像不支持该功能，则会提示“当前镜像版本不支持，请升级镜像”。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/bSrlYIZKREiS_9qbhzFO6A/zh-cn_image_0000002644940852.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=3FB91D10754B0614B4167D6C0498C82510BF37DB4C276BF0EBD81CA14AB6D143)

- 配置泳道范围：勾选ArkTS Snapshot泳道。这将使Allocation在录制结尾时自动抓取一份Snapshot快照用于关联分析。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/d7tNbKaqTIKvfTdjNr8qTg/zh-cn_image_0000002675100559.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=B0481A6BC19FCC1A01CB9C95C53E2CA9BB8244AC24808AD1229CD88DDC19AECE)


 - 启动录制：勾选了“[Local Handle](#table17319174010236)”开关后，如果是在应用本生命周期内首次录制local handle数据，会触发弹窗请求重启应用以便录制对应信息，此时点击OK允许重启即可。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/gZQGeqSRSOq6rWshTEeyrQ/zh-cn_image_0000002675020705.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=79E03E40601A2412660F2B7990BDFCAA30CB4255A23C5CD68B5B9F7636023491)

- 运行应用程序：运行目标应用，执行相关被怀疑引入内存泄漏的业务操作，持续一段时间以增加内存压力和捕获更多数据。
- 停止录制：自动触发抓取一份Snapshot快照用于关联分析。点击快照，查找到疑似泄漏对象Proxy 。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/mKtzfsepQTqJ4fY_adw6EQ/zh-cn_image_0000002645100756.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=2AA06A0AF49F26AB2C62FD20597F3EEF715D4682BBC35C08727143D4BE8B3C73)


 
**2. 配置Allocation录制模板并捕获数据**
 
- 定位可疑ArkTS对象：选中一个怀疑被泄漏的ArkTS对象实例（或对象类型），查看扩展标签页。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/xJuUA_IzSqOO1uCtPY5Qmg/zh-cn_image_0000002644940854.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=427508A1274363C7E31EEACCD2F6A5104427140873FFC66F754B2672A1E7DAA2)

- 查看Native List：若某个ArkTS对象的distance值为1，则可以通过扩展标签页中的Native List标签页，查看所有当前与该JS对象关联的Native句柄引用，以确认该JS对象是被Local Handle或Global Handle引用的对象。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/Q3OLegflQSGR9UMetZy7CA/zh-cn_image_0000002675100561.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=088706A7605DE74DD99104ED6A3E3CBF06CEF1FB0D58E04D9B86A56F43B5B827)

- 关键信息：1. 句柄类型：调用栈底层的符号ArkGlobalHandle或ArkLocalHandle判断泄漏类型。

2. 调用栈：通过调用栈，可以定位到应用的Native代码（可能是ArkUI框架代码或你自己代码）中创建napi_ref的地方。

3. 注意点：
如果该JS对象节点不是一个被[Local Handle](#table17319174010236)或者[Global Handle](#table17319174010236)引用的对象，则会提示“No Detail”。

4. 如果该JS对象确实是一个被Local Handle或者Global Handle引用的对象，但是对应的native内存的申请事件已经在此次录制之前完成内存分配，本次录制结果则无法展示对应的内存申请调用栈，需要重新录制，录制时需要注意将录制时执行的业务逻辑范围调整的尽量更早一些。

 
**3.**** 分析内存分配调用栈**
 
- 排查调用栈：“Native List”标签页中的调用栈，找到对应业务代码。
- 关键排查点：1. 检查是否在适当的时候调用了对应的句柄释放接口如napi_delete_reference等。

2. 梳理这段Native代码需要引用ArkTS对象的合理性，识别这个引用的生命周期是否过长，是否应该在某个条件满足后被释放。

3. 对于napi_ref，其引用计数是关键。确保在不再需要引用时正确调用了napi_delete_reference。注意，引用计数可能因其他代码路径的创建或删除操作而意外增减。

4. 检查libuv异步调用等场景，句柄作用域是否正确添加Handle Scope。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/CevNwemMS2uiLPPGlGwuUg/zh-cn_image_0000002675020709.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=22B7E24655B35A9E16F506B3E9B9FEAD407B94BA167675B61E4C77F5BBE02ACA)


 


 
 

#### 优化修复
1. 重新运行应用，再次使用Memory泳道监控。
2. 重复多次进出消息中心页。
3. 验证结果：
内存曲线恢复锯齿状，每次退出后回落至基线。
4. 再次抓取快照对比，多次操作后业务对象实例数量无明显增长。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/XNmdNruDSPaB2U2nkq96Gw/zh-cn_image_0000002645100758.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=DBFC5388EF1843B0CB8DF6311C9570DB5F7D65FDF27C777C6D21C9684BC4351E)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/uEIlh2MtTlCklvHMENsx3Q/zh-cn_image_0000002644940856.png?HW-CC-KV=V1&HW-CC-Date=20260730T072737Z&HW-CC-Expire=86400&HW-CC-Sign=2785127D03A2944EF3768DAE300BBFF8D61B867F47215FF08ACCA4C5A4EE5174)

 
 

#### 术语介绍
 
| 术语 | 解释 |
| --- | --- |
| GC Root | GC Root（Garbage Collection Root，垃圾回收引用链根节点） 是垃圾回收器进行可达性分析的起点。从GC Root能访问到的节点对象是“存活的”，否则会被回收。 |
| 引用链 | 在ArkTS中，“引用链”就是从某个GC Root（如VMRoot、FrameRoot等）出发，经过一连串的对象引用，最终到达目标对象的路径。 如果这个路径存在，则该对象是“存活”的，不会被GC回收； 如果从任何GC Root都无法找到一条到达该对象的引用链，该对象就是“不可达”的，会被标记为垃圾对象并回收。 |
| VMRoot | VMRoot是ArkTS虚拟机层面的根引用集合，代表GC遍历的起点。 |
| FrameRoot | FrameRoot是函数调用栈帧在GC遍历过程中的根节点。当函数被调用时，其局部变量和入参对象会被当前栈帧引用，从而成为GC的“可达”起点。 |
| Local Handle | Local Handle（本地句柄）是一种短期引用，用于在本地作用域（如函数调用栈）内持有对象，防止对象被垃圾回收。当作用域结束时，这些句柄会自动释放。 |
| Global Handle | Global Handle（全局句柄）例如napi_ref，用于长期持有对象引用，确保在对象生命周期内不会被垃圾回收机制回收。使用此类句柄时，开发者需要手动管理其生命周期，包括创建和销毁，以避免潜在的内存泄漏问题。 |
