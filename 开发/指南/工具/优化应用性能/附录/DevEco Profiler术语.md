# DevEco Profiler术语

更新时间：2026-04-30 02:42:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-devecostudio-glossary

## 异步栈缝合

在异步回栈时，该功能支持多回一层异步栈帧。如下图中的start_malloc_xxx_work异步调用malloc_xxx_work，当开关未开启时，仅能回malloc_xxx_work栈帧；当开关开启后，支持回malloc_xxx_work栈帧和start_malloc_xxx_work栈帧。
![](assets/DevEco%20Profiler术语/file-20260514133159433-0.png)
