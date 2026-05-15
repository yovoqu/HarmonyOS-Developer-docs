# PC设备录制Allocation模板时，Graphic Memory泳道中OpenGL ES子泳道无数据

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-14

问题现象

在使用PC设备时，通过FP回栈模式录制Allocation模板，Graphic Memory泳道中的OpenGL ES子泳道无数据。

可能原因

GPU底层库不支持FP回栈模式。

解决措施

开始录制前，单击工具控制栏中的
![](assets/PC设备录制Allocation模板时，Graphic%20Memory泳道中OpenGL%20ES子泳道无数据/file-20260515130335611-0.png)
按钮，设置内存分配栈回栈模式为DWARF。使用DWARF回栈模式采集数据时，性能开销较大，因此在录制Graphic Memory泳道时，建议不同时录制Native Allocation泳道。


![](assets/PC设备录制Allocation模板时，Graphic%20Memory泳道中OpenGL%20ES子泳道无数据/file-20260515130335611-1.png)
