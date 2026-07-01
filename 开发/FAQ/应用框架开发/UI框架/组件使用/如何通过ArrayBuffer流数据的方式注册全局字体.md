# 如何通过ArrayBuffer流数据的方式注册全局字体

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1254

#### 问题现象

在HarmonyOS中，除了通过font.registerFont接口注册本地的字体文件，是否支持将字体包通过ArrayBuffer流数据的方式进行加载和注册？
 
 

#### 背景知识

- ArkUI层提供了font.registerFont接口，此种方案可以直接注册本地工程或者Rawfile文件夹中的字体文件，参考[如何加载和使用自定义字体](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-21)。
- NAPI层的drawing模块提供了OH_Drawing_RegisterFontBuffer接口，支持通过ArrayBuffer流数据的方式注册字体文件，具体接口说明和传参可参考[OH_Drawing_RegisterFontBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-register-font-h#oh_drawing_registerfontbuffer)。

 
 

#### 解决方案
1. 从目标字体文件中读取其对应的ArrayBuffer数据，并将该数据传递至NAPI（Native API）层；
2. 在NAPI层通过调用OH_Drawing_RegisterFontBuffer接口，完成对该字体数据的注册操作；
3. 在ArkUI框架中调用已注册的字体，实现对应字体的使用与展示。
 
ArkTS实现：
 
```text
import <span style="color: rgb(0,0,255);">fontNapi </span>from <span style="color: rgb(255,0,170);">'libentry.so'</span><span style="color: rgb(181,106,1);">;</span>

<span style="color: rgb(181,106,1);">@Entry</span>
<span style="color: rgb(181,106,1);">@Component</span>
struct <span style="color: rgb(0,0,255);">Index </span><span style="color: rgb(255,0,170);">{</span>
  <span style="color: rgb(0,0,255);">message</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">string </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'Hello World'</span><span style="color: rgb(181,106,1);">;</span>

  <span style="color: rgb(0,0,255);">aboutToAppear</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(0,0,255);">void </span><span style="color: rgb(255,0,170);">{</span>
    <em>// </em><em><span style="color: rgb(128,128,128);">此处是模拟的读取本地字体文件后得到</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">，实际场景中可以直接传入字体的</span><span style="color: rgb(128,128,128);">ArrayBuffer</span></em>
    const <span style="color: rgb(0,0,255);">fontName </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'MyCustomFont'</span><span style="color: rgb(181,106,1);">; </span><em><span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">自定义字体名称</span></em>
    const <span style="color: rgb(0,0,255);">fontPath </span><span style="color: rgb(181,106,1);">= </span><span style="color: rgb(255,0,170);">'XXXX.ttf'</span><span style="color: rgb(181,106,1);">; </span><em>// </em><em><span style="color: rgb(128,128,128);">此处仅为示例，请开发者替换为可用的字体文件。</span></em>
    const <span style="color: rgb(0,0,255);">file </span><span style="color: rgb(181,106,1);">= </span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getUIContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getHostContext</span><span style="color: rgb(0,0,255);">()</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">resourceManager</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">getRawFileContentSync</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">fontPath</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(0,0,255);">fontNapi</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">registerFontFamily</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(0,0,255);">fontName</span><span style="color: rgb(181,106,1);">, </span><span style="color: rgb(0,0,255);">file</span><span style="color: rgb(181,106,1);">?.</span><span style="color: rgb(0,0,255);">buffer</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>

  <span style="color: rgb(0,0,255);">build</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
    <span style="color: rgb(0,0,255);">Row</span><span style="color: rgb(0,0,255);">() </span><span style="color: rgb(255,0,170);">{</span>
      <span style="color: rgb(0,0,255);">Column</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">{ </span><span style="color: rgb(0,0,255);">space</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(255,0,0);">10 </span><span style="color: rgb(255,0,170);">}</span><span style="color: rgb(0,0,255);">) </span><span style="color: rgb(255,0,170);">{</span>
        <span style="color: rgb(0,0,255);">Text</span><span style="color: rgb(0,0,255);">(</span>this<span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">message</span><span style="color: rgb(0,0,255);">)</span>
          <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">fontFamily</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'MyCustomFont'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
      <span style="color: rgb(255,0,170);">}</span>
      <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">width</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
    <span style="color: rgb(255,0,170);">}</span>
    <span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">height</span><span style="color: rgb(0,0,255);">(</span><span style="color: rgb(255,0,170);">'100%'</span><span style="color: rgb(0,0,255);">)</span><span style="color: rgb(181,106,1);">;</span>
  <span style="color: rgb(255,0,170);">}</span>
<span style="color: rgb(255,0,170);">}</span>
```
 
NAPI实现：
 
```text
<em>/*</em>
<em><span style="color: rgb(128,128,128);"> * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.</span></em>
<em><span style="color: rgb(128,128,128);"> */</span></em>


<span style="color: rgb(181,106,1);">#include "napi/native_api.h"</span>
<span style="color: rgb(181,106,1);">#include "native_drawing/drawing_register_font.h"</span>
<span style="color: rgb(181,106,1);">#include "native_drawing/drawing_font_collection.h"</span>

static napi_value registerFontFamily(napi_env env, napi_callback_info info) 
{
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取全局字体集对象</span><span style="color: rgb(128,128,128);">OH_Drawing_FontCollection</span></em>
    OH_Drawing_FontCollection *fontCollection = OH_Drawing_GetFontCollectionGlobalInstance();
    size_t argc = <span style="color: rgb(0,0,255);">2</span>;
    napi_value args[<span style="color: rgb(0,0,255);">2</span>];
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取字体名称</span></em>
    char fontName[<span style="color: rgb(0,0,255);">256</span>];
    size_t fontNameLen;
    napi_get_value_string_utf8(env, args[<span style="color: rgb(0,0,255);">0</span>], fontName, sizeof(fontName), &fontNameLen);
 <em>   <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">获取字体的</span><span style="color: rgb(128,128,128);">ArrayBuffer</span><span style="color: rgb(128,128,128);">数据</span></em>
    void *bufferData;
    size_t bufferLength;
    napi_get_arraybuffer_info(env, args[<span style="color: rgb(0,0,255);">1</span>], &bufferData, &bufferLength);
   <em> <span style="color: rgb(128,128,128);">// </span><span style="color: rgb(128,128,128);">注册字体</span></em>
    OH_Drawing_RegisterFontBuffer(fontCollection, fontName, reinterpret_cast<uint8_t *>(bufferData), bufferLength);
    return nullptr;
}
EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports) 
{
    napi_property_descriptor desc[] = {
        {"registerFontFamily", nullptr, registerFontFamily, nullptr, nullptr, nullptr, napi_default, nullptr}};
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[<span style="color: rgb(0,0,255);">0</span>]), desc);
    return exports;
}
EXTERN_C_END
static napi_module demoModule = {
    .nm_version = <span style="color: rgb(0,0,255);">1</span>,
    .nm_flags = <span style="color: rgb(0,0,255);">0</span>,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "entry",
    .nm_priv = ((void *)<span style="color: rgb(0,0,255);">0</span>),
    .reserved = {<span style="color: rgb(0,0,255);">0</span>},
};
extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
```
 
Index.d.ts声明：
 
```text
export const registerFontFamily: (fontName: string, file: ArrayBuffer) => void;
```
 
CMakeLists.txt：
 
```cpp
<span style="color: rgb(181,106,1);"># the </span>minimum version of CMake.
cmake_minimum_required(VERSION <span style="color: rgb(0,0,255);">3.5.0</span>)
project(registerFontBuffer)
set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
if(DEFINED PACKAGE_FIND_FILE)
    include(${PACKAGE_FIND_FILE})
endif()
include_directories(${NATIVERENDER_ROOT_PATH}
                    ${NATIVERENDER_ROOT_PATH}/include)
add_library(entry SHARED napi_init.cpp)
target_link_libraries(entry PUBLIC libace_napi.z.so libnative_drawing.so)
```
 
> [!NOTE]
> OH_Drawing_GetFontCollectionGlobalInstance这个接口是API 14才支持，需要把DevEco Studio和系统版本升级到对应的配套版本上进行使用，DevEco Studio请使用5.0.7.210及以上版本。
