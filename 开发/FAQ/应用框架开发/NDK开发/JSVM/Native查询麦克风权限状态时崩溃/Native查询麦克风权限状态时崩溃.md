# Native查询麦克风权限状态时崩溃

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-11

#### 问题现象

案例Demo：
 
```text
napi_value global;
  napi_get_global(env, &global);

  napi_status status;
  napi_value abilityAccessCtrlModule;
  status = napi_get_named_property(env, global, "abilityAccessCtrl", &abilityAccessCtrlModule);
  if(status != napi_ok) {
     return;
  }
  napi_value createAtManagerMethod;
  status = napi_get_named_property(env, abilityAccessCtrlModule, "createAtManager", &createAtManagerMethod);
  if(status != napi_ok) {
     return;
  }
```
 
如上，在native层调用ArkTS API查询当前麦克风的权限状态时，会出现崩溃。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/ZVS2J2NpQfeZln7q9K7ewA/zh-cn_image_0000002628388614.png?HW-CC-KV=V1&HW-CC-Date=20260723T012523Z&HW-CC-Expire=86400&HW-CC-Sign=1CCABA2CED99DB52FBA13E50C027150C1D2BF05F3EE6DF6395789648510C4184)

 
 

#### 背景知识

napi_value是一个C的结构体指针，表示一个JavaScript对象的引用。napi_value持有JS对象，同时，napi_value受handle_scope管理，scope中napi_value持有的JS对象不会被释放；超出scope后，napi_value将失效，不再持有对应的JS对象。参考：[使用Node-API接口进行生命周期相关开发](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-life-cycle#napi_open_handle_scopenapi_close_handle_scope)。
 
 

#### 问题定位

根据崩溃日志定位分析NULL pointer dereference原因。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/uGg2hGRyRPWUxniY0FpUCQ/zh-cn_image_0000002628548514.png?HW-CC-KV=V1&HW-CC-Date=20260723T012523Z&HW-CC-Expire=86400&HW-CC-Sign=059F6C2535378524AA379D7DD497D99507FF7DDE58E169744619C6EEE0877DCD)

 
对案例Demo进行debug分析可见abilityAccessCtrlModule获取出来是一个napi_undefined类型，而status = napi_get_named_property(env,abilityAccessCtrlModule,"createAtManager", &createAtManagerMethod)，期望abilityAccessCtrlModule是一个napi_value的object类型。
 
 

#### 分析结论

- NULL pointer dereference定位空指针引用位置，需确保在使用对象之前对其进行了非空的初始化。
- napi_value类型异常，检查参数类型。

 
 

#### 修改建议
1. 确保在使用对象之前对其进行了非空的初始化。
2. 检查参数类型，避免类型异常。
```text
#include "napi/native_api.h"


static napi_value CheckUndefined(napi_env env, napi_callback_info info) 
{
    napi_value res;
    napi_value global;


    napi_create_double(env, 1, &res);
    napi_get_global(env, &global);


    napi_status status;
    napi_value abilityAccessCtrlModule;
    status = napi_get_named_property(env, global, "abilityAccessCtrl", &abilityAccessCtrlModule);
    if (status != napi_ok) {
        return res;
    }


    <em>// 检查abilityAccessCtrlModule是否为undefined</em>
    napi_valuetype value_type;
    napi_typeof(env, abilityAccessCtrlModule, &value_type);
    if (value_type == napi_undefined) {
        <em>// 这是undefined类型</em>
        return res;
    }


   <em> // 不是undefined类型，继续执行其他操作</em>
    napi_value createAtManagerMethod;
    status = napi_get_named_property(env, abilityAccessCtrlModule, "createAtManager", &createAtManagerMethod);
    if (status != napi_ok) {
        return res;
    }
    napi_create_double(env, 0, &res);
    return res;
}


EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports) 
{
    napi_property_descriptor desc[] = {{"checkUndefined", nullptr, CheckUndefined, nullptr, nullptr, nullptr, napi_default, nullptr}};
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END


static napi_module demoModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "entry",
    .nm_priv = ((void *)0),
    .reserved = {0},
};


extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
```
