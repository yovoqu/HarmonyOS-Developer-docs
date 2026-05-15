# @ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-46

appId是调用方应用的包名。通过调用bundleManager.getBundleInfoForSelf()获取BundleInfo，然后通过BundleInfo对象的signatureInfo属性获取appId。
