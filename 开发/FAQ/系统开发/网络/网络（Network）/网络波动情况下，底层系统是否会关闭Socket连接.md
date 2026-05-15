# 网络波动情况下，底层系统是否会关闭Socket连接

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-33

问题现象

在网络连接不稳定，频繁出现连接和断开的情况下，底层系统是否会关闭Socket连接？

解决措施

在网络不稳定（网络频繁断开和连接）时，底层系统会断开连接并关闭Socket端口，不会等待超时返回。
