# 怎么解决打包时依赖的Har包没有打进去的问题

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-28

## 怎么解决打包时依赖的Har包没有打进去的问题
 


##### 问题现象

SDK项目中对功能做模块化拆分，如library、har1、har2，library依赖了har1和har2，点击Make Module 'library'发现har1和har2并没有打包进library.har中。
 
 

##### 背景知识

- [HAR包构建](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har)。
- 应用程序包开发和使用[har](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package)。

 
 

##### 问题定位

- 检查har1、har2模块module.json5文件中的type字段是否为har类型。
- 检查library模块oh-package.json5文件dependencies字段中是否已添加对har1、har2模块编译产物的依赖。

 
 

##### 分析结论

模块依赖配置错误，library模块未正确引用har1、har2。
 
 

##### 修改建议

**方案一**：
 
- 确认har1、har2模块module.json5文件中的type字段为har类型。
- 编译构建har1、har2，得到编译产物har1.har和har2.har。在library模块中新建文件夹libs（或其他名称），将编译产物har1.har和har2.har拷贝到libs文件夹中，在library模块中添加依赖指向模块内的两个har文件，编译构建library模块，此时har1和har2会被打包进library.har，可以供其他项目使用。

 
- 开发工程结构：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/LpqP9KfEQlWYoIZ_uG0xew/zh-cn_image_0000002628567956.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=CDEEE484B3C686C481E09492328E3FDA99446418246F6EDF3788150D81CC9BF1)


 
- library模块的oh-package-lock.json5：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/45rljVwuQj-RDpoMui1hRg/zh-cn_image_0000002658927279.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=DB59DF79390AA33293FD42730D87FD152161127CB0490B3C352FFE55EE0CDCE8)


 
- 编译工程结构：
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/iDkpwMR3RXWWW9Irxmp6Fw/zh-cn_image_0000002658807323.png?HW-CC-KV=V1&HW-CC-Date=20260701T025912Z&HW-CC-Expire=86400&HW-CC-Sign=12B9B73F85E8D7DD38E0FB1099B1198BDF739BBAAA0E941F8010AC5ED27B8AB1)


 
**方案二**：
 
发布HAR包到[ohpm](https://ohpm.openharmony.cn/#/cn/home)私仓，ohpm添加仓库，在oh-package.json5文件中配置依赖的har包，可以直接从仓库中下载安装。
 
发布HAR包[参考指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-har-publish)。
