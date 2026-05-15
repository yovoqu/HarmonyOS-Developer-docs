# 应用配置文件概述（Stage模型）

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-configuration-file-overview-stage

每个应用项目的代码目录下必须包含应用配置文件，这些配置文件会向编译工具、操作系统和应用市场提供应用的基本信息。

 在基于Stage模型开发的应用项目代码下，都存在一个app.json5配置文件、以及一个或多个module.json5配置文件。


> [!NOTE]
> 编译后，单个模块的编译产物中，app.json5和module.json5的内容会合并到一个module.json文件中，详情参考编译态包结构的编译打包后的视图。

 [app.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-configuration-file)包含以下内容：


 [module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)包含以下内容：
