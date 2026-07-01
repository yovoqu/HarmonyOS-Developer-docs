# 如何实现ArkTS到Native的跨模块长调用

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-7

#### 问题现象

整个调用链为hap ArkTS->har ArkTS->har Native侧->har ArkTS。设定hap模块为entry。
 1. entry模块ArkTS调用har ArkTS侧A.ets页面导出的接口。
2. har ArkTS侧A.ets页面中接口调用har Native侧的方法。
3. har Native侧方法通过napi_load_module_with_info来加载har ArkTS侧B.ets导出的自定义接口。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/FX_zAxBRSuWzsFhuc-a8tw/zh-cn_image_0000002659258289.png?HW-CC-KV=V1&HW-CC-Date=20260701T041135Z&HW-CC-Expire=86400&HW-CC-Sign=011F2A97F1A7791BC7F1AC1ED4658515E7EB0308D23724A700DBC6878C19766E)

 
har的ArkTS侧将函数包裹在命名空间中导出，其Native侧用napi_get_named_property加载函数，加载失败。
 
问题代码示例参考如下：
 
```ArkTS
<em>// har</em><em><span style="color: rgb(128,128,128);">包的</span><span style="color: rgb(128,128,128);">ObjectUtil.ets</span></em>
namespace  <span style="color: rgb(255,255,255);">ObjectUtil</span><span style="color: rgb(181,106,1);">{</span>
  export function <span style="color: rgb(0,0,255);">testOne</span><span style="color: rgb(255,0,170);">()</span><span style="color: rgb(181,106,1);">{</span>
    <span style="color: rgb(255,255,255);">console</span><span style="color: rgb(181,106,1);">.</span><span style="color: rgb(0,0,255);">info</span><span style="color: rgb(255,0,170);">(</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(132,63,161);">你好，世界！</span><span style="color: rgb(132,63,161);">'</span><span style="color: rgb(255,0,170);">)</span>
  <span style="color: rgb(181,106,1);">}</span>
<span style="color: rgb(181,106,1);">}</span>

export <span style="color: rgb(181,106,1);">{</span><span style="color: rgb(255,255,255);">ObjectUtil</span><span style="color: rgb(181,106,1);">}</span>
```
 
```cpp
<em>// har包的napi_init.cpp</em>
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">loadModule</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>) {
    napi_value result;
 <em>   // 1.使用napi_load_module_with_info加载Test文件中的模块</em>
    napi_status status <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">napi_load_module_with_info</span>(env, <span style="color: rgb(181,106,1);">"mytest_sdk/src/main/ets/common/ObjectUtil"</span>,
                                                    <span style="color: rgb(181,106,1);">"com.example.sodemo/mytest_sdk"</span>, <span style="color: rgb(128,128,128);">&</span>result);
    <span style="color: rgb(255,0,170);">if</span> (status <span style="color: rgb(128,128,128);">!=</span> napi_ok) {
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
    napi_value testFn;
   <em> // 2.使用napi_get_named_property获取test函数</em>
    status <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">napi_get_named_property</span>(env, result, <span style="color: rgb(181,106,1);">"testOne"</span>, <span style="color: rgb(128,128,128);">&</span>testFn); <em>// 获取失败，status：napi_object_expected</em>
    <span style="color: rgb(255,0,170);">if</span> (status <span style="color: rgb(128,128,128);">!=</span> napi_ok) {
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
 <em>   // 3.使用napi_call_function调用函数test</em>
    status <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">napi_call_function</span>(env, result, testFn, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
    <span style="color: rgb(255,0,170);">if</span> (status <span style="color: rgb(128,128,128);">!=</span> napi_ok) {
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
    <span style="color: rgb(255,0,170);">return</span> result;
}
```
 
 

#### 背景知识

应用开发中往往是由多个业务组共同完成一个APP的开发，每个业务组都有自己的工程，业务组会以HSP或har包的形式提供SDK能力给各个hap模块使用，这些SDK往往会提供C++接口或ets接口供其他模块直接调用。har包构建参考[如何构建har包并导出Native方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package#导出native方法)。
 
Node-API中的[napi_load_module_with_info](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-load-module-with-info#napi_load_module_with_info支持的场景)接口的功能是进行模块的加载，当模块加载出来之后，可以使用函数napi_get_property获取模块导出的变量，也可以使用napi_get_named_property获取模块导出的函数。
 
```text
<span style="color: rgb(0,0,255);">napi_status</span> <span style="color: rgb(181,106,1);">napi_load_module_with_info</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>,
                                       <span style="color: rgb(0,0,255);">const</span> <span style="color: rgb(0,0,255);">char*</span> <span style="color: rgb(0,0,255);">path</span>,
                                       <span style="color: rgb(0,0,255);">const</span> <span style="color: rgb(0,0,255);">char*</span> <span style="color: rgb(0,0,255);">module_info</span>,
                                       <span style="color: rgb(0,0,255);">napi_value</span><span style="color: rgb(0,0,255);">*</span> <span style="color: rgb(0,0,255);">result</span>);
```
  
| 参数 | 说明 |
| --- | --- |
| env | 当前的虚拟机环境。 |
| path | 加载的文件路径或者模块名。 |
| module_info | bundleName/moduleName的路径拼接。 |
| result | 加载的模块。 |
 
 
 

#### 解决方案
1. har的ArkTS侧导出接口时包裹了一层namespace，Native侧在加载时需要用napi_get_named_property()先获取到命名空间对象，再去获取函数对象（一共获取两次），无法直接获取函数。
2. har是集成到hap中的，其入口模块是hap，即entry模块。所以napi_load_module_with_info中：
path：加载文件路径或者moduleName。注意此处的moduleName指的是入口模块（即entry模块）中oh-package.json5中dependencies标签下为har定义的名称，而不是har模块的实际名称。

  hap（即entry模块）的oh-package.json5：
```json
{
  <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"entry"</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"version"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"1.0.0"</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"description"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"Please describe the basic information."</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"main"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">""</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"author"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">""</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"license"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">""</span><span style="color: rgb(181,106,1);">,</span>
  <span style="color: rgb(132,63,161);">"dependencies"</span><span style="color: rgb(181,106,1);">: </span>{
    <span style="color: rgb(132,63,161);">"mytest_sdk"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"file:../mytest_sdk"</span>
  }
}
```


  如以上示例，若依赖中配置是"lib_mytest_sdk": "file:../mytest_sdk"，则path参数中的moduleName为lib_mytest_sdk，而非mytest_sdk。即path：“lib_mytest_sdk/src/main/ets/common/ObjectUtil”，非“mytest_sdk/src/main/ets/common/ObjectUtil”。
3. module_info：bundleName/moduleName的路径拼接。此处的moduleName指的是被加载的模块（har）所在的hap下module.json5中module节点的name属性。

  hap（即entry模块）的module.json5：
```ArkTS
{
  <span style="color: rgb(132,63,161);">"module"</span><span style="color: rgb(181,106,1);">: </span>{
    <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"entry"</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(132,63,161);">"type"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"entry"</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(132,63,161);">"description"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$string:module_desc"</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(132,63,161);">"mainElement"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"EntryAbility"</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(132,63,161);">"deviceTypes"</span><span style="color: rgb(181,106,1);">: </span>[
      <span style="color: rgb(80,160,79);">"phone"</span>
    ]<span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(132,63,161);">"deliveryWithInstall"</span><span style="color: rgb(181,106,1);">: true,</span>
    <span style="color: rgb(132,63,161);">"installationFree"</span><span style="color: rgb(181,106,1);">: false,</span>
    <span style="color: rgb(132,63,161);">"pages"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$profile:main_pages"</span><span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(132,63,161);">"abilities"</span><span style="color: rgb(181,106,1);">: </span>[
      {
        <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"EntryAbility"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"srcEntry"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"./ets/entryability/EntryAbility.ets"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"description"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$string:EntryAbility_desc"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"icon"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$media:layered_image"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"label"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$string:EntryAbility_label"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"startWindowIcon"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$media:startIcon"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"startWindowBackground"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$color:start_window_background"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"exported"</span><span style="color: rgb(181,106,1);">: true,</span>
        <span style="color: rgb(132,63,161);">"skills"</span><span style="color: rgb(181,106,1);">: </span>[
          {
            <span style="color: rgb(132,63,161);">"entities"</span><span style="color: rgb(181,106,1);">: </span>[
              <span style="color: rgb(80,160,79);">"entity.system.home"</span>
            ]<span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(132,63,161);">"actions"</span><span style="color: rgb(181,106,1);">: </span>[
              <span style="color: rgb(80,160,79);">"ohos.want.action.home"</span>
            ]
          }
        ]
      }
    ]<span style="color: rgb(181,106,1);">,</span>
    <span style="color: rgb(132,63,161);">"extensionAbilities"</span><span style="color: rgb(181,106,1);">: </span>[
      {
        <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"EntryBackupAbility"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"srcEntry"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"./ets/entrybackupability/EntryBackupAbility.ets"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"type"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"backup"</span><span style="color: rgb(181,106,1);">,</span>
        <span style="color: rgb(132,63,161);">"exported"</span><span style="color: rgb(181,106,1);">: false,</span>
        <span style="color: rgb(132,63,161);">"metadata"</span><span style="color: rgb(181,106,1);">: </span>[
          {
            <span style="color: rgb(132,63,161);">"name"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"ohos.extension.backup"</span><span style="color: rgb(181,106,1);">,</span>
            <span style="color: rgb(132,63,161);">"resource"</span><span style="color: rgb(181,106,1);">: </span><span style="color: rgb(80,160,79);">"$profile:backup_config"</span>
          }
        ]<span style="color: rgb(181,106,1);">,</span>
      }
    ]
  }<span style="color: rgb(181,106,1);">,</span>
```


  如上图所示，module_info参数中的moduleName为入口模块的模块名entry，而非har的模块名mytest_sdk。module_info：com.example.sodemo/entry，非com.example.sodemo/mytest_sdk。
4. 完整示例参考如下：

  har包（即mytest_sdk模块）的napi_init.cpp：
```text
<span style="color: rgb(0,0,255);">static</span> <span style="color: rgb(0,0,255);">napi_value</span> <span style="color: rgb(181,106,1);">TestCall</span>(<span style="color: rgb(0,0,255);">napi_env</span> <span style="color: rgb(0,0,255);">env</span>, <span style="color: rgb(0,0,255);">napi_callback_info</span> <span style="color: rgb(0,0,255);">info</span>)
{
    <span style="color: rgb(0,0,255);">size_t</span> argc <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">2</span>;
    napi_value <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">2</span>] <span style="color: rgb(128,128,128);">=</span> {<span style="color: rgb(0,0,255);">nullptr</span>};
    <span style="color: rgb(181,106,1);">napi_get_cb_info</span>(env, info, <span style="color: rgb(128,128,128);">&</span>argc, args, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
    
    <span style="color: rgb(0,0,255);">size_t</span> len1 <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>; 
    <span style="color: rgb(181,106,1);">napi_get_value_string_utf8</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(128,128,128);">&</span>len1); <em>   // Get string length to len </em>
    <span style="color: rgb(0,0,255);">char</span><span style="color: rgb(128,128,128);">*</span> path <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(255,0,170);">new</span> <span style="color: rgb(0,0,255);">char</span>[len1<span style="color: rgb(128,128,128);">+</span><span style="color: rgb(80,160,79);">1</span>];                                   <em>// Allocate a char array of appropriate size</em>
    <span style="color: rgb(181,106,1);">napi_get_value_string_utf8</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">0</span>], path, len1 <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span>len1); <em> // get string </em>
    
    <span style="color: rgb(0,0,255);">size_t</span> len2 <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(80,160,79);">0</span>; 
    <span style="color: rgb(181,106,1);">napi_get_value_string_utf8</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>], <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(128,128,128);">&</span>len2);   <em> // Get string length to len </em>
    <span style="color: rgb(0,0,255);">char</span><span style="color: rgb(128,128,128);">*</span> moduleInfo <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(255,0,170);">new</span> <span style="color: rgb(0,0,255);">char</span>[len2<span style="color: rgb(128,128,128);">+</span><span style="color: rgb(80,160,79);">1</span>];                                   <em>// Allocate a char array of appropriate size</em>
    <span style="color: rgb(181,106,1);">napi_get_value_string_utf8</span>(env, <span style="color: rgb(0,0,255);">args</span>[<span style="color: rgb(80,160,79);">1</span>], moduleInfo, len2 <span style="color: rgb(128,128,128);">+</span> <span style="color: rgb(80,160,79);">1</span>, <span style="color: rgb(128,128,128);">&</span>len2); <em> // get string </em>
    
    <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"Receive：path[%{public}s], module_info:[%{public}s]</span><span style="color: rgb(181,106,1);">"</span>, path,moduleInfo);
    
    napi_value result;
  <em>  // 1. 使用napi_load_module_with_info加载Test文件中的模块</em>
    napi_status status <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">napi_load_module_with_info</span>(env, path,moduleInfo, <span style="color: rgb(128,128,128);">&</span>result);   
    <span style="color: rgb(255,0,170);">if</span> (status <span style="color: rgb(128,128,128);">!=</span> napi_ok) {
        <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"napi_load_module_with_info加载Test文件中的模块 失败: %{public}d"</span>, status);
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
    napi_value testFn;
    napi_value testNamespace;
   <em> // 2. 使用napi_get_named_property获取命名空间对象</em>
    status <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">napi_get_named_property</span>(env, result, <span style="color: rgb(181,106,1);">"ObjectUtil"</span>, <span style="color: rgb(128,128,128);">&</span>testNamespace);
    <span style="color: rgb(255,0,170);">if</span> (status <span style="color: rgb(128,128,128);">!=</span> napi_ok) {
        <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"napi_get_named_property获取命名空间对象 失败: %{public}d"</span>, status);
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
  <em>  // 2.1 使用napi_get_named_property获取testTwo函数</em>
    status <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">napi_get_named_property</span>(env, testNamespace, <span style="color: rgb(181,106,1);">"testOne"</span>, <span style="color: rgb(128,128,128);">&</span>testFn);
    <span style="color: rgb(255,0,170);">if</span> (status <span style="color: rgb(128,128,128);">!=</span> napi_ok) {
        <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"napi_get_named_property获取testTwo函数 失败: %{public}d"</span>, status);
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
  <em>  // 3. 使用napi_call_function调用函数test</em>
    status <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">napi_call_function</span>(env, testNamespace, testFn, <span style="color: rgb(80,160,79);">0</span>, <span style="color: rgb(0,0,255);">nullptr</span>, <span style="color: rgb(0,0,255);">nullptr</span>);
    <span style="color: rgb(255,0,170);">if</span> (status <span style="color: rgb(128,128,128);">!=</span> napi_ok) {
        <span style="color: rgb(181,106,1);">OH_LOG_INFO</span>(LOG_APP, <span style="color: rgb(181,106,1);">"napi_call_function调用函数test 失败: %{public}d"</span>, status);
        <span style="color: rgb(255,0,170);">return</span> <span style="color: rgb(0,0,255);">nullptr</span>;
    }
    napi_value ret;
    <span style="color: rgb(0,0,255);">std</span>::string str <span style="color: rgb(128,128,128);">=</span> <span style="color: rgb(181,106,1);">"TestCall"</span>;
    <span style="color: rgb(181,106,1);">napi_create_string_utf8</span>(env, <span style="color: rgb(0,0,255);">str</span>.<span style="color: rgb(181,106,1);">c_str</span>(), <span style="color: rgb(0,0,255);">str</span>.<span style="color: rgb(181,106,1);">size</span>(), <span style="color: rgb(128,128,128);">&</span>ret);
    <span style="color: rgb(255,0,170);">return</span> ret;
}
```
