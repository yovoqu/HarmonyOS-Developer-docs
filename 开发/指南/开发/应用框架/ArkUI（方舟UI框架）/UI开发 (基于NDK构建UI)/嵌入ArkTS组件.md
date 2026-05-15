# 嵌入ArkTS组件

更新时间：2026-04-30 02:41:24

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-embed-arkts-components

ArkUI在Native侧提供的能力作为ArkTS的子集，部分能力不会在Native侧提供，如声明式UI语法，自定义struct组件，UI高级组件。

针对需要使用ArkTS侧独立能力的场景，ArkUI开发框架提供了Native侧嵌入ArkTS组件的能力，该能力依赖[ComponentContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent)机制，通过ComponentContent完成对ArkTS组件的封装，然后将封装对象传递到Native侧，通过Native侧的[OH_ArkUI_GetNodeHandleFromNapiValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-napi-h#oh_arkui_getnodehandlefromnapivalue)接口转化为ArkUI_NodeHandle对象用于Native侧组件挂载使用。


> [!NOTE]
> 通过OH_ArkUI_GetNodeHandleFromNapiValue接口获得的ArkUI_NodeHandle对象只能作为子组件参数使用，如addChild接口的第二个参数，将该对象使用在其他场景下，如setAttribute设置属性将不生效并返回错误码。 针对Native侧修改ArkTS组件的场景，需要在Native侧通过Node-API方式构建ArkTS侧的更新数据，再通过ComponentContent的update接口更新。 构建自定义组件时，相关函数如measureNode等无法对ArkTS模块内部的组件进行调用。

以下示例代码在[接入ArkTS页面](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page)章节基础上引入ArkTS的Refresh组件。

**图1** Refresh组件挂载文本列表

![](assets/嵌入ArkTS组件/file-20260514130732765-0.gif)
