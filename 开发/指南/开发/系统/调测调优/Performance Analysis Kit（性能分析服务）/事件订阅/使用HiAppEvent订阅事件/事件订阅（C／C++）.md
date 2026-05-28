# 事件订阅（C/C++）

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-events-ndk

HiAppEvent提供了事件订阅接口，用于订阅并接收应用产生的事件。


##### 接口说明

API接口的使用说明，包括参数使用限制和取值范围，请参考[hiappevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。

**订阅接口功能介绍**：

| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher* watcher) | 添加应用的事件观察者。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher* watcher) | 移除应用的事件观察者。 |


**打点接口功能介绍**：

| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_Write(const char* domain, const char* name, enum EventType type, const ParamList list) | 实现对参数为列表类型的应用事件打点。 |




##### 事件订阅开发指导

以订阅崩溃事件（系统事件）和按钮点击事件（应用事件）为例，说明开发步骤。



##### 步骤一：新建工程及编译配置
1. 将示例工程依赖的jsoncpp库文件复制到新建工程中。

  打开链接[HiAppEvent示例工程EventSub](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/PerformanceAnalysisKit/HiAppEvent/EventSub)，并点击“下载当前目录”，下载EventSub工程文件。

  新建一个Native C++工程。从解压后的EventSub文件夹中拷贝jsoncpp库文件（entry/libs和entry/src/main/cpp/thirdparty整个目录）到新建的工程中，得到的目录结构如下：

  
```ArkTS
entry
├── libs        // 自行创建文件夹,放入相关的三方库
└── src
    ├── main
    │   ├── cpp
    │   │   ├── CMakeLists.txt       // 导入so链接
    │   │   ├── napi_init.cpp        // 功能函数，观察者定义
    │   │   ├── thirdparty    // 自行创建文件夹,放入相关的三方库
    │   │   │   └── jsoncpp
    │   │   └── types
    │   │       └── libentry
    │   │           ├── Index.d.ts        // 定义ArkTS接口
    │   │           └── oh-package.json5
    │   ├── ets
    │   │   ├── entryability
    │   │   │   └── EntryAbility.ets    // 新增接口调用
    │   │   ├── entrybackupability
    │   │   │   └── EntryBackupAbility.ets
    │   │   └── pages
    │   │       └── Index.ets        // 主页
```
该示例工程中jsoncpp库文件对应的源码来自[三方开源库jsoncpp](https://github.com/open-source-parsers/jsoncpp/archive/refs/tags/1.9.6.tar.gz)。
2. 编辑“CMakeLists.txt”文件，添加所需的源文件和动态库。

  
```cpp
set(GZ_FILE "${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/src/jsoncpp-1.9.6.tar.gz")
set(DEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../build")
# 检查是否存在entry/build目录
execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${DEST_DIR})
# 解压jsoncpp-1.9.6.tar.gz到entry/build，得到jsoncpp头文件的目录
execute_process(COMMAND tar -xzf ${GZ_FILE} -C ${DEST_DIR}
    WORKING_DIRECTORY ${DEST_DIR})

add_library(entry SHARED napi_init.cpp)
# 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
# 新增三方库依赖libjsoncpp.so(解析订阅事件中的json字符串)
target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/${OHOS_ARCH}/lib/libjsoncpp.so)
target_include_directories(entry PRIVATE ${DEST_DIR}/jsoncpp-1.9.6/include/json)
```

3. 编辑“napi_init.cpp”文件，导入依赖的文件并定义LOG_TAG：

  
```cpp
#include "napi/native_api.h"
// 根据工程中三方库jsoncpp的位置适配引用json.h的路径
#include "../../../build/jsoncpp-1.9.6/include/json/json.h"
#include "hiappevent/hiappevent.h"
#include "hilog/log.h"

#undef LOG_TAG
#define LOG_TAG "testTag"
```




##### 步骤二：订阅事件
1. 订阅事件。分别使用OnReceive类型观察者、OnTrigger类型观察者的订阅方式。

  
订阅崩溃事件（系统事件），采用OnReceive类型观察者的订阅方式，观察者接收到事件后会立即触发OnReceive()回调。编辑“napi_init.cpp”文件，定义OnReceive类型观察者相关方法：
2. 订阅按钮点击事件（应用事件），采用OnTrigger类型观察者的订阅方式。需满足OH_HiAppEvent_SetTriggerCondition()设置的条件，才能触发OnTrigger()回调。编辑 “napi_init.cpp”文件，定义OnTrigger类型观察者相关方法：
3. 编辑“napi_init.cpp”文件，添加按钮点击事件的打点接口：

  
```cpp
static napi_value WriteAppEvent(napi_env env, napi_callback_info info)
{
    auto params = OH_HiAppEvent_CreateParamList();
    OH_HiAppEvent_AddInt64Param(params, "clickTime", time(nullptr));
    OH_HiAppEvent_Write("button", "click", EventType::BEHAVIOR, params);
    OH_HiAppEvent_DestroyParamList(params);
    OH_LOG_INFO(LogType::LOG_APP, "writeEvent C++ success");
    return {};
}
```

4. 编辑“napi_init.cpp”文件，注册RegisterWatcherCrash()(订阅崩溃事件)、RegisterWatcherClick()（订阅按钮点击事件）、WriteAppEvent()(按钮点击事件打点接口)为ArkTS接口：

  
```cpp
// ...

static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        // ...
        { "registerWatcherCrash", nullptr, RegisterWatcherCrash, nullptr, nullptr, nullptr, napi_default, nullptr },
        { "registerWatcherClick", nullptr, RegisterWatcherClick, nullptr, nullptr, nullptr, napi_default, nullptr },
        { "writeAppEvent", nullptr, WriteAppEvent, nullptr, nullptr, nullptr, napi_default, nullptr },
        // ...
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
```

5. 编辑“index.d.ts”文件，定义ArkTS接口：

  
```ts
export const registerWatcherCrash: () => void;
export const registerWatcherClick: () => void;
export const writeAppEvent: () => void;
```

6. 编辑“EntryAbility.ets”文件，在onCreate()函数中添加接口调用：

  
```ArkTS
import testNapi from 'libentry.so';
```

```ArkTS
// 在onCreate()函数中添加C API接口调用
// 启动时，注册崩溃事件观察者
testNapi.registerWatcherCrash();
// 启动时，注册按钮点击事件观察者
testNapi.registerWatcherClick();
```




##### 步骤三：触发事件

编辑“Index.ets”文件，新增“WatchAppCrash ArkTS&C++”按钮以触发崩溃事件；新增“writeEvent C++”按钮，在按钮点击函数中进行事件打点。示例代码如下：

```ArkTS
import testNapi from 'libentry.so';
```

```ArkTS
Button('WatchAppCrash ArkTS&C++')
  .type(ButtonType.Capsule)
  .margin({
    top: 20
  })
  .backgroundColor('#0D9FFB')
  .width('80%')
  .height('5%')
  .onClick(() => {
    // 在按钮点击函数中构造一个crash场景，触发崩溃事件
    let result: object = JSON.parse('');
  })
```

```ArkTS
Button('writeEvent C++')
  .type(ButtonType.Capsule)
  .margin({
    top: 20
  })
  .backgroundColor('#0D9FFB')
  .width('80%')
  .height('5%')
  .onClick(() => {
    testNapi.writeAppEvent();
  })
```



##### 调测验证
1. 点击DevEco Studio界面中的运行按钮，运行应用工程。在应用界面中点击“WatchAppCrash ArkTS&C++”按钮，触发崩溃事件。应用退出后重新打开应用。
2. 搜索关键字“AppEvents”，在HiLog窗口查看应用处理崩溃事件数据的日志：

  
```text
AppEvents HiAppEvent success to read events with onReceive callback from C API
AppEvents HiAppEvent eventInfo.domain=OS
AppEvents HiAppEvent eventInfo.name=APP_CRASH
AppEvents HiAppEvent eventInfo.eventType=1
AppEvents HiAppEvent eventInfo.params.time=1750946685473
AppEvents HiAppEvent eventInfo.params.bundle_name=com.example.cxxxx
AppEvents HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_CRASH_1750946685805_64003.log"]
```

3. 点击“writeEvent C++”按钮，触发按钮点击事件。搜索关键字“AppEvents”，在HiLog窗口查看应用处理按钮点击事件数据的日志：

  
```text
AppEvents HiAppEvent success to read events with onTrigger callback from C API
AppEvents HiAppEvent eventInfo={"domain_":"button","name_":"click","type_":4,"time_":1750947007108,"tz_":"","pid_":64750,"tid_":64750,"clickTime":1750947007}
AppEvents HiAppEvent eventInfo.domain=button
AppEvents HiAppEvent eventInfo.name=click
AppEvents HiAppEvent eventInfo.eventType=4
AppEvents HiAppEvent eventInfo.params.clickTime=1750947007
```

4. 移除应用的事件观察者：

  
```cpp
static napi_value RemoveWatcher(napi_env env, napi_callback_info info)
{
    // 使观察者停止监听事件
    // ...
    OH_HiAppEvent_RemoveWatcher(eventWatcherT1);
    OH_HiAppEvent_RemoveWatcher(eventWatcherR1);
    // ...
    return {};
}
```

5. 销毁应用的事件观察者：

  
```cpp
static napi_value DestroyWatcher(napi_env env, napi_callback_info info)
{
    // 销毁创建的观察者，并置eventWatcher为nullptr。
    // ...
    OH_HiAppEvent_DestroyWatcher(eventWatcherT1);
    OH_HiAppEvent_DestroyWatcher(eventWatcherR1);
    eventWatcherT1 = nullptr;
    eventWatcherR1 = nullptr;
    // ...
    return {};
}
```
