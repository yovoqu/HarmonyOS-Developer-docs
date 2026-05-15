# 编译报错“Failed to get a resolved OhmUrl by filepath xx”

更新时间：2026-03-17 00:56:02

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-10

- **场景一：****问题现象** 如果工程在本地可编译成功，压缩后拷贝到其他环境中再打开该工程编译构建失败，提示 “ERROR:  ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xx”。 **解决措施** 该问题源于工程中存在oh_modules目录。由于oh_modules中包含软链接，压缩后软链接失效，导致在其他环境中编译时无法找到对应的文件。 删除工程中的oh_modules，执行File > Sync and Refresh Project。
![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-0.png)
- **场景二：****问题现象** 当配置第三方包依赖时，如果将依赖配置到devDependencies，而源码中又引用了这些依赖中的 API，会导致编译失败。例如，第三方包@hms-security/ucs-appauth将依赖@network/gr配置在devDependencies中，源码中使用了@network/gr的 API 时，编译会失败，提示错误信息：“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。
![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-1.png)

**问题确认**进入上面标黄色的源码文件中，可以看到依赖有红色告警信息。
![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-2.png)
- 进入包下的oh-package.json5文件，查看依赖配置为devDependencies。
![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-3.png)
- 向开发团队建议：运行时的依赖不应配置在devDependencies中。
- 在依赖上层引入对应的devDependencies中的第三方包规避此问题。


- **场景三：****问题现象** DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。 **问题确认** 检查工程目录下的build-profile.json5文件中modules字段配置的srcPath路径是否与实际路径不同，以及是否存在大小写不一致的问题。 **解决措施** 将build-profile.json5文件中modules字段的srcPath路径与真实路径保持一致。
- **场景四：****问题现象** 工程A以相对路径引用了工程B的模块，这种引用会导致报错。
![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-4.png)

![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-5.png)

![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-6.png)
**处理措施** 将工程B的har转换为工程A的一个模块引用。
- 把工程B的har提前打包，在A中 以.har的方式引用。
- 上传到仓库，以版本号的方式引用。

 场景五：
问题现象

DevEco Studio编译失败，提示“Error Message: Failed to get a resolved OhmUrl for 'hvigor\_ignore\_xxxxx' imported by xxx”。

处理措施

如果hvigor_ignore_xxxxx所在的模块是一个har模块，需要排查oh-package.json5中是否存在“"packageType": "InterfaceHar"”，如果存在，请删除“"packageType": "InterfaceHar"”。

如果hvigor_ignore_xxxxx所在的模块是一个hsp模块，需要排查\${模块路径}\build\default\cache\default\default@CompileArkTS\esmodule\${debug/release}\filesInfo.txt文件中是否存在hvigor_ignore_xxxxx路径，如果存在，可将hvigor_ignore_xxxxx路径所在的模块或包添加到当前编译模块oh-package.json5的dependencies中临时规避。
 场景六：
问题现象

DevEco Studio编译失败，提示“Failed to get a resolved OhmUrl for‘xxx’imported by‘yyy’”。


![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-7.png)


问题确认

1. 检查yyy所在模块是否为[字节码HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har#section16598338112415)，并查看工程级build-profile.json5的useNormalizedOHMUrl是否为true（缺省默认值为false）。如果为true，则默认构建字节码har。
2. 如果yyy模块是字节码har，请检查xxx依赖是否已配置在工程级oh-package.json5的dependencies中，但未配置在yyy模块级oh-package.json5的dependencies中。


处理措施

- 将xxx依赖配置到yyy模块oh-package.json5的dependencies中。
![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-8.png)
- 将yyy模块改为非字节码har，在模块级build-profile.json5文件中添加byteCodeHar字段并设置为false。


- **场景七：**请确认当前使用的DevEco Studio和SDK版本是配套的，点击菜单栏**Help > About DevEco Studio**，**Help > About HarmonyOS SDK**分别查看DevEco Studio和SDK版本，版本配套关系请参考[版本概览](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-502-release)。
![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-9.png)
- **场景八：****问题现象：** DevEco Studio编译失败，提示“ERROR:  ArkTS:ERROR failed to execute es2abc ERROR:  ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。 **处理措施** 该问题由工程中引用了非标准模块目录（目录内无module.json5）引起，如下图所示。
![](assets/编译报错“Failed%20to%20get%20a%20resolved%20OhmUrl%20by%20filepath%20xx”/file-20260515130045333-10.png)
 请新建Static Library模块，并将utils/common里面的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。
