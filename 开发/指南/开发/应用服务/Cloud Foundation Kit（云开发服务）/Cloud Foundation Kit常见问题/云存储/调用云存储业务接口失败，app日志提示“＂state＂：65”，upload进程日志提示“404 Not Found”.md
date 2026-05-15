# 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6

**问题现象**

 通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：


 **解决措施**

 出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

 请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
