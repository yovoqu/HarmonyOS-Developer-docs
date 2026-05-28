# 编译报错“The metadata field in FormExtensionAbility cannot be left blank or as an empty array”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-164

**错误描述**
 
FormExtensionAbility中的metadata字段必须非空且不为数组。
 
**可能原因**
 
在module.json5文件中，当ExtensionAbility的type为form时，metadata字段可以是空对象或空数组。
 

![](assets/编译报错“The%20metadata%20field%20in%20FormExtensionAbility%20cannot%20be%20left%20blank%20or%20as%20an%20empty%20array”/file-20260515130208101-0.png)

 
**解决措施**
 
在module.json5中type为form的ExtensionAbility中配置metadata字段，具体配置方式参考[配置ArkTS卡片的配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-configuration)。
