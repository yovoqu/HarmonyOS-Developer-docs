# content_embed_extension.h

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

定义服务端应用OE Extension相关数据结构和操作接口。

**引用文件：** <ContentEmbedKit/content_embed/content_embed_extension.h>

**库：** libcontent_embed_ndk.so

**系统能力：** SystemCapability.ContentEmbed.ObjectEditor

**起始版本：** 24

**相关模块：** [ContentEmbed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed)



##### 汇总



##### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ContentEmbed_Document | ContentEmbed_Document | 声明OE文档结构体类型。封装了被嵌入文档的元数据、内容和存储结构。 |
| ContentEmbed_ExtensionContext | ContentEmbed_ExtensionContext | 声明OE Extension上下文的结构体类型。 |
| ContentEmbed_ExtensionContext* | ContentEmbed_ExtensionContextHandle | 声明OE Extension上下文对象指针类型。 |
| ContentEmbed_ExtensionInstance | ContentEmbed_ExtensionInstance | 声明OE Extension实例的结构体类型。管理扩展的生命周期、回调注册和客户端OE对象关联等核心功能。 |
| ContentEmbed_ExtensionInstance* | ContentEmbed_ExtensionInstanceHandle | 声明OE Extension实例对象指针类型。 |
| ContentEmbed_Object | ContentEmbed_Object | 声明ContentEmbed_Object结构体类型。用于指向OE文档在服务端封装的文档嵌入和编辑的程序对象（简称服务端OE对象）。 |
| ContentEmbed_Object* | ContentEmbed_ObjectHandle | 声明ContentEmbed_Object对象指针类型。 |




##### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetContentEmbedContext(ContentEmbed_ExtensionInstanceHandle ceInstance, ContentEmbed_ExtensionContextHandle *ceContext) | - | 从OE Extension实例中获取其对应的OE Extension上下文对象。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetContext(ContentEmbed_ExtensionContextHandle ceContext, AbilityRuntime_ContextHandle *context) | - | 从OE Extension上下文中获取AbilityRuntime上下文。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetExtensionInstance(AbilityRuntime_ExtensionInstanceHandle baseInstance, ContentEmbed_ExtensionInstanceHandle *ceInstance) | - | 从ExtensionAbility基类实例中获取对应的OE Extension实例。 |
| typedef void (*OH_ContentEmbed_Extension_OnCreateFunc)(ContentEmbed_ExtensionInstanceHandle instance, AbilityBase_Want *want) | OH_ContentEmbed_Extension_OnCreateFunc | OE Extension实例创建时的生命周期函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Extension_RegisterOnCreateFunc注册到OE Extension实例。 |
| typedef void (*OH_ContentEmbed_Extension_OnDestroyFunc)(ContentEmbed_ExtensionInstanceHandle instance) | OH_ContentEmbed_Extension_OnDestroyFunc | OE Extension实例销毁时的生命周期函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Extension_RegisterOnDestroyFunc注册到OE Extension实例。 |
| typedef void (*OH_ContentEmbed_Extension_OnObjectAttachFunc)(ContentEmbed_ExtensionInstanceHandle instance, ContentEmbed_ObjectHandle object) | OH_ContentEmbed_Extension_OnObjectAttachFunc | 当客户端OE对象连接到OE Extension实例时触发此回调函数，用于执行服务端OE对象关联后的初始化操作。 开发者需要实现此函数并通过OH_ContentEmbed_Extension_RegisterOnObjectAttachFunc注册到OE Extension实例。 |
| typedef void (*OH_ContentEmbed_Extension_OnObjectDetachFunc)(ContentEmbed_ExtensionInstanceHandle instance, ContentEmbed_ObjectHandle object) | OH_ContentEmbed_Extension_OnObjectDetachFunc | 当客户端OE对象从OE Extension实例断开连接时触发此回调函数，用于执行服务端OE对象断开连接后的清理操作。 开发者需要实现此函数并通过OH_ContentEmbed_Extension_RegisterOnObjectDetachFunc注册到OE Extension实例。 |
| typedef void (*OH_ContentEmbed_Extension_OnWriteToDataStreamFunc)(ContentEmbed_ObjectHandle object) | OH_ContentEmbed_Extension_OnWriteToDataStreamFunc | 当服务端OE对象写入OE文档数据流时的回调函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Extension_RegisterOnWriteToDataStreamFunc注册到服务端OE对象。 |
| typedef void (*OH_ContentEmbed_Extension_OnGetSnapshotFunc)(ContentEmbed_ObjectHandle object) | OH_ContentEmbed_Extension_OnGetSnapshotFunc | 当客户端OE对象请求获取OE文档快照时的回调函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Extension_RegisterOnGetSnapshotFunc注册到服务端OE对象。 |
| typedef void (*OH_ContentEmbed_Extension_OnDoEditFunc)(ContentEmbed_ObjectHandle object) | OH_ContentEmbed_Extension_OnDoEditFunc | 当客户端OE对象请求编辑OE文档时的回调函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Extension_RegisterOnDoEditFunc注册到服务端OE对象。 |
| typedef void (*OH_ContentEmbed_Extension_OnGetEditStatusFunc)(ContentEmbed_ObjectHandle object, bool *isEditing, bool *isModified) | OH_ContentEmbed_Extension_OnGetEditStatusFunc | 当客户端OE对象请求OE文档编辑状态时的回调函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Extension_RegisterOnGetEditStatusFunc注册到服务端OE对象。 |
| typedef void (*OH_ContentEmbed_Extension_OnGetCapabilityFunc)(ContentEmbed_ObjectHandle object, uint32_t *bitmask) | OH_ContentEmbed_Extension_OnGetCapabilityFunc | 当客户端OE对象查询OE Extension实例支持能力时的回调函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Extension_RegisterOnGetCapabilityFunc注册到服务端OE对象。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnCreateFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnCreateFunc onCreateFunc) | - | 注册OE Extension实例创建时的生命周期函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnDestroyFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnDestroyFunc onDestroyFunc) | - | 注册OE Extension实例销毁时的生命周期函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnObjectAttachFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnObjectAttachFunc onObjectAttachFunc) | - | 注册客户端OE对象连接时的回调函数。 可以通过调用OH_ContentEmbed_Extension_UnRegisterOnObjectAttachFunc取消注册。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_UnRegisterOnObjectAttachFunc(ContentEmbed_ExtensionInstanceHandle instance) | - | 取消注册客户端OE对象连接时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnObjectDetachFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnObjectDetachFunc onObjectDetachFunc) | - | 注册客户端OE对象断开连接时的回调函数。 可以通过调用OH_ContentEmbed_Extension_UnRegisterOnObjectDetachFunc取消注册。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_UnRegisterOnObjectDetachFunc(ContentEmbed_ExtensionInstanceHandle instance) | - | 取消注册客户端OE对象断开连接时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnWriteToDataStreamFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnWriteToDataStreamFunc onWriteToDataStreamFunc) | - | 注册服务端OE对象写入OE文档数据流时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnGetSnapshotFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnGetSnapshotFunc onGetSnapshotFunc) | - | 注册客户端OE对象请求获取OE文档快照时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnDoEditFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnDoEditFunc onDoEditFunc) | - | 注册客户端OE对象请求编辑OE文档时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnGetEditStatusFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnGetEditStatusFunc onGetEditStatusFunc) | - | 注册客户端OE对象请求OE文档编辑状态时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnGetCapabilityFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnGetCapabilityFunc onGetCapabilityFunc) | - | 注册客户端OE对象查询OE Extension实例支持能力时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetContentEmbedDocument(ContentEmbed_ObjectHandle object, ContentEmbed_Document **ceDocument) | - | 获取服务端OE对象关联的OE文档实例。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnUpdate(ContentEmbed_ObjectHandle object) | - | 触发客户端OE对象注册的OE文档更新回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnError(ContentEmbed_ObjectHandle object, ContentEmbed_ErrorCode code) | - | 触发客户端OE对象注册的OE文档错误回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnEditingFinished(ContentEmbed_ObjectHandle object, bool dataModified) | - | 触发客户端OE对象注册的OE文档编辑完成回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnExtensionStopped(ContentEmbed_ExtensionInstanceHandle instance) | - | 触发OE Extension关联的所有客户端OE对象注册的OE Extension停止时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_SetSnapshot(ContentEmbed_ObjectHandle object, OH_PixelmapNative *pixelMap) | - | 设置客户端OE对象关联的OE文档快照图像。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_ContextStartSelfUIAbility(ContentEmbed_ExtensionContextHandle context, AbilityBase_Want *want) | - | 通过OE Extension上下文启动自身的UIAbility。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_ContextStartSelfUIAbilityWithStartOptions(ContentEmbed_ExtensionContextHandle context, AbilityBase_Want *want, AbilityRuntime_StartOptions *options) | - | 使用启动选项启动OE Extension上下文自身的UIAbility。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Extension_ContextTerminateAbility(ContentEmbed_ExtensionContextHandle context) | - | 销毁OE Extension。 |




##### 函数说明



##### OH_ContentEmbed_Extension_GetContentEmbedContext()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetContentEmbedContext(ContentEmbed_ExtensionInstanceHandle ceInstance, ContentEmbed_ExtensionContextHandle *ceContext)
```

**描述**

从OE Extension实例中获取其对应的OE Extension上下文对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle ceInstance | OE Extension实例对象的指针。 |
| ContentEmbed_ExtensionContextHandle *ceContext | 输出参数。调用成功后，该指针指向OE Extension实例的上下文对象。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_GetContext()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetContext(ContentEmbed_ExtensionContextHandle ceContext, AbilityRuntime_ContextHandle *context)
```

**描述**

从OE Extension上下文中获取AbilityRuntime上下文。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionContextHandle ceContext | OE Extension上下文对象的指针。 |
| AbilityRuntime_ContextHandle *context | 输出参数。调用成功后，该指针指向AbilityRuntime_ContextHandle上下文对象。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_GetExtensionInstance()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetExtensionInstance(AbilityRuntime_ExtensionInstanceHandle baseInstance, ContentEmbed_ExtensionInstanceHandle *ceInstance)
```

**描述**

从ExtensionAbility基类实例中获取对应的OE Extension实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| AbilityRuntime_ExtensionInstanceHandle baseInstance | AbilityRuntime_ExtensionInstanceHandle实例。 |
| ContentEmbed_ExtensionInstanceHandle *ceInstance | 输出参数。调用成功后，该指针指向OE Extension实例对象。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_OnCreateFunc()

```text
typedef void (*OH_ContentEmbed_Extension_OnCreateFunc)(ContentEmbed_ExtensionInstanceHandle instance, AbilityBase_Want *want)
```

**描述**

OE Extension实例创建时的生命周期函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Extension_RegisterOnCreateFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_registeroncreatefunc)注册到OE Extension实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | OE Extension实例对象的指针。 |
| AbilityBase_Want *want | AbilityBase_Want实例的指针。 |




##### OH_ContentEmbed_Extension_OnDestroyFunc()

```text
typedef void (*OH_ContentEmbed_Extension_OnDestroyFunc)(ContentEmbed_ExtensionInstanceHandle instance)
```

**描述**

OE Extension实例销毁时的生命周期函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Extension_RegisterOnDestroyFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_registerondestroyfunc)注册到OE Extension实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | OE Extension实例对象的指针。 |




##### OH_ContentEmbed_Extension_OnObjectAttachFunc()

```text
typedef void (*OH_ContentEmbed_Extension_OnObjectAttachFunc)(ContentEmbed_ExtensionInstanceHandle instance, ContentEmbed_ObjectHandle object)
```

**描述**

当客户端OE对象连接到OE Extension实例时触发此回调函数，用于执行服务端OE对象关联后的初始化操作。

开发者需要实现此函数并通过[OH_ContentEmbed_Extension_RegisterOnObjectAttachFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_registeronobjectattachfunc)注册到OE Extension实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | OE Extension实例对象的指针。 |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |




##### OH_ContentEmbed_Extension_OnObjectDetachFunc()

```text
typedef void (*OH_ContentEmbed_Extension_OnObjectDetachFunc)(ContentEmbed_ExtensionInstanceHandle instance, ContentEmbed_ObjectHandle object)
```

**描述**

当客户端OE对象从OE Extension实例断开连接时触发此回调函数，用于执行服务端OE对象断开连接后的清理操作。

开发者需要实现此函数并通过[OH_ContentEmbed_Extension_RegisterOnObjectDetachFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_registeronobjectdetachfunc)注册到OE Extension实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | OE Extension实例对象的指针。 |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |




##### OH_ContentEmbed_Extension_OnWriteToDataStreamFunc()

```text
typedef void (*OH_ContentEmbed_Extension_OnWriteToDataStreamFunc)(ContentEmbed_ObjectHandle object)
```

**描述**

当服务端OE对象写入OE文档数据流时的回调函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Extension_RegisterOnWriteToDataStreamFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_registeronwritetodatastreamfunc)注册到服务端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |




##### OH_ContentEmbed_Extension_OnGetSnapshotFunc()

```text
typedef void (*OH_ContentEmbed_Extension_OnGetSnapshotFunc)(ContentEmbed_ObjectHandle object)
```

**描述**

当客户端OE对象请求获取OE文档快照时的回调函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Extension_RegisterOnGetSnapshotFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_registerongetsnapshotfunc)注册到服务端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |




##### OH_ContentEmbed_Extension_OnDoEditFunc()

```text
typedef void (*OH_ContentEmbed_Extension_OnDoEditFunc)(ContentEmbed_ObjectHandle object)
```

**描述**

当客户端OE对象请求编辑OE文档时的回调函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Extension_RegisterOnDoEditFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_registerondoeditfunc)注册到服务端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |




##### OH_ContentEmbed_Extension_OnGetEditStatusFunc()

```text
typedef void (*OH_ContentEmbed_Extension_OnGetEditStatusFunc)(ContentEmbed_ObjectHandle object, bool *isEditing, bool *isModified)
```

**描述**

当客户端OE对象请求OE文档编辑状态时的回调函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Extension_RegisterOnGetEditStatusFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_registerongeteditstatusfunc)注册到服务端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| bool *isEditing | 输出参数。表示OE文档是否正在编辑，true表示正在编辑；false表示未编辑。 |
| bool *isModified | 输出参数。表示OE文档是否已被修改，true表示已被修改；false表示未修改。 |




##### OH_ContentEmbed_Extension_OnGetCapabilityFunc()

```text
typedef void (*OH_ContentEmbed_Extension_OnGetCapabilityFunc)(ContentEmbed_ObjectHandle object, uint32_t *bitmask)
```

**描述**

当客户端OE对象查询OE Extension实例支持能力时的回调函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Extension_RegisterOnGetCapabilityFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_registerongetcapabilityfunc)注册到服务端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| uint32_t *bitmask | 输出参数，表示OE Extension实例支持的能力，由ContentEmbed_CapabilityCode中的值组合而成。 |




##### OH_ContentEmbed_Extension_RegisterOnCreateFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnCreateFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnCreateFunc onCreateFunc)
```

**描述**

注册OE Extension实例创建时的生命周期函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | 指向OE Extension实例对象的指针。 |
| OH_ContentEmbed_Extension_OnCreateFunc onCreateFunc | 要注册的OH_ContentEmbed_Extension_OnCreateFunc生命周期函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_RegisterOnDestroyFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnDestroyFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnDestroyFunc onDestroyFunc)
```

**描述**

注册OE Extension实例销毁时的生命周期函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | 指向OE Extension实例对象的指针。 |
| OH_ContentEmbed_Extension_OnDestroyFunc onDestroyFunc | 要注册的OH_ContentEmbed_Extension_OnDestroyFunc生命周期函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_RegisterOnObjectAttachFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnObjectAttachFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnObjectAttachFunc onObjectAttachFunc)
```

**描述**

注册客户端OE对象连接时的回调函数。

可以通过调用[OH_ContentEmbed_Extension_UnRegisterOnObjectAttachFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_unregisteronobjectattachfunc)取消注册。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | 指向OE Extension实例对象的指针。 |
| OH_ContentEmbed_Extension_OnObjectAttachFunc onObjectAttachFunc | 要注册的OH_ContentEmbed_Extension_OnObjectAttachFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_UnRegisterOnObjectAttachFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_UnRegisterOnObjectAttachFunc(ContentEmbed_ExtensionInstanceHandle instance)
```

**描述**

取消注册客户端OE对象连接时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | 指向OE Extension实例对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_RegisterOnObjectDetachFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnObjectDetachFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnObjectDetachFunc onObjectDetachFunc)
```

**描述**

注册客户端OE对象断开连接时的回调函数。

可以通过调用[OH_ContentEmbed_Extension_UnRegisterOnObjectDetachFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h#oh_contentembed_extension_unregisteronobjectdetachfunc)取消注册。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | 指向OE Extension实例对象的指针。 |
| OH_ContentEmbed_Extension_OnObjectDetachFunc onObjectDetachFunc | 要注册的OH_ContentEmbed_Extension_OnObjectDetachFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_UnRegisterOnObjectDetachFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_UnRegisterOnObjectDetachFunc(ContentEmbed_ExtensionInstanceHandle instance)
```

**描述**

取消注册客户端OE对象断开连接时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | 指向OE Extension实例对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_RegisterOnWriteToDataStreamFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnWriteToDataStreamFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnWriteToDataStreamFunc onWriteToDataStreamFunc)
```

**描述**

注册服务端OE对象写入OE文档数据流时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| OH_ContentEmbed_Extension_OnWriteToDataStreamFunc onWriteToDataStreamFunc | 要注册的OH_ContentEmbed_Extension_OnWriteToDataStreamFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_RegisterOnGetSnapshotFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnGetSnapshotFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnGetSnapshotFunc onGetSnapshotFunc)
```

**描述**

注册客户端OE对象请求获取OE文档快照时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| OH_ContentEmbed_Extension_OnGetSnapshotFunc onGetSnapshotFunc | 要注册的OH_ContentEmbed_Extension_OnGetSnapshotFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_RegisterOnDoEditFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnDoEditFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnDoEditFunc onDoEditFunc)
```

**描述**

注册客户端OE对象请求编辑OE文档时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| OH_ContentEmbed_Extension_OnDoEditFunc onDoEditFunc | 要注册的OH_ContentEmbed_Extension_OnDoEditFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_RegisterOnGetEditStatusFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnGetEditStatusFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnGetEditStatusFunc onGetEditStatusFunc)
```

**描述**

注册客户端OE对象请求OE文档编辑状态时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| OH_ContentEmbed_Extension_OnGetEditStatusFunc onGetEditStatusFunc | 要注册的OH_ContentEmbed_Extension_OnGetEditStatusFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_RegisterOnGetCapabilityFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnGetCapabilityFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnGetCapabilityFunc onGetCapabilityFunc)
```

**描述**

注册客户端OE对象查询OE Extension实例支持能力时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| OH_ContentEmbed_Extension_OnGetCapabilityFunc onGetCapabilityFunc | 要注册的OH_ContentEmbed_Extension_OnGetCapabilityFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_GetContentEmbedDocument()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetContentEmbedDocument(ContentEmbed_ObjectHandle object, ContentEmbed_Document **ceDocument)
```

**描述**

获取服务端OE对象关联的OE文档实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| ContentEmbed_Document **ceDocument | 输出参数。调用成功后，该指针指向关联的OE文档实例。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_CallbackToOnUpdate()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnUpdate(ContentEmbed_ObjectHandle object)
```

**描述**

触发客户端OE对象注册的OE文档更新回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_CLIENT_CALLBACK_NOT_REGISTERED：表示客户端回调未注册。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_CLIENT_CALLBACK_FAILED：表示客户端回调执行失败。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_CallbackToOnError()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnError(ContentEmbed_ObjectHandle object, ContentEmbed_ErrorCode code)
```

**描述**

触发客户端OE对象注册的OE文档错误回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| ContentEmbed_ErrorCode code | 表示错误码，详细定义参见ContentEmbed_ErrorCode。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_CLIENT_CALLBACK_NOT_REGISTERED：表示客户端回调未注册。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_CLIENT_CALLBACK_FAILED：表示客户端回调执行失败。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_CallbackToOnEditingFinished()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnEditingFinished(ContentEmbed_ObjectHandle object, bool dataModified)
```

**描述**

触发客户端OE对象注册的OE文档编辑完成回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| bool dataModified | 表示文档数据是否已被修改。true表示有修改，false表示无修改。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_CLIENT_CALLBACK_NOT_REGISTERED：表示客户端回调未注册。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_CLIENT_CALLBACK_FAILED：表示客户端回调执行失败。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_CallbackToOnExtensionStopped()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnExtensionStopped(ContentEmbed_ExtensionInstanceHandle instance)
```

**描述**

触发OE Extension关联的所有客户端OE对象注册的OE Extension停止时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionInstanceHandle instance | 指向OE Extension实例对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_CLIENT_CALLBACK_NOT_REGISTERED：表示客户端回调未注册。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_CLIENT_CALLBACK_FAILED：表示客户端回调执行失败。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_SetSnapshot()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_SetSnapshot(ContentEmbed_ObjectHandle object, OH_PixelmapNative *pixelMap)
```

**描述**

设置客户端OE对象关联的OE文档快照图像。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ObjectHandle object | ContentEmbed_ObjectHandle实例。 |
| OH_PixelmapNative *pixelMap | 文档快照的像素图对象，详细信息参考OH_PixelmapNative。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 CE_ERR_IMAGE_PACKER_OPERATION_FAILED：表示图像操作失败。 |




##### OH_ContentEmbed_Extension_ContextStartSelfUIAbility()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_ContextStartSelfUIAbility(ContentEmbed_ExtensionContextHandle context, AbilityBase_Want *want)
```

**描述**

通过OE Extension上下文启动自身的[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability#uiability)。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionContextHandle context | 指向OE Extension上下文对象的指针。 |
| AbilityBase_Want *want | 启动UIAbility时传递的参数，详细信息参考AbilityBase_Want。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_SYSTEM_ABNORMAL：表示系统服务异常。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_ContextStartSelfUIAbilityWithStartOptions()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_ContextStartSelfUIAbilityWithStartOptions(ContentEmbed_ExtensionContextHandle context, AbilityBase_Want *want, AbilityRuntime_StartOptions *options)
```

**描述**

使用启动选项启动OE Extension上下文自身的[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability#uiability)。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionContextHandle context | 指向OE Extension上下文对象的指针。 |
| AbilityBase_Want *want | 启动UIAbility时传递的参数，详细信息参考AbilityBase_Want。 |
| AbilityRuntime_StartOptions *options | 启动UIAbility时的附加选项，详细信息参考AbilityRuntime_StartOptions。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_SYSTEM_ABNORMAL：表示系统服务异常。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Extension_ContextTerminateAbility()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_ContextTerminateAbility(ContentEmbed_ExtensionContextHandle context)
```

**描述**

销毁OE Extension。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionContextHandle context | 指向OE Extension上下文对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_SYSTEM_ABNORMAL：表示系统服务异常。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |
