# 显式Want跳转切换应用链接跳转适配指导

更新时间：2026-05-26 06:48:54

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-startup-adjust

从API 12开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用，推荐通过指定[应用链接](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup-overview#应用链接)的方式来实现。

本章节介绍如何从显式Want跳转切换到应用链接跳转。

> [!NOTE]
> 暂不支持显式Want中flag字段的转换。如需使用flag字段，建议仍采用显式Want跳转的方式。



#### 启动其他应用的UIAbility
1. 将待跳转的应用安装到设备，在其对应UIAbility的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中配置skills标签的entities字段、actions字段和uri字段：

  
"actions"列表中包含"ohos.want.action.viewData"。
2. "entities"列表中包含"entity.system.browsable"。
3. "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。uri的匹配规则参考[uri匹配](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/explicit-implicit-want-mappings#uri匹配规则)，domainVerify为true代表开启域名检查，通过App Linking匹配该应用时需经过配置的域名校验后才能匹配到。
4. 调用方通过[openLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12)接口执行跳转，需要传入link和[options](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-openlinkoptions)，不再需要传入bundleName、moduleName和abilityName。系统会根据传入的link匹配到符合skills配置的应用。

  
当options中的appLinkingOnly为true时，匹配到的应用会经过应用市场域名检查（需联网）返回域名校验检查的唯一匹配项或未匹配结果。
5. 当options中的appLinkingOnly为false时，会优先尝试以App Linking的方式拉起，如果没有匹配的应用则跳转默认浏览器打开网页。



#### 启动其他应用的UIAbility并获取返回结果
1. 将待跳转的应用安装到设备，在其对应UIAbility的[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)中配置skills标签的entities字段、actions字段和uri字段：

  
"actions"列表中包含"ohos.want.action.viewData"。
2. "entities"列表中包含"entity.system.browsable"。
3. "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。uri的匹配规则参考[uri匹配](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/explicit-implicit-want-mappings#uri匹配规则)，domainVerify为true代表开启域名检查，通过App Linking匹配该应用时需经过配置的域名校验后才能匹配到。
4. 调用方通过[openLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#openlink12)接口执行跳转，需要传入link和[options](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-openlinkoptions)，不再需要传入bundleName、moduleName和abilityName。系统会根据传入的link匹配到符合skills配置的应用。AbilityResult回调结果通过入参传入回调函数，在被启动的UIAbility停止自身后返回给调用方。启动成功和失败结果仍通过Promise返回。

  
当options中的appLinkingOnly为true时，匹配到的应用会经过应用市场域名检查（需联网）返回域名校验检查的唯一匹配项或未匹配结果。
5. 当options中的appLinkingOnly为false时，会优先尝试以App Linking的方式拉起，如果没有匹配的应用则跳转默认浏览器打开网页。
