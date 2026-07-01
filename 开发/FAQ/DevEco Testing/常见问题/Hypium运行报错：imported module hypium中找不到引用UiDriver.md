# Hypium运行报错：imported module hypium中找不到引用UiDriver

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-deveco-testing-faq-13

## Hypium运行报错：imported module hypium中找不到引用UiDriver
 


##### 问题现象

伙伴Hypium脚本中使用“from hypium.advance.deveco_testing import UiDriver”进行导入，在运行脚本时报错：imported module hypium中找不到引用UiDriver，该问题如何解决？
 
 

##### 背景知识

[DevEco Testing Hypium](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section16890204264419)是HarmonyOS平台的UI自动化测试框架，支持开发者使用python语言为应用编写UI自动化测试脚本。
 
 

##### 问题定位

- 查看运行环境上依赖的安装包是否存在，版本是否正确，执行pip list命令查看xdevice、hypium。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/1uS250WySi2e4X0DLBhyHA/zh-cn_image_0000002658923399.png?HW-CC-KV=V1&HW-CC-Date=20260701T025927Z&HW-CC-Expire=86400&HW-CC-Sign=8161EDA04C55A8D1C75D43598EE048CBBB590C624509AC30CF4E92B52E8D1E2C)

 安装成功后示例如下（具体版本号根据实际情况检查）：
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/XgrJxh0aQ3qcGWWkDatALA/zh-cn_image_0000002658803449.png?HW-CC-KV=V1&HW-CC-Date=20260701T025927Z&HW-CC-Expire=86400&HW-CC-Sign=295112C917E21ED2916579F76E855CE7C7F1DDF53E60FC762390C009081BBA01)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/m8XBC1ArSh6ZF66CgaZrQw/zh-cn_image_0000002628404186.png?HW-CC-KV=V1&HW-CC-Date=20260701T025927Z&HW-CC-Expire=86400&HW-CC-Sign=D78F2A7071245FA1B40136326C922DEFE26ACFDC2254098DB3990BECE88541F7)

 而伙伴的xdevice版本显示为0.0.0。
 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/jptzGVDTQfWPGUxVRjs0lw/zh-cn_image_0000002628564090.png?HW-CC-KV=V1&HW-CC-Date=20260701T025927Z&HW-CC-Expire=86400&HW-CC-Sign=8BF17F1F28215A7D712EF1FCB880F1E6B77A54CC2E4FD448A725EBE8AD0ECF6C)

- 检查import的导入方法使用是否正确。找到Hypium插件的安装包路径，打开hypium_api的md文件（举例D:\devecotesting-hypium-6.0.7.202\hypium-6.0.7.202\doc下的hypium_api_6.0.7.202.md）。
 在该文件中查找“import UiDriver”，未发现“hypium.advance.deveco_testing”。

 
 

##### 分析结论

- xdevice未有效安装，显示为0.0.0版本。
- import使用方法不正确，未在Hypium插件版本中找到“hypium.advance.deveco_testing”。

 
 

##### 修改建议

- 使用“python -m pip uninstall xx”命令进行xdevice和hypium卸载，需要依次卸载hypium、xdevice-ohos、xdevice-devicetest、xdevice。python -m pip uninstall -y hypium
 python -m pip uninstall -y xdevice-ohos
 python -m pip uninstall -y xdevice-devicetest
 python -m pip uninstall -y xdevice
- 按照[安装向导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hypium-python-guidelines#section191615399595)中的“安装Hypium”指导，重新进行xdevice和hypium的安装。
- 基于已安装的Hypium版本，使用“from hypium import UiDriver”或md文件中的“from hypium.action.device.uidriver import UiDriver”导入，举例：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/hGfxjnVmQy2tWzu9BMVMJg/zh-cn_image_0000002658923401.png?HW-CC-KV=V1&HW-CC-Date=20260701T025927Z&HW-CC-Expire=86400&HW-CC-Sign=BC8F89D72EFC330ABFD7604149041C0159CF336F210F1A2806B4123C5E09941A)
