# 使用HiCollie检测业务线程卡死卡顿问题（C/C++）

更新时间：2026-05-07 09:37:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hicollie-guidelines-ndk

#### 简介

用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为[应用冻屏](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines)。本文面向开发者介绍HiCollie模块对外提供检测业务线程卡死、卡顿，以及上报卡死事件的能力。



#### 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH_HiCollie_Init_StuckDetection | 注册应用业务线程卡死的周期性检测任务。用户实现回调函数, 用于定时检测业务线程卡死情况。 默认检测时间：3s上报BUSSINESS_THREAD_BLOCK_3S告警事件，6s上报BUSSINESS_THREAD_BLOCK_6S卡死事件。 说明：在非主线程使用该接口。 |
| OH_HiCollie_Init_StuckDetectionWithTimeout | 注册应用业务线程卡死的周期性检测任务。用户实现回调函数, 用于定时检测业务线程卡死情况。 开发者可以设置卡死检测时间，可设置的时间范围：[3, 15]，单位：s。 说明： - 在非主线程使用该接口。 - 从API version 18开始，支持该接口。 |
| OH_HiCollie_Init_JankDetection | 注册应用业务线程卡顿检测的回调函数。 线程卡顿监控功能需要开发者实现两个卡顿检测回调函数，分别放在业务线程处理事件的前后。作为插桩函数，监控业务线程处理事件执行情况。 说明：在非主线程使用该接口。 |
| OH_HiCollie_Report | 上报应用业务线程卡死事件，生成卡死故障日志，辅助定位应用卡死问题。 先调用OH_HiCollie_Init_StuckDetection或OH_HiCollie_Init_StuckDetectionWithTimeout接口，初始化检测的task。 如果task任务超时，结合业务逻辑，调用OH_HiCollie_Report接口上报卡死事件。 说明： - 在非主线程使用该接口。 - 该接口仅对release版本应用生效，对debug版本应用不生效。 |
| OH_HiCollie_ReportInputBlock | 上报应用输入无响应事件，生成卡死故障日志，辅助定位应用卡死问题。如果在PC或平板设备上，还会弹窗提示用户继续等待或关闭应用，其他设备不会弹窗。建议如下两种方式使用该接口。 方式一（推荐）：配合OH_HiCollie_Report、OH_HiCollie_Init_StuckDetection或OH_HiCollie_Init_StuckDetectionWithTimeout接口使用，业务线程通过上述接口周期性检测自身卡死情况，当满足业务线程卡死且有输入事件（如屏幕点击、鼠标点击、键盘输入等）条件时再调用OH_HiCollie_ReportInputBlock接口。 方式二：业务线程不通过OH_HiCollie_Report、OH_HiCollie_Init_StuckDetection或OH_HiCollie_Init_StuckDetectionWithTimeout接口也能检测自身卡死情况，则应用结合业务线程卡死情况和输入事件再调用OH_HiCollie_ReportInputBlock接口。 说明： - 该接口可以在主线程使用，比如输入事件需要先经过主线程再封装传递给业务线程处理，业务线程卡死时维护一个状态标志位，主线程结合业务线程的卡死状态标志位和输入事件再调用该接口。 - 该接口仅对release版本应用生效，对debug版本应用不生效。 - 从API version 24开始，支持该接口。 |
| OH_HiCollie_SetFreezeCallback | 将冻屏回调设置进系统，系统将在冻屏事件发生时回调此函数。 说明：从API version 24开始，支持该接口。 |
| OH_HiCollie_AssociateProcessReport | 主动报告一个进程的冻屏事件。此时会生成应用执行超时事件事件。 说明：从API version 24开始，支持该接口。 |


API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[HiCollie](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-h)。



#### 检测原理
1. 业务线程卡顿OH_HiCollie_Init_JankDetection故障规格，请参考[主线程超时事件检测原理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events#检测原理)。
2. 业务线程卡死故障：

  （1）OH_HiCollie_Init_StuckDetection检测原理：应用的watchdog线程会周期性进行业务线程判活检测。当判活检测超过3s没有被执行，上报BUSSINESS_THREAD_BLOCK_3S线程告警事件；超过6s依然没有被执行，上报BUSSINESS_THREAD_BLOCK_6S线程卡死事件。两个事件根据系统匹配规则生成appfreeze故障日志。

  （2）OH_HiCollie_Init_StuckDetectionWithTimeout检测原理：应用的watchdog线程会周期性进行业务线程判活检测。当判活检测超过stuckTimeout时间没有被执行，上报BUSSINESS_THREAD_BLOCK_3S告警事件；超过stuckTimeout * 2时间，依然没有被执行，上报BUSSINESS_THREAD_BLOCK_6S线程卡死事件。两个事件匹配生成appfreeze故障日志。


![](assets/使用HiCollie检测业务线程卡死卡顿问题（C／C++）/file-20260514131420108-0.png)


当开发者通过DevEco Studio的Debug按钮安装并启动应用时，会自动关闭当前工程的超时检测机制。避免调试过程出现超时检测影响开发者调试。





#### 日志规格
1. 业务线程卡死故障日志以appfreeze-开头，生成在“设备/data/log/faultlog/faultlogger/”路径下。该日志文件名格式为“appfreeze-应用包名-应用UID-毫秒级时间”。具体规格可参考[应用冻屏（AppFreeze）日志规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines#日志规格)。
2. OH_HiCollie_Init_StuckDetection日志规格，请参考[主线程超时事件日志规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/apptask-timeout-guidelines#日志规格)。



#### 开发步骤

下文将展示如何在应用内增加一个按钮，并单击该按钮以调用HiCollie Ndk接口。
1. 新建Native C++工程，目录结构如下：

  
```ArkTS
entry:
  src:
    main:
      cpp:
        types:
          libentry:
            - index.d.ts
        - CMakeLists.txt
        - napi_init.cpp
      ets:
        entryability:
          - EntryAbility.ts
        pages:
          - Index.ets
```

2. 编辑“CMakeLists.txt”文件，添加源文件及动态库：

  
```text
# 新增动态库依赖libhilog_ndk.z.so(日志输出)
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libohhicollie.so)
```

3. 编辑“napi_init.cpp”文件，导入依赖的文件，定义LOG_TAG，下述代码步骤用于模拟卡死卡顿场景，具体使用请结合业务需要。示例代码如下：

  
从API version 12开始，支持**应用线程卡顿检测**：OH_HiCollie_Init_JankDetection，示例代码如下：
4. 从API version 12开始，支持**应用线程卡死检测**： OH_HiCollie_Init_StuckDetection, 示例代码如下：
5. 从API version 18开始，支持**应用线程卡死检测，自定义检测时间**：OH_HiCollie_Init_StuckDetectionWithTimeout，示例代码如下：
6. 从API version 24开始，支持**应用线程卡死检测，应用主动上报输入无响应故障**：OH_HiCollie_ReportInputBlock，示例代码如下：
7. 从API version 24开始，支持**应用线程卡死检测，三方框架生成自定义日志**：OH_HiCollie_SetFreezeCallback、OH_HiCollie_AssociateProcessReport，示例代码如下：
8. 将TestHiCollieNdk注册为ArkTS接口。

  
OH_HiCollie_Init_JankDetection示例，编辑“index.d.ts”文件，定义ArkTS接口：
9. OH_HiCollie_Init_StuckDetection示例，编辑“index.d.ts”文件，定义ArkTS接口：
10. OH_HiCollie_Init_StuckDetectionWithTimeout示例，编辑“index.d.ts”文件，定义ArkTS接口：
11. OH_HiCollie_ReportInputBlock示例，编辑“index.d.ts”文件，定义ArkTS接口：
12. OH_HiCollie_SetFreezeCallbac、OH_HiCollie_AssociateProcessReport示例，编辑“index.d.ts”文件，定义ArkTS接口：
13. 编辑“Index.ets”文件：

  
```text
import testNapi from 'libentry.so'

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Column() {
        // 选择下方对应的功能，可在此处添加不同的点击事件
        
      }
      .width('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

添加点击事件，触发OH_HiCollie_Init_JankDetection方法。
14. 添加点击事件，触发OH_HiCollie_Init_StuckDetection方法。
15. 添加点击事件，触发OH_HiCollie_Init_StuckDetectionWithTimeout方法。
16. 添加点击事件，触发OH_HiCollie_Init_StuckDetectionWithTimeout方法和OH_HiCollie_ReportInputBlock方法。
17. 添加点击事件，触发OH_HiCollie_SetFreezeCallback方法和OH_HiCollie_AssociateProcessReport方法。
18. 点击DevEco Studio界面中的运行按钮，运行应用工程。
19. 在DevEco Studio的底部，切换到“Log”窗口，过滤自定义的LOG_TAG。

  
点击“testHiCollieJankNdk”按钮。
20. 点击“testHiCollieStuckNdk”按钮。
21. 点击“testHiCollieStuckWithTimeoutNdk”按钮。
22. 先点击“testHiCollieStuckNdk”按钮，再持续点击“testHiCollieInputBlock”按钮。
23. 先点击“testHiCollieSetFreezeCallback”按钮，再点击“testHiCollieAssociateProcessReport”按钮。
