# Hilog模块提供的OH_LOG_SetCallback接口返回的日志与系统落盘的Hilog日志是否一致

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-62

Hilog模块提供的OH_LOG_SetCallback接口返回的是该应用运行进程内打印的符合日志输出级别的全部日志，返回的日志不受系统超限机制管控。
 
系统落盘的Hilog日志是当前系统全部进程的符合日志输出级别的日志，包括应用通过OH_LOG_SetCallback接口监听的该应用运行进程内的日志。落盘的日志受系统超限机制管控，超限后的日志无法输出保存。
 
基于上述原因，针对该应用运行进程内的日志，OH_LOG_SetCallback返回的日志数量应该大于等于落盘中的应用日志数量。
