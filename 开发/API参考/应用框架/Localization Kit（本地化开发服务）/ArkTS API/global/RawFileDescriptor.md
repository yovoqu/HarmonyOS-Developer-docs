# RawFileDescriptor

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rawfiledescriptor
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

本模块提供rawfile文件所在hap的descriptor信息。
 
> [!NOTE]
> 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

#### 导入模块

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

```text
import { resourceManager } from '@kit.LocalizationKit'
```
 
  

#### RawFileDescriptor

**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Global.ResourceManager
  
| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fd | number | 否 | 否 | 文件描述符。 |
| offset | number | 否 | 否 | 起始偏移量。 |
| length | number | 否 | 否 | 文件长度。 |
