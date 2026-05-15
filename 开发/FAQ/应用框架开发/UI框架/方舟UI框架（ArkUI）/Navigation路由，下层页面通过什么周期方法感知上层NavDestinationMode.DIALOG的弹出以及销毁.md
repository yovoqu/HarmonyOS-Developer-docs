# Navigation路由，下层页面通过什么周期方法感知上层NavDestinationMode.DIALOG的弹出以及销毁

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-407

开发者可以使用observer对navDestination的生命周期进行统一管理，可参考：on('navDestinationUpdate')。

从API17开始，新增onActive、onInactive生命周期，dialog销毁、弹出时会分别触发下层页面的onActive、onInactive生命周期。
