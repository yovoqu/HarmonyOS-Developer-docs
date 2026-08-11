# 如何避免调用napi_release_threadsafe_function释放tsfn后js_cb被再次执行

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-12

#### 问题现象

```text
napi_release_threadsafe_function(this->tsfn, napi_tsfn_abort);
```
 
调用之后，napi_create_threadsafe_function创建的js_cb里面还是会有概率再执行一次。
 
 

#### 背景知识

napi_threadsafe_function的引用计数未归零时，应使用napi_tsfn_abort模式调用napi_release_threadsafe_function方法，确保env释放后不再持有或使用tsfn，详见：[napi_threadsafe_function内存泄漏应该如何处理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-faq-about-memory-leak#napi_threadsafe_function内存泄漏应该如何处理)。
 
 

#### 解决方案

在调用napi_release_threadsafe_function前设置线程共享的原子标志位，并在js_cb中优先检查该标志位。若已标记释放则直接返回，避免执行后续逻辑。结合互斥锁和状态变量，确保线程安全。实现示例：
 1. C++侧实现：
```text
#include "napi/native_api.h"
#include <thread>
#include <mutex>
#include <atomic>
#include <hilog/log.h>

#undef LOG_DOMAIN
#undef LOG_TAG
#define LOG_DOMAIN 0x3200 <em> // 全局domain宏，标识业务领域</em>
#define LOG_TAG "MY_TAG"   <em>// 全局tag宏，标识模块日志tag</em>

<em>// 全局变量定义</em>
static napi_threadsafe_function g_tsfn = nullptr;
static std::mutex g_releaseMutex;
static std::atomic<bool> g_isReleased(false);

<em>// JS回调函数</em>
static void CallJs(napi_env env, napi_value js_cb, void* context, void* data) 
{
    <em>// 第一重检查：原子标志位（无锁）</em>
    if (g_isReleased.load()) {
        OH_LOG_INFO(LOG_APP, "已释放后执行! Data: %{public}d", *(int*)data);
        return;
    }

   <em> // 第二重检查：互斥锁保护</em>
    std::lock_guard<std::mutex> lock(g_releaseMutex);
    if (g_isReleased.load()) {
        OH_LOG_INFO(LOG_APP, "互斥锁保护下检测到已释放! Data: %{public}d", *(int*)data);
        return;
    }

    <em>// 正常回调逻辑</em>
    OH_LOG_INFO(LOG_APP, "正常回调执行: %{public}d", *(int*)data);
}

<em>// 工作线程函数</em>
static void WorkerThread() 
{
    int data = 0;
    while (!g_isReleased.load()) {
        data++;
        napi_status status = napi_call_threadsafe_function(
            g_tsfn, 
            &data, 
            napi_tsfn_blocking
        );

        if (status != napi_ok) break;
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }
}

<em>// 安全释放函数</em>
static void ReleaseTSFN() 
{
    std::lock_guard<std::mutex> lock(g_releaseMutex);
    g_isReleased = true;

    if (g_tsfn != nullptr) {
        napi_release_threadsafe_function(g_tsfn, napi_tsfn_abort);
        g_tsfn = nullptr;
        OH_LOG_INFO(LOG_APP, "已释放线程安全函数");
    }
}

<em>// 主入口函数</em>
static napi_value StartTest(napi_env env, napi_callback_info info) 
{
   <em> // 获取JS回调函数</em>
    size_t argc = 1;
    napi_value argv;
    napi_get_cb_info(env, info, &argc, &argv, nullptr, nullptr);

   <em> // 重置释放状态</em>
    g_isReleased = false;

   <em> // 创建线程安全函数</em>
    napi_value work_name;
    napi_create_string_utf8(env, "TSFN_Work", NAPI_AUTO_LENGTH, &work_name);
    napi_status status = napi_create_threadsafe_function(
        env,
        argv,      <em> // JS回调函数</em>
        nullptr,      <em> // 异步资源</em>
        work_name,     <em>// 资源名称</em>
        0,             <em>// 最大队列长度 (0=无限制)</em>
        1,           <em>  // 初始线程数</em>
        nullptr,       <em>// 上下文</em>
        nullptr,      <em> // 最终回调</em>
        nullptr,      <em> // 最终数据</em>
        CallJs,       <em> // 回调函数</em>
        &g_tsfn       <em> // 输出TSFN</em>
    );

    if (status != napi_ok) {
        napi_throw_error(env, nullptr, "创建线程安全函数失败");
        return nullptr;
    }

  <em>  // 启动工作线程</em>
    std::thread worker(WorkerThread);
    worker.detach();

   <em> // 延迟释放线程（模拟竞态条件）</em>
    std::thread([] {
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
        OH_LOG_INFO(LOG_APP, "开始释放线程安全函数...");
        ReleaseTSFN();
    }).detach();

    return nullptr;
}

<em>// 模块注册</em>
EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports) 
{
    napi_property_descriptor desc[] = {
        {"startTest", nullptr, StartTest, nullptr, nullptr, nullptr, napi_default, nullptr}
    };
    napi_define_properties(env, exports, sizeof(desc)/sizeof(desc), desc);
    return exports;
}
EXTERN_C_END

static napi_module demoModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "entry",
    .nm_priv = ((void*)0),
    .reserved = {0},
};

extern "C" __attribute__((constructor)) void RegisterModule() 
{
    napi_module_register(&demoModule);
}
```

2. index.d.ts接口声明：
```text
export const startTest: (callback: (id: number) => void) => void;
```

3. index.ets侧调用Native接口启用线程：
```text
import testNapi from 'libentry.so';

@Entry
@Component
struct Index {

  build() {
    Row() {
      Column() {
        Button('启用线程')
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            testNapi.startTest(() => {
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

 
 

#### 总结

napi_release_threadsafe_function的abort模式会立即标记线程安全函数为已释放，但未完成的任务仍可能在finalize回调中执行，可以通过状态标记、互斥锁等方式避免js_cb被再次执行。
