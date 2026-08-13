# Native侧跨HAR/HSP模块接口调用

更新时间：2026-08-11 11:13:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-cross-har-hsp-interface-call

#### 概述

在大型应用开发中，应用通常会分为多个业务模块，业务模块常会以HSP或HAR包的形式提供SDK能力，这些SDK往往会提供Native接口给HAP模块的Native层直接调用，从而实现应用的复杂功能。而如何在Native侧跨HAR/HSP模块进行接口调用，是开发者经常遇到的问题。本文将介绍Native侧跨HAR/HSP模块调用两种典型场景，包括调用Native方法和调用ArkTS方法，以方便开发者更好的掌握Native侧跨模块调用的能力。
 
  

#### 实现原理

如图1所示，Native侧跨HAR/HSP模块调用原理主要包括以下步骤。
 1. 在Module1（HAP）模块中，ArkTS侧通过Node-API调用Native接口。
2. Module1（HAP）模块Native侧调用Module2（HSP/HAR）模块Native方法。

  
- 被调用方在Module2（HSP/HAR）模块中，创建头文件，并在build-profile.json5中配置头文件导出。

3. 被调用方在Module2（HSP/HAR）模块的CMakeLists.txt中进行配置，将源文件配置到so中。

4. 调用方在Module1（HAP）模块的oh-package.json5文件配置引入Module2（HSP/HAR）模块。

5. 调用方在Module1（HAP）模块的CMakeLists.txt中，配置引入Module2的so文件。

6. 调用方引入Module2（HSP/HAR）模块的头文件后，就可以调用Module2（HSP/HAR）模块的Native方法。
- 在Module2（HSP/HAR）模块中，Native侧通过Node-API接口进行模块加载，从而调用ArkTS方法。

 
**图 1** Native侧跨HAR/HSP模块调用原理图
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/S0f_N0GXRT-5jB9ndogq_g/zh-cn_image_0000002704391777.png?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=567A2B46935B21990365BF8AEE5DE6B7EF1A5B4D11FDFD9FB5C95FF3CCB39199)

 
  

#### Native侧跨HAR/HSP模块调用Native方法

如下图所示，Native侧跨HAR/HSP模块调用Native方法的调用链路为Module1 ArkTS -> Module1 Native -> Module2 Native。在HarmonyOS项目中，Native侧跨模块调用Native方法实际就是C++侧调用，需要配置编译链接依赖。Native侧跨HAR/HSP模块调用Native方法实现的关键是在Module2（HSP/HAR）模块的build-profile.json5中，配置头文件导出，并在CMakeLists.txt中进行配置，将源文件配置到so中。
 
**图 2** Native侧跨HAR/HSP模块调用Native方法
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/aAKXP79rR2a_AyF-uTd9UQ/zh-cn_image_0000002674631656.png?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=A4D8AAAAA808545B605333586C84CAEF8DC5C96A467B4FA3998DF8E6E29102D2)

 
  

#### 开发流程

Native侧跨HAR/HSP模块调用Native方法时，需要实现Module1（HAP）的ArkTS侧调用Module1（HSP/HAR）的Native侧、Module1（HAP）的Native侧调用Module2（HSP/HAR）的Native侧。在当前场景下，跨模块调用HAR模块和HSP模块的方式相同，当前以跨模块调用HAR模块为例，详细流程如下所示。
 1. 开发者需要创建Module2（HAR）模块staticModule，详细创建流程可以参考[创建库模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har#section643521083015)。
2. 在Module2中新建C++文件napi_har.cpp，再新建其头文件napi_har.h，并定义Native方法。

  napi_har.cpp代码如下所示。

  
```cpp
#include "napi/native_api.h"
#include "napi_har.h"

double harNativeAdd(double a, double b) {
    return a + b;
}
```
   napi_har.h代码如下所示。

  
```cpp
#ifndef CROSSMODULEREFERENCE_NAPI_HAR_H
#define CROSSMODULEREFERENCE_NAPI_HAR_H
#include <js_native_api_types.h>
// ...
double harNativeAdd(double a, double b);
napi_value harArkTSAdd(double a, double b);
#endif
```

3. 在Module2中的build-profile.json5中配置头文件导出。如果不做当前headerPath的配置，会导致Module1引用不到Module2的头文件。

  
```json
{
  "apiType": "stageMode",
  "buildOption": {
    "externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": "",
      "cppFlags": "",
      "abiFilters": ["x86_64", "arm64-v8a"]
    },
    "nativeLib": {
      "headerPath": "./src/main/cpp"
    },
    // ...
}
```

4. 在Module2的CMakeLists.txt中配置将源文件打包到so。

  
```cpp
# staticModule\src\main\cpp\CMakeLists.txt
add_library(add SHARED napi_init.cpp napi_har.cpp)
```

5. 在Module2模块创建后，需要在Module1的oh-package.json5文件中配置对应的依赖。如下所示，staticModule为新创建的HAR模块的文件名，static_module为HAR模块的名称。

  
```json
{
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "",
  "author": "",
  "license": "",
  "dependencies": {
    "libentry.so": "file:./src/main/cpp/types/libentry",
    "static_module": "file:../staticModule",
    // ...
  }
}
```

6. 在Module1中的CMakeLists.txt中配置so依赖。

  
> [!TIP]
> static_module::add中第一个参数static_module是module2的模块名称，第二个参数add是module2编译出来的so名称（不需要带上lib）。默认情况下，module2的模块名称与so名称相同，为了方便说明，在本案例中将so名称修改成了add。


  
```text
# entry\src\main\cpp\CMakeLists.txt
target_link_libraries(entry PUBLIC libace_napi.z.so static_module::add shared_module::calc)
```

7. 在Module1的napi_init.cpp中导入Module2的头文件napi_har.h，并调用其Native方法harNativeAdd()。
8. 在Module1的Native侧调用Module2的invokeHarNative()方法。

  
```cpp
static napi_value invokeHarNative(napi_env env, napi_callback_info info)
{
    size_t argc = 2;
    napi_value args[2] = {nullptr};

    napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

    napi_valuetype valuetype0;
    napi_typeof(env, args[0], &valuetype0);

    napi_valuetype valuetype1;
    napi_typeof(env, args[1], &valuetype1);

    double value0;
    napi_get_value_double(env, args[0], &value0);

    double value1;
    napi_get_value_double(env, args[1], &value1);

    napi_value sum;

    napi_create_double(env, harNativeAdd(value0, value1), &sum);

    return sum;
}
```

9. 在Module1的ArkTS侧调用Native侧的invokeHarNative()方法。

  
```ArkTS
Button($r('app.string.call_har_native_method'))
  .fontSize(16)
  .width('100%')
  .margin({ top: 12 })
  .onClick(() => {
    this.getUIContext().getPromptAction().showToast({
      message: 'HarNative method call succeed, result is ' + napi.invokeHarNative(2, 3).toString()
    });
  })
```

 
  

#### 实现效果

**图 3** Native侧调用HAR模块的Native方法
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/7yLB8_2zQTuOeMFoAUbz1Q/zh-cn_image_0000002704271611.gif?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=802C38F6377CA69A0009B14162679CBE387C008297A14D6C11E222F03DED278A)

 
  

#### Native侧跨HAR/HSP模块调用ArkTS方法

如下图所示，Native侧跨HAR/HSP模块调用ArkTS方法是[Native侧跨HAR/HSP模块调用Native方法](#native侧跨harhsp模块调用native方法)的基础上调用ArkTS方法。其关键是在Module2中获取Module1中的上下文napi_env，并根据上下文napi_env加载模块、调用对应的ArkTS方法。
 
**图 4** Native侧跨HAR/HSP模块调用ArkTS方法
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/ycElaLy_TzmMQ9YalzSLaA/zh-cn_image_0000002674471810.png?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=A0834737B2F2BEA08B98992A9A8F9DC17D353C8F72FA2B22ACD861DF66406C34)

 
  

#### 开发流程

Native侧跨HAR/HSP模块调用ArkTS方法具体实现方法如下所示。
 1. 在完成[Native侧跨HAR/HSP模块调用Native方法](#native侧跨harhsp模块调用native方法)后，在Module1中新增invokeHarArkTS()方法以准备调用HAR模块的ArkTS方法。
2. 在Module2的Native侧，新增setHarEnv()方法，用以传递napi_env，并在头文件中进行配置，代码如下所示。

  napi_har.h代码如下所示。

  
```cpp
#ifndef CROSSMODULEREFERENCE_NAPI_HAR_H
#define CROSSMODULEREFERENCE_NAPI_HAR_H
#include <js_native_api_types.h>
napi_env g_main_env;
void setHarEnv(napi_env env);
double harNativeAdd(double a, double b);
napi_value harArkTSAdd(double a, double b);
#endif
```
   napi_har.cpp代码如下所示。

  
```cpp
void setHarEnv(napi_env env) {
    g_main_env = env;
}
```

3. 在Module1中的napi_init.cpp中的Init()方法中调用setHarEnv()方法将Module1中的napi_env传递到Module2中。

  
```text
EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        { "add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr },
        { "invokeHarNative", nullptr, invokeHarNative, nullptr, nullptr, nullptr, napi_default, nullptr },
        { "invokeHarArkTS", nullptr, invokeHarArkTS, nullptr, nullptr, nullptr, napi_default, nullptr },
        { "invokeHspNative", nullptr, invokeHspNative, nullptr, nullptr, nullptr, napi_default, nullptr },
        { "invokeHspArkTS", nullptr, invokeHspArkTS, nullptr, nullptr, nullptr, napi_default, nullptr }
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    setHarEnv(env);
     // ...
    return exports;
}
EXTERN_C_END
```

4. 在Module2中创建ArkTS方法，提供给Module2的Native侧调用。

  
```ArkTS
export function add(a: number, b: number): number {
  return a + b;
}
```

5. 在Module2模块的build-profile.json5文件中进行以下配置。

  
```ArkTS
{
  "apiType": "stageMode",
  "buildOption": {
    // ...
    "arkOptions" : {
      "runtimeOnly" : {
        "sources": [
          "./src/main/ets/utils/Util.ets"
        ]
      }
    }
  },
  // ...
}
```

6. 在Module2的Native侧调用ArkTS方法，并配置到头文件中。详细步骤如下所示。

  
- 通过napi_load_module_with_info()加载模块，其中，第二个参数是待加载的ets文件的路径，第三个参数是bundleName+模块名。

7. 使用napi_get_named_property()获取模块导出的add()方法。

8. 使用napi_call_function()调用add()方法。

  napi_har.cpp代码如下所示。

  
```text
napi_value harArkTSAdd(double a, double b) {
    napi_env env = g_main_env;
    napi_value module;
    napi_status status = napi_load_module_with_info(env, "static_module/src/main/ets/utils/Util", "com.example.crossmodulereference/entry", &module);
    if (napi_ok != status) {
        return 0;
    }
    
    napi_value addFunc;
    napi_get_named_property(env, module, "add", &addFunc);
    
    napi_value addResult;
    napi_value argv[2] = {nullptr, nullptr};
    napi_create_double(env, a, &argv[0]);
    napi_create_double(env, b, &argv[1]);
    napi_call_function(env, module, addFunc, 2, argv, &addResult);
    
    return addResult;
}
```

- 在module1的Native侧调用module2的harArkTSAdd()方法。

  
```cpp
static napi_value invokeHarArkTS(napi_env env, napi_callback_info info)
{
    size_t argc = 2;
    napi_value args[2] = {nullptr};

    napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

    napi_valuetype valuetype0;
    napi_typeof(env, args[0], &valuetype0);

    napi_valuetype valuetype1;
    napi_typeof(env, args[1], &valuetype1);

    double value0;
    napi_get_value_double(env, args[0], &value0);

    double value1;
    napi_get_value_double(env, args[1], &value1);
    
    return harArkTSAdd(value0, value1);
}
```

- 在Module1的ArkTS侧调用Native侧的invokeHarArkTS()方法。

  
```ArkTS
Button($r('app.string.call_har_ArkTS_method'))
  .fontSize(16)
  .width('100%')
  .margin({ top: 12 })
  .onClick(() => {
    this.getUIContext().getPromptAction().showToast({ message: 'HarArkTS method call succeed, result is '
      + napi.invokeHarArkTS(2, 3).toString() });
  })
```


 
  

#### 实现效果

**图 5** Native侧调用HAR模块的ArkTS方法
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/auf8_KxHS1WiU1ytlfXvSA/zh-cn_image_0000002704391779.gif?HW-CC-KV=V1&HW-CC-Date=20260813T100027Z&HW-CC-Expire=86400&HW-CC-Sign=5D9AB3D831FF1324B94BA37A3B60CE8E2CB76CE2915F3095C85174E8B3706E7B)

 
  

#### 示例代码

- [Native侧跨HAR/HSP模块调用](https://gitcode.com/harmonyos_samples/CrossModuleReference)
