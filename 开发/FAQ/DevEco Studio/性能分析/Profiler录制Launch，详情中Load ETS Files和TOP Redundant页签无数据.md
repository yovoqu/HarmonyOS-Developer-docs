# Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-8

问题现象

Profiler录制Launch，将ETS文件监控时长配置为20000，录制成功后，详情中Load ETS Files和TOP Redundant页签无数据。


![](assets/Profiler录制Launch，详情中Load%20ETS%20Files和TOP%20Redundant页签无数据/file-20260515130332990-0.png)


![](assets/Profiler录制Launch，详情中Load%20ETS%20Files和TOP%20Redundant页签无数据/file-20260515130332990-1.png)


问题原因

ETS文件监控时长配置为20000，需要在拉起应用20000ms之后，才能生成对应的ETS冗余打点文件。

解决措施

将ETS文件监控时长配置为20000后，录制时长一定要大于配置时长。
