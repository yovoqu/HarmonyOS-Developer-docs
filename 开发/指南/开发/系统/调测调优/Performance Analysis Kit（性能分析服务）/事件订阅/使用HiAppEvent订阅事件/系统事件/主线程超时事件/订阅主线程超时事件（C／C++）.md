# 订阅主线程超时事件（C/C++）

更新时间：2026-03-12 09:39:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events-ndk

## 简介

本文介绍如何使用HiAppEvent提供的C/C++接口订阅主线程超时事件。接口的详细使用说明（参数限制、取值范围等）请参考[hiappevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。

## 接口说明


| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher *watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher *watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |


## 开发步骤


## 添加事件观察者

获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。 新建Native C++工程，并将上述文件导入到新建工程内，目录结构如下。
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
#include "hiappevent/hiappevent_event.h"
#undef LOG_TAG
#define LOG_TAG "testTag"
```

订阅系统事件。 onReceive类型观察者 编辑“napi_init.cpp”文件，定义onReceive类型观察者相关方法：
```text
// 定义一个变量，用来缓存创建的观察者的指针。
static HiAppEvent_Watcher *systemEventWatcher;

static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
    for (int i = 0; i                     将RegisterWatcher注册为ArkTS接口。       编辑“napi_init.cpp”文件，将RegisterWatcher注册为ArkTS接口：
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

             编辑工程中的“entry > src > main > ets > entryability> EntryAbility.ets”文件，在onCreate()函数中新增接口调用。
```text
// 导入依赖模块
import testNapi from 'libentry.so';

// 在onCreate()函数中新增接口调用
// 启动时，注册系统事件观察者
testNapi.registerWatcher();
```

             编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，添加一个Button按钮，并在其onClick函数中模拟触发主线程超时场景，示例代码如下：
```text
Button("timeOut350")
.fontSize(50)
.fontWeight(FontWeight.Bold)
.onClick(() => {
let t = Date.now();
while (Date.now() - t 点击DevEco Studio界面中的运行按钮，运行应用工程，可以快速点击2~3次timeOut350按钮，以触发主线程超时事件。

## 验证观察者是否订阅到主线程超时事件

主线程超时事件上报后，可以在Log窗口看到对系统事件数据的处理日志：
```text
HiAppEvent eventInfo.domain=OS
  HiAppEvent eventInfo.name=MAIN_THREAD_JANK
  HiAppEvent eventInfo.eventType=1
  HiAppEvent eventInfo.params.time=1717597063727
  HiAppEvent eventInfo.params.pid=45572
  HiAppEvent eventInfo.params.uid=20020151
  HiAppEvent eventInfo.params.bundle_name=com.example.nativemainthread
  HiAppEvent eventInfo.params.bundle_version=1.0.0
  HiAppEvent eventInfo.params.begin_time=1717597063225
  HiAppEvent eventInfo.params.end_time=1717597063727
  HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/watchdog/MAIN_THREAD_JANK_20240613221239_45572.txt"]
  HiAppEvent eventInfo.params.log_over_limit=0
```


> [!NOTE]
> 主线程超时事件具体规格可参考：主线程超时事件默认时间规格 和 主线程超时事件日志规格。


## 移除并销毁事件观察者

移除事件观察者：
```text
static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
    // 使观察者停止监听事件
    OH_HiAppEvent_RemoveWatcher(systemEventWatcher);
    return {};
}
```

销毁事件观察者：
```text
static napi_value DestroyWatcher(napi_env env, napi_callback_info info) {
    // 销毁创建的观察者，并置systemEventWatcher为nullptr。
    OH_HiAppEvent_DestroyWatcher(systemEventWatcher);
    systemEventWatcher = nullptr;
    return {};
}
```
