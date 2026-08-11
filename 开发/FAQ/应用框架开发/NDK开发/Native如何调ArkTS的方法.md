# Native如何调ArkTS的方法

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-30

1. 在index.d.ts文件中提供 ArkTS 接口方法。
 
```text
export const nativeCallArkTS: (a: object) => number;
```
 
2. 实现Native侧的NativeCallArkTS接口，代码如下：
 
```text
static napi_value NativeCallArkTS(napi_env env, napi_callback_info info) 
{     
    size_t argc = 1; 
   <em> // Declaring parameter array ARG</em>
    napi_value args[1] = { nullptr }; 
 
   <em> // Retrieve the passed parameters and place them in the parameter array 'args'</em>
    napi_get_cb_info(env, info, &argc, args , nullptr, nullptr); 
 
   <em> // Create int as an input parameter for ArkTS</em>
    napi_value argv = nullptr;     
    napi_create_int32(env, 2, &argv ); 
 
  <em>  // Call the incoming callback and return the result</em>
    napi_value result = nullptr; 
    napi_call_function(env, nullptr, args[0], 1, &argv, &result); 
    return result; 
}
```
 
3. 在ArkTS侧，通过nativeModule.nativeCallArkTS()方法传入回调函数。
 
entry/src/main/ets/pages/Index.ets
 
```text
<em>// Introduce native capabilities through import.</em>
import nativeModule from 'libentry.so'

@Entry
@Component
struct InvokeArkTSMethod {
  @State message: string = 'Test Node-API nativeCallArkTS result: ';

  build() {
    Row() {
      Column() {
       <em> // Call the nativeCallArkTS method, corresponding to the Native NativeCallArkTS, and call the ArkTS function in Native.</em>
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message += nativeModule.nativeCallArkTS((a: number) => {
              return a * 2;
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
 
**参考链接**
 
[Node-API典型使用场景](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-scenarios)
