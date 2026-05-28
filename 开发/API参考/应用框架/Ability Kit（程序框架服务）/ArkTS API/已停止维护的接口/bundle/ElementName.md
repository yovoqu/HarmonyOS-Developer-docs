# ElementName

更新时间：2026-03-23 08:10:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-elementname
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

ElementName信息，通过接口[Context.getElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context#contextgetelementname7)获取。
 
> [!NOTE]
> 本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 从API version 9开始，该模块不再维护，建议使用 bundleManager-ElementName 替代。

  

##### ElementName(deprecated)

> [!NOTE]
> 从API version 7开始支持，从API version 9开始废弃，建议使用 bundleManager-ElementName 替代。

 
ElementName信息，标识Ability的基本信息，通过接口[Context.getElementName](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context#contextgetelementname7)获取。
 
**系统能力：** SystemCapability.BundleManager.BundleFramework
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 是 | 设备id值。 |
| bundleName | string | 否 | 否 | 应用Bundle的名称。 |
| abilityName | string | 否 | 否 | Ability的名称。 |
| uri | string | 否 | 是 | 资源标识符。 |
| shortName | string | 否 | 是 | Ability的短名称。 |
