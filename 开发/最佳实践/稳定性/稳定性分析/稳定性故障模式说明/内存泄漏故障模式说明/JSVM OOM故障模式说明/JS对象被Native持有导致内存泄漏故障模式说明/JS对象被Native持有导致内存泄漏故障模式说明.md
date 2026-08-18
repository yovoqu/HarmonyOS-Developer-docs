# JS对象被Native持有导致内存泄漏故障模式说明

更新时间：2026-08-17 09:32:31

来源：https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-jsvm-oom-js-object-held-by-native

JSVM-API允许开发者通过创建引用、作用域等方式管理JS对象的生命周期，应合理使用这些接口，避免应用运行过程中产生过大的内存峰值。本文列举了五种JSVM-API错误使用的场景，分析JS对象被Native侧引用导致内存未及时释放的问题，并通过堆快照文件展示这些场景的堆内存特征。
 
本文将介绍以下内容：
 
- [根因描述](#section195923221756)
- [问题分析思路](#section757914312136)
- [关键字](#section561510114274)
- [案例一：JS对象引用未删除导致内存泄漏](#section915417229281)
- [案例二：未正确管理引用计数导致内存泄漏](#section10364014102813)
- [案例三：大对象生命周期超出实际业务需要导致内存泄漏](#section18426258154718)
- [案例四：未关闭Handle Scope导致内存泄漏](#section96598594204)
- [案例五：未销毁env导致内存泄漏](#section19604474275)

 

#### 根因描述

JSVM-API允许Native侧通过接口持有JS对象或其引用，辅助业务逻辑完整执行。有五种典型的使用场景，以及可能触发OOM的情况：
 1. JS对象引用未删除导致内存泄漏：OH_JSVM_CreateReference()、OH_JSVM_DeleteReference()可以让Native（如C++代码）侧引用某个JS对象，延长JS对象的生命周期， 配合完成业务逻辑。当大量引用未调用删除接口时，会引发OOM。
2. 未正确管理引用计数导致内存泄漏：OH_JSVM_ReferenceRef()、OH_JSVM_ReferenceUnref()可以管理引用计数，这两个接口通常与第一点中提到的引用创建、删除接口一起使用。业务逻辑通常会在OH_JSVM_ReferenceUnref()出参返回的新计数值为零时，调用OH_JSVM_DeleteReference()删除引用关系。因此，引用计数管理出现非预期的引用值时，会导致引用未删除，引发OOM。
3. 大对象生命周期超出实际业务需要导致内存泄漏：OH_JSVM_OpenHandleScope()、OH_JSVM_CloseHandleScope()可以管理Native侧创建的JS对象的生命周期。当大对象生命周期超出实际业务需要，应用内存占用处于较高水平，容易引发OOM。
4. 未关闭Handle Scope导致内存泄漏：OH_JSVM_OpenHandleScope()、OH_JSVM_CloseHandleScope()未成对调用，JS对象的生命周期和内存占用与开发者预期不符，容易引发OOM。
5. 未销毁env导致内存泄漏：OH_JSVM_CreateEnv()、OH_JSVM_DestroyEnv()可以管理用于执行JS代码的上下文结构（简称env），env中会存放生命周期较长的对象，包含虚拟机本身的各种方法，以及JS源码创建的Global对象。当env中包含大量Global对象，且未销毁时，会引发OOM。
 
 

#### 问题分析思路
1. 获取问题场景的Heap Snapshot，使用Chrome浏览器的DevTools展示各类JS对象在内存中的占比。
2. 将内存占比从高到低排序，关注Global handle、Handle scope、NativeContext的内存占用。
3. 开发者可结合源码，逐对象分析内存占用的合理性，找到引发OOM的对象。
 
 

#### 关键字

在Heap Snapshot引用链中找到以下关键字：
 
- Global handles：C++代码为了长期保留一个JS对象的引用而创建的持久化句柄，在生成Heap Snapshot时归入Global handles。
- Handle scope：Handle scope本身不是具体的JS对象，它可以抽象为作用域的概念。在Heap Snapshot文件中，Handle scope下面挂着的JS对象是在当前Handle scope范围内创建的JS对象，这些对象会随着Handle scope的销毁被释放。
- NativeContext：可将其理解为独立的JS运行沙盒，global_object展示了它所包含的JS Global对象。
- global_object：JSVM-API创建的env下包含的Global对象，在生成Heap Snapshot时归入global_object。

 
 

#### 案例一：JS对象引用未删除导致内存泄漏

以下为负向用例，用于说明JS对象引用使用完成后未删除导致的内存泄漏。该用例首先调用OH_JSVM_CreateArray()在当前作用域创建数组对象，随后调用OH_JSVM_CreateReference()创建数组对象的引用，并注释掉了对OH_JSVM_DeleteReference()的调用，最后调用OH_JSVM_CloseHandleScope()关闭当前作用域。由于对象引用未被删除，其引用的数组对象也无法随作用域关闭而回收，最终导致内存泄漏。
 
```cpp
static int32_t TestJsvmReference()
{
    OH_LOG_INFO(LOG_APP, "TestJsvmReference");
    JSVM_InitOptions initOptions = {0};
    JSVM_VM vm;
    JSVM_Env env = nullptr;
    JSVM_VMScope vmScope;
    JSVM_EnvScope envScope;
    JSVM_HandleScope handleScope;

    // Initialize the JS engine instance.
    if (g_aa == 0) {
        g_aa++;
        Check(OH_JSVM_Init(&initOptions));
    }

    // Prepare the JSVM environment.
    Check(OH_JSVM_CreateVM(nullptr, &vm));
    Check(OH_JSVM_OpenVMScope(vm, &vmScope));
    Check(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
    CheckRet(OH_JSVM_OpenEnvScope(env, &envScope), env);
    CheckRet(OH_JSVM_OpenHandleScope(env, &handleScope), env);

    // Create a JS array object and fill its elements.
    JSVM_Value array = nullptr;
    const size_t arrayLength = 1024;
    OH_JSVM_CreateArray(env, &array);
    for (int i = 0; i < arrayLength; i++) {
        char newStr[] = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ"
                        "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ"
                        "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ";
        JSVM_Value string = nullptr;
        CheckRet(OH_JSVM_CreateStringUtf8(env, newStr, JSVM_AUTO_LENGTH, &string), env);
        CheckRet(OH_JSVM_SetElement(env, array, i, string), env);
    }

    // Create a reference to the array object.
    JSVM_Ref ref;
    uint32_t refCountInit = 2;
    OH_JSVM_CreateReference(env, array, refCountInit, &ref);

    // In principle, when the usage of an object reference ends, it is necessary to call the
    // OH_JSVM_DeleteReference(env, ref) interface to delete the reference, ensuring that the memory occupied by the
    // reference and the referenced object can be properly released. Here, we deliberately omit calling the
    // OH_JSVM_DeleteReference(env, ref) interface to observe the heap memory situation.

    // Destroy the JSVM environment.
    CheckRet(OH_JSVM_CloseHandleScope(env, handleScope), env);

    // Export the JS heap memory in Heap Snapshot format.
    JSVM_CallbackInfo info;
    HeapMgmtTest(env, info);

    CheckRet(OH_JSVM_CloseEnvScope(env, envScope), env);
    Check(OH_JSVM_DestroyEnv(env));
    Check(OH_JSVM_CloseVMScope(vm, vmScope));
    Check(OH_JSVM_DestroyVM(vm));
    return 0;
}

static napi_value RunTestJsvmReference([[maybe_unused]] napi_env env, [[maybe_unused]] napi_callback_info info)
{
    TestJsvmReference();
    return nullptr;
}
```
 
 
HeapMgmtTest()函数封装了OH_JSVM_TakeHeapSnapshot()的调用细节。作用域关闭后，调用HeapMgmtTest()导出堆内存快照，开发者可通过分析该快照了解对象引用在堆内存快照上的特征，以辅助分析类似问题场景。
 

#### 分析思路

获取问题场景中Heap Snapshot的方法已在[堆内存快照](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-overview-of-jsvm-oom-fault-modes#section08171224103515)章节中介绍，本节介绍通过Chrome浏览器DevTools分析Heap Snapshot文件的流程。
 
1. 打开Chrome浏览器，按F12打开DevTools。
 
2. 在Memory页中，单击Load profile，上传内存快照文件，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/Igr-tUfARgSPNHh6ZBHSJw/zh-cn_image_0000002677658546.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=A29FD8965B770259B9434FECBBFFE48626FA26BE06AA795DC5FE8463CA5A21E1)

 

 
3. 打开后，默认显示Summary视图（按对象构造函数分组），按Retained size从大到小排序，可见68%的内存分布在Array对象中，Array中包含大量字符串元素，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/oWJmMLekQn-bQ74Ecmb85Q/zh-cn_image_0000002707458407.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=0D0C780F41AB8FDC7980F52F3FD99727FCF2086E646A6963C3FA930C2A9F58DC)

 
4. 切换至Containment视图（按引用关系追溯），按Retained size从大到小排序，依次展开Retained size最大的节点，直至无法进一步细分，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/kVLKVWITS0-cZuDHQXTa-A/zh-cn_image_0000002677818396.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=56E20EFF6AC5B19350820A144411656C4A1E53D23676BA524F5D8CD6C561C07F)

 
可见大量内存被Global handles引用，这是Native侧对JS对象的引用。
 
 
5. 结合内存快照中给出的对象类型以及其他信息，找到OH_JSVM_CreateReference()调用点，并梳理其对应的OH_JSVM_DeleteReference()是否正确执行。
 

#### 预防建议

引用的管理与Native代码结合，注意引用创建、删除是否成对出现。
 
 

#### 案例二：未正确管理引用计数导致内存泄漏

以下为负向用例，用于说明未正确管理引用计数导致的内存泄漏。该用例依次调用OH_JSVM_CreateArray()创建数组对象、OH_JSVM_CreateReference()创建数组对象引用、两次OH_JSVM_ReferenceRef()将引用计数增加2、一次OH_JSVM_ReferenceUnref()将引用计数减少1。由于引用计数与创建引用的初始值时不一致，OH_JSVM_DeleteReference()未被调用，导致内存泄漏。
 
```cpp
static int32_t TestJsvmReferenceRef()
{
    OH_LOG_INFO(LOG_APP, "TestJsvmReferenceRef");
    JSVM_InitOptions initOptions = {0};
    JSVM_VM vm;
    JSVM_Env env = nullptr;
    JSVM_VMScope vmScope;
    JSVM_EnvScope envScope;
    JSVM_HandleScope handleScope;

    // Initialize the JS engine instance.
    if (g_aa == 0) {
        g_aa++;
        Check(OH_JSVM_Init(&initOptions));
    }

    // Prepare the JSVM environment.
    Check(OH_JSVM_CreateVM(nullptr, &vm));
    Check(OH_JSVM_OpenVMScope(vm, &vmScope));
    Check(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
    CheckRet(OH_JSVM_OpenEnvScope(env, &envScope), env);
    CheckRet(OH_JSVM_OpenHandleScope(env, &handleScope), env);

    // Create a JS array object and fill its elements.
    JSVM_Value array = nullptr;
    const size_t arrayLength = 1024;
    OH_JSVM_CreateArray(env, &array);
    for (int i = 0; i < arrayLength; i++) {
        char newStr[] = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ"
                        "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ"
                        "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ";
        JSVM_Value string = nullptr;
        CheckRet(OH_JSVM_CreateStringUtf8(env, newStr, JSVM_AUTO_LENGTH, &string), env);
        CheckRet(OH_JSVM_SetElement(env, array, i, string), env);
    }

    // Create a reference to the array object.
    JSVM_Ref ref;
    uint32_t refCountInit = 2;
    OH_JSVM_CreateReference(env, array, refCountInit, &ref);

    uint32_t refCount;
    // Increase the reference count using OH_JSVM_ReferenceRef.
    OH_JSVM_ReferenceRef(env, ref, &refCount);
    OH_JSVM_ReferenceRef(env, ref, &refCount);
    // Decrease the reference count using OH_JSVM_ReferenceUnref.
    OH_JSVM_ReferenceUnref(env, ref, &refCount);
    // Because OH_JSVM_ReferenceUnref was called one less time, the reference count differs from its initial value when
    // the reference was created. As a result, the following condition is not met, and the OH_JSVM_DeleteReference
    // interface is never called.
    if (refCount == refCountInit) {
        OH_JSVM_DeleteReference(env, ref);
    }

    // Destroy the JSVM environment.
    CheckRet(OH_JSVM_CloseHandleScope(env, handleScope), env);

    // Export the JS heap memory in Heap Snapshot format.
    JSVM_CallbackInfo info;
    HeapMgmtTest(env, info);

    CheckRet(OH_JSVM_CloseEnvScope(env, envScope), env);
    Check(OH_JSVM_DestroyEnv(env));
    Check(OH_JSVM_CloseVMScope(vm, vmScope));
    Check(OH_JSVM_DestroyVM(vm));
    return 0;
}

static napi_value RunTestJsvmReferenceRef([[maybe_unused]] napi_env env, [[maybe_unused]] napi_callback_info info)
{
    TestJsvmReferenceRef();
    return nullptr;
}
```
 
 
HeapMgmtTest()封装了OH_JSVM_TakeHeapSnapshot()的调用细节。在作用域关闭后，调用HeapMgmtTest()导出堆内存快照，开发者可通过分析该快照了解对象引用在堆内存快照中的特征，以辅助分析类似问题。
 

#### 分析思路

获取问题场景中Heap Snapshot的方法已在[堆内存快照](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-overview-of-jsvm-oom-fault-modes#section08171224103515)章节中介绍，本节介绍通过Chrome浏览器DevTools分析Heap Snapshot文件的流程。
 
1. 打开Chrome浏览器，按F12打开DevTools。
 
2. 在Memory页中，单击Load profile，上传内存快照文件，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/3dFbSzqIRhC-CtyORCGvZw/zh-cn_image_0000002707578257.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=387D9252A2F5128193949371AF82D4D306394BCEE6B2A7D0D3C8894AF8B5CD51)

 

 
3. 打开后，默认显示Summary视图（按对象构造函数分组），按Retained size从大到小排序，可见68%的内存分布在Array对象中，Array中包含大量的字符串元素，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/1oP-xOtxRSWx5WR0j81Z-A/zh-cn_image_0000002677658548.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=6F9A971EE7238D646572B5AC4511A28B59F7F0F2918851BD9F8381833A332B36)

 
4. 切换至Containment视图（按引用关系追溯），按Retained size从大到小排序，依次展开Retained size最大的节点，直至无法进一步细分，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Zpy3QHWPQ_qbOV2c-EkNXw/zh-cn_image_0000002707458409.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=978DB057CA5A245CC2E55D9488FE6ABEB084B0100394D25FEDAB5B01FE8EC56B)

 
可见大量内存被Global handles引用，通常情况下这是Native侧对JS对象的引用。
 
5. 结合内存快照中给出的对象类型以及其他信息，走读代码，找到OH_JSVM_CreateReference()对应的JSVM_Ref对象，在业务代码上下文中梳理对该JSVM_Ref对象引用计数的管理，即OH_JSVM_ReferenceRef()、OH_JSVM_ReferenceUnref()是否成对出现。
 
 

#### 预防建议

引用管理在Native侧代码应用较多，需注意引用的创建与删除及引用计数的管理逻辑，在多线程场景下需注意数据竞争导致引用计数出现非预期的情况。
 
 

#### 案例三：大对象生命周期超出实际业务需要导致内存泄漏

以下为负向用例，用于说明大对象生命周期超出业务需求导致的内存泄漏。该用例调用OH_JSVM_OpenHandleScope()构建管理JS对象的作用域，随后使用花括号构建C++作用域，在C++作用域内调用OH_JSVM_CreateArray()创建数组对象。由于C++语法限制，该数组对象仅在花括号内可用，但其生命周期与管理JS对象的作用域一致。因此，在右花括号至OH_JSVM_CloseHandleScope()接口调用之间，数组对象占用的内存即为泄漏。该用例借助花括号语法凸显问题关键，在实际业务场景中，开发者应注意大对象生命周期管理，尽可能早地释放大对象。
 
```cpp
static int32_t TestJsvmHandleScopeEscape()
{
    OH_LOG_INFO(LOG_APP, "TestJsvmHandleScopeEscape");
    JSVM_InitOptions initOptions = {0};
    JSVM_VM vm;
    JSVM_Env env = nullptr;
    JSVM_VMScope vmScope;
    JSVM_EnvScope envScope;
    JSVM_HandleScope handleScope;

    // Initialize the JS engine instance.
    if (g_aa == 0) {
        g_aa++;
        Check(OH_JSVM_Init(&initOptions));
    }

    // Prepare the JSVM environment.
    Check(OH_JSVM_CreateVM(nullptr, &vm));
    Check(OH_JSVM_OpenVMScope(vm, &vmScope));
    Check(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
    CheckRet(OH_JSVM_OpenEnvScope(env, &envScope), env);

    // Create the outer Handle Scope.
    CheckRet(OH_JSVM_OpenHandleScope(env, &handleScope), env);
    {
        // Due to business logic requirements, a large array object needs to be created here. In principle, this large
        // array object requires an independent Handle Scope to precisely manage its lifecycle and avoid prolonged
        // memory occupation.
        JSVM_Value array = nullptr;
        const size_t arrayLength = 1024;
        // Because the inner Handle Scope was not created,
        // the lifecycle of the large array object is bound to the outer Handle Scope.
        OH_JSVM_CreateArray(env, &array);
        for (int i = 0; i < arrayLength; i++) {
            char newStr[] = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ"
                            "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ"
                            "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ";
            JSVM_Value string = nullptr;
            CheckRet(OH_JSVM_CreateStringUtf8(env, newStr, JSVM_AUTO_LENGTH, &string), env);
            CheckRet(OH_JSVM_SetElement(env, array, i, string), env);
        }
    }
    // Outside the scope, the array object cannot be used, but the memory it occupies is still not released.

    // Export the JS heap memory in Heap Snapshot format.
    JSVM_CallbackInfo info;
    HeapMgmtTest(env, info);

    // Destroy the JSVM environment.
    CheckRet(OH_JSVM_CloseHandleScope(env, handleScope), env);
    CheckRet(OH_JSVM_CloseEnvScope(env, envScope), env);
    Check(OH_JSVM_DestroyEnv(env));
    Check(OH_JSVM_CloseVMScope(vm, vmScope));
    Check(OH_JSVM_DestroyVM(vm));
    return 0;
}

static napi_value RunTestJsvmHandleScopeEscape([[maybe_unused]] napi_env env, [[maybe_unused]] napi_callback_info info)
{
    TestJsvmHandleScopeEscape();
    return nullptr;
}
```
 
 
HeapMgmtTest()函数封装了OH_JSVM_TakeHeapSnapshot()的调用细节。在右花括号至OH_JSVM_CloseHandleScope()接口调用之间，调用HeapMgmtTest()导出堆内存快照，开发者可分析该快照，了解作用域中JS对象在堆内存快照中的特征，以辅助分析相关问题场景。
 

#### 分析思路

获取问题场景中Heap Snapshot的方法已在[堆内存快照](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-overview-of-jsvm-oom-fault-modes#section08171224103515)章节中介绍，本节介绍通过Chrome浏览器DevTools分析Heap Snapshot文件的流程。
 
1. 打开Chrome浏览器，按下F12打开DevTools。
 
2. 在Memory页中，单击Load profile，上传内存快照文件，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Cht7ywWbQjyID8elMSDx7A/zh-cn_image_0000002677818398.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=7D759291F731611AF07C6A54CC44AF4A606C35E3391AA5CCB3DB71088E7FF89E)

 

 
3. 打开后，默认显示Summary视图（按对象构造函数分组），按Retained size从大到小排序，可见66%的内存分布在(string)类对象中，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/ld0u2XlkQ_-P1cVpWDFUuA/zh-cn_image_0000002707578259.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=B67DE6AEB6DB7B398949510033FC1809B204E33CCD9E126444F0C162518A07C3)

 
4. 切换至Containment视图（按引用关系追溯），按Retained size从大到小排序，依次展开Retained size最大的节点，直到无法进一步拆解，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/wwN0cgjqTUWtG7cw-3kh6A/zh-cn_image_0000002677658550.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=236CF0A6AE7ACCF39E5D7CB2F5AF076B2E704B758DF8A4D6298BEF1332B5889D)

 
可见大部分内存被Handle scopes引用，这是创建在作用域内的JS对象。
 
 
5. 结合内存快照中给出的对象类型以及其他信息，走读代码，结合业务上下文，找到该大对象创建的位置。
 

#### 预防建议

大对象在符合业务需求的前提下应尽可能早地释放。
 
 

#### 案例四：未关闭Handle Scope导致内存泄漏

以下为负向用例，用于说明未关闭Handle Scope导致的内存泄漏。该用例两次调用OH_JSVM_OpenHandleScope()构建出内外两层Handle Scope，并在内层Handle Scope中调用OH_JSVM_CreateArray()创建数组对象。该用例注释了内层Handle Scope的OH_JSVM_CloseHandleScope()调用，导致数组对象的生命周期从注释处延长到下一个OH_JSVM_CloseHandleScope()调用之前。在此期间，数组对象所占据的内存属于泄漏。
 
```cpp
static int32_t TestJsvmUnUseCloseHandleScope()
{
    OH_LOG_INFO(LOG_APP, "TestJsvmUnUseCloseHandleScope");
    JSVM_InitOptions initOptions = {0};
    JSVM_VM vm;
    JSVM_Env env = nullptr;
    JSVM_VMScope vmScope;
    JSVM_EnvScope envScope;
    JSVM_HandleScope handleScope;

    // Initialize the JS engine instance.
    if (g_aa == 0) {
        g_aa++;
        Check(OH_JSVM_Init(&initOptions));
    }

    // Prepare the JSVM environment.
    Check(OH_JSVM_CreateVM(nullptr, &vm));
    Check(OH_JSVM_OpenVMScope(vm, &vmScope));
    Check(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
    CheckRet(OH_JSVM_OpenEnvScope(env, &envScope), env);

    // Create the outer Handle Scope.
    CheckRet(OH_JSVM_OpenHandleScope(env, &handleScope), env);
    {
        // Due to business logic requirements, a large array object needs to be created here, and an independent Handle
        // Scope should be constructed to precisely manage its lifecycle, avoiding prolonged memory occupation.
        CheckRet(OH_JSVM_OpenHandleScope(env, &handleScope), env);
        JSVM_Value array = nullptr;
        const size_t arrayLength = 1024;
        // The lifecycle of the array object is bound to the inner Handle Scope.
        OH_JSVM_CreateArray(env, &array);
        for (int i = 0; i < arrayLength; i++) {
            char newStr[] = "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ"
                            "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ"
                            "AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQIISSTTUUVVWWXXYYZZ";
            JSVM_Value string = nullptr;
            CheckRet(OH_JSVM_CreateStringUtf8(env, newStr, JSVM_AUTO_LENGTH, &string), env);
            CheckRet(OH_JSVM_SetElement(env, array, i, string), env);
        }
        // The OH_JSVM_CloseHandleScope interface was not called to close the inner Handle Scope,
        // so the large array object remains alive.
    }

    // Export the JS heap memory in Heap Snapshot format.
    JSVM_CallbackInfo info;
    HeapMgmtTest(env, info);

    // Destroy the JSVM environment.
    CheckRet(OH_JSVM_CloseHandleScope(env, handleScope), env);
    CheckRet(OH_JSVM_CloseEnvScope(env, envScope), env);
    Check(OH_JSVM_DestroyEnv(env));
    Check(OH_JSVM_CloseVMScope(vm, vmScope));
    Check(OH_JSVM_DestroyVM(vm));
    return 0;
}

static napi_value RunTestJsvmUnUseCloseHandleScope([[maybe_unused]] napi_env env,
                                                   [[maybe_unused]] napi_callback_info info)
{
    TestJsvmUnUseCloseHandleScope();
    return nullptr;
}
```
 
 
HeapMgmtTest()函数封装了OH_JSVM_TakeHeapSnapshot()的调用细节。在右花括号到OH_JSVM_CloseHandleScope()接口调用之间，调用HeapMgmtTest()导出堆内存快照，开发者可通过分析该快照了解JS对象作用域中的对象在堆内存快照上的特征，以辅助分析类似问题场景。
 

#### 分析思路

获取问题场景中Heap Snapshot的方法已在[堆内存快照](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-overview-of-jsvm-oom-fault-modes#section08171224103515)章节中介绍，本节介绍通过Chrome浏览器DevTools分析Heap Snapshot文件的流程。
 
1. 打开Chrome浏览器，按下F12打开DevTools。
 
2. 在Memory页中，单击Load profile，上传内存快照文件，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/9plXlxe_RNmupAfQpWbb3A/zh-cn_image_0000002707458411.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=4C215CA30FCCFD70F4454B71FB8E86326C7C0ADEAB694996ED1375D4CB36B271)

 

 
3. 打开后，默认显示Summary视图（按对象构造函数分组），按Retained size从大到小排序，可见66%的内存分布在(string)类对象中，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/SS21OLhgTkSdmuYDLXhG_g/zh-cn_image_0000002677818400.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=EE4F8EAF934979734C743ED362EF266BD58EA23E4DAF441CD9F7FBB3B2D94C12)

 
4. 切换至Containment视图（按引用关系追溯），按Retained size从大到小排序，依次展开Retained size最大的节点，直至无法进一步细分，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/z4P-LQ5iQIWr8jT6r3pZ0w/zh-cn_image_0000002707578261.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=97A88289A64D0B2899BCE81032FEC28870F43E612E53D75558814187D4253E6C)

 
可见大量内存被Handle scopes引用，这些是创建在作用域内的JS对象。
 
 
5. 结合内存快照中给出的对象类型以及其他信息，走读代码，结合业务上下文，找到这个大对象创建的位置，并检查对象所在作用域的OH_JSVM_OpenHandleScope()、OH_JSVM_CloseHandleScope()是否成对出现，OH_JSVM_CloseHandleScope()是否有被执行。
 

#### 预防建议

要确保OH_JSVM_OpenHandleScope()、OH_JSVM_CloseHandleScope()成对出现，正确管理Handle Scope。
 
 

#### 案例五：未销毁env导致内存泄漏

以下为负向用例，用于说明未销毁env导致的内存泄漏。该用例调用JSVM-API构建JS代码执行环境，随后执行JS代码创建全局对象largeArray。JS代码执行完毕后调用JSVM-API销毁JS代码执行环境，在销毁环境的过程中，注释OH_JSVM_DestroyEnv()调用，env被保留。因此，挂载在env中的全局变量也不会被回收，导致内存泄漏。
 
```cpp
const char *SRC_CALL_NATIVE_UN_USE_DESTROY_ENV = R"JS(
    var largeArray = new Array(1024 * 1024 * 20).fill(0);
)JS";

static int32_t TestJsvmUnUseDestroyEnv()
{
    OH_LOG_INFO(LOG_APP, "TestJsvmUnUseDestroyEnv");
    JSVM_InitOptions initOptions = {0};
    JSVM_VM vm;
    JSVM_Env env = nullptr;
    JSVM_VMScope vmScope;
    JSVM_EnvScope envScope;
    JSVM_HandleScope handleScope;
    JSVM_Value result;

    // Initialize the JS engine instance.
    if (g_aa == 0) {
        g_aa++;
        Check(OH_JSVM_Init(&initOptions));
    }

    // Prepare the JSVM environment.
    Check(OH_JSVM_CreateVM(nullptr, &vm));
    Check(OH_JSVM_OpenVMScope(vm, &vmScope));
    Check(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
    CheckRet(OH_JSVM_OpenEnvScope(env, &envScope), env);
    CheckRet(OH_JSVM_OpenHandleScope(env, &handleScope), env);

    // Execute JS code, which will create global variables. The lifecycle of these global variables is bound to the env.
    JSVM_Script script;
    JSVM_Value jsSrc;
    CheckRet(OH_JSVM_CreateStringUtf8(env, SRC_CALL_NATIVE_UN_USE_DESTROY_ENV, JSVM_AUTO_LENGTH, &jsSrc), env);
    JSVM_Status status = OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);
    if (status != JSVM_OK) {
        OH_LOG_INFO(LOG_APP, "JSVM OOM Test: UnUseDestroyEnv compile failed");
    } else {
        OH_LOG_INFO(LOG_APP, "JSVM OOM Test: UnUseDestroyEnv compile success: ret is %{public}d", status);
    }
    Check(OH_JSVM_RunScript(env, script, &result));

    // Destroy the JSVM environment.
    CheckRet(OH_JSVM_CloseHandleScope(env, handleScope), env);
    CheckRet(OH_JSVM_CloseEnvScope(env, envScope), env);
    // Without calling OH_JSVM_DestroyEnv to destroy the env, the global variables bound to the env remain alive.

    // Export the JS heap memory in Heap Snapshot format.
    JSVM_CallbackInfo info;
    HeapMgmtTest(env, info);

    Check(OH_JSVM_CloseVMScope(vm, vmScope));
    Check(OH_JSVM_DestroyVM(vm));
    return 0;
}

static napi_value RunTestJsvmUnUseDestroyEnv([[maybe_unused]] napi_env env, [[maybe_unused]] napi_callback_info info)
{
    TestJsvmUnUseDestroyEnv();
    return nullptr;
}
```
 
 
HeapMgmtTest()函数封装了OH_JSVM_TakeHeapSnapshot()的调用细节。在OH_JSVM_DestroyEnv()注释点到OH_JSVM_CloseVMScope()接口调用之间，调用HeapMgmtTest()导出堆内存快照，开发者可通过分析该快照，了解JS全局对象在堆内存快照上的特征，以辅助分析类似问题场景。
 

#### 分析思路

获取问题场景中Heap Snapshot的方法已在[堆内存快照](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-overview-of-jsvm-oom-fault-modes#section08171224103515)章节中介绍，本节介绍通过Chrome浏览器DevTools分析Heap Snapshot文件的流程。
 
1. 打开Chrome浏览器，按下F12打开DevTools。
 
2. 在Memory页中，单击Load profile，上传内存快照文件，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/nirOryz8R1CEr3FHbFr2oA/zh-cn_image_0000002677658552.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=06BD627729210668CF35598D2E89BCDBD63E5E92BE05E41D77AACF31B956C10B)

 

 
3. 打开后，默认显示Summary视图（按对象构造函数分组），按Retained size从大到小排序，可见100%的内存分布在global_object中，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/rtmURuJMQ8CMvPikMQUXNw/zh-cn_image_0000002707458413.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=A17D1B4AD89798218751BB1590B2B8DE8000EEC7A66DEA60411214F3C94F09E1)

 
4. 切换至Containment视图（按引用关系追溯），按Retained size从大到小排序，依次展开Retained size最大的节点，直至无法进一步细分，如下图所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/sbANxnSrS2eTJO9jei6TVQ/zh-cn_image_0000002677818402.png?HW-CC-KV=V1&HW-CC-Date=20260818T063941Z&HW-CC-Expire=86400&HW-CC-Sign=7118989C6A5C3498492637B44ABF8C8ECAB0C401C232FDE6729B468D43E1BC8D)

 
可见大量内存被global_object引用，内存占用集中在全局对象。
 
 
5. 结合内存快照中给出的对象类型以及其他信息，走读代码，找到这个全局对象对应的上下文环境，检查OH_JSVM_CreateEnv()、OH_JSVM_DestroyEnv()是否成对出现，OH_JSVM_DestroyEnv()是否有被执行。
 

#### 预防建议

要确保OH_JSVM_CreateEnv()、OH_JSVM_DestroyEnv()成对出现，正确管理env。
