# NAPI执行上层回调时，如何获取env

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-29

libuv处理方式是在注册JS回调时保存env。在callback中从env中获取对应的JS线程的loop，再调用libuv接口抛JS任务到loop中执行。
 
napi_create_thread_safe_function函数调用时会触发参数中的napi_threadsafe_function_call_js函数，该函数可以获取env在js线程中执行，参考以下方式：
 
```text
#include "napi/native_api.h" 
#include <thread> 
#include "hilog/log.h" 
 
napi_ref cbObj = nullptr; 
<em>// Thread safety function</em>
napi_threadsafe_function tsfn; 
<em>// Native side Value Value</em>
static int cValue; 
 
 
<em>// Subthread running function </em>
static void CallJs(napi_env env, napi_value js_cb, void *context, void *data) { 
    std::thread::id this_id = std::this_thread::get_id(); 
    OH_LOG_INFO(LOG_APP, "threadId3 is +%{public}d", this_id); 
  <em>  // Get reference value </em>
    napi_get_reference_value(env, cbObj, &js_cb); 
 
  <em>  // Create an ArkTS number as an input parameter for the ArkTS function.</em>
    napi_value argv; 
    napi_create_int32(env, cValue, &argv); 
 
    napi_value result = nullptr; 
    napi_call_function(env, nullptr, js_cb, 1, &argv, &result); 
 
    napi_get_value_int32(env, result, &cValue); 
 
    napi_delete_reference(env, cbObj); 
} 
 
<em>// Native main thread</em>
static napi_value ThreadsTest(napi_env env, napi_callback_info info) { 
   <em> // The number of parameters obtained from ArkTS side</em>
    size_t argc = 1; 
    napi_value js_cb, work_name; 
 
   <em> // Get ArkTS parameters</em>
    napi_get_cb_info(env, info, &argc, &js_cb, nullptr, nullptr); 
 
   <em> // Napi_ref cbObj pointing to napi_value js_cb</em>
    napi_create_reference(env, js_cb, 1, &cbObj); 
 
   <em> // Create workname using UTF8 encoded C string data </em>
    napi_create_string_utf8(env, "Work Item", NAPI_AUTO_LENGTH, &work_name); 
 
  <em>  // Create thread safe function</em>
    napi_create_threadsafe_function(env, js_cb, NULL, work_name, 0, 1, NULL, NULL, NULL, CallJs, &tsfn); 
 
    std::thread::id this_id = std::this_thread::get_id(); 
    OH_LOG_INFO(LOG_APP, "threadId1 is +%{public}d", this_id); 
 
   <em> // Calling thread safe functions in other threads</em>
    std::thread t([]() { 
      <em>  // Can obtain thread ID</em>
        std::thread::id this_id = std::this_thread::get_id(); 
        OH_LOG_INFO(LOG_APP, "threadId2 is +%{public}d", this_id); 
        napi_acquire_threadsafe_function(tsfn); 
        napi_call_threadsafe_function(tsfn, NULL, napi_tsfn_blocking); 
    }); 
    t.detach(); 
 
    return NULL; 
}
```
