# napi关联的c层对象无法触发GC

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-12

#### 问题现象

在ArkTS创建一个对象，通过napi_wrap将ArkTS对象与Native的C++对象绑定，第一次创建ArkTS对象后触发napi_wrap的垃圾回收回调，等回收完成后再次创建对象，垃圾回收回调不会触发。
 
ArkTS侧创建对象：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/jiJx6WNyS26z5yWxXTkaCw/zh-cn_image_0000002658907827.png?HW-CC-KV=V1&HW-CC-Date=20260701T041133Z&HW-CC-Expire=86400&HW-CC-Sign=87AF284C1057AB8814973DC6FA9DD54DF81AEB992774CFFC5CFCA9FDD2EF081D)

 
C++侧构造函数和析构函数：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/hGQLAUr_TRO7h7gM6_gcZw/zh-cn_image_0000002658787891.png?HW-CC-KV=V1&HW-CC-Date=20260701T041133Z&HW-CC-Expire=86400&HW-CC-Sign=D35F306F21DAB8AD0C5DFE21A833127AC7F8DEBBD015971A15B3E0ADF9EF42DA)

 
napi_wrap绑定ArkTS对象与C++对象：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/WJPFwFjBSxKAHnt_4sHulw/zh-cn_image_0000002628388616.png?HW-CC-KV=V1&HW-CC-Date=20260701T041133Z&HW-CC-Expire=86400&HW-CC-Sign=A254DF5025C2C1D6EC1B212EF84D07211E2424CDEF1C3E9AB122E8935E3AA4D9)

 
 

#### 背景知识

- GC（全称[Garbage Collection](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gc-introduction)），即垃圾回收。在计算机领域，GC是指识别并释放内存中的不再使用的对象，以回收内存空间。
- napi_wrap可以将ArkTS对象与Native的C++对象绑定，后续操作时再通过napi_unwrap将ArkTS对象绑定的C++对象取出，并对其进行操作，详见：[Native与ArkTS对象绑定](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-object-wrap)。
- [napi_wrap_enhance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/napi#napi_wrap_enhance)用于在ArkTS对象上绑定一个NAPI模块对象实例并指定实例大小，开发者可以指定绑定的回调函数是否异步执行，如果异步执行，则回调函数必须是线程安全的。

 
 

#### 问题定位

多次创建对象，析构执行后，再次创建对象不会再执行析构。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/8A97zFsWQsKF6qfWQpA1nQ/zh-cn_image_0000002628548516.png?HW-CC-KV=V1&HW-CC-Date=20260701T041133Z&HW-CC-Expire=86400&HW-CC-Sign=CBD02560F123B8294F9B64625F7D7F2B605C4325B038DE3AC8EFEAF2E679D16F)

 
 

#### 分析结论

ArkTS侧的变量大小如果没有达到GC触发水位线，此时C++侧内存大小不在触发水位线计算范围内，不会触发GC行为，napi_wrap绑定的析构处理回调也不会调用。
 
 

#### 修改建议

将napi_wrap替换为[napi_wrap_enhance](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/napi#napi_wrap_enhance)，napi_wrap_enhance会在绑定的时候把Native对象大小传给虚拟机，实现及时回收，示例代码如下：
 
```text
// 通过napi_wrap将ArkTS对象jsThis与C++对象obj绑定
napi_status status = napi_wrap_enhance(env, jsThis, reinterpret_cast<void *>(obj), MyObject::Destructor, false,
                                       nullptr, // finalizeHint
                                       100 * 1024 * 1024, &obj->wrapper_);
```
 
 

#### 常见FAQ

Q：析构Object时调用了napi_remove_wrap，那么对应的FinalizeCallback是否应该被移除？
 
A：调用[napi_remove_wrap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/napi#napi_remove_wrap)的时候，如果封装中关联有finalize回调，HarmonyOS中该导出接口将在移除封装前调用它。
