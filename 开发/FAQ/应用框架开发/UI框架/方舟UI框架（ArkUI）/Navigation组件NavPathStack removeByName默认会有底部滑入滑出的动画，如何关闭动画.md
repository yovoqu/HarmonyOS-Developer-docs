# Navigation组件NavPathStack removeByName默认会有底部滑入滑出的动画，如何关闭动画

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-438

开发者可设置NavPathStack上的接口[disableAnimation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#disableanimation11)为true来关闭路由的跳转动画，disableAnimation同时控制removeByName等路由操作的动画开关。示例代码如下：
 
```text
this.pageStack.disableAnimation(true);
```
