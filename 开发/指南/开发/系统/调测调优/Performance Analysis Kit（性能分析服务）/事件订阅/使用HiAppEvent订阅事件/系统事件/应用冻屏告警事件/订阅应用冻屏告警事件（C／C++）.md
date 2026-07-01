# 订阅应用冻屏告警事件（C/C++）

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-appfreezewarning-events-ndk

## 订阅应用冻屏告警事件（C/C++）
   
    
          
##### 简介
     
本文介绍如何使用HiAppEvent提供的C/C++接口订阅应用冻屏告警事件。接口的详细使用说明（参数限制、取值范围等）请参考[hiappevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。
    
    
          
##### 接口说明
     
| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher *watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher *watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |
     
    
    
          
##### 开发步骤
    
    
          
##### [h2]添加事件观察者
     
以订阅应用冻屏告警事件为例，说明开发步骤。
     
 - 获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。
 - 新建Native C++工程，并将jsoncpp导入到新建工程内，目录结构如下。
       
```ArkTS
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

 - 编辑“CMakeLists.txt”文件，添加源文件及动态库。
       
```text
# 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
# 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
```

 - 编辑“napi_init.cpp”文件，导入依赖的文件，并定义LOG_TAG。
       
```text
#include "napi/native_api.h"
#include "json/json.h"
#include "hilog/log.h"
#include "hiappevent/hiappevent.h"

#undef LOG_TAG
#define LOG_TAG "testTag"
```

 - 订阅系统事件。
       
                 onReceive类型观察者
         编辑“napi_init.cpp”文件，定义onReceive类型观察者相关方法：
         
```text
// 定义一个变量，用来缓存创建的观察者的指针。
static HiAppEvent_Watcher *systemEventWatcher;

static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
    for (int i = 0; i       - 将RegisterWatcher注册为ArkTS接口。
       编辑“napi_init.cpp”文件，将RegisterWatcher注册为ArkTS接口：
       
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

 - 编辑“EntryAbility.ets”文件，在onCreate()函数中新增接口调用。
       
```text
// 导入依赖模块
import testNapi from 'libentry.so'

// 在onCreate()函数中新增接口调用
// 启动时，注册系统事件观察者
testNapi.registerWatcher();
```

 - 编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，新增按钮触发冻屏告警事件。示例代码如下：
       
```text
@Entry
  @Component
  struct Index {
    build() {
      RelativeContainer() {
        Column() {
          Button("appFreezeWarning", { stateEffect:true, type: ButtonType.Capsule})
            .width('75%')
            .height(50)
            .margin(15)
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
             // 在按钮点击函数中构造一个appFreezeWarning场景，触发应用冻屏告警事件
              const t = Date.now();
              while (Date.now() - t      
##### [h2]验证观察者是否订阅到应用冻屏告警事件
     
等待约一分钟后，可以在Log窗口看到对系统事件数据的处理日志。
     
```text
HiAppEvent eventInfo.domain=OS
HiAppEvent eventInfo.name=APPFREEZE_WARNING
HiAppEvent eventInfo.eventType=1
HiAppEvent eventInfo.params.time=1776946769389
HiAppEvent eventInfo.params.foreground=1
HiAppEvent eventInfo.params.app_running_unique_id=382145346984526931478
HiAppEvent eventInfo.params.bundle_version=1.0.0
HiAppEvent eventInfo.params.bundle_version_code=1000000
HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
HiAppEvent eventInfo.params.process_name=com.example.myapplication
HiAppEvent eventInfo.params.pid=1587
HiAppEvent eventInfo.params.uid=20010043
HiAppEvent eventInfo.params.exception={""message":"App main thread is not response!Main handler dump start time: 2026-04-23 20:19:28.903","name":"THREAD_BLOCK_3S"}
HiAppEvent eventInfo.params.hilog.size=6
HiAppEvent eventInfo.params.event_handler.size=16
HiAppEvent eventInfo.params.peer_binder.size=0
HiAppEvent eventInfo.params.threads.size=28
HiAppEvent eventInfo.params.memory={"rss":161080,"sys_avail_mem":1361464,"sys_free_mem":796232,"sys_total_mem":1992340,"vm_heap_total_size":"9961472","vm_heap_used_size":"7596424","vss":56960692}
HiAppEvent eventInfo.params.process_life_time=18
```
    
    
          
##### [h2]移除并销毁事件观察者
     
 - 移除事件观察者。
       
```text
static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
    // 使观察者停止监听事件
    OH_HiAppEvent_RemoveWatcher(systemEventWatcher);
    return {};
}
```

 - 销毁事件观察者。
       
```text
static napi_value DestroyWatcher(napi_env env, napi_callback_info info) {
    // 销毁创建的观察者，并置systemEventWatcher为nullptr。
    OH_HiAppEvent_DestroyWatcher(systemEventWatcher);
    systemEventWatcher = nullptr;
    return {};
}
```
