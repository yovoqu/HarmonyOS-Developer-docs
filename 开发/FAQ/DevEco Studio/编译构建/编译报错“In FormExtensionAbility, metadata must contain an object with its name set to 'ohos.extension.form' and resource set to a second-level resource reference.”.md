# 编译报错“In FormExtensionAbility, metadata must contain an object with its name set to 'ohos.extension.form' and resource set to a second-level resource reference.”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-165

**错误描述**
 
在FormExtensionAbility中，metadata必须包含一个对象，名称设置为“ohos.extension.form”，资源设置为二级资源引用。
 
**可能原因**
 
module.json5中type为form的ExtensionAbility中的metadata缺少name为ohos.extension.form的对象值，或者缺少resource字段。
 

![](assets/编译报错“In%20FormExtensionAbility,%20metadata%20must%20contain%20an%20object%20with%20its%20name%20set%20to%20'ohos.extension.form'%20and%20resource%20set%20to%20a%20second-level%20resource%20reference.”/file-20260515130208717-0.png)

 
**解决措施**
 
在module.json5中type为form的ExtensionAbility中增加metadata字段，补充一个name为“ohos.extension.form”的对象值，并配置对应的resource值，具体配置方式参考[配置ArkTS卡片的配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-configuration)。
