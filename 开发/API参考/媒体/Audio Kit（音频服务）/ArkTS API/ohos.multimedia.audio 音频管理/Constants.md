# Constants

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-c
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  
| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| DEFAULT_VOLUME_GROUP_ID9+ | number | 是 | 默认音量组id。 系统能力： SystemCapability.Multimedia.Audio.Volume |
| DEFAULT_INTERRUPT_GROUP_ID9+ | number | 是 | 默认音频中断组id。 系统能力： SystemCapability.Multimedia.Audio.Interrupt |
 
 
**示例：**
 
```text
import { audio } from '@kit.AudioKit';

const defaultVolumeGroupId = audio.DEFAULT_VOLUME_GROUP_ID;
const defaultInterruptGroupId = audio.DEFAULT_INTERRUPT_GROUP_ID;
```
