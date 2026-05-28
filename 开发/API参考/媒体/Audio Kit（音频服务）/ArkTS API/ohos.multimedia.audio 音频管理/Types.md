# Types

更新时间：2026-03-09 02:50:43

来源：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t
**支持设备：** Phone | PC/2in1 | Tablet | Wearable | TV

> [!NOTE]
> 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

  

##### AudioRendererChangeInfoArray9+

type AudioRendererChangeInfoArray = Array<Readonly&lt;AudioRendererChangeInfo&gt;>
 
数组类型，AudioRendererChangeInfo数组，只读。
 
**系统能力：** SystemCapability.Multimedia.Audio.Renderer
  
| 类型 | 说明 |
| --- | --- |
| Array<Readonly&lt;AudioRendererChangeInfo&gt;> | 数组类型，AudioRendererChangeInfo数组，只读。 |
 
 
  

##### AudioCapturerChangeInfoArray9+

type AudioCapturerChangeInfoArray = Array<Readonly&lt;AudioCapturerChangeInfo&gt;>
 
数组类型，AudioCapturerChangeInfo数组，只读。
 
**系统能力：** SystemCapability.Multimedia.Audio.Capturer
  
| 类型 | 说明 |
| --- | --- |
| Array<Readonly&lt;AudioCapturerChangeInfo&gt;> | 数组类型，AudioCapturerChangeInfo数组，只读。 |
 
 
  

##### AudioEffectInfoArray10+

type AudioEffectInfoArray = Array<Readonly&lt;AudioEffectMode&gt;>
 
待查询ContentType和StreamUsage组合场景下的音效模式数组类型，[AudioEffectMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioeffectmode10)数组，只读。
 
**系统能力：** SystemCapability.Multimedia.Audio.Renderer
  
| 类型 | 说明 |
| --- | --- |
| Array<Readonly&lt;AudioEffectMode&gt;> | 待查询ContentType和StreamUsage组合场景下的音效模式数组类型，AudioEffectMode数组，只读。 |
 
 
  

##### AudioDeviceDescriptors

type AudioDeviceDescriptors = Array<Readonly&lt;AudioDeviceDescriptor&gt;>
 
设备属性数组类型，为[AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiodevicedescriptor)的数组，只读。
 
**元服务API：** 从API version 12开始，该接口支持在元服务中使用。
 
**系统能力：** SystemCapability.Multimedia.Audio.Device
  
| 类型 | 说明 |
| --- | --- |
| Array<Readonly&lt;AudioDeviceDescriptor&gt;> | 设备属性数组类型，为AudioDeviceDescriptor的数组，只读。 |
 
 
  

##### AudioRendererWriteDataCallback12+

type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult | void
 
回调函数类型，用于音频渲染器的数据写入，回调函数结束后，音频服务会把data指向的数据放入队列里等待播放，因此请勿在回调外再次更改data指向的数据, 且务必保证往data填满待播放数据, 否则会导致音频服务播放杂音。
 
**系统能力：** SystemCapability.Multimedia.Audio.Renderer
 
**参数：**
  
| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | ArrayBuffer | 是 | 待写入缓冲区的数据。 |
 
 
**返回值：**
  
| 类型 | 说明 |
| --- | --- |
| AudioDataCallbackResult \| void | 如果返回 void 或 AudioDataCallbackResult.VALID：表示数据有效，将播放音频数据；如果返回 AudioDataCallbackResult.INVALID：表示数据无效，且音频数据不播放。 |
