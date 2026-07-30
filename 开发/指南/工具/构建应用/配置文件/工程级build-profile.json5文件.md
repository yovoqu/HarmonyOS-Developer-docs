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
<span style="color: rgb(48,48,48);">    └── signingConfig</span>
<span style="color: rgb(48,48,48);">    └── bundleName</span>
<span style="color: rgb(48,48,48);">    └── buildOption</span>
<span style="color: rgb(48,48,48);">        └── packOptions</span>
<span style="color: rgb(48,48,48);">            └── buildAppSkipSignHap</span>
<span style="color: rgb(48,48,48);">            └── </span>fastBuildApp
<span style="color: rgb(48,48,48);">            └── </span>enableSourceCodeCheck
<span style="color: rgb(48,48,48);">            └── </span>deduplicateHar
<span style="color: rgb(48,48,48);">            └── </span>appWithSignedPkg
<span style="color: rgb(48,48,48);">            └── </span>enableIncrementalSoCompress
<span style="color: rgb(48,48,48);">        └── debuggable</span>
        <span style="color: rgb(48,48,48);">└── </span>generateSharedTgz
<span style="color: rgb(48,48,48);">        └── resOptions</span>
<span style="color: rgb(48,48,48);">            └── </span>compression
<span style="color: rgb(48,48,48);">                └── </span>media
<span style="color: rgb(48,48,48);">                    └──</span> enable
<span style="color: rgb(48,48,48);">                └── </span>filters
<span style="color: rgb(48,48,48);">                    └──</span> method
<span style="color: rgb(48,48,48);">                        └──</span> type
<span style="color: rgb(48,48,48);">                        └──</span> blocks
<span style="color: rgb(48,48,48);">                    └──</span> files
<span style="color: rgb(48,48,48);">                        └──</span> path
<span style="color: rgb(48,48,48);">                        └──</span> size
<span style="color: rgb(48,48,48);">                        └──</span> resolution
<span style="color: rgb(48,48,48);">                    └──</span> exclude
<span style="color: rgb(48,48,48);">                        └──</span> path
<span style="color: rgb(48,48,48);">                        └──</span> size
<span style="color: rgb(48,48,48);">                        └──</span> resolution
<span style="color: rgb(48,48,48);">            └── </span>resCompileThreads
<span style="color: rgb(48,48,48);">            └── </span>copyCodeResource
<span style="color: rgb(48,48,48);">                └── </span>enable
<span style="color: rgb(48,48,48);">                └── </span>includes
<span style="color: rgb(48,48,48);">                └── </span>excludes
            <span style="color: rgb(48,48,48);">└── </span>ignoreResourcePattern
            <span style="color: rgb(48,48,48);">└── </span>excludeHarRes
            <span style="color: rgb(48,48,48);">└── </span>includeAppScopeRes
            <span style="color: rgb(48,48,48);">└── </span>idDefinedFilePath
<span style="color: rgb(48,48,48);">        └── externalNativeOptions</span>
<span style="color: rgb(48,48,48);">            └── path</span>
<span style="color: rgb(48,48,48);">            └── abiFilters</span>
<span style="color: rgb(48,48,48);">            └── arguments</span>
<span style="color: rgb(48,48,48);">            └── cppFlags</span>
<span style="color: rgb(48,48,48);">        └── sourceOption</span>
<span style="color: rgb(48,48,48);">            └── workers</span>
        └── nativeLib
<span style="color: rgb(48,48,48);">            └── </span>filter
<span style="color: rgb(48,48,48);">                └── </span>excludes
<span style="color: rgb(48,48,48);">                └── </span>pickFirsts
<span style="color: rgb(48,48,48);">                └── </span>pickLasts
<span style="color: rgb(48,48,48);">                └── </span>enableOverride
<span style="color: rgb(48,48,48);">                └── </span>select
<span style="color: rgb(48,48,48);">                    └──</span> package
<span style="color: rgb(48,48,48);">                    └──</span> version
<span style="color: rgb(48,48,48);">                    └──</span> includePattern
<span style="color: rgb(48,48,48);">                    └──</span> excludePattern
<span style="color: rgb(48,48,48);">                    └──</span> include
<span style="color: rgb(48,48,48);">                    └──</span> exclude
<span style="color: rgb(48,48,48);">            └── </span>debugSymbol
<span style="color: rgb(48,48,48);">                └── </span>strip
<span style="color: rgb(48,48,48);">                └── </span>exclude
<span style="color: rgb(48,48,48);">            └── </span>headerPath
<span style="color: rgb(48,48,48);">            └── </span>collectAllLibs
<span style="color: rgb(48,48,48);">            └── </span>excludeFromHar
<span style="color: rgb(48,48,48);">            └── </span>excludeSoFromInterfaceHar
<span style="color: rgb(48,48,48);">            └── </span>excludeSoFromBinXO
<span style="color: rgb(48,48,48);">        └── napiLibFilterOption</span>
<span style="color: rgb(48,48,48);">            └── excludes</span>
<span style="color: rgb(48,48,48);">            └── pickFirsts</span>
<span style="color: rgb(48,48,48);">            └── pickLasts</span>
<span style="color: rgb(48,48,48);">            └── enableOverride</span>
<span style="color: rgb(48,48,48);">        └── arkOptions</span>
<span style="color: rgb(48,48,48);">            └── </span>buildProfileFields
<span style="color: rgb(48,48,48);">            └── types</span>
<span style="color: rgb(48,48,48);">            └── </span>tscConfig
<span style="color: rgb(48,48,48);">                └── </span>targetESVersion
<span style="color: rgb(48,48,48);">                └── </span>maxFlowDepth
<span style="color: rgb(48,48,48);">                └── </span>tsImportSoCheck
<span style="color: rgb(48,48,48);">            └── </span>autoLazyImport
<span style="color: rgb(48,48,48);">            └── </span>autoLazyFilter
<span style="color: rgb(48,48,48);">                └── </span>include
<span style="color: rgb(48,48,48);">                └── </span>exclude
<span style="color: rgb(48,48,48);">            └── </span>reExportCheckMode
<span style="color: rgb(48,48,48);">            └── </span>branchElimination
<span style="color: rgb(48,48,48);">            └── </span>skipOhModulesLint
<span style="color: rgb(48,48,48);">            └── </span>expandImportPath
<span style="color: rgb(48,48,48);">                └── </span>enable
<span style="color: rgb(48,48,48);">                └── </span>exclude
<span style="color: rgb(48,48,48);">            └── apPath</span>
<span style="color: rgb(48,48,48);">            └── hostPGO</span>
        └── strictMode
<span style="color: rgb(48,48,48);">            └── </span>noExternalImportByPath
<span style="color: rgb(48,48,48);">            └── </span>useNormalizedOHMUrl
<span style="color: rgb(48,48,48);">            └── </span>caseSensitiveCheck
<span style="color: rgb(48,48,48);">            └── </span>duplicateDependencyCheck
<span style="color: rgb(48,48,48);">            └── </span>harLocalDependencyCheck
<span style="color: rgb(48,48,48);">            └── </span>enableStrictCheckOHModule
<span style="color: rgb(48,48,48);">            └── </span>disableStrictCheckPaths
<span style="color: rgb(48,48,48);">            └── </span>disableSendableCheckRules
<span style="color: rgb(48,48,48);">            └── </span>strictCheckerOnly
<span style="color: rgb(48,48,48);">            └── </span>apiCompatibilityCheck
        └── nativeCompiler
        └── removePermissions
<span style="color: rgb(48,48,48);">            └── </span>name
        └── preloadSystemSo
<span style="color: rgb(48,48,48);">    └── runtimeOS</span>
    └── arkTSVersion
<span style="color: rgb(48,48,48);">    └── compileSdkVersion</span>
<span style="color: rgb(48,48,48);">    └── compatibleSdkVersion</span>
<span style="color: rgb(48,48,48);">    └── targetSdkVersion</span>
<span style="color: rgb(48,48,48);">    └── </span>compatibleSdkVersionStage
<span style="color: rgb(48,48,48);">    └── bundleType</span>
<span style="color: rgb(48,48,48);">    └── label</span>
<span style="color: rgb(48,48,48);">    └── icon</span>
<span style="color: rgb(48,48,48);">    └── versionCode</span>
<span style="color: rgb(48,48,48);">    └── versionName</span>
<span style="color: rgb(48,48,48);">    └── </span>buildVersion
<span style="color: rgb(48,48,48);">    └── resource</span>
        └── directories
    └── output
        └── artifactName
    └── vendor
└── buildModeSet
    └── name
<span style="color: rgb(48,48,48);">    └── buildOption</span>
<span style="color: rgb(48,48,48);">└── multiProjects</span>
<span style="color: rgb(48,48,48);">└── </span>capabilities
    └── bundleName
    └── config
        └── name
        └── capability
        └── subCapabilities
            └── name
            └── capability
modules
<span style="color: rgb(48,48,48);">└── name</span>
<span style="color: rgb(48,48,48);">└── srcPath</span>
<span style="color: rgb(48,48,48);">└── targets</span>
<span style="color: rgb(48,48,48);">    └── </span><span style="color: rgb(48,48,48);">name</span>
<span style="color: rgb(48,48,48);">    └── applyToProducts</span>
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
