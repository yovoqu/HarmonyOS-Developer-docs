# 在使用UIAbilityContext时报401“The context must be a valid Context”的Context类型错误

更新时间：2026-03-25 01:58:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-76

401错误表示提供的上下文类型不正确，需要使用UIAbility的上下文。获取UIAbilityContext的方式如下：

```ts
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let uiAbilityContext = this.context;
    // ...
  }
}
```

参考链接

应用上下文Context
