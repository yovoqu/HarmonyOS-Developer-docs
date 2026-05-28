# content_embed_proxy.h

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-proxy-h
**支持设备：** Phone | PC/2in1 | Tablet

##### 概述

为客户端应用提供服务端应用注册的OE Extension信息查询接口和与服务端OE Extension对象交互的数据结构及相关操作接口。

**引用文件：** <ContentEmbedKit/content_embed/content_embed_proxy.h>

**库：** libcontent_embed_ndk.so

**系统能力：** SystemCapability.ContentEmbed.ObjectEditor

**起始版本：** 24

**相关模块：** [ContentEmbed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed)



##### 汇总



##### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ContentEmbed_Info | ContentEmbed_Info | 声明ContentEmbed_Info结构体类型。包含客户端可获取的ContentEmbed_Format集合信息。 |
| ContentEmbed_Format | ContentEmbed_Format | 声明ContentEmbed_Format结构体类型。包含服务端应用OE Extension注册的OEID、显示名称、描述信息、图标和文件扩展名等信息。 |
| ContentEmbed_ExtensionProxy | ContentEmbed_ExtensionProxy | 声明ContentEmbed_ExtensionProxy结构体类型。用于指向OE文档在客户端封装的文档嵌入和编辑的程序对象（简称客户端OE对象）。 |
| ContentEmbed_Document | ContentEmbed_Document | 声明OE文档结构体类型。封装了被嵌入的文档的元数据、内容和存储结构。 |
| ContentEmbed_Capability | ContentEmbed_Capability | 声明ContentEmbed_Capability结构体类型。 |




##### 宏定义

| 名称 | 描述 |
| --- | --- |
| MAX_NAME_LENGTH (1 * 1024) | 定义ContentEmbed_Format中名称字段的最大字符数限制。 起始版本： 24 |
| MAX_DESCRIPTION_LENGTH (1 * 1024) | 定义ContentEmbed_Format中描述字段的最大字符数限制。 起始版本： 24 |




##### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ContentEmbed_ErrorCode OH_ContentEmbed_CreateContentEmbedInfo(ContentEmbed_Info **info) | - | 创建ContentEmbed_Info实例。 开发者可通过OH_ContentEmbed_DestroyContentEmbedInfo销毁实例，以避免内存泄漏。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_DestroyContentEmbedInfo(ContentEmbed_Info *info) | - | 销毁ContentEmbed_Info实例。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_GetContentEmbedInfo(const char *locale, ContentEmbed_Info *info) | - | 根据区域设置获取ContentEmbed_Info实例。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_GetFormatCountFromInfo(const ContentEmbed_Info *info, uint32_t *count) | - | 获取ContentEmbed_Info实例中的ContentEmbed_Format实例的数量。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_GetFormatFromInfo(const ContentEmbed_Info *info, uint32_t index, ContentEmbed_Format **format) | - | 从ContentEmbed_Info实例中获取指定索引位置的ContentEmbed_Format实例。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_CreateContentEmbedFormat(ContentEmbed_Format **format) | - | 创建ContentEmbed_Format实例。 开发者可通过OH_ContentEmbed_DestroyContentEmbedFormat销毁实例，以避免内存泄漏。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_DestroyContentEmbedFormat(ContentEmbed_Format *format) | - | 销毁ContentEmbed_Format实例。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_GetContentEmbedFormatByOEidAndLocale(const char *oeid, const char *locale, ContentEmbed_Format *format) | - | 根据OEID和区域设置获取ContentEmbed_Format实例。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_GetOEidFromFormat(const ContentEmbed_Format *format, char *oeid) | - | 获取ContentEmbed_Format实例的OEID。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_GetNameAndDescriptionFromFormat(const ContentEmbed_Format *format, char *name, char *description) | - | 从ContentEmbed_Format实例中获取其本地化的显示名称和描述信息。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_GetIconFromFormat(const ContentEmbed_Format *format, OH_PixelmapNative **icon) | - | 获取ContentEmbed_Format实例的图标。 |
| char** OH_ContentEmbed_GetFileNameExtensionsFromFormat(const ContentEmbed_Format *format, unsigned int *count) | - | 获取ContentEmbed_Format实例的文件扩展名列表。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_CreateExtensionProxy(ContentEmbed_Document *document, ContentEmbed_ExtensionProxy **proxy, void *contextPtr) | - | 创建ContentEmbed_ExtensionProxy实例。 开发者可通过OH_ContentEmbed_DestroyExtensionProxy销毁实例，以避免内存泄漏。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_DestroyExtensionProxy(ContentEmbed_ExtensionProxy *proxy) | - | 销毁ContentEmbed_ExtensionProxy实例。 |
| typedef void (*OH_ContentEmbed_ClientCallbackOnUpdateFunc)(ContentEmbed_ExtensionProxy *proxy) | OH_ContentEmbed_ClientCallbackOnUpdateFunc | OE文档更新时通知客户端的回调函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Proxy_RegisterOnUpdateFunc将此函数注册到客户端OE对象。 |
| typedef void (*OH_ContentEmbed_ClientCallbackOnErrorFunc)(ContentEmbed_ExtensionProxy *proxy, ContentEmbed_ErrorCode error) | OH_ContentEmbed_ClientCallbackOnErrorFunc | OE文档错误时通知客户端的回调函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Proxy_RegisterOnErrorFunc将此函数注册到客户端OE对象。 |
| typedef void (*OH_ContentEmbed_ClientCallbackOnEditingFinishedFunc)(ContentEmbed_ExtensionProxy *proxy, bool dataModified) | OH_ContentEmbed_ClientCallbackOnEditingFinishedFunc | OE文档编辑完成时通知客户端的回调函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Proxy_RegisterOnEditingFinishedFunc将此函数注册到客户端OE对象。 |
| typedef void (*OH_ContentEmbed_ClientCallbackOnExtensionStoppedFunc)(ContentEmbed_ExtensionProxy *proxy) | OH_ContentEmbed_ClientCallbackOnExtensionStoppedFunc | OE Extension停止时回调函数类型。 开发者需要实现此函数并通过OH_ContentEmbed_Proxy_RegisterOnExtensionStoppedFunc将此函数注册到客户端OE对象。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnUpdateFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnUpdateFunc onUpdateFunc) | - | 向客户端OE对象注册OE文档更新时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnErrorFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnErrorFunc onErrorFunc) | - | 向客户端OE对象注册OE文档触发错误时回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnEditingFinishedFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnEditingFinishedFunc onEditingFinishedFunc) | - | 向客户端OE对象注册OE文档编辑完成时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnExtensionStoppedFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnExtensionStoppedFunc onExtensionStoppedFunc) | - | 向客户端OE对象注册OE Extension停止时的回调函数。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_StartWork(ContentEmbed_ExtensionProxy *proxy) | - | 连接服务端OE Extension，建立与OE Extension的通信通道。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_StopWork(ContentEmbed_ExtensionProxy *proxy) | - | 断开与OE Extension的通信通道。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetSnapshot(ContentEmbed_ExtensionProxy *proxy, OH_PixelmapNative **snapshot) | - | 从客户端OE对象获取当前OE文档的快照图像，用于预览或缩略图显示。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_DoEdit(ContentEmbed_ExtensionProxy *proxy) | - | 客户端OE对象请求OE Extension实例进入编辑模式。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetEditStatus(ContentEmbed_ExtensionProxy *proxy, bool *isEditing, bool *isModified) | - | 查询服务端OE Extension实例对OE文档的当前编辑状态和修改状态。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetCapability(ContentEmbed_ExtensionProxy *proxy, uint32_t *bitmask) | - | 获取服务端OE Extension实例拥有的能力，以位掩码形式返回，各位的含义参见ContentEmbed_CapabilityCode。 |
| ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetDocument(ContentEmbed_ExtensionProxy *proxy, ContentEmbed_Document **ceDocument) | - | 从客户端OE对象获取其关联的OE文档对象。 该OE文档对象通过OH_ContentEmbed_CreateDocumentByOEid、OH_ContentEmbed_CreateDocumentByFile或OH_ContentEmbed_LoadDocumentFromFile方式创建。 当该OE文档不再需要时，应调用OH_ContentEmbed_DestroyDocument将其销毁。 |




##### 函数说明



##### OH_ContentEmbed_CreateContentEmbedInfo()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_CreateContentEmbedInfo(ContentEmbed_Info **info)
```

**描述**

创建[ContentEmbed_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-info)实例。

开发者可通过[OH_ContentEmbed_DestroyContentEmbedInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-proxy-h#oh_contentembed_destroycontentembedinfo)销毁实例，以避免内存泄漏。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_Info **info | 输出参数。该指针指向新创建的ContentEmbed_Info对象。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_DestroyContentEmbedInfo()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_DestroyContentEmbedInfo(ContentEmbed_Info *info)
```

**描述**

销毁[ContentEmbed_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-info)实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_Info *info | 指向ContentEmbed_Info对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_GetContentEmbedInfo()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_GetContentEmbedInfo(const char *locale, ContentEmbed_Info *info)
```

**描述**

根据区域设置获取[ContentEmbed_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-info)实例。

**需要权限：** ohos.permission.CONNECT_OBJECTEDITOR_EXTENSION

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char *locale | 表示区域ID的字符串，由语言、脚本、国家地区组成，例如"zh-Hans-CN"。当locale为空时，默认使用系统区域设置。 |
| ContentEmbed_Info *info | 输出参数。该指针指向ContentEmbed_Info对象。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_PERMISSION_DENIED：表示权限校验失败。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_SYSTEM_ABNORMAL：表示系统服务工作异常。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_GetFormatCountFromInfo()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_GetFormatCountFromInfo(const ContentEmbed_Info *info, uint32_t *count)
```

**描述**

获取[ContentEmbed_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-info)实例中的[ContentEmbed_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-format)实例的数量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ContentEmbed_Info *info | 指向ContentEmbed_Info对象指针。 |
| uint32_t *count | 输出参数。存储ContentEmbed_Format实例的数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_GetFormatFromInfo()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_GetFormatFromInfo(const ContentEmbed_Info *info, uint32_t index, ContentEmbed_Format **format)
```

**描述**

从[ContentEmbed_Info](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-info)实例中获取指定索引位置的[ContentEmbed_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-format)实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ContentEmbed_Info *info | 指向ContentEmbed_Info对象指针。 |
| uint32_t index | 要获取的格式的索引，从0开始。 |
| ContentEmbed_Format **format | 输出参数。该指针指向ContentEmbed_Format对象。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_CreateContentEmbedFormat()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_CreateContentEmbedFormat(ContentEmbed_Format **format)
```

**描述**

创建[ContentEmbed_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-format)实例。

开发者可通过[OH_ContentEmbed_DestroyContentEmbedFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-proxy-h#oh_contentembed_destroycontentembedformat)销毁实例，以避免内存泄漏。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_Format **format | 输出参数。该指针指向新创建的ContentEmbed_Format对象。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_DestroyContentEmbedFormat()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_DestroyContentEmbedFormat(ContentEmbed_Format *format)
```

**描述**

销毁[ContentEmbed_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-format)实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_Format *format | 指向ContentEmbed_Format对象指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_GetContentEmbedFormatByOEidAndLocale()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_GetContentEmbedFormatByOEidAndLocale(const char *oeid, const char *locale, ContentEmbed_Format *format)
```

**描述**

根据OEID和区域设置获取[ContentEmbed_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-format)实例。

**需要权限：** ohos.permission.CONNECT_OBJECTEDITOR_EXTENSION

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char *oeid | 文档格式的唯一标识符字符串。 |
| const char *locale | 表示区域ID的字符串，由语言、脚本、国家地区组成，例如"zh-Hans-CN"。当locale为空时，默认使用系统区域设置。 |
| ContentEmbed_Format *format | 输出参数。该指针指向ContentEmbed_Format对象。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_PERMISSION_DENIED：表示权限校验失败。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_SYSTEM_ABNORMAL：表示系统服务工作异常。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_GetOEidFromFormat()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_GetOEidFromFormat(const ContentEmbed_Format *format, char *oeid)
```

**描述**

获取[ContentEmbed_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-format)实例的OEID。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ContentEmbed_Format *format | 指向ContentEmbed_Format对象指针。 |
| char *oeid | 输出参数。用于存储标识符OEID字符串的字符数组。建议数组长度为MAX_OEID_LENGTH。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_GetNameAndDescriptionFromFormat()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_GetNameAndDescriptionFromFormat(const ContentEmbed_Format *format, char *name, char *description)
```

**描述**

从[ContentEmbed_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-format)实例中获取其本地化的显示名称和描述信息。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ContentEmbed_Format *format | 指向ContentEmbed_Format对象指针。 |
| char *name | 输出参数。用于存储名称的字符数组。建议数组长度为MAX_NAME_LENGTH。 |
| char *description | 输出参数。用于存储描述信息的字符数组。建议数组长度为MAX_DESCRIPTION_LENGTH。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_GetIconFromFormat()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_GetIconFromFormat(const ContentEmbed_Format *format, OH_PixelmapNative **icon)
```

**描述**

获取[ContentEmbed_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-format)实例的图标。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ContentEmbed_Format *format | 指向ContentEmbed_Format对象指针。 |
| OH_PixelmapNative **icon | 输出参数。用于存储图标的OH_PixelmapNative实例指针。 开发者需要调用OH_PixelmapNative_Destroy销毁，以避免内存泄漏。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 |




##### OH_ContentEmbed_GetFileNameExtensionsFromFormat()

```text
char** OH_ContentEmbed_GetFileNameExtensionsFromFormat(const ContentEmbed_Format *format, unsigned int *count)
```

**描述**

获取[ContentEmbed_Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-format)实例的文件扩展名列表。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const ContentEmbed_Format *format | 指向ContentEmbed_Format对象指针。 |
| unsigned int *count | 输出参数。存储返回的文件扩展名数量。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| char** | 返回文件扩展名字符串数组的指针。 |




##### OH_ContentEmbed_CreateExtensionProxy()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_CreateExtensionProxy(ContentEmbed_Document *document, ContentEmbed_ExtensionProxy **proxy, void *contextPtr)
```

**描述**

创建[ContentEmbed_ExtensionProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-extensionproxy)实例。

开发者可通过[OH_ContentEmbed_DestroyExtensionProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-proxy-h#oh_contentembed_destroyextensionproxy)销毁实例，以避免内存泄漏。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_Document *document | 指向OE文档实例的指针。 |
| ContentEmbed_ExtensionProxy **proxy | 输出参数。该指针指向新创建的ContentEmbed_ExtensionProxy对象。 |
| void *contextPtr | 上下文实例的指针，用于传递应用上下文信息。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_DestroyExtensionProxy()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_DestroyExtensionProxy(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

销毁[ContentEmbed_ExtensionProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-contentembed-contentembed-extensionproxy)实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_ClientCallbackOnUpdateFunc()

```text
typedef void (*OH_ContentEmbed_ClientCallbackOnUpdateFunc)(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

OE文档更新时通知客户端的回调函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Proxy_RegisterOnUpdateFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-proxy-h#oh_contentembed_proxy_registeronupdatefunc)将此函数注册到客户端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |




##### OH_ContentEmbed_ClientCallbackOnErrorFunc()

```text
typedef void (*OH_ContentEmbed_ClientCallbackOnErrorFunc)(ContentEmbed_ExtensionProxy *proxy, ContentEmbed_ErrorCode error)
```

**描述**

OE文档错误时通知客户端的回调函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Proxy_RegisterOnErrorFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-proxy-h#oh_contentembed_proxy_registeronerrorfunc)将此函数注册到客户端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |
| ContentEmbed_ErrorCode error | 表示发生的错误码，详细定义参见ContentEmbed_ErrorCode。 |




##### OH_ContentEmbed_ClientCallbackOnEditingFinishedFunc()

```text
typedef void (*OH_ContentEmbed_ClientCallbackOnEditingFinishedFunc)(ContentEmbed_ExtensionProxy *proxy, bool dataModified)
```

**描述**

OE文档编辑完成时通知客户端的回调函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Proxy_RegisterOnEditingFinishedFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-proxy-h#oh_contentembed_proxy_registeroneditingfinishedfunc)将此函数注册到客户端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |
| bool dataModified | 表示OE文档数据是否被修改。true表示OE文档已修改；false表示未修改。 |




##### OH_ContentEmbed_ClientCallbackOnExtensionStoppedFunc()

```text
typedef void (*OH_ContentEmbed_ClientCallbackOnExtensionStoppedFunc)(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

OE Extension停止时回调函数类型。

开发者需要实现此函数并通过[OH_ContentEmbed_Proxy_RegisterOnExtensionStoppedFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-proxy-h#oh_contentembed_proxy_registeronextensionstoppedfunc)将此函数注册到客户端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |




##### OH_ContentEmbed_Proxy_RegisterOnUpdateFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnUpdateFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnUpdateFunc onUpdateFunc)
```

**描述**

向客户端OE对象注册OE文档更新时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |
| OH_ContentEmbed_ClientCallbackOnUpdateFunc onUpdateFunc | 要注册的OH_ContentEmbed_ClientCallbackOnUpdateFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Proxy_RegisterOnErrorFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnErrorFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnErrorFunc onErrorFunc)
```

**描述**

向客户端OE对象注册OE文档触发错误时回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |
| OH_ContentEmbed_ClientCallbackOnErrorFunc onErrorFunc | 要注册的OH_ContentEmbed_ClientCallbackOnErrorFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Proxy_RegisterOnEditingFinishedFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnEditingFinishedFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnEditingFinishedFunc onEditingFinishedFunc)
```

**描述**

向客户端OE对象注册OE文档编辑完成时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |
| OH_ContentEmbed_ClientCallbackOnEditingFinishedFunc onEditingFinishedFunc | 要注册的OH_ContentEmbed_ClientCallbackOnEditingFinishedFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Proxy_RegisterOnExtensionStoppedFunc()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnExtensionStoppedFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnExtensionStoppedFunc onExtensionStoppedFunc)
```

**描述**

向客户端OE对象注册OE Extension停止时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |
| OH_ContentEmbed_ClientCallbackOnExtensionStoppedFunc onExtensionStoppedFunc | 要注册的OH_ContentEmbed_ClientCallbackOnExtensionStoppedFunc回调函数。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Proxy_StartWork()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_StartWork(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

连接服务端OE Extension，建立与OE Extension的通信通道。

**需要权限：** ohos.permission.CONNECT_OBJECTEDITOR_EXTENSION

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_PERMISSION_DENIED：表示权限校验失败。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_CLIENT_CALLBACK_NOT_REGISTERED：表示必要的客户端回调未注册。 CE_ERR_SYSTEM_ABNORMAL：表示系统服务异常。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 CE_ERR_CONNECT_LIMIT_EXCEED：表示OE Extension连接数超出限制。 CE_ERR_FILE_NOT_GRANT：表示文件未被授权。 CE_ERR_DISK_FULL：表示磁盘已满。 |




##### OH_ContentEmbed_Proxy_StopWork()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_StopWork(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

断开与OE Extension的通信通道。

**需要权限：** ohos.permission.CONNECT_OBJECTEDITOR_EXTENSION

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_PERMISSION_DENIED：表示权限校验失败。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_SYSTEM_ABNORMAL：表示系统服务异常。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Proxy_GetSnapshot()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetSnapshot(ContentEmbed_ExtensionProxy *proxy, OH_PixelmapNative **snapshot)
```

**描述**

从客户端OE对象获取当前OE文档的快照图像，用于预览或缩略图显示。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |
| OH_PixelmapNative **snapshot | 输出参数。用于存储文档快照的OH_PixelmapNative实例指针。 开发者需要调用OH_PixelmapNative_Destroy销毁，以避免内存泄漏。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_NULL_POINTER：表示返回空指针。 CE_ERR_EXTENSION_ERROR：表示OE Extension发生错误。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 CE_ERR_EXTENSION_NOT_SUPPORT：表示OE Extension不支持该能力。 |




##### OH_ContentEmbed_Proxy_DoEdit()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_DoEdit(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

客户端OE对象请求OE Extension实例进入编辑模式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_EXTENSION_ERROR：表示OE Extension发生错误。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 CE_ERR_EXTENSION_NOT_SUPPORT：表示OE Extension不支持该能力。 |




##### OH_ContentEmbed_Proxy_GetEditStatus()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetEditStatus(ContentEmbed_ExtensionProxy *proxy, bool *isEditing, bool *isModified)
```

**描述**

查询服务端OE Extension实例对OE文档的当前编辑状态和修改状态。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |
| bool *isEditing | 输出参数。表示内容嵌入文档是否正在编辑。true表示正在编辑；false表示未在编辑。 |
| bool *isModified | 输出参数。表示内容嵌入文档是否已被修改。true表示已修改；false表示未修改。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_EXTENSION_ERROR：表示OE Extension发生错误。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Proxy_GetCapability()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetCapability(ContentEmbed_ExtensionProxy *proxy, uint32_t *bitmask)
```

**描述**

获取服务端OE Extension实例拥有的能力，以位掩码形式返回，各位的含义参见[ContentEmbed_CapabilityCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-common-h#contentembed_capabilitycode)。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |
| uint32_t *bitmask | 输出参数。表示服务端OE Extension实例拥有的能力，由ContentEmbed_CapabilityCode中的值组合而成。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_EXTENSION_ERROR：表示OE Extension发生错误。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |




##### OH_ContentEmbed_Proxy_GetDocument()

```text
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetDocument(ContentEmbed_ExtensionProxy *proxy, ContentEmbed_Document **ceDocument)
```

**描述**

从客户端OE对象获取其关联的OE文档对象。

该OE文档对象通过[OH_ContentEmbed_CreateDocumentByOEid](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-document-h#oh_contentembed_createdocumentbyoeid)、[OH_ContentEmbed_CreateDocumentByFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-document-h#oh_contentembed_createdocumentbyfile)或[OH_ContentEmbed_LoadDocumentFromFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-document-h#oh_contentembed_loaddocumentfromfile)方式创建。

当该OE文档不再需要时，应调用[OH_ContentEmbed_DestroyDocument](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-document-h#oh_contentembed_destroydocument)将其销毁。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| ContentEmbed_ExtensionProxy *proxy | 指向ContentEmbed_ExtensionProxy对象的指针。 |
| ContentEmbed_Document **ceDocument | 输出参数。用于存储OE文档实例的指针。 |


**返回：**

| 类型 | 说明 |
| --- | --- |
| ContentEmbed_ErrorCode | 返回特定的错误码： CE_ERR_OK：表示操作成功。 CE_ERR_PARAM_INVALID：表示参数检查失败。 CE_ERR_DEVICE_NOT_SUPPORTED：表示设备不支持。 CE_ERR_IN_DLP_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |
