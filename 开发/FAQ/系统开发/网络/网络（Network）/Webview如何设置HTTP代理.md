# Webview如何设置HTTP代理

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-93

## Webview如何设置HTTP代理
 


##### 问题现象

如何给Webview设置HTTP代理？
 
 

##### 解决方案

可以使用[connection.setAppHttpProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection#connectionsetapphttpproxy11)方法，设置应用级HTTP代理配置信息，此配置会作用到Web组件里的请求。
