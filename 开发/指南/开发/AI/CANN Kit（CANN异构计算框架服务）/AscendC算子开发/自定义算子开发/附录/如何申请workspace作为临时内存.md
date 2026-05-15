# 如何申请workspace作为临时内存

更新时间：2026-04-20 06:34:33

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-workspace

workspace是设备侧Global Memory上的一块内存。workspace内存分为两部分：系统workspace和开发者workspace。


- 需要使用Unified Buffer和L1 Buffer上空间且空间不够用时，可以将数据暂存至workspace上。
- 其他需要使用Global Memory上内存空间的场景。

不同开发方式下，具体的使用方法如下。
