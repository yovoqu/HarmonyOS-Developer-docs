# 秒级启动后，游戏出现类似UIContent is nullptr报错导致登录等异常，应该如何排查

更新时间：2026-05-08 09:27:50

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-faq-7

![](assets/秒级启动后，游戏出现类似UIContent%20is%20nullptr报错导致登录等异常，应该如何排查/file-20260514131716033-0.png)

 该报错通常是由于游戏在秒级启动后未重新获取并更新[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)，导致后续逻辑仍使用旧的Context对象。当[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability)被重新创建时，如果相关模块或三方SDK继续使用旧的UIAbilityContext，可能会导致接口调用异常、资源访问失败或SDK功能异常。

 排查要点：
