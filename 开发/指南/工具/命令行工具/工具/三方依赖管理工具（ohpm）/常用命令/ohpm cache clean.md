# ohpm cache clean

更新时间：2026-06-17 07:24:31

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-cache

清理 ohpm 缓存文件夹。
 

#### 命令格式

```text
ohpm cache clean  [<@group>/]<pkg> [options]
```
 
 
> [!NOTE]
> @group：三方库的命名空间，可选。ohpm 26.0.0.410版本新增。 pkg：三方库名称，必选。ohpm 26.0.0.410版本新增。

 

#### 功能描述

用于清理 ohpm 缓存文件夹。
 
 

#### Options

 

#### log_level

- 默认值：无
- 类型：String

 
从ohpm 6.0.2.636版本开始，可以在命令后配置--log_level &lt;string&gt;参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log_level的级别。
 
 

#### debug

- 默认值：false
- 类型：Boolean

 
从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log_level的级别。
 
 

#### --v

- 默认值：all
- 类型：String

 
从ohpm 26.0.0.410版本开始，可以在ohpm cache clean [<@group>/]&lt;pkg&gt; 命令后配置--v &lt;string&gt;参数，用于清除包下指定版本的元数据缓存文件。若未配置--v，则清除指定包全部的元数据缓存文件；若未设置具体版本，则清除指定包的all.json元数据缓存文件。
 
 

#### 示例

**示例1**
 
清理 ohpm 缓存文件夹，可执行以下命令：
 
```text
ohpm cache clean
```
 
结果示例：
 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/jB9NkmXXQv2Vnpkov3mRqA/zh-cn_image_0000002594634942.png?HW-CC-KV=V1&HW-CC-Date=20260624T020705Z&HW-CC-Expire=86400&HW-CC-Sign=E49556BBFB60D920747AB49B074D75B9BEB654A3980079F83608786942AC1E93)

 
**示例2**
 
清除包下的指定版本元数据文件，可执行以下命令：
 
```json
ohpm cache clean  // 清除 ~/.ohpm/cache 目录下系统创建的缓存目录和工程目录中.ohpm/lock/oh-install-meta.json5文件
ohpm cache clean @group/package // 清除指定包全部的元数据缓存文件
ohpm cache clean @group/package --v // 清除指定包的all.json元数据缓存文件
ohpm cache clean @group/package --v 2.0.0 // 清除指定包的2.0.0.json的元数据缓存文件
```
 
 

#### 关于缓存设计的说明

ohpm 将缓存数据存储在配置的 cache 目录下名为 content-v1 的文件夹中，存储所有通过 http 请求获取的 HAR 包数据。包的路径使用包的 sha512 哈希值分割成 3 段，第 1、2 位作为第一级目录，哈希值第 3、4 位作为第二级目录，哈希值第 5 位到结尾的所有字符作为文件名。使用哈希值可以将文件较均匀地分布在各个目录下，分成 3 层目录结构避免一个目录下文件数量过多，可以提升文件索引效率。
 
从ohpm 26.0.0.410版本开始新增元数据文件缓存，在cache 目录下名为 metadata 的文件夹中，将所有通过Http请求获取的元数据按group名称和包名分割目录存储到本地文件中，分为固定版本的元数据文件(x.x.x.json)和全量元数据文件(all.json)。
