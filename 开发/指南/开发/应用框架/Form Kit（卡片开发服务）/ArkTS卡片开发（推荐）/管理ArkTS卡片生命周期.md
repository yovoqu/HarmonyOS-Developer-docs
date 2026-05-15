# 管理ArkTS卡片生命周期

更新时间：2026-04-17 08:12:20

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-lifecycle

创建ArkTS卡片，需实现[FormExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability)生命周期接口。


> [!NOTE]
> FormExtensionAbility进程不能常驻后台，即在卡片生命周期回调函数中无法处理长时间的任务，在生命周期调度完成后会继续存在10秒，若在10秒内未收到新的生命周期回调，则进程将自动退出。针对可能需要10秒以上才能完成的业务逻辑，建议拉起主应用进行处理，处理完成后使用updateForm通知卡片进行刷新。
