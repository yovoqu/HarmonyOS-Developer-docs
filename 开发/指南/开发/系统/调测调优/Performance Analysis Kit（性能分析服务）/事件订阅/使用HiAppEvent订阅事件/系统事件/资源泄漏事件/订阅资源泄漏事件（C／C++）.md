# 订阅资源泄漏事件（C/C++）

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events-ndk

## 接口说明

本文介绍如何使用HiAppEvent提供的C/C++接口订阅资源泄漏事件。API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[hiappevent.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h)。 **订阅接口功能介绍**：
| 接口名 | 描述 |
| --- | --- |
| int OH_HiAppEvent_AddWatcher(HiAppEvent_Watcher *watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH_HiAppEvent_RemoveWatcher(HiAppEvent_Watcher *watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |


## 开发步骤


## 步骤一：新建工程

获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。 在DevEco Studio中新建工程，选择“Native C++”工程。目录结构如下：
```text
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

编辑“CMakeLists.txt”文件，添加源文件及动态库：
```text
# 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
# 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
```

编辑“napi_init.cpp”文件，导入依赖文件，并定义LOG_TAG：
```text
#include "napi/native_api.h"
#include "json/json.h"
#include "hilog/log.h"
#include "hiappevent/hiappevent.h"

#undef LOG_TAG
#define LOG_TAG "testTag"
```


## 步骤二：订阅系统事件

订阅系统事件： onReceive类型观察者： 编辑“napi_init.cpp”文件，定义onReceive类型观察者相关方法：
```text
// 定义一个变量，用来缓存创建的观察者的指针。
static HiAppEvent_Watcher *systemEventWatcher;

static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
    for (int i = 0; i                  onTrigger类型观察者：         编辑“napi_init.cpp”文件，定义OnTrigger类型观察者相关方法：
```text
// 定义一个变量，用来缓存创建的观察者的指针。
static HiAppEvent_Watcher *systemEventWatcher;

// 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
static void OnTake(const char *const *events, uint32_t eventLen) {
Json::Reader reader(Json::Features::strictMode());
Json::FastWriter writer;
for (int i = 0; i 将RegisterWatcher注册为ArkTS接口： 编辑“napi_init.cpp”文件，将RegisterWatcher注册为ArkTS接口：
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

编辑“EntryAbility.ets”文件，在onCreate()函数中添加接口调用：
```text
import testNapi from 'libentry.so'
import hidebug from '@kit.PerformanceAnalysisKit'
export default class EntryAbility extends UIAbility {
  onCreate(want, launchParam) {
    // 启动时，注册系统事件观察者
    testNapi.registerWatcher();
  }
}
```


## 步骤三：测试资源泄漏事件

编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加按钮并在其 onClick 函数中构造资源泄漏场景，以触发资源泄漏事件。 此处需要使用[hidebug.setAppResourceLimit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug#hidebugsetappresourcelimit12)设置内存限制，造成内存泄漏，同步在“开发者选项”中打开“系统资源泄漏日志”(开关状态变更后需重启设备)。接口示例代码如下：
```text
Button('pss leak')
    .type(ButtonType.Capsule)
    .margin({
      top: 20
    })
    .backgroundColor('#0D9FFB')
    .width('80%')
    .height('5%')
    .onClick(() => {
      // 设置一个简单的资源泄漏场景
      hilog.info(0x0000, 'testTag', 'click pss leak button');
      testNapi.leakMB(3072);
    })
```

添加 pss leak 相关内容： 编辑“napi_init.cpp”文件： 头文件加入：
```text
#include
#include
#include
#include
```

定义 pss leak 相关方法：
```text
// 读 /proc/self/smaps_rollup 中的 PSS 字段，统计当前进程的 PSS (单位 KB)
static int GetCurrentProcessPss()
{
    std::ifstream smapsFile("/proc/self/smaps_rollup");
    if (!smapsFile.is_open()) {
        std::cerr > label >>pss;
            totalPss += pss;
        }
    }
    smapsFile.close();
    std::cout  maxSafe) {
        printf("InjectNativeLeakMallocWithSize invalid size\n");
        return false;
    }
    p = (char *) malloc(size + 1);
    if (!p) {
        printf("InjectNativeLeakMallocWithSize malloc failed\n");
        return false;
    }
    void* err = memset(p, 'a', size);
    if (err == nullptr) {
        printf("InjectNativeLeakMallocWithSize memset failed\n");
        return false;
    }
    return true;
}

// 循环申请/释放内存，使进程 PSS 持续接近 target
static void InjectNativeLeakMallocUntil(int target)
{
    constexpr int leakSizePerTime = 5000000;
    std::vector mems;
    int curPss = GetCurrentProcessPss();
    while (curPss != 0) {
        char *p = nullptr;
        if (curPss  0) {
                char *dst = mems[0];
                mems.erase(mems.begin());
                free(dst);
            }
            std::cout (x * kilobyte));
    napi_value rtn;
    napi_get_undefined(env, &rtn);
    return rtn;
}
```

初始化：
```text
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        // ...
        { "leakMB", nullptr, LeakMB, nullptr, nullptr, nullptr, napi_default, nullptr}
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
```

编辑"Index.d.ts"文件： 添加类型声明：
```text
export const leakMB: (size: number) => void;
```

单击DevEco Studio界面中的运行按钮，运行应用工程，单击 pss leak 按钮后，等待15到30分钟，系统将上报应用内存泄漏事件。 同一个应用，24小时内至多上报一次资源泄漏事件，如果短时间内要二次上报，需要重启设备。 内存泄漏事件上报后，可以在Log窗口看到对系统事件数据的处理日志：
```text
08-07 03:53:35.314 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.domain=OS
08-07 03:53:35.314 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.name=RESOURCE_OVERLIMIT
08-07 03:53:35.314 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.eventType=1
08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.time=1502049167732
08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.pid=1587
08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.uid=20010043
08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.resource_type=pss_memory
08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.app_running_unique_id=12369547851223645271
08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.bundle_version=1.0.0
08-07 03:53:35.350 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.memory={"pss":2100257,"rss":1352644,"sys_avail_mem":250272,"sys_free_mem":60004,"sys_total_mem":1992340,"vss":2462936}
08-07 03:53:35.350 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1725614572401_6808.log","/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1725614572412_6808.log"]
08-07 03:53:35.350 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.log_over_limit=false
```


## 步骤四：移除观察者

移除事件观察者：
```text
static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
    // 移除观察者以停止监听事件
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
