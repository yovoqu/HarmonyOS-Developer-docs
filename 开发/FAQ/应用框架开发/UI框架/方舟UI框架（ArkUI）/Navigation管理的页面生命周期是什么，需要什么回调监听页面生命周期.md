# Navigation管理的页面生命周期是什么，需要什么回调监听页面生命周期

更新时间：2026-04-27 09:10:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-403

Navigation组件作为路由容器的实现，其生命周期承载在NavDestination组件上，以组件事件的形式开放。Navigation管理的页面生命周期包括onAppear（通用生命周期事件）、onShown（NavDestination组件布局显示之后执行）、onActive（NavDestination处于激活态触发）等等，具体可参考下方文档。可以通过Class (UIObserver)监听NavDestination组件的生命周期。

参考链接

组件导航(Navigation) (推荐)

页面生命周期
