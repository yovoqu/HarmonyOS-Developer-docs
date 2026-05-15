# rcp请求是否有数据大小限制

更新时间：2026-04-27 09:10:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-2

rcp请求默认情况下，response响应中最大数据量为50MB，超过此限制建议通过HttpEventsHandler的onDataReceive实现流式数据接收。


参考链接

response

HttpEventsHandler

onDataReceive
