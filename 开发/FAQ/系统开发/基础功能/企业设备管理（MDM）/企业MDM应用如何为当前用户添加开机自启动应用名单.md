# 企业MDM应用如何为当前用户添加开机自启动应用名单

更新时间：2026-06-26 07:48:29

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mdm-11

## 企业MDM应用如何为当前用户添加开机自启动应用名单
 


##### 问题现象

企业MDM应用如何实现在手机/PC系统重启后自动启动APP？获取不同空间的accountId参数，作为addAutoStartApps的参数，能否设置不同空间的自动启动APP？
 
 

##### 解决方案

- 企业MDM应用实现开机自启动可参考：添加开机自启动应用名单，使用[applicationManager.addAutoStartApps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-enterprise-applicationmanager#applicationmanageraddautostartapps)添加开机自启动应用名单。
- addAutoStartApps带accountId参数，只在最后调用addAutoStartApps的所属空间生效。
