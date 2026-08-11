# DevEco Studio如何调整页面窗口布局

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-42

#### 问题现象

 
- 问题一：侧边按键被删除后如何恢复？例如日志按钮。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/FtmQHg6gSY-BQ7_PSgdwCA/zh-cn_image_0000002628565334.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=49CC490B7A7B97A27436BC6D89879D5906D540875C482FA60FD9520EA54DE9C0)

- 问题二：日志窗口侧边功能按钮被删除后如何恢复？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/98uYHm-9Spen2XjAW0cAqQ/zh-cn_image_0000002628405432.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=0639689230BCED529673F23FAB573E2B9CAEF300FE7C365FA88D3FD8D69EDD4C)

- 问题三：需要结合断点和日志信息进行调试，如何设置调试界面和日志输出界面同时在底部展示？
调试窗口：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/p06sgda9TB2uqzEeFg0ILw/zh-cn_image_0000002658924639.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=CB8FC681B45C261CF35EF798618797761FA68DA9D7D90A6A5A5DF002AD9BB6DB)

- 日志窗口：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/-Y-Ld9UORoS3lItaHOOhgg/zh-cn_image_0000002658804703.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=179C3FF7F782BFD725665D0A154A074100DB523AB204DA243940712CAB878487)


 - 问题四：日志窗口中按键分别对应什么能力？
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/VrHmLC6SQPSCaAB_dALu9A/zh-cn_image_0000002628565336.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=8DD4CB76BD7D45DE9811444A64E8328EE7AB48DB41FEB958B2BE5BEE865CD102)


 

#### 背景知识

[DevEco Studio集成开发环境](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tools-overview#section268251193716)：HUAWEI DevEco Studio（获取工具请单击链接下载，以下简称DevEco Studio）是基于IntelliJ IDEA Community开源版本打造，面向HarmonyOS应用/元服务开发场景的一站式集成开发环境。提供AI辅助编程、编译构建、UI实时预览、代码调试、性能调优、模拟器等功能，帮助你高效开发HarmonyOS应用/元服务。
 
 

#### 解决方案

 
- 问题一：通过**视图**-**工具窗口**-**日志**或者**Ctrl+Alt+5**重新打开日志窗口。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/AGkGFxOWRH-VcZUnKChzkA/zh-cn_image_0000002628405434.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=335C622AA2C444661C4916A9619A65B8A6BF29DF1DAAB0BD0ECEFC21CD7BC024)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/QNrLZL_KTv-FtnyVCIKn9w/zh-cn_image_0000002658924641.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=CCBB96A68F828832672FDA58F5AB6FE4DBF250DDFBE7985EB55FEB4965A4F19C)


 - 问题二：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，选中**显示工具栏**。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/iJgak1kxTxWO8_R1-6U2nw/zh-cn_image_0000002658804705.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=422340F98D2A0CCF9C83B49DAB8DAA49BA1B11CBED6B2572C9E98E16BE768DAF)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/3ntib4r4QKWFi6_KKMa1cw/zh-cn_image_0000002628565338.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=17928635FD90ACFA020638E75D955580A5DB274C0C4F1062413707CE07EB36F2)


 - 问题三：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，选中**移动到**，调整窗口位置，可选择**底部 右**。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/mYwy_MxISQWMOBrnciQrEQ/zh-cn_image_0000002628405436.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=1D63834D07D096E571BADA687E4BDC0B552A7E2FC49F2D1CC8A02A8EA6C14644)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/PStiqfL2SjOrKPQuRUU1kw/zh-cn_image_0000002658924643.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=4842CEF9C8361D7EDAAE06AB98E435D26811AC8961A5C003C1CFA69877D4C6BB)


 - 问题四：通过将鼠标移动至日志窗口内，点击右上角三点显示菜单选项图标，或者鼠标右键点击日志窗口顶部，点击**？帮助**，即可跳转至文档介绍。
操作：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/rJJ9v-EwTbm5V2DbA6fadA/zh-cn_image_0000002658804707.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=B6B4E1499E6D7A709C56AB17FC353611F7E1E4DCAC0008402D5534E9F5AA19EB)

- 效果：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/u7SnG3_WQFGnyinMzDoQCA/zh-cn_image_0000002628565340.png?HW-CC-KV=V1&HW-CC-Date=20260811T005522Z&HW-CC-Expire=86400&HW-CC-Sign=28FAE1BB0EA78AD1206E8E0A99EEC658EA33DF47E408DB8379534D475DDF8700)
