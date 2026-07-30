# DevEco Studio如何调整页面窗口布局

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-42

#### 问题现象

 
- 问题一：侧边按键被删除后如何恢复？例如日志按钮。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/FtmQHg6gSY-BQ7_PSgdwCA/zh-cn_image_0000002628565334.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=E7BDB865DC4FABF3AEE87717C10C676BBBA6415967823C586A9068FECD735653)

- 问题二：日志窗口侧边功能按钮被删除后如何恢复？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/98uYHm-9Spen2XjAW0cAqQ/zh-cn_image_0000002628405432.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=DABA7241B260A5D880C84AB13DE3DE8636CFCAFD778BF9F10B9F65CF852ECCC3)

- 问题三：需要结合断点和日志信息进行调试，如何设置调试界面和日志输出界面同时在底部展示？
调试窗口：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/p06sgda9TB2uqzEeFg0ILw/zh-cn_image_0000002658924639.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=23B02752DC7E7662ECF554EBC5097680C1C7A295CF37DF62CEB9C5D39A42882D)

- 日志窗口：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/-Y-Ld9UORoS3lItaHOOhgg/zh-cn_image_0000002658804703.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=25F2A8046F2E54DED0826E53810E6A83AA78D6287C00AE15F913353B8F88DB9F)


 - 问题四：日志窗口中按键分别对应什么能力？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/VrHmLC6SQPSCaAB_dALu9A/zh-cn_image_0000002628565336.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=81E5B5E39E8FFE3D21936EFDD6370D5CD5A4FE5E74AAB4469ABBCAB2905780F1)


 

#### 背景知识

[DevEco Studio集成开发环境](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tools-overview#section268251193716)：HUAWEI DevEco Studio（获取工具请单击链接下载，以下简称DevEco Studio）是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助你高效开发HarmonyOS应用/元服务。
 
 

#### 解决方案

 
- 问题一：通过**视图**-**工具窗口**-**日志**或者**Ctrl+Alt+5**重新打开日志窗口。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/AGkGFxOWRH-VcZUnKChzkA/zh-cn_image_0000002628405434.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=61CE635B3C713BE7C70E8BCD9A6B20D1607459AA8260A58CAC11C82367533C49)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/QNrLZL_KTv-FtnyVCIKn9w/zh-cn_image_0000002658924641.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=ED1076C046DEE9C6400EBF4248F20AA1CD3408592B690D941CBA4091D75F8698)


 - 问题二：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，选中**显示工具栏**。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/iJgak1kxTxWO8_R1-6U2nw/zh-cn_image_0000002658804705.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=3940B383345780C0F64397F148914EEB57E8B481388D2D9E141B56C2214A95E4)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/3ntib4r4QKWFi6_KKMa1cw/zh-cn_image_0000002628565338.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=EF8E5CC60F7FCB05D2D40F635758B908CADB4B9F06DFE1891DC00D70998910A9)


 - 问题三：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，选中**移动到**，调整窗口位置，可选择**底部 右**。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/mYwy_MxISQWMOBrnciQrEQ/zh-cn_image_0000002628405436.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=5C052E2D8437E0C66C605606F21B8164A2495CA516CE15D42C4262B4ECB45777)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/PStiqfL2SjOrKPQuRUU1kw/zh-cn_image_0000002658924643.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=BC37EBAA231517F314CF09D3450D15E9A4A938362DCEFFAE78002B85BF530442)


 - 问题四：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，点击**？帮助**，即可跳转至文档介绍。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/rJJ9v-EwTbm5V2DbA6fadA/zh-cn_image_0000002658804707.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=F95C5E174A6EDA3AFF4DE9F7A19F86C0F3F7D8E20D77CCEA8B3836928EC9BCCC)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/u7SnG3_WQFGnyinMzDoQCA/zh-cn_image_0000002628565340.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=4CBF921891634852B9F0047B13C571D0356F0D5E061D4E04D2ADA43B7702F362)
