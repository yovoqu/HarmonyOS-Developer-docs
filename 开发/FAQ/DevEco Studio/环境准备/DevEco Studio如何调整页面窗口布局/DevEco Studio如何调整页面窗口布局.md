# DevEco Studio如何调整页面窗口布局

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-42

#### 问题现象

 
- 问题一：侧边按键被删除后如何恢复？例如日志按钮。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/FtmQHg6gSY-BQ7_PSgdwCA/zh-cn_image_0000002628565334.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=37FEC2649A254328BF0A536BC60A6389FA86E6D4EBD61B8FC272621ECCE61E93)

- 问题二：日志窗口侧边功能按钮被删除后如何恢复？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/98uYHm-9Spen2XjAW0cAqQ/zh-cn_image_0000002628405432.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=8A6384849B65736F4829AD975269E858FBFC72EB04C25A2732654EDAB3332DE0)

- 问题三：需要结合断点和日志信息进行调试，如何设置调试界面和日志输出界面同时在底部展示？
调试窗口：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/p06sgda9TB2uqzEeFg0ILw/zh-cn_image_0000002658924639.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=6C6757CF6742E41656F801ECABB6B9B5001F2BA7A5FB6EEA634511C7C782EE35)

- 日志窗口：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/-Y-Ld9UORoS3lItaHOOhgg/zh-cn_image_0000002658804703.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=B9513EED71DB21459312E6467AE89CD7397ECA75356DC58DD1AD2222526133F1)


 - 问题四：日志窗口中按键分别对应什么能力？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/VrHmLC6SQPSCaAB_dALu9A/zh-cn_image_0000002628565336.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=321817245639312688BCED0E9CB2A467D5F69C48D9D8F0454ABBF29AFC69077A)


 

#### 背景知识

[DevEco Studio集成开发环境](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tools-overview#section268251193716)：HUAWEI DevEco Studio（获取工具请单击链接下载，以下简称DevEco Studio）是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助你高效开发HarmonyOS应用/元服务。
 
 

#### 解决方案

 
- 问题一：通过**视图**-**工具窗口**-**日志**或者**Ctrl+Alt+5**重新打开日志窗口。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/AGkGFxOWRH-VcZUnKChzkA/zh-cn_image_0000002628405434.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=12C47D45EA6B378A44BED093FEAC145ABE625CE5B96368A5B6132D63D778F191)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/QNrLZL_KTv-FtnyVCIKn9w/zh-cn_image_0000002658924641.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=DFD81BD8799936665354021335868818649F510FB7DE935DB154CA25F62BC7F7)


 - 问题二：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，选中**显示工具栏**。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/iJgak1kxTxWO8_R1-6U2nw/zh-cn_image_0000002658804705.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=3DBD6517D021AC1A7BBFB0BC46EF0AD621C16AA3C8A6E96B108F4517B6A47183)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/3ntib4r4QKWFi6_KKMa1cw/zh-cn_image_0000002628565338.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=14B6B84C2D8C133D120FB21F1D58CC18E0D7CC51D0F440B600C6D9682B311E50)


 - 问题三：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，选中**移动到**，调整窗口位置，可选择**底部 右**。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/mYwy_MxISQWMOBrnciQrEQ/zh-cn_image_0000002628405436.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=5632137EFAC08CE83F10A1D9D4BB4069F786BDCFBA9D561F33035BE26246B2C2)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/PStiqfL2SjOrKPQuRUU1kw/zh-cn_image_0000002658924643.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=32CADAD48F314CFB45133778729D813372ACB1DD81344C00DCDEBB4964429CB4)


 - 问题四：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，点击**？帮助**，即可跳转至文档介绍。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/rJJ9v-EwTbm5V2DbA6fadA/zh-cn_image_0000002658804707.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=A434B282C7B0A0B52AF2E65838B74684C7B3506E37DC1F25777833EBF979CFA4)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/u7SnG3_WQFGnyinMzDoQCA/zh-cn_image_0000002628565340.png?HW-CC-KV=V1&HW-CC-Date=20260723T013908Z&HW-CC-Expire=86400&HW-CC-Sign=1912566AC3A96B7FA11F29D9295911412B3B820417B58DA8F8F4AB11DBC145C3)
