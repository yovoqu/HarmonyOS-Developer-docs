# hvigor-config.json5文件

更新时间：2026-07-29 07:25:01

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-set-options

**      


#### 配置文件结构

hvigor-config.json5文件整体的结构如下。

```json
modelVersion
dependencies
execution
└── analyze
└── daemon
└── incremental
└── parallel
└── typeCheck
└── optimizationStrategy
logging
└── level
debugging
└── stacktrace
nodeOptions
└── maxOldSpaceSize
└── maxSemiSpaceSize
└── exposeGC
javaOptions
└── Xmx
properties
└── hvigor.cacheDir
└── ohos.buildDir
└── enableSignTask
└── ohos.arkCompile.maxSize
└── hvigor.pool.cache.capacity
└── hvigor.pool.maxSize
└── ohos.pack.compressLevel
└── hvigor.analyzeHtml
└── hvigor.dependency.useNpm
└── ohos.compile.lib.entryfile
└── ohos.align.target
└── ohos.fallback.target
└── ohos.arkCompile.sourceMapDir
└── ohos.collect.debugSymbol
└── hvigor.enableMemoryCache
└── hvigor.memoryThreshold
└── ohos.nativeResolver
└── ohos.arkCompile.noEmitJs
└── ohos.arkCompile.singleFileEmit
└── ohos.sign.har
└── hvigor.keepDependency
└── ohos.arkCompile.emptyBundleName
└── ohos.uiTransform.Optimization
└── ohos.har.excludeHspDependencies
└── ohos.processLib.optimization
└── ohos.obfuscationRules.optimization
└── hvigor.incremental.optimization
└── hvigor.task.schedule.optimization
└── ohos.byteCodeHar.integratedOptimization
└── ohos.rollupCache.usePathPlaceholder
└── ohos.rollupCache.useSourceHash
└── ohos.arkCompile.writeRollupCache
└── ohos.align.deviceTypes
└── ohos.dependencies.types.enable
└── ohos.defaults.release.cmakebuildtype
└── ohos.defaults.autoLazyImport
└── hvigor.daemon.idleTimeout
parameterFile
```



#### 配置文件字段说明

hvigor-config.json5配置文件包含以下字段。



> [!NOTE] 说明
> 修改dependencies后，请根据界面提示，点击编辑器右上角Sync Now安装依赖。

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| modelVersion | 必选 | 字符串 | 开发态版本号。 默认版本号为DevEco Studio配套的modelVersion，以DevEco Studio 6.1.1 Release为例，配套的modelVersion为"6.1.1"。如需修改modelVersion，修改后的值不能小于5.0.0，且不能大于DevEco Studio配套的modelVersion。 |
| dependencies | 必选 | 对象 | 当前工程执行构建任务时，依赖的构建插件及版本，为npm源组件。 |
| execution | 可选 | 对象 | 执行构建的相关配置参数，仅在命令行场景下生效。 |
| logging | 可选 | 对象 | 日志相关配置参数。 |
| debugging | 可选 | 对象 | 调测相关配置参数。 |
| nodeOptions | 可选 | 对象 | Node相关配置参数。 |
| javaOptions | 可选 | 对象 | java相关配置参数。 |
| properties | 可选 | 对象 | 额外配置参数。 |
| parameterFile | 可选 | 字符串 | 自定义的参数化配置文件路径。 从DevEco Studio 6.0.2 Beta1版本开始支持。 |




#### execution

execution是执行构建的相关配置参数，除了optimizationStrategy字段外，其他字段仅在命令行构建场景下生效，如果通过DevEco Studio菜单栏构建，需要在**File > ****Settings**（macOS为**DevEco Studio > Preferences/Settings**）** > Build, Execution, Deployment > Build Tools > Hvigor**中设置。



> [!NOTE] 说明
> 更改模式后，首次编译会执行全量编译。

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| analyze | 可选 | 字符串/布尔值 | 构建分析模式。 normal（默认值）：普通模式，通过简单打点数据进行分析。原default模式已废弃。 advanced：进阶模式，通过更加详细的打点数据进行分析。如果需要更详细的任务耗时数据，请选择该模式。原verbose模式已废弃。 ultrafine：超精细化模式，与advanced模式相比，在ArkTS编译阶段记录更详细的打点数据，但开启后可能导致编译构建时间更长。从DevEco Studio 6.0.0 Beta1版本开始支持。 false：不启用构建分析。 |
| daemon | 可选 | 布尔值 | 是否启用守护进程编译。 true（缺省默认值）：启用。 false：不启用。 |
| incremental | 可选 | 布尔值 | 是否启用增量编译。 true（缺省默认值）：启用。 false：不启用。 |
| parallel | 可选 | 布尔值 | 是否启用并行编译。 true（缺省默认值）：启用。 false：不启用。 |
| typeCheck | 可选 | 布尔值 | 是否启用构建脚本hvigorfile.ts文件的类型检查，启用后构建效率可能会有所降低。 true：启用。 false（缺省默认值）：不启用。 |
| optimizationStrategy | 可选 | 字符串 | 指定构建模式。从DevEco Studio 5.1.1 Release版本开始支持。 performance：性能优先模式，可加快构建速度，但会占用更多内存。 memory（缺省默认值）：内存优先模式，可以减少编译内存占用。 |


execution字段示例：

```text
{
  "execution": {
    "analyze": "normal",
    "daemon": true,
    "incremental": true,
    "parallel": true,
    "typeCheck": false,
    "optimizationStrategy": "performance",
  }
}
```



#### logging

logging是日志相关配置参数。

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| level | 可选 | 字符串 | 构建时打印日志的级别。 debug：调测日志。 info（缺省默认值）：基本信息日志。 warn：告警日志。 error：错误日志。 |


logging字段示例：

```json
{
  "logging": {
    "level": "debug"
  }
}
```



#### debugging

debugging是调测相关配置参数。

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| stacktrace | 可选 | 布尔值 | 是否启用堆栈跟踪。 true：启用。 false（缺省默认值）：不启用。 |


debugging字段示例：

```json
{
  "debugging": {
    "stacktrace": true
  }
}
```



#### nodeOptions

nodeOptions是Node相关配置参数。

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| maxOldSpaceSize | 可选 | 整型数值 | 启用守护进程编译时，为守护进程设置最大的老生代内存大小，单位为MB，默认为8192MB。当工程代码量较大出现JS内存溢出时，可以调整该参数。 |
| maxSemiSpaceSize | 可选 | 整型数值 | 启用守护进程编译时，为守护进程设置新生代内存最大的半空间大小，单位为MB，默认为16MB。增加半空间大小可能会提高Node.js的吞吐量，但会消耗更多内存。 该字段从DevEco Studio 5.1.0 Release版本开始支持。 |
| exposeGC | 可选 | 布尔值 | 是否启用GC（Garbage Collection，内存回收），启用后会优化编译过程的峰值内存。 true（缺省默认值）：启用。 false：不启用。 |


nodeOptions字段示例：

```text
{
  "nodeOptions": {
    "maxOldSpaceSize": 8192,
    "maxSemiSpaceSize": 16,
    "exposeGC": true,
  }
}
```



#### javaOptions

javaOptions是java相关配置参数。

| 字段名称 | 可选/必选 | 类型 | 含义 |
| --- | --- | --- | --- |
| Xmx | 可选 | 整型数值 | 设置JVM最大堆内存，单位为MB，默认为512MB。 |


javaOptions字段示例：

```json
{
  "javaOptions": {
    "Xmx": 512
  }
}
```



#### properties

properties是额外配置参数。除了在hvigor-config.json5中配置properties外，还可以通过命令行参数-c或--config指定properties，命令行优先级比hvigor-config.json5更高，命令行配置方式请参考[命令行构建工具（hvigorw）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-commandline#section92386011817)。



> [!NOTE] 说明
> 如果配置为true，编译时不会做场景识别，即源码中任何符合语法规范的import语句都会被添加"lazy"。             仅支持Stage模型。             build-profile.json5文件中也可以通过autoLazyImport字段实现该能力，autoLazyImport的优先级比ohos.defaults.autoLazyImport更高。



> [!NOTE] 说明
> 模块级build-profile.json5文件中也可以通过arguments字段指定cmake构建类型，例如"arguments": "-DCMAKE_BUILD_TYPE=RelWithDebInfo"。arguments字段的优先级比ohos.defaults.release.cmakebuildtype更高。             在debug模式下构建时，该字段配置无效，默认使用Debug构建类型。



> [!NOTE] 说明
> 仅支持Stage模型。



> [!NOTE] 说明
> 该字段对字节码HAR不生效，字节码HAR产物的bundleName字段的值默认是变量。             预览时暂不支持配置该字段，字段默认取值为false。



> [!NOTE] 说明
> 仅支持在EntryAbility中使用loadContentByName加载首页，同时使用Navigation导航进行页面跳转时设置为true，否则会导致应用闪退。             预览时暂不支持配置该字段，字段默认取值为false。



> [!NOTE] 说明
> 配置该字段后，即使hvigor.enableMemoryCache配置为true，也不进行缓存。             该字段配置为很小的值时，构建任务会串行执行，等效于配置ohos.arkCompile.maxSize:1；配置为很大的值时，与不配置没有差异。



> [!NOTE] 说明
> 如果不配置，release模式时默认值为true，debug模式时默认值为false。             仅支持Stage模型。             nameCache文件仅在release模式下且开启混淆后才会生成，release模式下不开启混淆以及debug模式下均不生成这个文件。



> [!NOTE] 说明
> 从API 12开始支持。



> [!NOTE] 说明
> 同名的不同工程不可指定相同的存放位置。



> [!NOTE] 说明
> 同名的不同工程不可指定相同的存放位置。

表7 **properties字段说明                                         
字段名称

可选/必选

类型

含义

hvigor.cacheDir

可选

字符串

ohos.buildDir

可选

字符串

enableSignTask

可选

布尔值

是否启用HAP或HSP签名任务。

 - true（缺省默认值）：启用。
 - false：不启用。


ohos.arkCompile.maxSize

可选

整型数值

指定编译ArkTS线程的数量，默认为5。

hvigor.pool.cache.capacity

可选

整型数值

定义内存中缓存数据的容量，默认为4，数值越小，内存中缓存数据越少。配置为0，表示不启用内存缓存配置。

hvigor.pool.maxSize

可选

整型数值

指定编译过程中的线程数量，相比ohos.arkCompile.maxSize增加签名、打包等任务的线程。默认值为“工程的模块数”和“电脑虚拟核数-1”两者的较小值。

ohos.pack.compressLevel

可选

字符串

设置打包hap（压缩so）或app（压缩hap）时的压缩率等级。压缩率越高，压缩速度越慢。

 - fast（缺省默认值）：最低等级的压缩率，压缩速度最快。
 - standard：适中等级的压缩率，压缩速度适中。
 - ultimate：最高等级的压缩率，压缩速度最慢。


hvigor.analyzeHtml

可选

布尔值

是否生成构建可视化html文件。

 - true：生成构建可视化html文件。生成的html文件存放在工程的.hvigor/report目录下，该文件可直接在浏览器中打开。
 - false（缺省默认值）：不生成构建可视化html文件。


hvigor.dependency.useNpm

可选

布尔值

指定是否使用npm下载hvigor依赖。

若未配置该字段，当Node.js版本 ≥ 16时，默认使用pnpm下载依赖。在某些特定场景，可以通过配置该字段指定使用npm下载依赖。

 - true：对于任意Node版本，都使用npm下载依赖。
 - false（缺省默认值）：Node.js版本 ≥ 16时，使用pnpm下载依赖；Node.js版本 ＜ 16时，使用npm下载依赖。


ohos.compile.lib.entryfile

可选

布尔值

指定是否从入口文件开始编译：

 - true：表示从模块的入口文件开始编译，将编译入口文件及被引用的文件，没被引用的文件不会参与编译流程。
 - false（缺省默认值）：表示将src/main/ets下的ets和ts文件进行全量编译，涉及到以下场景：            1. 构建HSP时，存在于src/main/ets下的ets和ts文件都会被编译到产物中。

2. release模式对HAR混淆或构建字节码HAR时，存在于src/main/ets下的ets和ts文件都会被编译到产物中。

3. 构建HAP/HSP时，存在于动态依赖的HAR模块src/main/ets下的ets和ts文件都会被编译到产物中。


ohos.align.target

可选

字符串

指定本次构建任务所有涉及到的模块及其依赖的模块的target。详情请参考[多产物构建target](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products-guides#section7121513141619)。

ohos.fallback.target

可选

字符串数组

指定本次构建任务所有涉及到的模块及其依赖模块的fallback target，fallback target是一个特定优先级的target，各target的优先级顺序：align target > 命令行指定target > 被依赖的父模块target > fallback target > default target。详情请参考[多产物构建target](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products-guides#section7121513141619)。

ohos.arkCompile.sourceMapDir

可选

字符串

指定sourceMap文件的生成路径，方便开发者进行堆栈的回栈与错误信息的定位，当前仅支持Stage模型。若没有指定路径                                   
ohos.collect.debugSymbol

可选

布尔值

是否将[sourceMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle#section666114451518)、[nameCache](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle#section19215122372720)和带调试信息的so文件归档到产物路径下，根据选择的构建模式，如果是构建HAP/HSP/HAR，会归档到模块的build/{productName}/outputs/{targetName}/symbol的release或debug目录下；如果是构建APP，会将HAP/HSP模块的文件归档到工程的build/outputs/{productName}/symbol的release或debug目录下。

 - true：归档。                                   hvigor.enableMemoryCache

可选

布尔值

是否开启缓存，开启缓存会加快增量编译速度，关闭缓存能够节省内存占用，但是会增加增量编译时间。

  
true（缺省默认值）：开启。
 - false：不开启。


hvigor.memoryThreshold

可选

整型数值

内存管理阈值，单位为MB，当编译构建占用内存超过此阈值时，新加入的编译任务会等待，直到
