# debug启动调试

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug

可以按照如下方式启动调试会话。
 1. 如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。如果无法添加断点，请查看FAQ[调试过程中无法添加断点](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-1)。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/hFpy5L8ER9Cib2Zr9i86Og/zh-cn_image_0000002602066083.png?HW-CC-KV=V1&HW-CC-Date=20260528T014923Z&HW-CC-Expire=86400&HW-CC-Sign=A5EF38EE9240EE7FA6493F0F57525B38E80097A77425FE526241D0B4201507AE)


  设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
2. 在设备选择框中，选择调试的设备。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/4XcbTnnGS9yTr4AjIlS3zw/zh-cn_image_0000002571546600.png?HW-CC-KV=V1&HW-CC-Date=20260528T014923Z&HW-CC-Expire=86400&HW-CC-Sign=69456F7B74E3956A39E138E4B064F4FC5B3123AC65F654FC4F71197EE4639B73)

3. 选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-debug-configurations)。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/sRReZhlcSWiEvOGYu27lUg/zh-cn_image_0000002602186133.png?HW-CC-KV=V1&HW-CC-Date=20260528T014923Z&HW-CC-Expire=86400&HW-CC-Sign=7BEFD6B682AE2E3C860655D0E061EEB54602157A10368E0225EA6377EC8E2943)

4. 在工具栏中，单击Debug
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/2TBjosi-TpiHAYiTTV6QoQ/zh-cn_image_0000002602186135.png?HW-CC-KV=V1&HW-CC-Date=20260528T014923Z&HW-CC-Expire=86400&HW-CC-Sign=4712E32BE6D39342F5AE3BF3E35DDF5DD986A7C61DC3FE66B90E7C5C382684D5)
。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/AStgyJ_QT-uh-Ej4t-E3hg/zh-cn_image_0000002602186137.png?HW-CC-KV=V1&HW-CC-Date=20260528T014923Z&HW-CC-Expire=86400&HW-CC-Sign=B2486F5D87619D648446B13AE6265EA181CAC9462C397FEDAC908BAA8998F2E5)


  或者在工具栏中Run中选择Debug。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/k2vNyVWoTDOTiti4AboJ_A/zh-cn_image_0000002602186139.png?HW-CC-KV=V1&HW-CC-Date=20260528T014923Z&HW-CC-Expire=86400&HW-CC-Sign=EA0262D2E885BC5F05AFB11EC11D11644B1C4FA2DD6F73754DB01605AC493D2B)

5. 启动调试后，开发者可以通过[调试器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debugger)进行代码调试。

  如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/WZ1dMAfJQnarwBDmNccQ0g/zh-cn_image_0000002571546602.png?HW-CC-KV=V1&HW-CC-Date=20260528T014923Z&HW-CC-Expire=86400&HW-CC-Sign=6F037026D0B31F461C6BC17A3E73364E0B26FB6B14E7EC14F2E7A91ECD121B77)
