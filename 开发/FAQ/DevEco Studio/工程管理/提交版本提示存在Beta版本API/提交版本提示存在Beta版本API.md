# 提交版本提示存在Beta版本API

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-36

#### 问题现象

DevEco Studio运行过程中SDK报错或者提交预审时提示使用Beta版本API。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Yad2JSzQT-qFEd9VGKVz1g/zh-cn_image_0000002628567978.png?HW-CC-KV=V1&HW-CC-Date=20260730T072712Z&HW-CC-Expire=86400&HW-CC-Sign=F3BF426D7A82FB38A0F583BAFC3DF650985F7899BEAD2D4BB6F6104BAB744693)

 
 

#### 解决方案
1. 通过界面菜单选择“Help>About HarmonyOS SDK”查询当前SDK版本，若版本超期，请更新DevEco Studio提升SDK版本。
2. HarmonyOS应用需要将工程级build-profile.json5文件里的"[runtimeOS](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app#section45865492619)"字段配置为"HarmonyOS"。
3. 点击Help=>Check for Updates查看IDE版本检查，确定版本不是Beta版本的IDE。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/4jZuinBUTCSzsHyPTBBehA/zh-cn_image_0000002658927299.png?HW-CC-KV=V1&HW-CC-Date=20260730T072712Z&HW-CC-Expire=86400&HW-CC-Sign=4DBFE29DDFE51314A96658958443D1F90F0A00B4A3DCAB888815C79D5EBF493C)

4. 在手机的设置=>关于手机中检查SDK版本，保证SDK版本和手机版本统一，可以升级手机系统或使用手机系统对应版本的IDE。
5. 检查包体中pack.info文件中的releaseType是否为Beta，若为Beta，用release版本IDE进行打包即可。
