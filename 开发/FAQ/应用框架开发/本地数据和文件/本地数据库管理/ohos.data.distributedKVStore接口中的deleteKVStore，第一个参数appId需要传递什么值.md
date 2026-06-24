# @ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值

更新时间：2026-06-15 08:43:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-46

appId是应用的唯一标识，由包名、下划线和证书公钥的Base64编码组成。可以调用[bundleManager.getBundleInfoForSelf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfoforself)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含appId信息。示例代码可参见：[如何获取应用信息中的appId](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common-problem-of-application#如何获取应用信息中的appid)。
