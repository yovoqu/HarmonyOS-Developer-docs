# Native侧如何合理管控对象的生命周期

更新时间：2026-03-17 00:56:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-80

**解决措施**
 
在进行Node-API调用时，引擎堆中的对象的句柄（handle）会作为napi_value返回，这些句柄控制对象的生命周期。对象句柄与一个scope相关联，默认scope的生命周期与native方法调用的生命周期一致。因此，这些句柄关联的对象在native方法调用期间保持存活状态。
 
许多情况下，句柄必须在比native方法更短或更长的生命周期内保持有效。下面描述如何管理对象的生命周期。
 1. 缩短napi_value对象的生命周期——使句柄的生命周期比native方法的调用生命周期更短。例如：

  考虑使用for循环遍历大型数组。此方法会创建大量句柄，消耗较多资源。

  为了处理这种情况，Node-API提供了建立新scope的能力，新创建的句柄（handle）将与该scope关联。不再需要这些句柄时，可以关闭scope，与scope关联的句柄将失效。打开/关闭scope的方法有 napi_open_handle_scope 和 napi_close_handle_scope。

  Node-API中，scope的层次结构是嵌套的。任何时候只有一个活动scope，所有新句柄都会在该作用域处于活动状态时与之关联。scope必须按相反顺序关闭，在native方法中创建的所有scope必须在该方法返回前关闭。

  关于句柄的相关代码使用可参考：[生命周期管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-guidelines#生命周期管理)

  在嵌套作用域时，来自内部作用域的句柄有时需要超出该作用域的寿命。为了支持这种情况，Node-API支持"escapable scope"，允许一个句柄提升（promoted），以便它逃离当前作用域，将句柄的寿命从当前作用域更改为外部作用域。用于打开/关闭"escapable scope"的方法有napi_open_escapable_handle_scope和napi_close_escapable_handle_scope。

  提升句柄的请求是通过只能调用一次的napi_escape_handle发出的。
2. 延长napi_value对象的生命周期——在native方法外创建和引用napi_value对象。Node-API提供了创建对象持久引用的方法，适用于多线程的开发场景。普通句柄（handle）的生命周期由作用域管理，作用域在 native 侧函数结束前关闭。每个引用都有一个计数，计数大于等于 0。计数为 0 的引用会被收集，称为“弱”引用；计数大于 0 的引用不会被收集。

  例如：创建构造器后，若需在使用时创建实例，应为该构造器创建引用。

  napi_ref：指向napi_value，允许用户管理napi_value值的生命周期。

  napi_create_reference(napi_env env, napi_value value, uint32_t initial_refcount, napi_ref* result); 为napi_value对象创建一个引用，以延长其生命周期。调用者需要自己管理引用的生命周期。

  napi_delete_reference(napi_env env, napi_ref ref); 删除传入的引用。

  napi_reference_ref(napi_env env, napi_ref ref, uint32_t *result); 增加传入的引用的引用计数，并获取新的计数。

  napi_reference_unref(napi_env env, napi_ref ref, uint32_t *result); 减少传入的引用的引用计数，并获取新的计数。

  napi_get_reference_value(napi_env env, napi_ref ref, napi_value *result); 获取与引用相关联的napi_value对象。

  关于引用相关接口的使用可以参考：[使用callback方式示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-asynchronous-task#使用callback方式示例)
