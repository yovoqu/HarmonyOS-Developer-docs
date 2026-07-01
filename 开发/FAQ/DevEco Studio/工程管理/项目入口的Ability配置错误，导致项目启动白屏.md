# 项目入口的Ability配置错误，导致项目启动白屏

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-34

#### 问题现象

工程中存在多个模块，其中包括HAP模块hapA中依赖了HAR模块harA，现在选择模块hapA，然后启动项目后，应用界面呈现白屏。工程目录如下所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/LpjXK-VcQTmHVejr7kJ4qA/zh-cn_image_0000002628567966.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=F30438D636E763E502587482F48A76F80588157C9D9422E3454D5548BDB53EEA)

 
 

#### 背景知识

- HAP是应用安装和运行的基本单元。HAP包是由代码、资源、第三方库、配置文件等打包生成的模块包，其主要分为两种类型：entry和feature。详情可参考[HAP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hap-package)。
- HAR是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不支持在设备上单独安装或运行，只能作为应用模块的依赖项被引用。详情可参考[HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package)。
- Stage模型应用程序中，HAR模块支持在配置文件中声明UIAbility组件，但不支持在配置文件中声明page页面，可以包含page页面，并通过[命名路由](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing#命名路由)的方式进行跳转，详情可参考[Stage模型应用程序包结构](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-package-structure-stage)选择合适的包类型。

 
 

#### 问题定位

- 在DevEco中展开HAR模块harA的模块目录，检查下是否模块创建后手动添加了UIAbility组件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/-T2QGj7zRzut2QyK37VjBg/zh-cn_image_0000002658927287.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=08EF287854332187A1C9C9495D24AF6467BF7E1907FF11092C0A6DF3A33C1789)

- 在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,查看项目入口的Ability配置的是否正确。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/gkpMwar4Tlm_D7dlzhwucw/zh-cn_image_0000002658807331.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=FD283BD0C2F87EB2A3BDD8A8503803658677A69B1F662CB265B7E227C4778119)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/PxSCGeQuT6iVnbE9JoOHHw/zh-cn_image_0000002628408070.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=8F290D56C157DDB2889450BCA812D1D8A106EEADB4BED15678CF37E92CEBCC3F)


 
 

#### 分析结论

在选择模块hapA启动项目时，由于模块harA中手动添加并声明了UIAbility组件，而HAR模块中不支持在配置文件中声明page页面，模块hapA依赖了harA，项目入口的Ability配置成了模块harA的UIAbility，所以启动后应用呈现白屏。
 
 

#### 修改建议

在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,将项目入口的Ability配置成模块hapA的UIAbility。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/oELakd_wQ0SIbjs7Rgejnw/zh-cn_image_0000002628567970.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=673F0A7A1AC7C4DD634B01BAE79FA9C75854D3627D01B5510AAA7313A769D93E)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/jMUzFQCnTD-3Gzm8ATnVXg/zh-cn_image_0000002658927289.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=40B949644D9AE62A0304FED9E631FB78AB575FF20B06F431B34B820EE14F0AD9)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/u40XEXiRQ-WFcE1VoPG2kw/zh-cn_image_0000002658807335.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=55311BD67D9CAB9B851E087C11A594B6505DEC869D2BA7E5422E76575A494D31)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/jZJxSA_iQ7WxK43WHDVE9w/zh-cn_image_0000002628408074.png?HW-CC-KV=V1&HW-CC-Date=20260701T041009Z&HW-CC-Expire=86400&HW-CC-Sign=0BF45A10DD8958D51ECDDABCE9434E97EA8C3D3D389EC7BD1EDBB9926BE624FF)
