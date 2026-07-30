# 解析应用minidump文件

更新时间：2026-07-28 12:07:32

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-analyze-dump

应用崩溃时支持生成minidump文件，具体请参考[OH_HiAppEvent_SetEventConfig接口说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events#oh_hiappevent_seteventconfig接口说明)。从26.0.0版本开始，DevEco Studio支持对minidump文件进行解析，并展示异常堆栈，帮助开发者快速分析定位问题。
 

#### 操作步骤
1. 打开**Log**窗口，点击**AnalyzeDump**页签打开界面，选择要解析的dump文件和带调试信息的so目录（默认是模块下的build/{product}/intermediates/libs/{target}/{abi}，其中product和target默认是default，{abi}是设备CPU架构类型，如arm64-v8a），点击**Start Analyze**开始解析。
> [!NOTE]
> 应用运行崩溃时产生的dump，需要借助同一次构建生成的so文件中的符号信息才能解析。若使用源码变更后重新构建生成的so目录，可能会因符号不一致导致解析结果不准确或解析失败。


  
![](assets/解析应用minidump文件/file-202607081034263e6f2eba.png)

2. 等待解析成功后，默认会展示异常线程和对应的堆栈，展开堆栈可查看变量信息，支持切换查看不同线程的堆栈，点击堆栈中的超链接可以跳转到对应的源码。
![](assets/解析应用minidump文件/file-2026070810342697af2cc9.png)

3. 支持查看指定地址的内存，填写内存地址，点击**View**即可查看。也可以直接右键点击变量查看内存。
![](assets/解析应用minidump文件/file-2026070810342725eaa7b7.png)


  点击**Settings**，可设置进制、偏移量和内存数量。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/1WasSTeqRge9FYf7WXgPyQ/zh-cn_image_0000002648077256.png?HW-CC-KV=V1&HW-CC-Date=20260730T072033Z&HW-CC-Expire=86400&HW-CC-Sign=D5225E708DC5F6BF273572E95D7832E446C17DF6449BCD1CEA432ACA0AD5D28E)
