# ohpm convert

更新时间：2026-07-15 09:00:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-convert

将npm三方库转换为ohpm三方库。因为语法差异，转换时仅对文件进行格式转换，不修改原npm包的代码逻辑。若HAR包在转换后出现代码不兼容的报错，开发者需修改原npm包的代码做适配。
 

#### 命令格式

```text
ohpm convert [[<@group>/]<pkg>[@<version> | @tag:<tag>]] --registry <string> [--publish]
ohpm convert <node_modules_path> [--publish]
```
 
> [!NOTE]
> @group：三方库的命名空间，可选。 pkg：三方库名称，必选。 version：三方库的版本号，可选。 tag：三方库的标签，标签会标记三方库的某个版本号，可选。

 
 

#### 功能描述

将指定npm仓库中的某个包或者本地node_modules目录下的包转换成满足ohpm格式要求的HAR包，并保存至当前工作目录，转换后的包将支持上传至ohpm-repo私仓或OpenHarmony三方库中心仓。
 
- ohpm convert @group/pkg@version --registry &lt;npm仓库地址&gt;

  下载指定仓库中的某个包及其所有依赖项，并且将该包及其依赖转换为满足ohpm格式要求的HAR包。
- ohpm convert &lt;node_modules_path&gt;

  转换本地node_modules中的所有包为满足ohpm格式要求的HAR包，&lt;node_modules_path&gt;必须为npm执行install命令后生成的node_modules目录。

  示例：

  
```text
ohpm convert ./xxxx/node_modules
```


 
 
> [!TIP]
> ohpm convert命令仅保留npm包中package.json配置文件中的name、version、main、types、license、description、author、keywords、homepage、repository、artifactType、dependencies、devDependencies、dynamicDependencies、overrides、scripts、hooks，module、packageType、typesVersions、exports和jsnext:main字段，具体字段说明请参考 oh-package.json5 字段说明 。

 

#### Options

 

#### registry

- 默认值：无
- 类型：URL

 
可以在convert命令后面配置 --registry &lt;registry&gt; 参数，指定仓库地址。如果指定了--registry，convert命令将从远程仓库地址下载指定的包及其依赖后，进行转换处理。如果没有指定--registry，convert命令将从本地node_modules目录进行转换处理。
 
 

#### publish

- 默认值：false
- 类型：Boolean

 
可以在 convert命令后面配置 --publish 参数 ，若指定该参数，执行convert命令前请确认.ohpmrc推包相关配置无误，当所有包转换完成后将根据.ohpmrc中的配置依次进行推包。
 
 

#### log_level

- 默认值：无
- 类型：String

 
从ohpm 6.0.2.636版本开始，可以在convert命令后配置--log_level &lt;string&gt;参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log_level的级别。
 
 

#### debug

- 默认值：false
- 类型：Boolean

 
从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log_level的级别。
 
 

#### 示例

**转换远程npm三方库中的包**
 
转换npm三方库中的axios包，执行以下命令：
 
```text
ohpm convert axios --registry https://registry.npmjs.org/
```
 
结果示例：
 
```text
PS C:\Users\xxxxx\Desktop> ohpm convert axios --registry https://registry.npmjs.org
...
ohpm INFO: > start convert package: asynckit@0.4.0
ohpm INFO: > start convert package: axios@1.6.8
ohpm INFO: > start convert package: combined-stream@1.0.8
...
ohpm INFO: A total of 9 packets are converted successfully.
ohpm INFO: Converted packages are saved to the "C:\Users\xxxxx\Desktop\convert_1712127991590" directory.
```
 

![](assets/ohpm%20convert/file-20260514134427148-2.png)

 

 
**转换本地node_modules目录中的包**
 
执行npm install uuid后，转换本地node_modules目录中的包，执行以下命令：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/eeTzVUOyRuK1sg9Pe0AUsg/zh-cn_image_0000002594475138.png?HW-CC-KV=V1&HW-CC-Date=20260723T012116Z&HW-CC-Expire=86400&HW-CC-Sign=6C991EA0947B8FE870D47A68809ECAEBDDC229EFF823DF7789693772D5C1BFBA)

 
```text
ohpm convert C:\Users\xxxxx\Desktop\uuidInstallDir\node_modules
```
 
结果示例：
 
```text
PS C:\Users\xxxxx\Desktop> ohpm convert C:\Users\xxxxx\Desktop\uuidInstallDir\node_modules
ohpm INFO: > start convert package: uuid
...
ohpm INFO: A total of 1 package(s) are converted successfully.
ohpm INFO: Converted packages are saved to the "C:\Users\xxxxx\Desktop\convert_1712128912583" directory.
```
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/vKcC_o6jThii3UKgTBnMMA/zh-cn_image_0000002594635060.png?HW-CC-KV=V1&HW-CC-Date=20260723T012116Z&HW-CC-Expire=86400&HW-CC-Sign=14526A8F827EDC182D7036C98E25E204FF9F28AEF0FBE9CEFC2FA139B7D24B5A)
