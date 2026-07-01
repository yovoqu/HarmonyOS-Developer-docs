# 解析应用minidump文件

更新时间：2026-06-24 07:08:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-analyze-dump

## 解析应用minidump文件
 

应用崩溃时支持生成minidump文件，具体请参考[OH_HiAppEvent_SetEventConfig接口说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events#oh_hiappevent_seteventconfig接口说明)。从26.0.0版本开始，DevEco Studio支持对minidump文件进行解析，并展示异常堆栈，帮助开发者快速分析定位问题。
 

##### 操作步骤

- 打开**Log**窗口，点击**AnalyzeDump**打开界面，选择要解析的dump文件和[带调试信息的so目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle#section1623725511263)，点击**Start Analyze**开始解析。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/Pl7kaWqpQaam5Or0HGndng/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260701T025445Z&HW-CC-Expire=86400&HW-CC-Sign=ABFFD75E8817522EDA3C30479D569D68CAD78CBCE103021F045D8C959800E34C)
 
应用运行崩溃时产生的dump，需要借助同一次构建生成的so文件中的符号信息才能解析。因此，此处选择的so目录，必须是该应用在构建时存放so文件的原始目录。若替换为其他时间或通过其他构建生成的so目录，会因符号不一致导致无法解析。
 

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/wSHv4UsZTBSuFWO1_bJftg/zh-cn_image_0000002624994491.png?HW-CC-KV=V1&HW-CC-Date=20260701T025445Z&HW-CC-Expire=86400&HW-CC-Sign=4A540D522BA7141AE8BA8FF2D84448F7513C92B18071C5C992123A59FF172335)

- 等待解析成功后，默认会展示异常线程和对应的堆栈，展开堆栈可查看变量信息，支持切换查看不同线程的堆栈，点击堆栈中的超链接可以跳转到对应的源码。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/wVMnPtt8T5-QDHDtw0LTZg/zh-cn_image_0000002625074631.png?HW-CC-KV=V1&HW-CC-Date=20260701T025445Z&HW-CC-Expire=86400&HW-CC-Sign=97058FBDBDD604CAE1486A8AFFA2A0C9F8371AC8ACF96568966E18B986E68AD1)

- 支持查看指定地址的内存，填写内存地址，点击**View**即可查看。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/vmfWohe9QSuxhE8xokH65w/zh-cn_image_0000002624994489.png?HW-CC-KV=V1&HW-CC-Date=20260701T025445Z&HW-CC-Expire=86400&HW-CC-Sign=EB78641FADEAA4E6B677506702D4C7F24CD5AEC162A08633424280ADC95FF1B6)

 点击**Settings**，可设置进制、偏移量和内存数量。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/E52KcB0-Teuob8db2k3gcQ/zh-cn_image_0000002594475130.png?HW-CC-KV=V1&HW-CC-Date=20260701T025445Z&HW-CC-Expire=86400&HW-CC-Sign=0E15272B754380DA25C0B7AEF36790BB6AE9F54BF2181D52D0844C9758C99D30)
