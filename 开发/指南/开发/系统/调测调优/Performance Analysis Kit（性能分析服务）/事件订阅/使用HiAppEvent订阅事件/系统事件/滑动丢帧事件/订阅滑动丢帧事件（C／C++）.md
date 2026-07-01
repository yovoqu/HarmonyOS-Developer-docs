# 订阅滑动丢帧事件（C/C++）

更新时间：2026-06-12 06:54:11

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-scroll-jank-c

## 订阅滑动丢帧事件（C/C++）
 
 

##### 接口说明

本文介绍如何使用HiAppEvent提供的C/C++接口订阅滑动丢帧事件。详细使用说明请参考[HiAppEvent C API文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。
  
| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher *watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher *watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |
 
 
  

##### 开发步骤

- 获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README中Amalgamated source的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。
- 新建Native C++工程，并将上述文件导入到新建工程，目录结构如下。
  
```ArkTS
entry:
  src:
    main:
      cpp:
 - json:
 - json.h
 - json-forwards.h
 - types:
            libentry:
 - index.d.ts
 - CMakeLists.txt
 - napi_init.cpp
 - jsoncpp.cpp
      ets:
 - entryability:
 - EntryAbility.ets
 - pages:
 - Index.ets
```

- 在“CMakeLists.txt”文件中，添加源文件和动态库。
  
```text
# 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
# 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
```

- 在“napi_init.cpp”文件中，导入依赖文件，并定义LOG_TAG。
  
```text
#include "napi/native_api.h"
#include "json/json.h"
#include "hilog/log.h"
#include "hiappevent/hiappevent.h"

#undef LOG_TAG
#define LOG_TAG "testTag"
```

- 订阅系统事件。
  
onReceive类型观察者，在“napi_init.cpp”文件中，定义onReceive类型观察者的方法：

  
```text
static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen)
{
    for (int i = 0; i - 将RegisterWatcher注册为ArkTS接口。
  
在“napi_init.cpp”文件中，将RegisterWatcher注册为ArkTS接口：

  
```text
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        { "registerWatcherReceive", nullptr, RegisterWatcherReceive, nullptr, nullptr, nullptr, napi_default, nullptr },
        { "registerWatcherTrigger", nullptr, RegisterWatcherTrigger, nullptr, nullptr, nullptr, napi_default, nullptr },
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
```
  
- 在“index.d.ts”文件中，定义ArkTS接口：

  
```text
export const registerWatcherReceive: () => void;
export const registerWatcherTrigger: () => void;
```
 - 在“EntryAbility.ets”文件的onCreate()函数中添加接口调用。
  
```text
// 导入依赖模块
import testNapi from 'libentry.so';
// 在onCreate()函数中新增接口调用
// 启动时，注册系统事件观察者
testNapi.registerWatcherReceive();
testNapi.registerWatcherTrigger();
```

- 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加一个List组件，在列表的滑动事件中添加耗时操作，示例代码如下：
  
```text
struct Index {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
  build() {
    List({ space: 10 }) {
      ForEach(this.arr, (item: number) => {
        ListItem() {
          Text(`${item}`)
            .width('100%')
            .height(100)
            .fontSize(20)
            .fontColor(Color.White)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0x007DFF)
        }
      })
    }
    .onScrollIndex((firstIndex: number) => {
      let i = 1;
      while (i
