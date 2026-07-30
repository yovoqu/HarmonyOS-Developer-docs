# 工程级build-profile.json5文件

更新时间：2026-07-28 12:07:32

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile-app

**      


#### 配置文件结构

工程级build-profile.json5文件整体的结构如下。

```json
app
└── signingConfigs
    └── name
    └── material
        └── storePassword
        └── certpath
        └── keyAlias
        └── keyPassword
        └── profile
        └── signAlg
        └── storeFile
    └── type
└── products
    └── name
    └── signingConfig
    └── bundleName
    └── buildOption
        └── packOptions
            └── buildAppSkipSignHap
            └── fastBuildApp
            └── enableSourceCodeCheck
            └── deduplicateHar
            └── appWithSignedPkg
            └── enableIncrementalSoCompress
        └── debuggable
        └── generateSharedTgz
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
            └── idDefinedFilePath
        └── externalNativeOptions
            └── path
            └── abiFilters
            └── arguments
            └── cppFlags
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
        └── napiLibFilterOption
            └── excludes
            └── pickFirsts
            └── pickLasts
            └── enableOverride
        └── arkOptions
            └── buildProfileFields
            └── types
            └── tscConfig
                └── targetESVersion
                └── maxFlowDepth
                └── tsImportSoCheck
            └── autoLazyImport
            └── autoLazyFilter
                └── include
                └── exclude
            └── reExportCheckMode
            └── branchElimination
            └── skipOhModulesLint
            └── expandImportPath
                └── enable
                └── exclude
            └── apPath
            └── hostPGO
        └── strictMode
            └── noExternalImportByPath
            └── useNormalizedOHMUrl
            └── caseSensitiveCheck
            └── duplicateDependencyCheck
            └── harLocalDependencyCheck
            └── enableStrictCheckOHModule
            └── disableStrictCheckPaths
            └── disableSendableCheckRules
            └── strictCheckerOnly
            └── apiCompatibilityCheck
        └── nativeCompiler
        └── removePermissions
            └── name
        └── preloadSystemSo
    └── runtimeOS
    └── arkTSVersion
    └── compileSdkVersion
    └── compatibleSdkVersion
    └── targetSdkVersion
    └── compatibleSdkVersionStage
    └── bundleType
    └── label
    └── icon
    └── versionCode
    └── versionName
    └── buildVersion
    └── resource
        └── directories
    └── output
        └── artifactName
    └── vendor
└── buildModeSet
    └── name
    └── buildOption
└── multiProjects
└── capabilities
    └── bundleName
    └── config
        └── name
        └── capability
        └── subCapabilities
            └── name
            └── capability
modules
└── name
└── srcPath
└── targets
    └── name
    └── applyToProducts
```



#### 配置文件字段说明

工程级build-profile.json5文件包含以下字段。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| app | 对象 | 必选 | 编译配置信息。 |
| modules | 对象数组 | 必选 | 工程中包含的所有模块的信息，数组长度至少为1。 |




#### app

app是工程级的编译配置，包含签名、product等信息。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| signingConfigs | 对象数组 | 可选 | 签名方案信息，可配置多个。 |
| products | 对象数组 | 可选 | 产品品类，可配置多个。如需配置多个，相关说明请参见配置多目标产物章节。 |
| buildModeSet | 对象数组 | 可选 | 构建模式集合，可配置多个。 |
| multiProjects | 布尔值 | 可选 | 当前工程是否支持多工程构建： true：支持。 false（缺省默认值）：不支持。 |
| capabilities | 对象数组 | 可选 | 应用开通的开放能力，具体开通方式请参考关联注册应用进行签名。 从DevEco Studio 6.0.0 Beta5版本开始支持。 |




#### modules

modules是一个对象数组，用于描述工程中包含的所有模块，数组长度至少为1。模块配置包括名称、路径和target-product关联配置。



> [!NOTE] 说明
> 当前支持引用其他工程下的HAR和HSP模块。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 模块的名称。该名称需与module.json5文件中的module.name保持一致。 在FA模型中，对应的文件为config.json。 |
| srcPath | 字符串 | 必选 | 模块的源码路径，为模块根目录相对工程根目录的相对路径，允许模块根目录不在当前工程下，详情请参考导入/引用模块。 |
| targets | 对象数组 | 可选 | 模块的target信息，用于定制多目标构建产物时，配置模块target和应用product之间的关联关系。HAR模块无需配置。 |


            | 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | target名称，在各个模块级build-profile.json5中的targets字段定义。 |
| applyToProducts | 字符串数组 | 可选 | target关联的product。HAR模块无需配置。 |


modules字段示例：

```json
{
  "modules": [
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": [
        {
          "name": "default",
          "applyToProducts": [  
            "default"    // 表示将该模块下的"default" Target打包到"default" Product中
          ]
        }
      ]
    }
  ]
}
```



#### signingConfigs

signingConfigs是一个对象数组，用于配置签名方案，可配置多个。

| 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| name | 字符串 | 必选 | 签名方案的名称，仅支持数字和字母，长度为1~64个字符。 |
| material | 对象 | 必选 | 签名方案相关材料，如密码、证书等。 通过File > Project Structure... > Project > Signing Configs界面，进行自动签名后，material节点中的各配置项会自动填充。 |
| type | 字符串 | 可选 | 签名类型： HarmonyOS OpenHarmony |


            | 字段名称 | 类型 | 可选/必选 | 含义 |
| --- | --- | --- | --- |
| storePassword | 字符串 | 必选 | 密钥库密码，以密文形式呈现。 |
| certpath | 字符串 | 必选 | 调试或发布证书文件地址，文件后缀为.cer，支持绝对路径和相对路径，相对路径以工程根目录为起点。 |
| keyAlias | 字符串 | 必选 | 密钥别名信息。 |
| keyPassword | 字符串 | 必选 | 密钥密码，以密文形式呈现。 |
| profile | 字符串 | 必选 | 调试或发布证书Profile文件地址，文件后缀为.p7b，支持绝对路径和相对路径，相对路径以工程根目录为起点。 |
| signAlg | 字符串 | 必选 | 密钥库signAlg参数。当前可配置值SHA256withECDSA。 |
| storeFile | 字符串 | 必选 | 密钥库文件地址，文件后缀为.p12，支持绝对路径和相对路径，相对路径以工程根目录为起点。 |


signingConfigs字段示例：

```json
// 使用绝对路径
{
  "app": { 
    "signingConfigs": [
      {
        "name": "default",
        "type": "HarmonyOS",
        "material": {  
          "certpath": "D:\\SigningConfig\\debug_hos.cer",
          "storePassword": "************************************",  // 密文形式的密钥库密码
          "keyAlias": "debugKey",
          "keyPassword": "************************************",  // 密文形式的密钥密码
          "profile": "D:\\SigningConfig\\debug_hos.p7b", 
          "signAlg": "SHA256withECDSA",
          "storeFile": "D:\\SigningConfig\\debug_hos.p12"
        }
      }
    ]
  }
}
// 使用相对路径
{
  "app": { 
    "signingConfigs": [
      {
        "name": "default",
        "type": "HarmonyOS",
        "material": {  
          "certpath": "./SigningConfig/debug_hos.cer",
          "storePassword": "************************************",  // 密文形式的密钥库密码
          "keyAlias": "debugKey",
          "keyPassword": "************************************",  // 密文形式的密钥密码
          "profile": "./SigningConfig/debug_hos.p7b", 
          "signAlg": "SHA256withECDSA",
          "storeFile": "./SigningConfig/debug_hos.p12"
        }
      }
    ]
  }
}
```



#### products

products是一个对象数组，用于配置产品品类信息，可配置多个，如通用默认版、付费版、免费版等。如需配置多个，相关说明请参见[配置多目标产物](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products)章节。



> [!NOTE] 说明
> 配置products中的label、icon、versionCode、versionName、resource字段后，编译构建时将根据此处的配置替换app.json5中的相关配置，常用于应用和元服务可分可合构建打包场景。



> [!NOTE] 说明
> 配置betaX就能生成在对应betaX版本镜像上运行的应用，但是无法使用高于betaX版本的特性，例如在API 12中beta3版本提供的sendable function和lazy import两个特性在配置beta2或beta1时无法正常使用。



> [!NOTE] 说明
> 运行环境是HarmonyOS时，该字段不需要显性配置，编译时默认使用DevEco Studio内置的SDK版本。如果配置，只能配置为当前DevEco Studio配套的SDK版本，不允许配置为其他SDK版本。             运行环境是OpenHarmony时，必须配置该字段。



> [!NOTE] 说明
> 建议配置该字段。             构建APP包时，打包工具会对HSP和HAP的targetSdkVersion字段进行校验，满足条件的才能打包，具体请参考打包工具。



> [!NOTE] 说明
> 构建APP包时，打包工具会对HSP和HAP的compatibleSdkVersion字段进行校验，满足条件的才能打包，具体请参考打包工具。

表7 **products                                         
字段名称

类型

可选/必选

含义

name

字符串

必选

产品的名称，必须存在name为"default"的product。

signingConfig

字符串

可选

当前产品品类的签名方案名称，需要在[signingConfigs.name](#section153288223224)中定义。如果没有配置，默认不签名。

compatibleSdkVersion

字符串/数值

必选

标识应用/元服务运行所需兼容的最低SDK版本，应用/元服务不能安装在低于该版本的设备。当前支持的版本参考[所有HarmonyOS版本](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-allversion)。相关字段与应用兼容性关系参见[应用兼容性说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/app-compatibility)。

从API 26.0.0开始，HarmonyOS和OpenHarmony配置统一，字段类型是字符串，配置示例："compatibleSdkVersion": "26.0.0"。

API 26.0.0之前的版本：

 - 运行环境是HarmonyOS时，字段类型是字符串，配置示例："compatibleSdkVersion": "6.1.1(24)"。
运行环境是OpenHarmony时，字段类型是数值，配置示例："compatibleSd
