# 分布式对象必须要把默认obj的属性的每一个项值都设置undefined否则都会倒灌

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-26

在分布式对象组网时，如果两个对象的数据不一致，需要进行一次同步。后加入组网的对象的数据被视为最新数据，将覆盖先加入组网的数据。当新对象属性值为undefined时，系统会保留旧对象对应属性值，并接收已有数据。
