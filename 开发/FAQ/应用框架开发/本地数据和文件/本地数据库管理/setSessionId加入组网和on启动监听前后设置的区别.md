# setSessionId加入组网和on启动监听前后设置的区别

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-27

开发者应先启动监听再设置setSessionId加入组网，如果顺序相反，在setSessionId和启动监听之间的时间段内发生的数据变化将无法获取。具体影响需根据业务逻辑和代码确定。
