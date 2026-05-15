# 是否可以在TaskPool中动态加载模块（HAR、HSP、SO）

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-47

TaskPool的动态加载能力与主线程相同。然而，TaskPool线程加载后，由于模块化线程隔离，无法被主线程复用。
