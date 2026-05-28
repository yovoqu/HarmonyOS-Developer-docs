# ohpm-repo import_userinfo

更新时间：2026-01-15 06:51:04

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-import-userinfo

导入用户DB数据。
 

#### 前提条件

已成功执行[export_userinfo 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-userinfo)。
 
 

#### 命令格式

```text
ohpm-repo import_userinfo <zip_file> [options]
```
 
 

#### 功能描述

根据提供的zip文件导入用户DB数据到ohpm-repo。
 
 

#### 参数

 

#### &lt;zip_file&gt;

- 类型： String
- 必填参数

 
必须在import_userinfo命令后面配置&lt;zip_file&gt;参数，指定执行[export_userinfo 命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-export-userinfo)导出的zip文件。
 
 

#### 选项

 

#### clean-db

- 默认值：false
- 类型：Boolean

 
可以在import_userinfo命令后面配置--clean-db参数，指定在导入数据前先清空DB数据。
 
 

#### 示例

执行以下命令：
 
```text
ohpm-repo import_userinfo <zip_file> --clean-db
```
 
结果示例：
 
```json
PS D:\> ohpm-repo import_userinfo D:\export_userInfo_1754738056722.zip --clean-db
[2025-08-09T19:19:31.623] [INFO] default - verifying the validity of the meta crypto component.
[2025-08-09T19:19:31.633] [INFO] default - the meta crypto component is verified successfully.
[2025-08-09T19:19:31.639] [INFO] default - initialize "file database" successfully.
[2025-08-09T19:19:31.660] [INFO] default - all database data has been cleaned.
[2025-08-09T19:19:31.660] [INFO] default - importing data in the 'user.json' file.
...
[2025-08-09T19:19:31.673] [INFO] default - importing data in the 'system_security.json' file.
[2025-08-09T19:19:31.674] [INFO] default - data import finished.
```
