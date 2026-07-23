# 项目入口的Ability配置错误，导致项目启动白屏

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-34

#### 问题现象

工程中存在多个模块，其中包括HAP模块hapA中依赖了HAR模块harA，现在选择模块hapA，然后启动项目后，应用界面呈现白屏。工程目录如下所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/LpjXK-VcQTmHVejr7kJ4qA/zh-cn_image_0000002628567966.png?HW-CC-KV=V1&HW-CC-Date=20260723T013913Z&HW-CC-Expire=86400&HW-CC-Sign=80E65F8948DCE2B6B6B30234B1669B859F8E0917E7C6D727397574D44AE712F8)

 
 

#### 背景知识

- HAP是应用安装和运行的基本单元。HAP包是由代码、资源、第三方库、配置文件等打包生成的模块包，其主要分为两种类型：entry和feature。详情可参考[HAP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hap-package)。
- HAR是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不支持在设备上单独安装或运行，只能作为应用模块的依赖项被引用。详情可参考[HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package)。
- Stage模型应用程序中，HAR模块支持在配置文件中声明UIAbility组件，但不支持在配置文件中声明page页面，可以包含page页面，并通过[命名路由](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing#命名路由)的方式进行跳转，详情可参考[Stage模型应用程序包结构](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-package-structure-stage)选择合适的包类型。

 
 

#### 问题定位

- 在DevEco中展开HAR模块harA的模块目录，检查下是否模块创建后手动添加了UIAbility组件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/-T2QGj7zRzut2QyK37VjBg/zh-cn_image_0000002658927287.png?HW-CC-KV=V1&HW-CC-Date=20260723T013913Z&HW-CC-Expire=86400&HW-CC-Sign=5AD70B575C8EAAD427758C603C7D3B327EA13249DC9360B2DA9CFEA5338BDB79)

- 在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,查看项目入口的Ability配置的是否正确。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/gkpMwar4Tlm_D7dlzhwucw/zh-cn_image_0000002658807331.png?HW-CC-KV=V1&HW-CC-Date=20260723T013913Z&HW-CC-Expire=86400&HW-CC-Sign=00CBD1E5E3DA4A0C259A7784B1FA810DF908F8F46E6062A29EC0946540F77FB3)


  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/PxSCGeQuT6iVnbE9JoOHHw/zh-cn_image_0000002628408070.png?HW-CC-KV=V1&HW-CC-Date=20260723T013913Z&HW-CC-Expire=86400&HW-CC-Sign=E463C1F17E06CD0FAA65C67E9EB4934A4DDFB120DAEA9C01C4A206266F705B25)


 
 

#### 分析结论

在选择模块hapA启动项目时，由于模块harA中手动添加并声明了UIAbility组件，而HAR模块中不支持在配置文件中声明page页面，模块hapA依赖了harA，项目入口的Ability配置成了模块harA的UIAbility，所以启动后应用呈现白屏。
 
 

#### 修改建议

在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,将项目入口的Ability配置成模块hapA的UIAbility。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/oELakd_wQ0SIbjs7Rgejnw/zh-cn_image_0000002628567970.png?HW-CC-KV=V1&HW-CC-Date=20260723T013913Z&HW-CC-Expire=86400&HW-CC-Sign=B25CFC2D3FF420445549AAC515896A194F4E30752B14F8AADD6F8EAE9CC81CB5)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/jMUzFQCnTD-3Gzm8ATnVXg/zh-cn_image_0000002658927289.png?HW-CC-KV=V1&HW-CC-Date=20260723T013913Z&HW-CC-Expire=86400&HW-CC-Sign=690BC6D2A643591C28E62CA7E1285D8E4B98FF0733F26E6825A9727A8BBB6656)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/u40XEXiRQ-WFcE1VoPG2kw/zh-cn_image_0000002658807335.png?HW-CC-KV=V1&HW-CC-Date=20260723T013913Z&HW-CC-Expire=86400&HW-CC-Sign=A50B4430A4E28CDA55CAE3679A9F5B63D4332B549335F1F8889E3F8C8B70E843)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/jZJxSA_iQ7WxK43WHDVE9w/zh-cn_image_0000002628408074.png?HW-CC-KV=V1&HW-CC-Date=20260723T013913Z&HW-CC-Expire=86400&HW-CC-Sign=FD7F5D5356F583E89AFE8A7829311723AEEACCC15CD0C716286DEBF146BB6420)
