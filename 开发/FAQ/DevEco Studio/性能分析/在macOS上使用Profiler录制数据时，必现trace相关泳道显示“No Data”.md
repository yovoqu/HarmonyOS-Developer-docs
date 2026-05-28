# 在macOS上使用Profiler录制数据时，必现trace相关泳道显示“No Data”

更新时间：2026-03-10 06:16:35

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-13

**问题现象**
 
在macOS上使用Profiler录制数据时，可能必现trace相关泳道显示“No Data”。
 

![](assets/在macOS上使用Profiler录制数据时，必现trace相关泳道显示“No%20Data”/file-20260515130335088-0.png)

 
**问题原因**
 
当前macOS型号的芯片不支持trace_streamer解析，导致在录制数据时，trace相关泳道显示“No Data”。
 
**根因验证**
 
可以通过以下步骤验证：
 1. 在macOS的DevEco Studio安装目录下，找到trace_streamer.exe所在的目录。
2. 使用命令行工具，运行trace_streamer.exe 1.htrace -e 1.db命令来解析一个trace文件。
3. 如果命令执行结果为zsh: bad CPU type in executable，说明当前macOS芯片不支持trace_streamer解析。
 
**解决措施**
 
由于提供的trace_streamer.exe二进制文件是针对x86架构的，如果macOS使用的是ARM架构，则无法支持。可以通过安装Rosetta转义层来解决此问题。
