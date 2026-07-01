# napi_load_module_with_info使用限制和注意事项

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-19

## napi_load_module_with_info使用限制和注意事项
 


##### 问题现象

[napi_load_module_with_info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/napi#napi_load_module_with_info)支持开发者在C++侧加载工程内模块及文件，该接口在使用时有哪些使用限制和注意事项？
 
 

##### 解决方案

- 参数说明： 
| 参数名 | 含义说明 |
| --- | --- |
| path | 要加载的文件路径/模块名。如：“entry/src/main/ets/Test”。 |
| module_info | app.json5中配置的工程名/待加载模块所在的HAP下module.json5中配置的模块名的路径拼接，如：“com.example.application/entry”。 |
- 异常返回值说明及处理方法： 
| 返回值名 | 含义说明 | 异常处理方法 |
| --- | --- | --- |
| napi_invalid_arg | env/result为nullptr。 | 检查传入的参数，确保参数值准确不为空。 |
| napi_generic_failure | 模块加载失败。 | 检查文件路径/模块信息是否准确，确保目标路径下文件存在。 |
| napi_pending_exception | 调用接口前有未捕获的ArkTS异常。 | 可以参考官方文档中清除异常接口napi_get_and_clear_last_exception和调用前检查异常接口napi_is_exception_pending来定位异常发生的位置。 |

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/eYB61iznQKO47LSrClQUww/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025532Z&HW-CC-Expire=86400&HW-CC-Sign=658934A54D1F05C11C567C1507D624E2DCC2CB291091575FFCD5B3ACEECAC929)
 

- 加载本地工程模块内文件时，要求path以moduleName开头。
- 因为应用间的hsp包也可以通过napi_load_module_with_info接口加载，所以module_info参数中必须指定bundleName和moduleName。
- 编译构建后，HAR模块被打包到各个模块之中，其入口模块仍然是HAP模块。所以在调用HAR模块时，path的模块名称要填HAP模块中oh-package.json5中定义的依赖HAR的名称，而不是HAR模块的实际名称。
- 如果在HAP/HSP中直接或间接使用了三方包，该三方包中使用napi_load_module_with_info接口加载其他模块A，则需要在HAP/HSP中也添加A的依赖。
- 在加载非模块内文件时，需要对调用模块的build-profile.json5进行配置：
```text
buildOption->arkOptions->runtimeOnly->packages->oh-package.json5文件中dependencies配置的依赖名。
```

- 在[napi_create_ark_runtime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/napi#napi_create_ark_runtime)接口创建的运行时环境中使用时，若希望加载的模块不被系统回收，可以通过[napi_create_reference](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/napi#napi_create_reference)方法将模块存储起来。
- 在ohosTest中使用时，需要将加载路径改为“entry/src/ohosTest/ets/test/Ability.test”，module_info中的模块名改成entry_test。

 

 
 

##### 总结

与[napi_load_module](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/napi#napi_load_module)仅支持在主线程使用相比，napi_load_module_with_info不仅支持在主线程中使用，也可以在[新创建的ArkTS基础运行时环境中使用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-ark-runtime)。
 
napi_load_module_with_info支持加载hap/hsp/har/native模块等多种场景，具体使用可以参考[使用示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-load-module-with-info#使用示例)。
 
在实现模块加载时，推荐优先使用napi_load_module_with_info接口。
