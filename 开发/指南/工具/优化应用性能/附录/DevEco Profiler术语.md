# DevEco Profiler术语

更新时间：2026-07-28 12:07:32

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-devecostudio-glossary

#### 异步栈缝合

在异步回栈时，可单击工具控制栏中的
![](assets/DevEco%20Profiler术语/file-20260514133159433-0.png)
按钮，配置异步栈嵌套层数和异步回栈层数。
 
如下图中的start_malloc_xxx_work异步调用malloc_xxx_work，当开关未开启时，仅能回malloc_xxx_work栈帧；当开关开启后，支持回malloc_xxx_work栈帧和start_malloc_xxx_work栈帧。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Jz_di-HLS7OYdqaX59S7AA/zh-cn_image_0000002677996883.png?HW-CC-KV=V1&HW-CC-Date=20260730T071824Z&HW-CC-Expire=86400&HW-CC-Sign=105473C4F84B553E1871FAB75E7A46420EC4413C131E8439652F5C0CA8345792)
