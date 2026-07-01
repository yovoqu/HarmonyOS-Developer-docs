# 项目入口的Ability配置错误，导致项目启动白屏

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-34

## 项目入口的Ability配置错误，导致项目启动白屏
 


##### 问题现象

工程中存在多个模块，其中包括HAP模块hapA中依赖了HAR模块harA，现在选择模块hapA，然后启动项目后，应用界面呈现白屏。工程目录如下所示：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/LpjXK-VcQTmHVejr7kJ4qA/zh-cn_image_0000002628567966.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=7D46352CFE442C914BC311BD831E1C754B6C15300ED6CED81B70A47C2238E837)

 
 

##### 背景知识

- HAP是应用安装和运行的基本单元。HAP包是由代码、资源、第三方库、配置文件等打包生成的模块包，其主要分为两种类型：entry和feature。详情可参考[HAP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hap-package)。
- HAR是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。HAR不支持在设备上单独安装或运行，只能作为应用模块的依赖项被引用。详情可参考[HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package)。
- Stage模型应用程序中，HAR模块支持在配置文件中声明UIAbility组件，但不支持在配置文件中声明page页面，可以包含page页面，并通过[命名路由](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing#命名路由)的方式进行跳转，详情可参考[Stage模型应用程序包结构](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-package-structure-stage)选择合适的包类型。

 
 

##### 问题定位

- 在DevEco中展开HAR模块harA的模块目录，检查下是否模块创建后手动添加了UIAbility组件。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/-T2QGj7zRzut2QyK37VjBg/zh-cn_image_0000002658927287.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=AF5A66A4A6096B1ACE3CF3FEC1E1134E82AF28CD2B7B8CDA27A0DA2D2D5E1240)

- 在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,查看项目入口的Ability配置的是否正确。
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/gkpMwar4Tlm_D7dlzhwucw/zh-cn_image_0000002658807331.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=F60BD3F12C67249785D726D31B006282412778A026B05507A5784F26C14E014A)

 
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/PxSCGeQuT6iVnbE9JoOHHw/zh-cn_image_0000002628408070.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=D3C7900E8CE0D2CAF2C95D98478F2D7496E6A30C47C531A63C39DFBC93994D2D)


 
 

##### 分析结论

在选择模块hapA启动项目时，由于模块harA中手动添加并声明了UIAbility组件，而HAR模块中不支持在配置文件中声明page页面，模块hapA依赖了harA，项目入口的Ability配置成了模块harA的UIAbility，所以启动后应用呈现白屏。
 
 

##### 修改建议

在DevEco中依次选择“hapA”-“Edit Configurations”-“Launch Options”-“Ability”,将项目入口的Ability配置成模块hapA的UIAbility。
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/oELakd_wQ0SIbjs7Rgejnw/zh-cn_image_0000002628567970.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=55DE69503977E39ED5150824FB20B35456222CF6C9C7D83EEFA66F0D48D8D039)

 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/jMUzFQCnTD-3Gzm8ATnVXg/zh-cn_image_0000002658927289.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=802B245E1B79004947538706AD4F3366F208D42F7B54810F270FDEA0B42BE714)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/u40XEXiRQ-WFcE1VoPG2kw/zh-cn_image_0000002658807335.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=675C4EAF3C508ADE14E33C32A48C9FB9B6A7202A11775207B450B9EBDDD5A395)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/jZJxSA_iQ7WxK43WHDVE9w/zh-cn_image_0000002628408074.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=9F2957C5AB760D4063B86E5F18CA067FA362AE31E3326C72D5EB9AF2AC1B9BBD)
