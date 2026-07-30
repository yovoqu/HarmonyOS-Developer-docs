# 项目入口的Ability配置错误，导致项目启动白屏

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-34

#### 问题现象

工程中存在多个模块，其中包括HAP模块hapA中依赖了HAR模块harA，现在选择模块hapA，然后启动项目后，应用界面呈现白屏。工程目录如下所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/LpjXK-VcQTmHVejr7kJ4qA/zh-cn_image_0000002628567966.png?HW-CC-KV=V1&HW-CC-Date=20260730T072712Z&HW-CC-Expire=86400&HW-CC-Sign=320C1BA5D3DAC2BAF2DE16735F070744A87F91A63B5D07C890B08FAC24E8AAC7)

 
 

#### 背景知识

- HAP是应用安装和运行的基本单元。HAP包是由代码、资源、第三方库、配置文件等打包生成的模块包，其主要分为两种类型：entry和feature。详情可参考[HAP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hap-package)。
- HAR是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不支持在设备上单独安装或运行，只能作为应用模块的依赖项被引用。详情可参考[HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package)。
- Stage模型应用程序中，HAR模块支持在配置文件中声明UIAbility组件，但不支持在配置文件中声明page页面，可以包含page页面，并通过[命名路由](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing#命名路由)的方式进行跳转，详情可参考[Stage模型应用程序包结构](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-package-structure-stage)选择合适的包类型。

 
 

#### 问题定位

- 在DevEco中展开HAR模块harA的模块目录，检查下是否模块创建后手动添加了UIAbility组件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/-T2QGj7zRzut2QyK37VjBg/zh-cn_image_0000002658927287.png?HW-CC-KV=V1&HW-CC-Date=20260730T072712Z&HW-CC-Expire=86400&HW-CC-Sign=6407129FE859C109CFFCD19EC7AE3BFEBD6B12E25A5CA9FB3E5C6CFC69969418)

- 在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,查看项目入口的Ability配置的是否正确。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/gkpMwar4Tlm_D7dlzhwucw/zh-cn_image_0000002658807331.png?HW-CC-KV=V1&HW-CC-Date=20260730T072712Z&HW-CC-Expire=86400&HW-CC-Sign=7B40C18652F4427F282C91D6BD8460F3C08C1F2F779D24CC9A0BAF7CC0B447DB)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/PxSCGeQuT6iVnbE9JoOHHw/zh-cn_image_0000002628408070.png?HW-CC-KV=V1&HW-CC-Date=20260730T072712Z&HW-CC-Expire=86400&HW-CC-Sign=CC84A8E2F7CDC1B8A5BA6C3DF9EEE9672F77042821C60482627A3245C237E636)


 
 

#### 分析结论

在选择模块hapA启动项目时，由于模块harA中手动添加并声明了UIAbility组件，而HAR模块中不支持在配置文件中声明page页面，模块hapA依赖了harA，项目入口的Ability配置成了模块harA的UIAbility，所以启动后应用呈现白屏。
 
 

#### 修改建议

在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,将项目入口的Ability配置成模块hapA的UIAbility。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/oELakd_wQ0SIbjs7Rgejnw/zh-cn_image_0000002628567970.png?HW-CC-KV=V1&HW-CC-Date=20260730T072712Z&HW-CC-Expire=86400&HW-CC-Sign=93BEDFF820D40CA9053F68C66454C5DC2CD76E39646B3305D985EC4625BEDA77)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/jMUzFQCnTD-3Gzm8ATnVXg/zh-cn_image_0000002658927289.png?HW-CC-KV=V1&HW-CC-Date=20260730T072712Z&HW-CC-Expire=86400&HW-CC-Sign=E22C635639E5243BD96649DEEEEC022F3B23766F77D7F86D853A3250A44B3939)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/u40XEXiRQ-WFcE1VoPG2kw/zh-cn_image_0000002658807335.png?HW-CC-KV=V1&HW-CC-Date=20260730T072712Z&HW-CC-Expire=86400&HW-CC-Sign=073149B27516639BEDC43374C0E4118892C54088D81C5B00AD84499E0E09827F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/jZJxSA_iQ7WxK43WHDVE9w/zh-cn_image_0000002628408074.png?HW-CC-KV=V1&HW-CC-Date=20260730T072712Z&HW-CC-Expire=86400&HW-CC-Sign=C0A0766208E2ADCBE234BDC78A7D945CEBF70768B6B1DABDEA13FC370F766F00)
