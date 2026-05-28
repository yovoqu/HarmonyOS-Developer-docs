# 如何解决Web组件加载的HTML页面内检测网络状态失败

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-8

**问题现象**
 
在HTML页面中，使用window.navigator.onLine获取网络状态，在联网/断网情况下返回值均为false。
 
**解决措施**
 
配置应用以获取网络信息权限：ohos.permission.GET_NETWORK_INFO
 
**参考链接**
 
[ohos.permission.GET_NETWORK_INFO](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissionget_network_info)
