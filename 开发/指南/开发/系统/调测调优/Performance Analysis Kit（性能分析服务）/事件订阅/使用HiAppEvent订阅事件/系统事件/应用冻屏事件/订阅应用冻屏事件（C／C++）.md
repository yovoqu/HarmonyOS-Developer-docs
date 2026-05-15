# 订阅应用冻屏事件（C/C++）

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events-ndk

## 简介

本文介绍如何使用HiAppEvent提供的C/C++接口订阅应用冻屏事件。接口的详细使用说明（参数限制、取值范围等）请参考[hiappevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。

## 接口说明


| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher *watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher *watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |


## 开发步骤


## 添加事件观察者

以订阅应用冻屏事件为例，说明开发步骤。 获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。 新建Native C++工程，并将jsoncpp导入到新建工程内，目录结构如下。
```text
entry:
  src:
    main:
      cpp:
        json:
          - json.h
          - json-forwards.h
        types:
          libentry:
            - index.d.ts
        - CMakeLists.txt
        - jsoncpp.cpp
        - napi_init.cpp
      ets:
        entryability:
          - EntryAbility.ets
        pages:
          - Index.ets
```

编辑“CMakeLists.txt”文件，添加源文件及动态库。
```text
# 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
# 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
```

编辑“napi_init.cpp”文件，导入依赖的文件，并定义LOG_TAG。
```text
#include "napi/native_api.h"
#include "json/json.h"
#include "hilog/log.h"
#include "hiappevent/hiappevent.h"

#undef LOG_TAG
#define LOG_TAG "testTag"
```

订阅系统事件。 onReceive类型观察者 编辑“napi_init.cpp”文件，定义onReceive类型观察者相关方法：
```text
// 定义一个变量，用来缓存创建的观察者的指针。
static HiAppEvent_Watcher *systemEventWatcher;

static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
    for (int i = 0; i                  onTrigger类型观察者         编辑“napi_init.cpp”文件，定义OnTrigger类型观察者相关方法：
```text
// 定义一个变量，用来缓存创建的观察者的指针。
static HiAppEvent_Watcher *systemEventWatcher;

// 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
static void OnTake(const char *const *events, uint32_t eventLen) {
Json::Reader reader(Json::Features::strictMode());
Json::FastWriter writer;
for (int i = 0; i 将RegisterWatcher注册为ArkTS接口。 编辑“napi_init.cpp”文件，将RegisterWatcher注册为ArkTS接口：
```text
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        { "registerWatcher", nullptr, RegisterWatcher, nullptr, nullptr, nullptr, napi_default, nullptr }
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
```

编辑“index.d.ts”文件，定义ArkTS接口：
```text
export const registerWatcher: () => void;
```

编辑“EntryAbility.ets”文件，在onCreate()函数中新增接口调用。
```text
// 导入依赖模块
import testNapi from 'libentry.so'

// 在onCreate()函数中新增接口调用
// 启动时，注册系统事件观察者
testNapi.registerWatcher();
```

编辑“Index.ets”文件，新增按钮触发卡顿事件。
```text
Button("appFreeze").onClick(() => {
  setTimeout(()=>{
    while(true) {}
  }, 1000)
})
```

点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“appFreeze”，触发一次应用无响应事件。

## 验证观察者是否订阅到应用无响应事件

应用工程崩溃退出后再次运行可以在Log窗口看到对系统事件数据的处理日志。
```text
HiAppEvent eventInfo.domain=OS
HiAppEvent eventInfo.name=APP_FREEZE
HiAppEvent eventInfo.eventType=1
HiAppEvent eventInfo.params.time=1502049167732
HiAppEvent eventInfo.params.foreground=1
HiAppEvent eventInfo.params.app_running_unique_id=382145346984526931478
HiAppEvent eventInfo.params.bundle_version=1.0.0
HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
HiAppEvent eventInfo.params.process_name=com.example.myapplication
HiAppEvent eventInfo.params.pid=1587
HiAppEvent eventInfo.params.uid=20010043
HiAppEvent eventInfo.params.uuid=a78a23b20f3dd9730f18a5cfa2304deac1104ac4086755c4a59cf7c72d414e2e
HiAppEvent eventInfo.params.exception={"message":"App main thread is not response!","name":"THREAD_BLOCK_6S"}
HiAppEvent eventInfo.params.hilog.size=6
HiAppEvent eventInfo.params.event_handler.size=16
HiAppEvent eventInfo.params.event_handler_3s.size=15
HiAppEvent eventInfo.params.event_handler_6s.size=16
HiAppEvent eventInfo.params.peer_binder.size=0
HiAppEvent eventInfo.params.threads.size=28
HiAppEvent eventInfo.params.memory={"pss":0,"rss":0,"sys_avail_mem":1326520,"sys_free_mem":940588,"sys_total_mem":1992340,"vm_heap_total_size":"9961472","vm_heap_used_size":"7596424","vss":0}
HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_FREEZE_1502049185239_1587.log"]
HiAppEvent eventInfo.params.log_over_limit=0
HiAppEvent eventInfo.params.process_life_time=18
HiAppEvent eventInfo.params.external_callback_log=THREAD_BLOCK_3S:log3s THREAD_BLOCK_6S:log6s
```

若应用无法启动或长时间未启动，开发者可以参考[使用FaultLogExtensionAbility订阅事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fault-log-extension-app-events-arkts)回调重写的函数，进行延迟上报。

## 移除并销毁事件观察者

移除事件观察者。
```text
static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
    // 使观察者停止监听事件
    OH_HiAppEvent_RemoveWatcher(systemEventWatcher);
    return {};
}
```

销毁事件观察者。
```text
static napi_value DestroyWatcher(napi_env env, napi_callback_info info) {
    // 销毁创建的观察者，并置systemEventWatcher为nullptr。
    OH_HiAppEvent_DestroyWatcher(systemEventWatcher);
    systemEventWatcher = nullptr;
    return {};
}
```
