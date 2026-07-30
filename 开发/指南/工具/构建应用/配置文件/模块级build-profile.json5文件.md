# 模块级build-profile.json5文件

更新时间：2026-07-28 12:07:32

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile

**      


#### 配置文件结构

模块级build-profile.json5文件整体的结构如下。

```json
apiType
targets
└── name
└── runtimeOS
└── config
    └── distroFilter / distributionFilter
        └── apiVersion
            └── policy
            └── value
        └── screenShape
            └── policy
            └── value
        └── screenWindow
            └── policy
            └── value
        └── screenDensity
            └── policy
            └── value
        └── countryCode
            └── policy
            └── value
    └── deviceType
    └── buildOption
    └── atomicService
        └── preloads
            └── moduleName
└── source
    └── abilities
        └── name
        └── pages
        └── res
        └── icon
        └── label
        └── launchType
    └── pages
    └── sourceRoots
└── resource
    └── directories
└── output
    └── artifactName
showInServiceCenter
buildOption
buildOptionSet
└── name
└── debuggable
└── generateSharedTgz
└── copyFrom
└── resOptions
    └── compression
        └── media
            └── enable
        └── filters
            └── method
                └── type
                └── blocks
            └── files
                └── path
                └── size
                └── resolution
            └── exclude
                └── path
                └── size
                └── resolution
    └── resCompileThreads
    └── copyCodeResource
        └── enable
        └── includes
        └── excludes
    └── ignoreResourcePattern
    └── excludeHarRes
    └── includeAppScopeRes
    └── qualifiersConfig
        └── Mcc&Mnc
        └── Locale
        └── Orientation
        └── Device
        └── ColorMode
        └── Density
└── externalNativeOptions
    └── path
    └── abiFilters
    └── arguments
    └── cppFlags
    └── cFlags
    └── targets
└── sourceOption
    └── workers
└── nativeLib
    └── filter
        └── excludes
        └── pickFirsts
        └── pickLasts
        └── enableOverride
        └── select
            └── package
            └── version
            └── includePattern
            └── excludePattern
            └── include
            └── exclude
    └── debugSymbol
        └── strip
        └── exclude
    └── headerPath
    └── collectAllLibs
    └── excludeFromHar
    └── excludeSoFromInterfaceHar
    └── excludeSoFromBinXO
    └── librariesInfo
        └── name
        └── linkLibraries
    └── enableSoDirCollection
└── napiLibFilterOption
    └── excludes
    └── pickFirsts
    └── pickLasts
    └── enableOverride
└── arkOptions
    └── runtimeOnly
        └── sources
        └── packages
        └── excludePackages
    └── types  
    └── obfuscation
        └── ruleOptions
            └── enable
            └── files
        └── consumerFiles
    └── buildProfileFields
    └── integratedHsp
    └── transformLib
    └── branchElimination
    └── byteCodeHar
    └── bundledDependencies
    └── packSourceMap
    └── autoLazyImport
    └── autoLazyFilter
        └── include
        └── exclude
    └── reExportCheckMode
    └── skipOhModulesLint
    └── expandImportPath
        └── enable
        └── exclude
    └── widget
        └── transitiveDeps
    └── apPath
    └── hostPGO
└── packingOptions
    └── asset
        └── include
        └── exclude
    └── customizedOptions
        └── basePackage
└── removePermissions
    └── name
buildModeBinder
└── buildModeName
└── mappings
    └── targetName
    └── buildOptionName
entryModules
```



#### 配置文件字段说明

下表为"Ability"类型的Module（HAP）对应的模块级build-profile.json5中配置项包含的字段，"Library"类型的Module（HAR和HSP）对应的模块级build-profile.json5中配置项为下表罗列范围的子集。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| apiType | 字符串 | 可选 | API模型类型： stageMode：Stage模型，后续长期演进的模型，推荐使用该模型。 faMode：FA模型。 |
| targets | 对象数组 | 可选 | 定义的target，可配置多个；若配置，数组长度至少为1。 |
| showInServiceCenter | 布尔值 | 可选 | 是否显示在服务中心： true：显示。 false（缺省默认值）：不显示。 |
| buildOption | 对象 | 可选 | 模块在构建过程中的相关配置。 其中不支持配置name、debuggable和copyFrom字段。 在FA模型中，arkOptions配置中仅支持配置types字段。 |
| buildOptionSet | 对象数组 | 可选 | 表16buildOption的集合，其中name字段必填，每个配置都是当前支持的编译过程中所有可用工具的通用配置选项集。 |
| buildModeBinder | 对象数组 | 可选 | 构建模式（debug、release 等）与构建配置（buildOption）的关联配置。通过该配置可以将不同的构建配置和target进行组合，并绑定到对应的构建模式上，其中构建模式需要在工程级别的构建模式列表中已定义。 |
| entryModules | 字符串数组 | 可选 | Feature类型模块所关联的入口模块，仅对FA模型工程生效。 |




#### targets

targets用于给模块配置[多目标产物](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products)，可配置多个；若配置，数组长度至少为1。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | target名称。 |
| runtimeOS | 字符串 | 可选 | target的目标运行环境： HarmonyOS OpenHarmony |
| config | 对象 | 可选 | target相关配置。 |
| source | 对象 | 可选 | target的源码范围。 |
| resource | 对象 | 可选 | target包含的资源目录。 |
| output | 对象 | 可选 | 定制产品生成的应用包的配置。 |


            | 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| directories | 字符串数组 | 可选 | 资源目录地址。 |


            | 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| artifactName | 字符串 | 必选 | 自定义产品生成的应用包名称，可由数字、英文字母、中划线、下划线和英文句号（.）组成，支持输入版本号。 |


targets字段示例：

```json
"targets": [
  {
    "name": "default",
    "resource": {
      "directories": ["./src/main/resources"]
    },
    "output": {
      "artifactName": "customizedTargetOutputName-1.0.0"
    }
  }
]
```



#### config

config是target相关配置。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| distroFilter | 对象 | 可选 | 应用市场分发规则。在FA模型中使用。 |
| distributionFilter | 对象 | 可选 | 应用市场分发规则。在Stage模型中使用。 |
| deviceType | 字符串数组 | 可选 | target支持的设备类型，必须在module.json5中已定义。 在FA模型中，对应的文件为config.json。 |
| buildOption | 对象 | 可选 | 模块在构建过程中的相关配置。 其中不支持配置name、debuggable和copyFrom字段。 |
| atomicService | 对象 | 可选 | 元服务相关配置，仅支持在Stage模型中配置。 |




#### source

source用于指定target的源码范围。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| abilities | 对象数组 | 可选 | 自定义target的能力范围。 在FA模型工程中支持对Ability源码目录下的page页面进行定制。 |
| pages | 字符串数组 | 可选 | Stage模型工程中支持对pages源码目录的page页面进行定制，数组长度至少为1。 |
| sourceRoots | 字符串数组 | 可选 | Stage模型工程中支持对差异化代码空间进行定制，数组长度至少为1。数组中的值有以下限制： 必须唯一； 必须为相对路径； 类型必须为文件夹； 文件夹必须真实存在； 文件夹必须与src/main同级； 当数组中存在多个值时，寻址的优先级为数组中值的顺序。 |


source字段示例：

```text
"targets": [
  {
    "name": "default",
    "source": {
       "pages": [         // Stage模型
        "pages/Index"
      ],
      "abilities": [     // FA模型
        {
          "name": ".MainAbility",
          "pages": [
            "pages/index"
          ]
        }
      ],
      "sourceRoots": [
        "./src/default"
      ]
    }
  }
]
```



#### distroFilter/distributionFilter

distroFilter/distributionFilter用于指定应用市场分发规则，distroFilter在FA模型中使用，distributionFilter在Stage模型中使用。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| apiVersion | 对象 | 可选 | 支持的apiVersion范围。 |
| screenShape | 对象 | 可选 | 屏幕形状的支持策略。 |
| screenWindow | 对象 | 可选 | 应用运行时窗口的分辨率支持策略。 |
| screenDensity | 对象 | 可选 | 屏幕的像素密度支持策略。 |
| countryCode | 对象 | 可选 | 应用需要分发的国家地区码。 |




#### apiVersion

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| policy | 字符串 | 必选 | 取值规则： include：需要包含的value属性。 exclude：需要排除的value属性。 |
| value | 整型数组 | 必选 | 支持的取值为API Version存在的整数值，例如10。 |




#### screenShape

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| policy | 字符串 | 必选 | 取值规则： include：需要包含的value属性。 exclude：需要排除的value属性。 |
| value | 字符串数组 | 必选 | 支持的取值范围： circle：圆形 rect：矩形 |




#### screenWindow

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| policy | 字符串 | 必选 | 当前取值仅支持“include”。 include：需要包含的value属性。 |
| value | 字符串数组 | 必选 | 单个字符串的取值格式为“宽*高”，取值为整数像素值，例如"454*454"。 |




#### screenDensity

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| policy | 字符串 | 必选 | 取值规则： include：需要包含的value属性。 exclude：需要排除的value属性。 |
| value | 字符串数组 | 必选 | 取值范围： sdpi：小规模的屏幕密度（Small-scale Dots per Inch），适用于dpi取值为(0,120]的设备。 mdpi：中规模的屏幕密度（Medium-scale Dots Per Inch），适用于dpi取值为(120,160]的设备。 ldpi：大规模的屏幕密度（Large-scale Dots Per Inch），适用于dpi取值为(160,240]的设备。 xldpi：大规模的屏幕密度（Extra Large-scale Dots Per Inch），适用于dpi取值为(240,320]的设备。 xxldpi：大规模的屏幕密度（Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(320，480]的设备。 xxxldpi：表示大规模的屏幕密度（Extra Extra Extra Large-scale Dots Per Inch），适用于dpi取值为(480, 640]的设备。 |




#### countryCode

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| policy | 字符串 | 必选 | 取值规则： include：需要包含的value属性。 exclude：需要排除的value属性。 |
| value | 字符串数组 | 必选 | 国家地区码取值，具体值以ISO-3166-1标准为准。支持多个国家和地区枚举定义。 |


distroFilter/distributionFilter字段示例：

```json
"targets": [
  {
    "name": "default",
    "config": {
      "distributionFilter": {
        "apiVersion": {
          "policy": "include",
          "value": [12]
        },
        "screenShape": {
          "policy": "include",
          "value": [
            "circle",
            "rect"
          ]
        },
        "screenWindow": {
          "policy": "include",
          "value": [
            "454*454",
            "466*466"
          ]
        },
        "screenDensity": {
          "policy": "exclude",
          "value": [
            "ldpi",
            "xldpi"
          ]
        },
        "countryCode": {
          "policy": "include",
          "value": [
            "CN"
          ]
        }
      }
    },
  }
]
```



#### atomicService

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| preloads | 对象数组 | 可选 | 定义当前模块运行时预加载的模块。 |


| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| moduleName | 字符串 | 可选 | 预加载的模块名称。 |


atomicService字段示例：

```json
"targets": [
  {
    "name": "default",
    "config": {
      "atomicService": {
        "preloads": [
          {
            "moduleName": "preloadSharedLibrary"
          }
        ]
      }
    }
  }
]
```



#### abilities

abilities用于自定义target的能力范围。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 指定target选择的ability的名称。 |
| pages | 字符串数组 | 可选 | FA模型中，指定target选择的ability的page。 |
| res | 字符串数组 | 可选 | 指定资源目录。 |
| icon | 字符串 | 可选 | 指定ability图标文件的索引，格式为"$media:ability_icon"。 |
| label | 字符串 | 可选 | 指定对用户可见的名称，要求采用该名称的资源索引，以支持多语言。 |
| launchType | 字符串 | 可选 | 指定ability的启动模式： multiton：多实例模式，每次启动创建一个新实例。 standard：同multiton，建议使用multiton替代。 singleton（缺省默认值）：单实例模式，仅第一次启动创建新实例。 specified：指定实例模式，运行时由开发者决定是否创建新实例。 |


abilities字段示例：

```json
"targets": [
  {
    "name": "default",
    "source": {
      "abilities": [
        {
          "name": "EntryAbility",
          "icon": "$media:layered_image",
          "label": "$string:EntryAbility_label",
          "launchType": "singleton"
        }
      ]
    }
  }
]
```



#### buildOption

buildOption是模块在构建过程中的相关配置，buildOptionSet和targets中也支持配置buildOption。此外，工程级build-profile.json5中也支持配置buildOption。工程级别buildOption配置会与模块级别的buildOption进行合并，具体合并规则和优先级请参考[合并编译选项规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-compilation-options-customizing-guide#section1727865610255)。



> [!NOTE] 说明
> 该字段配置后仅对HSP模块生效。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 可选 | 构建配置方案buildOption的名称。 |
| debuggable | 布尔值 | 可选 | 当前编译产物是否为可调试模式(debug)： true：可调试。 false：不可调试。 如果未配置debuggable字段，使用release的编译模式时，默认值为false，使用其他编译模式时，默认值为true。 |
| generateSharedTgz | 布尔值 | 可选 | 编译HSP模块时是否生成tgz包。 true：生成。 false：不生成。 如果未配置generateSharedTgz，根据debuggable字段决定是否生成tgz包。debuggable为true时，不生成tgz包，debuggable为false时，生成tgz包。 从DevEco Studio 5.1.1 Beta1版本开始支持。 |
| copyFrom | 字符串 | 可选 | 配置已定义的buildOption的name，表示从本模块已有的buildOption复制配置。 |
| resOptions | 对象 | 可选 | 资源编译配置项。 |
| externalNativeOptions | 对象 | 可选 | Native编译配置项。 |
| sourceOption | 对象 | 可选 | 源码相关配置。使用不同的标签对源代码进行分类，以便在构建过程中对不同的源代码进行不同的处理。 |
| nativeLib | 对象 | 可选 | Native 库（.so）相关配置。 |
| napiLibFilterOption | 对象 | 可选 | NAPI库（.so）文件的筛选选项。标记为废弃，不建议使用，推荐使用nativeLib/filter。 |
| arkOptions | 对象 | 可选 | ArkTS编译配置。 |
| packingOptions | 对象 | 可选 | 打包配置项，仅支持HAR模块。 |
| removePermissions | 对象数组 | 可选 | 指定编译时需要删除的依赖包中的冗余权限，模块本身的权限不会被删除，仅HAP/HSP模块支持配置。 |




#### resOptions

resOptions是资源编译配置项。



> [!NOTE] 说明
> qualifiersConfig不能为{}，至少配置一类限定词。             如果配置了限定词，取值不能为空数组[]，数组中的值不能为空字符串""。             仅支持Stage模型。



> [!NOTE] 说明
> 该字段仅对HSP模块生效。             配置为false后，app.json5的icon和label字段不再对HSP模块生效。



> [!NOTE] 说明
> 仅支持在HAP/HSP中配置。



> [!NOTE] 说明
> 如果规则中带有路径（例如./src/main/a.png），该规则不生效。             如果未配置该字段，打包HAP/HSP时存在默认的过滤规则：默认不打包.git、.svn、.scc、.ds_store、desktop.ini、picasa.ini、cvs、thumbs.db以及以.开头的隐藏文件/目录和以~结尾的文件。             配置该字段后，会覆盖默认的过滤规则；如果字段配置为空数组，则不应用任何过滤规则，即全部资源都打包。



> [!NOTE] 说明
> 该字段对不开启混淆的源码HAR不生效。

表17 **resOptions                                         
字段名称

类型

可选/必选

含义

[compression](#section2095319147103)

对象

可选

对工程预置图片资源进行纹理压缩的编译配置参数。

resCompileThreads

整型数值

可选

资源编译的线程数量 ，最小为1，最大为主机的CPU核数。

该字段从DevEco Studio 5.1.0 Release版本开始支持。

[copyCodeResource](#table1476161719356)

对象

可选

对模块的src/mai    

#### arkOptions

arkOptions是ArkTS编译配置。



> [!NOTE] 说明
> API 11及以上版本不再支持，即该字段配置后不再生效。



> [!NOTE] 说明
> HAR模块不支持配置。



> [!NOTE] 说明
> 如果配置为true，编译时不会做场景识别，即源码中任何符合语法规范的import语句都会被添加"lazy"。             仅支持Stage模型。



> [!NOTE] 说明
> 如果不配置，debug模式默认值为true，release模式默认值为false。             将sourceMap打包到release的HAR包中，可能会导致HAR中的代码资产泄露。



> [!NOTE] 说明
> 仅支持字节码HAR配置该字段。             从API 12开始支持。             仅支持Stage模型。



> [!NOTE] 说明
> 从API 12开始支持。             从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，当工程级build-profile.json5中useNormalizedOHMUrl配置为true时，byteCodeHar缺省默认值为true；当useNormalizedOHMUrl配置为false时，byteCodeHar缺省默认值为false。



> [!NOTE] 说明
> 仅支持API 11及以上的Stage模型。             HAR模块仅字节码HAR配置生效，非字节码HAR配置不生效。             仅支持const声明的bool类型常量和const声明的string/number类型常量的判断表达式。             不支持间接导入，例如A文件中定义const变量A1，B文件导入A1，导出B1，ets导入B1进行判断，无法进行裁剪。



> [!NOTE] 说明
> Mac环境下添加配置后插桩未生效的问题请参考FAQ。             HAR模块仅字节码HAR配置生效，非字节码HAR配置不生效。



> [!NOTE] 说明
> 从API 12开始支持。             需在工程级build-profile.json5中配置useNormalizedOHMUrl为true后使用。             该字段仅在HSP模块中配置后生效。

**表22 **arkOptions                                         
字段名称

类型

可选/必选

含义

[runtimeOnly](#table19892123422118)

对象

可选

配置变量动态import的文件和依赖的包名，仅支持在Stage模型中配置。

runtimeOnly为非必选配置，当工程需要以变量方式动态import文件、目录的相对路径或三方包时，需要通过配置runtimeOnly来确保其加入编译流程。详情请参考[动态import变量表达式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dynamic-import#动态import变量表达式)。

[types](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkoptions-guide#types)

字符串数组

可选

自定义类型，可配置包名或d.ts/d.ets文件路径。

[obfuscation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-obfuscation)

对象

可选

代码混淆配置。

[buildProfileFields](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para)

对象

可选

运行时可获取的自定义构建参数，支持键值对配置，key可由数字、英文、下划线、中划线组成，value类型仅支持string、number、boolean。

integratedHsp

布尔值

可选

是否为[集成态HSP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/integrated-hsp)。


[transformLib](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/customize-bytecode-during-compilation)

字符串

可选

字节码插桩插件配置，允许开发者在编译时对字节码进行插桩修改，仅支持Stage模型，格式为相对路径，不同系统要求的文件类型如下，文件内容需要在对应平台生成，不能拷贝修改后缀名混用。

 - Windows                                   branchElimination

布尔值

可选

是否启用代码分支裁剪，减少编译产物大小，开启后，在release编译模式下，不会被执行到的代码分支会被裁剪掉，示例请参考[branchElimination示例](#li71611425123512)。

  
true：启用（将导致使用"ApplyChanges"功能时，对const声明的常量的值进行的修改可能不生效）。                                   byteCodeHar

布尔值

可选

是否构建字节码HAR，仅在HAR模块中配置后生效。详情请参考[构建字节码HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har#section16598338112415)。

  
true：支持。
