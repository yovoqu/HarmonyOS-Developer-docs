# DevEco Studio版本更新后问题汇总

更新时间：2026-06-26 07:47:42

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-34

#### 问题现象

DevEco Studio版本更新无法正常使用，原因有哪些？
 
 

#### 背景知识

DevEco Studio不支持自更新，需要开发者前往[官网链接](https://developer.huawei.com/consumer/cn/download/)下载最新版本安装。
 
 

#### 问题定位

- **DevEco Studio版本更新无法正常使用，可能有多种现象和原因，汇总如下：**

| 问题现象 | 问题原因 |

| 项目无法正常启动，提示hvigor没能同步 | hvigor相关配置文件未更新 |

| 项目运行失败，报错“A page configured in 'test_pages.json' must have one and only one '@Entry' decorator” | 新版本默认路径文件夹名变更 |

| 执行测试任务失败 | 新版本测试框架版本与原工程不匹配 |

| DevEco Studio无法正常启动 | 旧版本缓存文件未清理 |

 
- **场景一：项目无法正常启动，提示hvigor没能同步。**报错如下图：

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/jg5YNJOJRBCoKsRVpv767Q/zh-cn_image_0000002658804377.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=2896CF6ADC55092288601D0CE4A74962B8EED1DD0AFCDDA3E52E1D1191068327)


  根据报错信息可知：问题原因是当前hvigor的开发态配置版本与IDE能支持的开发态配置版本不匹配。
- **场景二：项目运行失败，报错“A page configured in 'test_pages.json' must have one and only one '@Entry' decorator”。**报错信息：A page configured in 'test_pages.json' must have one and only one '@Entry' decorator。

  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/Ca-vKq0eQ36qOqjQ7hRkOA/zh-cn_image_0000002628565014.png?HW-CC-KV=V1&HW-CC-Date=20260730T072710Z&HW-CC-Expire=86400&HW-CC-Sign=C6ECC2E9684F04BD20EDD64AA6D648B50FBC9CF7AD6932205D73E71C4911CC37)


  根据报错信息可知：问题原因是配置在test_pages.json里的页面必须有且只能有一个'@Entry'装饰器。
- **场景三：执行测试任务失败。**问题现象：升级DevEco Studio后，打开先前创建的工程并执行测试框架任务时遇到失败。

  常见原因：由于新版本测试框架版本与原工程不匹配，直接使用原工程会失败。
- **场景四：DevEco Studio无法正常启动。**问题现象：升级DevEco Studio后，DevEco Studio无法正常启动。

  常见原因：旧版本缓存文件未清理导致启动失败。

 
 

#### 分析结论

- **场景一：当前hvigor的开发态配置版本与IDE能支持的开发态配置版本不匹配。**
- **场景二：配置在test_pages.json里的页面必须有且只能有一个'@Entry'装饰器。**
- **场景三：新版本测试框架版本与原工程不匹配。**
- **场景四：旧版本缓存文件未清理。**

 
 

#### 修改建议

- **场景一：提供如下两种方案，推荐使用第一种方案。**
运行前检查：在DevEco Studio中通过“Help -> Check for Updates”来检查更新，确保使用的DevEco Studio和SDK是[最新版本](https://developer.huawei.com/consumer/cn/download/deveco-studio)，避免一些已知的兼容性问题。检查项目的build-profile.json5文件中的[compileSdkVersion](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-new-features)和[compatibleSdkVersion](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/deveco-studio-new-features)字段，确保设置正确并且相互兼容，视情况进行修改。参考[官方文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-allversion)，确认DevEco Studio版本与API版本是否匹配。
- 新建一个项目，把新项目的build-profile.json5、module.json5、hvigor-config.json5复制进旧项目，通过打包使用正确配置文件解决问题。

 - **场景二：将TestRunner、TestAbility目录改为小写testrunner、testability，再次运行测试用例。[参考文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-6)。**
- **场景三：使用升级后的DevEco Studio创建新工程，迁移原有测试任务。**

  升级原工程，具体包括以下步骤：1. 升级hypium插件版本：在工程级oh-package.json5中，将hypium升级至最新版本。

2. 替换OpenHarmonyTestRunner入口文件：新建工程，将src/ohosTest/ets/testrunner/OpenHarmonyTestRunner.ets文件替换原工程的该文件。

3. 修正错误：替换完上述文件后，根据错误提示修改细节。
- **场景四：清理缓存文件后，重启DevEco Studio。**

  缓存文件位置如下：
MAC的缓存路径为：~/Library/Caches/Huawei/和~/Library/Application Support/Huawei/。
- Windows的缓存路径为：C:/Users/&lt;用户名&gt;/AppData/Local/Huawei/。
