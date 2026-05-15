# 关于对relationalStore.RdbStore的使用问题：如何查询数据库，需要开一个子线程吗

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-47

查询数据库可以使用@ohos.data.relationalStore模块提供的query方法，该方法是异步方法，因此对于查询数据库操作，不需要开子线程。
