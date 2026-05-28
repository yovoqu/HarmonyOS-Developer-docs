# @ohos.app.ability.FenceExtensionContext (FenceExtensionContext)

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-fenceextensioncontext

FenceExtensionContext是FenceExtensionAbility的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)，提供FenceExtensionAbility的相关配置信息以及启动Ability接口。

> [!NOTE]
> 本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。 本模块接口仅可在Stage模型下使用。



#### 导入模块

```text
import { FenceExtensionContext } from '@kit.LocationKit';
```



#### 使用说明

在使用FenceExtensionContext的功能前，需要通过FenceExtensionAbility获取。

```text
import { FenceExtensionAbility, FenceExtensionContext } from '@kit.LocationKit';

class MyFenceExtensionAbility extends FenceExtensionAbility {
  onCreate() {
    let fenceExtensionContext: FenceExtensionContext = this.context;
  }
}
```
