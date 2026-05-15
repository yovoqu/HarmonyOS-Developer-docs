# fileUri

更新时间：2026-03-19 08:47:51

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileuri
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


## 概述
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV

文件统一资源标识符（File Uniform Resource Identifier）。

支持fileuri与路径path的转换，和fileuri的有效性校验。

该类主要用于 URI 格式验证和 URI 转换处理。且uri用于应用间文件分享场景，将应用沙箱路径按照固定关系转换为URI;

调用者需保证所有接口入参的有效性，接口按照固定规则转换输出结果，并不检查其是否存在。

**系统能力：** SystemCapability.FileManagement.AppFileService

**起始版本：** 12


## 文件汇总
**支持设备：** Phone / PC/2in1 / Tablet / Wearable / TV


| 名称 | 描述 |
| --- | --- |
| [oh_file_uri.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-file-uri-h) | 提供uri和路径path之间的相互转换，目录uri获取，以及uri的有效性校验的方法。 |
