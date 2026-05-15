# 如何使用Sqlite全文检索能力

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-9

解决措施

没有提供直接的接口，需要执行SQL语句CREATE VIRTUAL TABLE语句建立FTS表，再使用MATCH操作符实现检索。

executeSql：执行包含指定参数但不返回值的SQL语句。

querySql：根据指定的SQL语句查询数据库中的数据。
