# 如何进行DevEco Studio编译构建初步性能分析

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-70

Build Analyzer工具显示编译构建的重要信息，帮助开发者分析和排查性能问题。
 
构建完成后，通过以下方式打开Build Analyzer窗口：
 
- 在底部的工具栏区域，单击Build Analyzer窗口进行查看。
- 在左侧边栏单击
![](assets/如何进行DevEco%20Studio编译构建初步性能分析/file-20260515130125543-0.png)
，打开Build Analyzer窗口。
- 完成构建后首次打开Build Analyzer时，窗口显示构建分析概览，如下图所示：

 

![](assets/如何进行DevEco%20Studio编译构建初步性能分析/file-20260515130125543-1.png)

 
如需查看构建任务时间图谱，从下拉菜单中点击Tasks，默认进入时间图谱界面。该界面分块显示构建历史记录、构建任务时长图谱、构建日志及日志详情信息，如下图所示：
 

![](assets/如何进行DevEco%20Studio编译构建初步性能分析/file-20260515130125543-2.png)

 
事件信息：
  
| 事件 | 子事件 | 业务 |
| CompileResource |    | 资源编译 |
| PackageHap |    | 打包工具 |
| SignHap |    | 签名工具 |
| BuildNativeWithCmake |    | cpp编译工具链 |
| CompileArkTS | watchChangedFiles | ArkUI |
| CompileArkTS | invalidCachePlugin | 编译构建 |
| CompileArkTS | oh-resolve | 编译构建 |
| CompileArkTS | moduleInfoMetaPlugin | 编译构建 |
| CompileArkTS | commonjs | 编译构建 |
| CompileArkTS | 语言和类型编译器 | ArkUI 语言和类型编译器 |
| CompileArkTS | ArkUI | ArkUI |
| CompileArkTS | buildInstrument | 测试框架 |
| CompileArkTS | 模块化，es2abc | 模块化，es2abc 语言和类型编译器 |
| CompileArkTS | 编译构建 | 编译构建 |
| CompileArkTS | 编译构建 | 编译构建 |
| CompileArkTS | ignorePlugin：编译构建工具 | 编译构建 |
| CompileArkTS | api范式 | api范式 |
|    | commonPlugin：编译构建工具 | 编译构建 |
 
 
参考链接：
 
[分析构建性能](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-analyzer)
