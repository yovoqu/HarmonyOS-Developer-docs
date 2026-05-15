# NativeBundle开发指导

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-bundle-guidelines

## 场景介绍

开发者可以通过本指导了解在HarmonyOS应用中，如何使用Native Bundle接口获取应用自身相关信息。

## 接口说明

常用接口如下表所示，具体API说明详见[Native_Bundle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle)。
| 接口名 | 描述 |
| --- | --- |
| [OH_NativeBundle_GetCurrentApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getcurrentapplicationinfo) | 获取应用自身相关信息。 |
| [OH_NativeBundle_GetAppId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getappid) | 获取自身应用的appId信息。 |
| [OH_NativeBundle_GetAppIdentifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getappidentifier) | 获取自身应用的appIdentifier信息。 |
| [OH_NativeBundle_GetMainElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getmainelementname) | 获取自身应用入口的信息。 |
| [OH_NativeBundle_GetCompatibleDeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getcompatibledevicetype) | 获取自身应用适用的设备类型。 |
| [OH_NativeBundle_IsDebugMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_isdebugmode) | 查询当前应用的调试模式。从API version 20开始支持。 |
| [OH_NativeBundle_GetModuleMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getmodulemetadata) | 获取当前应用的元数据信息。从API version 20开始支持。 |
| [OH_NativeBundle_GetAbilityResourceInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h#oh_nativebundle_getabilityresourceinfo) | 获取支持打开特定文件类型的组件资源信息列表。从API version 21开始支持。 |


## 开发步骤

**1. 创建工程**
![](assets/NativeBundle开发指导/file-20260514132736308-0.png)
**2. 添加依赖** 创建完成后，DevEco Studio会在工程生成cpp目录，目录中包含types/libentry/index.d.ts、napi_init.cpp、CMakeLists.txt等文件。 打开src/main/cpp/CMakeLists.txt，在target_link_libraries依赖中添加包管理的libbundle_ndk.so。
```text
target_link_libraries(entry PUBLIC libace_napi.z.so libbundle_ndk.so)
```

打开src/main/cpp/napi_init.cpp文件，添加头文件。
```text
// napi依赖头文件
#include "napi/native_api.h"
// native接口依赖头文件
#include "bundle/ability_resource_info.h"
#include "bundle/native_interface_bundle.h"
// free()函数依赖的基础库
#include
```

**3. 修改源文件** 打开src/main/cpp/napi_init.cpp文件，文件Init会对当前方法进行初始化映射，这里定义对外的接口。
```text
EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        { "add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr },
        // 新增方法getCurrentApplicationInfo
        { "getCurrentApplicationInfo", nullptr, GetCurrentApplicationInfo, nullptr,
            nullptr, nullptr, napi_default, nullptr},
        // 新增方法getAppId
        { "getAppId", nullptr, GetAppId, nullptr, nullptr, nullptr, napi_default, nullptr},
        // 新增方法getAppIdentifier
        { "getAppIdentifier", nullptr, GetAppIdentifier, nullptr, nullptr, nullptr, napi_default, nullptr},
        // 新增方法getMainElementName
        { "getMainElementName", nullptr, GetMainElementName, nullptr, nullptr, nullptr, napi_default, nullptr},
        // 新增方法getCompatibleDeviceType
        { "getCompatibleDeviceType", nullptr, GetCompatibleDeviceType, nullptr,
            nullptr, nullptr, napi_default, nullptr},
        // 新增方法isDebugMode
        { "isDebugMode", nullptr, IsDebugMode, nullptr, nullptr, nullptr, napi_default, nullptr},
        // 新增方法getModuleMetadata
        { "getModuleMetadata", nullptr, GetModuleMetadata, nullptr, nullptr, nullptr, napi_default, nullptr},
        // 新增方法getAbilityResourceInfo
        { "getAbilityResourceInfo", nullptr, GetAbilityResourceInfo, nullptr, nullptr, nullptr, napi_default, nullptr}
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END
```

在src/main/cpp/napi_init.cpp文件中获取Native的包信息对象，并转为js的包信息对象，即可在js侧获取应用的信息：
```text
static napi_value GetCurrentApplicationInfo(napi_env env, napi_callback_info info)
{
    // 调用Native接口获取应用信息
    OH_NativeBundle_ApplicationInfo nativeApplicationInfo = OH_NativeBundle_GetCurrentApplicationInfo();
    napi_value result = nullptr;
    napi_create_object(env, &result);
    // Native接口获取的应用包名转为js对象里的bundleName属性
    napi_value bundleName;
    napi_create_string_utf8(env, nativeApplicationInfo.bundleName, NAPI_AUTO_LENGTH, &bundleName);
    napi_set_named_property(env, result, "bundleName", bundleName);
    // Native接口获取的指纹信息转为js对象里的fingerprint属性
    napi_value fingerprint;
    napi_create_string_utf8(env, nativeApplicationInfo.fingerprint, NAPI_AUTO_LENGTH, &fingerprint);
    napi_set_named_property(env, result, "fingerprint", fingerprint);
    // 最后为了防止内存泄漏，手动释放
    free(nativeApplicationInfo.bundleName);
    free(nativeApplicationInfo.fingerprint);
    return result;
}

static napi_value GetAppId(napi_env env, napi_callback_info info)
{
    // 调用Native接口获取应用appId
    char* appId = OH_NativeBundle_GetAppId();
    // Native接口转成nAppId返回
    napi_value nAppId;
    napi_create_string_utf8(env, appId, NAPI_AUTO_LENGTH, &nAppId);
    // 最后为了防止内存泄漏，手动释放
    free(appId);
    return nAppId;
}

static napi_value GetAppIdentifier(napi_env env, napi_callback_info info)
{
    // 调用Native接口获取应用appIdentifier
    char* appIdentifier = OH_NativeBundle_GetAppIdentifier();
    // Native接口转成nAppIdentifier返回
    napi_value nAppIdentifier;
    napi_create_string_utf8(env, appIdentifier, NAPI_AUTO_LENGTH, &nAppIdentifier);
    // 最后为了防止内存泄漏，手动释放
    free(appIdentifier);
    return nAppIdentifier;
}

static napi_value GetMainElementName(napi_env env, napi_callback_info info)
{
    // 调用Native接口获取应用入口的信息
    OH_NativeBundle_ElementName elementName = OH_NativeBundle_GetMainElementName();
    napi_value result = nullptr;
    napi_create_object(env, &result);
    // Native接口获取的应用包名转为js对象里的bundleName属性
    napi_value bundleName;
    napi_create_string_utf8(env, elementName.bundleName, NAPI_AUTO_LENGTH, &bundleName);
    napi_set_named_property(env, result, "bundleName", bundleName);
    // Native接口获取的模块名称转为js对象里的moduleName属性
    napi_value moduleName;
    napi_create_string_utf8(env, elementName.moduleName, NAPI_AUTO_LENGTH, &moduleName);
    napi_set_named_property(env, result, "moduleName", moduleName);
    // Native接口获取的ability名称转为js对象里的abilityName属性
    napi_value abilityName;
    napi_create_string_utf8(env, elementName.abilityName, NAPI_AUTO_LENGTH, &abilityName);
    napi_set_named_property(env, result, "abilityName", abilityName);
    // 最后为了防止内存泄漏，手动释放
    free(elementName.bundleName);
    free(elementName.moduleName);
    free(elementName.abilityName);
    return result;
}

static napi_value GetCompatibleDeviceType(napi_env env, napi_callback_info info)
{
    // 调用Native接口获取应用deviceType
    char* deviceType = OH_NativeBundle_GetCompatibleDeviceType();
    // Native接口转成nDeviceType返回
    napi_value nDeviceType;
    napi_create_string_utf8(env, deviceType, NAPI_AUTO_LENGTH, &nDeviceType);
    // 最后为了防止内存泄漏，手动释放
    free(deviceType);
    return nDeviceType;
}

static napi_value IsDebugMode(napi_env env, napi_callback_info info)
{
    bool isDebug = false;
    // 调用Native接口获取应用DebugMode的信息，该接口从API version 20开始支持
    bool isSuccess = OH_NativeBundle_IsDebugMode(&isDebug);
    // 调用Native接口失败抛出异常
    if (isSuccess == false) {
        napi_throw_error(env, nullptr, "call failed");
        return nullptr;
    }
    // Native接口转成debug返回
    napi_value debug;
    napi_get_boolean(env, isDebug, &debug);
    return debug;
}

static napi_value GetModuleMetadata(napi_env env, napi_callback_info info)
{
    size_t moduleCount = 0;
    // 调用Native接口获取应用元数据的信息，该接口从API version 20开始支持
    OH_NativeBundle_ModuleMetadata* modules = OH_NativeBundle_GetModuleMetadata(&moduleCount);
    if (modules == nullptr || moduleCount == 0) {
        napi_throw_error(env, nullptr, "no metadata found");
        return nullptr;
    }
    napi_value result;
    napi_create_array(env, &result);
    for (size_t i = 0; i           **4. 接口暴露**                  在src/main/cpp/types/libentry/Index.d.ts文件中，声明暴露接口。
```text
export const add: (a: number, b: number) => number;
export const getCurrentApplicationInfo: () => object;   // 新增暴露方法 getCurrentApplicationInfo
export const getAppId: () => string; // 新增暴露方法 getAppId
export const getAppIdentifier: () => string; // 新增暴露方法 getAppIdentifier
export const getMainElementName: () => object; // 新增暴露方法 getMainElementName
export const getCompatibleDeviceType: () => string; // 新增暴露方法 getCompatibleDeviceType
export const isDebugMode: () => boolean; // 新增暴露方法 isDebugMode
export const getModuleMetadata: () => object; // 新增暴露方法 getModuleMetadata
export const getAbilityResourceInfo: (fileType: string) => object; // 新增暴露方法 getAbilityResourceInfo
```

          **5. js侧调用**                  打开src/main/ets/pages/Index.ets，导入"libentry.so"，调用Native接口打印出获取的信息内容。示例如下：
```text
import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

const DOMAIN = 0x0000;

@Entry
@Component
struct Index {
@State message: string = 'Hello World';

build() {
Row() {
Column() {
Text(this.message)
.fontSize(\$r('app.float.page_text_font_size'))
.fontWeight(FontWeight.Bold)
.onClick(() => {
this.message = 'Welcome';
hilog.info(DOMAIN, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
let appInfo = testNapi.getCurrentApplicationInfo();
console.info("bundleNative getCurrentApplicationInfo success, data is " + JSON.stringify(appInfo));
let appId = testNapi.getAppId();
console.info("bundleNative getAppId success, appId is " + appId);
let appIdentifier = testNapi.getAppIdentifier();
console.info("bundleNative getAppIdentifier success, appIdentifier is " + appIdentifier);
let mainElement = testNapi.getMainElementName();
console.info("bundleNative getMainElementName success, data is " + JSON.stringify(mainElement));
let deviceType = testNapi.getCompatibleDeviceType();
console.info("bundleNative getCompatibleDeviceType success, deviceType is " + deviceType);
let isDebugMode = testNapi.isDebugMode();
console.info("bundleNative isDebugMode success, isDebugMode is " + isDebugMode);
let moduleMetadata = testNapi.getModuleMetadata();
console.info("bundleNative getModuleMetadata success, data is " + JSON.stringify(moduleMetadata));
let fileType: string = '.png';
let abilityResourceInfo = testNapi.getAbilityResourceInfo(fileType);
console.info("bundleNative getAbilityResourceInfo success, data is " + JSON.stringify(abilityResourceInfo));
})
}
.width('100%')
}
.height('100%')
}
}
```

          关于包管理NDK接口说明，可参考[Native_Bundle模块介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle)。
