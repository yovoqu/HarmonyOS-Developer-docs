# so信息可视化

更新时间：2026-03-17 02:59:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-so

在native调试窗口中，点击**Layout Settings**
![](assets/so信息可视化/file-20260514133002650-0.png)
，勾选**Modules**，打开模块视图。
 
在native调试期间，**Modules**窗口会列出并显示有关应用使用的so信息。点击各属性可按升序/降序来排序，支持字符串匹配搜索。
 

![](assets/so信息可视化/file-20260514133002650-1.png)

 
- 加载符号表文件如果符号未加载，可右键点击模块，选择**Load Modules**，加载本地携带符号信息的so文件。加载成功后，Symbol Status列会显示"Symbols Loaded"。

  如需将符号恢复为初始状态，可右键点击模块，选择**Reset ****Modules**。
- 添加源码地址映射加载的符号表文件路径默认是编译时的路径，若与本地的源码文件路径不一致时，需要关联源码文件。右键点击模块，选择**Set Source Mapping**，选择本地源码文件路径，映射成功后，Source Root Path列会显示映射后的路径。

  如需恢复为默认路径，可右键点击模块，选择**Reset ****Source Mapping****s**。
