# 编辑器内存告警

更新时间：2026-08-05 01:58:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-12

#### 问题现象

在编辑ArkTS代码的时候收到内存告警，告警的场景有哪些，如何解决？
 
 

#### 问题定位

编辑器代码过程中收到内存告警，可能有多种现象和原因，汇总如下：
  
| 问题场景 | 问题原因 |
| --- | --- |
| ArkTS语言服务因内存不足而终止 | 多次执行git pull或切分支等大量修改代码的操作时，编辑器的Node进程内存峰值超过上限（默认为8GB），来不及回收内存导致OOM，编辑功能失效。 |
| ArkTS语言服务可用内存不足 | Node进程实际使用内存与启动时设置的内存上限配置比超过95%，继续使用容易导致Node进程内存达到上限频繁触发垃圾回收，导致代码联想等功能出现卡顿。 |
| ArkTS语言服务异常终止 | 工程代码量较大超出启动内存(默认为8GB)或多次执行git pull或切分支等大量修改代码的操作时，编辑器的Node进程内存峰值超过上限（默认为8GB），来不及回收内存导致OOM。 |
| 扫描文件并建立索引失败 | 编辑器启动时会扫描工程代码，当开发的工程代码量超过一定大小时，可能导致编辑器的Node进程超出内存上限（默认为8GB），从而导致编辑器启动失败。 |
 
 
 

#### 场景1

**问题现象**
 

![](assets/编辑功能失效，提示“ArkTS%20language%20service%20terminated%20due%20to%20memory%20constraints.”/file-20260515130025554-0.png)

 
**解决措施**
 
可以调整编辑器Node进程的内存上限来解决上述问题，请根据工程代码量和开发环境内存大小配置合适的Node进程内存上限。内存上限值需要随工程的代码量和复杂程度增长，通常代码量300万行的工程建议配置大于12G，400万行建议配置大于15G，每增加100万行增加3G，可根据具体情况适当增减。
 
以配置内存上限为12G举例，打开DevEco Studio，通过菜单栏的Help > Edit Custom Properties...，打开idea.properties配置文件。在文件中新增一行 arkts.server.max.old.space.size=12288，然后重启DevEco Studio。编辑器Node进程的内存上限将设置为12288M（即12G）。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/spQW6czfTPWe5VpEs-hrVw/zh-cn_image_0000002689477947.png?HW-CC-KV=V1&HW-CC-Date=20260813T095546Z&HW-CC-Expire=86400&HW-CC-Sign=20848B9DC38E7D94F797A7BF15D831145B43CDA36F946D102716277D88F85279)

 
 

#### 场景2

**问题现象**
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/YmDLLTOPQ2G58oIFDIQKFg/zh-cn_image_0000002689597745.png?HW-CC-KV=V1&HW-CC-Date=20260813T095546Z&HW-CC-Expire=86400&HW-CC-Sign=3F0F9F60E16DE82023F8A672F840CE17D30549E651264FF9AB7F247615D9C6F2)

 
**解决措施**
 
可以通过设置当前工程编辑器语言服务的Node进程的内存上限来解决上述问题。
 
点击配置内存（打开DevEco Studio，通过菜单栏的文件>设置... 打开，搜索内存设置）增加ArkTS语言服务最大内存大小的值。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/lWP0mrImQB6gvWlx46LXxw/zh-cn_image_0000002659358418.png?HW-CC-KV=V1&HW-CC-Date=20260813T095546Z&HW-CC-Expire=86400&HW-CC-Sign=863D3EFF29837A00E95FAA2F4383A53FCF43F478EC8B3A7E60C2C2814B72E439)

 
默认值通常为8G，如果在idea.properties中配置了arkts.server.max.old.space.size值则默认值等于该值。ArkTS语言服务最大内存大小是工程独立配置，配置后不会影响其他工程。idea.properties中的arkts.server.max.old.space.size值为全局配置。
 
 

#### 场景3

**问题现象**
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/VAKQ-HvqQT-cZRahYxx4Ew/zh-cn_image_0000002659518340.png?HW-CC-KV=V1&HW-CC-Date=20260813T095546Z&HW-CC-Expire=86400&HW-CC-Sign=F64C9D914DE14E4199176A07DF5F7A56BFFDC1F8C55D3F0E0B035A003A7BB72C)

 
**解决措施**
 
措施1：设置当前工程编辑器Node进程的内存上限同场景2。
 
措施2：可配置部分模块不加载[卸载和加载模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-load-unload-modules)。
 
 

#### 场景4

**问题现象**
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/QX83AsSxQ9W_KqcbGsTMMQ/zh-cn_image_0000002689477949.png?HW-CC-KV=V1&HW-CC-Date=20260813T095546Z&HW-CC-Expire=86400&HW-CC-Sign=9F67226D55B23AD7FA2B56CBAB92CF2B03CC88B4C137C9AF7A86A8ED74B9124B)

 
**解决措施**
 
优先按照场景2修改，若当前版本没有ArkTS语言服务最大内存大小设置则按照场景1修改。
