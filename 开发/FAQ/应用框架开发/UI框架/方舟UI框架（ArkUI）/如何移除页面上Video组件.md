# 如何移除页面上Video组件

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-187

问题现象

ForEach刷新UI，数组中的Video组件移除了，但屏幕上还有之前的Video组件占着屏幕。

解决措施

采用规避的方式，在移除Video前调用exitFullscreen()方法退出全屏播放，这样才能正常的移除掉Video组件。

参考链接

Video
