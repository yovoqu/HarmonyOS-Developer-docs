# 订阅任务执行超时事件（C/C++）

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-apphicollie-events-ndk

##### 简介

本文介绍如何使用HiAppEvent提供的C/C++接口订阅任务执行超时事件。接口的详细使用说明（参数限制、取值范围等）请参考[hiappevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。



##### 接口说明

| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher *watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher *watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |




##### 开发步骤



##### 添加事件观察者

以实现对用户点击按钮触发卡顿场景生成的卡顿事件订阅为例，说明开发步骤。
1. 获取该示例工程依赖的jsoncpp文件，打开链接[HiAppEvent示例工程EventSub](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/PerformanceAnalysisKit/HiAppEvent/EventSub)，点击“下载当前目录”，下载EventSub工程文件。
2. 新建Native C++工程，从解压后的EventSub工程中拷贝jsoncpp库文件（entry/libs和entry/src/main/cpp/thirdparty文件夹）到新建的工程之中，新工程目录结构如下：

  
```ArkTS
entry:
  libs:    //  放置jsoncpp关联三方库的文件夹
  src:
    main:
      cpp:
        thirdparty:
          jsoncpp:    //  放置jsoncpp关联三方库的文件夹
        types:
          libentry:
            - index.d.ts
        - CMakeLists.txt
        - napi_init.cpp
      ets:
        entryability:
          - EntryAbility.ets
        pages:
          - Index.ets
```
该示例工程中jsoncpp库文件对应的源码来自[三方开源库jsoncpp](https://github.com/open-source-parsers/jsoncpp/archive/refs/tags/1.9.6.tar.gz)。
3. 编辑“CMakeLists.txt”文件，添加所需源文件及动态库。

  
```cpp
add_library(entry SHARED napi_init.cpp)
# 新增动态库依赖libhiappevent_ndk.z.so、libhilog_ndk.z.so（日志输出）及libohhicollie.so（hicollie检测）
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libohhicollie.so libhiappevent_ndk.z.so)

set(GZ_FILE "${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/src/jsoncpp-1.9.6.tar.gz")
set(DEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../build")
# 检查是否存在entry/build目录
execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${DEST_DIR})
# 解压jsoncpp-1.9.6.tar.gz到entry/build，得到jsoncpp头文件的目录
execute_process(COMMAND tar -xzf ${GZ_FILE} -C ${DEST_DIR}
    WORKING_DIRECTORY ${DEST_DIR})

# 新增三方库依赖libjsoncpp.so(解析订阅事件中的json字符串)
target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/${OHOS_ARCH}/lib/libjsoncpp.so)
target_include_directories(entry PRIVATE ${DEST_DIR}/jsoncpp-1.9.6/include/json)
```

4. 编辑“napi_init.cpp”文件，导入依赖的头文件，并定义LOG_TAG。

  
```cpp
#include "napi/native_api.h"
// 根据工程中三方库jsoncpp的位置适配引用json.h的路径
#include "../../../build/jsoncpp-1.9.6/include/json/json.h"
#include "hiappevent/hiappevent.h"
#include "hilog/log.h"

#undef LOG_TAG
#define LOG_TAG "testTag"
```

5. 订阅系统事件：

  
onReceive类型观察者
6. onTrigger类型观察者
7. 新增TestHiCollieTimerNdk函数。

  编辑“napi_init.cpp”文件，新增TestHiCollieTimerNdk函数，构造任务执行超时事件：

  
```cpp
#include <unistd.h>
#include "hicollie/hicollie.h"
```

```cpp
// 定义回调函数
void CallBack(void*)
{
    OH_LOG_INFO(LogType::LOG_APP, "HiCollieTimerNdk CallBack");  // 回调函数中打印日志
}

static napi_value TestHiCollieTimerNdk(napi_env env, napi_callback_info info)
{
    int id;
    // 设置HiCollieTimer 参数（Timer任务名，超时时间，回调函数，回调函数参数，超时发生后行为）
    HiCollie_SetTimerParam param = {"testTimer", 1, CallBack, nullptr, HiCollie_Flag::HICOLLIE_FLAG_LOG};
    HiCollie_ErrorCode errorCode = OH_HiCollie_SetTimer(param, &id);  // 注册HiCollieTimer函数执行时长超时检测一次性任务
    if (errorCode == HICOLLIE_SUCCESS) {  // HiCollieTimer任务注册成功
        OH_LOG_INFO(LogType::LOG_APP, "HiCollieTimer taskId: %{public}d", id); // 打印任务id
        sleep(2);  // 模拟执行耗时函数，在这里简单的将线程阻塞2s
        OH_HiCollie_CancelTimer(id);  // 根据id取消已注册任务
    }
    return nullptr;
}
```

8. 将RegisterWatcher及TestHiCollieTimerNdk注册为ArkTS接口。

  编辑“napi_init.cpp”文件，在Init函数中的desc[]数组中将TestHiCollieTimerNdk、RegisterAppHicollieWatcherR及RegisterAppHicollieWatcherR方法注册为ArkTS接口。

  
```cpp
// 将TestHiCollieTimerNdk注册为ArkTS接口
{ "TestHiCollieTimerNdk", nullptr, TestHiCollieTimerNdk, nullptr, nullptr, nullptr, napi_default, nullptr },
```

```cpp
{ "RegisterAppHicollieWatcherR", nullptr, RegisterAppHicollieWatcherR, nullptr, nullptr, nullptr,
    napi_default, nullptr },
```

```cpp
{ "RegisterAppHicollieWatcherT", nullptr, RegisterAppHicollieWatcherT, nullptr, nullptr, nullptr,
    napi_default, nullptr },
```
编辑“index.d.ts”文件，定义ArkTS接口：

  
```ts
export const TestHiCollieTimerNdk: () => void;
```

```ts
export const RegisterAppHicollieWatcherR: () => void;
```

```ts
export const RegisterAppHicollieWatcherT: () => void;
```

9. 编辑“EntryAbility.ets”文件，在onCreate()函数中新增接口调用。

  
```ArkTS
import testNapi from 'libentry.so';
```

```ArkTS
// 在onCreate()函数中新增接口调用，启动时注册系统事件观察者R
testNapi.RegisterAppHicollieWatcherR();
```

```ArkTS
// 在onCreate()函数中新增接口调用，启动时注册系统事件观察者T
testNapi.RegisterAppHicollieWatcherT();
```

10. 编辑“Index.ets”文件，新增按钮触发任务执行超时事件。

  
```ArkTS
import testNapi from 'libentry.so';
```
在Index页面新增触发TestHiCollieTimerNdk方法的按钮。

  
```ArkTS
// 添加点击事件，触发TestHiCollieTimerNdk方法。
Button('TestHiCollieTimerNdk')
  .type(ButtonType.Capsule)
  .margin({
    top: 20
  })
  .backgroundColor('#0D9FFB')
  .width('80%')
  .height('5%')
  .onClick(() => {
    testNapi.TestHiCollieTimerNdk();
  })
```

11. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“TestHiCollieTimerNdk”，触发任务执行超时事件。



##### 验证观察者是否订阅到任务执行超时事件

应用工程崩溃退出后再次运行可以在Log窗口看到对系统事件数据的处理日志。

```text
HiAppEvent eventInfo.domain=OS
HiAppEvent eventInfo.name=APP_HICOLLIE
HiAppEvent eventInfo.eventType=1
HiAppEvent eventInfo.params.time=1740993639620
HiAppEvent eventInfo.params.foreground=1
HiAppEvent eventInfo.params.bundle_version=1.0.0
HiAppEvent eventInfo.params.process_name=com.example.myapplication
HiAppEvent eventInfo.params.pid=26251
HiAppEvent eventInfo.params.uid=20020172
HiAppEvent eventInfo.params.uuid=4e5d7d0e18f5d6d84cf4f0c9e80d66d0b646c1cc2343d3595f07abb0d3547feb
HiAppEvent eventInfo.params.exception={"message":"","name":"APP_HICOLLIE"}
HiAppEvent eventInfo.params.hilog.size=77
HiAppEvent eventInfo.params.peer_binder.size=18
HiAppEvent eventInfo.params.memory={"pss":0,"rss":124668,"sys_avail_mem":2220032,"sys_free_mem":526680,"sys_total_mem":11692576,"vss":4238700}
HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_HICOLLIE_1740993644458_26215.log"]
HiAppEvent eventInfo.params.log_over_limit=0
HiAppEvent eventInfo.params.external_callback_log=THREAD_BLOCK_3S:log3s THREAD_BLOCK_6S:log6s
```



##### 移除并销毁事件观察者
1. 移除事件观察者。

  
```cpp
static napi_value RemoveWatcher(napi_env env, napi_callback_info info)
{
    // 使观察者停止监听事件
    // ···
    OH_HiAppEvent_RemoveWatcher(appHicollieWatcherR);
    OH_HiAppEvent_RemoveWatcher(appHicollieWatcherT);
    // ···
    return {};
}
```

2. 销毁事件观察者。

  
```cpp
static napi_value DestroyWatcher(napi_env env, napi_callback_info info)
{
    // 销毁创建的观察者，并置eventWatcher为nullptr。
    // ···
    OH_HiAppEvent_DestroyWatcher(appHicollieWatcherR);
    OH_HiAppEvent_DestroyWatcher(appHicollieWatcherT);
    appHicollieWatcherR = nullptr;
    appHicollieWatcherT = nullptr;
    // ···
    return {};
}
```
